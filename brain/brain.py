from memory.memory import save_memory, get_memory
from ai.chat import chat_stream
from internet.search import search_web
from skills.browser import open_website
from skills.google import google_search
from skills.opener import open_app
from skills.calculator import calculate

def think(user):

    user = user.lower()

    # Debug
    print("You said:", user)

    # Memory
    if "my name is" in user:
        name = user.replace("my name is", "").strip()
        save_memory("name", name)
        return f"Nice to meet you {name}."

    elif "what is my name" in user:
        name = get_memory("name")

        if name:
            return f"Your name is {name}."
        return "I don't know your name yet."

    # Google Search
    google = google_search(user)
    if google:
        return google

    # Browser
    website = open_website(user)
    if website:
        return website

    # Open App
    app = open_app(user)
    if app:
        return app

    # Calculator
    calc = calculate(user)
    if calc:
        return calc

    # Internet
    latest_keywords = [
        "today",
        "latest",
        "news",
        "weather",
        "current",
        "live"
    ]

    if any(word in user for word in latest_keywords):
        result = search_web(user)
        if result:
            return result

    # AI
    return chat_stream(user)