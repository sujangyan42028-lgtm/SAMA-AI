from ai.chat import chat

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = chat(question)
    print("SAMA:", answer)