#!/bin/bash

# Lay thu muc hien tai cua script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGES_DIR="$SCRIPT_DIR"

# Mau sac
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

show_help() {
    echo ""
    echo "EDU RAG Platform - Deploy Script"
    echo "================================="
    echo ""
    echo "Su dung: ./deploy.sh [lenh]"
    echo ""
    echo "Cac lenh:"
    echo "  load    - Load Docker images tu file .tar"
    echo "  up      - Khoi dong tat ca containers"
    echo "  down    - Dung tat ca containers"
    echo "  restart - Khoi dong lai tat ca containers"
    echo "  logs    - Xem logs cua tat ca containers"
    echo "  status  - Xem trang thai containers"
    echo "  clean   - Xoa tat ca images va containers khong su dung"
    echo ""
}

load_images() {
    echo -e "${YELLOW}[*] Dang load Docker images...${NC}"
    
    if [ -f "$IMAGES_DIR/edu-rag-backend.tar" ]; then
        echo "Loading backend image..."
        docker load -i "$IMAGES_DIR/edu-rag-backend.tar"
    else
        echo -e "${RED}[!] Khong tim thay: $IMAGES_DIR/edu-rag-backend.tar${NC}"
    fi
    
    if [ -f "$IMAGES_DIR/edu-rag-frontend.tar" ]; then
        echo "Loading frontend image..."
        docker load -i "$IMAGES_DIR/edu-rag-frontend.tar"
    else
        echo -e "${RED}[!] Khong tim thay: $IMAGES_DIR/edu-rag-frontend.tar${NC}"
    fi
    
    echo -e "${GREEN}[+] Hoan thanh load images!${NC}"
}

up_containers() {
    echo -e "${YELLOW}[*] Dang khoi dong containers...${NC}"
    cd "$SCRIPT_DIR"
    docker-compose up -d
    echo -e "${GREEN}[+] Containers da khoi dong!${NC}"
    docker-compose ps
}

down_containers() {
    echo -e "${YELLOW}[*] Dang dung containers...${NC}"
    cd "$SCRIPT_DIR"
    docker-compose down
    echo -e "${GREEN}[+] Containers da dung!${NC}"
}

restart_containers() {
    echo -e "${YELLOW}[*] Dang khoi dong lai containers...${NC}"
    cd "$SCRIPT_DIR"
    docker-compose restart
    echo -e "${GREEN}[+] Containers da khoi dong lai!${NC}"
    docker-compose ps
}

show_logs() {
    cd "$SCRIPT_DIR"
    docker-compose logs -f
}

show_status() {
    cd "$SCRIPT_DIR"
    echo ""
    echo "=== Container Status ==="
    docker-compose ps
    echo ""
    echo "=== Docker Images ==="
    docker images | grep edu-rag
    echo ""
}

clean_all() {
    echo -e "${YELLOW}[*] Dang don dep...${NC}"
    cd "$SCRIPT_DIR"
    docker-compose down --rmi all --volumes --remove-orphans
    docker system prune -af
    echo -e "${GREEN}[+] Da don dep xong!${NC}"
}

# Main
cd "$SCRIPT_DIR"

case "$1" in
    load)
        load_images
        ;;
    up)
        up_containers
        ;;
    down)
        down_containers
        ;;
    restart)
        restart_containers
        ;;
    logs)
        show_logs
        ;;
    status)
        show_status
        ;;
    clean)
        clean_all
        ;;
    *)
        show_help
        ;;
esac