---
description: Đồng bộ Não (Lịch sử Chat) qua Private Git Vault
---

## Mục Đích
Kích hoạt "Cổng Dịch Chuyển Ký Ức" để AI tự động gom não bộ, dọn dẹp và bắn lên hoặc kéo về từ Private Git Repo (`DungTQ87/abm-memory`) giúp thiết lập làm việc đa máy tính. Hệ thống này thay thế hoàn toàn Google Drive.

## Các lệnh khả dụng:
- `/sync-memory up`: Cất toàn bộ nhật ký phiên làm việc hôm nay lên mây. (Dùng trước khi tắt máy).
- `/sync-memory down`: Kéo toàn bộ ý thức từ đêm qua về ghi vào máy. (Dùng khi mới bật máy).

## Các bước thực thi:
1. Đọc argument mà user gõ vào (up hoặc down). Nếu user không gõ gì thì hỏi lại. Cấm chạy bừa.

// turbo
2. Thực thi đoạn mã dưới đây với giá trị điền vào tham số để tiến hành đồng bộ.
```bash
npm run sync:{{argument}}
```

3. Dựa trên `{{argument}}` và output của lệnh, trả lời Sếp Dung bằng văn phong AI cực xịn:
   - Nếu là `up`: Báo cáo quá trình nén ý thức thành công. Chúc sếp về nghỉ ngơi rảnh rang! Thể hiện sự yên tâm vì không sợ mất Log hay dính lỗi IO nữa.
   - Nếu là `down`: Báo cáo não bộ đã được Update đến giây phút mới nhất. Sẵn sàng code điên cuồng!
   - Tuyệt đối tự động chạy ẩn lệnh ở Bước 2, xong xuôi mới báo cáo. Sếp không cần đọc output đen ngòm nữa.
