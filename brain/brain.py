from memory.memory import save_memory, get_memory
from memory.long_memory import remember, recall

from ai.chat import chat_stream

from internet.search import search_web

from skills.browser import open_website
from skills.google import google_search
from skills.opener import open_app
from skills.calculator import calculate

from plugins.manager import run_plugins


def think(user):

    user = user.lower().strip()

    print("You said:", user)

    # ==========================
    # FAST REPLIES
    # ==========================

    if user in ["hello", "hi", "hey"]:
        return "Hello Sahil."

    elif user in ["what is your name", "who are you"]:
        return "My name is SAMA."

    elif "who created you" in user or user == "created":
        return "I was created by Sahil Khan."

    elif user in ["how are you", "how are you doing"]:
        return "I am doing great. Thank you for asking."

    elif user == "good morning":
        return "Good morning Sahil."

    elif user == "good night":
        return "Good night Sahil."

    elif user in ["thank you", "thanks"]:
        return "You are welcome."

    # ==========================
    # MEMORY
    # ==========================

    if "my name is" in user:

        name = user.replace("my name is", "").strip()

        save_memory("name", name)

        return f"Nice to meet you {name}."

    elif "what is my name" in user:

        name = get_memory("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."

    # ==========================
    # LONG MEMORY
    # ==========================

    if "my favourite coin is" in user:

        coin = user.replace("my favourite coin is", "").strip()

        remember("favorite_coin", coin)

        return f"I will remember that your favourite coin is {coin}."

    elif "what is my favourite coin" in user:

        coin = recall("favorite_coin")

        if coin:
            return f"Your favourite coin is {coin}."

        return "You haven't told me your favourite coin yet."

    elif "my goal is" in user:

        goal = user.replace("my goal is", "").strip()

        remember("goal", goal)

        return "I will remember your goal."

    elif "what is my goal" in user:

        goal = recall("goal")

        if goal:
            return f"Your goal is {goal}."

        return "You haven't told me your goal yet."

    elif "i like" in user:

        like = user.replace("i like", "").strip()

        remember("likes", like)

        return f"I will remember that you like {like}."

    elif "what do i like" in user:

        like = recall("likes")

        if like:
            return f"You like {like}."

        return "You haven't told me what you like yet."

    elif "my dream car is" in user:

        car = user.replace("my dream car is", "").strip()

        remember("dream_car", car)

        return f"I will remember that your dream car is {car}."

    elif "what is my dream car" in user:

        car = recall("dream_car")

        if car:
            return f"Your dream car is {car}."

        return "You haven't told me your dream car yet."

    elif "i live in" in user:

        city = user.replace("i live in", "").strip()

        remember("city", city)

        return f"I will remember that you live in {city}."

    elif "where do i live" in user:

        city = recall("city")

        if city:
            return f"You live in {city}."

        return "You haven't told me where you live yet."

    # ==========================
    # GOOGLE SEARCH
    # ==========================

    google = google_search(user)

    if google:
        return google

    # ==========================
    # WEBSITE
    # ==========================

    website = open_website(user)

    if website:
        return website

    # ==========================
    # OPEN APPS
    # ==========================

    app = open_app(user)

    if app:
        return app

    # ==========================
    # CALCULATOR
    # ==========================

    calc = calculate(user)

    if calc:
        return calc

    # ==========================
    # INTERNET SEARCH
    # ==========================

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

    # ==========================
    # PLUGINS
    # ==========================

    plugin = run_plugins(user)

    if plugin:
        return plugin

    # ==========================
    # AI
    # ==========================

    return chat_stream(user)