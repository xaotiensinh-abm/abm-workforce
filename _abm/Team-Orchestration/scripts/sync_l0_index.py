#!/usr/bin/env python3
"""
Sync Level 0 Skills Index (skills-index-l0.json)
Phân tích toàn bộ SKILL.md trong hệ thống ABM và trích xuất Name + Description, 
tạo ra file JSON siêu tối ưu để Jarvis có thể nạp toàn bộ danh mục skill mà không bị quá tải context.
"""

import json
import re
from pathlib import Path

# Paths
ABM_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SKILLS_DIR = ABM_ROOT / "_abm" / "bmm" / "agents" / "skills"
CONFIG_DIR = ABM_ROOT / "_abm" / "_config"
OUTPUT_FILE = CONFIG_DIR / "skills-index-l0.json"


def parse_frontmatter(content: str) -> dict:
    """Trích xuất frontmatter YAML từ SKILL.md một cách an toàn."""
    frontmatter = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split("\n"):
                line = line.strip()
                if ":" in line and not line.startswith("#"):
                    key, _, value = line.partition(":")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if value:
                        frontmatter[key] = value
    return frontmatter


def main():
    if not SKILLS_DIR.exists():
        print(f"❌ Không tìm thấy thư mục: {SKILLS_DIR}")
        return

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    l0_index = []
    
    # Duyệt qua các sub_dir trong skills/
    for skill_path in sorted(SKILLS_DIR.iterdir()):
        # Bỏ qua hidden dirs (e.g. .git), _quarantine, và files
        if not skill_path.is_dir() or skill_path.name.startswith(".") or skill_path.name.startswith("_"):
            continue
            
        skill_md_path = skill_path / "SKILL.md"
        if not skill_md_path.exists():
            continue
            
        content = skill_md_path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(content)
        
        name = frontmatter.get("name", skill_path.name)
        desc = frontmatter.get("description", "Không có mô tả.")
        
        l0_index.append({
            "name": name,
            "description": desc
        })
        
    # Write ra file JSON
    OUTPUT_FILE.write_text(json.dumps(l0_index, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"✅ Đã tạo Level 0 Index tại: {OUTPUT_FILE}")
    print(f"   Tổng số skills: {len(l0_index)}")
    
    # Tính toán kích thước token ước tính (~ 4 chars / token)
    json_str = json.dumps(l0_index, ensure_ascii=False)
    approx_tokens = len(json_str) // 4
    print(f"   Ước tính Payload Tokens: ~{approx_tokens} tokens")


if __name__ == "__main__":
    main()
