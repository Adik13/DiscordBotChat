from dotenv import load_dotenv
import os
import discord
from app.chatgpt_ai.connect_openai import chatgpt_response

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_history = []

    async def on_ready(self):
        print('Logged in as:', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        self.message_history.append(message.content)
        if len(self.message_history) > 5:
            self.message_history.pop(0)

        response = chatgpt_response(message.content, self.message_history)
        await message.channel.send(f"You said: {message.content}\n{response}")

intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)

client.run(discord_token)
