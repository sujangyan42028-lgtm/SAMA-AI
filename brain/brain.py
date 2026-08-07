from brain.fast_reply import reply
from brain.emotion_handler import handle as emotion_handle
from brain.memory_handler import handle as memory_handle
from brain.intent import detect_intent
from brain.router import execute
from brain.nlp import normalize
from brain.knowledge import ask
from brain.plugin_router import plugin_router


def split_tasks(user):

    user = normalize(user)

    separators = [
        " and ",
        " then ",
        ",",
        " after that "
    ]

    tasks = [user]

    for sep in separators:

        new_tasks = []

        for task in tasks:
            new_tasks.extend(task.split(sep))

        tasks = new_tasks

    return [t.strip() for t in tasks if t.strip()]


def think(user):

    original_user = user.strip()

    print("You said:", original_user)

    # -------------------------
    # FAST REPLY
    # -------------------------

    result = reply(original_user.lower())

    if result:
        return result

    # -------------------------
    # EMOTION
    # -------------------------

    result = emotion_handle(original_user)

    if result:
        return result

    # -------------------------
    # MEMORY
    # -------------------------

    result = memory_handle(original_user)

    if result:
        return result

    # -------------------------
    # PLUGINS (FIRST)
    # -------------------------

    result = plugin_router(original_user)

    if result:
        return result

    # -------------------------
    # KNOWLEDGE
    # -------------------------

    result = ask(original_user)

    if result:
        return result

    # -------------------------
    # MULTI TASK
    # -------------------------

    tasks = split_tasks(original_user)

    if len(tasks) > 1:

        answers = []

        for task in tasks:

            intent = detect_intent(task)

            if intent != "ai":
                task = normalize(task)

            result = execute(intent, task)

            if result:
                answers.append(result)

        return "\n".join(answers)

    # -------------------------
    # SINGLE INTENT
    # -------------------------

    intent = detect_intent(original_user)

    if intent != "ai":
        original_user = normalize(original_user)

    return execute(intent, original_user)