from app.discord_bot.connect_discord import client, discord_token
from app.chatgpt_ai.connect_openai import openai

openai.api_key='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'


if __name__ == '__main__':
    client.run(discord_token)
