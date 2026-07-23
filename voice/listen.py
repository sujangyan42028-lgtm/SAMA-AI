import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You:", text)
        return text

    except Exception as e:
        print("ERROR:", e)
        return ""