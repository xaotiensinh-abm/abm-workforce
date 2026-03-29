# ⚠️ THƯ MỤC LEGACY — KHÔNG CÒN HOẠT ĐỘNG

> **Phiên bản:** v2.0 (đã thay thế bởi `Ban/` trong v3.0)
> **Ngày deprecated:** 2026-03-10
> **Lý do:** Refactor sang Kiến Trúc Tòa Soạn v3.0

## Trạng thái

Các files trong thư mục `Workers/` và `SubAgents/` đã được **thay thế** bởi 
hệ thống 6 Ban trong `Ban/`:

| Workers/ (v2.0 — NGƯNG) | Ban/ (v3.0 — ĐANG HOẠT ĐỘNG) |
|--------------------------|------------------------------|
| `intake-worker.md` | `Ban/content/lead-content.md` |
| `research-worker.md` | `Ban/content/research.md` |
| `strategy-worker.md` | `Ban/content/analysis.md` |
| `longform-worker.md` | `Ban/style/` (6 BTV) |
| `social-worker.md` | `Ban/platform/` (facebook, tiktok, linkedin) |
| `video-worker.md` | `Ban/platform/video.md` |
| `critique-worker.md` | `Ban/quality/` (7 BTV) |
| `quality-worker.md` | `Ban/quality/lead-quality.md` |

## Khi nào Tham khảo

Chỉ tham khảo files này khi:
- Cần xem logic cũ để so sánh
- Debug vấn đề liên quan đến kiến trúc
- **KHÔNG** dùng các files này cho pipeline production

## Pipeline Hiện tại

Xem `Orchestrator/routing-matrix.md` — pipeline v3.0:
```
content/ → style/ → quality/ → platform/
```
