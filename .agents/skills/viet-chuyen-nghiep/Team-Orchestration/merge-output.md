# Pipeline: Ghép File Output (merge-output) — v3.1

## Khi nào kích hoạt
- Content dài (>10,000 từ) được viết thành nhiều file part
- Cần ghép nhiều module/chapter thành một tài liệu hoàn chỉnh
- Cần đảm bảo encoding UTF-8 chuẩn cho tiếng Việt

## Pipeline

```
Workers/merge-worker → quality/ (verify) → Output
     │                     │
     └─ merge-parts.py     └─ Kiểm tra encoding + tiếng Việt
```

## Bước chi tiết

### 1. Merge Worker (Workers/merge-worker.md)
1. Xác định danh sách file cần merge (theo pattern hoặc chỉ định thủ công)
2. Chạy script Python:
   ```
   // turbo
   python D:\AntigravityWorkspace\Viet-chuyen-nghiep\scripts\merge-parts.py --dir <thư_mục> --pattern <tên> --output <file>
   ```
3. Nếu cần chỉ định file cụ thể:
   ```
   // turbo
   python D:\AntigravityWorkspace\Viet-chuyen-nghiep\scripts\merge-parts.py --files file1.md file2.md file3.md --output merged.md
   ```

### 2. Verify (quality/)
1. Kiểm tra file output tồn tại
2. Kiểm tra encoding UTF-8 (không BOM)
3. Kiểm tra tiếng Việt hiển thị đúng
4. Đếm tổng chars/lines/ước tính thời lượng đọc

### 3. Output
- File Markdown duy nhất, UTF-8 without BOM
- Tổng hợp đầy đủ nội dung từ tất cả parts
- Sẵn sàng xuất bản hoặc chuyển đổi (DOCX/PDF)

## Lưu ý

> ⚠️ **KHÔNG BAO GIỜ** dùng PowerShell `Set-Content` hoặc `Out-File` để merge file tiếng Việt.
> PowerShell mặc định sử dụng encoding Windows-1252 hoặc UTF-8 with BOM, gây lỗi hiển thị.
> **LUÔN** dùng Python script `merge-parts.py`.
