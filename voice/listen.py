import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            text = recognizer.recognize_google(
                audio,
                language="hi-IN"
            )

            print("You:", text)

            return text

        except sr.WaitTimeoutError:
            print("Timeout")
            return ""

        except Exception as e:
            print(e)
            return ""


def listen_quick():
    return listen()