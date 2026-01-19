"""
Test RAG - Chat thử nghiệm với hệ thống RAG
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core.generator import get_generator

def main():
    print("[INFO] Khởi tạo hệ thống RAG...")
    generator = get_generator()
    print("[INFO] Sẵn sàng. Nhập 'exit' để thoát.\n")
    
    while True:
        query = input("Câu hỏi: ").strip()
        
        if query.lower() == "exit":
            print("[INFO] Tạm biệt!")
            break
        
        if not query:
            continue
        
        print("[INFO] Đang xử lý...")
        result = generator.generate(query)
        
        print(f"\nTrả lời: {result['answer']}\n")

if __name__ == "__main__":
    main()