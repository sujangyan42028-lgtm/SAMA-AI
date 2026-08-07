import os
import ctypes
import subprocess


def run(user):

    user = user.lower()

    try:

        if "shutdown" in user:

            os.system("shutdown /s /t 0")

            return "PC shutdown ho raha hai."

        elif "restart" in user:

            os.system("shutdown /r /t 0")

            return "PC restart ho raha hai."

        elif "sleep" in user:

            ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

            return "PC sleep mode me ja raha hai."

        elif "lock" in user:

            ctypes.windll.user32.LockWorkStation()

            return "PC lock kar diya."

        elif "screenshot" in user:

            try:
                from PIL import ImageGrab

                img = ImageGrab.grab()

                path = "screenshot.png"

                img.save(path)

                return f"Screenshot save ho gaya: {path}"

            except Exception:
                return "Screenshot ke liye Pillow install karo."

        elif "task manager" in user:

            subprocess.Popen("taskmgr.exe")

            return "Task Manager open kar diya."

        elif "control panel" in user:

            subprocess.Popen("control.exe")

            return "Control Panel open kar diya."

        return None

    except Exception as e:

        print("[SYSTEM ERROR]", e)

        return "System command execute nahi ho paya."