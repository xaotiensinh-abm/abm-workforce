# twin.yaml schema

`twin.yaml` là lớp canonical machine-readable của enterprise twin.

## Top-level sections
- profile
- scope
- operating_model
- role_system
- process_system
- decision_system
- knowledge_system
- tooling_system
- artifact_adaptation
- anti_patterns
- convergence
- quality_notes
- orchestration_system (optional)

## Yêu cầu
- `profile.label` không để trống
- `profile.primary_language` hiện là `vi`
- `scope.team_or_business_area` và `scope.boundary` phải rõ
- ít nhất một trong `process_system.core_processes`, `decision_system.decision_rules`, `role_system.core_roles` phải có nội dung

## orchestration_system (optional)
Dùng khi twin được ghép từ nhiều pack ngành, sub-pack hoặc functional pack.

Các trường nên có:
- `source_packs`: danh sách pack nền được tham chiếu
- `composition_goal`: lý do ghép pack
- `integration_points`: chỗ giao nhau giữa các pack như lead-to-legal, booking-to-handover, schedule-to-treatment-plan, order-to-governance
- `shared_metrics`: metric dùng để nối nhiều pack
- `boundary_notes`: ghi rõ ranh giới để tránh copy nhầm facts từ pack mẫu
