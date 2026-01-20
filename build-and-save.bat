@echo off
echo ========================================
echo   EDU RAG Platform - Build Docker Images
echo ========================================
echo.

REM Tao thu muc docker-images neu chua ton tai
if not exist "docker-images" mkdir docker-images

echo [1/4] Building backend image...
docker build -t edu-rag-backend:latest -f Dockerfile.backend .
if %errorlevel% neq 0 (
    echo Loi: Khong the build backend image!
    exit /b 1
)

echo [2/4] Building frontend image...
docker build -t edu-rag-frontend:latest -f frontend/Dockerfile frontend
if %errorlevel% neq 0 (
    echo Loi: Khong the build frontend image!
    exit /b 1
)

echo [3/4] Saving backend image...
docker save edu-rag-backend:latest -o docker-images/edu-rag-backend.tar
if %errorlevel% neq 0 (
    echo Loi: Khong the save backend image!
    exit /b 1
)

echo [4/4] Saving frontend image...
docker save edu-rag-frontend:latest -o docker-images/edu-rag-frontend.tar
if %errorlevel% neq 0 (
    echo Loi: Khong the save frontend image!
    exit /b 1
)

echo.
echo ========================================
echo   Hoan thanh!
echo ========================================
echo.

REM Copy .env file neu ton tai
if exist ".env" (
    copy .env docker-images\.env >nul
    echo File .env da duoc copy vao docker-images/
)

REM Copy deploy.sh file neu ton tai
if exist "deploy.sh" (
    copy deploy.sh docker-images\deploy.sh >nul
    echo File deploy.sh da duoc copy vao docker-images/
)

REM Copy docker-compose.images.yml file (dung cho manual deploy)
if exist "docker-compose.images.yml" (
    copy docker-compose.images.yml docker-images\docker-compose.yml >nul
    echo File docker-compose.yml da duoc copy vao docker-images/
)

echo.
echo Cac file da duoc luu tai:
echo   - docker-images/edu-rag-backend.tar
echo   - docker-images/edu-rag-frontend.tar
echo   - docker-images/.env
echo   - docker-images/deploy.sh
echo   - docker-images/docker-compose.yml
echo.
echo Copy thu muc docker-images len server va chay:
echo   chmod +x deploy.sh
echo   ./deploy.sh load
echo   ./deploy.sh up
echo.