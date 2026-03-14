---
name: workshop-facilitation
description: "Tổ chức workshop AI — agenda design, hands-on labs, facilitation, Q&A, feedback collection"
---

# Tổ Chức Workshop AI — Workshop Facilitation

## Mục đích
Skill này giúp lên kế hoạch và tổ chức workshop đào tạo AI hiệu quả, từ agenda đến follow-up.

## Quy trình 4 giai đoạn

### Giai đoạn 1: Lên kế hoạch (2-4 tuần trước)

```yaml
workshop_plan:
  title: "[Tên workshop]"
  format: "onsite | online | hybrid"
  duration: "2h | half_day | full_day | 2_days"
  max_attendees: 30
  
  target_audience:
    who: "Ai tham gia?"
    level: "beginner | intermediate | advanced"
    prerequisites: ["..."]
  
  objectives:
    - "Sau workshop, người tham gia sẽ..."
  
  logistics:
    venue: "[Địa điểm / Platform]"
    equipment:
      - "Laptop (mỗi người)"
      - "Projector / Screen share"
      - "Whiteboard / Miro"
      - "Wifi ổn định"
    materials:
      - "Handout in sẵn"
      - "Starter code notebooks"
      - "Dataset pre-loaded"
    registration: "Google Form / Eventbrite"
    recording: true
```

### Giai đoạn 2: Thiết kế Agenda

**Workshop nửa ngày (4 giờ) — Template:**

| Thời gian | Hoạt động | Phương pháp | Thời lượng |
|-----------|-----------|------------|-----------|
| 08:30 | Check-in + Networking | Ice-breaker | 15' |
| 08:45 | Giới thiệu + Mục tiêu | Presentation | 15' |
| 09:00 | **Phần 1: Concept** | Lecture + Q&A | 45' |
| 09:45 | ☕ Break | | 15' |
| 10:00 | **Phần 2: Demo** | Live coding | 30' |
| 10:30 | **Phần 3: Hands-on Lab** | Pair programming | 60' |
| 11:30 | Show & Tell | Nhóm trình bày | 15' |
| 11:45 | Wrap-up + Feedback | Survey | 15' |

**Nguyên tắc:**
- **Mỗi 45-60 phút**: Break 10-15 phút
- **Tỷ lệ nghe:làm**: 30:70
- **Pair programming**: 2 người/nhóm cho hands-on
- **Không quá 4 giờ/ngày** cho online

### Giai đoạn 3: Facilitation (Ngày diễn ra)

**Checklist trước workshop:**
- [ ] Test projector/screen share
- [ ] Kiểm tra wifi + backup mobile hotspot
- [ ] Starter code chạy được trên tất cả máy
- [ ] Dataset đã download sẵn (không phụ thuộc internet)
- [ ] Nước uống + snacks (onsite)
- [ ] Recording setup (online)

**Kỹ thuật facilitation:**

| Tình huống | Xử lý |
|-----------|-------|
| Người tham gia im lặng | Hỏi trực tiếp theo tên, polling tool |
| Câu hỏi off-topic | "Câu hỏi hay! Ghi vào parking lot, cuối buổi trả lời" |
| Lỗi kỹ thuật | TA hỗ trợ 1:1, facilitator tiếp tục |
| Chênh lệch trình độ | Pair beginner + advanced, bonus tasks |
| Quá giờ | Cắt Q&A, gửi tài liệu bổ sung sau |

**Vai trò cần có:**
- **Facilitator** (1): Dẫn chương trình, giảng bài
- **TA** (1-2 per 15 người): Hỗ trợ kỹ thuật, debug
- **MC** (1, optional): Quản lý thời gian, Q&A

### Giai đoạn 4: Follow-up (1-7 ngày sau)

```yaml
follow_up:
  day_0:  # Ngay sau workshop
    - "Gửi email cảm ơn + recording link"
    - "Share slide deck + notebooks"
    - "Mở survey feedback"
  
  day_3:
    - "Gửi tài liệu đọc thêm"
    - "Reminder điền feedback"
    - "Invite nhóm community (Telegram/Discord)"
  
  day_7:
    - "Tổng hợp feedback → báo cáo"
    - "Gửi certificate (nếu có)"
    - "Upsell khóa học đầy đủ"
```

## Feedback Collection

```yaml
feedback_survey:
  questions:
    - type: "nps"
      question: "Bạn có giới thiệu workshop này cho đồng nghiệp? (0-10)"
    - type: "rating_5"
      question: "Nội dung (1-5)"
    - type: "rating_5"
      question: "Giảng viên (1-5)"
    - type: "rating_5"
      question: "Thực hành (1-5)"
    - type: "open"
      question: "Điều gì bạn thích nhất?"
    - type: "open"
      question: "Điều gì cần cải thiện?"
    - type: "multiple_choice"
      question: "Bạn muốn học tiếp chủ đề nào?"
      options: ["LLM", "Computer Vision", "MLOps", "RAG", "Agent"]
  
  target_response_rate: ">= 60%"
```

## Output khi được yêu cầu

1. **Workshop Plan** — Logistics, audience, objectives
2. **Agenda** — Timeline chi tiết, phương pháp, thời lượng
3. **Facilitation Guide** — Kịch bản, kỹ thuật xử lý tình huống
4. **Follow-up Plan** — Email sequence, feedback, upsell
5. **Budget Estimate** — Chi phí venue, F&B, materials
