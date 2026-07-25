import subprocess
import tempfile
import os
import pygame
import time
import threading

from utils.threading_manager import run_background

ENGINE = "engine/piper.exe"
MODEL = "engine/en_US-lessac-medium.onnx"
CONFIG = "engine/en_US-lessac-medium.onnx.json"
ESPEAK = "engine/espeak-ng-data"

pygame.mixer.init()

lock = threading.Lock()

is_speaking = False


def speak(text):

    global is_speaking

    if not text:
        return

    text = str(text).strip()

    print("SAMA:", text)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        wav = temp.name

    result = subprocess.run(
        [
            ENGINE,
            "--model", MODEL,
            "--config", CONFIG,
            "--espeak_data", ESPEAK,
            "--output_file", wav
        ],
        input=text,
        text=True,
        encoding="utf-8",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode != 0:
        return

    with lock:

        is_speaking = True

        pygame.mixer.music.load(wav)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.01)

        is_speaking = False

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    if os.path.exists(wav):
        os.remove(wav)


def speak_async(text):
    run_background(speak, text)


def stop_speaking():

    global is_speaking

    if is_speaking:
        pygame.mixer.music.stop()
        is_speaking = False