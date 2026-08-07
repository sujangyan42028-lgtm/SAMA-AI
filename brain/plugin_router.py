from plugins.selector import select_plugin
from plugins.manager import run_plugin


def plugin_router(user):

    plugin = select_plugin(user)

    if not plugin:
        return None

    try:

        return run_plugin(plugin, user)

    except Exception as e:

        print(f"[PLUGIN ERROR] {plugin}: {e}")

        return None