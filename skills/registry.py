from skills.browser import open_website
from skills.google import google_search
from skills.opener import open_app
from skills.calculator import calculate


def execute(user):

    handlers = [

        google_search,
        open_website,
        open_app,
        calculate

    ]

    for handler in handlers:

        result = handler(user)

        if result:
            return result

    return None