# 🚀 Getting Started — ABM-Vibecoding

## Tóm tắt

**ABM-Vibecoding** = Superpowers framework + ABM Workforce orchestration.
18 skills cá nhân hóa cho Vibecoding workflow, 100% tiếng Việt cho business output.

## Quick Start (3 phút)

### 1. Kiểm tra setup
```powershell
Get-ChildItem -Recurse -Filter "SKILL.md" skills\ | Measure-Object  # Expected: 18
```

### 2. Skill nào dùng khi nào?

| Tôi muốn... | Skill |
|---|---|
| 🧠 Brainstorm ý tưởng | `brainstorming` |
| 📋 Lập kế hoạch | `writing-plans` |
| 🔧 Fix bug có hệ thống | `systematic-debugging` |
| ✅ Viết test trước code | `test-driven-development` |
| 🔍 Review code | `requesting-code-review` + `receiving-code-review` |
| 📝 Thực thi kế hoạch | `executing-plans` |
| 🌿 Branch riêng | `using-git-worktrees` |
| 🏁 Hoàn tất branch | `finishing-a-development-branch` |
| 🤖 Parallel tasks | `dispatching-parallel-agents` |
| 📋 Giao việc ABM | `abm-contract-driven-development` |
| 🔍 Đánh giá đa chiều | `abm-multi-persona-review` |
| ✅ Xác minh kết quả | `evidence-driven-verification` |
| 🚀 Push GitHub tối ưu | `git-workflow-optimization` |

### 3. Workflow cơ bản

```
CEO yêu cầu → Brainstorming → Writing Plans → Executing Plans → Review → Push
                    ↓                ↓              ↓           ↓         ↓
              abm-contract    bite-sized tasks  evidence    2-stage    git-workflow
```

### 4. ABM Rules chính

1. **Iron Law:** Không kết luận mà chưa có bằng chứng MỚI
2. **Contract:** Không giao việc mà không có hợp đồng
3. **Two-Stage Review:** Spec compliance TRƯỚC, quality SAU
4. **Brainstorming Gate:** Không code trước khi design approved
5. **Tiếng Việt 100%:** Mọi output bằng tiếng Việt

## Cấu trúc

```
ABM-Vibecoding/
├── GEMINI.md                      ← Entry point
├── GETTING-STARTED.md             ← Bạn đang đọc file này
├── DEPENDENCY-GRAPH.md            ← Skill dependencies (Mermaid)
├── skills/
│   ├── using-superpowers/         ← Meta + tool mapping
│   ├── brainstorming/             ← Phase 1: Ý tưởng
│   ├── writing-plans/             ← Phase 2: Kế hoạch
│   ├── executing-plans/           ← Phase 3: Thực thi
│   ├── test-driven-development/   ← Testing discipline
│   ├── systematic-debugging/      ← 4-phase debugging
│   ├── [+ 8 more core skills]
│   ├── abm-contract-driven-development/ ← [ABM] Delegation Chain
│   ├── abm-multi-persona-review/  ← [ABM] 8-persona review
│   ├── evidence-driven-verification/ ← [ABM] Iron Law
│   └── git-workflow-optimization/ ← [ABM] Push optimization
├── hooks/                         ← Git hooks (Windows)
└── tests/                         ← Test suite
```

## Git Workflow

Push theo quy trình tối ưu — xem `skills/git-workflow-optimization/SKILL.md`:
```powershell
# Commit convention
git commit -m "feat(skill-name): description"
git commit -m "skill(new-skill): initial implementation"
git commit -m "docs: update Getting Started"

# Push
git push origin develop
```

## Tham khảo

- [ABM Global Rules](file:///C:/Users/ADMIN/.gemini/RULES.md)
- [Dependency Graph](DEPENDENCY-GRAPH.md)
- [Antigravity Tools Mapping](skills/using-superpowers/references/antigravity-tools.md)
