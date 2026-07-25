import json
import os

FILE = "memory/long_memory.json"


def load_memory():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def remember(key, value):

    data = load_memory()

    data[key] = value

    save_memory(data)


def recall(key):

    data = load_memory()

    return data.get(key)