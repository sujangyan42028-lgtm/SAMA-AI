import re

REPLACEMENTS = {
    # Sirf commands ke liye common spelling fixes
    "kese": "kaise",
    "open chrome": "open chrome",
    "open youtube": "open youtube",
}


def normalize(text):

    text = text.lower().strip()

    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)

    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    return text


def extract_folder(command):

    command = command.lower()

    words = [
        "create",
        "make",
        "new",
        "folder",
        "the",
        "a",
        "banao",
        "bana"
    ]

    for w in words:
        command = command.replace(w, "")

    return command.strip()


def extract_delete_folder(command):

    command = command.lower()

    words = [
        "delete",
        "remove",
        "folder",
        "the",
        "a",
        "hatao",
        "delete karo"
    ]

    for w in words:
        command = command.replace(w, "")

    return command.strip()