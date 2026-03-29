# Tài Liệu Chuyên Sâu (Extracted from Lõi)

## 5 Bước Xác Minh (Kết hợp ABM + Superpowers)

```
Bước 1: XÁC ĐỊNH — Lệnh/bước nào chứng minh kết quả?
Bước 2: CHẠY    — Thực thi lệnh kiểm tra (MỚI, đầy đủ, fresh)
Bước 3: ĐỌC     — Toàn bộ output, kiểm tra exit code, đếm failures
Bước 4: XÁC NHẬN — Output CÓ xác nhận kết quả KHÔNG?
Bước 5: CHỈ KHI ĐÓ — Mới tuyên bố KÈM bằng chứng cụ thể
```

## Bảng Xác Minh

| Tuyên bố | Yêu cầu | KHÔNG đủ |
|---|---|---|
| "Tests pass" | Output: 0 failures | "Chắc là pass" |
| "Build thành công" | exit code 0 | "Linter ok" |
| "Bug đã fix" | Test gốc pass + regression test | "Code đã sửa" |
| "Task hoàn tất" | Checklist 100% + evidence | "Đã làm xong" |
| "Agent completed" | VCS diff + verify changes | Agent nói "success" |
| "Requirements met" | Line-by-line checklist | "Tests passing" |

## Cờ Đỏ — DỪNG NGAY

Khi thấy mình nghĩ:
- "Chắc là xong rồi" → CHƯA xác minh
- "Có vẻ đúng" → CHƯA có evidence  
- "Lẽ ra phải chạy" → CHƯA chạy
- "Agent nói thành công" → CHƯA kiểm tra độc lập
- Vui mừng TRƯỚC KHI kiểm tra → SAI quy trình
- "Chỉ lần này thôi" → KHÔNG có ngoại lệ

## Rationalizations (Biện minh)

| Biện minh | Thực tế |
|---|---|
| "Chắc là ok" | CHẠY lệnh kiểm tra |
| "Tôi tin tưởng" | Confidence ≠ evidence |
| "Agent nói success" | Verify INDEPENDENTLY |
| "Linter passed" | Linter ≠ compiler ≠ runtime |
| "Đã test manual" | Manual ≠ automated, không có record |
| "Mệt rồi" | Mệt ≠ excuse |

## ABM Attestation Format

Khi xác minh xong, tạo Attestation:

```markdown
## Chứng Nhận Xác Minh

| Hạng mục | Kết quả | Evidence |
|---|---|---|
| Tests | ✅ X/X passed | `[lệnh]` → output |
| Build | ✅ exit 0 | `[lệnh]` → output |
| Scope | ✅ Trong phạm vi | Files: [list] |
| Requirements | ✅ 5/5 criteria met | Checklist verified |

**Confidence:** 0.95
**Scope violations:** Không
```

## Tích hợp

**Thay thế:** superpowers:verification-before-completion (tất cả chức năng + ABM Attestation)
**Kết hợp:** superpowers:test-driven-development (RED-GREEN verification)
**Kết hợp:** abm-contract-driven-development (Bước 5: Xác minh)


<!-- 📦 Refactored by ABM Skill Architect v1.0 | ABM Workforce | 9-Layer Token Optimized -->