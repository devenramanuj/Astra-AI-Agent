from gemini_client import ask_gemini
from business_data import BUSINESS_DATA
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

    text = ask_gemini(prompt)

    remember(message, text)

    return text


if __name__ == "__main__":

    print("Astra AI Agent Started")

    user_message = input("User: ")

    answer = astra_chat(user_message)

    print("\nAstra:")
    print(answer)

    print("\nMemory:")
    print(get_memory())
