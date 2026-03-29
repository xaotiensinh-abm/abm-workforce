---
description: Giao việc đào tạo cho Jarvis — thiết kế khóa học, tài liệu, workshop, chứng chỉ AI
---

# /training — Phòng Đào Tạo ABM

## Khi nào dùng
- Thiết kế khóa học AI mới
- Tạo tài liệu đào tạo (slide, lab, handout)
- Lên kế hoạch workshop
- Thiết kế chương trình chứng chỉ
- Quản lý LMS và tiến độ học viên

## Cách dùng
```
/training [mô tả yêu cầu]
```

## Ví dụ
```
/training Thiết kế khóa học "AI cho Marketing" dành cho marketer, 8 tuần online
/training Tạo lab exercise về fine-tuning LLM với LoRA
/training Lên kế hoạch workshop AI Agents nửa ngày cho 30 người
/training Thiết kế chương trình chứng chỉ AI 3 cấp cho ABM
```

## Quy trình
1. Jarvis nhận yêu cầu → phân loại: `training` / `course` / `workshop`
2. Load skills: `course-design`, `training-content`, `student-assessment`
3. Tạo hợp đồng → giao `training-specialist`
4. Worker thực hiện → trả chứng nhận + bằng chứng
5. Jarvis xác minh → trình CEO

## Skills liên quan
- `course-design` — Thiết kế khóa học
- `lms-management` — Quản lý LMS
- `student-assessment` — Đánh giá học viên
- `training-content` — Tài liệu đào tạo
- `workshop-facilitation` — Tổ chức workshop
- `certification-program` — Chương trình chứng chỉ
