from brain.brain import think


def get_response(user):

    answer = think(user)

    if not answer:
        return "Sorry, I couldn't understand."

    return answer