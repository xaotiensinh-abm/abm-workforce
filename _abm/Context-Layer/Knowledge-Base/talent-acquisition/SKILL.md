---
name: "talent-acquisition"
description: "Tuyển dụng pipeline — sourcing, screening, interviewing, offer. ATS workflow + employer branding."
---

# 🎯 Talent Acquisition — Tuyển Dụng

## Sử dụng khi

- Xây dựng pipeline tuyển dụng
- Sourcing candidates (job boards, LinkedIn, referral)
- Thiết kế quy trình phỏng vấn
- Employer branding strategy

## KHÔNG sử dụng khi

- Viết JD → dùng `hr-operations`
- Đánh giá nhân viên hiện tại → dùng `performance-review`
- Onboarding → dùng `hr-operations`

## PIPELINE TUYỂN DỤNG

```
Sourcing → Screening → Interview → Offer → Onboarding
  100%       40%         15%       8%      5%
```

### Bước 1: Sourcing
- [ ] Đăng tin: TopCV, VietnamWorks, LinkedIn, Facebook Jobs
- [ ] Employee referral (ưu tiên — quality cao nhất)
- [ ] Headhunting cho vị trí senior
- [ ] University partnerships cho intern/fresher

### Bước 2: Screening
```yaml
screening_criteria:
  must_have: []      # Loại ngay nếu thiếu
  nice_to_have: []   # Cộng điểm
  culture_fit: []    # Đánh giá qua behavioral questions
  red_flags: []      # Auto-reject
```

### Bước 3: Interview Framework
| Vòng | Người PV | Focus | Thời gian |
|------|---------|-------|:---------:|
| 1 | HR | Culture fit, motivation | 30 phút |
| 2 | Hiring Manager | Technical/professional | 45 phút |
| 3 | Team Lead | Teamwork, scenarios | 30 phút |
| 4 | CEO (if senior) | Vision alignment | 20 phút |

### Bước 4: Offer
- [ ] Benchmark lương thị trường
- [ ] Package: lương + phụ cấp + benefits
- [ ] Offer letter template
- [ ] Deadline accept: 3-5 ngày làm việc

## METRICS

```
Time-to-fill: < 30 ngày (target)
Cost-per-hire: tổng chi phí / số người tuyển
Quality-of-hire: performance rating sau 6 tháng
Offer acceptance rate: > 80%
```

## QUY TẮC

1. Referral **luôn ưu tiên** — quality + retention cao nhất
2. Structured interview — cùng câu hỏi cho mọi ứng viên
3. Decision trong 48h sau vòng cuối — không để ứng viên chờ
4. Feedback cho 100% ứng viên bị reject
