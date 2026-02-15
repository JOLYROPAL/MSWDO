from fastapi import APIRouter
from pydantic import BaseModel

from core.services.chatbot_service import ChatbotService


class ChatPrompt(BaseModel):
    message: str


class ChatReply(BaseModel):
    answer: str


router = APIRouter(prefix="/chatbot", tags=["chatbot"])


@router.post("/ask", response_model=ChatReply)
def ask_chatbot(payload: ChatPrompt):
    return ChatReply(answer=ChatbotService().respond(payload.message))
