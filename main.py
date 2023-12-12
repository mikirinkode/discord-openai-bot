# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # Reply to the message, if the message is ping, reply with pong
        if message.content == 'ping':
            # await message.channel.send('pong')
            # If the message is already in a thread, send the message to the thread else create new thread first
            if not isinstance(message.channel, discord.Thread):
                thread = await message.create_thread(name='thread name')
            else:
                thread = message.channel
            # add is typing effect
            await thread.typing():
            await thread.send('pong')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
