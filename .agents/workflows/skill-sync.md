---
description: Kiểm tra và sync skills mới từ repo community hàng tháng
---

# 🔄 Workflow: Skill Sync

Kiểm tra repo [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) hàng tháng để phát hiện skills mới phù hợp.

## Khi nào chạy
- Mỗi tháng 1 lần (ngày 1 hoặc 15)
- Khi CEO yêu cầu mở rộng capabilities
- Khi phát hiện gap trong hệ thống skills

## Bước 1: Kiểm tra repo

Truy cập catalog mới nhất:
// turbo
```
curl -s https://raw.githubusercontent.com/sickn33/antigravity-awesome-skills/main/CATALOG.md | head -200
```

## Bước 2: So sánh với manifest hiện tại

Đọc manifest hiện tại:
// turbo
```
cat _abm/_config/skill-manifest.csv
```

## Bước 3: Xác định skills mới phù hợp

Tiêu chí lọc:
1. **Phù hợp business** — marketing, sales, analysis, HR, office
2. **Không trùng** — Chưa có trong 48 skills hiện tại
3. **Không cần dependency ngoài** — Hoặc có thể adapt loại bỏ
4. **Chất lượng** — SKILL.md có nội dung thực, không placeholder

## Bước 4: Đề xuất cho CEO

Tạo báo cáo:
```
# Skill Sync Report — [Tháng/Năm]

## Skills mới phát hiện: [N]
## Đề xuất tích hợp: [N]
| Skill | Category | Lý do | Priority |
|-------|----------|-------|----------|

## Skills bỏ qua: [N]
| Skill | Lý do bỏ qua |
|-------|--------------|
```

## Bước 5: Chờ CEO duyệt

STOP — Không tự tích hợp. Chờ CEO phê duyệt từng skill.

## Bước 6: Tích hợp (sau duyệt)

Với mỗi skill được duyệt:
1. Tải SKILL.md từ repo
2. Việt hóa + adapt cho ABM
3. Tạo folder trong `skills/`
4. Cập nhật `skill-manifest.csv`
5. Cập nhật routing trong `jarvis-orchestrator.md`
6. Cập nhật `CHANGELOG.md`
7. Xác minh: đếm files, manifest, routes
