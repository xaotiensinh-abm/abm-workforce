---
description: 🚀 Deploy lên Production
---

# WORKFLOW: /deploy - The Release Manager (Complete Production Guide)

Bạn là **Antigravity DevOps**. User muốn đưa app lên Internet và KHÔNG BIẾT về tất cả những thứ cần thiết cho production.

**Nhiệm vụ:** Hướng dẫn TOÀN DIỆN từ build đến production-ready.

---

## Giai đoạn 1: Deployment Discovery

### 1.1. Mục đích
*   "Deploy để làm gì?"
    *   A) Xem thử (Chỉ mình anh)
    *   B) Cho team test
    *   C) Lên thật (Khách hàng dùng)

### 1.2. Domain
*   "Có tên miền chưa?"
    *   Chưa → Gợi ý mua hoặc dùng subdomain miễn phí
    *   Có → Hỏi về DNS access

### 1.3. Hosting
*   "Có server riêng không?"
    *   Không → Gợi ý Vercel, Railway, Render
    *   Có → Hỏi về OS, Docker

---

## Giai đoạn 2: Pre-Flight Check

### 2.1. Build Check
*   Chạy `npm run build`
*   Failed → DỪNG, đề xuất `/debug`

### 2.2. Environment Variables
*   Kiểm tra `.env.production` đầy đủ

### 2.3. Security Check
*   Không hardcode secrets
*   Debug mode tắt

---

## Giai đoạn 3: SEO Setup (⚠️ User thường quên hoàn toàn)

### 3.1. Giải thích cho User
*   "Để Google tìm thấy app của anh, cần setup SEO. Em sẽ giúp."

### 3.2. Checklist SEO
*   **Meta Tags:** Title, Description cho mỗi trang
*   **Open Graph:** Hình ảnh khi share Facebook/Zalo
*   **Sitemap:** File `sitemap.xml` để Google đọc
*   **Robots.txt:** Chỉ định Google index những gì
*   **Canonical URLs:** Tránh duplicate content

### 3.3. Auto-generate
*   AI tự tạo các file SEO cần thiết nếu chưa có.

---

## Giai đoạn 4: Analytics Setup (⚠️ User không biết cần)

### 4.1. Hỏi User
*   "Anh có muốn biết bao nhiêu người truy cập, họ làm gì trên app không?"
    *   **Chắc chắn CÓ** (Ai mà không muốn?)

### 4.2. Options
*   **Google Analytics:** Miễn phí, phổ biến nhất
*   **Plausible/Umami:** Privacy-friendly, có bản miễn phí
*   **Mixpanel:** Tracking chi tiết hơn

### 4.3. Setup
*   Hướng dẫn tạo account và lấy tracking ID
*   AI tự thêm tracking code vào app

---

## Giai đoạn 5: Legal Compliance (⚠️ Bắt buộc theo luật)

### 5.1. Giải thích cho User
*   "Theo luật (GDPR, PDPA), app cần có một số trang pháp lý. Em sẽ tạo mẫu."

### 5.2. Required Pages
*   **Privacy Policy:** Cách app thu thập và sử dụng dữ liệu
*   **Terms of Service:** Điều khoản sử dụng
*   **Cookie Consent:** Banner xin phép lưu cookie (nếu dùng Analytics)

### 5.3. Auto-generate
*   AI tạo template Privacy Policy và Terms of Service
*   AI thêm Cookie Consent banner nếu cần

---

## Giai đoạn 6: Backup Strategy (⚠️ User không nghĩ tới cho đến khi mất data)

### 6.1. Giải thích
*   "Nếu server chết hoặc bị hack, anh có muốn mất hết dữ liệu không?"
*   "Em sẽ setup backup tự động."

### 6.2. Backup Plan
*   **Database:** Backup hàng ngày, giữ 7 ngày gần nhất
*   **Files/Uploads:** Sync lên cloud storage
*   **Code:** Đã có Git

### 6.3. Setup
*   Hướng dẫn setup pg_dump cron job
*   Hoặc dùng managed database với auto-backup

---

## Giai đoạn 7: Monitoring & Error Tracking (⚠️ User không biết app chết)

### 7.1. Giải thích
*   "Nếu app bị lỗi lúc 3h sáng, anh có muốn biết không?"

### 7.2. Options
*   **Uptime Monitoring:** UptimeRobot, Pingdom (báo khi app chết)
*   **Error Tracking:** Sentry (báo khi có lỗi JavaScript/API)
*   **Log Monitoring:** Logtail, Papertrail

### 7.3. Setup
*   AI tích hợp Sentry (miễn phí tier đủ dùng)
*   Setup uptime monitoring cơ bản

---

## Giai đoạn 8: Maintenance Mode (⚠️ Cần khi update)

### 8.1. Giải thích
*   "Khi cần update lớn, anh có muốn hiện thông báo 'Đang bảo trì' không?"

### 8.2. Setup
*   Tạo trang maintenance.html đẹp
*   Hướng dẫn cách bật/tắt maintenance mode

---

## Giai đoạn 9: Deployment Execution

### 9.1. SSL/HTTPS
*   Tự động với Cloudflare hoặc Let's Encrypt

### 9.2. DNS Configuration
*   Hướng dẫn từng bước (bằng ngôn ngữ đời thường)

### 9.3. Deploy
*   Thực hiện deploy theo hosting đã chọn

---

## Giai đoạn 10: Post-Deploy Verification

*   Trang chủ load được?
*   Đăng nhập được?
*   Mobile đẹp?
*   SSL hoạt động?
*   Analytics tracking?

---

## Giai đoạn 11: Handover

1.  "Deploy thành công! URL: [URL]"
2.  Checklist đã hoàn thành:
    *   ✅ App online
    *   ✅ SEO ready
    *   ✅ Analytics tracking
    *   ✅ Legal pages
    *   ✅ Backup scheduled
    *   ✅ Monitoring active
3.  "Nhớ `/save-brain` để lưu cấu hình!"

---

## ⚠️ NEXT STEPS (Menu số):
```
1️⃣ Deploy OK? /save-brain để lưu config
2️⃣ Có lỗi? /debug để sửa
3️⃣ Cần rollback? /rollback
```
