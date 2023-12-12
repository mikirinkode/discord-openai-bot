# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os
from clients.openai_client import OpenAIClient

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
openai_key = os.environ.get('OPENAI_API_KEY')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if not self.user.mentioned_in(message): return

        # If the message is already in a thread, send the message to the thread else create new thread first
        if not isinstance(message.channel, discord.Thread):
            thread = await message.create_thread(name='Chatting with your Personal AI')
        else:
            thread = message.channel

        # add is typing effect
        await thread.typing()

        client = OpenAIClient(openai_key)
        reply = client.complete([
            {"role": "system", "content": "Kamu adalah AI Assistant. Balas dengan bahasa casual jaksel"},
            {"role": "user", "content": message.content}
        ])

        await thread.send(reply)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
