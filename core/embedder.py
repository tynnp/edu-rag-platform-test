"""
Embedder module - Tạo vector embeddings sử dụng Google Gemini API (qua LangChain)
"""

from typing import List
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from .config import LLM_API_KEY, EMBEDDING_MODEL

class Embedder:
    def __init__(self, model_name: str = "models/text-embedding-004"):
        if not LLM_API_KEY:
            raise ValueError("LLM_API_KEY chưa được cấu hình!")
        
        self.model_name = model_name
        self.dimension = 768
        
        self.client = GoogleGenerativeAIEmbeddings(
            model=model_name,
            google_api_key=LLM_API_KEY
        )
        
    def embed_text(self, text: str) -> List[float]:
        try:
            return self.client.embed_query(text)
        except Exception as e:
            print(f"Lỗi embedding text: {e}")
            return [0.0] * self.dimension
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        try:
            return self.client.embed_documents(texts)
        except Exception as e:
            print(f"Lỗi embedding texts: {e}")
            return [[0.0] * self.dimension for _ in texts]
    
    def get_dimension(self) -> int:
        return self.dimension

_embedder_instance = None

def get_embedder(model_name: str = "models/text-embedding-004") -> Embedder:
    global _embedder_instance
    if _embedder_instance is None or _embedder_instance.model_name != model_name:
        _embedder_instance = Embedder(model_name)
    return _embedder_instance