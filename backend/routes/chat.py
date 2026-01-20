"""
Chat routes - API endpoints cho chat
"""

from fastapi import APIRouter
from ..schemas import ChatRequest, ChatResponse
from core.generator import get_generator
from core.config import LLM_MODEL, LLM_API_KEY
from google import genai

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_without_rag(request: ChatRequest):
    client = genai.Client(api_key=LLM_API_KEY)
    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=request.message
    )
    
    return ChatResponse(
        answer=response.text,
        use_rag=False
    )

@router.post("/chat/rag", response_model=ChatResponse)
def chat_with_rag(request: ChatRequest):
    generator = get_generator()
    result = generator.generate(request.message, debug=True)
    
    return ChatResponse(
        answer=result["answer"],
        context=result.get("context"),
        use_rag=True
    )