from skills.calculator import calculate


def calculator_plugin(user):

    result = calculate(user)

    if result:
        return result

    return None