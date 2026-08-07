def detect_intent(user):

    user = user.lower().strip()

    # -------------------------
    # FILE / FOLDER
    # -------------------------

    if any(x in user for x in [

        "create",
        "make",
        "delete",
        "remove",
        "folder",
        "file",

        "banao",
        "bana",
        "delete karo",
        "folder banao",
        "folder hatao"

    ]):
        return "file"

    # -------------------------
    # APP
    # -------------------------

    if any(x in user for x in [

        "open",
        "launch",
        "start",
        "run",

        "khol",
        "khol do",
        "open karo"

    ]):
        return "app"

    # -------------------------
    # CALCULATOR
    # -------------------------

    if any(x in user for x in [

        "calculate",
        "+",
        "-",
        "*",
        "/",
        "plus",
        "minus",
        "multiply",
        "divide"

    ]):
        return "calculator"

    # -------------------------
    # INTERNET
    # -------------------------

    if any(x in user for x in [

        "search",
        "google",
        "find",
        "look up",
        "lookup",

        "news",
        "latest",
        "today",
        "current",
        "live",
        "update",
        "breaking",

        "weather",
        "temperature",
        "forecast",

        "price",
        "bitcoin",
        "ethereum",
        "crypto",
        "gold",
        "silver",
        "stock",
        "share",
        "market",

        "ipl",
        "cricket",
        "match",
        "score",

        "aaj",
        "abhi",

        "search karo",
        "google karo"

    ]):
        return "internet"

    # -------------------------
    # AI
    # -------------------------

    return "ai"