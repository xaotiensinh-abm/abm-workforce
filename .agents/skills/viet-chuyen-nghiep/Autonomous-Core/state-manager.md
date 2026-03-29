# Quản lý Trạng thái Runtime

## Mục đích

Theo dõi **trạng thái toàn bộ session** — task nào đang chạy, worker nào
đã xong, output nào đã thu, risk flags nào cần chú ý.

## State Structure

```yaml
session_state:
  # --- Task identity ---
  task_id: "[auto-generated]"
  task_type: "[write-new/edit-draft/...]"
  pipeline: "[pipeline name]"
  complexity: "[light/standard/heavy]"
  started_at: "[timestamp]"
  
  # --- Pipeline progress ---
  current_step: "[worker đang chạy]"
  completed_steps:
    - worker: "[intake-worker]"
      status: "done"
      output_key: "[intake_output]"
    - worker: "[research-worker]"  
      status: "done"
      output_key: "[research_output]"
  pending_steps: ["strategy-worker", "longform-worker", "quality-worker"]
  
  # --- Collected outputs ---
  outputs:
    intake_output: { ... }
    research_output: { ... }
  
  # --- Risk & issues ---
  risk_flags:
    - type: "[unverified_claim/source_conflict/domain_risk]"
      detail: "[mô tả]"
      source_worker: "[research-worker]"
  
  # --- Revision tracking ---
  revision_count: 0
  max_revisions: 2
  
  # --- Final state ---
  final_verdict: "[pending/pass/needs_revision/fail]"
  confidence: "[high/medium/low]"
```

## State Transitions

```
INITIALIZED → INTAKE_RUNNING → INTAKE_DONE
→ RESEARCH_RUNNING → RESEARCH_DONE
→ STRATEGY_RUNNING → STRATEGY_DONE
→ WRITING_RUNNING → WRITING_DONE
→ QUALITY_RUNNING → QUALITY_DONE
    ├─ PASS → COMPLETED ✅
    ├─ NEEDS_REVISION → REVISION_LOOP (back to WRITING)
    └─ FAIL → ESCALATED
```

## State Operations

| Operation | Trigger | Action |
|-----------|---------|--------|
| `init_session` | Task start | Create state object |
| `update_step` | Worker complete | Mark step done, store output |
| `add_risk_flag` | Worker detect risk | Append to risk_flags |
| `increment_revision` | Quality reject | revision_count++ |
| `finalize` | All steps pass | Set final_verdict |

## Ràng buộc

- State LUÔN được update — không bao giờ để stale
- Mỗi worker output PHẢI được lưu — cho cross-reference
- max_revisions = 2 — vượt = escalate
- Risk flags tích lũy — không bị xóa khi retry
