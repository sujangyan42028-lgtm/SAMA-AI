import os
import shutil

from brain.nlp import extract_folder, extract_delete_folder

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")


def file_manager(command):

    command = command.lower().strip()

    # ==========================
    # CREATE FOLDER
    # ==========================

    if any(x in command for x in ["create", "make"]):

        name = extract_folder(command)

        if name:

            path = os.path.join(DESKTOP, name)

            try:
                os.makedirs(path, exist_ok=True)
                return f"Folder '{name}' created successfully."

            except Exception as e:
                return str(e)

    # ==========================
    # DELETE FOLDER
    # ==========================

    if any(x in command for x in ["delete", "remove"]):

        name = extract_delete_folder(command)

        if name:

            path = os.path.join(DESKTOP, name)

            try:
                shutil.rmtree(path)
                return f"Folder '{name}' deleted successfully."

            except FileNotFoundError:
                return f"Folder '{name}' not found."

            except Exception as e:
                return str(e)

    return None