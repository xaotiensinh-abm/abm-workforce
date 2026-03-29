---
description: Giao việc Kỹ thuật Tự Động Hóa N8N cho Jarvis. Thiết kế luồng, kết nối App và triển khai Automations.
---
// turbo-all

# 🤖 Giao việc Tự Động Hóa N8N (N8N Automation Expert)

## Bước 1: Kích hoạt Jarvis & Phân tách Task
1. Load Jarvis Orchestrator (`/jarvis`).
2. Khai báo Hợp Đồng Ủy Quyền:
   - **Bên giao:** Ban Giám Đốc (CEO).
   - **Bên nhận:** N8N Automation Expert (Lính đánh thuê chuyên nghiệp).
   - **Nhiệm vụ:** Thiết kế, kiểm thử và thiết lập một luồng tự động hóa chạy trơn tru thông qua n8n MCP Server.

## Bước 2: Kích hoạt Chuyên gia N8N
1. Gọi Skill: Load File `.agents/skills/n8n-automation-expert/SKILL.md` để Agent học thuộc cách sử dụng Tool.
2. Trích xuất yêu cầu N8N thực tế từ User prompt:
   - Nếu user yêu cầu "tìm" -> Dùng tool `n8n_search_templates`.
   - Nếu user thiết kế từ đầu -> Tham khảo Tool `n8n_search_nodes`.
   - Nếu sếp yêu cầu Deploy -> Chốt Config JSON xong, xả Tool `n8n_create_workflow` cắm thẳng vào máy chủ n8n đang nối kết.

## Bước 3: Đệ trình Bằng chứng & Hoàn thành
- Tool `n8n_test_workflow` nổ -> Đưa bằng chứng log Test thành công lên bàn Giám Đốc.
- Không có chứng nhận hoàn thành API trả về = Tuyệt đối CẤM báo cáo "Xong việc".
