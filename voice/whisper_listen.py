import tempfile
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def listen():

    print("🎤 Listening...")

    samplerate = 16000
    duration = 5

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:

        sf.write(f.name, audio, samplerate)

        segments, _ = model.transcribe(
            f.name,
            language="en"
        )

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    print("You:", text)

    return text