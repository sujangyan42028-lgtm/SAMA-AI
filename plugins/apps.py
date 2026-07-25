from skills.opener import open_app


def apps_plugin(user):

    result = open_app(user)

    if result:
        return result

    return None