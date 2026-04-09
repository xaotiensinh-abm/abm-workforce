#!/usr/bin/env python3
"""
Format Adapter — Convert Hermes SKILL.md → ABM SKILL.md

Hermes format:
  - When to Use / Procedure / Pitfalls / Verification
  - metadata.hermes.{tags, category, fallback_for_toolsets, requires_toolsets}

ABM format:
  - Sử dụng khi / KHÔNG sử dụng khi / Quy trình / Quy tắc sắt / Output format / Related Skills
  - Frontmatter: name, version, author, last_updated_date, description

Usage:
  python format_adapter.py --input hermes_skill.md --output abm_skill.md
  python format_adapter.py --input hermes_skill.md --stdout
  echo "content" | python format_adapter.py --stdin --output abm_skill.md
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def parse_hermes_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from Hermes SKILL.md."""
    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()

            for line in fm_text.split("\n"):
                line = line.strip()
                if ":" in line and not line.startswith("#"):
                    key, _, value = line.partition(":")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if value:
                        frontmatter[key] = value

    return frontmatter, body


def extract_sections(body: str) -> dict:
    """Extract major sections from Hermes skill body."""
    sections = {}
    current_section = "intro"
    current_content = []

    for line in body.split("\n"):
        # Match ## headings
        heading_match = re.match(r'^#{1,3}\s+(.+)', line)
        if heading_match:
            # Save previous section
            if current_content:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = heading_match.group(1).strip()
            current_content = []
        else:
            current_content.append(line)

    # Save last section
    if current_content:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def map_section_name(hermes_name: str) -> str:
    """Map Hermes section heading → ABM section heading."""
    name_lower = hermes_name.lower().strip()

    mapping = {
        "when to use": "Sử dụng khi",
        "usage": "Sử dụng khi",
        "triggers": "Sử dụng khi",
        "trigger conditions": "Sử dụng khi",
        "procedure": "Quy trình",
        "steps": "Quy trình",
        "instructions": "Quy trình",
        "how to use": "Quy trình",
        "workflow": "Quy trình",
        "pitfalls": "Quy tắc sắt",
        "warnings": "Quy tắc sắt",
        "known issues": "Quy tắc sắt",
        "common mistakes": "Quy tắc sắt",
        "gotchas": "Quy tắc sắt",
        "verification": "Output format",
        "output": "Output format",
        "expected output": "Output format",
        "examples": "Ví dụ",
        "example": "Ví dụ",
        "configuration": "Cấu hình",
        "config": "Cấu hình",
        "setup": "Cấu hình",
        "references": "Tài liệu tham khảo",
        "resources": "Tài liệu tham khảo",
    }

    for key, value in mapping.items():
        if key in name_lower:
            return value

    # Keep original if no mapping found
    return hermes_name


def convert_hermes_to_abm(content: str, source: str = "hermes-hub") -> str:
    """Convert Hermes SKILL.md content → ABM SKILL.md format."""

    frontmatter, body = parse_hermes_frontmatter(content)
    sections = extract_sections(body)

    # Build ABM frontmatter
    name = frontmatter.get("name", "imported-skill")
    version = frontmatter.get("version", "1.0.0")
    description = frontmatter.get("description", "Imported from Hermes Hub")
    today = date.today().isoformat()

    abm_frontmatter = f"""---
name: "{name}"
version: {version}
author: "Hermes Hub Import"
last_updated_date: {today}
description: "{description}"
source: "{source}"
---"""

    # Build title
    title_section = sections.get("intro", "")
    # Find first # heading in intro
    title_match = re.match(r'^#\s+(.+)', title_section)
    title = title_match.group(1) if title_match else f"# {name}"
    if not title.startswith("#"):
        title = f"# {title}"

    # Build body sections
    abm_sections = []

    # "Sử dụng khi" section
    for key in sections:
        mapped = map_section_name(key)
        if mapped == "Sử dụng khi":
            abm_sections.append(f"## Sử dụng khi\n\n{sections[key]}")
            break
    else:
        abm_sections.append("## Sử dụng khi\n\n- *(Imported — cần bổ sung trigger conditions)*")

    # "KHÔNG sử dụng khi" section (Hermes doesn't have this — generate from metadata)
    not_use = []
    # Check for fallback_for_toolsets hint in original content
    if "fallback_for" in content.lower():
        not_use.append("- Skill này là fallback — kiểm tra skill chính trước")
    not_use.append("- *(Cần CEO review và bổ sung routing rules)*")
    abm_sections.append(f"## KHÔNG sử dụng khi\n\n" + "\n".join(not_use))

    # Map remaining sections
    for key, value in sections.items():
        if key == "intro":
            continue
        mapped = map_section_name(key)
        if mapped in ("Sử dụng khi",):  # Already added
            continue
        abm_sections.append(f"## {mapped}\n\n{value}")

    # Add "Related Skills" if not present
    has_related = any("Related" in s for s in abm_sections)
    if not has_related:
        abm_sections.append("## Related Skills\n\n- *(Cần mapping với ABM skills hiện có)*")

    # Assemble
    result = f"""{abm_frontmatter}

{title}

> ⚠️ **IMPORTED FROM HERMES HUB** — Source: `{source}`
> Cần CEO review trước khi activate. Chạy `/review` để đánh giá.

{chr(10).join(abm_sections)}
"""

    return result.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Hermes → ABM SKILL.md Format Converter")
    parser.add_argument("--input", "-i", help="Input Hermes SKILL.md file path")
    parser.add_argument("--output", "-o", help="Output ABM SKILL.md file path")
    parser.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--stdout", action="store_true", help="Write to stdout")
    parser.add_argument("--source", "-s", default="hermes-hub", help="Source identifier")
    parser.add_argument("--dry-run", action="store_true", help="Preview conversion without writing")

    args = parser.parse_args()

    # Read input
    if args.stdin:
        content = sys.stdin.read()
    elif args.input:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"❌ File không tồn tại: {args.input}", file=sys.stderr)
            sys.exit(1)
        content = input_path.read_text(encoding="utf-8")
    else:
        parser.error("Cần --input hoặc --stdin")
        return

    # Convert
    result = convert_hermes_to_abm(content, source=args.source)

    # Output
    if args.dry_run:
        print("🔄 [DRY RUN] Preview conversion:")
        print(f"   Source: {args.source}")
        print(f"   Input : {args.input or 'stdin'}")
        print(f"   Output: {args.output or 'stdout'}")
        print(f"{'='*60}")
        print(result)
        return

    if args.stdout or not args.output:
        print(result)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"✅ Converted: {args.output}")
        print(f"   Lines: {result.count(chr(10))}")
        print(f"   Size: {len(result)} bytes")


if __name__ == "__main__":
    main()
