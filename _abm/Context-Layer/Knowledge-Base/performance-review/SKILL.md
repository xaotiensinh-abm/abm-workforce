---
name: "performance-review"
description: "Đánh giá hiệu suất nhân viên — KPI tracking, 360° feedback, PIP, calibration sessions."
---

# 📊 Performance Review — Đánh Giá Hiệu Suất

## Sử dụng khi

- Đánh giá KPI hàng quý/năm
- Thiết kế khung đánh giá 360°
- Xây dựng Performance Improvement Plan (PIP)
- Calibration sessions giữa managers

## KHÔNG sử dụng khi

- Tuyển dụng → dùng `talent-acquisition`
- Khảo sát engagement → dùng `employee-engagement`
- Viết JD → dùng `hr-operations`

## KHUNG ĐÁNH GIÁ

### KPI Framework
```yaml
kpi_review:
  employee: ""
  period: "Q1/2026"
  objectives:
    - name: ""
      weight: 30   # tổng = 100%
      target: ""
      actual: ""
      score: 0      # 1-5
      evidence: ""
  overall_score: 0
  rating: ""  # Xuất sắc / Tốt / Đạt / Cần cải thiện / Không đạt
```

### Thang Đánh Giá
| Điểm | Rating | Mô tả |
|:----:|--------|-------|
| 5 | Xuất sắc | Vượt xa kỳ vọng, impact rõ ràng |
| 4 | Tốt | Vượt kỳ vọng ở nhiều mặt |
| 3 | Đạt | Hoàn thành đúng kỳ vọng |
| 2 | Cần cải thiện | Chưa đạt một số mục tiêu |
| 1 | Không đạt | Không hoàn thành, cần PIP |

### 360° Feedback
```
Sources:
├── Self-assessment (nhân viên tự đánh giá)
├── Manager review (quản lý trực tiếp)
├── Peer review (2-3 đồng nghiệp)
├── Direct reports (cấp dưới, nếu có)
└── Cross-functional (phòng ban khác)
```

### Performance Improvement Plan (PIP)
- [ ] Xác định gap cụ thể
- [ ] Mục tiêu cải thiện SMART
- [ ] Timeline: 30/60/90 ngày
- [ ] Hỗ trợ: mentor, training
- [ ] Check-in hàng tuần
- [ ] Tiêu chí pass/fail rõ ràng

## QUY TẮC

1. Đánh giá dựa trên **bằng chứng**, không cảm tính
2. Calibration bắt buộc giữa managers (tránh thiên vị)
3. PIP là cơ hội cải thiện, **không phải hình phạt**
4. Feedback phải **kịp thời** — không đợi cuối năm
