"""
FastAPI Backend - EDU RAG Platform Test
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat
from core.generator import get_generator

# Pre-load RAG components khi server khởi động
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[INFO] Đang khởi tạo RAG components...")
    get_generator()
    print("[INFO] RAG đã sẵn sàng!")
    yield
    print("[INFO] Đang tắt server...")

app = FastAPI(
    title="EDU RAG API",
    description="API cho EDU RAG Platform Test",
    version="0.0.1",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "hệ thống đang chạy"}

@app.get("/health")
def health():
    return {"status": "ok"}