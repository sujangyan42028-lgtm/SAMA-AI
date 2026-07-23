def wait_for_wake():
    word = input("Say SAMA: ")

    if word.lower() == "sama":
        return True