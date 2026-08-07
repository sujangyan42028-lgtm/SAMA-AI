import webbrowser
import urllib.parse


def run(user):

    query = urllib.parse.quote(user)

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)

    return "Theek hai, Google par search kar raha hoon."