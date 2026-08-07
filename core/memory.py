import json
import os
import threading


MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "sama_memory.json"
)

_lock = threading.Lock()


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

    except (json.JSONDecodeError, OSError):
        pass

    return {}


def save_memory(memory):

    with _lock:
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as file:
                json.dump(
                    memory,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        except OSError as error:
            print("Memory save error:", error)


def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)


def recall(key):

    memory = load_memory()

    return memory.get(key)


def forget(key):

    memory = load_memory()

    if key in memory:
        del memory[key]
        save_memory(memory)
        return True

    return False


def get_all_memory():

    return load_memory()