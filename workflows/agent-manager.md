---
description: Workflow quản lý Agents chuyên sâu (Mission Control) - Biến mỗi task thành một dự án Multi-Agent
---

## Phase 1: Mission Control (Planning)

1. **Analyze Request**
   - Đọc kỹ yêu cầu của user và context hiện tại.
   - Xác định quy mô task (Simple vs Complex).

2. **Define Squad (Đội ngũ)**
   - Xác định các Role cần thiết. Ví dụ:
     - `Tech Lead`: Architect, plan technology.
     - `Developer`: Implement code.
     - `Tester`: Verify output.
     - `Designer`: UI/UX specs.

3. **Draft Mission Plan**
   - Tạo file `mission_control.md` tại root workspace (hoặc brain artifacts).
   - **Format bắt buộc**:
     ```markdown
     # Mission Control Status: [PLANNING]
     ## Objective
     ...
     ## Squad
     - [ ] Role 1: [Task description]
     - [ ] Role 2: ...
     ## Execution Plan
     1. [Agent Name]: [Action]
     2. ...
     ```

4. **Review Request**
   - Dừng lại và hỏi user: "Tôi đã lập kế hoạch trong `mission_control.md`. Bạn có muốn điều chỉnh gì không hay bắt đầu triển khai (Execute)?"

---

## Phase 2: Execution Loop (Sau khi User Approve)

5. **Update Status**
   - Cập nhật `mission_control.md` -> Status: **[EXECUTION]**.

6. **Execute Squad Tasks**
   - Thực hiện tuần tự hoặc song song các task đã định nghĩa.
   - **Quy tắc**:
     - Mỗi khi chuyển sang Role mới, hãy thông báo: "🔴 **Activating [Role Name]**..."
     - Luôn cập nhật trạng thái vào `mission_control.md` sau khi hoàn thành mỗi mục.

---

## Phase 3: Final Verification

7. **Verification**
   - Kích hoạt `Quality Assurance Agent` để kiểm tra lại toàn bộ kết quả.
   - Update `mission_control.md` -> Status: **[COMPLETED]**.

8. **Handover**
   - Báo cáo tổng kết cho User.
