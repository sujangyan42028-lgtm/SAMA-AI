from ai.client import client
from memory.conversation import remember, recall
import json

MODEL = "qwen2.5:0.5b"

history = []

SYSTEM_PROMPT = """
You are SAMA.
Created by Sahil Khan.

Rules:
- Keep replies short.
- Never mention ChatGPT or OpenAI.
- Reply in plain text.
"""


def chat_stream(question):

    question = question.strip()

    history.append({
        "role": "user",
        "content": question
    })

    # Load previous conversations
    past = recall()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add old conversations
    for chat in past[-10:]:

        messages.append({
            "role": "user",
            "content": chat["user"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["assistant"]
        })

    # Add current conversation
    messages += history

    response = client.stream(
        "POST",
        "/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": True,
            "keep_alive": "1h",
            "options": {
                "temperature": 0.2,
                "num_predict": 50,
                "num_ctx": 512,
                "num_thread": 8,
                "top_k": 20,
                "top_p": 0.8
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
                answer.append(data["message"]["content"])

    final_answer = "".join(answer).strip()

    history.append({
        "role": "assistant",
        "content": final_answer
    })

    # Keep only last 4 live messages
    history[:] = history[-4:]

    # Save conversation permanently
    remember(question, final_answer)

    return final_answer