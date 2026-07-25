import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-2.5-flash"


def ask_gemini(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text

def ask_gemini_with_tools(prompt, tools):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "tools": tools
        }
    )

    return response
