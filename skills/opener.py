import subprocess

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "google chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "notepad": "notepad.exe",
    "notebook": "notepad.exe",

    "calculator": "calc.exe",
    "calc": "calc.exe",

    "paint": "mspaint.exe",

    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",

    "vscode": r"C:\Users\hyder\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "vs code": r"C:\Users\hyder\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "code": r"C:\Users\hyder\AppData\Local\Programs\Microsoft VS Code\Code.exe",
}


def open_app(command):

    command = command.lower().strip()

    if "open" not in command:
        return None

    for app_name, app_path in APPS.items():

        if app_name in command:

            try:
                subprocess.Popen(app_path)
                return f"Opening {app_name}."

            except Exception as e:
                return f"I couldn't open {app_name}. Error: {e}"

    return None