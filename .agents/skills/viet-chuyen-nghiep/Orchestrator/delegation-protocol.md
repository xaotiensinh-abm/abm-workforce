# Quy trình Giao thác có Hợp đồng — v3.0

## Nguyên tắc cốt lõi

Hệ thống viet-chuyen-nghiep vận hành theo mô hình **Delegation Chain Management**:
- **Forward Delegation:** trách nhiệm giao xuống tầng dưới
- **Liability Return:** trách nhiệm kết quả quay ngược lên tầng trên

## Giao thác xuôi: Tổng Biên Tập → Trưởng Ban

Khi Tổng Biên Tập giao việc cho Trưởng Ban, phải ghi rõ:

| Trường | Mô tả | Bắt buộc |
|--------|--------|----------|
| `task_type` | Loại tác vụ (write/edit/grade/critique) | ✅ |
| `output_format` | Format đầu ra mong muốn | ✅ |
| `success_criteria` | Tiêu chí thành công | ✅ |
| `quality_threshold` | Ngưỡng chất lượng tối thiểu | ✅ |
| `ban_truoc` | Cần output từ Ban nào trước | ✅ |
| `deadline_hint` | Ưu tiên tốc độ hay chất lượng | ⚪ |

### Ví dụ

```yaml
hop_dong:
  task_type: "write-new"
  output_format: "blog_post"
  success_criteria: "1200 từ, anti-AI ≤ 30%, rubric ≥ 75"
  quality_threshold: 75
  ban_truoc: "content"  # → style nhận output từ content
  deadline_hint: "chất lượng"
```

## Giao thác xuôi: Trưởng Ban → BTV

Khi Trưởng Ban giao việc cho BTV chuyên biệt:
- Tác vụ con **cụ thể**, không mơ hồ
- BTV **không được lệch scope** — chỉ làm đúng chuyên môn
- Output **phải theo YAML chuẩn** trong `interface-contract.md`

## Trả kết quả: BTV → Trưởng Ban → Tổng Biên Tập

Khi trả kết quả ngược lên, mỗi tầng phải ghi:

```yaml
output: "[nội dung kết quả]"
confidence: "high" | "medium" | "low"
unresolved_risks:
  - "[claim chưa verify]"
  - "[nguồn chưa chắc chắn]"
dependency_assumptions:
  - "[giả định Ban trước đã confirm]"
```

## Quy tắc Liability

1. **BTV lỗi** → Trưởng Ban phải phát hiện và xử lý trước khi trả về Tổng BT
2. **Trưởng Ban lỗi** → Tổng BT phải phát hiện và xử lý trước khi trả user
3. **Không được trả kết quả thô** nếu task cần xuất bản hoàn chỉnh
4. **Không đổ lỗi xuống dưới** — tầng trên chịu trách nhiệm kiểm soát chất lượng tầng dưới

## Quy trình Khôi phục

Khi phát hiện output không đạt:
1. Xác định Ban/BTV nào gây lỗi
2. Giao lại task với ghi chú REVISE cụ thể
3. Nếu REVISE 2 lần vẫn lỗi → REJECT → escalate lên Tổng BT
4. Tổng BT quyết định: retry / chuyển Ban khác / hỏi user
