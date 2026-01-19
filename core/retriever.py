"""
Retriever module - Tìm kiếm chunks liên quan với câu hỏi
"""

import json
from typing import List, Dict, Any
from .vector_store import get_vector_store
from .config import TOP_K

class Retriever:
    # Khởi tạo retriever
    def __init__(self, collection_name: str = "edu_documents"):
        self.vector_store = get_vector_store(collection_name)
        self.top_k = TOP_K
    
    # Tìm kiếm chunks liên quan nhất với câu hỏi
    def retrieve(self, query: str, k: int = None) -> List[Dict[str, Any]]:
        if k is None:
            k = self.top_k
        
        results = self.vector_store.similarity_search_with_score(query, k=k)
        
        chunks = []
        for doc, score in results:
            chunks.append({
                "text": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })
        return chunks
    
    # Tìm kiếm và trả về context dạng JSON
    def get_context(self, query: str, k: int = None) -> str:
        chunks = self.retrieve(query, k)
        
        context_chunks = []
        for chunk in chunks:
            context_chunks.append({
                "text": chunk["text"],
                "source": chunk["metadata"].get("source"),
                "section": chunk["metadata"].get("section"),
                "order": chunk["metadata"].get("order")
            })
        
        return json.dumps(context_chunks, ensure_ascii=False, indent=2)

_retriever_instance = None

# Lấy instance Retriever (singleton pattern)
def get_retriever(collection_name: str = "edu_documents") -> Retriever:
    global _retriever_instance
    if _retriever_instance is None:
        _retriever_instance = Retriever(collection_name)
    return _retriever_instance