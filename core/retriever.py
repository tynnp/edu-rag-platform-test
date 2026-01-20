"""
Retriever module - Tìm kiếm chunks liên quan với câu hỏi
"""

import json
from typing import List, Dict, Any
from .vector_store import get_vector_store
from .config import TOP_K

class Retriever:
    def __init__(self, collection_name: str = "edu_documents"):
        self.vector_store = get_vector_store(collection_name)
        self.top_k = TOP_K
    
    def retrieve(self, query: str, k: int = None, use_hybrid: bool = True) -> List[Dict[str, Any]]:
        if k is None:
            k = self.top_k
        
        # Ưu tiên hybrid search
        if use_hybrid:
            results = self.vector_store.hybrid_search(query, k=k)
        else:
            results = self.vector_store.similarity_search_with_score(query, k=k)
        
        chunks = []
        for doc, score in results:
            chunks.append({
                "text": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })
        return chunks
    
    def get_context(self, query: str, k: int = None) -> str:
        chunks = self.retrieve(query, k)
        
        context_chunks = []
        for chunk in chunks:
            context_chunks.append({
                "text": chunk["text"],
                "source": chunk["metadata"].get("source"),
                "section": chunk["metadata"].get("section"),
                "page": chunk["metadata"].get("page")
            })
        
        return json.dumps(context_chunks, ensure_ascii=False, indent=2)

_retriever_instance = None

# Lấy instance Retriever (singleton pattern)
def get_retriever(collection_name: str = "edu_documents") -> Retriever:
    global _retriever_instance
    if _retriever_instance is None:
        _retriever_instance = Retriever(collection_name)
    return _retriever_instance