from gemini_client import ask_gemini_with_tools
from business_data import BUSINESS_DATA
from tools import create_order, ORDER_TOOL
from memory import remember, get_memory


def astra_chat(message):
    prompt = f"""
તમે Astra AI Employee છો.

Business Information:
{BUSINESS_DATA}

User:
{message}

જવાબ વ્યવસાયિક રીતે આપો.
"""

    response = ask_gemini_with_tools(
    prompt,
    [ORDER_TOOL]
)

text = response.text

remember(message, text)

return text


if __name__ == "__main__":

    print("Astra AI Agent Started")

    user_message = "મને 2 લિટર તેલ જોઈએ છે"

    answer = astra_chat(user_message)

    print("\nAstra:")
    print(answer)

    print("\nMemory:")
    print(get_memory())
