---
description: Lưu trạng thái công việc vào memory — save task, daily save, milestone save
---
// turbo-all

# 💾 Workflow /save — Lưu Trạng Thái Công Việc

## Bước 1: Load skill save
Đọc skill: `{project-root}/_abm/bmm/agents/skills/save/SKILL.md`

## Bước 2: Thu thập thông tin
Tự động quét conversation hiện tại và thu thập:
- Tasks đã hoàn thành / đang làm / bị chặn
- Files đã tạo / sửa / xóa
- Quyết định quan trọng
- Kiến thức mới học được
- Trạng thái plan (nếu có)
- Skill đã sử dụng

## Bước 3: Xác định loại save
- Nếu user nói "save" sau 1 task → `task_save`
- Nếu user nói "save" cuối ngày → `daily_save`
- Nếu đạt milestone quan trọng → `milestone_save`

## Bước 4: Đếm save tiếp theo
Kiểm tra thư mục `_abm/Context-Layer/Second-Brain/memory/saves/`:
- Đếm số files hiện có
- save_id = SAVE-{số tiếp theo, 3 chữ số}

## Bước 5: Tạo file YAML
Tạo file mới: `_abm/Context-Layer/Second-Brain/memory/saves/SAVE-{NNN}-{YYYY-MM-DD}.yaml`
Theo format chuẩn trong SKILL.md

## Bước 6: Hiển thị xác nhận
Hiện bảng tóm tắt cho CEO:
```
💾 ĐÃ LƯU — SAVE-{NNN} | {date} {time}
📌 {title}
✅ Hoàn thành: {N} | 🔄 Đang làm: {N}
📋 Ngày mai: {priority}
```

## Bước 7: Commit (tùy chọn)
Nếu CEO muốn commit, chạy:
```bash
git add _abm/Context-Layer/Second-Brain/memory/saves/
git commit -m "save: SAVE-{NNN} — {title}"
```
