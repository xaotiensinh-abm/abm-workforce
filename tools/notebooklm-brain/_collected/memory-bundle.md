# ABM Workforce — Session Memory
# Bộ nhớ dài hạn: task history, session logs, patterns
# Generated: 2026-03-16 09:05
# By: ABM - DũngTQ


============================================================
# TASK LOG — Lịch sử công việc
============================================================

# Task Log — JARVIS Multi-Agent System
# Append-only log. Every contract completion creates 1 entry.
# Used by: knowledge-crystallizer, capability-evolver, HEARTBEAT

log:
  - task_id: "TG-001-W1"
    timestamp: "2026-03-08T14:00:00+07:00"
    type: "hr"
    worker: "hr-specialist"
    status: "COMPLETED"
    confidence: 0.85
    files_changed: 1
    retries: 0
    human_gate: false
    risk_level: "low"
    roma_tier: "Tier3-Content"
    skills_used: ["hr-operations"]
    summary: "Tạo JD Frontend Developer — 2 năm kinh nghiệm, React, HCM"

  - task_id: "TG-002-W1"
    timestamp: "2026-03-08T14:30:00+07:00"
    type: "marketing"
    worker: "marketing-specialist"
    status: "COMPLETED"
    confidence: 0.90
    files_changed: 4
    retries: 0
    human_gate: false
    risk_level: "low"
    roma_tier: "Tier3-Content"
    skills_used: ["email-marketing", "copywriting", "marketing-psychology"]
    summary: "Email sequence 4 bước giới thiệu sản phẩm mới — welcome, nurture, offer, re-engage"

  - task_id: "TG-003-W1"
    timestamp: "2026-03-08T15:00:00+07:00"
    type: "report"
    worker: "business-analyst"
    status: "COMPLETED"
    confidence: 0.80
    files_changed: 1
    retries: 1
    human_gate: false
    risk_level: "medium"
    roma_tier: "Tier2-Intelligence"
    skills_used: ["data-analysis", "office-documents"]
    summary: "Báo cáo kinh doanh tháng 3 — KPI dashboard + recommendations"

  - task_id: "TG-004-W1"
    timestamp: "2026-03-08T15:30:00+07:00"
    type: "docs"
    worker: "office-manager"
    status: "COMPLETED"
    confidence: 0.88
    files_changed: 1
    retries: 0
    human_gate: false
    risk_level: "low"
    roma_tier: "Tier3-Content"
    skills_used: ["office-documents", "workflow-automation"]
    summary: "SOP onboarding khách hàng mới — 12 steps + automation blueprint"

  - task_id: "TG-005-W1"
    timestamp: "2026-03-08T16:00:00+07:00"
    type: "marketing"
    worker: "marketing-specialist"
    status: "COMPLETED"
    confidence: 0.92
    files_changed: 30
    retries: 0
    human_gate: false
    risk_level: "low"
    roma_tier: "Tier3-Content"
    skills_used: ["content-strategy", "social-content", "copywriting"]
    summary: "Content calendar tháng 4 — 30 posts Facebook + LinkedIn, chủ đề ra mắt sản phẩm"

# --- KPI SUMMARY ---
# Total tasks: 5
# Success rate: 100% (5/5)
# Avg confidence: 0.87
# Retry rate: 4% (1 retry / 5 tasks)
# Skills most used: copywriting (2), office-documents (2)
# Agents most used: marketing-specialist (2)



============================================================
# SESSION: SESSION-002-2026-03-13.md
============================================================

# SESSION-002 — Tài Liệu & Slide Đào Tạo Antigravity.Google

**Ngày**: 2026-03-13 22:46
**Loại**: milestone_save
**Workspace**: G:\AGY

---

## Tóm tắt phiên
Xây dựng hoàn chỉnh tài liệu đào tạo nội bộ Antigravity.Google (.md 15 chương) và bộ slide đào tạo 43 trang HTML TailwindCSS. Trải qua nhiều vòng redesign: dark theme → light theme → mở rộng nội dung chi tiết hướng business, bỏ coding examples.

## ✅ Đã hoàn thành
- Deep research Antigravity.Google (web, docs, updates T3/2026)
- Tạo tài liệu đào tạo .md 15 chương từ cơ bản đến nâng cao
- Tạo slide deck HTML + TailwindCSS CDN (43 slides)
- Redesign UI: dark → light theme, màu sắc tươi trẻ pastel
- Scale up bố cục: icon, text, cards cân đối viewport
- Mở rộng từ 19 → 43 slides với nội dung chi tiết
- Nội dung hướng business: viết proposal, email KH, báo cáo KPI, phân tích thị trường
- Thuật ngữ Anh-Việt có phiên âm + ví dụ

## 🔄 Đang làm dở
- Không có — slide và tài liệu hoàn chỉnh

## ❌ Bị chặn / Issues
- Không có blocker

## 📁 Files thay đổi
### Tạo mới
- `_abm-output/TAI-LIEU-DAO-TAO-ANTIGRAVITY-GOOGLE.md` — Tài liệu đào tạo 15 chương
- `_abm-output/slides/index.html` — 43 slides TailwindCSS light theme
- `_abm-output/slides/styles.css` — CSS gốc (đã thay bằng TailwindCSS inline)

### Sửa đổi
- `_abm-output/slides/index.html` — Nhiều lần: dark→light, scale up, mở rộng 19→43 slides

## 💡 Quyết định quan trọng
- Dùng TailwindCSS CDN thay CSS thuần — CEO yêu cầu
- Light theme + pastel gradient — CEO yêu cầu "giao diện sáng, tươi trẻ"
- Bỏ mọi ví dụ coding, thay bằng ví dụ business — CEO yêu cầu
- Single-file HTML (không cần server) — thuận tiện cho đào tạo nội bộ
- 43 slides chi tiết — CEO yêu cầu tối thiểu 40 trang

## 🧠 Kiến thức mới
- Antigravity.Google ra mắt 18/11/2025, miễn phí, 6 AI models
- Update T3/2026: Auto-continue, Async feedback, AGENTS.md, AI Credits
- Pricing: Individual $0, Developer (Google One AI), Team (Workspace Ultra), Org (Coming Soon)
- AI Credits: $25 = 2,500 credits, dùng khi hết quota miễn phí
- Competitors: Cursor ($20), Windsurf ($15), GitHub Copilot ($10)

## 📋 Việc cần làm tiếp (NEXT SESSION)
1. Thu thập feedback sau buổi đào tạo nội bộ
2. Bổ sung screenshots/GIFs giao diện thật của Antigravity vào slides
3. Cân nhắc tạo bản PDF từ slides HTML
4. Cập nhật nội dung nếu có update mới sau T3/2026

## 🔗 References
- `_abm-output/TAI-LIEU-DAO-TAO-ANTIGRAVITY-GOOGLE.md` — tài liệu gốc
- `_abm-output/slides/index.html` — slide deck cuối cùng
- `antigravity.google` — website chính thức



============================================================
# SESSION: SESSION-003-2026-03-14.md
============================================================

# SESSION-003 — Nâng Cấp Giáo Trình Đào Tạo ABM Workforce v2.0

**Ngày**: 2026-03-14 08:12
**Loại**: milestone_save
**Workspace**: G:\AGY

---

## Tóm tắt phiên
Tái cấu trúc hoàn toàn giáo trình đào tạo ABM Workforce từ 8 phần sơ sài → 10 phần chi tiết, tập trung vibe working theo công việc thực tế ABMEdu.vn. Đưa hướng dẫn cài đặt lên đầu. Tích hợp triết lý Brain-First, Done-With-You, 4D Model. Cài pandoc và đóng gói DOCX thành công.

## ✅ Đã hoàn thành
- Nghiên cứu giáo trình cũ (1087 dòng, 8 phần) + 8 KI artifacts
- Đọc tài liệu Coaching 1-1 ABMEdu (222 dòng, 4 phần, 20+ modules)
- Truy cập abmedu.vn lấy thông tin: 3 tầng đào tạo, 6 chương trình, tầm nhìn/sứ mệnh
- Lập kế hoạch nâng cấp (implementation_plan.md) — CEO approved "LGTM"
- Viết Phần 1: Cài đặt & Khởi động (đưa lên đầu, 5 bước + checklist)
- Viết Phần 2: Antigravity & ABM Workforce là gì (bảng so sánh, sơ đồ DCM)
- Viết Phần 3: Giao tiếp Jarvis (18 commands, 10 mẹo prompt, 5 lab chi tiết)
- Viết Phần 4: Vibe Working Marketing & Content (FB, Email, SEO, Chatbot)
- Viết Phần 5: Vibe Working Bán hàng, CSKH & Vận hành (Proposal, SOP, KPI)
- Viết Phần 6: Vibe Working Đào tạo, Branding & Đóng gói Tri thức
- Viết Phần 7: Hiểu cấu trúc ABM Workforce (routing, 55 skills, 6 nhóm)
- Viết Phần 8: Xây dựng Workflow & Tạo Skill (7 bước, template)
- Viết Phần 9: Agent, Knowledge & Second Brain (SOUL.md, 5-Layer, 4 tầng)
- Viết Phần 10: Phụ lục — FAQ 23 câu + Bảng tham chiếu 18 commands + 10 skills
- Sửa lỗi URL: antigravity.dev → antigravity.google
- Xóa thông tin sai về bản Mobile
- Cài pandoc v3.9 (winget)
- Đóng gói DOCX thành công

## 🔄 Đang làm dở
- Đóng gói PDF — pandoc cần xelatex (chưa cài), đã tạo HTML styled để in PDF thủ công

## ❌ Bị chặn / Issues
- PDF engine: xelatex chưa cài, cần MiKTeX hoặc TeX Live (~2GB) → đề xuất CEO in PDF từ HTML bằng Ctrl+P

## 📁 Files thay đổi
### Tạo mới
- `_abm-output/GIAO-TRINH-DAO-TAO-ABM-WORKFORCE.docx` — Giáo trình DOCX (pandoc)
- `_abm-output/GIAO-TRINH-DAO-TAO-ABM-WORKFORCE-print.html` — HTML styled cho in PDF
- `_abm-output/print-style.css` — CSS cho bản in

### Sửa đổi
- `_abm-output/GIAO-TRINH-DAO-TAO-ABM-WORKFORCE.md` — Viết lại hoàn toàn từ 1087 → 1274 dòng, tái cấu trúc 10 phần

## 💡 Quyết định quan trọng
- Đảo cấu trúc: Cài đặt lên Phần 1 (thay vì Phần 8 cũ) — theo yêu cầu CEO
- Thêm 3 phần Vibe Working mới (4-6) — theo yêu cầu CEO tập trung công việc ABMEdu
- Tích hợp triết lý ABMEdu (Brain-First, Done-With-You, 4D) vào giáo trình
- URL chính xác: antigravity.google (không phải antigravity.dev)
- Không có bản Mobile chính thức

## 🧠 Kiến thức mới
- ABMEdu.vn có 3 tầng đào tạo: Foundation → Skill Labs → Capstone Clinics
- 6 chương trình đào tạo: 7 Ngày Online, Offline 4 buổi, SMEs Blended, BECA, Giáo viên 4.0, VIP Community
- Coaching 1:1 Platinum: 250 triệu, 12 tháng, 24 buổi, triết lý Done-With-You
- Mô hình 4D: Define → Design → Deliver → Duplicate
- URL Antigravity chính xác: https://antigravity.google

## 📋 Việc cần làm tiếp (NEXT SESSION)
1. Cài MiKTeX/TeX Live để tạo PDF bằng pandoc, hoặc CEO in PDF từ HTML
2. Git commit + push giáo trình mới
3. Review giáo trình với học viên thử → thu thập feedback
4. Cân nhắc bổ sung hình ảnh/infographic vào giáo trình

## 🔗 References
- `_abm-output/GIAO-TRINH-DAO-TAO-ABM-WORKFORCE.md` — Giáo trình chính
- `G:\07_Knowledge\Coaching 1-1 tai lieu.md` — Tài liệu coaching ABMEdu
- `https://abmedu.vn` — Website chính thức
- `https://antigravity.google` — Antigravity IDE



============================================================
# SESSION: SESSION-004-2026-03-14.md
============================================================

# SESSION-004 — Nâng cấp Giáo Trình ABM Workforce → Web Premium + Deploy Netlify

**Ngày**: 2026-03-14 10:03
**Loại**: milestone_save
**Workspace**: G:\AGY

---

## Tóm tắt phiên
Chuyển đổi file HTML giáo trình ABM Workforce (2321 dòng) thành web app TailwindCSS v4 premium. Deploy lên Netlify. Thực hiện audit phản biện đa chiều 8 personas, chấm điểm 10 chiều. Fix toàn bộ 15 vấn đề P0-P2.

## ✅ Đã hoàn thành
- Tạo dự án `giao-trinh-web/` với build script chuyển đổi HTML → TailwindCSS
- Design premium: dark/light mode, sidebar scroll spy, code blocks + copy
- Deploy Netlify thành công → https://giao-trinh-abm-workforce.netlify.app
- Audit phản biện 8 personas: Hacker, Auditor, CEO, Architect, Pragmatist, Competitor, Operator, New Hire
- Fix P0: Logo ABM, Search modal (Ctrl+K), CTA bar conversion
- Fix P1: Sidebar collapsible 3 nhóm (🟢🟡🔴), Reading time auto, Hero animated orbs, Netlify `_headers`, OG meta đầy đủ, Progress tracker %
- Fix P2: Print/PDF button, Progress tracking localStorage, Section dots, Accessibility (skip-link, aria-labels, focus-visible)

## 🔄 Đang làm dở
- Không có — tất cả đã hoàn thành

## ❌ Bị chặn / Issues
- Custom domain `docs.abmedu.vn` — cần CEO trỏ DNS CNAME về Netlify
- TailwindCSS CDN 300KB — cần PostCSS build + purge (Node.js setup)

## 📁 Files thay đổi
### Tạo mới
- `_abm-output/giao-trinh-web/index.html` — Trang chính ~107KB, TailwindCSS v4
- `_abm-output/giao-trinh-web/style.css` — Custom CSS (hero orbs, sidebar, print, accessibility)
- `_abm-output/giao-trinh-web/app.js` — JS logic (dark mode, search, progress tracking, reading time)
- `_abm-output/giao-trinh-web/build.js` — Node.js build script chuyển đổi HTML
- `_abm-output/giao-trinh-web/logo.png` — Logo ABM từ abmedu.vn
- `_abm-output/giao-trinh-web/_headers` — Netlify security + cache headers

### Sửa đổi
- Không có file cũ bị sửa (dự án mới hoàn toàn)

## 💡 Quyết định quan trọng
- Dùng TailwindCSS v4 CDN thay vì PostCSS build — ưu tiên tốc độ phát triển
- Dark mode mặc định — phù hợp target CEO/professional
- Sidebar collapsible chia 3 nhóm theo cấp độ — giúp học viên mới không bị overwhelm
- Logo lấy từ abmedu.vn thay vì tạo mới — đảm bảo nhất quán thương hiệu
- CTA bar dẫn về abmedu.vn — conversion path rõ ràng

## 🧠 Kiến thức mới
- Netlify deploy qua MCP tool — không cần CLI, deploy trực tiếp từ Antigravity
- TailwindCSS v4 CDN hỗ trợ dark mode class toggle nhanh
- IntersectionObserver hiệu quả cho reading progress tracking
- `_headers` file cho Netlify — security headers + cache control
- OG meta cần absolute URL cho image (không dùng relative path)

## 📋 Việc cần làm tiếp (NEXT SESSION)
1. **Custom domain** — CEO trỏ DNS `docs.abmedu.vn` CNAME → Netlify
2. **TailwindCSS PostCSS build** — giảm 300KB → ~15KB CSS
3. **AI illustrations** — generate hình minh họa cho mỗi phần giáo trình
4. **Netlify Analytics** — enable tracking đọc giả
5. **A/B test CTA** — theo dõi conversion rate

## 🔗 References
- Live URL: https://giao-trinh-abm-workforce.netlify.app
- Netlify Site ID: fb5eb705-1d82-45ab-a3c0-e8b56ef63722
- Source HTML: `_abm-output/GIAO-TRINH-DAO-TAO-ABM-WORKFORCE.html`
- Audit report: audit-phan-bien.md (artifacts)
- Logo source: https://abmedu.vn/images/logo-320.png



============================================================
# SESSION: SESSION-005-2026-03-15.md
============================================================

# SESSION-005 — Dashboard v4.0: 11 Phòng Ban + Task Detail Modal + /save Pipeline

**Ngày**: 2026-03-15 07:56
**Loại**: milestone_save
**Workspace**: G:\AGY

---

## Tóm tắt phiên
Nâng cấp dashboard ABM Workforce lên v4.0: sidebar 11 phòng ban, fix encoding task-data.js, thêm 6 tasks mới (28 total). Xây dựng task detail modal (click task → slide panel chi tiết thật). Nâng cấp /save workflow v4.0 tự động sync task-history.json → dashboard. Push GitHub 2 lần.

## ✅ Đã hoàn thành
- Dashboard v4.0 — sidebar 11 phòng ban (từ 6 → 11), dynamic department views
- Fix task-data.js encoding tiếng Việt + thêm 6 tasks (22→28)
- Task detail modal — click task → slide panel: mô tả, files, quyết định, bằng chứng, skills, tiến độ
- task-history.json enriched — 28 tasks + detail fields (description, files_changed, decisions, evidence, session_id, duration)
- sync.ps1 v4.0 — export detail, đếm workers, UTF-8
- /save workflow v4.0 — thêm Bước 8 (auto-ghi task-history) + Bước 9 (auto sync dashboard)
- Push GitHub 2 commits: dashboard v4.0 + task detail modal

## 🔄 Đang làm dở
- Không có — tất cả đã hoàn thành

## ❌ Bị chặn / Issues
- sync.ps1 gặp encoding issue khi chạy PowerShell với Unicode → workaround: tạo task-data.js trực tiếp bằng tool

## 📁 Files thay đổi
### Sửa đổi
- `dashboard/index.html` — Dashboard v4.0: sidebar 11 PB + task detail modal (CSS + JS + HTML)
- `dashboard/task-data.js` — 28 tasks + detail fields, encoding UTF-8 đúng
- `dashboard/task-history.json` — 28 tasks + 6 detail fields mới mỗi task
- `dashboard/sync.ps1` — v4.0: export detail, workers, UTF-8
- `.agents/workflows/save.md` — v4.0: thêm bước auto-sync task-history + dashboard

## 💡 Quyết định quan trọng
- Task detail modal dùng slide-in panel (phải) thay vì modal overlay — UX tốt hơn, không che task table
- task-history.json là single source of truth — /save ghi vào đây, sync.ps1 đọc ra task-data.js
- Tạo task-data.js trực tiếp bằng file tool (bypass PowerShell Unicode encoding issue)
- 11 phòng ban xác nhận từ jarvis-orchestrator.md: thêm Đào Tạo, R&D, CSKH, Kế Toán, Pháp Chế, Vận Hành

## 🧠 Kiến thức mới
- PowerShell ConvertTo-Json + Out-File có vấn đề encoding Unicode tiếng Việt trên Windows
- Workaround: dùng [System.IO.File]::WriteAllText() với UTF8Encoding($false) cho BOM-free
- Dashboard file:// protocol hoạt động tốt trên Chrome/Edge (không cần web server)
- Slide-in panel UX pattern: position fixed, right transition, backdrop-filter blur

## 📋 Việc cần làm tiếp (NEXT SESSION)
1. Fix sync.ps1 encoding issue — hoặc viết bằng Node.js thay PowerShell
2. Test /save workflow end-to-end trong phiên mới — verify pipeline đầy đủ
3. Thêm tasks mới khi có công việc mới — task-history.json auto-grow
4. Cân nhắc deploy dashboard lên Netlify (không chỉ local file://)
5. Research community skills mới cho ABM

## 🔗 References
- Dashboard: `dashboard/index.html` (file:// local)
- Task data pipeline: `task-history.json` → `sync.ps1` → `task-data.js`
- /save workflow: `.agents/workflows/save.md`
- GitHub: github.com/xaotiensinh-abm/abm-workforce



============================================================
# LESSONS LEARNED — Bài học kinh nghiệm
============================================================

﻿# Lessons Learned — Bài Học Quan Trọng

## 1. Skill Explosion Problem (2026-03)
- 116 skills → context overload → giảm xuống 76
- Lesson: Quality > Quantity, luôn audit trước khi add mới
- Rule: Mỗi skill mới phải qua Skill Generator 9 phases

## 2. Manifests Must Stay Updated
- Manifests outdated = routing sai = output sai
- Lesson: Mỗi lần add/remove skill → update manifest ngay
- Rule: Tạo sync script chạy sau mỗi thay đổi

## 3. Done-With-You ≠ Done-For-You
- Khách mong ABM làm hộ → phải set expectation rõ từ Discovery Call
- Lesson: Disqualify clients không sẵn sàng commit
- Rule: ICP filter trong high-ticket-sales skill

## 4. SubAgents/Workers Must Exist
- Delegation chain thiết kế nhưng không implement → chỉ là tài liệu
- Lesson: Architecture cần implementation, không chỉ design
- Rule: Mỗi SubAgent phải có SOUL.md + Skills + Attestation format



============================================================
# PATTERN: ceo-preferences.yaml
============================================================

# CEO Preferences — Sở thích và kỳ vọng của CEO
# Tri thức tích lũy từ tương tác với user
# Dùng bởi: tất cả agents khi tạo output

preferences:
  communication:
    language: "Vietnamese"
    style: "Thực thi trước, lý thuyết sau"
    reporting: "Bảng tóm tắt ngắn gọn. Dashboard > văn bản dài."
    feedback: "Nói 'ok' = approve full. Nói 'sửa lại' = specific fix."

  content:
    email: "Luôn có A/B subject lines"
    reports: "Executive summary ≤200 words. Data-backed insights."
    jd: "Salary range (không fixed). Include interview scorecard."
    documents: "Action items phải có: what, who, when."

  workflow:
    preference: "Slash commands — /marketing, /hr, /report"
    decision_speed: "Nhanh — ít câu hỏi, nhiều hành động"
    review_style: "Đánh giá đa chiều — 8 perspectives minimum"
    quality_bar: "Không chấp nhận minimum viable — phải premium"

  system:
    naming: "ABM = AI Business Master"
    language_all: "Tiếng Việt cho mọi mô tả, UI, hướng dẫn"
    structure: "Workforce pattern — SubAgents, Workers, Autonomous-Core..."
    evolution: "Liên tục tối ưu — từ 5.55 → 8.72/10 trong 1 session"



============================================================
# PATTERN: failure-patterns.yaml
============================================================

# Failure Patterns — Mẫu thất bại và cách tránh
# Mỗi failure pattern = 1 bài học từ sai lầm
# Dùng bởi: jarvis decision-making, HEARTBEAT red flags

patterns:
  - pattern_id: "FP-001"
    name: "Context Bomb"
    discovered_in: "Critical Review v3"
    category: "architecture"
    description: "Load tất cả 25 skills vào orchestrator → 3,500 tokens trước khi user nói gì"
    root_cause: "Liệt kê đầy đủ mọi skill inline thay vì lazy loading"
    impact: "Context window bị lấp → giảm chất lượng response"
    fix_applied: "Context Engineering 5-layer + 3 mandatory only + skill-routing lazy load"
    prevention: "RULE: Mỗi agent tối đa 3 skills loaded cùng lúc"
    severity: "critical"

  - pattern_id: "FP-002"
    name: "Phantom Agents"
    discovered_in: "Critical Review v2"
    category: "governance"
    description: "Agent được tham chiếu trong routing nhưng không có file definition"
    root_cause: "Thêm agent vào permission tree mà không tạo SOUL.md/agent file"
    impact: "Jarvis delegate cho agent không tồn tại → task fail silently"
    fix_applied: "Tạo SOUL.md cho tất cả 5 business agents"
    prevention: "RULE: Dùng add-agent workflow — 5 bước + verification checklist"
    severity: "high"

  - pattern_id: "FP-003"
    name: "Spec Without Evidence"
    discovered_in: "Critical Review v4"
    category: "observability"
    description: "Hệ thống có đầy đủ spec nhưng 0 runtime evidence"
    root_cause: "Chỉ thiết kế framework mà không chạy task thật"
    impact: "Evolver, crystallizer, KPI dashboard = tất cả inert. Auditor score = 3/10."
    fix_applied: "Seed 5 tasks + 3 contracts + 2 attestations"
    prevention: "RULE: Sau khi thêm bất kỳ cơ chế nào → PHẢI chạy ít nhất 1 task để verify"
    severity: "high"

  - pattern_id: "FP-004"
    name: "Manual Multi-File Rename"
    discovered_in: "BMAD → ABM rebrand"
    category: "operations"
    description: "Rename thủ công trên 200+ files → dễ miss, syntax errors"
    root_cause: "PowerShell quoting issues khi dùng inline commands"
    impact: "Script fails → phải viết file .ps1 riêng"
    fix_applied: "Luôn viết script .ps1 riêng cho batch operations"
    prevention: "RULE: Batch operations > 10 files → viết .ps1 script, KHÔNG inline"
    severity: "medium"



============================================================
# PATTERN: rejected-ideas.yaml
============================================================

# Rejected Ideas Backlog
# Creative Strategist ghi lai cac y tuong khong duoc chon
# Review moi thang de reconsider

rejected_ideas: []

# FORMAT:
# - id: "REJ-001"
#   date: "2026-03-10"
#   project: ""
#   idea: ""
#   reason_rejected: ""
#   conditions_to_reconsider: ""
#   potential_future_use: ""
#   score: 0



============================================================
# PATTERN: success-patterns.yaml
============================================================

# Success Patterns — Mẫu thành công đã học
# Mỗi pattern = 1 cách làm đã được chứng minh hiệu quả
# Dùng bởi: knowledge-crystallizer, capability-evolver, jarvis decision-making

patterns:
  - pattern_id: "SP-001"
    name: "Email Sequence Psychology"
    learned_from: ["TG-002-W1"]
    category: "marketing"
    description: "Email sequence 4 bước áp dụng 4 mô hình tâm lý khác nhau"
    recipe:
      step_1: "Welcome email — dùng Reciprocity (cho giá trị miễn phí)"
      step_2: "Nurture email — dùng Authority (chia sẻ expertise)"
      step_3: "Offer email — dùng Scarcity + Urgency (khan hiếm + gấp)"
      step_4: "Re-engage email — dùng Social Proof (bằng chứng xã hội)"
    kpi: "Predicted open rate: 25-35%"
    confidence: 0.9
    times_used: 1

  - pattern_id: "SP-002"
    name: "JD Vietnam Market"
    learned_from: ["TG-001-W1"]
    category: "hr"
    description: "JD cho thị trường IT Việt Nam — cấu trúc + mức lương phù hợp"
    recipe:
      structure: "Overview → Responsibilities (8) → Requirements (6) → Benefits (5) → Interview Process"
      salary_tip: "Luôn range (VD: 15-25M) — không fixed. Tham khảo thị trường."
      bonus: "Thêm Interview Scorecard → hỗ trợ tuyển dụng thực tế"
    confidence: 0.85
    times_used: 1

  - pattern_id: "SP-003"
    name: "Script-Based Restructure"
    learned_from: ["S-002"]
    category: "architecture"
    description: "Dùng PowerShell script cho mọi restructure lớn (>50 files)"
    recipe:
      step_1: "Tạo script — New-Item directories"
      step_2: "Copy-Item files theo mapping"
      step_3: "Chạy verify script — check tất cả paths"
      step_4: "Batch-replace content references nếu paths đổi"
    antipattern: "KHÔNG manual copy — dễ miss files, mất tracking"
    confidence: 0.95
    times_used: 1

  - pattern_id: "SP-004"
    name: "Weighted Scoring Review"
    learned_from: ["CS-001"]
    category: "review"
    description: "Chấm điểm weighted trung thực hơn unweighted"
    recipe:
      top_weights: "Kiến trúc (15%) + Enforcement (15%) = 30% tổng"
      key_insight: "Unweighted inflate score — enforcement thường thấp nhưng quan trọng nhất"
      perspectives: "8 personas minimum — mỗi persona PHẢI có verdict riêng kèm evidence"
    confidence: 0.92
    times_used: 3

