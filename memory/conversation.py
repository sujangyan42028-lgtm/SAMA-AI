import json
import os

FILE = "memory/conversation.json"


def load_chat():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_chat(chat):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(chat, f, indent=4)


def remember(user, assistant):

    chat = load_chat()

    chat.append({
        "user": user,
        "assistant": assistant
    })

    chat = chat[-20:]

    save_chat(chat)


def recall():

    return load_chat()