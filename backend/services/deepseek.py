import httpx
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key="sk-591d577127ee419981f66972d1cb0590", base_url="https://api.deepseek.com")


def query_deepseek(user_message: str, context: str, intent: str):
    prompt = f"""
    You are a helpful assistant on the PartSelect website. You only answer questions about refrigerator and dishwasher parts. You provide accurate, clear information based on documentation provided.
    Task: Based on intent '{intent}', respond with clear, specific help.
    """

    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_message},
    ],
    max_tokens=248,
    temperature=1.25,
    stream=False
)

    return response.choices[0].message.content