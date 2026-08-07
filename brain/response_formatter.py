def format_response(text):

    if not text:
        return text

    text = text.strip()

    replacements = {

        "i'm good": "Main theek hoon.",
        "i am good": "Main theek hoon.",
        "how about you": "Tum kaise ho?",
        "yes": "Haan.",
        "no": "Nahi.",
        "thank you": "Shukriya.",
        "you're welcome": "Koi baat nahi.",

        "python is": "Python ek",
        "programming language": "programming language hai",
        "artificial intelligence": "Artificial Intelligence",
        "automation": "automation",
        "web development": "web development",

        "who created you": "Mujhe Sahil Khan ne banaya hai.",
        "i was created by sahil khan": "Mujhe Sahil Khan ne banaya hai."
    }

    lower = text.lower()

    for eng, hin in replacements.items():
        lower = lower.replace(eng, hin)

    return lower.capitalize()