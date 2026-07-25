import time

from core.response import get_response
from core.session import Session

from wakeword.wake import wait_for_wake_word

from voice.listen import listen
from voice.speak import speak, speak_async, stop_speaking

from automation.automation import execute


def run():

    session = Session()

    speak("SAMA version 8 initialized.")

    while True:

        # Wake word sirf tab jab session inactive ho
        if not session.active:
            wait_for_wake_word()
            session.start()

        start = time.time()

        user = listen()

        print(f"🎤 Listen Time: {time.time() - start:.2f} sec")

        # Agar kuch nahi suna
        if not user:

            if session.expired():
                session.stop()
                print("💤 Session Ended")
                speak("Going to sleep.")

            continue

        session.update()

        user = user.strip().lower()

        # Stop Speaking
        if user == "stop":
            stop_speaking()
            continue

        # Exit
        if user in ["take care", "goodbye", "exit"]:

            speak("Goodbye Sahil.")
            break

        # Automation
        start = time.time()

        action = execute(user)

        if action:

            print(f"⚙️ Action Time: {time.time() - start:.2f} sec")

            speak(action)

            continue

        print(f"⚙️ Action Time: {time.time() - start:.2f} sec")

        # AI
        start = time.time()

        answer = get_response(user)

        think_time = time.time() - start

        print("=" * 40)
        print(f"🧠 AI Response Time : {think_time:.2f} sec")
        print("=" * 40)

        speak_async(answer)