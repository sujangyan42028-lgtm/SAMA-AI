def reason(user):

    user = user.lower()

    plan = {
        "needs_search": False,
        "needs_compare": False,
        "needs_calculation": False,
        "needs_summary": False
    }

    search_words = [
        "best",
        "latest",
        "top",
        "compare",
        "vs",
        "review",
        "price",
        "buy"
    ]

    calc_words = [
        "calculate",
        "+",
        "-",
        "*",
        "/"
    ]

    summary_words = [
        "summary",
        "summarize",
        "explain"
    ]

    if any(word in user for word in search_words):
        plan["needs_search"] = True

    if "compare" in user or "vs" in user:
        plan["needs_compare"] = True

    if any(word in user for word in calc_words):
        plan["needs_calculation"] = True

    if any(word in user for word in summary_words):
        plan["needs_summary"] = True

    return plan