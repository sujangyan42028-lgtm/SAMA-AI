import requests

print("🔥 DICTIONARY PLUGIN LOADED")

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def run(user):

    print("🔥 DICTIONARY PLUGIN RUNNING")

    user = user.lower()

    remove_words = [
        "meaning",
        "definition",
        "define",
        "what is",
        "kya hai",
        "matlab",
        "ka matlab",
        "ka meaning",
        "meaning of",
        "batao",
        "please"
    ]

    word = user

    for item in remove_words:
        word = word.replace(item, " ")

    word = " ".join(word.split()).lower()

    print("Searching word:", word)
    print("Request URL:", URL + word)

    if not word:
        return "Kaunsa word dekhna hai?"

    try:

        r = requests.get(
            URL + word,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        print("Status Code:", r.status_code)

        if r.status_code != 200:
            print(r.text)
            return "Word nahi mila."

        data = r.json()[0]

        word_name = data.get("word", word)

        phonetic = data.get("phonetic", "")

        meaning = data["meanings"][0]

        part = meaning.get("partOfSpeech", "Unknown")

        definition = meaning["definitions"][0].get(
            "definition",
            "No definition found."
        )

        example = meaning["definitions"][0].get("example")

        answer = (
            f"{word_name}\n\n"
            f"Part of Speech : {part}\n\n"
            f"Meaning : {definition}"
        )

        if phonetic:
            answer += f"\n\nPronunciation : {phonetic}"

        if example:
            answer += f"\n\nExample : {example}"

        return answer

    except Exception as e:

        print("[DICTIONARY ERROR]", e)

        return "Dictionary API error."