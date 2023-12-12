import os
import openai

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def complete(self, messages) -> str:
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=messages,
        )
        return completion.choices[0].message.content