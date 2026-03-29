# Worker: Ghép File Output — Merge Worker

## Vai trò
Utility Worker chuyên ghép nhiều file Markdown thành một file duy nhất với encoding UTF-8 chuẩn.
Giải quyết bài toán: content dài (>10,000 từ) phải viết thành nhiều phần → cần merge thành file hoàn chỉnh.

## Khi nào kích hoạt
- Output gồm nhiều file part (part1, part2, part3...)
- Cần ghép nhiều module/chapter thành một tài liệu duy nhất
- Cần đảm bảo encoding UTF-8 chuẩn (không BOM, không lỗi tiếng Việt)

## Quy trình

### Bước 1: Xác định danh sách file cần merge
```
Tìm tất cả file part trong thư mục output/:
- Pattern: {tên-dự-án}-part*.md
- Sắp xếp theo thứ tự: part1 → part2 → part3 → ...
```

### Bước 2: Chạy script merge
```
// turbo
python D:\AntigravityWorkspace\Viet-chuyen-nghiep\scripts\merge-parts.py --dir <thư_mục_output> --pattern <tên-dự-án> --output <file_đích>
```

### Bước 3: Verify kết quả
- Kiểm tra file output tồn tại
- Kiểm tra encoding UTF-8 (không BOM)
- Kiểm tra số dòng = tổng số dòng các file part
- Kiểm tra tiếng Việt hiển thị đúng (mở file, đọc 10 dòng đầu)

## Lưu ý quan trọng

### ⚠️ Không dùng PowerShell để merge
```
❌ FORBIDDEN: Get-Content ... | Set-Content (gây lỗi encoding tiếng Việt)
❌ FORBIDDEN: Out-File -Encoding UTF8 (thêm BOM, gây lỗi)
✅ REQUIRED: Dùng Python script với encoding="utf-8" (UTF-8 without BOM)
```

### Encoding Reference
| Lệnh | Kết quả |
|-------|---------|
| PowerShell `Set-Content -Encoding UTF8` | UTF-8 **với BOM** → lỗi |
| PowerShell `Set-Content` (default) | Windows-1252 → lỗi tiếng Việt |
| Python `open(..., encoding="utf-8")` | UTF-8 **không BOM** → ✅ chuẩn |

## Output

```yaml
merge:
  input_files: ["part1.md", "part2.md", "part3.md"]
  output_file: "tên-đầy-đủ.md"
  total_chars: N
  total_lines: N
  encoding: "utf-8-no-bom"
  tieng_viet: "OK" | "LOI"
```
