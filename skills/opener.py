import subprocess

apps = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "vscode": r"C:\Users\hyder\AppData\Local\Programs\Microsoft VS Code\Code.exe"
}

def open_app(command):

    command = command.lower()

    for app in apps:
        if f"open {app}" in command:
            try:
                subprocess.Popen(apps[app])
                return f"Opening {app}."
            except Exception:
                return f"I couldn't open {app}."

    return None