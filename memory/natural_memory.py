from memory.memory import remember

IMPORTANT_PATTERNS = [
    "i like",
    "i love",
    "i prefer",
    "my goal is",
    "my dream is",
    "my favourite",
    "my favorite",
    "i live in",
    "my name is",
    "i am",
    "i work as",
    "i study",
]

def learn(text):

    text = text.lower().strip()

    for pattern in IMPORTANT_PATTERNS:

        # Sirf statement save kare, question nahi
        if text.startswith(pattern):

            value = text[len(pattern):].strip()

            if value:
                key = pattern.replace(" ", "_")
                remember(key, value)

            return True

    return False