# Bộ nhớ Kinh nghiệm: Ban Tiếp nhận

## Mẫu phân tích Brief đã kiểm chứng

### Pattern 1: "Viết bài" ambiguity resolution
```
User: "Viết bài về AI"
→ Questions to ask:
  1. Bài cho ai đọc? (audience)
  2. Đăng ở đâu? (platform → content_type)
  3. Mục đích gì? (educate/sell/entertain)
→ Default nếu user không trả lời: blog, general audience, educate
```

### Pattern 2: Multi-output detection
```
User: "Viết 3 bài cho FB, Threads, LinkedIn"
→ Parse: 1 request → 3 outputs → cùng topic, khác format
→ Route: write-new pipeline × 3 (parallel)
```

### Pattern 3: Implicit quality expectation
```
User: "cho sếp xem"    → quality: publish-ready
User: "draft nhanh"     → quality: draft
User: "xuất bản"        → quality: publish-ready + proofread
User: "thử viết xem"    → quality: draft, relaxed constraints
```

## Các lỗi Brief thường gặp

| Failure | Root cause | Fix |
|---------|-----------|-----|
| Writer viết sai tone | Brief thiếu audience | ALWAYS extract audience |
| Output quá dài/ngắn | Brief thiếu length hint | Ask expected length |
| Sai platform format | Brief thiếu platform | Detect from context clues |

## Bài học: Khi nào hỏi vs khi nào mặc định

- **Hỏi**: audience, platform (critical for routing)
- **Assume**: tone=professional, format=markdown (safe defaults)
- **Never assume**: domain-sensitive content, output length > 3000 từ
