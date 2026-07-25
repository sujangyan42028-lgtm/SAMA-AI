from openwakeword.model import Model
import sounddevice as sd
import numpy as np

model = Model()

print("Loaded:", model.models.keys())

def wait_for_wake_word():

    print("Waiting for 'Hey Jarvis'...")

    samplerate = 16000
    blocksize = 1280

    with sd.InputStream(
        samplerate=samplerate,
        channels=1,
        dtype="int16",
        blocksize=blocksize
    ) as stream:

        while True:

            audio, _ = stream.read(blocksize)

            audio = audio.flatten().astype(np.int16)

            prediction = model.predict(audio)

            score = prediction["hey_jarvis"]

            if score > 0.5:
                print("Wake Word Detected!")
                return