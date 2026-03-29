---
name: using-superpowers
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: Khởi chạy trước MỌI cuộc hội thoại - thiết lập tư duy truy xuất và sử dụng skill ABM Workforce, BẮT BUỘC ưu tiên gọi Skill trước khi trả lời hoặc hành động.
---

<SUBAGENT-STOP>
Nếu bạn là Subagent (ví dụ: Code Worker, Reviewer) được Delegator/Jarvis phân công một Hợp đồng (Contract) cụ thể, bỏ qua skill này và tập trung vào task.
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
Nếu có dù chỉ 1% khả năng một hệ thống skill có thể áp dụng cho yêu cầu hiện tại, bạn TUYỆT ĐỐI BẮT BUỘC phải gọi tool/skill đó ra để đọc.

NẾU CÓ SKILL PHÙ HỢP CÔNG VIỆC CỦA BẠN, BẠN KHÔNG CÓ QUYỀN LỰA CHỌN. BẠN PHẢI DÙNG NÓ.

Đây là điều khoản không thể thương lượng. Đừng cố vòng vo để chối bỏ trách nhiệm này.
</EXTREMELY-IMPORTANT>

## Trình Tự Ưu Tiên (Instruction Priority)

Các Skill nội bộ của ABM Workforce sẽ ghi đè lên prompt mặc định của hệ thống, tuy nhiên **Mệnh lệnh của CEO/Người dùng luôn đứng cao nhất**:

1. **Chỉ thị trực tiếp của User** (CLAUDE.md, GEMINI.md, AGENTS.md, tin nhắn trực tiếp) — Quyền lực tuyệt đối
2. **Hệ thống Kỹ năng (Skills)** — Ghi đè hệ thống khi có xung đột
3. **System prompt mặc định** — Nền tảng phụ trợ, ưu tiên thấp nhất

Ví dụ: Nếu User bảo "Không dùng TDD" nhưng Skill bảo "Luôn dùng TDD", hãy chiều theo User.

## Cách Gọi Skill

- **Trên Claude Code / IDE:** Dùng tool `Skill`. Khi kích hoạt, đọc kỹ và làm theo. Không tự ý dùng tool File Read để đọc lén nội dung `SKILL.md`.
- **Trên Gemini CLI:** Dùng tool `activate_skill`. Metadata đã được nạp sẵn.

# Hướng Dẫn Kích Hoạt

## Nguyên Tắc Cốt Lõi (The Rule)

**Gọi những skill có vẻ liên quan TRƯỚC BẤT KỲ CÂU TRẢ LỜI HAY HÀNH ĐỘNG NÀO.** 
Ngay cả 1% cơ hội cũng phải kiểm tra. Nếu check xong thấy không hợp lý thì không dùng. 

> **Sơ đồ tư duy (Decision Flowchart):** Được lưu trữ tại `references/process-flow.md`. AI hãy đọc nếu cần rà soát quá trình định tuyến luồng hội thoại.

## Cờ Đỏ (Red Flags)

Nếu bạn vừa có những suy nghĩ sau, HÃY DỪNG LẠI—đây là biểu hiện của sự lười biếng, làm ẩu:

| Suy Nghĩ Ngụy Biện | Sự Thật Phũ Phàng |
|---------|---------|
| "Cái này là câu hỏi đơn giản thôi" | Câu hỏi = Task. Phải check skill. |
| "Tôi cần hỏi lại (Clarify) User trước đã" | Bắt buộc check Skill TRƯỚC khi đặt câu hỏi. |
| "Để tôi đọc lướt qua codebase trước đã" | Kỹ năng định hướng CÁCH khảo sát code. Check trước. |
| "Tôi gõ lệnh search nhanh là ra" | Lệnh bash/search không có tư duy ngữ cảnh. Check skill gốc. |
| "Cái này dùng skill thì to tát quá" | Nếu skill đã sinh ra, BẮT BUỘC phải dùng. |
| "Tôi thuộc lòng nội dung skill này rồi" | Skill luôn được Release bản mới. Phải đọc bản mới nhất. |
| "Tôi sẽ làm fix nhanh file này rồi tính tiếp" | Rủi ro sập hệ thống cao. Kiểm tra gốc gác trước. |
| "Tôi hiểu khái niệm này mà" | Hiểu khái niệm (kiến thức chung) ≠ Tuân thủ quy trình (ABM System). |

## Phân Loại & Ưu Tiên Skill

Khi có nhiều skill có thể áp dụng, sắp xếp thứ tự nạp:

1. **Nhóm Quy trình (Process Skills):** (`brainstorming`, `systematic-debugging`) - Đây là La Bàn. Quyết định HOW (Cách làm).
2. **Nhóm Trực thi (Implementation Skills):** (`frontend-design`, `mcp-builder`) - Đây là Công Cụ. Hỗ trợ quá trình Gõ Code.

"Xây giùm tôi app X" -> Mở `brainstorming` trước, sau đó mới đến các skill frontend.
"Fix cho tôi lỗi này" -> Mở `systematic-debugging` trước.

## Nối Mạch ABM Workforce
Mọi hoạt động phải tuân theo chuỗi **Delegation Chain** của Jarvis:
- Lệnh User đến -> Mọi hành vi lập kế hoạch phải qua `writing-plans` để lập **Hợp Đồng (Contract)**.
- Khi hoàn tất công việc -> Bắt buộc qua `verification-before-completion` để tạo **Chứng Nhận (Attestation)** trước khi báo hiệu "Xong!".
