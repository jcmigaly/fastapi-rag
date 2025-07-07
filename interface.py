from models.schemas import ChatMessage, ChatRequest, ChatResponse
import requests

chat_messages: list[ChatMessage] = [ChatMessage()]

def printMessage(message: ChatMessage):
    print(f" \n{message.role}: {message.content}")

def flow():
    while True:
        printMessage(chat_messages[-1])

        userInput = str(input(f"\nuser: "))
        userMessage = ChatMessage()
        userMessage.role = 'user'
        userMessage.content = userInput
        chat_messages.append(userMessage)

        messages_dict = [dict(message) for message in chat_messages]
        response = requests.post("http://127.0.0.1:8000/chat", json={"messages": messages_dict}).json()
        systemMessage = ChatMessage()
        systemMessage.role = response["role"]
        systemMessage.content = response["content"]
        chat_messages.append(systemMessage)

flow()