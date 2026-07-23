from memory.memory import save_memory, get_memory
from ai.chat import chat
from internet.search import search_web

def think(user):

    user = user.lower()

    # Memory
    if "my name is" in user:
        name = user.replace("my name is", "").strip()
        save_memory("name", name)
        return f"Nice to meet you {name}."

    elif "what is my name" in user:
        name = get_memory("name")

        if name:
            return f"Your name is {name}."
        return "I don't know your name yet."

    # Internet for latest information
    latest_keywords = [
        "today",
        "latest",
        "news",
        "weather",
        "current",
        "live"
    ]

    if any(word in user for word in latest_keywords):
        result = search_web(user)
        if result:
            return result

    # AI
    return chat(user)