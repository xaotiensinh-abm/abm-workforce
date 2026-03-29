# HEARTBEAT
# Periodic tasks Jarvis should check automatically

## Every task completion:
- [ ] Log to task-log.yaml
- [ ] Save contract to contracts/{task_id}.yaml
- [ ] Save attestation to attestations/{task_id}.yaml

## Every 10 tasks:
- [ ] Run knowledge-crystallizer skill
- [ ] Generate KPI dashboard
- [ ] Check retry_rate — if >20%, investigate

## Every session end:
- [ ] Run memory-keeper backup
- [ ] Summarize session in knowledge item

## Red flags to auto-escalate:
- Worker confidence < 0.5
- 2+ consecutive task failures
- Security evaluator finding severity=critical
- Human gate triggered but not responded to
