# ABM-Workforce Repo-Local Instructions (Claude/Gemini/Antigravity)

## 1. Ngôn ngữ & Giao tiếp (MANDATORY)
* **Luôn luôn giao tiếp 100% bằng Tiếng Việt.** 
* Dùng giọng điệu chuyên nghiệp, ngắn gọn, báo cáo số liệu thực tế, KHÔNG chèn placeholders.
* "ok" nghĩa là sếp duyệt -> thực thi luôn, tuyệt đối không hỏi lại.
* "sửa lại" nghĩa là làm lại theo ý sếp.

## 2. Progressive Disclosure (Tiết kiệm Token)
* Kiến trúc ABM hiện có hơn 110 Skills.
* **KHÔNG BAO GIỜ** dùng command để scan và đọc toàn bộ thư mục `_abm/bmm/agents/skills/`.
* Khi cần tra cứu Skill, **HÃY LUÔN ĐỌC** file `_abm/_config/skills-index-l0.json` trước để lấy danh sách cấp 0. Chỉ khi nào tìm đúng Skill phù hợp thì mới đọc vào thư mục chi tiết (Ví dụ: `_abm/bmm/agents/skills/[skill-name]/SKILL.md`).

## 3. Delegation Chain & Bằng Chứng
* Bất cứ tác vụ ủy quyền nào cho SubAgent/Worker đều phải có Hợp đồng (Contract) và Báo cáo Nghiệm thu (Attestation).
* KHÔNG BAO GIỜ chốt "Đã hoàn thành" (hoặc tick checkbox task) khi chưa thu thập Bằng chứng (Evidence) thông qua lệnh verify, run tests, web check. Bằng chứng Trực tiếp > Câu nói.

## 4. Workflows & Artifacts
* Mọi kế hoạch triển khai phải được lưu tại `.gemini/antigravity/brain/[conversation-id]/implementation_plan.md`.
* Theo dõi các bước làm việc tại file `task.md` cũng trong thư mục não bộ trên.
* Xoá bỏ tư duy "Làm thay" - hãy "Tạo vỏ bọc" (Harness): Khi sếp yêu cầu một chức năng mới, đừng vội code cứng. Hãy sinh ra một Skill mới nếu tiến trình đó lặp lại.

## 5. Cấm kỵ
* Tuyệt đối không xóa, dịch chuyển các file gốc tại `_abm/bmm/agents/skills/` nếu không dùng tool hỗ trợ.
* KHÔNG sửa/xóa các Rule hệ thống của người dùng (User Global Rules).
