FROM node:18-alpine as build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN echo "VITE_API_BASE_URL=/api" > .env.production
RUN npm run build

# Serve bằng Nginx
FROM nginx:alpine

# Copy kết quả build vào thư mục serve của Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copy cấu hình Nginx tùy chỉnh
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]