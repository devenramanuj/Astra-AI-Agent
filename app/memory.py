memory = []

def remember(user, assistant):
    memory.append({
        "user": user,
        "assistant": assistant
    })

def get_memory():
    return memory
