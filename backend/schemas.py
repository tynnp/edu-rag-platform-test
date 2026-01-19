"""
Schemas - Pydantic models cho request/response
"""

from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    context: Optional[str] = None
    use_rag: bool