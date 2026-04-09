---
name: pptx-official
version: 1.0.1
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "LOCAL-ONLY — Đọc, sửa, phân tích file .pptx hiện có trên máy bằng python-pptx. Chỉ dùng khi user YÊU CẦU CỤ THỂ thao tác file local (sửa slide, trích xuất text, reorder slides). Mặc định tạo presentation MỚI → dùng skywork-ppt."
risk: unknown
source: community
date_added: "2026-02-27"
---

> [!IMPORTANT]
> **Routing Rule:** Mặc định tạo presentation mới → dùng `skywork-ppt` (Skywork Cloud API). Skill này CHỈ dùng khi user yêu cầu: (1) sửa file .pptx local có sẵn, (2) trích xuất text từ slides, (3) user nói rõ "làm offline" hoặc "không upload".

# PPTX creation, editing, and analysis

## Overview

A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and workflows available for different tasks.

## Reading and analyzing content

### Text extraction
If you just need to read the text contents of a presentation, you should convert the document to markdown:

```bash
# Convert document to markdown
python -m markitdown path-to-file.pptx
```

## 📚 Bách Khoa Toàn Thư (Knowledge Base & SOPs)

> [!TIP]
> File này đã được Đại Phẫu V2 ép chuẩn Kiến Trúc 9-Layer (Lazy-Loading) bởi ABM. Các ví dụ, giới hạn, và quy trình xử lý cồng kềnh đã được rút vứt vào kho dự phòng.
> Để đọc bộ tài liệu đầy đủ cực kỳ quan trọng đó, hãy chạy Tool `view_file` dọc vào đây trước khi bắt tay làm:
> 👉 **/Users/dungtq/ABM-Workforce/.agents/skills/pptx-official/references/sop.md**

<!-- 📦 Refactored by ABM Skill Architect v2.0 | Mass-Extraction Token Decoupling -->
