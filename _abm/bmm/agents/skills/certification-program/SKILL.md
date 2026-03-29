---
name: certification-program
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Chương trình chứng chỉ AI — tiêu chuẩn, exam design, certificate template, alumni tracking"
---

# Chương Trình Chứng Chỉ AI — Certification Program

## Mục đích
Skill này giúp thiết kế và vận hành chương trình chứng chỉ AI chuyên nghiệp cho ABM Education.

## Hệ thống chứng chỉ 3 cấp

```
┌─────────────────────────────────────────────────────┐
│                  🏆 AI SPECIALIST                    │
│            Gold — Portfolio 3+ projects              │
│          Advanced modules + Peer review             │
├─────────────────────────────────────────────────────┤
│               🥈 AI PRACTITIONER                     │
│           Silver — Core + 1 Capstone                │
│        Foundation + Core modules completed          │
├─────────────────────────────────────────────────────┤
│               🥉 AI FOUNDATION                      │
│           Bronze — Foundation modules               │
│         Python + ML basics + 1 mini-project         │
└─────────────────────────────────────────────────────┘
```

### Chi tiết từng cấp

```yaml
certification_levels:
  - level: "AI Foundation"
    badge: "🥉"
    color: "#CD7F32"
    requirements:
      modules: ["Python for AI", "Math for ML", "ML Basics"]
      quiz_avg: ">= 70%"
      project: "1 mini-project (classification hoặc regression)"
      duration: "4-6 tuần"
    skills_validated:
      - "Python data manipulation (pandas, numpy)"
      - "Supervised learning cơ bản"
      - "Data visualization"
      - "Model evaluation metrics"
  
  - level: "AI Practitioner"
    badge: "🥈"
    color: "#C0C0C0"
    prerequisites: ["AI Foundation"]
    requirements:
      modules: ["Deep Learning", "NLP/CV", "MLOps Basics"]
      quiz_avg: ">= 75%"
      project: "1 capstone end-to-end"
      peer_review: "Review 2 projects + được review"
      duration: "8-12 tuần"
    skills_validated:
      - "Deep learning (PyTorch/TensorFlow)"
      - "Transfer learning"
      - "Model deployment cơ bản"
      - "Experiment tracking"
  
  - level: "AI Specialist"
    badge: "🏆"
    color: "#FFD700"
    prerequisites: ["AI Practitioner"]
    requirements:
      modules: ["LLM & Prompt Engineering", "RAG Systems", "AI Agents"]
      quiz_avg: ">= 80%"
      portfolio: "3+ projects với documentation"
      presentation: "Demo project cho panel"
      duration: "12-16 tuần"
    skills_validated:
      - "LLM fine-tuning"
      - "RAG pipeline design"
      - "Multi-agent systems"
      - "Production deployment"
```

## Exam Design

### Format thi

```yaml
exam_format:
  foundation:
    duration: "90 phút"
    sections:
      - quiz: { questions: 30, type: "MCQ + code output", weight: 40 }
      - coding: { tasks: 3, type: "Colab notebook", weight: 60 }
    proctoring: "self-paced"
  
  practitioner:
    duration: "3 giờ"
    sections:
      - quiz: { questions: 20, type: "MCQ + short answer", weight: 20 }
      - coding: { tasks: 2, type: "Build model từ scratch", weight: 40 }
      - project_defense: { duration: "15 phút", type: "Trình bày + Q&A", weight: 40 }
    proctoring: "live (Zoom)"
  
  specialist:
    duration: "Take-home 1 tuần"
    sections:
      - project: { type: "End-to-end AI system", weight: 60 }
      - documentation: { type: "Technical report", weight: 20 }
      - presentation: { duration: "20 phút", type: "Panel review", weight: 20 }
    proctoring: "panel review"
```

### Nguyên tắc ra đề
1. **Không hỏi thuần lý thuyết** — luôn có context thực tế
2. **Dataset mới** — không dùng dataset đã practice
3. **Open-ended** — cho phép nhiều approach hợp lệ
4. **Time-pressured nhưng fair** — đủ thời gian cho average student
5. **Anti-cheating**: Random question pool, unique datasets

## Certificate Template

```yaml
certificate:
  layout: "landscape_A4"
  elements:
    header: "ABM EDUCATION"
    logo: "abm_logo.png"
    title: "CHỨNG CHỈ [CẤP ĐỘ]"
    body: |
      Chứng nhận [Họ tên]
      đã hoàn thành chương trình đào tạo
      [Tên khóa học]
      với kết quả [Loại]
    details:
      - "Mã chứng chỉ: ABM-[LEVEL]-[YYYY]-[XXXX]"
      - "Ngày cấp: [DD/MM/YYYY]"
      - "Có hiệu lực: 2 năm"
    signatures:
      - name: "Trịnh Quang Dũng"
        title: "Giám đốc ABM Education"
    qr_code: "https://abm.edu.vn/verify/[cert_id]"
    
  verification:
    url: "https://abm.edu.vn/verify"
    method: "QR code → tra cứu online"
    blockchain: false  # Phase 2
```

## Alumni Tracking

```yaml
alumni_program:
  database:
    fields:
      - student_id
      - name, email, phone
      - certification_level
      - completion_date
      - expiry_date
      - current_company
      - linkedin_url
  
  engagement:
    monthly:
      - "Newsletter: AI trends + job openings"
    quarterly:
      - "Alumni meetup (online/offline)"
      - "Guest speaker slots cho alumni"
    yearly:
      - "Re-certification reminder"
      - "Alumni survey: career impact"
  
  benefits:
    - "Giảm 30% khóa học tiếp theo"
    - "Access community exclusive (Discord)"
    - "Job board partner companies"
    - "Referral bonus: 500K/học viên mới"
  
  metrics:
    - career_advancement: "% alumni thăng tiến / chuyển ngành"
    - salary_increase: "% tăng lương sau chứng chỉ"
    - nps: "Net Promoter Score alumni"
    - referral_rate: "% alumni giới thiệu người mới"
```

## Revenue Reporting

```yaml
revenue_metrics:
  per_course:
    - gross_revenue: "Tổng doanh thu = Số học viên × Giá khóa"
    - net_revenue: "Sau giảm giá, hoàn tiền, affiliate commission"
    - cost_per_student: "Chi phí giảng viên + platform + marketing / Số HV"
    - profit_margin: "(Net revenue - Total cost) / Net revenue × 100"
    - break_even: "Số HV tối thiểu để hòa vốn"
  
  per_student:
    - ltv: "Revenue trung bình 1 HV trong toàn bộ lifecycle"
    - courses_per_student: "Trung bình bao nhiêu khóa / HV"
    - referral_value: "Revenue từ HV được giới thiệu bởi alumni"
    - upsell_rate: "% HV mua khóa tiếp theo"
  
  cohort_analysis:
    - month_0: "Enrollment + first payment"
    - month_3: "Completion rate + upsell rate"
    - month_6: "Referral rate + NPS"
    - month_12: "Re-certification rate + LTV"
  
  dashboard:
    frequency: "Monthly"
    kpis:
      - "MRR (Monthly Recurring Revenue)"
      - "Churn rate HV"
      - "CAC (Customer Acquisition Cost)"
      - "LTV / CAC ratio (target: ≥ 3)"
      - "Revenue per instructor"
```

---

## Re-certification Policy

```yaml
recertification:
  validity: "2 năm kể từ ngày cấp"
  
  renewal_options:
    option_1_exam:
      name: "Thi lại (rút gọn)"
      duration: "60 phút"
      pass_score: 75
      fee: "30% giá khóa gốc"
      content: "Kiến thức mới + core concepts"
    
    option_2_project:
      name: "Nộp project mới"
      deadline: "30 ngày kể từ ngày đăng ký"
      requirements: "1 project dùng công nghệ AI mới nhất"
      fee: "20% giá khóa gốc"
    
    option_3_course:
      name: "Học khóa nâng cao"
      discount: "30% cho alumni"
      auto_renew: true
  
  grace_period: "3 tháng sau hết hạn — vẫn được gia hạn"
  expired_action: "Chuyển badge thành 'Expired' — cần thi lại đầy đủ"
  
  notification:
    - "6 tháng trước: Email nhắc + giảm giá early bird 20%"
    - "3 tháng trước: Email + options gia hạn"
    - "1 tháng trước: Email urgent"
    - "Hết hạn: Email + chuyển badge"
  
  ai_specific:
    reason: "AI thay đổi nhanh — kiến thức 2 năm có thể lỗi thời"
    update_areas:
      - "LLM models mới (GPT → Gemini → Claude → ...)"
      - "Frameworks mới (LangChain → LlamaIndex → ...)"
      - "Best practices cập nhật"
      - "Regulations mới (EU AI Act, VN AI guidelines)"
```

---

## Output khi được yêu cầu

1. **Certification Framework** — 3 cấp, requirements, skills validated
2. **Exam Blueprint** — Format, sections, câu hỏi mẫu
3. **Certificate Template** — Design + mã xác thực
4. **Alumni Program** — Engagement plan, benefits, metrics
5. **Re-certification Policy** — Validity, renewal options, notifications
6. **Revenue Report** — Per-course, per-student, cohort, KPIs
