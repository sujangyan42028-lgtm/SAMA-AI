import asyncio
import edge_tts
import os
import uuid

VOICE = "en-US-GuyNeural"

async def _speak(text):
    filename = f"{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)
    os.system(f'start "" "{filename}"')

def speak(text):
    print("SAMA:", text)
    asyncio.run(_speak(text))