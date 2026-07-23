import asyncio
import edge_tts
import pygame
import os
import uuid

VOICE = "en-IN-NeerjaNeural"    # Indian female voice

pygame.mixer.init()

async def _speak(text):
    filename = f"{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)

def speak(text):
    print("SAMA:", text)
    asyncio.run(_speak(text))