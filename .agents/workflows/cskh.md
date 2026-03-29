---
description: Giao việc chăm sóc khách hàng cho Jarvis — email follow-up, churn prevention, satisfaction
---
// turbo-all

## Workflow: /cskh — Chăm Sóc Khách Hàng

1. Đọc file `.agents/workflows/jarvis.md` để hiểu quy trình Jarvis
2. Xác định task_type = "cskh"
3. Jarvis tự động route skills: `agent-email-cli`, `churn-prevention`, `email-marketing`
4. Nếu cần viết copy → thêm skill `copywriting`
5. Nếu cần tạo tài liệu → thêm skill `docx`
6. Thực hiện theo quy trình delegation-chain
7. ⚠️ Email gửi khách hàng PHẢI được CEO duyệt trước khi gửi
8. Trả attestation + bằng chứng cho CEO
