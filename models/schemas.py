from pydantic import BaseModel, Field
from typing import Literal, List

class ChatMessage(BaseModel):
    role: Literal["system", "user"] = Field(default="system")
    content: str = Field(default="Hi, how can I help you today?")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(...)

class ChatResponse(BaseModel):
    answer: str = Field(...)
