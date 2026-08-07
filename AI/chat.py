from ai.client import client
from memory.conversation import remember, recall
from ai.personality import SYSTEM_PROMPT
from brain.knowledge import learn
import json
from config import MODEL, OLLAMA_URL


history = []


def chat_stream(question):

    original_question = question.strip()

    history.append({
        "role": "user",
        "content": original_question
    })

    past = recall()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Last 3 conversations
    for chat in past[-3:]:

        messages.append({
            "role": "user",
            "content": chat["user"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["assistant"]
        })

    messages.extend(history)

    response = client.stream(
        "POST",
        "/api/chat",
        json={
            "model": MODEL,
            "messages": messages,
            "stream": True,
            "keep_alive": "1h",
            "options": {
                "temperature": 0.1,
                "num_predict": 35,
                "num_ctx": 512,
                "num_thread": 8,
                "top_k": 20,
                "top_p": 0.9,
                "repeat_penalty": 1.11
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

    # Save conversation
    remember(original_question, final_answer)

    # Auto Learn
    if (
        len(final_answer) > 25
        and "mujhe nahi pata" not in final_answer.lower()
        and "i don't know" not in final_answer.lower()
    ):
        learn(original_question, final_answer)

    return final_answer