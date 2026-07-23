import webbrowser

websites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "x": "https://x.com"
}

def open_website(command):

    command = command.lower()

    for site, url in websites.items():
        if f"open {site}" in command:
            webbrowser.open(url)
            return f"Opening {site}."

    return None