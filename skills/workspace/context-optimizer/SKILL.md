---
name: context-optimizer
description: Tối ưu ngữ cảnh và token tự động. Tự kích hoạt khi context dài, conversation phức tạp, hoặc multi-step task. Use PROACTIVELY for long conversations, complex multi-file tasks, context window management, or when detecting context rot symptoms like repeated errors or forgotten instructions.
metadata:
  author: Antigravity
  version: "1.0"
  category: context-management
---

# Context Optimizer

## Khi nào TỰ ĐỘNG kích hoạt
Skill này **tự kích hoạt** khi phát hiện:
- Conversation đã **dài** (>20 lượt tương tác)
- Task **multi-step** phức tạp (>5 files thay đổi)
- Có dấu hiệu **Context Rot**: quên instruction, lặp lại lỗi, output giảm chất lượng
- Cần load nhiều **reference files** cùng lúc

## Chiến lược tối ưu

### 1. Dynamic Context Loading (Just-in-Time)
KHÔNG load hết thông tin từ đầu. Chỉ load khi cần:
- Đọc SKILL.md trước → chỉ đọc references/ khi cần chi tiết
- Dùng `view_file` với range cụ thể thay vì đọc toàn bộ file
- Dùng `grep_search` để tìm chính xác thay vì scan toàn bộ

### 2. Structured Note-Taking
Khi task dài, tự động duy trì ghi chú có cấu trúc:
```
## Working Notes
- Goal: [Mục tiêu chính]
- Done: [Đã làm gì]
- Current: [Đang làm gì]
- Blocked: [Nếu có vấn đề]
- Key files: [Files quan trọng đang xử lý]
```

### 3. Compaction Strategy
Khi phát hiện context dài:
- Tóm tắt các bước đã hoàn thành thay vì giữ chi tiết
- Loại bỏ output cũ không còn relevant
- Giữ lại: decisions, errors encountered, current state

### 4. Pre-computed Loading
Load thông tin nền tảng trước cho tasks thường gặp:
- CLAUDE.md / .brain files → load đầu session
- Project structure → scan lần đầu, cache mental model
- Recent changes → git log ngắn

## Quy tắc
1. **Minimal Viable Context**: Chỉ load thông tin minimal cần thiết
2. **Recall > Precision**: Ưu tiên nhớ đủ trước, sau đó mới lọc bớt
3. **No Context Stuffing**: Không nhồi nhét token-heavy content vào context
