from ai.client import client
import json

MODEL = "qwen2.5:0.5b"

history = []

SYSTEM_PROMPT = """
You are SAMA (Smart Artificial Mind Assistant).

You were created by Sahil Khan.

Rules:
- Always introduce yourself as SAMA.
- If someone asks who created you, answer: I was created by Sahil Khan.
- Keep replies short and natural.
- Never mention OpenAI or ChatGPT.
- Never use emojis.
- Reply in plain text only.
"""


def chat_stream(question):

    history.append({
        "role": "user",
        "content": question
    })

    response = client.stream(
        "POST",
        "/api/chat",
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ] + history,
            "stream": True,
            "keep_alive": "1h",
            "options": {
                "temperature": 0.2,
                "num_predict": 120,
                "num_ctx": 1024,
                "num_thread": 8
            }
        }
    )

    answer = []

    with response as r:

        for line in r.iter_lines():

            if not line:
                continue

            data = json.loads(line)

            if "message" in data:
                token = data["message"]["content"]
                answer.append(token)

    final_answer = "".join(answer).strip()

    history.append({
        "role": "assistant",
        "content": final_answer
    })

    history[:] = history[-8:]

    return final_answer