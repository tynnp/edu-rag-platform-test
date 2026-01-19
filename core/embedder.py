"""
Embedder module - Tạo vector embeddings cho văn bản tiếng Việt
Sử dụng model: dangvantuan/vietnamese-embedding
"""

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class Embedder:
    # Khởi tạo embedder với model chỉ định
    def __init__(self, model_name: str = "dangvantuan/vietnamese-embedding"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
    
    # Tạo embedding cho một đoạn văn bản
    def embed_text(self, text: str) -> List[float]:
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding.tolist()
    
    # Tạo embeddings cho nhiều đoạn văn bản
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()
    
    # Trả về số chiều của vector embedding
    def get_dimension(self) -> int:
        return self.dimension

_embedder_instance = None

# Lấy instance embedder (singleton pattern)
def get_embedder(model_name: str = "dangvantuan/vietnamese-embedding") -> Embedder:
    global _embedder_instance
    if _embedder_instance is None or _embedder_instance.model_name != model_name:
        _embedder_instance = Embedder(model_name)
    return _embedder_instance