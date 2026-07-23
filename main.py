from brain.brain import think
from automation.automation import execute
from voice.listen import listen
from voice.speak import speak

print("=" * 40)
print("        SAMA AI v3.0")
print("=" * 40)

speak("Hello Sahil. I am SAMA.")

while True:

    print("🎤 Listening...")
    user = listen()

    if user == "":
        continue

    if user.lower() == "bye":
        speak("Goodbye Sahil.")
        break

    print("⚙️ Checking Skills...")
    action = execute(user)

    if action:
        print("🔊 Speaking...")
        speak(action)
    else:
        print("🧠 Thinking...")
        answer = think(user)

        print("🔊 Speaking...")
        speak(answer)