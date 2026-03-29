---
description: "Thiết lập Hợp đồng Code (Implementation Plan) chuẩn ABM. Dùng khi đã có Document/Spec thiết kế và cần biên dịch thành danh sách Task."
---

// turbo-all

# 📋 Write Plan — Spec → Implementation Plan

## Bước 1: Load Writing Plans Skill
Đọc và thực thi toàn bộ skill:
- Load file: `{project-root}/.agents/skills/writing-plans/SKILL.md`
- Follow ALL steps trong skill

## Bước 2: Tạo Implementation Plan
1. Đọc spec/design doc hiện có
2. Phân tách thành bite-sized tasks
3. Xác định dependencies giữa tasks
4. Viết plan chi tiết với acceptance criteria
5. Trình CEO review plan

## Bước 3: Chuyển sang Execution
Sau khi plan approved → invoke `/execute-plan` để thực thi.
