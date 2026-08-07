import asyncio
import edge_tts
import tempfile
import pygame
import os
import threading
import time

from config import VOICE
from utils.threading_manager import run_background

pygame.mixer.init()

lock = threading.Lock()

is_speaking = False


async def generate(text, output):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="+5%",
        pitch="+0Hz"
    )

    await communicate.save(output)


def speak(text):

    global is_speaking

    if not text:
        return

    text = str(text).strip()

    print("SAMA:", text)

    try:

        with tempfile.NamedTemporaryFile(
            suffix=".mp3",
            delete=False
        ) as temp:

            mp3 = temp.name

        print("Generating Voice...")

        asyncio.run(generate(text, mp3))

        print("Voice Generated:", mp3)

        with lock:

            is_speaking = True

            print("Playing Audio...")

            pygame.mixer.music.load(mp3)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.01)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

            is_speaking = False

        if os.path.exists(mp3):
            os.remove(mp3)

        print("Audio Finished.")

    except Exception as e:

        is_speaking = False

        print("=" * 50)
        print("SPEAK ERROR")
        print(e)
        print("=" * 50)


def speak_async(text):
    run_background(speak, text)


def stop_speaking():

    global is_speaking

    if is_speaking:

        pygame.mixer.music.stop()

        is_speaking = False