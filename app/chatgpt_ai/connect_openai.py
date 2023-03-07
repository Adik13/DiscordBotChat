from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def chatgpt_response(prompt,
                     message_history=[],
                     model_engine="text-davinci-003",
                     temperature=0.7,
                     max_tokens=150,
                     top_p=1):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        n=1,
        stream=False,
        user=message_history,
    )
    message_history.append(response.choices[0].text)
    return response.choices[0].text.strip()
