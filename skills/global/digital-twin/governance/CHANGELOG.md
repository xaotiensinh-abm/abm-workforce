# Changelog: digital-twin (L8)

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] - 2026-03-28

### Added
- **Standardized Metadata**: `metadata.json` (L1) with Tier-S classification.
- **Example Layer**: `examples/` (L4) with Happy, Edge, and Anti-pattern cases.
- **Output Contract**: `output-contracts/twin.md` (L7) based on `_standards/output-contracts/ops.md`.
- **Governance Layer**: `governance/` (L8) directory with `MATURITY.md` and `CHANGELOG.md`.

### Modified
- **Directory Structure**: Upgraded from partial compliance (7/9) to full 9-Layer (9/9).
- **Audit Logic**: Integrated with `_standards/scripts/skill_health_check.py`.

### Fixed
- **Score Discrepancy**: Standardized folder names to ensure recognition by the Health Check script.

---

## [2.0.0] - 2026-01-15

### Added
- **Referenced Modes**: `build`, `operate`, `update`, `audit`.
- **Reference Library**: 62 core reference files.
- **Validation Script**: `validate_twin_yaml.py`.

---

## [1.0.0] - 2025-11-20

### Added
- **Initial Release**: Core `SKILL.md` for Enterprise OS.
