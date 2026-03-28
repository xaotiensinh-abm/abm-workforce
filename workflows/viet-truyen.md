---
description: 📖 Viết Truyện Dài Kỳ v1.0 — Module chuyên biệt viết truyện serialized đa phong cách, thuộc hệ thống Viết Chuyên Nghiệp
---

# WORKFLOW: /viet-truyen — Viết Truyện Dài Kỳ Đa Phong Cách

Module chuyên biệt cho **viết truyện dài kỳ serialized** tiếng Việt. Thuộc skill viet-chuyen-nghiep v3.3.

---

## Khi nào kích hoạt

- ✅ Tạo series truyện mới (world-building, character, plot)
- ✅ Viết chương tiếp theo cho series đang chạy
- ✅ Sửa chương theo phản biện / scorecard
- ✅ Review / chấm điểm chương
- ✅ Thay đổi canon / hiến pháp truyện
- ✅ Deep research bổ sung tri thức cho thể loại mới
- ❌ Truyện ngắn / one-shot → dùng `/viet-pro`
- ❌ Task không liên quan viết fiction

---

## Bước 1: Load Orchestrator

// turbo
```
view_file: D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\viet-truyen-orchestrator.md
```

## Bước 2: Xác định Mode

| Mode | Khi nào | File |
|------|---------|------|
| `new-series` | Tạo series mới từ brief | `modes/new-series.md` |
| `next-chapter` | Viết chương tiếp (DEFAULT) | `modes/next-chapter.md` |
| `rewrite-chapter` | Sửa chương theo scorecard | `modes/rewrite-chapter.md` |
| `review-only` | Chấm điểm, phản biện | `modes/review-only.md` |
| `change-control` | Sửa canon / hiến pháp | `modes/change-control.md` |
| `research-pack` | Deep research thể loại mới | `modes/research-pack.md` |

## Bước 3: Load genre + knowledge packs

```
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\genres\     → 8 genre packs
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\knowledge\  → 5 knowledge packs
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\style\      → 4 style packs
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\review\     → 3 review files
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\brain\      → 8 Second Brain schemas
D:\AntigravityWorkspace\Viet-chuyen-nghiep\VietTruyen\templates\  → 3 templates
```

## Bước 4: Chạy pipeline 5 tầng

```
T0 BOOTSTRAP → T1 STRATEGY → T2 EXECUTION → T3 SYNTHESIS → T4 MATERIALIZATION
```

## Bước 5: Fiction Review Council

Chấm 10 tiêu chí, ngưỡng PASS ≥ 9.0/10. Xem `review/fiction-scoring-rubric.md`.

---

## Quick Commands

| Lệnh | Mô tả |
|-------|--------|
| `/viet-truyen` | Kích hoạt module, auto-detect mode |
| `/viet-truyen new [brief]` | Tạo series mới |
| `/viet-truyen next` | Viết chương tiếp |
| `/viet-truyen rewrite [chapter]` | Sửa chương |
| `/viet-truyen review [chapter]` | Chấm điểm chương |
| `/viet-truyen research [topic]` | Deep research thể loại/tri thức |

---

## Auto Deep-Research

Khi gặp thể loại chưa có genre pack → tự động kích hoạt `research-pack` mode → tạo pack mới → quay lại pipeline.
