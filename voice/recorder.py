import sounddevice as sd
import soundfile as sf
import numpy as np
import tempfile
import torch
from silero_vad import load_silero_vad, get_speech_timestamps

SAMPLE_RATE = 16000
CHANNELS = 1
MAX_SECONDS = 5

print("Loading Silero VAD...")
vad_model = load_silero_vad()


def record():

    temp = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    filename = temp.name
    temp.close()

    print("🎤 Listening...")

    audio = sd.rec(
        int(MAX_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )

    sd.wait()

    audio = audio.flatten()

    wav = torch.from_numpy(audio)

    speech = get_speech_timestamps(
        wav,
        vad_model,
        sampling_rate=SAMPLE_RATE
    )

    if speech:

        start = speech[0]["start"]
        end = speech[-1]["end"]

        audio = audio[start:end]

    sf.write(
        filename,
        audio,
        SAMPLE_RATE
    )

    return filename