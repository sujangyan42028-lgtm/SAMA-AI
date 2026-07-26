def reply(user):

    user = user.lower()

    if user in ["hello", "hi", "hey"]:
        return "Hello Sahil."

    if user in ["what is your name", "who are you"]:
        return "My name is SAMA."

    if "who created you" in user or user == "created":
        return "I was created by Sahil Khan."

    if user in ["how are you", "how are you doing"]:
        return "I am doing great. Thank you for asking."

    if user == "good morning":
        return "Good morning Sahil."

    if user == "good night":
        return "Good night Sahil."

    if user in ["thank you", "thanks"]:
        return "You are welcome."

    return None