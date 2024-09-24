# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the YogaGPT project.


import os

import discord
import openai
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

discord_bot_token = os.getenv("DISCORD_YOGAGPT_SECRET")
openai_api_key = os.getenv("OPENAI_API_KEY")


class YogaGPT(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # don't respond to ourselves
        if message.author == self.user:
            return

        response = await self.call_chat_gpt(message.content)
        await message.channel.send(response)

    async def call_chat_gpt(self, message):
        client = OpenAI(api_key=openai_api_key)

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-instruct",
                messages=[{
                    "role": "user",
                    "content": message
                }],
                temperature=1,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                response_format={"type": "text"})
            return response["choices"][0]["message"]["content"]
        except openai.RateLimitError as e:
            # Handle the rate limit error
            print(e)
            return "Sorry, the bot has reached its API usage limit. Please try again later."

        except Exception as e:
            # Handle other errors
            return f"An error occurred: {str(e)}"


def run_yoga_gpt():
    intents = discord.Intents.default()
    intents.message_content = True
    client = YogaGPT(intents=intents)
    client.run(discord_bot_token)
