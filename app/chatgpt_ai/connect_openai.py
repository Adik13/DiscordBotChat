from dotenv import load_dotenv
import openai
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')
openai.api_key='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'

def chatgpt_response(prompt, message_history=None):
    if message_history:
        prompt = f"{message_history}{prompt}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,  # Добавить параметр stop
        temperature=0.7,
    )
    message = response.choices[0].text
    return message.strip()
