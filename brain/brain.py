from brain.fast_reply import reply
from brain.emotion_handler import handle as emotion_handle
from brain.memory_handler import handle as memory_handle
from brain.app_handler import handle as app_handle
from brain.internet_handler import handle as internet_handle
from brain.ai_handler import handle as ai_handle
from brain.planner import plan
def split_tasks(user):

    user = user.lower()

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

    tasks = [t.strip() for t in tasks if t.strip()]

    return tasks

def think(user):

    user = user.lower().strip()

    print("You said:", user)
    tasks = split_tasks(user)

    if len(tasks) > 1:

        answers = []

        for task in tasks:

            result = app_handle(task)

            if result:
                answers.append(result)
                continue

            result = internet_handle(task)

            if result:
                answers.append(result)
                continue

            result = ai_handle(task)

            answers.append(result)

        return "\n".join(answers)
    # Fast Replies
    result = reply(user)
    if result:
        return result

    # Emotion
    result = emotion_handle(user)
    if result:
        return result

    # Memory
    result = memory_handle(user)
    if result:
        return result
    result = app_handle(user)
    if result:
        return result
    # AI Planner
    task = plan(user)

    if task["type"] == "app":
        result = app_handle(user)
        if result:
            return result

    elif task["type"] == "internet":
        result = internet_handle(user)
        if result:
            return result

    elif task["type"] == "calculator":
        result = app_handle(user)
        if result:
            return result

    elif task["type"] == "multi":
        result = app_handle(user)
        if result:
            return result

        result = internet_handle(user)
        if result:
            return result

    # AI
    return ai_handle(user)