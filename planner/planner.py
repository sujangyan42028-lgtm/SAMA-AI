def plan(user):

    user = user.lower()

    steps = []

    if "search" in user or "find" in user:
        steps.append("internet")

    if "youtube" in user:
        steps.append("youtube")

    if "translate" in user:
        steps.append("translator")

    if "weather" in user:
        steps.append("weather")

    if "news" in user:
        steps.append("news")

    return steps