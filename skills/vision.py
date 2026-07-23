from PIL import Image
import mss

def capture_screen():

    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

        img = Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )

        img.save("screen.png")

    return "screen.png"