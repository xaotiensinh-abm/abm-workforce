---
description: Giao việc pháp chế - tuân thủ cho Jarvis — hợp đồng, văn bản pháp lý, compliance
---
// turbo-all

## Workflow: /legal — Pháp Chế & Tuân Thủ

1. Đọc file `.agents/workflows/jarvis.md` để hiểu quy trình Jarvis
2. Xác định task_type = "legal"
3. Jarvis tự động route skills: `docx`, `office-documents`, `internal-comms`
4. Nếu cần PDF → thêm skill `pdf`
5. Thực hiện theo quy trình delegation-chain
6. ⚠️ Văn bản pháp lý PHẢI được CEO review trước khi finalize
7. Trả attestation + bằng chứng cho CEO
