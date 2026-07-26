from memory.memory import remember, recall

TRAITS = [
    "happy",
    "sad",
    "angry",
    "excited",
    "tired",
    "motivated",
    "confused",
    "busy",
    "free"
]


def learn_personality(text):

    text = text.lower()

    for trait in TRAITS:

        if f"i am {trait}" in text:
            remember("mood", trait)
            return True

    if "i like" in text:
        remember("interest", text.replace("i like", "").strip())
        return True

    return False


def personality_reply(user):

    user = user.lower()

    if "how am i" in user:

        mood = recall("mood")

        if mood:
            return f"You seem to be feeling happy {mood}."

        return None

    if "what do i like" in user:

        interest = recall("interest")

        if interest:
            return f"You like {interest}."

        return None

    return None