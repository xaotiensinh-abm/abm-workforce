# Architecture Decisions — ADR Log

## ADR-001: Hybrid 3-Tier Skill Structure (2026-03-14)
- **Decision**: Skills ≤120 monolith, 120-250 +CHECKLIST, ≥250 full modular
- **Rationale**: Balance context efficiency + quality gates
- **Alternatives rejected**: Full modular (context 6x), pure monolith (no traceability)

## ADR-002: Global Deployment via Junctions (2026-03-14)
- **Decision**: Use Windows junction links from ~/.agents/skills/ → ABM source
- **Rationale**: Single source of truth in project, available globally
- **Risk**: Junction breaks if source moves

## ADR-003: Vietnamese-First Rules (2026-03)
- **Decision**: 100% Vietnamese for all business output
- **Rationale**: Target market = VN CEOs, readability first
- **Exception**: Code comments, technical terms with VN explanation
