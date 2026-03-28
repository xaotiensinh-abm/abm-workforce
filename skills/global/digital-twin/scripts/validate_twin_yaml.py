#!/usr/bin/env python3
"""Validate enterprise twin.yaml for the digital-twin skill."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any
import yaml

REQUIRED_TOP_LEVEL = {
    "version": int,
    "profile": dict,
    "scope": dict,
    "operating_model": dict,
    "role_system": dict,
    "process_system": dict,
    "decision_system": dict,
    "knowledge_system": dict,
    "tooling_system": dict,
    "artifact_adaptation": dict,
    "anti_patterns": list,
    "convergence": dict,
    "quality_notes": dict,
}

SECTION_SPECS = {
    "profile": {
        "label": str,
        "primary_language": str,
        "source_count": int,
        "source_mix": dict,
        "confidence": str,
        "status": str,
    },
    "scope": {
        "team_or_business_area": str,
        "boundary": str,
        "primary_users": list,
        "time_horizon": str,
    },
    "operating_model": {
        "mission": str,
        "operating_principles": list,
        "service_boundaries": list,
        "standard_of_execution": str,
    },
    "role_system": {
        "core_roles": list,
        "responsibilities": list,
        "handoff_patterns": list,
        "escalation_paths": list,
    },
    "process_system": {
        "core_processes": list,
        "trigger_map": list,
        "input_output_pairs": list,
        "sla_expectations": list,
    },
    "decision_system": {
        "decision_types": list,
        "decision_rules": list,
        "approval_layers": list,
        "exception_rules": list,
    },
    "knowledge_system": {
        "canonical_artifacts": list,
        "reporting_cadence": list,
        "metric_stack": list,
        "glossary_terms": list,
    },
    "tooling_system": {
        "systems": list,
        "system_roles": list,
        "data_dependencies": list,
        "failure_points": list,
    },
    "artifact_adaptation": {
        "sop": str,
        "playbook": str,
        "onboarding_guide": str,
        "memo": str,
        "report_template": str,
        "meeting_brief": str,
        "checklist": str,
        "faq": str,
        "dashboard_note": str,
        "escalation_note": str,
    },
    "convergence": {
        "invariants": list,
        "tendencies": list,
        "accidents": list,
    },
    "quality_notes": {
        "strengths": list,
        "limitations": list,
        "mixed_source_warning": str,
        "coverage_gaps": list,
    },
}

OPTIONAL_SECTION_SPECS = {
    "orchestration_system": {
        "source_packs": list,
        "composition_goal": str,
        "integration_points": list,
        "shared_metrics": list,
        "boundary_notes": list,
    }
}

ALLOWED_CONFIDENCE = {"low", "usable", "high"}
ALLOWED_STATUS = {"provisional", "stable", "mature"}

def fail(msg: str):
    return False, msg

def load_yaml(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def ensure_keys(obj: dict[str, Any], spec: dict[str, type], prefix: str):
    for key, expected_type in spec.items():
        if key not in obj:
            return fail(f"Missing key: {prefix}{key}")
        if not isinstance(obj[key], expected_type):
            return fail(f"Key {prefix}{key} must be {expected_type.__name__}, got {type(obj[key]).__name__}")
    return True, 'ok'

def validate_twin_yaml(path: Path):
    if not path.exists():
        return fail(f"File not found: {path}")
    try:
        data = load_yaml(path)
    except Exception as e:
        return fail(f"Failed to parse YAML: {e}")
    if not isinstance(data, dict):
        return fail('Root of twin.yaml must be a mapping')
    ok, msg = ensure_keys(data, REQUIRED_TOP_LEVEL, '')
    if not ok:
        return ok, msg
    for section, spec in SECTION_SPECS.items():
        ok, msg = ensure_keys(data[section], spec, f'{section}.')
        if not ok:
            return ok, msg
    for section, spec in OPTIONAL_SECTION_SPECS.items():
        if section in data:
            if not isinstance(data[section], dict):
                return fail(f'{section} must be a mapping if present')
            ok, msg = ensure_keys(data[section], spec, f'{section}.')
            if not ok:
                return ok, msg
    if data['profile']['primary_language'] != 'vi':
        return fail("profile.primary_language must be 'vi' for this MVP skill")
    if data['profile']['confidence'] not in ALLOWED_CONFIDENCE:
        return fail('profile.confidence must be one of: low, usable, high')
    if data['profile']['status'] not in ALLOWED_STATUS:
        return fail('profile.status must be one of: provisional, stable, mature')
    sm = data['profile']['source_mix']
    for k in ('upload','pasted_text','url'):
        if k not in sm or not isinstance(sm[k], int):
            return fail(f'profile.source_mix.{k} must exist and be int')
    if data['profile']['source_count'] < sum(sm.values()):
        return fail('profile.source_count should be greater than or equal to the sum of source_mix values')
    if not data['profile']['label'].strip():
        return fail('profile.label must not be empty')
    if not data['scope']['team_or_business_area'].strip():
        return fail('scope.team_or_business_area must not be empty')
    if not data['scope']['boundary'].strip():
        return fail('scope.boundary must not be empty')
    content_lists = [
        data['role_system']['core_roles'],
        data['process_system']['core_processes'],
        data['decision_system']['decision_rules'],
    ]
    if all(len(v) == 0 for v in content_lists):
        return fail('twin.yaml is too empty: fill at least one of role_system.core_roles, process_system.core_processes, decision_system.decision_rules')
    return True, 'twin.yaml is valid'

def main():
    if len(sys.argv) != 2:
        print('Usage: python validate_twin_yaml.py path/to/twin.yaml')
        return 1
    valid, message = validate_twin_yaml(Path(sys.argv[1]))
    print(message)
    return 0 if valid else 1

if __name__ == '__main__':
    raise SystemExit(main())
