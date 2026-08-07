def extract_folder_name(command):

    command = command.lower().strip()

    words = command.split()

    if "folder" not in words:
        return None

    index = words.index("folder")

    # CREATE / MAKE
    if "create" in words or "make" in words:

        if index + 1 < len(words):
            return " ".join(words[index + 1:])

    # DELETE
    if "delete" in words:

        if index > 0:
            return " ".join(words[1:index])

    return None