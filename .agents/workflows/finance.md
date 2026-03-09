---
description: Giao việc kế toán - tài chính cho Jarvis — báo cáo tài chính, bảng lương, phân tích chi phí
---
// turbo-all

## Workflow: /finance — Kế Toán & Tài Chính

1. Đọc file `.agents/workflows/jarvis.md` để hiểu quy trình Jarvis
2. Xác định task_type = "finance"
3. Jarvis tự động route skills: `xlsx`, `data-analysis`, `startup-financial-modeling`
4. Nếu cần báo cáo PDF → thêm skill `pdf`
5. Nếu cần trình bày → thêm skill `pptx`
6. Thực hiện theo quy trình delegation-chain
7. ⚠️ Số liệu tài chính PHẢI verify bằng chứng trước khi report
8. Trả attestation + bằng chứng cho CEO
