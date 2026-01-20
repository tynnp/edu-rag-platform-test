"""
Generator module - Sinh câu trả lời sử dụng LLM (Google Gemini)
"""

from google import genai
from typing import Dict, Any
from .retriever import get_retriever
from .config import LLM_MODEL, LLM_API_KEY

SYSTEM_PROMPT = """Bạn là trợ lý AI hỗ trợ trả lời câu hỏi về nội quy lớp học trực tuyến của Trường THPT Huỳnh Thúc Kháng.

Hướng dẫn:
1. Trả lời chính xác, ngắn gọn dựa trên ngữ cảnh được cung cấp.
2. Trích dẫn nguồn: "Theo [tên tài liệu], phần [section], mục [số], trang [page]."
3. Nếu câu hỏi về tiêu đề, mô tả chung hoặc lời kết thì không cần trích dẫn chi tiết.
4. Nếu không tìm thấy thông tin, trả lời: "Tôi không tìm thấy thông tin này trong tài liệu."
5. Trả lời bằng tiếng Việt, rõ ràng và dễ hiểu."""

class Generator:
    def __init__(self):
        self.client = genai.Client(api_key=LLM_API_KEY)
        self.model = LLM_MODEL
        self.retriever = get_retriever()
    
    def _build_prompt(self, query: str, context: str) -> str:
        return f"""{SYSTEM_PROMPT}

Ngữ cảnh:
{context}

Câu hỏi: {query}

Trả lời:"""
    
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
        
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )
            
            answer = response.text
            
        except Exception as e:
            answer = f"[Lỗi khi gọi API: {str(e)}]"
        
        return {
            "query": query,
            "answer": answer,
            "context": context,
            "chunks": chunks
        }
    
    def answer(self, query: str, k: int = None) -> str:
        result = self.generate(query, k)
        return result["answer"]

_generator_instance = None

def get_generator() -> Generator:
    global _generator_instance
    if _generator_instance is None:
        _generator_instance = Generator()
    return _generator_instance