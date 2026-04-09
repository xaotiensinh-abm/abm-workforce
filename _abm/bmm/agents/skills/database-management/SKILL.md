---
name: "database-management"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Quản lý database chuyên trách — schema design, migration, query optimization, data integrity. SQL/NoSQL patterns, caching, monitoring."
---

# 🗄️ Database Management — Quản Lý Cơ Sở Dữ Liệu

## Sử dụng khi

- Thiết kế schema cho project mới
- Viết migration scripts (UP + DOWN)
- Tối ưu query performance
- Data integrity check / validation
- Chuyển đổi database (SQL ↔ NoSQL)
- Backup / restore strategy

## KHÔNG sử dụng khi

- Phân tích dữ liệu business → dùng `data-analysis`
- Tạo báo cáo Excel → dùng `skywork-excel` (mặc định) hoặc `xlsx-official` (local only)
- Cần workflow automation → dùng `workflow-automation`

## SCHEMA DESIGN FRAMEWORK

### Bước 1: Entity-Relationship Analysis
```
1. Xác định entities (bảng/collection)
2. Xác định relationships:
   - 1:1 → merge hoặc FK
   - 1:N → FK ở bảng "many"
   - N:N → junction table
3. Xác định attributes cho mỗi entity
4. Xác định primary keys + unique constraints
```

### Bước 2: Checklist thiết kế
```
✅ Primary keys — UUID vs auto-increment vs ULID
✅ Foreign keys — ON DELETE CASCADE hay SET NULL?
✅ Indexes — cho fields trong WHERE/JOIN/ORDER BY
✅ Constraints — NOT NULL, UNIQUE, CHECK, DEFAULT
✅ Soft delete — deleted_at TIMESTAMP NULL
✅ Audit fields — created_at, updated_at, created_by
✅ Enum/Status — lookup table vs CHECK constraint
✅ Timestamps — TIMESTAMP WITH TIME ZONE (UTC)
```

### Bước 3: Naming Convention

| Đối tượng | Convention | Ví dụ |
|-----------|-----------|-------|
| Table | snake_case, số nhiều | `users`, `order_items` |
| Column | snake_case | `first_name`, `created_at` |
| Primary key | `id` hoặc `{table}_id` | `id`, `user_id` |
| Foreign key | `{referenced_table}_id` | `user_id`, `order_id` |
| Junction table | `{table1}_{table2}` | `user_roles`, `product_tags` |
| Index | `idx_{table}_{columns}` | `idx_users_email` |
| Unique constraint | `uq_{table}_{columns}` | `uq_users_email` |

## MIGRATION PROTOCOL

### Quy trình bắt buộc:
```
1. Viết migration script (UP + DOWN) — LUÔN có rollback
2. Code review migration script
3. Test trên local/staging TRƯỚC
4. ⚠️ BACKUP production TRƯỚC khi chạy
5. Chạy migration trong maintenance window
6. Verify data integrity SAU migration
7. Monitor performance 24h sau migration
```

### Template migration (SQL):
```sql
-- Migration: add_verified_at_to_users
-- Up
ALTER TABLE users ADD COLUMN verified_at TIMESTAMP NULL;
CREATE INDEX idx_users_verified_at ON users(verified_at);

-- Down (rollback)
DROP INDEX idx_users_verified_at;
ALTER TABLE users DROP COLUMN verified_at;
```

### ⚠️ Dangerous operations — CẦN KẾ HOẠCH ĐẶC BIỆT:
```
🔴 DROP TABLE         → Backup bảng trước, keep 30 ngày
🔴 DROP COLUMN        → Verify không có code reference
🟡 RENAME TABLE/COL   → Phải update tất cả code trước
🟡 ALTER TYPE          → Có thể lock table lớn
🟡 ADD NOT NULL        → Cần DEFAULT value trước
```

## QUERY OPTIMIZATION

### Phát hiện slow queries:
```sql
-- PostgreSQL: queries > 500ms
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
WHERE mean_exec_time > 500
ORDER BY total_exec_time DESC
LIMIT 20;
```

### Optimization checklist:
```
1. EXPLAIN ANALYZE mọi query chậm
2. Kiểm tra: có dùng index scan hay sequential scan?
3. N+1 queries → batch/join
4. SELECT * → chỉ select columns cần
5. Pagination: LIMIT/OFFSET → cursor-based (large datasets)
6. Subqueries → JOIN (nếu data lớn)
7. LIKE '%text%' → full-text search index
```

### Index strategy:
```
✅ Nên index:
   - Columns trong WHERE clause thường xuyên
   - Columns trong JOIN conditions
   - Columns trong ORDER BY
   - Foreign keys

❌ Không nên index:
   - Columns ít selectivity (boolean, status với ít values)
   - Bảng nhỏ (< 1000 rows)
   - Columns thường xuyên UPDATE
```

## NoSQL PATTERNS (MongoDB/Firestore)

### Embed vs Reference decision tree:
```
Embed khi:
  ✅ Relationship 1:few (< 100 items)
  ✅ Data luôn đọc cùng nhau
  ✅ Data ít thay đổi
  ✅ Không cần query riêng sub-documents

Reference khi:
  ✅ Relationship 1:many hoặc N:N
  ✅ Data thay đổi độc lập
  ✅ Cần query riêng
  ✅ Document size > 1MB risk
```

## BACKUP STRATEGY

| Loại | Tần suất | Retention | Tool |
|------|---------|-----------|------|
| Full backup | Hàng ngày (2AM) | 30 ngày | pg_dump / mongodump |
| Incremental | Mỗi 6 giờ | 7 ngày | WAL archiving |
| Point-in-time | Liên tục | 7 ngày | WAL / oplog |
| Pre-migration | Trước mỗi migration | Vĩnh viễn | Manual |

## QUY TẮC SẮT

1. **LUÔN backup** trước migration — KHÔNG NGOẠI LỆ
2. **KHÔNG hardcode** connection strings → dùng env vars
3. Schema changes → **migration script**, KHÔNG sửa tay
4. **Index** mọi field dùng trong WHERE/JOIN/ORDER BY
5. **Monitor** query performance — set alert cho > 1s
6. **Data validation** ở DB level (constraints) + app level

## Related Skills
- data-analysis, skywork-excel (mặc định tạo Excel), xlsx-official (local only), workflow-automation
