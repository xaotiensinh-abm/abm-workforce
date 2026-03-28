---
description: 🌐 Quản lý Cloudflare Tunnel
---

# Cloudflare Tunnel Configuration

## ⚠️ QUAN TRỌNG - ĐỌC TRƯỚC KHI THAY ĐỔI

Hệ thống sử dụng **MỘT tunnel duy nhất** cho nhiều services. KHÔNG tạo tunnel mới, chỉ thêm hostname vào config hiện có.

---

## 📋 Hiện Trạng (Cập nhật: 2026-01-13)

### Tunnel đang sử dụng
| Thuộc tính | Giá trị |
|------------|---------|
| **Tunnel ID** | `aa304557-6390-44bd-a052-7d7fe2a6e7d6` |
| **Tunnel Name** | `revenue-bot` |
| **Domain** | `ebebot.click` |
| **Chạy như** | Windows Scheduled Task (`CloudflaredTunnel`) dưới SYSTEM account |

### Scheduled Tasks (chạy khi startup)
| Task Name | Executable | Mô tả |
|-----------|------------|-------|
| `CloudflaredTunnel` | `cloudflared.exe tunnel run` | Cloudflare Tunnel daemon |
| `WebhookServer` | `node.exe D:\revenue-bot\webhook-server.js` | LINE Bot webhook server (port 39412) |

### Hostname đã cấu hình
| Hostname | Service (Port) | Mô tả |
|----------|----------------|-------|
| `webhook.ebebot.click` | `http://localhost:39412` | LINE Bot webhook server |
| `pg.ebebot.click` | `http://localhost:8888` | Erablue App (Docker production) |

### Config file locations
| User | Path |
|------|------|
| **SYSTEM (production)** | `C:\Windows\System32\config\systemprofile\.cloudflared\config.yml` |
| **Backend user** | `C:\Users\15931 - Backend\.cloudflared\config.yml` |

---

## 🔧 Cách Thêm Hostname Mới

### Bước 1: Cập nhật config.yml
Thêm hostname mới vào **TRƯỚC** dòng `- service: http_status:404`:

```yaml
tunnel: aa304557-6390-44bd-a052-7d7fe2a6e7d6
credentials-file: C:\Windows\System32\config\systemprofile\.cloudflared\aa304557-6390-44bd-a052-7d7fe2a6e7d6.json
ingress:
  - hostname: webhook.ebebot.click
    service: http://localhost:39412
  - hostname: pg.ebebot.click
    service: http://localhost:8888
  # === THÊM HOSTNAME MỚI Ở ĐÂY ===
  - hostname: new-service.ebebot.click
    service: http://localhost:XXXX
  # ================================
  - service: http_status:404  # <-- LUÔN ĐỂ CUỐI CÙNG
```

### Bước 2: Thêm DNS route
```powershell
cloudflared tunnel route dns aa304557-6390-44bd-a052-7d7fe2a6e7d6 new-service.ebebot.click
```

### Bước 3: Restart tunnel (PowerShell Admin)
```powershell
Stop-ScheduledTask -TaskName "CloudflaredTunnel"
Start-Sleep 2
Start-ScheduledTask -TaskName "CloudflaredTunnel"
```

### Bước 4: Verify
```powershell
curl https://new-service.ebebot.click
```

---

## ⚠️ Các Lỗi Thường Gặp

### Lỗi 1033 - Tunnel không kết nối
**Nguyên nhân**: Cloudflared không chạy hoặc credentials sai
**Giải pháp**:
```powershell
# Kiểm tra process
tasklist /FI "IMAGENAME eq cloudflared.exe"

# Nếu không chạy, start lại task
Start-ScheduledTask -TaskName "CloudflaredTunnel"
```

### Lỗi 502 - Bad Gateway
**Nguyên nhân**: Service backend không chạy hoặc port sai
**Giải pháp**: Kiểm tra port đúng chưa
```powershell
netstat -ano | findstr ":PORT_NUMBER"
```

### Lỗi "Failed to add route: record already exists"
**Nguyên nhân**: DNS record đã tồn tại
**Giải pháp**: Vào Cloudflare Dashboard → DNS → xóa record cũ → chạy lại lệnh

---

## 📁 Credentials & Files

| File | Mô tả |
|------|-------|
| `aa304557-...7d6.json` | Tunnel credentials (KHÔNG xóa!) |
| `cert.pem` | Account certificate |
| `config.yml` | Ingress rules |

---

## 🚫 KHÔNG LÀM

1. ❌ KHÔNG tạo tunnel mới - chỉ thêm hostname vào tunnel hiện có
2. ❌ KHÔNG xóa file `.json` credentials
3. ❌ KHÔNG chạy cloudflared thủ công (dùng Scheduled Task)
4. ❌ KHÔNG dùng tunnel cũ `d164e5de-...` (đã hỏng)

---

## ✅ Checklist Khi Thêm Service Mới

- [ ] Service đang chạy ở localhost:PORT?
- [ ] Port đã confirm bằng `netstat`?
- [ ] Đã thêm hostname vào config.yml (SYSTEM path)?
- [ ] Đã chạy `cloudflared tunnel route dns`?
- [ ] Đã restart Scheduled Task?
- [ ] Đã test bằng curl/browser?
- [ ] Đã cập nhật bảng "Hostname đã cấu hình" trong file này?
