# Evidence bank schema

Mỗi kết luận về twin phải bám vào các evidence unit.

```yaml
id: ""
source_id: ""
artifact_type: ""
excerpt: ""
role: "trigger | input | step | owner | handoff | decision_rule | exception | approval | metric | cadence | control | escalation | output"
signals:
  scope: []
  role_system: []
  process_system: []
  decision_system: []
  metric_system: []
  tooling_system: []
strength: 1
cross_source_support: []
notes: ""
```

## Quy tắc
- Không dựng rule lõi chỉ từ một excerpt đẹp.
- Ưu tiên evidence xuất hiện ở nhiều nguồn hoặc nhiều loại artefact.
- Giữ excerpt đủ dài để thấy owner, trigger, exception hoặc output khi có.
