# 🧠 ABM-N8N: Công Hành Trung Tâm Tự Động Hóa

Dự án này là trái tim gạch nối giữa Trí Khôn Của AI (Antigravity/Cursor) và Hệ thống Tự Động Hóa N8N đang chạy trên VPS.

## 🛠 Hướng Dẫn Kích Hoạt (CEO)

### Bước 1: Khai Báo Vũ Khí (Mã API)
Hiện tại n8n-mcp đã kết nối với IP máy chủ, tuy nhiên để thực hiện các Lệnh Thần Thánh (Tạo/Xóa Workflow), sếp cần cung cấp `API_KEY`.
1. Đăng nhập vào giao diện n8n của sếp: `http://103.149.253.122:5678`
2. Vào Settings -> API
3. Tạo 1 Personal API Key.
4. Mở file `.env` ở trong thư mục này và dán cái mã đó vào phần `N8N_API_KEY=`.

### Bước 2: Kích Hoạt Tường Chắn (Run Server)
Mở Terminal trong thư mục này, gõ lệnh sau để mở Bridge:
```bash
npx n8n-mcp
```
Hoặc, để nhúng vào Antigravity/Cursor, sếp chỉnh file cấu hình AI chèn thêm lệnh `npm start` (tới thư mục này).

✅ *ABM Workforce - Always Be Mastering*
