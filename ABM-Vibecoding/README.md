<div align="center">

# 🧠 ABM-Vibecoding

### *AI-Powered Agentic Skills Framework for Vibecoding Workflow*

[![Skills](https://img.shields.io/badge/Skills-18-blueviolet?style=for-the-badge&logo=sparkles)](skills/)
[![ABM](https://img.shields.io/badge/ABM_Workforce-Integrated-ff6b6b?style=for-the-badge&logo=robot)](GETTING-STARTED.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Based On](https://img.shields.io/badge/Based_On-Superpowers_v5.0.0-orange?style=for-the-badge)](https://github.com/obra/superpowers)

**Hệ thống 18 skills agentic tích hợp ABM Workforce orchestration — tối ưu hóa cho Vibecoding workflow.**

[Quick Start](#-quick-start) · [Skills](#-18-skills) · [Architecture](#-architecture) · [ABM Integration](#-abm-workforce-integration) · [Usage Guide](USAGE-GUIDE.md) · [Contributing](#-contributing)

</div>

---

## ⚡ Điểm nổi bật

<table>
<tr>
<td width="50%">

### 🔮 Superpowers gốc
- 14 dev skills
- Manual orchestration
- Code review only
- English documentation
- Basic verification

</td>
<td width="50%">

### 🚀 ABM-Vibecoding
- **18 skills** (14 + 4 ABM custom)
- **6-bước Delegation Chain** tự động
- **8-persona multi-dimensional review**
- **100% Tiếng Việt** cho business output
- **Iron Law + Rationalization Table**

</td>
</tr>
</table>

---

## 🏗 Architecture

```mermaid
graph TB
    subgraph CEO["👤 CEO / User"]
        REQ[\"Yêu cầu mới"\]
    end

    subgraph GATE["🚦 ABM Gate System"]
        direction LR
        G0["Bước 0<br/>Pre-Flight<br/>Skill Check"]
        G1["Bước 1<br/>Phân tích<br/>Task Type"]
        G15["Bước 1.5<br/>Brainstorming<br/>GATE"]
    end

    subgraph ENGINE["⚙️ ABM Engine"]
        direction LR
        CONTRACT["📋 Bước 2-4<br/>Contract<br/>+ Worker"]
        EXECUTE["🔧 Bước 5<br/>Thực hiện"]
        VERIFY["✅ Bước 6-7<br/>Two-Stage<br/>Review"]
    end

    subgraph OUTPUT["📊 Output"]
        REPORT["📄 Báo cáo<br/>+ Evidence"]
    end

    REQ --> G0 --> G1 --> G15
    G15 -->|"Approved"| CONTRACT
    CONTRACT --> EXECUTE --> VERIFY
    VERIFY -->|"Pass"| REPORT
    VERIFY -->|"Fail"| EXECUTE
    REPORT --> CEO

    style CEO fill:#1a1a2e,stroke:#e94560,color:#fff
    style GATE fill:#16213e,stroke:#0f3460,color:#fff
    style ENGINE fill:#0f3460,stroke:#533483,color:#fff
    style OUTPUT fill:#533483,stroke:#e94560,color:#fff
```

---

## 📦 18 Skills

### Workflow Pipeline

```mermaid
graph LR
    subgraph PLAN["🧠 PLANNING"]
        B["brainstorming"]
        WP["writing-plans"]
    end

    subgraph BUILD["⚙️ BUILDING"]
        EP["executing-plans"]
        SDD["subagent-driven-dev"]
        TDD["test-driven-dev"]
        SD["systematic-debugging"]
    end

    subgraph REVIEW["🔍 REVIEW"]
        RCR["requesting-review"]
        RECV["receiving-review"]
        VBC["verification"]
    end

    subgraph SHIP["🚀 SHIP"]
        GW["git-worktrees"]
        FDB["finishing-branch"]
        GWO["git-workflow-opt"]
    end

    B --> WP --> EP & SDD
    EP & SDD --> RCR --> RECV
    RECV --> VBC --> FDB --> GWO

    style PLAN fill:#6c5ce7,color:#fff,stroke:#a29bfe
    style BUILD fill:#0984e3,color:#fff,stroke:#74b9ff
    style REVIEW fill:#00b894,color:#fff,stroke:#55efc4
    style SHIP fill:#e17055,color:#fff,stroke:#fab1a0
```

### Danh sách đầy đủ

<table>
<tr>
<th>🧠 Planning</th>
<th>⚙️ Building</th>
<th>🔍 Review</th>
<th>🚀 Ship</th>
</tr>
<tr>
<td>

`brainstorming`
`writing-plans`

</td>
<td>

`executing-plans`
`subagent-driven-dev`
`test-driven-dev`
`systematic-debugging`
`dispatching-parallel`

</td>
<td>

`requesting-code-review`
`receiving-code-review`
`verification-before-completion`

</td>
<td>

`using-git-worktrees`
`finishing-a-dev-branch`
`using-superpowers`
`writing-skills`

</td>
</tr>
</table>

### 🔷 4 Custom ABM Skills

<table>
<tr>
<td width="25%" align="center">

**📋 Contract-Driven Dev**

6-bước Delegation Chain
`Contract → Worker →`
`Attestation → Verify`

</td>
<td width="25%" align="center">

**🔍 Multi-Persona Review**

8 personas × weighted scoring
`Hacker · Auditor · CEO`
`Architect · Pragmatist`

</td>
<td width="25%" align="center">

**✅ Evidence Verification**

Iron Law + Rationalization
`"Chưa có evidence`
`= chưa kết luận"`

</td>
<td width="25%" align="center">

**🚀 Git Workflow Opt**

Pre-push checklist
`Convention · Branch`
`Strategy · CI/CD`

</td>
</tr>
</table>

---

## 🛡️ Iron Law — Kỷ Luật Sắt

> **KHÔNG KẾT LUẬN MÀ CHƯA CÓ BẰNG CHỨNG XÁC MINH MỚI (FRESH).**
>
> *Vi phạm chữ = vi phạm tinh thần. Không có ngoại lệ.*

```mermaid
graph LR
    A["🔍 XÁC ĐỊNH<br/>Lệnh nào<br/>chứng minh?"] --> B["⚡ CHẠY<br/>Fresh execution<br/>không dùng cache"]
    B --> C["📖 ĐỌC<br/>Full output<br/>+ exit code"]
    C --> D{"✅ XÁC NHẬN<br/>Output confirm?"}
    D -->|"Yes + Evidence"| E["📣 TUYÊN BỐ<br/>kèm bằng chứng"]
    D -->|"No"| F["🔴 DỪNG<br/>Báo thực trạng"]

    style A fill:#fd79a8,color:#fff
    style B fill:#fdcb6e,color:#2d3436
    style C fill:#74b9ff,color:#fff
    style D fill:#a29bfe,color:#fff
    style E fill:#00b894,color:#fff
    style F fill:#d63031,color:#fff
```

### Rationalization Table — Bảng Chống Biện Minh

| 🤔 Biện minh | ⚡ Thực tế |
|---|---|
| *"Chắc là ok rồi"* | → **CHẠY** lệnh xác minh |
| *"Tôi tự tin"* | → Confidence ≠ evidence |
| *"Agent nói success"* | → Verify **INDEPENDENTLY** |
| *"Quá đơn giản để sai"* | → Đơn giản ≈ **dễ sai nhất** |
| *"Mệt, cần nhanh"* | → Mệt ≠ excuse |
| *"Spirit vs letter"* | → Vi phạm letter = vi phạm spirit |

---

## 🔷 ABM Workforce Integration

### Two-Stage Review

```mermaid
graph TD
    subgraph S1["Stage 1: Spec Compliance"]
        C1["✅ Acceptance Criteria?"]
        C2["✅ Scope đúng?"]
        C3["✅ Over/Under-building?"]
    end

    subgraph S2["Stage 2: Quality Review"]
        C4["✅ Evidence fresh?"]
        C5["✅ Budget ok?"]
        C6["✅ Risk check?"]
        C7["✅ Best practices?"]
    end

    INPUT["📥 Worker Output"] --> S1
    S1 -->|"PASS"| S2
    S1 -->|"FAIL"| FIX1["🔧 Fix → Re-verify S1"]
    S2 -->|"PASS"| ACCEPT["✅ CHẤP NHẬN"]
    S2 -->|"FAIL"| FIX2["🔧 Fix → Re-verify S2"]

    style S1 fill:#0984e3,color:#fff,stroke:#74b9ff
    style S2 fill:#6c5ce7,color:#fff,stroke:#a29bfe
    style ACCEPT fill:#00b894,color:#fff
    style FIX1 fill:#fdcb6e,color:#2d3436
    style FIX2 fill:#fdcb6e,color:#2d3436
```

### 8-Persona Review System

```mermaid
pie title Trọng Số Review Personas
    "🔴 Hacker" : 15
    "📊 Auditor" : 15
    "💼 CEO" : 15
    "🏗️ Architect" : 15
    "🔧 Pragmatist" : 10
    "⚔️ Competitor" : 10
    "🔄 Operator" : 10
    "📚 New Hire" : 10
```

---

## 🚀 Quick Start

```powershell
# 1. Clone
git clone https://github.com/xaotiensinh-abm/ABM-Vibecoding.git

# 2. Verify
cd ABM-Vibecoding
Get-ChildItem -Recurse -Filter "SKILL.md" skills\ | Measure-Object
# → Count: 18

# 3. Explore
cat GETTING-STARTED.md
```

> 📖 Xem chi tiết tại **[GETTING-STARTED.md](GETTING-STARTED.md)**

---

## 📂 Cấu trúc dự án

```
ABM-Vibecoding/
├── 📄 GEMINI.md                     ← Entry point (auto-load)
├── 📄 GETTING-STARTED.md            ← Quick start guide
├── 📄 DEPENDENCY-GRAPH.md           ← Skill dependency map
├── 📄 gemini-extension.json         ← Gemini CLI config
│
├── 🧠 skills/
│   ├── brainstorming/               ← 💡 Ideation workflow
│   ├── writing-plans/               ← 📋 Implementation plans
│   ├── executing-plans/             ← ⚙️ Plan execution
│   ├── test-driven-development/     ← 🧪 TDD discipline
│   ├── systematic-debugging/        ← 🔧 4-phase debugging
│   ├── subagent-driven-development/ ← 🤖 Multi-agent execution
│   ├── dispatching-parallel-agents/ ← ⚡ Parallel dispatch
│   ├── requesting-code-review/      ← 🔍 Review workflow
│   ├── receiving-code-review/       ← 📝 Feedback handling
│   ├── verification-before-completion/ ← ✅ Verification gate
│   ├── using-git-worktrees/         ← 🌿 Branch isolation
│   ├── finishing-a-development-branch/ ← 🏁 Branch completion
│   ├── using-superpowers/           ← 📖 Meta + tool mapping
│   ├── writing-skills/              ← ✍️ Skill creation (TDD)
│   │
│   ├── abm-contract-driven-development/ ← 📋 [ABM] Delegation Chain
│   ├── abm-multi-persona-review/    ← 🔍 [ABM] 8-persona review
│   ├── evidence-driven-verification/← ✅ [ABM] Iron Law
│   └── git-workflow-optimization/   ← 🚀 [ABM] Push optimization
│
├── 🪝 hooks/                        ← Git hooks (Windows)
└── 🧪 tests/                        ← Test suite
```

---

## 🔧 Git Workflow

```powershell
# Commit Convention
git commit -m "feat(skill-name): mô tả thay đổi"
git commit -m "skill(new-skill): initial implementation"
git commit -m "fix(debugging): sửa lỗi regex pattern"
git commit -m "docs: cập nhật Getting Started"

# Branch Strategy
#   main     → Production-ready (PR only)
#   develop  → Integration
#   skill/*  → New skill development
#   fix/*    → Bug fixes
```

---

## 🙏 Credits

<table>
<tr>
<td align="center">

**obra/superpowers**
Framework gốc v5.0.0
[GitHub](https://github.com/obra/superpowers)

</td>
<td align="center">

**ABM Workforce**
AI Business Master
Orchestration System

</td>
<td align="center">

**Antigravity**
Google Deepmind
Advanced Agentic Coding

</td>
</tr>
</table>

---

<div align="center">

*📦 Customized by ABM Skill Generator v1.0 | ABM Workforce | Antigravity*

**[⬆ Back to Top](#-abm-vibecoding)**

</div>
