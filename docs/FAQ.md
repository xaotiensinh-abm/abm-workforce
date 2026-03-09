# ❓ FAQ — Câu Hỏi Thường Gặp

## Mục Lục

1. [ABM Workforce là gì?](#1-abm-workforce-là-gì)
2. [Cài đặt như thế nào?](#2-cài-đặt-như-thế-nào)
3. [Làm sao biết nên dùng lệnh nào?](#3-làm-sao-biết-nên-dùng-lệnh-nào)
4. [Skill là gì? Có bao nhiêu skills?](#4-skill-là-gì)
5. [Làm sao thêm skill mới?](#5-thêm-skill-mới)
6. [Lệnh không chạy / AI không hiểu?](#6-lệnh-không-chạy)
7. [Làm sao lưu công việc?](#7-lưu-công-việc)
8. [Health check hệ thống?](#8-health-check)
9. [Email sandbox là gì?](#9-email-sandbox)
10. [9 phòng ban mapping như thế nào?](#10-phòng-ban)

---

## 1. ABM Workforce là gì?

**ABM (AI Business Master) Workforce** là hệ thống AI đa agent điều phối doanh nghiệp. Jarvis — Trưởng Điều Phối — quản lý 5 SubAgents, 10 Workers, 66 Skills, phục vụ 9 phòng ban.

**Khác biệt với AI thông thường:**
- Mọi task đều có **hợp đồng** (scope, criteria)
- Mọi kết quả đều có **bằng chứng** (evidence)
- **100% tiếng Việt**

---

## 2. Cài đặt như thế nào?

```bash
git clone https://github.com/xaotiensinh-abm/abm-workforce.git
cd abm-workforce
```

Mở trong **Antigravity** hoặc IDE hỗ trợ `.gemini/` rules. Không cần cài dependencies.

---

## 3. Làm sao biết nên dùng lệnh nào?

| Bạn muốn... | Gõ lệnh |
|-------------|---------|
| Menu tổng | `/jarvis` |
| Viết content | `/marketing` |
| Tuyển dụng | `/hr` |
| Báo cáo tài chính | `/finance` |
| Bán hàng | `/sales` |
| CSKH | `/cskh` |
| Pháp lý | `/legal` |
| Sửa code | `/dev` |
| Đánh giá | `/review` |
| Tài liệu | `/docs` |
| Báo cáo | `/report` |
| Lưu tiến độ | `/save` |

**Hoặc nói trực tiếp** — Jarvis tự phân loại:
```
"Viết email marketing cho sản phẩm X"
→ Jarvis tự route → marketing → load skills → thực hiện
```

---

## 4. Skill là gì?

Skill = bộ hướng dẫn chuyên sâu cho AI. Mỗi skill là file `SKILL.md` với:
- **name** + **description**: AI biết khi nào dùng
- **Sử dụng khi**: Điều kiện kích hoạt
- **KHÔNG sử dụng khi**: Tránh dùng sai → cross-reference skill khác
- **Hướng dẫn chi tiết**: Cách thực hiện

**Hiện có 66 skills** trong 10 nhóm: Hệ thống, Marketing, Phát triển, Web, Văn phòng số, HR, Phân tích, Nâng cao, Multimedia.

---

## 5. Thêm skill mới

```
/jarvis → skill-creator
```

7 pha: Thu thập intent → Phỏng vấn → Viết SKILL.md → Test → Đánh giá → Tối ưu → Đăng ký manifest.

Hoặc sync từ community:
```
/skill-sync
```

---

## 6. Lệnh không chạy / AI không hiểu?

**Checklist xử lý:**

1. ✅ File `.gemini/RULES.md` có tồn tại?
2. ✅ IDE có hỗ trợ `.gemini/` rules?
3. ✅ Đã gõ `/jarvis` để kích hoạt?
4. ✅ Thử mô tả yêu cầu bằng tiếng Việt đơn giản hơn

**Chạy health check:**
```bash
pwsh scripts/health-check.ps1 -Verbose
```

---

## 7. Lưu công việc

```
/save
```

3 loại save:
- **task_save**: Sau khi xong 1 task
- **daily_save**: Cuối ngày làm việc
- **milestone_save**: Đạt cột mốc quan trọng

File lưu tại: `_abm/Context-Layer/Second-Brain/memory/saves/`

---

## 8. Health check hệ thống

```bash
pwsh scripts/health-check.ps1
```

Kiểm tra 6 mục:
1. **Sync**: Skills ↔ KB ↔ Manifest
2. **Frontmatter**: name, description
3. **KHÔNG sử dụng khi**: Coverage
4. **Routing**: Routes + fallback
5. **Components**: SubAgents, Workers, Workflows
6. **File integrity**: Empty files, core files

Thêm `-Verbose` để xem chi tiết, `-Fix` để tự sửa.

---

## 9. Email sandbox là gì?

Skill `agent-email-cli` có **sandbox mode mặc định BẬT**:
- AI soạn email → hiển thị **PREVIEW**
- CEO review → gõ "ok gửi" → mới gửi thật
- Nếu không confirm → **KHÔNG gửi**

Tránh gửi email nhầm ra ngoài.

---

## 10. 9 phòng ban mapping như thế nào?

| Phòng ban | Workflow | Coverage |
|-----------|----------|:--------:|
| Ban Giám Đốc | `/jarvis`, `/review` | 100% |
| HC - Nhân Sự | `/hr`, `/docs` | 80% |
| Kế Toán | `/finance`, `/report` | 80% |
| Marketing | `/marketing` | 100% |
| Kinh Doanh | `/sales` | 80% |
| CSKH | `/cskh` | 80% |
| IT | `/dev` | 100% |
| Vận Hành | — | 30% |
| Pháp Chế | `/legal` | 50% |

Mỗi phòng ban có agent, skills, workflow riêng. Chi tiết xem README.md.
