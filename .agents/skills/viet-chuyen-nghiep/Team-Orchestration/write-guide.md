# Pipeline: Viết User Guide (write-guide) — v3.1

## Khi nào kích hoạt
- User yêu cầu viết user guide, SOP, hướng dẫn sử dụng
- User yêu cầu viết onboarding guide, FAQ, API docs, manual
- Tín hiệu: "viết hướng dẫn", "viết user guide", "viết SOP", "viết manual",
  "viết tài liệu hướng dẫn", "onboarding guide", "API documentation", "FAQ"

## Pipeline

```
content/ → style/ (technical + presentation) → quality/ → platform/ (docs) → Output
   │                    │                          │              │
   │                    │                          │              └─ Document format
   │                    │                          └─ Accuracy check
   │                    └─ Technical writing + visual structure
   └─ Research + process mapping
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` nhận brief → xác định:
   - Loại guide: user manual, SOP, FAQ, onboarding, API docs
   - Đối tượng đọc: end-user, admin, developer, nhân viên mới
   - Level chi tiết: beginner-friendly vs. advanced reference
   - Scope: full product hay feature-specific
2. `research.md` thu thập:
   - Quy trình/sản phẩm cần document
   - Common pain points + FAQs
   - Screenshots/diagrams cần thiết (placeholder)
3. `analysis.md` đề xuất:
   - Cấu trúc tài liệu (task-based vs. feature-based)
   - Navigation strategy (search, TOC, cross-ref)
4. Output: **Guide Blueprint YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến 2 BTV:
   - `technical.md` — biên tập ngôn ngữ kỹ thuật, accuracy
   - `presentation.md` — visual hierarchy, callout boxes, numbering
2. Kết hợp xử lý:
   - Step-by-step instructions (numbered, clear actions)
   - Prerequisites + expected outcomes per section
   - Troubleshooting section (problem → solution format)
   - Glossary nếu có thuật ngữ chuyên ngành
3. Output: **Guide Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - fact-check (accuracy of steps, versions, paths)
   - consistency (thuật ngữ, naming convention, tone)
   - natural (dễ hiểu, không mơ hồ)
   - punctuation + capitalization
2. Bonus check: **Completeness** (có thiếu step nào không?)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. BTV Tài Liệu format:
   - Numbered sections (1. / 1.1 / 1.1.1)
   - Screenshot placeholders with captions
   - Callout boxes: Tip, Warning, Note, Important
   - Table of Contents auto-gen
   - Version tracking header
3. Output: **Guide sẵn sàng xuất bản**

## Guide Types — Format tham khảo

### User Manual
```
1. Giới thiệu
2. Cài đặt / Bắt đầu
3. Tính năng chính (task-based)
4. Cấu hình nâng cao
5. Troubleshooting
6. Appendix / Glossary
```

### SOP
```
1. Mục đích
2. Phạm vi áp dụng
3. Trách nhiệm
4. Quy trình (flowchart + steps)
5. Biểu mẫu kèm theo
6. Lịch sử thay đổi
```

### Onboarding Guide
```
1. Chào mừng + Giới thiệu công ty
2. Tuần đầu tiên — Checklist
3. Công cụ cần thiết
4. Quy trình làm việc
5. Ai hỏi gì — Contact directory
6. FAQ nhân viên mới
```

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/guide-standards.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/technical.md` — technical editing
- `Ban/style/presentation.md` — visual structure
- `Ban/platform/docs.md` — document formatting
- `Workers/guide-worker.md` — execution templates (SOP layouts, callout boxes, troubleshooting templates) ★
