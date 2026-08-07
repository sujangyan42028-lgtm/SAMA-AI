from internet.search import search_web
from ai.chat import chat_stream


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
        "breaking",
        "bitcoin",
        "ethereum",
        "gold",
        "stock",
        "ipl",
        "match",
        "score"
    ]

    if any(word in user.lower() for word in latest_keywords):

        try:

            result = search_web(user)

            if result:

                prompt = f"""
You are SAMA.

Using the search results below, answer the user's question naturally in Hinglish.

User Question:
{user}

Search Results:
{result}

Give only the final answer.
"""

                return chat_stream(prompt)

        except Exception as e:

            print(f"[INTERNET ERROR] {e}")

    return None