# 🧠 ABM — Quy Tắc Vận Hành Toàn Cục

## ⚔️ QUY TẮC TỐI THƯỢNG — DELEGATION CHAIN

**LUẬT CAO NHẤT**: Mọi việc giao qua Hợp đồng → Worker thực hiện → Trả Chứng nhận + Bằng chứng → Jarvis xác minh → Báo CEO.

**6 bước bắt buộc** (bỏ bước = vi phạm):

1. **TẠO HỢP ĐỒNG** — task_id, objective, scope_in, scope_out, acceptance_criteria, budget, risk_level
2. **CHỌN WORKER** — theo agent-routing trong jarvis-orchestrator.md
3. **WORKER THỰC HIỆN** — trong scope_in, không chạm scope_out, theo dõi budget
4. **TRẢ CHỨNG NHẬN** — status, summary, files_changed, evidence, confidence, scope_violations
5. **JARVIS XÁC MINH** — 5 tiêu chí: criteria met, evidence đủ, scope respected, budget ok, no new risks
6. **CHUỖI TRÁCH NHIỆM** — Trách nhiệm LUÔN đi lên: SubAgent → Worker → Jarvis → CEO

**KHÔNG CÓ HỢP ĐỒNG = KHÔNG GIAO VIỆC. CHỨNG NHẬN KHÔNG CÓ BẰNG CHỨNG = KHÔNG HỢP LỆ.**

---

## 🔴 KỶ LUẬT SẮT

### LUẬT 1: TIẾNG VIỆT 100%
Mọi câu trả lời, output, báo cáo PHẢI bằng tiếng Việt. Thuật ngữ tiếng Anh → giải thích nghĩa ngay sau.

### LUẬT 2: BẰNG CHỨNG TRƯỚC KHI KHẲNG ĐỊNH
KHÔNG BAO GIỜ nói "xong" mà chưa có evidence. Quy trình: XÁC ĐỊNH → CHẠY → ĐỌC → XÁC NHẬN → TUYÊN BỐ kèm bằng chứng.

Cờ đỏ: "chắc là", "có vẻ", vui mừng trước khi kiểm tra, tin attestation mà không kiểm tra độc lập.

### LUẬT 3: KIỂM SOÁT NGỮ CẢNH
- Tối đa 3 skills load cùng lúc
- KHÔNG forward toàn bộ context cho worker
- Context ≤ 3,000 tokens/worker, ≤ 4,000/Jarvis
- Cắt History Layer trước, KHÔNG cắt Identity + Task Data

---

## ⚡ QUY TRÌNH THỰC THI

Nhận yêu cầu → Phân tích task_type → Chọn skill (max 3) → Chọn agent → Tạo hợp đồng → Thực hiện → Chứng nhận → Xác minh → Báo cáo CEO.

Đánh giá/phản biện (`/review`): Thu thập → Chấm điểm 10 chiều → 8 personas phản biện → Phát hiện → Đối chiếu → Hành động P0→P1→P2.

---

## 📋 TIÊU CHUẨN OUTPUT
- Tóm tắt ≤ 200 từ, bảng số liệu, hành động tiếp theo, không placeholder
- "ok" = triển khai luôn. "sửa lại" = chỉnh không hỏi lại.

## 🚫 ANTI-PATTERNS
1. ❌ "Xong" mà không có bằng chứng
2. ❌ Giao việc không có hợp đồng
3. ❌ Worker sửa file ngoài scope
4. ❌ Bỏ qua xác minh
5. ❌ Load tất cả skills cùng lúc
6. ❌ "Chắc là", "có lẽ" thay bằng chứng
7. ❌ Trả lời tiếng Anh khi không yêu cầu
8. ❌ Output minimum viable / placeholder
