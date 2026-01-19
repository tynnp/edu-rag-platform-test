"""
VectorStore module - Kết nối PostgreSQL với pgvector
"""

import os
from typing import List, Dict, Any, Optional
from langchain_postgres import PGVector
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from .config import get_connection_string, EMBEDDING_MODEL

class VectorStore:
    # Khởi tạo kết nối đến PostgreSQL pgvector
    def __init__(self, collection_name: str = "edu_documents"):
        self.collection_name = collection_name
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        self.connection_string = get_connection_string()
        self._store = None
    
    # Lazy load PGVector store
    def _get_store(self) -> PGVector:
        if self._store is None:
            self._store = PGVector(
                collection_name=self.collection_name,
                connection=self.connection_string,
                embeddings=self.embeddings,
                use_jsonb=True
            )
        return self._store
    
    # Thêm chunks vào vector store
    def add_chunks(self, chunks: List[Dict[str, Any]]) -> List[str]:
        documents = []
        for chunk in chunks:
            doc = Document(
                page_content=chunk["text"],
                metadata={
                    "chunk_id": chunk.get("chunk_id"),
                    "source": chunk.get("source"),
                    "section": chunk.get("section"),
                    "order": chunk.get("order")
                }
            )
            documents.append(doc)
        
        store = self._get_store()
        ids = store.add_documents(documents)
        return ids
    
    # Tìm kiếm chunks tương tự với query
    def similarity_search(self, query: str, k: int = 5) -> List[Document]:
        store = self._get_store()
        results = store.similarity_search(query, k=k)
        return results
    
    # Tìm kiếm với điểm số similarity
    def similarity_search_with_score(self, query: str, k: int = 5) -> List[tuple]:
        store = self._get_store()
        results = store.similarity_search_with_score(query, k=k)
        return results

_vector_store_instance = None

# Lấy instance VectorStore (singleton pattern)
def get_vector_store(collection_name: str = "edu_documents") -> VectorStore:
    global _vector_store_instance
    if _vector_store_instance is None:
        _vector_store_instance = VectorStore(collection_name)
    return _vector_store_instance