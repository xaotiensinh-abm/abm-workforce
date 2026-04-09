---
name: "hermes-hub-client"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "Tìm kiếm, đánh giá và import skills từ Hermes Skills Hub ecosystem (agentskills.io, skills.sh, GitHub taps) vào ABM-Workforce. Auto-convert Hermes format → ABM format. Quarantine + review trước khi activate."
---

# 🌐 Hermes Hub Client — Import Skills Từ Open-Source Ecosystem

## Sử dụng khi

- CEO/Jarvis cần tìm skill mới cho một lĩnh vực (ví dụ: kubernetes, SEO, data pipeline)
- Muốn xem cộng đồng open-source có community skills gì hữu ích
- Import skill từ Hermes Hub / skills.sh / GitHub repos vào ABM ecosystem
- Đánh giá skill bên ngoài trước khi activate trong ABM

## KHÔNG sử dụng khi

- Tạo skill mới từ scratch → dùng `skill-generator`
- Cải thiện skill hiện có → dùng `capability-evolver`
- Quản lý skill nội bộ ABM → dùng `skill-manifest.csv` trực tiếp

## NGUỒN DỮ LIỆU

Hermes-agent v0.8.0 tích hợp 6+ skill sources:

| Source | ID | Mô tả |
|--------|-----|--------|
| Official Optional | `official` | Maintained trong Hermes repo |
| skills.sh | `skills-sh` | Vercel's public directory |
| Well-known endpoints | `well-known` | URL-based discovery (/.well-known/skills/) |
| GitHub taps | `github` | openai/skills, anthropics/skills, VoltAgent... |
| ClawHub | `clawhub` | Third-party marketplace |
| LobeHub | `lobehub` | Community marketplace |

## QUY TRÌNH IMPORT 5 BƯỚC

```
Bước 1: SEARCH   → Tìm skill theo keyword từ nhiều sources
Bước 2: INSPECT  → Xem chi tiết skill (nội dung, metadata, dependencies)
Bước 3: EVALUATE → Đánh giá: có trùng ABM skill hiện có không? Chất lượng?
Bước 4: CONVERT  → Hermes SKILL.md → ABM SKILL.md (auto-convert format)
Bước 5: REVIEW   → Quarantine → CEO approve → Activate vào ABM
```

### Bước 1: Search

```bash
# Tìm skills về kubernetes
python scripts/search_hub.py --query "kubernetes"

# Tìm từ source cụ thể
python scripts/search_hub.py --query "react" --source skills-sh

# Tìm từ GitHub tap
python scripts/search_hub.py --query "security" --source github --tap "openai/skills"
```

### Bước 2-3: Inspect + Evaluate

```bash
# Xem chi tiết skill
python scripts/search_hub.py --inspect "openai/skills/k8s"

# So sánh với ABM skills hiện có
python scripts/search_hub.py --compare "skill-name" --manifest _abm/_config/skill-manifest.csv
```

### Bước 4: Convert Format

```bash
# Convert Hermes → ABM format
python scripts/format_adapter.py --input /path/to/hermes/SKILL.md --output /path/to/abm/SKILL.md

# Convert và đặt vào quarantine
python scripts/install_skill.py --source "github:openai/skills/k8s" --quarantine
```

### Bước 5: Activate

```bash
# Review skill trong quarantine
python scripts/install_skill.py --approve "skill-name"

# Hoặc reject
python scripts/install_skill.py --reject "skill-name" --reason "trùng với ABM skill X"
```

## FORMAT CONVERSION RULES

| Hermes Section | ABM Section | Ghi chú |
|---------------|-------------|---------|
| `name` | `name` | Giữ nguyên |
| `description` | `description` | Dịch sang tiếng Việt nếu cần |
| `version` | `version` | Giữ nguyên |
| *(không có)* | `author` | Default: "Hermes Hub Import" |
| *(không có)* | `last_updated_date` | Ngày import |
| `When to Use` | `Sử dụng khi` | Dịch |
| *(không có)* | `KHÔNG sử dụng khi` | Thêm routing rules |
| `Procedure` | `Quy trình` | Dịch |
| `Pitfalls` | `Quy tắc sắt` | Dịch |
| `Verification` | `Output format` | Adapt |
| `metadata.hermes.tags` | *(ghi chú)* | Lưu vào comment |
| `metadata.hermes.category` | *(thư mục)* | Map → ABM category |
| `fallback_for_toolsets` | `KHÔNG sử dụng khi` | Convert → routing rule |
| `requires_toolsets` | `Sử dụng khi` | Convert → prerequisite |

## PROGRESSIVE DISCLOSURE (từ Hermes)

ABM có thể áp dụng mô hình 3 level loading:

```
Level 0: skills-index-l0.json → [{name, description}, ...] (~3k tokens cho 110 skills)
Level 1: skill_view(name)     → Full SKILL.md content
Level 2: skill_view(name, path) → Specific reference file trong scripts/
```

Jarvis chỉ load Level 0 khi bắt đầu. Khi cần → load Level 1 (full SKILL.md).
Khi cần scripts/templates → load Level 2.

> [!IMPORTANT]
> Progressive Disclosure giúp giảm ~80% token usage khi routing skills.
> Thay vì load tất cả 110 SKILL.md, chỉ load index 3k tokens.

## QUY TẮC SẮT

1. **KHÔNG import skill chưa qua quarantine** — CEO phải approve
2. **KHÔNG import skill trùng** — check skill-manifest.csv trước
3. **Always add ABM frontmatter** — author, last_updated_date, version
4. **Always add routing** — "Sử dụng khi" + "KHÔNG sử dụng khi"
5. **Giữ attribution** — ghi rõ source (hermes-hub:source-id/skill-path)
6. **Security scan** — kiểm tra scripts/ cho dangerous operations

## OUTPUT FORMAT

```yaml
import_result:
  skill_name: "imported-skill"
  source: "github:openai/skills/k8s"
  original_format: "hermes"
  converted_format: "abm"
  status: "quarantine | approved | rejected"
  conflicts: ["existing-skill-name"]  # nếu có trùng
  files_created:
    - "_abm/bmm/agents/skills/{name}/SKILL.md"
    - "_abm/bmm/agents/skills/{name}/scripts/..."
  reviewer: "CEO"
  review_date: "YYYY-MM-DD"
```

## Related Skills

- skill-generator (tạo skill mới), capability-evolver (cải thiện skill)
- context-engineering (progressive disclosure), security-review (scan imported skills)
