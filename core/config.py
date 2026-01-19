"""
Config module - Cấu hình chung cho hệ thống RAG
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Database settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "edu_rag")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

# Embedding model
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "dangvantuan/vietnamese-embedding")

# LLM settings
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash-lite")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")

# Retrieval settings
TOP_K = int(os.getenv("TOP_K", "5"))

# Auth
PIN_CODE = os.getenv("PIN_CODE", "123456")

# Trả về connection string cho PostgreSQL
def get_connection_string() -> str:
    return f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"