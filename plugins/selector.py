from plugins.registry import PLUGIN_MAP


def select_plugin(user):

    user = user.lower().strip()

    best_plugin = None
    best_score = 0

    for plugin, keywords in PLUGIN_MAP.items():

        score = 0

        for keyword in keywords:

            if keyword in user:
                score += 1

        if score > best_score:
            best_score = score
            best_plugin = plugin

    return best_plugin