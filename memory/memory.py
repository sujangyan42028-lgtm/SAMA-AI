import json
import os

FILE = "memory/memory.json"


def load():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def remember(key, value):

    data = load()

    data[key] = value

    save(data)


def recall(key):

    data = load()

    return data.get(key)


def forget(key):

    data = load()

    if key in data:
        del data[key]
        save(data)


def clear_memory():

    save({})