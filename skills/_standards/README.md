# 📐 ABM-Workforce Skill Standards

> **9-Layer Skill Engineering Compliance Framework**
> Chuẩn hoá chất lượng cho 143 skills của ABM-Workforce v3.0

---

## Cấu trúc thư mục

```
_standards/
├── SKILL-TEMPLATE-V2.md          # Template chuẩn cho skill mới (9-Layer compliant)
├── README.md                      # File này
├── output-contracts/              # Layer 7: Output Contract theo domain
│   ├── code.md                    # Development (W1:CodeAgent)
│   ├── content.md                 # Content (W2:ContentAgent)
│   ├── business.md                # Business (W3:BusinessAgent)
│   ├── design.md                  # Design (W4:DesignAgent)
│   └── ops.md                     # Operations (W7:OpsAgent)
├── templates/                     # (Phase 2) Output templates
└── governance/                    # Layer 8: Governance
    └── 00-SKILL-MATURITY-REGISTRY.yaml  # Central registry
```

## 9 Layer Model

| Layer | Tên | Cách comply |
|:-----:|------|------------|
| 0 | Use Case & Trigger Map | `description` + `metadata.tags` trong frontmatter |
| 1 | Metadata | Extended YAML frontmatter (version, worker-id, maturity, tags) |
| 2 | Core SKILL.md | Goal + Instructions + Examples + Constraints |
| 3 | References | Tách tri thức nền → `references/` folder |
| 4 | Examples | ≥3 categories: ✅ Happy Path, ⚠️ Edge Case, ❌ Anti-Example |
| 5 | Scripts & Tools | Validation/automation scripts trong `scripts/` |
| 6 | Assets & Templates | Output templates trong `assets/templates/` |
| 7 | Output Contract | Self-check rubric + format requirements |
| 8 | Governance | CHANGELOG.md + version + owner trong metadata |

## Cách sử dụng

### Tạo skill mới
1. Copy `SKILL-TEMPLATE-V2.md` → `new-skill/SKILL.md`
2. Chọn Output Contract phù hợp domain
3. Fill theo template, đảm bảo ≥3 examples

### Nâng cấp skill cũ
1. Tra `governance/00-SKILL-MATURITY-REGISTRY.yaml` → xem tier hiện tại
2. Xác định layers thiếu
3. Bổ sung theo thứ tự: L7 (Contract) → L4 (Examples) → L3 (References) → L5 (Scripts)

### Audit skill
1. Chạy maturity check theo 9 layers
2. Update tier trong registry
3. Đặt upgrade priority

## Naming Conventions

| Folder | Dùng cho | Ví dụ |
|--------|---------|-------|
| `references/` | Tri thức nền (L3) | domain-knowledge.md, schemas.md |
| `examples/` | Ví dụ I/O (L4) | happy-path.md, edge-cases.md |
| `scripts/` | Scripts & Tools (L5) | validate.py, health_check.py |
| `assets/templates/` | Templates (L6) | output-template.md, checklist.md |

> ⚠️ **Convention**: Dùng `references/` thay vì `resources/` hoặc `modules/`.
> Các skill cũ dùng tên khác sẽ được migrate dần.
