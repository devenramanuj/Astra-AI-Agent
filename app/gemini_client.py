import os

from google import genai
from google.genai import types
from dotenv import load_dotenv

from tools import create_order

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
        config=types.GenerateContentConfig(
            tools=tools
        )
    )

    # Gemini એ function call કર્યો છે?
    if (
        response.candidates
        and response.candidates[0].content.parts
        and hasattr(response.candidates[0].content.parts[0], "function_call")
        and response.candidates[0].content.parts[0].function_call
    ):

        fc = response.candidates[0].content.parts[0].function_call

        if fc.name == "create_order":

            order = create_order(
                product=fc.args["product"],
                quantity=fc.args["quantity"],
                price=fc.args["price"]
            )

            followup = client.models.generate_content(
                model=MODEL,
                contents=[
                    prompt,
                    types.Part.from_function_response(
                        name="create_order",
                        response=order
                    )
                ]
            )

            return followup

    return response
