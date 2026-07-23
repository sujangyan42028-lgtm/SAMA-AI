import webbrowser
import urllib.parse

def google_search(command):

    command = command.lower()

    keywords = [
        "search google for",
        "search for",
        "google",
        "search"
    ]

    for key in keywords:
        if key in command:

            query = command.replace(key, "").strip()

            if query == "":
                return None

            url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

            webbrowser.open(url)

            return f"Searching Google for {query}."

    return None