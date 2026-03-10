---
name: "database-management"
description: "Quản lý database chuyên trách — schema design, migration, query optimization, data integrity. SQL/NoSQL patterns cho project thực tế."
---

# 🗄️ Database Management — Quản Lý Cơ Sở Dữ Liệu

Skill chuyên trách thiết kế, quản lý và tối ưu database cho project.

## Sử dụng khi

- Thiết kế schema cho project mới
- Viết migration scripts
- Tối ưu query performance
- Data integrity check / validation
- Chuyển đổi database (SQL ↔ NoSQL)

## KHÔNG sử dụng khi

- Phân tích dữ liệu business → dùng `data-analysis`
- Tạo báo cáo Excel → dùng `xlsx`
- Cần workflow automation → dùng `workflow-automation`

## SCHEMA DESIGN CHECKLIST

```
1. [ ] Xác định entities + relationships
2. [ ] Normalization (3NF hoặc đủ dùng)
3. [ ] Primary keys + Foreign keys
4. [ ] Indexes cho query thường dùng
5. [ ] Constraints (NOT NULL, UNIQUE, CHECK)
6. [ ] Soft delete (deleted_at) vs Hard delete
7. [ ] Audit fields (created_at, updated_at, created_by)
8. [ ] Enum/Status fields → dùng lookup table
```

## MIGRATION PROTOCOL

```
1. Viết migration script (UP + DOWN)
2. Test trên staging TRƯỚC
3. Backup production TRƯỚC khi chạy
4. Chạy migration
5. Verify data integrity SAU migration
6. ⚠️ KHÔNG bao giờ chạy migration trực tiếp trên production mà không backup
```

## PATTERNS

### SQL (PostgreSQL/MySQL)
- Naming: `snake_case` cho tables + columns
- Table names: **số nhiều** (users, orders, products)
- Junction tables: `user_roles`, `order_items`
- Indexes: `idx_{table}_{column}`

### NoSQL (MongoDB/Firestore)
- Collection names: **số nhiều** lowercase
- Document structure: embed vs reference decision
- Embed khi: 1:few, data luôn đọc cùng nhau
- Reference khi: 1:many, data thay đổi độc lập

## QUY TẮC SẮT

1. **LUÔN backup** trước migration
2. **KHÔNG hardcode** connection strings → dùng env vars
3. Schema changes → **migration script**, KHÔNG sửa tay
4. **Index** mọi field dùng trong WHERE/JOIN/ORDER BY

---

## Nguồn gốc
- BMAD feedback điểm 3: Database agent chuyên trách
- ABM Workforce v2.6
