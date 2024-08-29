from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('OPENAI_API_KEY')

def get_gpt_response(message):
    client = OpenAI(api_key=api)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"{message}"
            }
        ]
    )

    return completion.choices[0].message.content
