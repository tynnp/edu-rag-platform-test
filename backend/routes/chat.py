"""
Chat routes - API endpoints cho chat
"""

from fastapi import APIRouter
from ..schemas import ChatRequest, ChatResponse
from core.generator import get_generator
from core.config import LLM_MODEL, LLM_API_KEY
import google.generativeai as genai

router = APIRouter()

# Chat không RAG
@router.post("/chat", response_model=ChatResponse)
def chat_without_rag(request: ChatRequest):
    genai.configure(api_key=LLM_API_KEY)
    model = genai.GenerativeModel(LLM_MODEL)
    
    response = model.generate_content(request.message)
    
    return ChatResponse(
        answer=response.text,
        use_rag=False
    )

# Chat có RAG
@router.post("/chat/rag", response_model=ChatResponse)
def chat_with_rag(request: ChatRequest):
    generator = get_generator()
    result = generator.generate(request.message, debug=True)
    
    return ChatResponse(
        answer=result["answer"],
        context=result.get("context"),
        use_rag=True
    )