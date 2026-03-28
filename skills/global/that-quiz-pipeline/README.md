# THAT Quiz Pipeline

> **Tình huống — Hành động — An toàn — Tư duy**
> Production-grade quiz generation for 12 Vietnamese school grades

## Overview

THAT Quiz Pipeline là một ABM Skill chuyên biệt cho việc chuyển đổi **kịch bản bài giảng số hóa** thành **thư viện câu hỏi trắc nghiệm** production-grade. Mỗi module tạo 12 file (lop-01.md → lop-12.md), mỗi file 30 câu hỏi với 3 level độ khó.

## Pipeline

```
KỊCH BẢN       Phase 1            Phase 2           Phase 3           Phase 4
CÓ SẴN    →   SINH CÂU HỎI   →   AUDIT           →   NÂNG CẤP      →   ĐÓNG GÓI
(input)        THÔ                (Phát hiện bias)     DISTRACTOR        FINAL
               30 câu/lớp                              (Bẫy tâm lý)
```

## Key Features

- **4-Phase Pipeline**: Sinh → Audit → Nâng cấp Distractor → Đóng gói
- **Anti Length Bias**: Đáp án A-D đồng đều 15-25 từ
- **Psychological Traps**: 4 loại bẫy tâm lý cho distractor
- **Key Balance**: A ≈ B ≈ C ≈ D (7-8/30 câu)
- **Age-Appropriate**: Ngôn ngữ tùy chỉnh theo 12 khối lớp
- **9-Point Quality Checklist**: Kiểm tra trước khi ship

## Directory Structure

```
that-quiz-pipeline/
├── SKILL.md                          ← Main skill instructions
├── README.md                         ← This file
└── resources/
    ├── references/
    │   └── SOP-Nang-Cap-Distractor.md   ← Distractor upgrade methodology
    ├── examples/
    │   └── lop-01-sample.md             ← Sample output format
    └── templates/
        ├── chu-de-phu-template.md       ← Sub-topic table templates
        └── audit-checklist.md           ← Audit & tracking checklists
```

## Quick Start

```bash
# Sinh câu hỏi từ kịch bản
"Từ kịch bản [file], tạo 30 câu hỏi lớp [X] theo format THAT"

# Audit bộ câu hỏi
"Audit bộ câu hỏi [file]: key distribution + Length Bias + distractor"

# Nâng cấp distractor
"Nâng cấp distractor Level 2+3 của [file] theo SOP bẫy tâm lý"

# Batch sinh cả cấp
"Tạo câu hỏi lớp 1-5 cho module [tên] từ kịch bản [file]"
```

## Target Project

Dự án **12 Kỹ Năng An Toàn Cho Trẻ Em** — Viết Chuyên Nghiệp
- Repository: `viet-chuyen-nghiep`
- Path: `docs/THAT/{N},{ten-chu-de}/`

## Integration

| Cần | Dùng skill/workflow |
|-----|---------------------|
| Viết kịch bản mới | `/viet-pro`, `/content-research-writer` |
| Review chất lượng | `/abm-review` (W8:CriticAgent) |
| Xuất DOCX | `docx-document-builder` |
| BSR Compliance | BSR AI Compliance Framework KI |

---

*THAT Quiz Pipeline v1.0 — ABM-Workforce Skill*
*"Kịch bản có sẵn → Thư viện câu hỏi production-grade"*
