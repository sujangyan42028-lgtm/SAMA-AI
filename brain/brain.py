import ollama
from memory.memory import save_memory, get_memory
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
        else:
            return "I don't know your name yet."

    # AI
    try:
        response = ollama.chat(
            model="qwen2.5:1.5b",
            messages=[
                {
                    "role": "user",
                    "content": user
                }
            ]
        )

        return response["message"]["content"]

    # Internet Backup
    except Exception:
        result = search_web(user)

        if result:
            return result

        return "Sorry, I couldn't find an answer."