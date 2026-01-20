"""
VectorStore module - Kết nối PostgreSQL với pgvector
"""

from typing import List, Dict, Any
from langchain_postgres import PGVector
from langchain_core.documents import Document
from .config import get_connection_string
from .embedder import get_embedder

class VectorStore:
    # Khởi tạo kết nối đến PostgreSQL pgvector
    def __init__(self, collection_name: str = "edu_documents"):
        self.collection_name = collection_name
        self.embeddings = get_embedder().client 
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
            keywords = chunk.get("keywords", [])
            keywords_str = ", ".join(keywords) if keywords else ""
            
            doc = Document(
                page_content=chunk["text"],
                metadata={
                    "chunk_id": chunk.get("chunk_id"),
                    "source": chunk.get("source", ""),
                    "section": chunk.get("section", ""),
                    "page": chunk.get("page", 1),
                    "keywords": keywords_str
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
    
    def hybrid_search(self, query: str, k: int = 5, keyword_boost: float = 0.3) -> List[tuple]:
        store = self._get_store()
        results = store.similarity_search_with_score(query, k=k*2)
        query_keywords = set(query.lower().split())
        
        reranked = []
        for doc, score in results:
            doc_keywords = doc.metadata.get("keywords", "").lower()
            keyword_matches = sum(1 for kw in query_keywords if kw in doc_keywords)
            
            # Tính điểm mới: score gốc + boost từ keyword
            boosted_score = score - (keyword_matches * keyword_boost)
            reranked.append((doc, boosted_score, keyword_matches))
        
        reranked.sort(key=lambda x: x[1])
        return [(doc, score) for doc, score, _ in reranked[:k]]

_vector_store_instance = None

# Lấy instance VectorStore (singleton pattern)
def get_vector_store(collection_name: str = "edu_documents") -> VectorStore:
    global _vector_store_instance
    if _vector_store_instance is None:
        _vector_store_instance = VectorStore(collection_name)
    return _vector_store_instance