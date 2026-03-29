# Trưởng Ban Tư Liệu — Lead Examples

## Vai trò
Quản lý thư viện bài mẫu đã duyệt. Là nguồn reference cho mọi Ban 
khi cần xem "bài đạt chuẩn trông như thế nào".

## Cấu trúc Thư viện

```
examples/
├─ lead-examples.md   ← (file này)
├─ blog/              ← Bài blog mẫu
├─ social/            ← Post MXH mẫu
├─ ebook/             ← Chapter ebook mẫu
├─ email/             ← Email doanh nghiệp mẫu
├─ video/             ← Video script mẫu
└─ report/            ← Báo cáo mẫu
```

## Tiêu chuẩn Nhập mẫu

Bài mẫu chỉ được lưu khi:
1. ✅ Đã PASS đầy đủ Ban Kiểm Duyệt (6/6)
2. ✅ Điểm chất lượng ≥85/100
3. ✅ Anti-AI: Grade A hoặc B
4. ✅ Được Tổng Biên Tập duyệt

## Metadata Mỗi Bài mẫu

```yaml
bai_mau:
  tieu_de: "..."
  loai: "blog" | "social" | "ebook" | "email" | "video" | "report"
  tone: "..." # từ tone-of-voice-guide.md
  audience: "..."
  diem_chat_luong: X/100
  ngay_duyet: "YYYY-MM-DD"
  diem_manh: ["..."]  # tại sao bài này được chọn
  ghi_chu: "..."
```

## Cách Sử dụng

| Ai dùng | Khi nào | Mục đích |
|---------|---------|---------|
| Ban Thu Thập | Đầu pipeline | Xem format mẫu |
| Ban Biên Tập | Khi biên tập | Tham chiếu tone/style |
| Ban Kiểm Duyệt | Khi chấm điểm | Benchmark chất lượng |
| Ban Phát Triển | Khi audit | Kiểm tra consistency |

## Tham chiếu hiện có
- `assets/examples/example-edit-draft.md`
- `assets/examples/example-social-posts.md`
- `assets/examples/example-critique-report.md`
