from skills.browser import open_website


def browser_plugin(user):

    result = open_website(user)

    if result:
        return result

    return None