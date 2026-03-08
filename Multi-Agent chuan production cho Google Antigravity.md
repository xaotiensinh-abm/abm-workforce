Dưới đây là bản **blueprint triển khai Multi-Agent chuẩn production cho Google Antigravity** mà bạn có thể đưa cho đội triển khai như một **design spec + operating model**.

Tôi nói rõ một điểm trước: theo tài liệu công khai, Antigravity hiện là một **agent-first development platform** có **Editor View**, **Agent Manager/Manager Surface**, quản lý nhiều agent trên nhiều workspace, có **browser subagent**, **Artifacts** (implementation plan, walkthrough, screenshots/recordings), **Skills**, **MCP**, **Review Changes**, **Knowledge Items**, cùng các cơ chế **Strict Mode / sandboxing**. Vì vậy, cách hợp lý nhất là **xây lớp Multi-Agent “trên” các primitive này**, thay vì giả định có thể sửa trực tiếp runtime lõi của Google. ([Google Developers Blog][1])

## 1) Kết luận thiết kế

Từ tài liệu bạn đưa và bức ảnh “Delegation Chain Management”, mô hình đúng nhất cho Antigravity không phải là “mọi agent đều tự do ngang hàng”, mà là:

**Một Lead Orchestrator chịu trách nhiệm cuối cùng**, phân rã tác vụ thành **Task Groups**, ủy quyền cho các worker chuyên biệt bằng **contract rõ ràng**, yêu cầu **attestation/evidence** khi worker trả kết quả, rồi mới tổng hợp, xác minh và trình cho người dùng qua **Artifacts + Review Changes + Walkthrough**. Trách nhiệm luôn “flow up” từ sub-agent lên worker, rồi lên orchestrator. Điều này khớp với triết lý trong syllabus: bắt đầu từ kiến trúc **simple & composable**, kết hợp dần **routing + orchestrator-workers + parallelization + evaluator-optimizer + context engineering + human oversight** thay vì nhảy ngay vào một framework quá tự do. 

## 2) Những gì nên tận dụng sẵn từ Antigravity

Antigravity đã có sẵn gần như đủ “khối nền” cho một hệ thống multi-agent nghiêm túc:

* **Agent Manager** làm “mission control”, giám sát nhiều agent trên nhiều workspace. ([Google Developers Blog][1])
* **Task Groups** để chia task lớn thành các đơn vị nhỏ hơn, có thể làm đồng thời. ([Google Antigravity][2])
* **Implementation Plan artifact** để trình bản kế hoạch kỹ thuật trước khi code. ([Google Antigravity][3])
* **Walkthrough, screenshots, browser recordings** để giao tiếp bất đồng bộ giữa agent và người dùng, đặc biệt hữu ích cho UI/browser tasks. ([Google Antigravity][4])
* **Browser subagent** chạy model chuyên biệt cho thao tác web và được tách profile Chrome riêng. ([Google Antigravity][5])
* **Skills** dưới dạng thư mục có `SKILL.md` để đóng gói quy trình nghiệp vụ và chuyên môn. ([Google Codelabs][6])
* **MCP** để agent kéo context và công cụ từ database, services, GitHub/Notion/Linear-like sources theo chuẩn hóa. ([Google Cloud][7])
* **Review Changes** để kiểm tra diff, comment trực tiếp trên thay đổi. ([Google Antigravity][8])
* **Knowledge Items** để lưu “trí nhớ vận hành” và tái dùng ở các task sau. ([Google Antigravity][9])
* **Strict Mode + sandboxing** để giới hạn truy cập và chặn network khi cần an toàn cao. ([Google Antigravity][10])

Nói ngắn gọn: **Antigravity đã có control surface, artifact channel, browser lane, skills lane, data/tool lane và security lane**. Phần còn thiếu là **operating contract**, **role taxonomy**, **verification discipline** và **governance chuẩn production**.

## 3) Kiến trúc chuẩn nên triển khai

### 3.1. Ba lớp kiến trúc

**Lớp 1: Control Plane**
Đây là nơi quyết định “ai làm gì, được làm tới đâu, khi nào dừng”.

Gồm:

* **Lead Orchestrator**
* **Task Router**
* **Policy / Risk Engine**
* **Budget & Retry Controller**
* **Context Manager**
* **Memory Curator**

**Lớp 2: Execution Plane**
Đây là nơi worker thực thi.

Gồm:

* **Code Worker**
* **Test / QA Worker**
* **Browser QA Subagent**
* **Infra / DevOps Worker**
* **Data / MCP Worker**
* **Security / Compliance Evaluator**
* **Docs / Walkthrough Worker**

**Lớp 3: Human Assurance Plane**
Đây là nơi người dùng kiểm soát chất lượng.

Gồm:

* **Implementation Plan review**
* **Review Changes**
* **Walkthrough / screenshots / browser recordings**
* **Approval gates**
* **Rollback / retry / escalate**

### 3.2. Nguyên tắc cứng

1. **Chỉ 1 agent giao tiếp ở cấp “chịu trách nhiệm” với người dùng**
   Lead Orchestrator là đầu mối duy nhất đại diện cho hệ thống.

2. **Worker không merge/deploy trực tiếp nếu chưa qua verifier hoặc human gate**
   Điều này biến “liability flows up” từ ảnh thành policy vận hành.

3. **Mọi delegation phải có contract + attestation**
   Không giao việc kiểu mơ hồ.

4. **Context không đi thẳng toàn bộ xuống mọi worker**
   Chỉ đưa phần cần thiết. Các phần còn lại được truy xuất động qua Skills, MCP, files, artifacts, Knowledge Items. Đây là áp dụng đúng context engineering. 

## 4) Cấu trúc agent chuẩn cho Antigravity

Tôi đề xuất **7 vai trò chuẩn** sau.

### A. Lead Orchestrator

Vai trò:

* nhận intent của người dùng
* tạo implementation plan
* chia Task Groups
* chọn worker
* tổng hợp kết quả
* quyết định retry / escalate / finish

Được phép:

* đọc repo mức rộng
* đọc artifacts
* gọi worker
* trình kế hoạch cho người dùng

Không nên:

* trực tiếp sửa quá nhiều code khi task lớn

### B. Router / Triage Agent

Vai trò:

* phân loại task: bug, feature, refactor, UI, infra, data, docs
* xác định độ rủi ro
* chọn pattern thực thi

Quy tắc:

* task nhỏ: single agent
* task trung bình: orchestrator + code + test
* task UI: thêm browser subagent
* task data: thêm MCP/data worker
* task rủi ro cao: thêm evaluator + human approval

### C. Code Worker

Vai trò:

* sửa code, tạo module, refactor, viết tests cơ bản
* chỉ làm trong phạm vi task contract

Output:

* changed files
* summary
* self-check
* open questions

### D. Test / Verifier Worker

Vai trò:

* chạy test, lint, typecheck, static scan
* kiểm tra acceptance criteria
* xác nhận patch có thật sự pass hay chưa

Đây là worker bắt buộc cho task thay đổi code.

### E. Browser QA Subagent

Vai trò:

* verify UI flow, visual regressions, interaction bugs
* tạo screenshots/recordings
* trả bằng chứng cho orchestrator

Antigravity đã có browser subagent và artifact lane rất hợp với vai trò này. ([Google Antigravity][5])

### F. Data / MCP Worker

Vai trò:

* truy vấn schema, logs, analytics, docs, tickets, DB
* lấy context động qua MCP thay vì nhồi mọi thứ vào prompt

Đây là chìa khóa để tránh context phình to và giúp task “có dữ liệu thật”. ([Google Cloud][7])

### G. Documentation / Walkthrough Worker

Vai trò:

* tạo walkthrough
* tạo change summary
* cập nhật docs nội bộ
* lưu lesson learned vào Knowledge Items

## 5) Chuẩn Contract – Attestation – Liability

Đây là phần quan trọng nhất nếu bạn muốn đội Antigravity triển khai “đúng chuẩn”, thay vì chỉ “multi-agent cho có”.

### 5.1. Task Contract chuẩn

Mỗi lần giao việc từ Orchestrator xuống Worker phải có cấu trúc gần như sau:

```json
{
  "task_id": "TG-03-W2",
  "parent_task_id": "TG-03",
  "owner_agent": "lead_orchestrator",
  "executor_agent": "code_worker",
  "objective": "Fix login redirect loop on OAuth callback",
  "scope_in": [
    "auth/callback handler",
    "session validation",
    "frontend redirect guard"
  ],
  "scope_out": [
    "database schema changes",
    "deployment"
  ],
  "workspace": "feature/oauth-fix",
  "allowed_tools": [
    "editor",
    "terminal:test",
    "read_files"
  ],
  "allowed_mcp_resources": [],
  "required_artifacts": [
    "diff_summary",
    "test_result",
    "risk_note"
  ],
  "acceptance_criteria": [
    "existing auth tests pass",
    "manual login flow succeeds",
    "no infinite redirect"
  ],
  "budget": {
    "max_tool_calls": 20,
    "max_runtime_minutes": 15,
    "max_retries": 2
  },
  "risk_level": "medium",
  "handoff_format": "structured_markdown"
}
```

### 5.2. Attestation chuẩn

Worker trả kết quả không chỉ bằng “xong rồi”, mà phải kèm:

```json
{
  "task_id": "TG-03-W2",
  "status": "done_with_risks",
  "summary": "Patched redirect guard and session check",
  "files_changed": [
    "src/auth/callback.ts",
    "src/auth/session.ts"
  ],
  "tests_run": [
    "pnpm test auth",
    "pnpm typecheck"
  ],
  "evidence": [
    "test log artifact",
    "screenshot link",
    "browser recording"
  ],
  "known_risks": [
    "no production env validation"
  ],
  "confidence": 0.82,
  "needs_followup": true,
  "recommended_next_agent": "browser_qa_subagent"
}
```

### 5.3. Liability rules

Biến bức ảnh thành rule vận hành:

* **Worker chịu trách nhiệm với Orchestrator**
* **Subagent chịu trách nhiệm với Worker gọi nó**
* **Người dùng chỉ chấp nhận output của Lead Orchestrator**
* **Không có chuyện “browser subagent nói pass nên hệ thống pass”**
* **Lead Orchestrator luôn là bên ký duyệt logic cuối**

## 6) Luồng vận hành chuẩn end-to-end

### Bước 1. Intake & triage

Router phân loại task và risk.

* Feature nhỏ → single-agent
* Feature đa file → orchestrator-workers
* UI flow → thêm browser verification
* High-risk → strict mode + sandbox + human gate

### Bước 2. Planning

Lead Orchestrator tạo **Implementation Plan artifact**.
Plan phải có:

* problem statement
* impacted files / systems
* task groups
* risks
* verification plan
* rollback plan

Antigravity đã có artifact loại implementation plan đúng cho bước này. ([Google Antigravity][3])

### Bước 3. Delegation

Orchestrator chia task thành Task Groups và contract cho từng worker.
Quy tắc:

* subtask độc lập thì chạy song song
* subtask phụ thuộc thì chain
* rủi ro cao thì phải có evaluator độc lập

### Bước 4. Execution

Workers làm trong workspace/phạm vi được cấp.

* Code Worker sửa code
* Test Worker chạy kiểm tra
* Browser QA Subagent verify UI
* Data Worker gọi MCP để lấy schema/logs/tickets
* Docs Worker chuẩn bị walkthrough

### Bước 5. Verification

Có ít nhất 3 lớp verify:

* **syntactic**: lint/type/test
* **behavioral**: browser flow / integration
* **policy**: security / scope / risky operations

### Bước 6. Human review

Người dùng review qua:

* **Review Changes**
* **Walkthrough**
* **screenshots / recordings**
* comment trực tiếp trên diff/artifact

Antigravity đã hỗ trợ review diff và comment trực tiếp trong manager/editor. ([Google Antigravity][8])

### Bước 7. Final synthesis

Lead Orchestrator tạo:

* executive summary
* what changed
* what was verified
* remaining risks
* recommended next step

### Bước 8. Memory update

Lesson learned, reusable rules, known patterns được đẩy vào **Knowledge Items** hoặc thành **Skill** mới để tái dùng cho các task tương tự. ([Google Antigravity][9])

## 7) Pattern vận hành chuẩn theo loại task

### 7.1. Bug fix

Mẫu:
`Router -> Orchestrator -> Code Worker -> Test Worker -> Browser QA -> Orchestrator`

Dùng khi:

* lỗi rõ ràng
* acceptance criteria xác định được
* cần turnaround nhanh

### 7.2. Feature implementation

Mẫu:
`Router -> Orchestrator -> Spec/Plan -> Code Worker(s) song song -> Test Worker -> Browser QA -> Docs Worker -> Orchestrator`

Dùng khi:

* thay đổi đa file
* cần UI verification
* cần walkthrough

### 7.3. Refactor / migration

Mẫu:
`Router -> Orchestrator -> Impact Analysis Worker -> Code Worker(s) -> Static Analysis / Test -> Risk Evaluator -> Orchestrator`

Dùng khi:

* ảnh hưởng diện rộng
* cần tránh regression ẩn

### 7.4. Data-aware development

Mẫu:
`Router -> Orchestrator -> MCP/Data Worker -> Code Worker -> Integration Verifier -> Orchestrator`

Dùng khi:

* cần schema thật
* cần logs thật
* cần DB/service context thật

## 8) Security & governance chuẩn production

Đây là phần bắt buộc nếu muốn proposal đủ mạnh.

### 8.1. Chế độ mặc định

* **Strict Mode bật theo mặc định cho repo nhạy cảm**
* **Sandbox mặc định cho lệnh shell có network hoặc ghi hệ thống**
* browser dùng allowlist/denylist
* agent chỉ thấy workspace + vùng Antigravity cần thiết, không mở rộng bừa bãi

Các cơ chế này có trong docs của Antigravity và rất nên dùng làm lớp governance gốc. ([Google Antigravity][10])

### 8.2. Phân quyền theo vai trò

* Orchestrator: read rộng, write hạn chế
* Code Worker: write trong workspace được cấp
* Test Worker: execute tests, không deploy
* Browser QA: browser only
* Data Worker: MCP read-only mặc định
* Release Worker: chỉ tồn tại khi có approval riêng

### 8.3. Cổng phê duyệt

Bắt buộc human gate khi:

* thay đổi auth / payments / IAM
* chạy lệnh phá hủy
* chạm production configs
* mở network ngoài allowlist
* thay đổi schema DB
* tạo/xóa secrets

### 8.4. Rollback

Mỗi plan phải có rollback clause:

* files impacted
* revert strategy
* test to confirm revert
* fallback owner

## 9) Observability & KPI

Nếu không đo, multi-agent sẽ thành “nhiều agent hơn, lỗi khó hơn”.

### 9.1. Metrics bắt buộc

Ở mức task:

* task success rate
* first-pass accept rate
* median time to completion
* retry rate
* human intervention rate
* reopen rate sau merge

Ở mức quality:

* test pass rate
* regression escape rate
* diff churn
* % tasks có đủ evidence
* % task kết thúc bằng walkthrough usable

Ở mức orchestration:

* số worker / task
* parallelism efficiency
* dead delegation rate
* attestation completeness rate
* fallback trigger rate

Ở mức economics:

* token/cost per accepted task
* cost per merged LOC
* cost per successful UI verification
* time saved vs single-agent baseline

### 9.2. Trace bắt buộc cho mỗi task

Mỗi task cần có:

* plan artifact
* task group lineage
* contract chain
* tool call summary
* evidence list
* reviewer comments
* final decision

Antigravity có artifact system, panes, browser subagent view và knowledge primitives rất phù hợp để làm “trace surface”; việc cần thêm là chuẩn hóa schema và dashboard vận hành phía bạn. ([Google Antigravity][11])

## 10) Chiến lược tối ưu hóa

### 10.1. Tối ưu #1: Không multi-agent hóa mọi thứ

Sai lầm lớn nhất là task nào cũng spawn nhiều agent.

Rule:

* task nhỏ, rõ, 1-2 file → 1 agent
* task trung bình, đa file → 2-4 agent
* task lớn, nhiều domain → 5-8 agent
* chỉ dùng council/voting cho task khó đánh giá hoặc rủi ro cao

Điều này đúng với syllabus: bắt đầu đơn giản, chỉ tăng độ phức tạp khi có bằng chứng hiệu quả. 

### 10.2. Tối ưu #2: Context tối thiểu + tải động

* không nhồi full repo vào mọi worker
* worker chỉ nhận scope, acceptance criteria, file targets
* kiến thức dài hạn đẩy vào Skills / Knowledge Items
* dữ liệu động lấy qua MCP
* bằng chứng lớn đẩy thành artifact, không nhét hết vào context

### 10.3. Tối ưu #3: Verifier rẻ hơn creator

Dùng mô hình/worker “kiểm” rẻ hơn hoặc hẹp hơn thay vì để agent mạnh nhất làm tất cả.

* creator mạnh cho planning / code synthesis
* verifier rẻ hơn cho schema checks, lint, policy checks, diff checks

### 10.4. Tối ưu #4: Skill hóa workflow lặp lại

Bất kỳ chuỗi thao tác nào lặp từ 3 lần trở lên nên đóng gói thành **Skill**:

* create feature skeleton
* migrate API route
* add test harness
* generate rollout checklist
* create implementation plan template
* browser verification for login/cart/checkout

Antigravity public docs và codelab xác nhận Skills là primitive mở rộng agent rất phù hợp cho các workflow kiểu này. ([Google Codelabs][6])

## 11) Roadmap triển khai đề xuất

### Phase 0 — Baseline

Mục tiêu:

* đo single-agent baseline trước
* chuẩn hóa task taxonomy
* định nghĩa contract schema
* định nghĩa artifact schema

Deliverables:

* task classes
* risk matrix
* acceptance criteria checklist
* metrics dashboard v1

### Phase 1 — Multi-agent foundation

Mục tiêu:

* dựng Lead Orchestrator
* 4 worker cốt lõi: Code, Test, Browser QA, Docs
* implementation plan + walkthrough + review changes flow

Deliverables:

* orchestration prompt/spec
* contract/attestation schema
* task group policy
* retry/fallback policy

### Phase 2 — Enterprise context

Mục tiêu:

* MCP integration cho logs, DB, tickets, docs
* read-only by default
* context loading strategy

Deliverables:

* MCP allowlist
* data access policy
* retrieval ranking rules
* knowledge item lifecycle

### Phase 3 — Governance & production hardening

Mục tiêu:

* strict mode profiles
* sandbox defaults
* human approval gates
* rollback automation
* security evaluator

Deliverables:

* policy engine
* sensitive task templates
* audit trail
* compliance checklist

### Phase 4 — Continuous optimization

Mục tiêu:

* skill library
* self-improvement loop
* evaluator-optimizer on prompts/plans
* cost routing

Deliverables:

* skills catalog
* prompt tuning loop
* auto postmortem
* regression benchmark suite

## 12) Bản đặc tả ngắn để gửi cho team triển khai

Bạn có thể gửi nguyên văn yêu cầu triển khai theo dạng này:

**Mục tiêu**
Xây một hệ thống multi-agent trên Antigravity theo mô hình lead orchestrator + specialized workers, với contract-based delegation, artifact-based verification, MCP-based dynamic context, strict governance và measurable observability.

**Yêu cầu bắt buộc**

1. Một lead orchestrator chịu trách nhiệm cuối.
2. Mọi delegation phải có Task Contract chuẩn.
3. Worker bắt buộc trả Attestation có evidence.
4. Code changes phải qua Test Verifier.
5. UI changes phải có browser evidence.
6. Task lớn phải đi qua Implementation Plan artifact.
7. Output cuối phải có Walkthrough.
8. High-risk tasks phải chạy Strict Mode + sandbox + human gate.
9. Reusable workflows phải đóng gói thành Skills.
10. Mọi task phải có trace và KPI.

**Định nghĩa thành công**

* tăng first-pass accept rate
* giảm reviewer back-and-forth
* giảm regressions
* giảm cost/task so với multi-agent tự do
* tăng tốc độ hoàn thành task trung bình mà không giảm chất lượng

## Khuyến nghị cuối cùng

Nếu triển khai thật, tôi khuyên **không bắt đầu bằng “hệ thống hội đồng agent đầy đủ”**. Bắt đầu đúng nhất cho Antigravity là:

**Lead Orchestrator + Code Worker + Test Verifier + Browser QA + Docs/Walkthrough Worker**, rồi sau đó mới thêm **Data/MCP Worker** và **Security Evaluator**.

Đó là cấu hình vừa đủ mạnh, bám sát primitive hiện có của Antigravity, lại phù hợp với triết lý trong tài liệu bạn đưa: **simple, composable, observable, verifiable**. 
