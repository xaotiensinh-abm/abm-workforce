# HỒ SƠ THIẾT KẾ: Kiến trúc Đồng bộ Đa Thiết bị ABM
**Ngày:** 2026-03-29
**Người phụ trách:** Jarvis Trưởng Điều Phối
**Lựa chọn:** Phương án A — Phân Quyền Trị (Git + Cloud Drive Symlink)

## 1. Trữ lượng Dữ Liệu
Hệ sinh thái ABM hiện tại chạy bằng 2 não riêng rẽ:
- `ABM-Workforce` (Gắn bó hữu nghị với Codebase, có khả năng Revert lỗi cao) -> Dùng Git phân nhánh.
- `App Data (.gemini/antigravity)` (Sinh tồn trên hàng chục MB JSON lịch sử dạng Flat file lưu liên tục) -> Dùng Cloud Drive (iCloud/GDrive) để bảo tồn theo mốc thời gian thực.

## 2. Các Bước Triển Khai (Dự kiến)
1. **Thiết lập Nửa Codebase:**
   - Commit & đẩy tất cả thay đổi trên `/Users/dungtq/ABM-Workforce` lên Repo Github `xaotiensinh-abm/abm-workforce`.
   - Cài đặt `scripts/sync.sh` ở dưới máy thứ 2 lôi git về.
2. **Thiết lập Nửa Trí Nhớ (Antigravity):**
   - Di chuyển cứng gốc rễ thư mục `~/.gemini/antigravity` sang 1 ổ Cloud (ví dụ: `~/Library/Mobile Documents/com~apple~CloudDocs/Antigravity`).
   - Tạo Symlink (Luồng ảo) cắm từ `.gemini/antigravity` nối vào ổ Cloud trên.
   - Thao tác tương tự ở trên Máy MAC Phụ.
3. **Mô hình Khai Thác (Hoạt động):**
   - Code xong tính năng -> Sếp gõ `git push`.
   - Máy kia mở lên -> Gõ `git pull`.
   - Nhưng toàn bộ Chat History (brain) thì máy kia tự động có sẵn mà chẳng cần ấn bất cứ nút nào!

## 3. Quản trị Rủi Ro (Safety Check)
- Lúc Setup Symlink, TUYỆT ĐỐI ngắt tiến trình Antigravity để không bị lỗi Lock File. (Tức là Jarvis và hệ thống IDE sẽ phải tạm đóng trong vòng vài giây).

<!-- Phê chuẩn bởi CEO. Đã sẵn sàng nạp cho Writing-Plans -->
