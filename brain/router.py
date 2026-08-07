from brain.app_handler import handle as app_handle
from brain.internet_handler import handle as internet_handle
from brain.ai_handler import handle as ai_handle


def execute(intent, user):

    user = user.strip()

    # -------------------------
    # APP / FILE / CALCULATOR
    # -------------------------

    if intent in ["app", "file", "calculator"]:

        result = app_handle(user)

        if result:
            return result

    # -------------------------
    # INTERNET
    # -------------------------

    elif intent == "internet":

        result = internet_handle(user)

        if result:
            return result

    # -------------------------
    # AI
    # -------------------------

    elif intent == "ai":

        return ai_handle(user)

    # -------------------------
    # UNKNOWN
    # -------------------------

    return ai_handle(user)