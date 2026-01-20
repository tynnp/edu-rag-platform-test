# EDU RAG Platform Test - Frontend

Giao diện người dùng cho hệ thống hỏi đáp RAG.

## Công nghệ

- React 19
- Vite
- Tailwind CSS

## Cài đặt

```bash
npm install
```

## Chạy development

```bash
npm run dev
```

Truy cập: http://localhost:5173

## Build production

```bash
npm run build
```

Kết quả build: `dist/`

## Cấu trúc

```
src/
├── components/     # React components
├── pages/          # Các trang (PIN, Chat)
├── services/       # API calls
└── types/          # TypeScript types
```

## Biến môi trường

Tạo file `.env`:

```env
VITE_API_BASE_URL=http://localhost:8000/api
```

Khi deploy với Docker, giá trị sẽ là `/api` (Nginx proxy).