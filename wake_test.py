import openwakeword
from openwakeword.model import Model

model = Model(inference_framework="onnx")

print("SAMA wake word ready... bolo kuch")

while True:
    audio = input("Type 'sama': ")

    if audio.lower() == "sama":
        print("✅ SAMA activated!")