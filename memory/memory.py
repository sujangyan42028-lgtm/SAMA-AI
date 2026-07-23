import json
import os

FILE = "memory.json"

def save_memory(key, value):
    data = {}

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data[key] = value

    with open(FILE, "w") as f:
        json.dump(data, f)

def get_memory(key):
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
            return data.get(key)

    return None