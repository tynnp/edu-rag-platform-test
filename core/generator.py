"""
Generator module - Sinh câu trả lời sử dụng LLM
"""

import google.generativeai as genai
from typing import List, Dict, Any
from .retriever import get_retriever
from .config import LLM_MODEL, LLM_API_KEY

SYSTEM_PROMPT = """Bạn là trợ lý AI hỗ trợ trả lời câu hỏi về nội quy lớp học trực tuyến.
Dựa vào ngữ cảnh được cung cấp, hãy trả lời câu hỏi một cách chính xác và ngắn gọn.
Khi trả lời, hãy chỉ rõ thông tin đến từ phần nào (ví dụ: "Theo tài liệu ... phần I. Đối với học sinh, mục 3...").
Nếu không tìm thấy thông tin trong ngữ cảnh, hãy nói rằng bạn không có thông tin về vấn đề đó.
Trả lời bằng tiếng Việt."""

class Generator:
    # Khởi tạo generator với LLM
    def __init__(self):
        genai.configure(api_key=LLM_API_KEY)
        self.model = genai.GenerativeModel(LLM_MODEL)
        self.retriever = get_retriever()
    
    # Tạo prompt với context và câu hỏi
    def _build_prompt(self, query: str, context: str) -> str:
        return f"""{SYSTEM_PROMPT}

Ngữ cảnh:
{context}

Câu hỏi: {query}

Trả lời:"""
    
    # Sinh câu trả lời cho câu hỏi
    def generate(self, query: str, k: int = None, debug: bool = True) -> Dict[str, Any]:
        chunks = self.retriever.retrieve(query, k)
        
        if debug:
            print(f"[DEBUG] Tìm thấy {len(chunks)} chunks liên quan:")
            for i, chunk in enumerate(chunks, 1):
                section = chunk["metadata"].get("section", "N/A")
                score = chunk["score"]
                text_preview = chunk["text"][:80].replace("\n", " ")
                print(f"[{i}] [score: {score:.4f}] {section},  {text_preview}...")
        
        context = self.retriever.get_context(query, k)
        prompt = self._build_prompt(query, context)
        response = self.model.generate_content(prompt)
        
        return {
            "query": query,
            "answer": response.text,
            "context": context,
            "chunks": chunks
        }
    
    # Sinh câu trả lời (chỉ trả về text)
    def answer(self, query: str, k: int = None) -> str:
        result = self.generate(query, k)
        return result["answer"]

_generator_instance = None

# Lấy instance Generator (singleton pattern)
def get_generator() -> Generator:
    global _generator_instance
    if _generator_instance is None:
        _generator_instance = Generator()
    return _generator_instance