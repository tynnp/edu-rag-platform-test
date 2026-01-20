<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=40&pause=1000&color=6366F1&center=true&vCenter=true&width=500&lines=EDU+RAG+Platform+Test)](https://git.io/typing-svg)

<img src="https://img.shields.io/badge/version-0.0.1-blue?style=for-the-badge" alt="Version" />
<img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License" />
<img src="https://img.shields.io/badge/status-Active-success?style=for-the-badge" alt="Status" />

<br/>

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**Hệ thống hỏi đáp thông minh sử dụng RAG (Retrieval-Augmented Generation) cho nội quy lớp học trực tuyến.**

</div>

---

## Giới thiệu

EDU RAG Platform Test là hệ thống chatbot thử nghiệm, sử dụng kỹ thuật RAG để trả lời các câu hỏi liên quan đến nội quy lớp học trực tuyến. Hệ thống kết hợp:

- **Retrieval**: Tìm kiếm ngữ nghĩa trong cơ sở dữ liệu vector (pgvector).
- **Augmented Generation**: Sử dụng Google Gemini để sinh câu trả lời dựa trên ngữ cảnh.

---

## Cấu trúc thư mục

```
edu-rag-platform-test/
├── backend/                 # API Backend (FastAPI)
│   ├── routes/              # Định nghĩa các endpoint
│   │   ├── auth.py          # Xác thực PIN
│   │   └── chat.py          # Chat API
│   ├── tests/               # Unit tests cho backend
│   ├── main.py              # Entry point
│   └── schemas.py           # Pydantic schemas
│
├── core/                    # RAG Core Logic
│   ├── tests/               # Unit tests cho core
│   ├── config.py            # Cấu hình từ .env
│   ├── embedder.py          # Tạo embeddings
│   ├── generator.py         # Sinh câu trả lời (LLM)
│   ├── ingest.py            # Nạp dữ liệu vào vector store
│   ├── retriever.py         # Truy xuất ngữ cảnh
│   └── vector_store.py      # Kết nối pgvector
│
├── data/                    # Dữ liệu
│   ├── chunks/              # Các đoạn văn bản đã chia
│   ├── processed/           # Văn bản đã xử lý
│   └── raw/                 # Dữ liệu gốc
│
├── frontend/                # Giao diện (React + Vite)
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Các trang (PIN, Chat)
│   │   ├── services/        # API calls
│   │   └── types/           # TypeScript types
│   ├── Dockerfile           # Build frontend image
│   └── nginx.conf           # Cấu hình Nginx
│
├── .github/workflows/       # GitHub Actions
│   └── deploy.yml           # Auto deploy khi push tag
│
├── Dockerfile.backend       # Build backend image
├── docker-compose.yml       # Docker Compose config
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── .env                     # Biến môi trường (không commit)
```

---

## Yêu cầu

### Chạy local

- Python 3.11+
- Node.js 18+
- PostgreSQL với extension pgvector

### Chạy với Docker

- Docker 20.10+
- Docker Compose 1.29+

---

## Cài đặt

### Chạy local

1. Clone repository:

```bash
git clone https://github.com/tynnp/edu-rag-platform-test.git
cd edu-rag-platform-test
```

2. Tạo file `.env` ở thư mục gốc:

```env
# Database
DB_HOST=your_db_host
DB_PORT=5432
DB_NAME=edu_rag
DB_USER=your_user
DB_PASSWORD=your_password

# Embedding
EMBEDDING_MODEL=dangvantuan/vietnamese-embedding

# LLM
LLM_MODEL=gemini-3-flash-preview
LLM_API_KEY=your_gemini_api_key

# Retrieval
TOP_K=5

# Auth
PIN_CODE=123456
```

3. Cài đặt và chạy Backend:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

4. Cài đặt và chạy Frontend:

```bash
cd frontend
npm install
npm run dev
```

5. Truy cập `http://localhost:5173` và nhập PIN để sử dụng.

---

### Chạy với Docker

1. Clone repository:

```bash
git clone https://github.com/tynnp/edu-rag-platform-test.git
cd edu-rag-platform-test
```

2. Tạo file `.env` ở thư mục gốc (xem mẫu ở trên).

3. Build và chạy:

```bash
docker-compose up -d --build
```

4. Truy cập `http://localhost:3508` và nhập PIN để sử dụng.

---

## Cấu hình

| Biến môi trường | Mô tả |
|-----------------|-------|
| `DB_HOST` | Địa chỉ PostgreSQL server |
| `DB_PORT` | Cổng PostgreSQL |
| `DB_NAME` | Tên database |
| `DB_USER` | Tên người dùng database |
| `DB_PASSWORD` | Mật khẩu database |
| `EMBEDDING_MODEL` | Model embedding (mặc định: dangvantuan/vietnamese-embedding) |
| `LLM_MODEL` | Model LLM (mặc định: gemini-3-flash-preview) |
| `LLM_API_KEY` | API Key của Google Gemini |
| `TOP_K` | Số lượng chunks truy xuất (mặc định: 5) |
| `PIN_CODE` | Mã PIN để truy cập hệ thống |

---

## Triển khai (Deploy)

Hệ thống hỗ trợ tự động deploy qua GitHub Actions khi push tag.

### Cấu hình GitHub Secrets

Vào `Settings > Secrets and variables > Actions` của repository và thêm:

| Secret | Mô tả |
|--------|-------|
| `SSH_HOST` | IP của server |
| `SSH_USER` | Username SSH (vd: root) |
| `SSH_PASSWORD` | Mật khẩu SSH |
| `SSH_PORT` | Cổng SSH (vd: 22) |
| `ENV_FILE` | Toàn bộ nội dung file .env |

### Triển khai

```bash
git tag v1.0.0
git push origin v1.0.0
```

Workflow sẽ tự động:
1. Copy source code lên server.
2. Tạo file .env từ secret.
3. Chạy docker-compose để build và khởi động container.

---

<div align="center">

<img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT License" />

<br/>

Dự án này được phát hành theo giấy phép **MIT License**
