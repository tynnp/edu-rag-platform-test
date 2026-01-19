"""
Ingest module - Import chunks vào PostgreSQL pgvector
"""

import os
import json
import glob
from .vector_store import get_vector_store

CHUNKS_DIR = "data/chunks"

# Đọc tất cả chunk files từ thư mục
def load_chunks_from_files(chunks_dir: str = CHUNKS_DIR):
    chunks = []
    pattern = os.path.join(chunks_dir, "chunk-*.json")
    files = sorted(glob.glob(pattern), key=lambda x: int(x.split("chunk-")[1].split(".json")[0]))
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            chunk = json.load(f)
            chunks.append(chunk)
    
    return chunks

# Import chunks vào vector store
def ingest_chunks(chunks_dir: str = CHUNKS_DIR):
    chunks = load_chunks_from_files(chunks_dir)
    vector_store = get_vector_store()
    ids = vector_store.add_chunks(chunks)
    return ids

# Main function (khi chạy trực tiếp)
def main():
    print(f"[INFO] Đang tải chunks từ {CHUNKS_DIR}")
    chunks = load_chunks_from_files(CHUNKS_DIR)
    print(f"[INFO] Đã tải {len(chunks)} chunks từ {CHUNKS_DIR}")
    
    confirm = input("[CONFIRM] Import vào database? (y/n): ")
    if confirm.lower() != "y":
        print("[INFO] Đã hủy")
        return
    
    print("[INFO] Đang import vào PostgreSQL pgvector...")
    vector_store = get_vector_store()
    ids = vector_store.add_chunks(chunks)
    print(f"[INFO] Hoàn thành. Đã import {len(ids)} chunks")

if __name__ == "__main__":
    main()