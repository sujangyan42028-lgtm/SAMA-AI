from memory.memory import save_memory, get_memory

def think(user):

    user = user.lower()

    if "my name is" in user:
        name = user.replace("my name is", "").strip()
        save_memory("name", name)
        return f"Nice to meet you {name}."

    elif "what is my name" in user:
        name = get_memory("name")

        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet."

    return "I don't understand."