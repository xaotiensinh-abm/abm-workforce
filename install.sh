#!/bin/bash

# ==============================================================================
# Trình Cài Đặt (Installer) ABM-Workforce Framework cho MacOS / Linux
# Tác Giả: DungTQ - Kiến Trúc Sư Đa Trí Tuệ (Jarvis)
# ==============================================================================

# Màu Sắc Đẹp Cho Terminal
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "    ___   ____  __  ___    _       __  ____   ____  __ __   ______   ____   ____   ______   _____"
echo "   /   | / __ )/  |/  /   | |     / / / __ \\ / __ \\/ //_/  / ____/  / __ \\ / __ \\ / ____/  / ___/"
echo "  / /| |/ __  / /|_/ /    | | /| / / / / / // /_/ / ,<    / /_     / / / // /_/ // /_     / __/  "
echo " / ___ / /_/ / /  / /     | |/ |/ / / /_/ // _, _/ /| |  / __/    / /_/ // _, _// __/    / /___  "
echo "/_/  |_\____/_/  /_/      |__/|__/  \____//_/ |_/_/ |_| /_/       \____//_/ |_|/_/      /_____/  "
echo "                                                                                                   "
echo -e "${NC}"

echo -e "${GREEN}Chào mừng ngài CEO đến với Tầng Lõi Hệ Thống 9 Lớp (ABM Framework).${NC}"
echo -e "${YELLOW}Hệ thống này sẽ giăng bẫy 119 Skills và Rule Base AI vào đúng cấu trúc Antigravity của sếp.${NC}"
echo ""

# Hỏi tên CEO
read -p "Sếp tên gì (Để mớm cung cho Jarvis gọi tên)? [Ví dụ: Dung TQ]: " CEO_NAME
if [ -z "$CEO_NAME" ]; then
    CEO_NAME="CEO"
fi

echo -e "\n⏳ Đang cào dữ liệu xương sống từ cục máy chủ Đám Mây Github..."

# Tải ZIP của Repo
curl -sL https://github.com/xaotiensinh-abm/abm-workforce/archive/refs/heads/main.zip -o abm-core.zip

# Giải nén âm thầm
unzip -q abm-core.zip

# Bốc 2 Cụm Lõi ra Project Hiện Tại
cp -r abm-workforce-main/.agents .
cp -r abm-workforce-main/_abm .
cp abm-workforce-main/docs/superpowers/rules.md _abm/RULES_GLOBAL.md 2>/dev/null || true

# Xóa Rác Tải Về
rm -rf abm-workforce-main abm-core.zip

# Bơm tên sếp vào Cấu Hình
CONFIG_FILE="_abm/bmm/config.yaml"
if [ -f "$CONFIG_FILE" ]; then
    # Dùng cú pháp tương thích Mac (sed -i '') và Linux
    sed -i.bak "s/user_name: .*/user_name: $CEO_NAME/" "$CONFIG_FILE"
    rm -f "${CONFIG_FILE}.bak"
fi

echo -e "\n${GREEN}🎉 TẤT CẢ HOÀN TẤT. KÍNH CHÀO ${CEO_NAME} TRƯỞNG QUẢN!${NC}"
echo -e "Trong VSCode / IDE, Sếp hãy gọi: ${CYAN}/jarvis${NC} hoặc ${CYAN}@[tên-skill]${NC} ra là chúng nó sẽ tuân theo lệnh nhé."
echo -e "Hãy Ủng Hộ Tác Giả Ly Cafe Cà Phê bằng cách quét QR Code trên README nhé! Cảm Ơn Sếp!"
