# Attestation Template — Worker/SubAgent Output Report

## Required Fields (BẮT BUỘC)

task_id: [TG-{nhom}-W{worker}]
status: [xong | xong_co_rui_ro | bi_chan | that_bai]
summary: |
  [Tóm tắt kết quả trong 2-3 câu]
files_changed:
  - [đường dẫn file 1]
  - [đường dẫn file 2]
evidence:
  - [Screenshot URL hoặc terminal output]
  - [Test results]
confidence: [0.0 - 1.0]
scope_violations: [co | khong]
budget_used: [số tool calls / thời gian]

## Validation Rules
- status = 'xong' → confidence >= 0.8 BẮT BUỘC
- evidence PHẢI có ít nhất 1 item (không được trống)
- files_changed PHẢI list chính xác (không 'nhiều files')
- scope_violations = 'co' → Jarvis PHẢI review ngay
