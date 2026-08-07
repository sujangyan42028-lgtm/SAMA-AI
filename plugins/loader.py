import os
import importlib

plugins = {}


def load_plugins():

    global plugins

    plugins.clear()

    folder = "plugins"

    for file in os.listdir(folder):

        if (
            file.endswith(".py")
            and file != "__init__.py"
            and file != "manager.py"
            and file != "loader.py"
        ):

            module_name = file[:-3]

            try:

                module = importlib.import_module(
                    f"plugins.{module_name}"
                )

                plugins[module_name] = module

                print(f"[PLUGIN] Loaded -> {module_name}")

            except Exception as e:

                print(f"[PLUGIN ERROR] {module_name}: {e}")
                print("Loaded Plugins:", plugins.keys())
    return plugins