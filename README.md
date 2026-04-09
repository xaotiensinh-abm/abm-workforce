<div align="center">
  <img src="https://m.media-amazon.com/images/M/MV5BNGFmOWZiYTEtYTkyMS00ZmJjLThhODctYzllZGQ0NDIyZDZhXkEyXkFqcGc@._V1_QL75_UY281_CR14,0,500,281_.jpg" alt="ABM Workforce Architecture" width="300" style="border-radius: 10px; margin-bottom: 20px;"/>
  <h1>ABM Workforce System 3.0</h1>
  <h3>AI Business Master — Enterprise Harness & Multi-Agent Framework</h3>
  <p>Hệ thống Điều phối Đa Trí Tuệ (Multi-Agent) cấp độ Doanh nghiệp. Thiết kế theo tiêu chuẩn <strong>Awesome Harness Engineering</strong>, tối ưu tuyệt đối cho Google Antigravity IDE và Claude Desktop.</p>
</div>

---

## 🎯 Tổng Quan Hệ Thống

**ABM Workforce** không phải là một thư viện Prompt thông thường. Đây là một **Hệ Sinh Thái AI (AI Operating System)** được cấu trúc theo tiêu chuẩn **Harness Engineering**. Dự án giải quyết triệt để 3 bài toán lớn nhất của AI hiện đại:
1. **Context Window Bloat**: Vỡ ngữ cảnh khi Agent đọc quá nhiều file.
2. **Hallucination & Tool Spam**: Agent gọi nhầm công cụ (tools) liên tục ngốn Token.
3. **Execution Safety**: Thiếu xác minh tự động trước khi hoàn thành công việc.

Hệ thống vận hành theo **Chuỗi Uỷ Quyền (Delegation Chain)** dưới sự dẫn dắt của `Jarvis` (Lead Orchestrator), ký kết các Hợp đồng Thực thi (Contracts), và tự động đánh giá chéo hiệu suất thông qua Trace Grading.

---

## 💎 Cấu Trúc Lớp Vỏ "Harness Engineering" (Core Innovations)

Trong phiên bản Big Update mới nhất, ABM đã quy hoạch về **111 Enterprise Skills** với 4 thành tựu công nghệ cốt lõi:

### 1. Repo-Local Instructions & Progressive Disclosure
Khác với các hệ thống AI cố gắng đọc tất cả file cùng lúc, ABM áp dụng chiến thuật "Tiết lộ Dần dần" (Progressive Disclosure):
- **`CLAUDE.md` & `AGENTS.md`**: Thiết lập "Luật chơi" ngay ở Root Directory. Mọi model AI khi boot vào dự án đều bị khống chế: Chỉ dùng Tiếng Việt, không tùy tiện xóa log, và bắt buộc quét danh mục cấp thấp (`Level 0 Index`) trước.
- **`skills-index-l0.json`**: Danh bạ từ điển nhẹ gọn (~6K tokens) thay thế việc quét toàn bộ ổ cứng, tiết kiệm 90% chi phí Context.

### 2. Context Condensation (Nén Ngữ Cảnh)
Sử dụng siêu-kỹ năng `capability-evolver`, hệ thống liên tục giám sát các Conversation logs dài lê thê (>10,000 tokens) để **Tự động Nén (Condense)** thành các bản tóm tắt mục tiêu ngắn gọn (`goals.md`), giúp Agent không bao giờ bị "mất trí nhớ dài hạn".

### 3. Agent Evals & Observability (Tự Đánh Giá Giám Sát)
Không để Agent tự tung tự tác, ABM tích hợp **Cơ chế Trace Grading**:
- Hệ thống `abm-agent-evals` tự động quét lại log các Tool Calls của chính các Agent sau mỗi Sprint.
- Chấm điểm số lần lặp vô hạn, số thao tác thừa, và đệ trình báo cáo JSONL tại `.agents/traces/evals_log.jsonl`. CEO hoàn toàn giám sát được chất lượng nhân sự AI.

### 4. MCP Registry & 9Router Proxy
- Hỗ trợ **Model Context Protocol (MCP)** chuẩn mực qua kho đăng ký tập trung `_abm/_config/mcp-registry.yaml`.
- Tích hợp natively với `claude-router.sh`, giúp định tuyến mọi traffic qua Proxy nội bộ với độ trễ thấp và chi phí tối ưu nhất trong khi vẫn móc nối vạn năng tới Local Nodes, N8N, Docker...

---

## 🧠 Mô Hình Cấu Trúc Tập Đoàn (Virtual Enterprise Ecosystem)

Nhờ sự hỗ trợ của Kiến trúc Harness, 111 Skills được luân chuyển mượt mà thông qua 10 Phòng Ban Chuyên Trách.

Sử dụng Slash Commands (`/`) trong IDE để gọi tên căn phòng xử lý:

### 👑 Ban Giám Đốc & Điều Phối (Executive Board)
- **`/jarvis` (Orchestrator):** Trưởng bộ phận điều phối. Phân loại tác vụ và định tuyến.
- **`/review` & `/council`:** Hội đồng Thẩm định Tối cao. Check chéo logic đa chiều.
- **`/recap` & `/save`:** Ghi nhớ trạng thái phiên làm việc.

### 💻 Ban Công Nghệ & R&D (Engineering & Tech)
- **`/dev`:** Xử lý Code, Refactor và thực thi kỹ thuật.
- **`abm-review-pr` & `systematic-debugging`:** Khắc tinh của Bug. Logic RCA chuyên sâu.
- **`/security-audit`:** Chuyên gia AppSec Ops đánh giá Input/Output OWASP.
- **`/docs`:** Chuẩn hóa tài liệu theo Diátaxis Framework.

### 📢 Ban Sales & Marketing
- **`/marketing` & `/viet` (Tòa Soạn V3.2):** Cỗ máy Content hạng nặng đa nền tảng.
- **`/sales`:** Tối ưu hóa phễu, định giá (Pricing), chốt Sales Pitch.
- **`/cskh`:** Hỗ trợ quy trình Churn Prevention.

### 🏢 Ban Vận Hành & Hỗ Trợ (Back-Office)
- **`/hr` & `/training`:** Thiết kế khung bài giảng, Workshop và tuyển dụng.
- **`/finance`:** Lập kế hoạch dòng tiền startup, ROI calculator.
- **`/legal`:** Soát xét hợp đồng chuyên nghiệp.

---

## ⚙️ Hướng Dẫn Cài Đặt Khởi Tạo (Deployment)

Dự án cài đặt dễ dàng bằng 1 dòng lệnh vào bất kỳ thư mục Workspace đang trống hoặc dự án đang chạy nào của tổ chức.

**Cho hệ điều hành MacOS / Linux (Bash):**
```bash
bash <(curl -s https://raw.githubusercontent.com/xaotiensinh-abm/abm-workforce/main/install.sh)
```

**Cho hệ điều hành Windows (PowerShell):**
Mở PowerShell dưới quyền Quản trị (Administrator):
```powershell
irm https://raw.githubusercontent.com/xaotiensinh-abm/abm-workforce/main/install.ps1 | iex
```

*Hệ thống sẽ tự động khởi tạo cấu trúc xương sống `.agents/` và `_abm/` vào môi trường làm việc của bạn.*

---

<div align="center">
  <p><b>ABM Workforce</b> — Kiến tạo bởi đội ngũ kỹ thuật Lõi.</p>
  <i>Powered by Agentic Execution Architectures.</i>
</div>
