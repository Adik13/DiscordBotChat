from app.discord_bot.connect_discord import client, discord_token
from app.chatgpt_ai.connect_openai import openai


if __name__ == '__main__':
    client.run(discord_token)
