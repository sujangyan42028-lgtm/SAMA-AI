import ollama

MODEL = "qwen2.5:1.5b"

history = []

def chat(question):

    history.append({
        "role": "user",
        "content": question
    })

    response = ollama.chat(
        model=MODEL,
        messages=history
    )

    answer = response["message"]["content"]

    history.append({
        "role": "assistant",
        "content": answer
    })

    # Last 20 messages hi yaad rakho
    if len(history) > 20:
        del history[:2]

    return answer