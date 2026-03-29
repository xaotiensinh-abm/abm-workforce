# Pipeline: Deep Research (deep-research) — v3.0

## Khi nào kích hoạt
- User muốn nghiên cứu thuần, không cần viết output

## Pipeline

```
content/ (research full) → quality/ (verify) → Output
     │                          │
     │                          └─ fact-check xác minh
     └─ Research 5 lớp + analysis
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — CHẾ ĐỘ ĐẦY ĐỦ
1. `lead-content.md` xác định câu hỏi nghiên cứu
2. `research.md` thu thập nguồn 5 lớp, cross-verify
3. `analysis.md` tổng hợp findings, rút insight
4. Output: **Báo cáo nghiên cứu** (sources, key findings, gaps)

### 2. Ban Kiểm Duyệt (quality/) — CHẾ ĐỘ VERIFY
1. `fact-check.md` xác minh claims chính
2. Output: **Báo cáo đã verify** + mức tin cậy
