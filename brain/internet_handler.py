from internet.search import search_web


def handle(user):

    latest_keywords = [
        "today",
        "latest",
        "news",
        "weather",
        "current",
        "live",
        "price",
        "update",
        "breaking"
    ]

    if any(word in user.lower() for word in latest_keywords):

        result = search_web(user)

        if result:
            return result

    return None