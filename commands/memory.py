from memory.memory import save_memory, get_memory

def remember_name(name):
    save_memory("name", name)
    return f"Nice to meet you {name}"

def tell_name():
    name = get_memory("name")

    if name:
        return f"Your name is {name}"

    return "I don't know your name yet."