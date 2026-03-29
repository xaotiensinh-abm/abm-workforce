# Hướng Dẫn Nối Ống Mạng Git (Topology) 
**Bảo toàn dữ liệu Cá Nhân (DungTQ87) vs Dữ liệu Lõi (xaotiensinh-abm)**

Để sở hữu một trạm trung chuyển Code Mượt Mà, sếp làm nốt 1 Lệnh này để Cắm cái Cống chính (`origin`) vào Repo Cá Nhân của sếp nhé!

1. Sếp lên Github bằng account `DungTQ87`, tạo 1 cái Repo mới trống trơn có tên là `my-abm-workforce` (Hay tên gì tùy sếp, nhớ để chế độ Private để không ai nhòm ngó file mật cá nhân).
2. Sếp dán (Paste) cái Link Repo đấy vào lệnh này để gõ vô Terminal:

```bash
git remote add origin https://github.com/DungTQ87/my-abm-workforce.git
```

## Chạy lệnh thường ngày (Sau khi cấy luồng xong)
Hệ thống mạng lưới Git của sếp giờ đây đã có Trí khôn 2 Chiều:

**A. Đưa file Cá nhân & Bài Giảng & Scripts lên Github (Chỉ mình dùng)**
```bash
git add .
git commit -m "update data cá nhân"
git push origin main
```
*Lệnh này sẽ tự bay về kho riêng `DungTQ87` của sếp.*

**B. Kéo tính năng Lõi (Core engine) từ Kho Công Cộng**
Lâu lâu sếp thấy Cộng đồng bảo `xaotiensinh-abm` mới có Skill mới ngon lắm, hay fix bug Antigravity gì đó. Sếp Hút Máu nó về bằng lệnh:
```bash
git pull upstream main --rebase
```
*Lệnh này sẽ tự lọc Code mới và đơm ngược vào máy tính sếp, trong khi vẫn giữ đồ cá nhân không bị đẩy đi lung tung.*
