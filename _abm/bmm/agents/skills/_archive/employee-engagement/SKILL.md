---
name: "employee-engagement"
description: "Khảo sát & nâng cao gắn kết nhân viên — eNPS, pulse surveys, action plans, retention strategies."
---

# 💚 Employee Engagement — Gắn Kết Nhân Viên

## Sử dụng khi

- Đo engagement hiện tại (eNPS, pulse survey)
- Phân tích nguyên nhân turnover
- Xây dựng action plan cải thiện engagement
- Thiết kế recognition programs

## KHÔNG sử dụng khi

- Đánh giá KPI → dùng `performance-review`
- Tuyển dụng → dùng `talent-acquisition`
- Onboarding → dùng `hr-operations`

## eNPS (Employee Net Promoter Score)

```
Câu hỏi: "Trên thang 0-10, bạn có giới thiệu công ty này cho bạn bè?"

9-10 = Promoters (phấn khởi)
7-8  = Passives (trung lập)
0-6  = Detractors (không hài lòng)

eNPS = %Promoters - %Detractors
  > +50 = Xuất sắc
  > +30 = Tốt
  > +10 = Ổn
  < 0   = CẢNH BÁO
```

## PULSE SURVEY (Hàng tháng)

```yaml
pulse_survey:
  questions:
    - "Tôi hiểu rõ mục tiêu công việc" # 1-5
    - "Quản lý trực tiếp lắng nghe tôi" # 1-5
    - "Tôi có cơ hội phát triển" # 1-5
    - "Tôi tự hào về công ty" # 1-5
    - "Khối lượng công việc hợp lý" # 1-5
  open_text: "Điều gì bạn muốn thay đổi?"
  frequency: "monthly"
  anonymous: true
```

## ACTION PLAN

| Driver | Action | Owner | Deadline |
|--------|--------|-------|----------|
| Career growth | Lộ trình thăng tiến | HR | 30 ngày |
| Recognition | Chương trình khen thưởng | Manager | 14 ngày |
| Work-life balance | Flexible hours pilot | CEO | 60 ngày |
| Communication | Town hall hàng tháng | CEO | 7 ngày |

## QUY TẮC

1. Survey **ẩn danh** — tuyệt đối bảo mật
2. **Hành động** sau survey — không survey rồi để đó
3. Share kết quả tổng với toàn team (transparency)
4. Đo lại sau 90 ngày để track improvement
