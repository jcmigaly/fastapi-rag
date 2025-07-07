from fastapi import APIRouter

from models.schemas import ChatMessage, ChatRequest, ChatResponse
from services.get_message import get_message

router = APIRouter()

@router.post('/chat')
def get_ai_message(request: ChatRequest):
    # Isolate messages
    messages = request.messages
    question = messages[-1]
    history = messages[-6:-1]
    print("question", question)
    print("history", history)

    # Put messages into getAIMessage helepr
    message = get_message(question, history)
    print(message)
    return message