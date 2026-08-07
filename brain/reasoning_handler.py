from reasoning.reasoner import reason


def handle(user):

    plan = reason(user)

    return plan