from plugins.loader import load_plugins

plugins = load_plugins()


def run_plugin(name, user):

    if name not in plugins:
        return None

    module = plugins[name]

    if hasattr(module, "run"):

        return module.run(user)

    return None