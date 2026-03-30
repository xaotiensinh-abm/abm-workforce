# Pipeline: Kiểm Duyệt Xuất Bản (publish-ready) — v3.0

## Khi nào kích hoạt
- User có bài đã viết xong → cần kiểm duyệt lần cuối trước xuất bản

## Pipeline

```
quality/ (full 6 kiểm tra) → platform/ → Output
         │                       │
         └─ PASS/REVISE          └─ Tối ưu platform
```

## Bước chi tiết

### 1. Ban Kiểm Duyệt (quality/) — CHẾ ĐỘ ĐẦY ĐỦ
1. Chạy **6 kiểm tra** song song:
   - `punctuation.md` — dấu câu
   - `capitalization.md` — viết hoa
   - `natural.md` — văn phong tự nhiên
   - `anti-ai.md` — phát hiện AI
   - `fact-check.md` — kiểm chứng claims
   - `consistency.md` — nhất quán
2. Quyết định: PASS → platform/ | REVISE → trả user + ghi chú

### 2. Ban Xuất Bản (platform/)
1. Nếu PASS → `lead-platform.md` tối ưu cho nền tảng mục tiêu
2. Output: **Content publish-ready** + checklist xuất bản
