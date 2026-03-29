Dưới đây là **bản thiết kế skill hoàn chỉnh cho `viet-pro`**, ứng dụng trực tiếp 2 ý từ ảnh:

* **Ảnh 1: Delegation Chain Management** → dùng làm **mô hình điều phối phân cấp**: Tổng điều phối → Worker → Sub-agent, trách nhiệm đi xuống, liability đi ngược lên.
* **Ảnh 2: Cấu trúc thư mục hệ nhiều lớp** → dùng làm **kiến trúc file/folder chuẩn**: core, orchestration, context, knowledge base, second brain, outputs, config, verify.

---

# 1. Tư tưởng thiết kế cốt lõi

`viet-pro` không nên là một skill viết đơn lẻ.

Nó nên là một **newsroom engine** gồm:

* **1 Orchestrator trung tâm**
* **nhiều Worker phòng ban**
* **nhiều SubAgent chuyên đề**
* **mỗi tầng có memory, knowledge, tools, second brain riêng**
* **trách nhiệm kết quả luôn dồn ngược về Orchestrator**

Tức là áp dụng đúng logic của ảnh 1:

> **Forward Delegation**
> Tổng biên tập giao việc xuống phòng ban, phòng ban giao tiếp xuống chuyên viên

> **Liability Return**
> Kết quả có lỗi thì trách nhiệm đánh giá và hợp nhất quay ngược lên tầng trên

Và áp dụng đúng tinh thần ảnh 2:

> **Skill không chỉ có prompt**
> mà có engine, orchestration, context layer, knowledge base, second brain, outputs, config, validation

---

# 2. Mục tiêu của skill

`viet-pro` phục vụ 6 nhóm tác vụ chính:

1. **Viết mới**

   * ebook
   * tài liệu
   * sách chuyên môn
   * bài social
   * caption
   * kịch bản video

2. **Sửa bản nháp**

   * làm rõ ý
   * tự nhiên hơn
   * gọn hơn
   * đúng giọng hơn

3. **Chấm bài**

   * thang 100
   * rubric rõ ràng
   * nhận xét theo tiêu chí

4. **Phản biện nội dung**

   * chỉ ra lỗ hổng
   * phản biện luận điểm
   * nêu rủi ro fact / logic / cấu trúc

5. **Deep research trước khi làm**

   * áp dụng cho tất cả hạng mục
   * tìm nguồn
   * phân biệt fact / assumption / opinion

6. **Xuất bản đa định dạng**

   * long-form
   * social đa nền tảng
   * video script

---

# 3. Kiến trúc phân cấp theo ảnh 1

## 3.1. Tầng A — Delegator A / Orchestrator

Tên nội bộ:

* **Editor-in-Chief**
* hoặc **Tổng Biên Tập**

Vai trò:

* nhận yêu cầu người dùng
* phân loại nhiệm vụ
* lập kế hoạch điều phối
* giao việc cho Worker phù hợp
* thu kết quả từ Worker
* chạy kiểm duyệt cuối
* xuất đầu ra cuối cùng

Không trực tiếp làm mọi việc chi tiết.

---

## 3.2. Tầng B — Delegatee B / Worker

Đây là các **phòng ban chính**.

Tôi đề xuất 8 worker chính:

1. **intake-worker**
2. **research-worker**
3. **strategy-worker**
4. **longform-worker**
5. **social-worker**
6. **video-worker**
7. **critique-worker**
8. **quality-worker**

Mỗi worker:

* nhận nhiệm vụ từ Orchestrator
* chia nhỏ cho sub-agent
* tổng hợp đầu ra cấp phòng ban
* trả kết quả lên Orchestrator

---

## 3.3. Tầng C — Sub-delegatee C / SubAgent

Đây là chuyên viên chuyên đề.

Ví dụ:

### `research-worker` có các sub-agent:

* source-finder
* credibility-checker
* contradiction-checker
* citation-organizer

### `longform-worker` có các sub-agent:

* ebook-architect
* document-structurer
* explainer-writer
* tone-refiner

### `social-worker` có các sub-agent:

* facebook-writer
* threads-writer
* linkedin-writer
* short-caption-writer
* repurpose-agent

### `video-worker` có các sub-agent:

* hook-builder
* short-script-writer
* retention-designer
* cta-finisher

### `critique-worker` có các sub-agent:

* rubric-scorer
* logic-critic
* clarity-critic
* revision-advisor

### `quality-worker` có các sub-agent:

* anti-ai-auditor
* consistency-checker
* claim-risk-checker
* final-proofreader

---

# 4. Sơ đồ trách nhiệm

## 4.1. Forward delegation

Luồng giao việc:

Người dùng
→ Editor-in-Chief
→ Worker phù hợp
→ SubAgent phù hợp

## 4.2. Liability return

Luồng trách nhiệm:

SubAgent lỗi
→ Worker chịu trách nhiệm hợp nhất
→ Editor-in-Chief chịu trách nhiệm đầu ra cuối

Tức là skill phải có rule:

* tầng dưới được phép chuyên môn hóa
* tầng trên phải có nghĩa vụ kiểm soát chất lượng
* không được trả kết quả thô chưa qua hợp nhất nếu task cần xuất bản hoàn chỉnh

---

# 5. Cấu trúc phòng ban hoàn chỉnh

## 5.1. Ban Tổng Biên Tập

Nhiệm vụ:

* định tuyến yêu cầu
* quyết định pipeline
* kiểm soát tiêu chuẩn chung
* hợp nhất đầu ra cuối
* quyết định khi nào cần research lại hoặc phản biện lại

Memory riêng:

* trạng thái task hiện tại
* room map: phòng ban nào đã tham gia
* mục tiêu cuối
* format đầu ra
* risk flags

Knowledge riêng:

* routing rules
* policy tổng
* output standards
* escalation rules

Tools riêng:

* task classifier
* workflow selector
* merge controller
* final gate checker

Second brain riêng:

* mẫu pipeline hiệu quả
* pattern phối hợp phòng ban
* lỗi orchestration thường gặp
* heuristics chọn worker

---

## 5.2. Ban Tiếp Nhận & Giải Mã Brief

Nhiệm vụ:

* bóc tách brief
* xác định loại task
* xác định đối tượng
* xác định mục tiêu
* xác định thiếu dữ liệu

Memory:

* brief gốc
* yêu cầu ẩn
* constraints
* audience
* success criteria

Knowledge:

* brief decomposition
* audience mapping
* content intent taxonomy

Tools:

* brief parser
* missing-info detector
* audience profiler
* output classifier

Second brain:

* mẫu brief tốt
* lỗi brief mơ hồ
* câu hỏi làm rõ hiệu quả

---

## 5.3. Ban Research

Nhiệm vụ:

* research đầu tiên cho mọi task
* xác định nguồn đáng tin
* phân loại fact vs opinion
* tìm mâu thuẫn nguồn
* chuẩn bị nền dữ kiện cho các ban khác

Memory:

* research questions
* source map
* confidence levels
* unresolved claims

Knowledge:

* source credibility framework
* fact classification
* citation rules
* contradiction handling

Tools:

* source discovery
* source evaluator
* contradiction checker
* evidence organizer

Second brain:

* whitelist nguồn mạnh theo lĩnh vực
* blacklist pattern nguồn yếu
* case xử lý khi nguồn mâu thuẫn
* mẫu note research tốt

---

## 5.4. Ban Chiến Lược & Outline

Nhiệm vụ:

* chuyển research thành góc tiếp cận
* tạo big idea
* lên outline
* thiết kế flow logic

Memory:

* thesis
* angle
* narrative frame
* outline draft

Knowledge:

* outline frameworks
* persuasive structures
* educational structures
* content architecture

Tools:

* outline builder
* angle generator
* section planner
* message hierarchy mapper

Second brain:

* thư viện outline mạnh
* pattern chuyển research → outline
* lỗi cấu trúc thường gặp

---

## 5.5. Ban Long-form / Tài liệu / Ebook

Nhiệm vụ:

* viết ebook
* viết tài liệu
* viết handbook
* viết sách chuyên môn
* diễn giải dễ hiểu

Memory:

* chapter map
* terminology
* tone setting
* examples used
* unresolved gaps

Knowledge:

* ebook structure
* document structure
* explainer writing
* chapter logic
* educational clarity

Tools:

* chapter planner
* paragraph balancer
* explainer rewriter
* tone controller

Second brain:

* template ebook
* template handbook
* mẫu section mạnh
* before/after long-form

---

## 5.6. Ban Social Content

Nhiệm vụ:

* viết content mạng xã hội
* tối ưu theo nền tảng
* repurpose từ long-form
* tạo chuỗi bài

Memory:

* target platform
* hook style
* CTA style
* depth level
* repurpose source

Knowledge:

* Facebook patterns
* Threads patterns
* LinkedIn patterns
* short-form post mechanics

Tools:

* platform formatter
* hook generator
* CTA generator
* repurpose engine

Second brain:

* hook library
* CTA library
* viral patterns
* authority patterns
* soft-sell patterns

---

## 5.7. Ban Video Script

Nhiệm vụ:

* viết script video ngắn
* thiết kế hook
* tối ưu retention
* thiết kế CTA cuối

Memory:

* duration
* beat map
* scene shifts
* hook type
* payoff line

Knowledge:

* short video structure
* spoken style writing
* retention principles
* CTA patterns

Tools:

* script timer
* spoken rewriter
* beat mapper
* retention optimizer

Second brain:

* 15s / 30s / 60s script patterns
* opening loops
* punchline types
* series episode formulas

---

## 5.8. Ban Critique & Grading

Nhiệm vụ:

* chấm bài thang 100
* phản biện nội dung
* phát hiện lỗ hổng logic
* đề xuất hướng sửa

Memory:

* scoring sheet
* weaknesses list
* revision priorities
* severity map

Knowledge:

* rubric 100
* critique framework
* editorial review method
* argument analysis

Tools:

* rubric scorer
* clarity critic
* logic critic
* revision suggester

Second brain:

* thư viện lỗi phổ biến
* mẫu feedback tốt
* examples theo band điểm 40 / 60 / 80 / 95

---

## 5.9. Ban Quality, Compliance & Anti-AI

Nhiệm vụ:

* kiểm cuối
* làm tự nhiên
* phát hiện văn sáo
* kiểm nhất quán
* cảnh báo claim rủi ro

Memory:

* repeated phrases
* risky claims
* style drift
* unresolved inconsistencies

Knowledge:

* anti-ai patterns
* natural Vietnamese writing rules
* consistency checks
* risk wording for finance/bđs/giáo dục

Tools:

* anti-ai auditor
* repetition detector
* consistency checker
* risk-claim checker
* proofreader

Second brain:

* danh sách cụm từ “mùi AI”
* checklist xuất bản
* lỗi cuối thường gặp
* patterns sửa tự nhiên

---

# 6. Kiến trúc thư mục hoàn chỉnh theo ảnh 2

Dưới đây là cấu trúc nên dùng cho skill.

```text
viet-pro/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── Orchestrator/
│   ├── editor-in-chief.md
│   ├── delegation-protocol.md
│   ├── liability-return.md
│   ├── routing-matrix.md
│   └── escalation-rules.md
├── Workers/
│   ├── intake-worker.md
│   ├── research-worker.md
│   ├── strategy-worker.md
│   ├── longform-worker.md
│   ├── social-worker.md
│   ├── video-worker.md
│   ├── critique-worker.md
│   └── quality-worker.md
├── SubAgents/
│   ├── intake/
│   │   ├── brief-parser.md
│   │   ├── audience-profiler.md
│   │   └── requirement-extractor.md
│   ├── research/
│   │   ├── source-finder.md
│   │   ├── credibility-checker.md
│   │   ├── contradiction-checker.md
│   │   └── citation-organizer.md
│   ├── strategy/
│   │   ├── angle-generator.md
│   │   ├── thesis-builder.md
│   │   ├── outline-builder.md
│   │   └── structure-recommender.md
│   ├── longform/
│   │   ├── ebook-architect.md
│   │   ├── document-structurer.md
│   │   ├── explainer-writer.md
│   │   └── tone-refiner.md
│   ├── social/
│   │   ├── facebook-writer.md
│   │   ├── threads-writer.md
│   │   ├── linkedin-writer.md
│   │   ├── short-caption-writer.md
│   │   └── repurpose-agent.md
│   ├── video/
│   │   ├── hook-builder.md
│   │   ├── short-script-writer.md
│   │   ├── retention-designer.md
│   │   └── cta-finisher.md
│   ├── critique/
│   │   ├── rubric-scorer.md
│   │   ├── logic-critic.md
│   │   ├── clarity-critic.md
│   │   └── revision-advisor.md
│   └── quality/
│       ├── anti-ai-auditor.md
│       ├── consistency-checker.md
│       ├── claim-risk-checker.md
│       └── final-proofreader.md
├── Autonomous-Core/
│   ├── task-classifier.md
│   ├── mode-selector.md
│   ├── workflow-engine.md
│   ├── output-engine.md
│   ├── scoring-engine.md
│   ├── critique-engine.md
│   ├── research-engine.md
│   ├── memory-engine.md
│   ├── knowledge-loader.md
│   ├── second-brain-loader.md
│   ├── tool-router.md
│   └── state-manager.md
├── Team-Orchestration/
│   ├── write-new.md
│   ├── edit-draft.md
│   ├── deep-research.md
│   ├── critique-content.md
│   ├── grade-content.md
│   ├── publish-ready.md
│   ├── longform-pipeline.md
│   ├── social-pipeline.md
│   ├── video-pipeline.md
│   └── recovery-protocol.md
├── _design-specs/
│   ├── architecture-overview.md
│   ├── department-contracts.md
│   ├── memory-spec.md
│   ├── knowledge-spec.md
│   ├── tool-spec.md
│   ├── second-brain-spec.md
│   ├── output-spec.md
│   ├── quality-gate-spec.md
│   └── evaluation-spec.md
├── Context-Layer/
│   ├── CoreModules/
│   │   ├── global-rules.md
│   │   ├── language-vietnamese.md
│   │   ├── rubric-100.md
│   │   ├── anti-ai-global.md
│   │   ├── source-trust-framework.md
│   │   └── risk-domain-rules.md
│   ├── Knowledge-Base/
│   │   ├── global/
│   │   │   ├── writing-principles.md
│   │   │   ├── nonfiction-frameworks.md
│   │   │   ├── platform-behaviors.md
│   │   │   ├── video-structures.md
│   │   │   └── editorial-review.md
│   │   └── departments/
│   │       ├── intake/
│   │       ├── research/
│   │       ├── strategy/
│   │       ├── longform/
│   │       ├── social/
│   │       ├── video/
│   │       ├── critique/
│   │       └── quality/
│   └── Second-Brain/
│       ├── global/
│       │   ├── heuristics.md
│       │   ├── checklists.md
│       │   ├── mistake-patterns.md
│       │   └── best-practices.md
│       └── departments/
│           ├── intake/
│           ├── research/
│           ├── strategy/
│           ├── longform/
│           ├── social/
│           ├── video/
│           ├── critique/
│           └── quality/
├── Memory/
│   ├── global-memory.md
│   ├── project-memory.md
│   ├── session-state.md
│   └── departments/
│       ├── editor-in-chief-memory.md
│       ├── intake-memory.md
│       ├── research-memory.md
│       ├── strategy-memory.md
│       ├── longform-memory.md
│       ├── social-memory.md
│       ├── video-memory.md
│       ├── critique-memory.md
│       └── quality-memory.md
├── Tools/
│   ├── global-tools.md
│   └── departments/
│       ├── intake-tools.md
│       ├── research-tools.md
│       ├── strategy-tools.md
│       ├── longform-tools.md
│       ├── social-tools.md
│       ├── video-tools.md
│       ├── critique-tools.md
│       └── quality-tools.md
├── assets/
│   ├── templates/
│   │   ├── ebook-outline.md
│   │   ├── document-outline.md
│   │   ├── facebook-post.md
│   │   ├── threads-post.md
│   │   ├── short-video-script.md
│   │   ├── critique-report.md
│   │   └── grading-report.md
│   ├── rubrics/
│   │   └── rubric-100.md
│   ├── checklists/
│   │   ├── research-checklist.md
│   │   ├── longform-checklist.md
│   │   ├── social-checklist.md
│   │   ├── video-checklist.md
│   │   ├── critique-checklist.md
│   │   └── publish-checklist.md
│   └── examples/
│       ├── ebook-examples.md
│       ├── social-examples.md
│       ├── video-examples.md
│       └── critique-examples.md
├── Outputs/
│   └── README.md
├── workforce-config.json
├── README.md
├── HUONG-DAN-SU-DUNG.md
└── verify.sh
```

---

# 7. Ý nghĩa từng khối thư mục

## `Orchestrator/`

Chứa luật điều phối cấp tổng.

## `Workers/`

Chứa vai trò và contract của từng phòng ban.

## `SubAgents/`

Chứa chuyên môn hóa sâu cho từng worker.

## `Autonomous-Core/`

Đây là “động cơ vận hành” của toàn skill:

* phân loại task
* chọn mode
* chọn workflow
* quản lý state
* nạp knowledge / memory / second brain

## `Team-Orchestration/`

Các pipeline phối hợp liên phòng ban.

## `_design-specs/`

Tài liệu thiết kế nội bộ, để skill dễ mở rộng và audit.

## `Context-Layer/`

Kho tri thức và kinh nghiệm được nạp có chọn lọc.

## `Memory/`

Bộ nhớ tác nghiệp theo tầng.

## `Tools/`

Quy định bộ công cụ nào được dùng ở đâu.

## `Outputs/`

Thư mục output runtime.

## `workforce-config.json`

File cấu hình lực lượng lao động của skill.

---

# 8. workforce-config.json nên chứa gì

File này là trung tâm cấu hình lực lượng vận hành.

Ví dụ cấu trúc logic:

```json
{
  "language": "vi",
  "default_research_mode": "deep-first",
  "default_scoring_scale": 100,
  "orchestrator": "editor-in-chief",
  "workers": [
    "intake-worker",
    "research-worker",
    "strategy-worker",
    "longform-worker",
    "social-worker",
    "video-worker",
    "critique-worker",
    "quality-worker"
  ],
  "routing": {
    "ebook": ["intake-worker", "research-worker", "strategy-worker", "longform-worker", "quality-worker"],
    "document": ["intake-worker", "research-worker", "strategy-worker", "longform-worker", "quality-worker"],
    "social": ["intake-worker", "research-worker", "strategy-worker", "social-worker", "quality-worker"],
    "video": ["intake-worker", "research-worker", "strategy-worker", "video-worker", "quality-worker"],
    "critique": ["intake-worker", "research-worker", "critique-worker", "quality-worker"],
    "grading": ["intake-worker", "research-worker", "critique-worker", "quality-worker"]
  },
  "liability_return": true,
  "quality_gate_required": true
}
```

---

# 9. Cấu trúc memory theo nhiều tầng

## 9.1. Global memory

Áp dụng toàn skill:

* tiếng Việt
* luôn research trước
* chấm theo 100
* ưu tiên văn tự nhiên
* tránh claim chắc chắn ở tài chính / bđs

## 9.2. Project memory

Theo từng dự án:

* tone thương hiệu
* audience
* mục tiêu
* preferred format
* domain

## 9.3. Department memory

Theo từng phòng ban:

* research team nhớ nguồn
* social team nhớ hook style
* video team nhớ duration
* longform team nhớ thuật ngữ

## 9.4. Task/session memory

Theo tác vụ đang chạy:

* outline hiện tại
* section hiện tại
* unresolved issues
* revision notes

---

# 10. Knowledge base theo nhiều lớp

## Lớp toàn cục

* nguyên tắc viết tiếng Việt
* framework research
* rubric 100
* anti-ai
* output rules

## Lớp phòng ban

* research methods
* ebook structure
* social platform behavior
* video script structure
* critique standards
* quality audit rules

---

# 11. Second brain theo đúng tinh thần ảnh 2

Phần `Second-Brain/` là nơi làm skill “có kinh nghiệm”.

Nó không phải lý thuyết. Nó là:

* mẫu tốt
* mẫu dở
* heuristic
* checklist
* bài học rút ra
* lỗi lặp
* before/after

Ví dụ:

### `Second-Brain/departments/social/`

* hook-library.md
* cta-library.md
* viral-patterns.md
* authority-post-patterns.md

### `Second-Brain/departments/quality/`

* ai-smell-phrases.md
* repetition-patterns.md
* last-mile-checklist.md

### `Second-Brain/departments/research/`

* trusted-sources-by-domain.md
* weak-source-signals.md
* contradiction-cases.md

---

# 12. Bộ tools trong skill

Vì đây là skill viết, “tools” nên được định nghĩa như **năng lực thao tác**, không nhất thiết là code script.

## Global tools

* task classifier
* research router
* outline builder
* scoring engine
* critique engine
* publish checker

## Department tools

Mỗi phòng có tool spec riêng trong `Tools/departments/`.

Ví dụ:

* `research-tools.md`
* `longform-tools.md`
* `social-tools.md`

Mỗi file nên mô tả:

* tool name
* input
* output
* khi nào dùng
* khi nào không dùng
* dependency với memory / knowledge nào

---

# 13. Workflow chính của hệ thống

## 13.1. Viết mới

Intake
→ Research
→ Strategy
→ Writer phù hợp
→ Quality
→ Orchestrator final

## 13.2. Sửa bản nháp

Intake
→ Critique diagnosis
→ Research check
→ Writer rewrite
→ Quality
→ Final

## 13.3. Chấm bài

Intake
→ Research if needed
→ Rubric scoring
→ Critique commentary
→ Quality fairness check
→ Final report

## 13.4. Phản biện nội dung

Intake
→ Research
→ Logic critique
→ Revision advice
→ Quality
→ Final

---

# 14. Design contract giữa các tầng

Đây là phần rất quan trọng từ ảnh 1.

Mỗi tầng phải có “contract” rõ ràng.

## Hợp đồng Điều phối → Ban

* giao nhiệm vụ rõ loại đầu ra
* ghi rõ success criteria
* ghi rõ quality threshold
* ghi rõ dependency

## Hợp đồng Ban → Trợ lý

* tác vụ con cụ thể
* không được lệch scope
* phải trả kết quả theo format

## Return contract

Kết quả trả về phải ghi rõ:

* output
* confidence
* unresolved risks
* dependency assumptions

Như vậy mới đúng tinh thần:
**delegation có hợp đồng, liability có đường quay về**.

---

# 15. Draft mô tả trigger cho `SKILL.md`

```yaml
---
name: viet-pro
description: comprehensive vietnamese writing orchestration system for planning, researching, drafting, editing, grading, critiquing, and polishing ebooks, professional documents, social media content, and social video scripts. use when chatgpt needs to perform deep research first, then coordinate specialized writing departments, workers, and subagents to produce high-quality vietnamese outputs with clear structure, natural language, quality control, and scoring on a 100-point scale.
---
```

---

# 16. Draft logic trong SKILL.md

Phần body nên ngắn, chỉ đóng vai trò tổng điều phối.

Nó nên yêu cầu ChatGPT làm theo thứ tự:

1. xác định loại nhiệm vụ
2. kích hoạt deep research trước
3. chọn worker pipeline
4. nạp đúng memory / knowledge / second brain
5. ủy quyền xuống subagent phù hợp
6. hợp nhất đầu ra
7. chạy quality gate
8. trả kết quả cuối

Không nên nhồi toàn bộ rule chi tiết vào `SKILL.md`.
Các chi tiết để ở các file riêng.

---

# 17. Quy tắc vàng của skill

1. **Luôn research trước**
2. **Không viết ngay khi brief còn mơ hồ**
3. **Mỗi worker chỉ làm đúng scope**
4. **Mọi đầu ra đều qua quality gate**
5. **Kết quả cuối luôn do Orchestrator chịu trách nhiệm**
6. **Chấm bài luôn theo rubric 100**
7. **Tiếng Việt là ngôn ngữ mặc định**
8. **Ưu tiên tự nhiên hơn sáo rỗng**
9. **Phân biệt fact, assumption, opinion**
10. **Với domain nhạy cảm, dùng ngôn ngữ thận trọng**

---

# 18. Ưu điểm của bản thiết kế này

So với skill thường, thiết kế này mạnh hơn ở 5 điểm:

* **Có điều phối phân cấp**, không bị prompt monolith
* **Có liability chain**, nên dễ kiểm soát lỗi
* **Có context layer rõ ràng**, dễ mở rộng
* **Có second brain riêng theo phòng ban**, nên càng dùng càng “khôn”
* **Có workforce config**, nên dễ nâng cấp thành hệ nhiều skill con sau này

---

# 19. Roadmap build thực tế

## Phase 1

Dựng bộ khung:

* `SKILL.md`
* `agents/openai.yaml`
* `Orchestrator/`
* `Workers/`
* `Team-Orchestration/`
* `workforce-config.json`

## Phase 2

Dựng context:

* `Context-Layer/CoreModules/`
* `Knowledge-Base/global/`
* `Second-Brain/global/`
* `Memory/`

## Phase 3

Dựng chuyên môn:

* `SubAgents/`
* knowledge theo phòng
* second brain theo phòng
* template / rubric / checklist

## Phase 4

Dựng kiểm định:

* `verify.sh`
* quality gates
* sample cases
* output examples

---

# 20. Kết luận chốt

Từ 2 ảnh input, mô hình đúng nhất cho `viet-pro` là:

* **ảnh 1** cho bạn **kiến trúc điều phối phân cấp**
* **ảnh 2** cho bạn **kiến trúc thư mục nhiều lớp**
* kết hợp lại thành **một skill newsroom orchestration system**

Nói ngắn gọn, `viet-pro` nên là:

> **Một tổng biên tập AI điều phối đội ngũ phòng ban, worker và sub-agent**
> dùng **memory + knowledge + tools + second brain** riêng theo từng tầng
> để **research, viết, sửa, chấm, phản biện, và kiểm duyệt** nội dung tiếng Việt ở mức chuyên nghiệp.


