---
name: evidence-driven-verification
description: Xác minh dựa trên bằng chứng, áp dụng trước khi tuyên bố hoàn thành một công việc, debug xong, hoặc vượt qua các test cases. Kết hợp ABM LUẬT 2 và verification-before-completion.
---

# Evidence-Driven Verification (Xác Minh Dựa Trên Bằng Chứng)

Tích hợp ABM LUẬT 2 ("Bằng Chứng Trước Khi Khẳng Định") và củng cố thành một quy trình xác minh tối ưu trước khi kết luận hoàn thành tác vụ.

**Nguyên tắc cốt lõi:** CHỨNG MINH trước khi TUYÊN BỐ. Không có evidence (bằng chứng) = Không có kết luận (hoàn thành).

## Khi nào sử dụng (Triggers)
Auto-activate triggers (VN): "xác minh kết quả", "chứng minh chạy được", "xác minh không lỗi", "chạy test kiểm chứng", "kiểm tra bằng chứng", "nghiệm thu"
Auto-activate triggers (EN): "evidence verification", "verify behavior", "ensure it works", "proof of success", "acceptance verification"

Sử dụng bất cứ khi nào bạn định kết luận: "Task này đã xong", "Code này đã chạy được", "Lỗi này đã sửa xong".

## Luật Sắt (The Iron Law)

```
KHÔNG TUYÊN BỐ "XONG" MÀ CHƯA TÌM RA & TRÌNH BÀY BẰNG CHỨNG XÁC MINH MỚI
```

## 5 Bước Xác Minh

```
Bước 1: XÁC ĐỊNH — Lệnh, thao tác, test case nào chứng minh output hoạt động?
Bước 2: CHẠY — Thực thi lệnh kiểm tra (MỚI nhất, đầy đủ nhất, fresh execution).
Bước 3: ĐỌC — Phân tích toàn bộ output, kiểm tra exit codes, check đếm failures/warnings.
Bước 4: XÁC NHẬN — Output có đủ mạnh để xác nhận kết quả thành công không?
Bước 5: KẾT LUẬN — Chỉ khi vượt qua 4 bước trên mới tuyên bố "Đã xong" kèm bằng chứng.
```

## Bảng Đối Chiếu Sự Thật (Bảng Xác Minh)

| Tuyên bố (Claim) | Yêu cầu Bằng Chứng | Ví dụ KHÔNG Hợp Lệ |
|---|---|---|
| "Tests pass" | Run & trả Output: 0 failures | "Chắc là sẽ pass thôi" / Readme nói pass |
| "Build thành công" | Run build: Exit code 0 | "Linter báo ok" |
| "Bug đã fix" | Test gốc pass + Chạy regression test | "Code file kia đã sửa" |
| "Task hoàn tất" | Checklist verify 100% kèm evidence | "Tất cả file đã lưu" |
| "Agent đã xong" | Cung cấp VCS Diff + Run test logic | Agent rep "Success" là tin |
| "Requirements met" | Traceback line-by-line acceptance | "Tests pass" (test không nói lên AC) |

## Cờ Đỏ Cảnh Báo — PHẢI DỪNG LẠI NHÌN NHẬN

Khi nhận thấy bạn (hoặc Agent) đang biện hộ:
- "Chắc là xong rồi" → Lập tức nhận ra: CHƯA XÁC MINH.
- "Logic có vẻ đúng" → Lập tức nhận ra: CHƯA CÓ BẰNG CHỨNG THỰC THI.
- "Lẽ ra phải chạy, nó là default" → CHƯA CHẠY.
- "Agent gọi là success" → CHƯA XÁC THỰC LẠI ĐỘC LẬP.
- Mừng thầm trước khi bấm run -> Đang làm trái quy trình.
- "Thôi lướt qua một lần này" → KHÔNG CÓ NGOẠI LỆ.

## Các Sự Ngụy Biện Phổ Biến (Rationalizations)

| Ngụy biện | Đánh thức thực tế |
|---|---|
| "Chắc là ok, quá rành rồi" | Vẫn phải CHẠY lệnh kiểm chứng thực thụ |
| "Tôi tin tưởng bản thân/code snippet" | Sự tự tin (Confidence) ≠ Bằng chứng (Evidence) |
| "Agent log output Success" | Verify INDEPENDENTLY (kiểm duyệt đầu ra độc lập) |
| "Đã pass linter rồi mà" | Linter không thay cho compiler và runtime logic error |
| "Cái này đã test bằng cơm (manual) rồi" | Manual không để lại Evidence log, do đó nó vô giá trị trong hệ thống Automated |
| "Làm dài quá mệt rồi" | Sự mệt mỏi ≠ một cái cớ (excuse) |

## ABM Attestation Format (Mẫu Xác Nhận)

Khi qua bước verification thành công, ghi lại Chứng Nhận:

```markdown
## Chứng Nhận Xác Minh

| Hạng mục | Kết quả | Evidence Reference |
|---|---|---|
| Tests | ✅ X/X passed | `[lệnh]` → output snippet |
| Build | ✅ exit 0 | `[lệnh]` → output snippet |
| Scope | ✅ Trong phạm vi | Danh sách Files |
| Requirements | ✅ Đạt 5/5 criteria | Mapping output với Requirement |

**Confidence Index:** 0.95
**Scope Violations:** Không
```

Bất cứ task nào hoàn tất, cũng cần tham chiếu bằng chứng này trong Output cho người dùng.
