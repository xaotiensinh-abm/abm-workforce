---
description: ✍️ Viết Chuyên Nghiệp v3.1 — Hệ thống viết tiếng Việt chuyên nghiệp với Kiến Trúc Tòa Soạn (6 Ban, 31 BTV)
---

# WORKFLOW: /viet-pro — Viết Chuyên Nghiệp Tiếng Việt

Kích hoạt skill **Viết Chuyên Nghiệp v3.1** — Kiến Trúc Tòa Soạn AI.

---

## Khi nào kích hoạt

- ✅ Viết ebook, tài liệu chuyên môn, handbook
- ✅ Viết content social đa nền tảng (FB, TikTok, LinkedIn)
- ✅ Viết kịch bản video (short/long form)
- ✅ Sửa bản nháp cho tự nhiên hơn
- ✅ Chấm bài viết thang 100 điểm
- ✅ Phản biện nội dung, kiểm tra logic
- ✅ Kiểm tra anti-AI, xuất bản
- ❌ Task không liên quan đến viết tiếng Việt

---

## Bước 1: Load Skill Definition

// turbo
```
view_file: C:\Users\PC\.gemini\antigravity\skills\viet-chuyen-nghiep\SKILL.md
```

## Bước 2: Xác định loại task

Phân loại yêu cầu user theo bảng routing:

| Yêu cầu | Pipeline | Các Ban |
|----------|----------|---------|
| Viết mới (ebook, blog, social, video) | `write-new` | content → style → quality → platform |
| Sửa bản nháp | `edit-draft` | content → style → quality |
| Chấm bài | `grade-content` | content → quality (rubric) |
| Phản biện | `critique-content` | content → quality (critique) |
| Research thuần | `deep-research` | content → quality |
| Xuất bản | `publish-ready` | quality → platform |
| Viết email | `write-email` | content → style → quality → platform (email) |
| Viết giáo trình | `write-curriculum` | content → style → quality → platform (docs) |
| Viết user guide/SOP | `write-guide` | content → style → quality → platform (docs) |
| **Ghép file output** | `merge-output` | merge-worker → quality (verify encoding) |

Chi tiết: đọc `Orchestrator/routing-matrix.md`

## Bước 3: Chạy pipeline

Theo thứ tự Ban đã xác định. Đọc file pipeline chi tiết tại:

// turbo
```
view_file: D:\AntigravityWorkspace\Viet-chuyen-nghiep\Team-Orchestration\write-new.md
```

Hoặc pipeline tương ứng: `edit-draft.md`, `grade-content.md`, `critique-content.md`, `deep-research.md`, `publish-ready.md`, `write-email.md`, `write-curriculum.md`, `write-guide.md`, `merge-output.md`

## Bước 4: Load Ban agents khi cần

```
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Ban\content\  → 3 BTV
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Ban\style\    → 8 BTV
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Ban\quality\  → 7 BTV
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Ban\platform\ → 9 BTV
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Workers\      → 13 Workers
D:\AntigravityWorkspace\Viet-chuyen-nghiep\scripts\      → Utility scripts
D:\AntigravityWorkspace\Viet-chuyen-nghiep\Ban\meta\     → 3 agents
```

## Bước 5: Quality gate

Đọc `Orchestrator/escalation-rules.md` nếu cần escalation.

---

## Quick Commands

| Lệnh | Mô tả |
|-------|--------|
| `/viet-pro` | Kích hoạt skill, bắt đầu pipeline |
| `/viet-pro viết ebook` | Trực tiếp vào write-new pipeline |
| `/viet-pro chấm bài` | Trực tiếp vào grade-content pipeline |
| `/viet-pro sửa bài` | Trực tiếp vào edit-draft pipeline |
| `/viet-pro phản biện` | Trực tiếp vào critique-content pipeline |
| `/viet-pro ghép file` | Merge nhiều file part thành 1 file (UTF-8) |
| `/viet-pro viết email` | Trực tiếp vào write-email pipeline |
| `/viet-pro viết giáo trình` | Trực tiếp vào write-curriculum pipeline |
