def reply(user):

    user = user.lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey", "hii", "helo"]:
        return "Namaste Sahil! Main SAMA hoon."

    if user in ["good morning", "morning"]:
        return "Good Morning Sahil! 😊"

    if user in ["good night", "night"]:
        return "Good Night Sahil. Achhe se aaram karna."

    if user in ["good evening"]:
        return "Good Evening Sahil."

    # Identity
    if user in [
        "who are you",
        "tum kaun ho",
        "ap kaun ho"
    ]:
        return "Main SAMA hoon."

    if user in [
        "who created you",
        "tumhe kisne banaya",
        "tumhen kisne banaya",
        "kisne banaya"
    ]:
        return "Mujhe Sahil Khan ne banaya hai."

    # Feelings
    if user in [
        "how are you",
        "kaise ho",
        "kese ho",
        "kaisa ho"
    ]:
        return "Main bilkul theek hoon. Tum kaise ho?"

    # Thanks
    if user in [
        "thank you",
        "thanks",
        "shukriya",
        "thankyou"
    ]:
        return "Koi baat nahi Sahil. 😊"

    # Python
    if user in [
        "python kya hai",
        "what is python"
    ]:
        return "Python ek programming language hai jo software, website, AI aur automation banane ke kaam aati hai."

    # Bitcoin
    if user in [
        "bitcoin kya hai",
        "what is bitcoin"
    ]:
        return "Bitcoin ek digital cryptocurrency hai jo blockchain technology par kaam karti hai."

    # AI
    if user in [
        "ai kya hai",
        "artificial intelligence kya hai"
    ]:
        return "AI ka matlab Artificial Intelligence hai. Ye machines ko insaano ki tarah sochne aur seekhne ki capability deta hai."

    # Trading
    if user in [
        "trading kya hai",
        "what is trading"
    ]:
        return "Trading ka matlab assets ko buy aur sell karke profit kamaana hota hai."

    return None