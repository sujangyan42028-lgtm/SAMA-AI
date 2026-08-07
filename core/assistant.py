import time

from core.response import get_response
from core.session import Session
from core.memory import (
    remember,
    recall,
    forget,
    get_all_memory
)

from wakeword.wake import wait_for_wake_word

from voice.listen import listen
from voice.speak import speak, stop_speaking

from automation.automation import execute

window = None


def set_window(win):
    global window
    window = win


def run(gui=None):

    global window

    if gui is not None:
        window = gui

    session = Session()

    from config import VERSION

    speak(f"{VERSION} initialized.")

    while True:

        if not session.active:

            if window:
                window.sleep()

            wait_for_wake_word()

            session.start()

            if window:
                window.ready()

            speak("Haan Sahil, bolo.")

        while session.active:

            if window:
                window.listening()

            start = time.time()

            user = listen()

            print(f"🎤 Listen Time: {time.time()-start:.2f} sec")

            if not user:

                if session.expired():

                    print("💤 Session Ended")

                    if window:
                        window.sleep()

                    speak("Theek hai, main sleep mode me ja rahi hoon.")

                    session.stop()

                    break

                continue

            session.update()

            user = user.strip().lower()

            if window:
                window.add_message("You", user)

            # =========================
            # MEMORY
            # =========================

            if user.startswith("remember"):

                text = user.replace("remember", "", 1).strip()

                if ":" in text:

                    key, value = text.split(":", 1)

                    remember(
                        key.strip(),
                        value.strip()
                    )

                    answer = (
                        f"I will remember that "
                        f"{key.strip()} is {value.strip()}."
                    )

                    if window:
                        window.add_message("SAMA", answer)
                        window.speaking()

                    speak(answer)

                    if window:
                        window.ready()

                    continue

            if user.startswith("what is"):

                key = user.replace(
                    "what is",
                    "",
                    1
                ).strip()

                value = recall(key)

                if value:
                    answer = f"{key} is {value}."
                else:
                    answer = "I don't remember that yet."

                if window:
                    window.add_message("SAMA", answer)
                    window.speaking()

                speak(answer)

                if window:
                    window.ready()

                continue
            # =========================
            # STOP SPEAKING
            # =========================

            if user == "stop":

                stop_speaking()

                if window:
                    window.ready()

                continue

            # =========================
            # EXIT
            # =========================

            if user in ["take care", "goodbye", "exit"]:

                if window:
                    window.sleep()

                speak("Goodbye Sahil.")

                return

            # =========================
            # THINKING
            # =========================

            if window:
                window.thinking()

            start = time.time()

            action = execute(user)

            print(f"⚙️ Action Time: {time.time()-start:.2f} sec")

            if action:

                if window:
                    window.add_message("SAMA", action)
                    window.speaking()

                speak(action)

                if window:
                    window.ready()

                continue

            # =========================
            # AI RESPONSE
            # =========================

            start = time.time()

            answer = get_response(user)

            print("=" * 40)
            print(f"🧠 AI Response Time : {time.time()-start:.2f} sec")
            print("=" * 40)

            if window:
                window.add_message("SAMA", answer)
                window.speaking()

            speak(answer)

            if window:
                window.ready()