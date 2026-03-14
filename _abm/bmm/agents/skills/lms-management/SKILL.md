---
name: lms-management
description: "Quản lý hệ thống đào tạo trực tuyến — cấu trúc khóa học online, drip content, enrollment, completion tracking"
---

# Quản Lý LMS — Learning Management System

## Mục đích
Skill này giúp thiết lập và quản lý hệ thống đào tạo trực tuyến cho doanh nghiệp đào tạo AI.

## Nền tảng LMS phù hợp

| Platform | Phù hợp | Chi phí | Đặc điểm |
|----------|---------|---------|-----------|
| **Moodle** | Tổ chức GD lớn | Miễn phí (self-host) | Mã nguồn mở, customize mạnh |
| **Teachable** | Startup đào tạo | $39-119/tháng | Dễ dùng, payment tích hợp |
| **Thinkific** | Creator cá nhân | $36-149/tháng | Funnel marketing tốt |
| **Custom** | DN riêng | Tùy | Next.js + DB, toàn quyền |

## Cấu trúc khóa học online

### Template cấu trúc
```yaml
lms_course:
  title: "[Tên khóa]"
  slug: "[url-friendly]"
  pricing:
    type: "free | paid | subscription"
    price: "[VNĐ]"
    trial_days: 7
  
  enrollment:
    max_students: null  # null = unlimited
    open_date: "YYYY-MM-DD"
    close_date: null
    prerequisites: ["course-slug-1"]
  
  drip_schedule:
    enabled: true
    release_type: "fixed_date | days_after_enrollment | completion_based"
    modules:
      - module_id: "M01"
        available: "day_0"
      - module_id: "M02"
        available: "day_7"
        requires_completion: "M01"  # unlock sau khi hoàn thành M01
  
  content_types:
    - video: { host: "youtube | vimeo | bunny", max_length: "20min" }
    - text: { format: "markdown | html" }
    - quiz: { type: "multiple_choice | code_challenge" }
    - assignment: { submission: "file | github_repo | live_demo" }
    - live_session: { platform: "zoom | google_meet", recording: true }
  
  completion:
    certificate: true
    criteria:
      - "Hoàn thành ≥ 80% video"
      - "Đạt ≥ 70% tổng quiz"
      - "Nộp capstone project"
    badge: "AI Practitioner Level 1"
```

### Drip Content Strategy

```
Tuần 1: Module Foundation (mở ngay)
    ↓ Quiz M01 đạt ≥ 70%
Tuần 2: Module Core (auto-unlock)
    ↓ Lab M02 nộp
Tuần 3: Module Advanced (auto-unlock)
    ↓ Quiz M03 đạt ≥ 70%
Tuần 4: Capstone (auto-unlock)
    ↓ Nộp project + peer review
Tuần 5: Certification (auto-unlock)
```

## Enrollment & Student Management

### Onboarding flow
1. **Đăng ký** → Welcome email + hướng dẫn setup môi trường
2. **Ngày 1** → Orientation video + community group invite
3. **Ngày 3** → Check-in: đã setup chưa? Cần hỗ trợ?
4. **Tuần 1** → First milestone celebration email

### Theo dõi tiến độ
```yaml
student_tracking:
  metrics:
    - completion_rate       # % nội dung hoàn thành
    - quiz_avg_score        # Điểm trung bình quiz
    - time_spent            # Tổng thời gian học
    - last_active           # Lần cuối online
    - assignment_status     # Đã nộp / Chưa nộp / Trễ
  
  alerts:
    inactive_7_days: "Gửi email nhắc nhở"
    behind_schedule: "Gửi email hỗ trợ"
    quiz_failed_3x: "Giao mentor hỗ trợ"
    completed: "Gửi certificate + upsell"
```

### Churn Prevention cho học viên
| Tín hiệu | Hành động |
|-----------|-----------|
| Không login 5 ngày | Email nhắc + highlight bài tiếp theo |
| Quiz fail 2 lần | Gợi ý xem lại video + tài liệu bổ trợ |
| Không nộp assignment | Email + offer office hours |
| Drop rate > 30% | Review lại module, thu feedback |

## Analytics Dashboard

| Metric | Mục tiêu | Cách tính |
|--------|---------|-----------|
| Completion Rate | ≥ 70% | Students hoàn thành / Total enrolled |
| NPS Score | ≥ 50 | Survey cuối khóa |
| Quiz Pass Rate | ≥ 80% | Pass first attempt / Total attempts |
| Time to Complete | Đúng schedule | Avg days / Expected days |
| Revenue per Student | Tăng YoY | Total revenue / Total students |

## Instructor Management

### Tuyển chọn giảng viên
```yaml
instructor_criteria:
  required:
    - expertise: "≥ 3 năm kinh nghiệm thực tế trong lĩnh vực AI"
    - portfolio: "≥ 2 projects AI đã triển khai production"
    - communication: "Giảng bài rõ ràng, tiếng Việt lưu loát"
    - demo_lesson: "Dạy thử 30 phút — đánh giá bởi panel 3 người"
  bonus:
    - "Kinh nghiệm giảng dạy / mentoring"
    - "Có publications / open-source contributions"
    - "Certification từ Google, AWS, hoặc tương đương"
```

### Onboarding giảng viên
1. **Tuần 1**: Đọc course-design SKILL + ABM brand guidelines
2. **Tuần 1**: Nhận template slide, lab, rubric từ `training-content`
3. **Tuần 2**: Soạn 1 module mẫu → review bởi lead instructor
4. **Tuần 2**: Dạy thử (dry run) nội bộ → feedback
5. **Tuần 3**: Dạy chính thức module đầu tiên (có TA hỗ trợ)

### Đánh giá giảng viên
```yaml
instructor_evaluation:
  frequency: "Sau mỗi khóa"
  metrics:
    - student_rating: { target: ">= 4.0/5", weight: 30 }
    - completion_rate: { target: ">= 70%", weight: 20 }
    - nps_score: { target: ">= 50", weight: 20 }
    - content_quality: { reviewer: "lead instructor", weight: 15 }
    - on_time_delivery: { target: "100%", weight: 15 }
  
  actions:
    excellent: "Bonus + mời dạy khóa nâng cao"
    good: "Giữ nguyên + feedback improvement"
    below: "Mentor + cải thiện 1 khóa → re-evaluate"
    poor: "Không mời lại"
```

---

## Gamification

### Hệ thống XP & Level
```yaml
gamification:
  xp_system:
    actions:
      - watch_video: 10
      - complete_quiz: 25
      - pass_quiz_first_try: 50
      - submit_lab: 30
      - submit_project: 100
      - peer_review: 20
      - daily_login_streak: 5
      - help_in_community: 15
    
    levels:
      - { level: 1, name: "AI Newbie", xp: 0, badge: "🌱" }
      - { level: 2, name: "Data Explorer", xp: 100, badge: "🔍" }
      - { level: 3, name: "Model Builder", xp: 300, badge: "🔧" }
      - { level: 4, name: "Neural Architect", xp: 600, badge: "🏗️" }
      - { level: 5, name: "AI Master", xp: 1000, badge: "🧠" }

  streaks:
    daily_login: "🔥 Streak — bonus XP sau 7 ngày liên tiếp"
    weekly_quiz: "⚡ Quiz Master — hoàn thành quiz đúng hạn 4 tuần liên tiếp"
    lab_perfect: "💎 Perfect Lab — 3 labs liên tiếp 100%"

  leaderboard:
    scope: "Per course + All-time"
    display: "Top 10 + vị trí cá nhân"
    reset: "Mỗi khóa mới"
    privacy: "Opt-in (mặc định tắt)"

  badges:
    - { name: "First Blood", trigger: "Hoàn thành module đầu tiên" }
    - { name: "Speed Runner", trigger: "Hoàn thành module trước deadline 3 ngày" }
    - { name: "Helper", trigger: "Giúp 5 bạn trong community" }
    - { name: "100% Club", trigger: "Hoàn thành 100% khóa học" }
    - { name: "Reviewer Pro", trigger: "Peer review 5 projects" }
```

---

## Output khi được yêu cầu

1. **LMS Setup Plan** — Platform, cấu trúc, timeline
2. **Course Structure YAML** — Modules, drip schedule, completion criteria
3. **Student Journey Map** — Onboarding → Learning → Certification
4. **Analytics Template** — Dashboard metrics + alerts
5. **Instructor Playbook** — Tuyển, onboard, đánh giá giảng viên
6. **Gamification Config** — XP, levels, badges, leaderboard
