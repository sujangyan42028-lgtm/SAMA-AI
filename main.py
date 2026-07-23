from brain.brain import think
from automation.automation import execute
from voice.listen import listen
from voice.speak import speak

print("=" * 40)
print("        SAMA AI v3.0")
print("=" * 40)

speak("Hello Sahil. I am SAMA.")

while True:

    user = listen()

    if user == "":
        continue

    if user.lower() == "bye":
        speak("Goodbye Sahil.")
        break

    action = execute(user)

    if action:
        speak(action)
    else:
        answer = think(user)
        speak(answer)