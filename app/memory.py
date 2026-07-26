memory = []


def remember(user: str, assistant: str):
    memory.append({
        "user": user,
        "assistant": assistant
    })


def get_memory():
    return memory
