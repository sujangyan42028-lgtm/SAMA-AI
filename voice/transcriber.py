from faster_whisper import WhisperModel

print("Loading Whisper Small Model...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

CORRECTIONS = {
    "reading folder": "trading folder",
    "reading": "trading",
    "tradings": "trading",
    "bit coin": "bitcoin",
    "beat coin": "bitcoin",
    "note pad": "notepad",
    "note pet": "notepad",
    "vs code": "vscode",
    "visual studio code": "vscode",
    "google chrome": "chrome",
    "chrome browser": "chrome",
    "jarvis": "sama",
    "same": "sama",
    "summer": "sama"
}


def clean_text(text):

    text = text.lower().strip()

    text = (
        text.replace(".", "")
        .replace(",", "")
        .replace("?", "")
        .replace("!", "")
    )

    while "  " in text:
        text = text.replace("  ", " ")

    for wrong, right in CORRECTIONS.items():
        text = text.replace(wrong, right)

    return text


def transcribe(audio_file):

    segments, info = model.transcribe(
        audio_file,
        language="en",
        beam_size=8,
        best_of=8,
        temperature=0.0,
        vad_filter=True,
        condition_on_previous_text=False,
        word_timestamps=False
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    text = clean_text(text)

    print("=" * 45)
    print("Whisper:", text)
    print("Language:", info.language)
    print("=" * 45)

    return text