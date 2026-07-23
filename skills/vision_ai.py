import ollama

def analyze_image(image_path, question="What is in this image?"):

    response = ollama.chat(
        model="moondream",
        messages=[
            {
                "role": "user",
                "content": question,
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]