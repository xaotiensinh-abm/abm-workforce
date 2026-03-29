# Nhật ký Phiên — Phiên mẫu #001

## Thông tin phiên

```yaml
phien_id: "VCN-001"
ngay: "2026-03-10"
loai_task: "viết-mới"
pipeline: "write-new"
do_phuc_tap: "trung bình"
nguoi_dung: "user_demo"
```

## Dòng thời gian

| Bước | Ban | Kết quả | Thời gian |
|------|-----|---------|-----------|
| 1 | Tiếp nhận | Brief parsed: blog, audience=marketer, tone=professional | 0:00 |
| 2 | Nghiên cứu | 5 nguồn Tier 1, 3 nguồn Tier 2, 0 mâu thuẫn | 0:02 |
| 3 | Chiến lược | Góc: contrarian, thesis xác định, outline 5 phần | 0:03 |
| 4 | Viết dài | Bản thảo 1200 từ, markdown format | 0:05 |
| 5 | Chất lượng | Anti-AI: 35/100 ✅, rubric: 82/100 ✅, risk: 0 flags | 0:06 |

## Kết quả

```yaml
trang_thai: "hoàn thành"
diem_rubric: 82
diem_anti_ai: 35
so_tu: 1200
vong_sua: 0
co_risk: false
```

## Bài học rút ra

1. **Brief rõ ràng = output tốt:** User nêu rõ audience + platform → pipeline chạy mượt
2. **Nguồn Tier 1 đủ:** Không cần dùng Tier 3 cho topic phổ biến
3. **Anti-AI dưới 40 ngay lần đầu:** Do strategy chọn góc contrarian, tự nhiên tránh sáo rỗng

## Mẫu cần ghi nhớ

- Topic marketing + audience marketer → ưu tiên data-driven angle
- Blog 1000-1500 từ = sweet spot cho medium-depth content
- Contrarian angle giảm AI-smell hiệu quả hơn rewrite
