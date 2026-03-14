---
name: memory-keeper
description: Backup and snapshot all critical agent context — contracts, attestations, task logs, knowledge items — into archive with git sync. Use before maintenance, after critical tasks, or on schedule.
---

## KHONG su dung khi

- Can luu task state -> dung save. Can tinh che tri thuc -> dung knowledge-crystallizer.


# Memory Keeper — Context Backup & Recovery

> Adapted from CLAWDBOT's [memory-keeper](https://github.com/CrimsonDevil333333/memory-keeper) for the Jarvis Multi-Agent system.

## Overview

Copies critical system state files into a safe archive and optionally commits to git.
Preserves directory structure for easy restore and history inspection.

## Khi nào sử dụng
- Before system maintenance/upgrade
- After completing major task group
- Scheduled backup (via HEARTBEAT)
- Before destructive operations
- Recovery after corruption

## Files to Backup

### Critical (ALWAYS backup)
```
{output_folder}/task-log.yaml                    → Task completion history
{output_folder}/contracts/*.yaml                 → All task contracts
{output_folder}/attestations/*.yaml              → All attestations
_abm/bmm/agents/jarvis/SOUL.md                  → Agent consciousness
_abm/bmm/agents/jarvis/AGENTS.md                → Agent registry
_abm/bmm/agents/jarvis/HEARTBEAT.md             → Periodic tasks
_abm/bmm/agents/jarvis/MEMORY.md                → Memory pointers
_abm/bmm/agents/jarvis/USER.md                  → User preferences
_abm/bmm/data/governance-policy.yaml            → Governance rules
_abm/_config/skill-manifest.csv                 → Skill registry
```

### Optional (backup if changed)
```
_abm/bmm/agents/jarvis-orchestrator.md          → Full agent definition
_abm/bmm/agents/skills/*/SKILL.md               → All skill definitions
_abm/bmm/data/task-contract-template.yaml       → Contract template
_abm/bmm/data/attestation-template.yaml         → Attestation template
```

## Backup Process

### Step 1: Create Snapshot
```
Archive layout:
{archive_path}/
├── {date}/
│   ├── task-log.yaml
│   ├── contracts/
│   │   └── *.yaml
│   ├── attestations/
│   │   └── *.yaml
│   ├── consciousness/
│   │   ├── SOUL.md
│   │   ├── AGENTS.md
│   │   ├── HEARTBEAT.md
│   │   ├── MEMORY.md
│   │   └── USER.md
│   ├── governance/
│   │   └── governance-policy.yaml
│   └── skills/
│       └── skill-manifest.csv
```

### Step 2: Git Commit (optional)
```bash
cd {archive_path}
git add .
git commit -m "backup: {date} — {task_count} tasks, {skill_count} skills"
git push origin main
```

### Step 3: Verify Backup
```
□ All critical files copied?
□ File sizes match originals?
□ Git commit successful?
□ Can restore from backup?
```

## Restore Process

```bash
# Restore specific date
cp -r {archive_path}/{date}/* {project_root}/

# Verify restoration
diff {archive_path}/{date}/task-log.yaml {output_folder}/task-log.yaml
```

## Integration with HEARTBEAT

In `jarvis/HEARTBEAT.md`:
```
Every session end:
- [ ] Run memory-keeper backup
```

## Safety Rules
- ❌ NEVER overwrite backup with empty files
- ❌ NEVER delete backup directory
- ✅ ALWAYS verify file count after backup
- ✅ ALWAYS keep at least 7 daily backups
- ✅ ALWAYS git commit with descriptive message
