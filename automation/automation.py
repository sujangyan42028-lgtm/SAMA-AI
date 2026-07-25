import os

APPS = {
    "open notepad": ("notepad", "Opening Notepad..."),
    "open calculator": ("calc", "Opening Calculator..."),
    "open paint": ("mspaint", "Opening Paint..."),
    "open command prompt": ("start cmd", "Opening Command Prompt..."),
}

def execute(command):

    command = command.lower().strip()

    if command in APPS:
        app, message = APPS[command]
        os.system(app)
        return message

    return None