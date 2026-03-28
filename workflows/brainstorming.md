---
description: Brainstorming ý tưởng thành thiết kế chi tiết trước khi implement
---

Workflow biến ý tưởng thành thiết kế hoàn chỉnh qua đối thoại tự nhiên. **BẮT BUỘC** dùng trước mọi creative work.

---

## Khi nào dùng

- Tạo features mới
- Build components
- Thêm functionality
- Modify behavior

---

## Quy trình

### 1. Hiểu Ý tưởng

1. **Check project context**: files, docs, recent commits
2. **Hỏi câu hỏi từng cái một** để refine idea
3. **Prefer multiple choice** khi có thể
4. **Focus**: purpose, constraints, success criteria

### 2. Khám phá Approaches

1. Đề xuất 2-3 approaches khác nhau với trade-offs
2. Present options conversationally
3. **Lead với recommended option** và giải thích lý do

### 3. Trình bày Design

1. Break thành sections 200-300 words
2. **Hỏi sau mỗi section**: "Phần này có ổn không?"
3. Cover: architecture, components, data flow, error handling, testing
4. Sẵn sàng quay lại clarify nếu cần

---

## Sau Design

### Documentation

```
docs/plans/YYYY-MM-DD-<topic>-design.md
```

Commit design document to git.

### Implementation (nếu tiếp tục)

1. Hỏi: "Ready to set up for implementation?"
2. Tạo isolated workspace
3. Tạo detailed implementation plan

---

## Key Principles

| Principle | Mô tả |
|-----------|-------|
| **One question at a time** | Không overwhelm với nhiều câu hỏi |
| **Multiple choice preferred** | Dễ trả lời hơn open-ended |
| **YAGNI ruthlessly** | Remove unnecessary features |
| **Explore alternatives** | Luôn 2-3 approaches trước khi settle |
| **Incremental validation** | Present design từng phần, validate mỗi phần |
| **Be flexible** | Quay lại clarify khi cần |
