import subprocess
import os

APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "explorer": "explorer.exe",
    "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}


def run(user):

    user = user.lower()

    if "open" in user:

        for app, path in APPS.items():

            if app in user:

                try:

                    path = os.path.expandvars(path)

                    subprocess.Popen(path)

                    return f"{app.title()} opened."

                except Exception as e:

                    print(e)

                    return f"{app.title()} open nahi hua."

    if "close" in user:

        for app in APPS:

            if app in user:

                os.system(f"taskkill /f /im {app}.exe >nul 2>&1")

                return f"{app.title()} closed."

    return None