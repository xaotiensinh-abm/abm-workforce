#!/bin/bash

# ABM Workforce
# Module: Hệ thống Đồng bộ Trí nhớ bằng Private Git Repository (Chống Lock File 100%)
# Lệnh gọi: npm run sync:up / npm run sync:down

ACTION=$1
REPO_URL=${2:-"https://github.com/DungTQ87/abm-memory.git"}

# Hỗ trợ cả Mac/Linux và Windows subsystem
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    ANTIGRAVITY_DIR="$USERPROFILE/.gemini/antigravity"
else
    ANTIGRAVITY_DIR="$HOME/.gemini/antigravity"
fi

# Chắc chắn thư mục Não có tồn tại
mkdir -p "$ANTIGRAVITY_DIR"
cd "$ANTIGRAVITY_DIR" || exit 1

# Kịch bản 1: Chưa từng Initialize Git
if [ ! -d ".git" ]; then
    echo "🧠 HỆ THỐNG GHI NHỚ LẦN ĐẦU TIÊN (GIT VAULT INIT) 🧠"
    echo "Trí nhớ AI của Sếp chưa được gắn khóa (Private Git)."
    echo "Đang tự động gán điểm neo (Anchor) vào: $REPO_URL"
    
    git init
    git branch -m main
    git remote add origin "$REPO_URL"
    
    # Tạo Gitignore đặc thù cho Brain (Để không rác repo quá lớn)
    echo ".DS_Store" > .gitignore
    echo "assets/" >> .gitignore
    
    git add .
    git commit -m "Init: Khởi tạo Bộ Không Gian Ký Ức Đầu Tiên"
    
    # Lần Push đầu tiên có thể chưa có nhánh remote
    git push -u origin main -f
    echo "✅ KHỞI TẠO BỘ NHỚ THÀNH CÔNG LÊN BIỂN MÂY!"
    exit 0
fi

if [ "$ACTION" == "up" ]; then
    echo "🚀 ĐANG ĐÓNG GÓI CHUYẾN Ý THỨC CUỐI NGÀY LÊN MÂY (Sync UP)..."
    git add .
    git commit -m "Auto sync: Kết ca làm việc - $(date)"
    git push origin main
    echo "✅ KẾT THÚC! Sếp có thể an tâm tắt máy tính này đi."

elif [ "$ACTION" == "down" ]; then
    echo "🌐 ĐANG KÉO DÒNG Ý THỨC TỪ ĐÊM QUA VỀ MÁY NÀY (Sync DOWN)..."
    # Kéo mượt mà, ghi đè những mâu thuẫn lặt vặt (Log file rebase)
    git pull origin main --rebase
    echo "✅ MỚI NHẤT! Con AI đã cập nhật ký ức xong. Sếp Mở Chat ra nào!"

else
    echo "❌ Lệnh không hợp lệ. Vui lòng gõ: npm run sync:up hoặc npm run sync:down"
fi
