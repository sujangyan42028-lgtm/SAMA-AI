from memory.memory import remember, recall
from memory.natural_memory import learn
from memory.personality import learn_personality, personality_reply


def handle(user):

    user = user.lower().strip()

    # Learn personality
    learn_personality(user)

    # Learn natural memory
    learn(user)

    # Personality replies
    reply = personality_reply(user)
    if reply:
        return reply

    # ==========================
    # NATURAL MEMORY
    # ==========================

    if "what do i love" in user:

        value = recall("i_love")

        if value:
            return f"You love {value}."

        return "You haven't told me what you love."

    elif "what do i prefer" in user:

        value = recall("i_prefer")

        if value:
            return f"You prefer {value}."

        return "You haven't told me what you prefer."

    elif "what is my dream" in user:

        value = recall("my_dream_is")

        if value:
            return f"Your dream is {value}."

        return "You haven't told me your dream."

    # ==========================
    # NAME MEMORY
    # ==========================

    elif "my name is" in user:

        name = user.replace("my name is", "").strip()

        remember("name", name)

        return f"Nice to meet you {name}."

    elif "what is my name" in user:

        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."

    # ==========================
    # GOAL MEMORY
    # ==========================

    elif "my goal is" in user:

        goal = user.replace("my goal is", "").strip()

        remember("goal", goal)

        return "I will remember your goal."

    elif "what is my goal" in user:

        goal = recall("goal")

        if goal:
            return f"Your goal is {goal}."

        return "You haven't told me your goal."

    return None