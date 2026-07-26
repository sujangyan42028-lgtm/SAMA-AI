import os
import shutil

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")


def file_manager(command):

    command = command.lower().strip()

    # Create Folder
    if "create folder" in command:

        name = command.replace("create folder", "").strip()

        if not name:
            return None

        path = os.path.join(DESKTOP, name)

        try:
            os.makedirs(path, exist_ok=True)
            return f"Folder '{name}' created successfully."

        except Exception as e:
            return f"Error: {e}"

    # Delete Folder
    if "delete folder" in command:

        name = command.replace("delete folder", "").strip()

        path = os.path.join(DESKTOP, name)

        try:
            shutil.rmtree(path)
            return f"Folder '{name}' deleted."

        except Exception:
            return "Folder not found."

    return None