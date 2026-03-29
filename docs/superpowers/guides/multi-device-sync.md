# HƯỚNG DẪN ĐỒNG BỘ ĐA THIẾT BỊ 
**Dành riêng cho Hệ sinh thái ABM Workforce & Antigravity IDE**

Quy trình này áp dụng tư duy "Trị phân quyền": Source Code lưu trên Github để phiên bản hóa, và Dữ liệu Cấu Hình ẩn (Trí khôn Antigravity) cắm trên bộ Cloud Drive chung (GDrive/iCloud).

## 🚀 Tính năng nổi bật
- Mở máy thứ 2 lên: Mọi logic Chatbot, Logs, Skills đều được chuyển sinh mượt mà.
- Tránh bị đầy rác JSON History trên kho Git của Github.
- Cực kỳ bảo mật và dễ quản trị (Tự động hóa hoàn toàn bằng 1 script duy nhất).

---

## Bước 1: Khởi động cỗ máy chủ lực (Tại Macbook 1)
Bước này dùng để đóng gói Bộ Não đang thông minh sẵn của sếp trên Macbook chính, cất lên Mây.

1. **Cam kết Code:** `git add .`, sau đó `git commit -m "chore: push before sync"` và `git push`. (Hãy chắc chắn tài liệu, folder `ABM-Workforce` đã vứt hết lên Repository Cloud Github).
2. **Kích hoạt Script Đồng bộ Thần Kinh:**
   - **Nếu máy 1 là Macbook:** Mở iTerm/Terminal tại thư mục Workspace ABM:
     ```bash
     chmod +x scripts/setup-sync.sh
     ./scripts/setup-sync.sh
     ```
   - **Nếu máy 1 là Windows:** Mở PowerShell bằng quyền Quản trị (Run as Administrator) tại thư mục Workspace ABM:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     .\scripts\setup-sync.ps1
     ```
3. Cứ cắm đường dẫn tới thư mục Cloud Drive (Ví dụ: `~/Google Drive/My Drive` đối với Mac, hoặc `G:\My Drive` đối với Windows) của sếp vào khi có bảng hỏi hiện lên.
4. Đợi tầm 15s cho mây đồng bộ dữ liệu não `.gemini/antigravity` (hoặc `%USERPROFILE%\.gemini\antigravity`) vừa được bưng lên.

---

## Bước 2: Gọi Hồn Tại Phiên Bản Clone (Tại Macbook 2 Mới)
1. Cài đặt các IDE, Docker Desktop y chang máy gốc. (Git clone repo `ABM-Workforce` từ Github về đúng chỗ `~/ABM-Workforce`).
2. Tương tự như trên, mở màn hình lệnh (iTerm cho Mac / PowerShell As Admin cho Windows) ở thư mục `ABM-Workforce` và chạy:
   - **Macbook:** `./scripts/setup-sync.sh`
   - **Windows:** `.\scripts\setup-sync.ps1`
3. Khai báo cái đường dẫn Cloud Gốc đúng y chang ở Bước 1. (Chú ý đảm bảo Google Drive ở Máy 2 đã Download sạch đống Cache bộ não `antigravity-brain` về máy rồi nhé sếp).
4. File script tự động phân tích Máy 2 chưa có não -> Tạo 1 cầu nối ảo (Symlink/Junction) nhét ngược vào trí nhớ cục bộ của hệ điều hành.

---

## Bước 3: Lệnh Khởi Khách Thường Ngày
Từ giờ về sau, công việc của sếp ở Máy 1 hay Máy 2 chỉ gồm:

1. **Mở máy/Bắt đầu ca làm:**
   ```bash
   git pull origin main
   ```
2. Mở thư mục IDE lên và hưởng thụ vì toàn bộ Trí Nhớ Phiên Làm Việc (Conversation History, Tasks) đã tự cào từ iCloud sang.
3. **Đóng máy/Kết ca:**
   ```bash
   git add .
   git commit -m "Auto sync: Kết ca"
   git push origin main
   ```

> Tuân thủ tuyệt đối quy trình trên để tránh "Rối loạn Ý thức Song song" (Ví dụ: Cùng bật Antigravity ở cả 2 máy một lúc sẽ gây lock file sinh đụng độ).
