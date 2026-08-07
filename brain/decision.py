def decide(user):

    user = user.lower()

    if any(x in user for x in [
        "open",
        "create",
        "delete",
        "folder",
        "youtube",
        "weather",
        "news"
    ]):
        return "plugin"

    if any(x in user for x in [
        "who",
        "what",
        "why",
        "python",
        "bitcoin",
        "history",
        "science"
    ]):
        return "knowledge"

    return "ai"