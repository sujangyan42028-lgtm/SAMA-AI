from skills.browser import open_website
from skills.google import google_search
from skills.opener import open_app
from skills.calculator import calculate
from skills.file_manager import file_manager

def handle(user):

    google = google_search(user)
    if google:
        return google

    website = open_website(user)
    if website:
        return website

    app = open_app(user)
    if app:
        return app

    calc = calculate(user)
    if calc:
        return calc
    result = file_manager(user)

    if result:
        return result
    return None