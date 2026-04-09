---
name: xlsx-official
version: 1.0.1
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "LOCAL-ONLY — Đọc, sửa, phân tích file .xlsx/.csv hiện có trên máy bằng openpyxl. Chỉ dùng khi user YÊU CẦU CỤ THỂ thao tác file local (sửa Excel, chỉnh formula, format cells). Mặc định tạo Excel MỚI → dùng skywork-excel."
risk: unknown
source: community
date_added: "2026-02-27"
---

> [!IMPORTANT]
> **Routing Rule:** Mặc định tạo Excel/spreadsheet mới → dùng `skywork-excel` (Skywork Cloud API). Skill này CHỈ dùng khi user yêu cầu: (1) sửa file .xlsx local có sẵn, (2) chỉnh formula/formatting, (3) user nói rõ "làm offline" hoặc "không upload".

# Requirements for Outputs

## All Excel files

### Zero Formula Errors
- Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preserve Existing Templates (when updating templates)
- Study and EXACTLY match existing format, style, and conventions when modifying files
- Never impose standardized formatting on files with established patterns
- Existing template conventions ALWAYS override these guidelines

## 📚 Bách Khoa Toàn Thư (Knowledge Base & SOPs)

> [!TIP]
> File này đã được Đại Phẫu V2 ép chuẩn Kiến Trúc 9-Layer (Lazy-Loading) bởi ABM. Các ví dụ, giới hạn, và quy trình xử lý cồng kềnh đã được rút vứt vào kho dự phòng.
> Để đọc bộ tài liệu đầy đủ cực kỳ quan trọng đó, hãy chạy Tool `view_file` dọc vào đây trước khi bắt tay làm:
> 👉 **/Users/dungtq/ABM-Workforce/.agents/skills/xlsx-official/references/sop.md**

<!-- 📦 Refactored by ABM Skill Architect v2.0 | Mass-Extraction Token Decoupling -->
