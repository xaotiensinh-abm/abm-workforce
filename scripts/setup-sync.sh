#!/bin/bash

# ABM Workforce
# Kịch bản đồng bộ não bộ Antigravity IDE (Trí Nhớ) lên Cloud Drive

echo "================================================="
echo "🧠 THIẾT LẬP ĐỒNG BỘ NGUYÊN KHỐI ANTIGRAVITY IDE "
echo "================================================="
echo ""

# Đường dẫn mặc định
ANTIGRAVITY_DIR="$HOME/.gemini/antigravity"

# Nếu chạy ở Mac 1 (Chưa Sync) -> Chuyển data lên Cloud
# Nếu chạy ở Mac 2 (Đã Sync) -> Chỉ cắm Symlink về Cloud

echo "Nhập đường dẫn thư mục Cloud Drive dùng để đồng bộ gốc của sếp:"
echo "(Ví dụ: /Users/dungtq/Library/Mobile Documents/com~apple~CloudDocs/ABM-Cloud hoặc /Users/dungtq/Google Drive/My Drive)"
read -p "Đường dẫn Cloud: " CLOUD_DIR

if [ -z "$CLOUD_DIR" ]; then
    echo "❌ Hủy. Vui lòng cung cấp đường dẫn Cloud Drive hợp lệ."
    exit 1
fi

# Chắc chắn Cloud Directory tồn tại
mkdir -p "$CLOUD_DIR"

DEST_DIR="$CLOUD_DIR/antigravity-brain"

echo "Đang xử lý thiết lập..."

# Case 1: Thư mục gốc Antigravity tồn tại dưới dạng thư mục tĩnh (chưa Symlink)
if [ -d "$ANTIGRAVITY_DIR" ] && [ ! -L "$ANTIGRAVITY_DIR" ]; then
    echo "🔍 Phát hiện thư mục gốc Antigravity IDE chưa được đồng bộ."
    
    # Kiểm tra xem trên Cloud đã có dữ liệu chưa (Để hỏi merge/ghi đè)
    if [ -d "$DEST_DIR" ]; then
        echo "⚠️ TRÊN MÂY ĐÃ TỒN TẠI BỘ NÃO ANTIGRAVITY KHÁC"
        echo "Bạn muốn ghi đè bộ não cũ trên máy này, hay hợp nhất?"
        echo "Nhấn Ctrl+C để hủy nếu sợ mất dữ liệu. Sript sẽ tự dời thư mục gốc thành .gemini/antigravity.bak"
        sleep 3
        mv "$ANTIGRAVITY_DIR" "${ANTIGRAVITY_DIR}.bak"
        echo "Đã backup não bộ cũ trên máy thành antigravity.bak"
    else
        echo "🚀 Đang bê toàn bộ Trí nhớ (Log/Knowledge) đưa lên Cloud Mây ($DEST_DIR)..."
        mv "$ANTIGRAVITY_DIR" "$DEST_DIR"
    fi
    
    echo "🔗 Đang tạo luồng (Symlink) từ mây về lại máy tại $ANTIGRAVITY_DIR ..."
    ln -s "$DEST_DIR" "$ANTIGRAVITY_DIR"
    echo "✅ XONG MÁY 1! Toàn bộ lịch sử chat và trí khôn đã bắt đầu được Cloud Drive Upload lên mạng."

# Case 2: Nếu chưa có thư mục Antigravity trên máy (Macbook thứ 2 mới mua/cài)
elif [ ! -d "$ANTIGRAVITY_DIR" ]; then
    echo "🔍 Phát hiện máy thứ 2 (hoặc chưa khởi tạo Antigravity)."
    
    if [ ! -d "$DEST_DIR" ]; then
        echo "❌ LỖI: Trên $DEST_DIR chưa có dữ liệu não bộ. Hãy chạy kịch bản này ở máy chủ (Máy Số 1) trước, chờ iCloud Upload xong rồi chạy máy số 2 nhé sếp!"
        exit 1
    fi
    
    echo "🔗 Khởi tạo luồng thần kinh (Symlink) từ mây nối vào não Macbook này..."
    ln -s "$DEST_DIR" "$ANTIGRAVITY_DIR"
    echo "✅ XONG MÁY 2! Sếp có thể mở IDE, dữ liệu phiên trước đã được khôi phục thành công 100%!"

# Case 3: Đã là Symlink (Đã thiết lập rồi)
elif [ -L "$ANTIGRAVITY_DIR" ]; then
    echo "✅ Máy này đã được setup đồng bộ mây thành công rồi sếp ơi (Symlink đã tồn tại)!"
fi

echo ""
echo "================================================="
echo "🎉 Tất cả hoàn thành. Hợp Đồng Sync Đa Thiết Bị Ký Kết Thành Công!"
