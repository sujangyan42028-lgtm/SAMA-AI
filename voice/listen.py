import speech_recognition as sr

recognizer = sr.Recognizer()

recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def listen():

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.2)

        try:
            audio = recognizer.listen(
                source,
                timeout=3,
                phrase_time_limit=3
            )

            text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

            print("You:", text)
            return text

        except sr.WaitTimeoutError:
            return ""

        except Exception:
            return ""


def listen_quick():

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source, duration=0.1)

        try:
            audio = recognizer.listen(
                source,
                timeout=4,
                phrase_time_limit=5
            )

            text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

            print("You:", text)
            return text

        except sr.WaitTimeoutError:
            return ""

        except Exception:
            return ""