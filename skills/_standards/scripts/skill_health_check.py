#!/usr/bin/env python3
"""
ABM-Workforce Skill Health Check v1.0
Validates skill compliance against 9-Layer Skill Engineering framework.

Usage:
    python skill_health_check.py <skill_path>           # Check single skill
    python skill_health_check.py --all <skills_root>    # Check all skills
    python skill_health_check.py --report <skills_root> # Generate full report

Example:
    python skill_health_check.py C:/Users/PC/.gemini/antigravity/skills/digital-twin
    python skill_health_check.py --all C:/Users/PC/.gemini/antigravity/skills
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime


# ═══════════════════════════════════════════════
# 9-LAYER DEFINITION
# ═══════════════════════════════════════════════

LAYERS = {
    "L0": {
        "name": "Use Case & Trigger Map",
        "check": "has_description_and_tags",
        "weight": 1,
    },
    "L1": {
        "name": "Metadata (Frontmatter)",
        "check": "has_frontmatter",
        "weight": 1,
    },
    "L2": {
        "name": "Core SKILL.md",
        "check": "has_skill_md",
        "weight": 2,  # weighted higher — essential
    },
    "L3": {
        "name": "References",
        "check": "has_references",
        "weight": 1,
    },
    "L4": {
        "name": "Examples",
        "check": "has_examples",
        "weight": 1,
    },
    "L5": {
        "name": "Scripts & Tools",
        "check": "has_scripts",
        "weight": 1,
    },
    "L6": {
        "name": "Assets & Templates",
        "check": "has_assets",
        "weight": 1,
    },
    "L7": {
        "name": "Output Contract & QC",
        "check": "has_output_contract",
        "weight": 1,
    },
    "L8": {
        "name": "Governance",
        "check": "has_governance",
        "weight": 1,
    },
}

TIER_THRESHOLDS = {
    "S": 7,  # 7-9 layers
    "A": 4,  # 4-6 layers
    "B": 2,  # 2-3 layers
    "C": 0,  # 0-1 layers
}

REQUIRED_FRONTMATTER = ["name", "description"]
EXTENDED_FRONTMATTER = ["metadata.version", "metadata.worker-id", "metadata.maturity", "metadata.category", "metadata.tags"]
REFERENCE_DIRS = ["references", "resources", "modules", "knowledge"]
EXAMPLE_DIRS = ["examples"]
SCRIPT_DIRS = ["scripts"]
ASSET_DIRS = ["assets", "templates"]


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from SKILL.md content."""
    fm = {}
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return fm
    
    for line in match.group(1).strip().split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, _, value = line.partition(':')
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def read_skill_md(skill_path: Path) -> tuple[str, dict]:
    """Read SKILL.md and return (content, frontmatter)."""
    skill_file = skill_path / "SKILL.md"
    if not skill_file.exists():
        return "", {}
    
    try:
        content = skill_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            content = skill_file.read_text(encoding="utf-8-sig")
        except Exception:
            content = skill_file.read_text(encoding="latin-1")
    
    fm = parse_frontmatter(content)
    return content, fm


def check_layer(layer_id: str, skill_path: Path, content: str, fm: dict) -> dict:
    """Check a single layer compliance. Returns {passed, details, suggestions}."""
    result = {"passed": False, "details": "", "suggestions": []}
    
    if layer_id == "L0":
        # Use Case & Trigger Map: has description + tags  
        has_desc = bool(fm.get("description", "").strip())
        has_tags = "tags" in str(fm) or "metadata" in content.lower()
        result["passed"] = has_desc
        result["details"] = f"description={'✅' if has_desc else '❌'}, tags={'✅' if has_tags else '⚠️'}"
        if not has_desc:
            result["suggestions"].append("Add 'description' to frontmatter")
        if not has_tags:
            result["suggestions"].append("Add 'metadata.tags' for trigger mapping")
            
    elif layer_id == "L1":
        # Metadata: has proper frontmatter
        has_name = bool(fm.get("name", ""))
        has_desc = bool(fm.get("description", ""))
        result["passed"] = has_name and has_desc
        missing = [f for f in REQUIRED_FRONTMATTER if not fm.get(f)]
        result["details"] = f"required={2-len(missing)}/2, extended={'partial' if any(k in str(fm) for k in ['version','worker','maturity']) else 'none'}"
        if missing:
            result["suggestions"].append(f"Add required frontmatter: {', '.join(missing)}")
            
    elif layer_id == "L2":
        # Core SKILL.md: substantial content with structure
        # Method 1: Check for canonical sections
        sections = {
            "goal": bool(re.search(r'#\s*(Goal|PURPOSE|Mục tiêu|Overview|Role|Identity|Mission)', content, re.I)),
            "instructions": bool(re.search(r'#\s*(Instructions?|Steps?|How|Workflow|Pipeline|Hướng dẫn|Process|Procedure|Phase|Stage|Module|Core)', content, re.I)),
            "examples": bool(re.search(r'#\s*(Examples?|Ví dụ|Usage|Demo|Sample|Template|Pattern|Case)', content, re.I)),
            "constraints": bool(re.search(r'#\s*(Constraints?|Rules?|Limitations?|Giới hạn|KHÔNG|Never|Important|Warning|Critical|Anti)', content, re.I)),
        }
        found_sections = sum(sections.values())
        # Method 2: Count markdown headings and word count
        heading_count = len(re.findall(r'^#{1,4}\s+', content, re.MULTILINE))
        word_count = len(content.split())
        # Pass if: 2+ canonical sections, OR 3+ headings with 100+ words
        result["passed"] = found_sections >= 2 or (heading_count >= 3 and word_count >= 100)
        result["details"] = f"{found_sections}/4 canonical, {heading_count} headings, {word_count} words"
        if not result["passed"]:
            missing = [k for k, v in sections.items() if not v]
            result["suggestions"].append(f"Add sections: {', '.join(missing[:3])}")
            
    elif layer_id == "L3":
        # References: has references/ or resources/ directory
        has_refs = any((skill_path / d).is_dir() for d in REFERENCE_DIRS)
        inline_refs = content.lower().count("reference") + content.lower().count("resource")
        result["passed"] = has_refs
        result["details"] = f"directory={'✅' if has_refs else '❌'}, inline_mentions={inline_refs}"
        if not has_refs:
            result["suggestions"].append("Create references/ directory with domain knowledge files")
            
    elif layer_id == "L4":
        # Examples: has examples/ dir OR ≥3 inline examples
        has_dir = any((skill_path / d).is_dir() for d in EXAMPLE_DIRS)
        example_count = len(re.findall(r'##\s*(?:Ví dụ|Example)\s*\d', content, re.I))
        if example_count == 0:
            example_count = len(re.findall(r'```\s*\n.*?\n```', content, re.DOTALL))
            example_count = min(example_count, 5)  # cap code blocks
        result["passed"] = has_dir or example_count >= 3
        result["details"] = f"directory={'✅' if has_dir else '❌'}, inline_examples={example_count}"
        if not result["passed"]:
            result["suggestions"].append("Add ≥3 examples: ✅ Happy Path, ⚠️ Edge Case, ❌ Anti-Example")
            
    elif layer_id == "L5":
        # Scripts & Tools
        has_scripts = any((skill_path / d).is_dir() for d in SCRIPT_DIRS)
        script_files = list(skill_path.glob("scripts/*")) if (skill_path / "scripts").exists() else []
        result["passed"] = has_scripts and len(script_files) > 0
        result["details"] = f"directory={'✅' if has_scripts else '❌'}, files={len(script_files)}"
        if not result["passed"]:
            result["suggestions"].append("Create scripts/ with validation or automation tools")
            
    elif layer_id == "L6":
        # Assets & Templates
        has_assets = any((skill_path / d).is_dir() for d in ASSET_DIRS)
        has_nested = (skill_path / "assets" / "templates").is_dir()
        result["passed"] = has_assets
        result["details"] = f"assets={'✅' if has_assets else '❌'}, templates={'✅' if has_nested else '❌'}"
        if not result["passed"]:
            result["suggestions"].append("Create assets/templates/ with output template files")
            
    elif layer_id == "L7":
        # Output Contract & QC
        has_contract = (skill_path / "OUTPUT-CONTRACT.md").exists()
        has_rubric = bool(re.search(r'(rubric|scorecard|checklist|quality|evaluation)', content, re.I))
        has_self_check = bool(re.search(r'(self.?check|validation|verify|assert)', content, re.I))
        result["passed"] = has_contract or (has_rubric and has_self_check)
        result["details"] = f"contract_file={'✅' if has_contract else '❌'}, inline_rubric={'✅' if has_rubric else '❌'}, self_check={'✅' if has_self_check else '❌'}"
        if not result["passed"]:
            result["suggestions"].append("Add OUTPUT-CONTRACT.md or inline rubric+self-check sections")
            
    elif layer_id == "L8":
        # Governance
        has_changelog = (skill_path / "CHANGELOG.md").exists()
        has_gov_dir = (skill_path / "governance").is_dir()
        has_gov_changelog = (skill_path / "governance" / "CHANGELOG.md").exists()
        has_maturity = (skill_path / "governance" / "MATURITY.md").exists()
        has_version = bool(fm.get("version") or re.search(r'version.*\d+\.\d+', str(fm), re.I))
        has_owner = bool(fm.get("owner") or fm.get("worker-id") or re.search(r'worker.?id', str(fm), re.I))
        result["passed"] = has_changelog or has_gov_changelog or has_gov_dir or (has_version and has_owner)
        result["details"] = f"changelog={'✅' if (has_changelog or has_gov_changelog) else '❌'}, governance_dir={'✅' if has_gov_dir else '❌'}, maturity={'✅' if has_maturity else '❌'}, version={'✅' if has_version else '❌'}, owner={'✅' if has_owner else '❌'}"
        if not result["passed"]:
            result["suggestions"].append("Add governance/CHANGELOG.md + MATURITY.md or root CHANGELOG.md")
    
    return result


def audit_skill(skill_path: Path) -> dict:
    """Full 9-layer audit of a single skill."""
    skill_path = Path(skill_path)
    content, fm = read_skill_md(skill_path)
    
    if not content:
        return {
            "name": skill_path.name,
            "path": str(skill_path),
            "error": "No SKILL.md found",
            "tier": "C",
            "score": 0,
            "layers": {},
        }
    
    layers_result = {}
    passed_count = 0
    total_suggestions = []
    
    for layer_id, layer_def in LAYERS.items():
        result = check_layer(layer_id, skill_path, content, fm)
        layers_result[layer_id] = {
            "name": layer_def["name"],
            **result,
        }
        if result["passed"]:
            passed_count += 1
        total_suggestions.extend(result["suggestions"])
    
    # Determine tier
    tier = "C"
    for t, threshold in TIER_THRESHOLDS.items():
        if passed_count >= threshold:
            tier = t
            break
    
    return {
        "name": fm.get("name", skill_path.name),
        "path": str(skill_path),
        "tier": tier,
        "score": f"{passed_count}/9",
        "passed_layers": [lid for lid, r in layers_result.items() if r["passed"]],
        "missing_layers": [lid for lid, r in layers_result.items() if not r["passed"]],
        "layers": layers_result,
        "top_suggestions": total_suggestions[:5],
        "word_count": len(content.split()),
    }


def scan_all_skills(root_path: Path) -> list[dict]:
    """Scan all skill directories under a root path."""
    results = []
    root = Path(root_path)
    
    for item in sorted(root.iterdir()):
        if item.is_dir() and not item.name.startswith(('.', '_')):
            if (item / "SKILL.md").exists():
                results.append(audit_skill(item))
    
    return results


def print_single_report(result: dict):
    """Print formatted report for a single skill."""
    tier_emoji = {"S": "🏆", "A": "⭐", "B": "📦", "C": "⚠️"}
    
    print(f"\n{'='*60}")
    print(f"  {tier_emoji.get(result['tier'], '?')} SKILL: {result['name']}")
    print(f"  Tier: {result['tier']} | Score: {result['score']} | Words: {result.get('word_count', '?')}")
    print(f"{'='*60}")
    
    if result.get("error"):
        print(f"  ❌ ERROR: {result['error']}")
        return
    
    print(f"\n  ✅ Passed: {', '.join(result['passed_layers'])}")
    print(f"  ❌ Missing: {', '.join(result['missing_layers'])}")
    
    print(f"\n  {'─'*50}")
    print(f"  {'Layer':<8} {'Status':<4} {'Details'}")
    print(f"  {'─'*50}")
    
    for lid, layer in result["layers"].items():
        status = "✅" if layer["passed"] else "❌"
        print(f"  {lid:<8} {status:<4} {layer['details'][:50]}")
    
    if result["top_suggestions"]:
        print(f"\n  📋 Top Suggestions:")
        for i, s in enumerate(result["top_suggestions"], 1):
            print(f"     {i}. {s}")
    print()


def print_summary_report(results: list[dict]):
    """Print summary report for all skills."""
    tier_counts = {"S": 0, "A": 0, "B": 0, "C": 0}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
    
    print(f"\n{'='*60}")
    print(f"  📊 ABM-WORKFORCE SKILL HEALTH REPORT")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Total Skills Scanned: {len(results)}")
    print(f"{'='*60}")
    
    print(f"\n  TIER DISTRIBUTION:")
    print(f"  🏆 Tier S (Mature):     {tier_counts.get('S', 0)}")
    print(f"  ⭐ Tier A (Structured): {tier_counts.get('A', 0)}")
    print(f"  📦 Tier B (Basic):      {tier_counts.get('B', 0)}")
    print(f"  ⚠️  Tier C (Orphan):     {tier_counts.get('C', 0)}")
    
    # Health score
    total = len(results)
    if total > 0:
        health = (tier_counts.get('S', 0) * 100 + tier_counts.get('A', 0) * 75 + 
                  tier_counts.get('B', 0) * 40 + tier_counts.get('C', 0) * 10) / total
        print(f"\n  🩺 Overall Health Score: {health:.0f}/100")
    
    # Skills by tier
    for tier_label in ["S", "A", "B", "C"]:
        tier_skills = [r for r in results if r["tier"] == tier_label]
        if tier_skills:
            print(f"\n  {'─'*50}")
            print(f"  TIER {tier_label}:")
            for r in sorted(tier_skills, key=lambda x: x["score"], reverse=True):
                print(f"    {r['score']} | {r['name']:<35} | ✅ {','.join(r['passed_layers'])}")
    
    # Most common missing layers
    missing_counter = {}
    for r in results:
        for m in r.get("missing_layers", []):
            missing_counter[m] = missing_counter.get(m, 0) + 1
    
    print(f"\n  {'─'*50}")
    print(f"  MOST COMMON GAPS:")
    for layer, count in sorted(missing_counter.items(), key=lambda x: -x[1])[:5]:
        pct = count / total * 100 if total > 0 else 0
        print(f"    {layer} ({LAYERS[layer]['name']}): {count} skills ({pct:.0f}%)")
    
    print()


def main():
    parser = argparse.ArgumentParser(description="ABM-Workforce Skill Health Check")
    parser.add_argument("path", help="Path to skill directory or skills root")
    parser.add_argument("--all", action="store_true", help="Scan all skills in directory")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--tier", choices=["S", "A", "B", "C"], help="Filter by tier")
    
    args = parser.parse_args()
    path = Path(args.path)
    
    if not path.exists():
        print(f"❌ Path not found: {path}")
        sys.exit(1)
    
    if args.all or args.report:
        results = scan_all_skills(path)
        
        if args.tier:
            results = [r for r in results if r["tier"] == args.tier]
        
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        elif args.report:
            print_summary_report(results)
        else:
            for r in results:
                print_single_report(r)
    else:
        result = audit_skill(path)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print_single_report(result)


if __name__ == "__main__":
    main()
