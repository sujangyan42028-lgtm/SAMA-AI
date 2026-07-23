from skills.vision import capture_screen
from skills.vision_ai import analyze_image

image = capture_screen()

answer = analyze_image(
    image,
    "Describe everything you see on this screen."
)

print(answer)