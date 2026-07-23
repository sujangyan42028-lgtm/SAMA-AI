import os

def execute(command):

    command = command.lower()

    if command == "open notepad":
        os.system("notepad")
        return "Opening Notepad..."

    elif command == "open calculator":
        os.system("calc")
        return "Opening Calculator..."

    elif command == "open paint":
        os.system("mspaint")
        return "Opening Paint..."

    elif command == "open command prompt":
        os.system("start cmd")
        return "Opening Command Prompt..."

    return None
