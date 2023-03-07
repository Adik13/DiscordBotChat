from dotenv import load_dotenv
import os
import discord
from app.chatgpt_ai.connect_openai import chatgpt_response
from .command_parser import parse_command

chat_history = {}
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')


async def on_message(message):
    global chat_history
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    else:
        command = parse_command(message)
        prompt = message.content
        if message.channel.id not in chat_history:
            chat_history[message.channel.id] = []
        response = chatgpt_response(prompt, chat_history[message.channel.id], **command)
        chat_history[message.channel.id].append(response)
        await message.channel.send(response)


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = None
        self.content = None
        self.author = None
        self.message_history = []

    async def on_ready(self):
        print('Logged in as:', self.user)


intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)
client.run(discord_token)


def run():
    return None
