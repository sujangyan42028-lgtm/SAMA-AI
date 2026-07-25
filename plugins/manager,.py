from plugins.calculator import calculator_plugin
from plugins.browser import browser_plugin
from plugins.apps import apps_plugin


plugins = [
    calculator_plugin,
    browser_plugin,
    apps_plugin,
]


def run_plugins(user):

    for plugin in plugins:

        result = plugin(user)

        if result:
            return result

    return None