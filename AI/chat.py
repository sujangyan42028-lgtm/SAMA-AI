import ollama

MODEL = "qwen2.5:1.5b"

history = []

SYSTEM_PROMPT = """
You are SAMA (Smart Artificial Mind Assistant).

You were created by Sahil.

Rules:
- Always introduce yourself as SAMA.
- If someone asks who created you, answer: "I was created by Sahil."
- Be friendly, intelligent and professional.
- Give short answers unless the user asks for details.
- Remember the conversation.
- Help with coding, trading, business, studying, technology and daily life.
- Never mention OpenAI, ChatGPT or any other creator.
"""

def chat_stream(question):

    history.append({
        "role": "user",
        "content": question
    })

    stream = ollama.chat(
        model=MODEL,
        stream=True,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + history
    )

    answer = ""

    print("\nSAMA: ", end="", flush=True)

    for chunk in stream:
        text = chunk["message"]["content"]
        print(text, end="", flush=True)
        answer += text

    print()

    history.append({
        "role": "assistant",
        "content": answer
    })

    if len(history) > 20:
        history.pop(0)
        history.pop(0)

    return answer