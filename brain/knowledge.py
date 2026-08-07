import json
import os

KNOWLEDGE_PATH = "knowledge"
DEFAULT_FILE = os.path.join(KNOWLEDGE_PATH, "general.json")


def ask(question):

    question = question.lower().strip()

    if not os.path.exists(KNOWLEDGE_PATH):
        os.makedirs(KNOWLEDGE_PATH)

    if not os.path.exists(DEFAULT_FILE):
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)

    for file in os.listdir(KNOWLEDGE_PATH):

        if not file.endswith(".json"):
            continue

        path = os.path.join(KNOWLEDGE_PATH, file)

        try:

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

        except Exception:
            continue

        for key, value in data.items():

            if key.lower() in question:
                return value

    return None


def learn(question, answer):

    question = question.lower().strip()

    if not os.path.exists(KNOWLEDGE_PATH):
        os.makedirs(KNOWLEDGE_PATH)

    if not os.path.exists(DEFAULT_FILE):

        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4, ensure_ascii=False)

    try:

        with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    except Exception:

        data = {}

    if question not in data:
        data[question] = answer

    with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)