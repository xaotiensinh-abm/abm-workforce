"""
ABM - DũngTQ | NotebookLM Second Brain — Collector
===================================================
Thu thập và gộp SKILL.md files + session logs thành bundles
sẵn sàng upload lên Google NotebookLM.
"""

import os
import yaml
from pathlib import Path
from datetime import datetime

BRAND = "ABM - DũngTQ"
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"


def load_config() -> dict:
    """Load cấu hình từ config.yaml."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_skills(config: dict) -> list[Path]:
    """
    Gộp SKILL.md files thành 1 bundle.
    Trả về danh sách đường dẫn file bundle đã tạo.
    """
    skills_dir = Path(config["paths"]["skills_dir"])
    collected_dir = SCRIPT_DIR / config["paths"]["collected_dir"]
    collected_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n  🔍 [{BRAND}] Quét SKILL.md từ: {skills_dir}")

    # Thu thập tất cả SKILL.md (bỏ _archive)
    skills = []
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith("_"):
            continue
        skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            skills.append(skill_file)

    print(f"  📦 Tìm thấy {len(skills)} skills (bỏ _archive)")

    # Gộp tất cả vào 1 bundle
    header = (
        f"# ABM Workforce — Knowledge Brain\n"
        f"# Tập hợp tất cả SKILL.md files\n"
        f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"# By: {BRAND}\n\n"
    )

    entries = []
    for skill_file in skills:
        content = skill_file.read_text(encoding="utf-8", errors="replace")
        skill_name = skill_file.parent.name
        entry = f"\n{'='*60}\n# SKILL: {skill_name}\n# Path: {skill_file.relative_to(skills_dir)}\n{'='*60}\n\n{content}\n"
        entries.append(entry)

    bundle_path = collected_dir / "skills-bundle-01.md"
    bundle_content = header + "\n".join(entries)
    bundle_path.write_text(bundle_content, encoding="utf-8")
    total_size = bundle_path.stat().st_size
    print(f"  📄 Bundle: {len(skills)} skills, {total_size // 1024} KB → {bundle_path.name}")
    print(f"  ✅ Tổng: {len(skills)} skills → 1 bundle\n")

    return [bundle_path]


def collect_memory(config: dict) -> list[Path]:
    """
    Gộp session logs, task-log, patterns, lessons-learned thành memory bundle.
    Trả về danh sách đường dẫn file bundle đã tạo.
    """
    collected_dir = SCRIPT_DIR / config["paths"]["collected_dir"]
    collected_dir.mkdir(parents=True, exist_ok=True)

    print(f"  🧠 [{BRAND}] Thu thập Memory data...")

    parts = []
    header = (
        f"# ABM Workforce — Session Memory\n"
        f"# Bộ nhớ dài hạn: task history, session logs, patterns\n"
        f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"# By: {BRAND}\n\n"
    )

    # 1. Task log
    task_log = Path(config["paths"]["task_log"])
    if task_log.exists():
        content = task_log.read_text(encoding="utf-8", errors="replace")
        parts.append(f"\n{'='*60}\n# TASK LOG — Lịch sử công việc\n{'='*60}\n\n{content}\n")
        print(f"  📋 Task log: {task_log.name} ({len(content)} bytes)")

    # 2. Session saves
    session_dir = Path(config["paths"]["session_saves_dir"])
    if session_dir.exists():
        for session_file in sorted(session_dir.glob("SESSION-*.md")):
            content = session_file.read_text(encoding="utf-8", errors="replace")
            parts.append(f"\n{'='*60}\n# SESSION: {session_file.name}\n{'='*60}\n\n{content}\n")
            print(f"  📝 Session: {session_file.name} ({len(content)} bytes)")

    # 3. Lessons learned
    lessons = Path(config["paths"]["lessons_learned"])
    if lessons.exists():
        content = lessons.read_text(encoding="utf-8", errors="replace")
        parts.append(f"\n{'='*60}\n# LESSONS LEARNED — Bài học kinh nghiệm\n{'='*60}\n\n{content}\n")
        print(f"  📖 Lessons: {lessons.name} ({len(content)} bytes)")

    # 4. Patterns
    patterns_dir = Path(config["paths"]["patterns_dir"])
    if patterns_dir.exists():
        for pattern_file in sorted(patterns_dir.glob("*.yaml")):
            content = pattern_file.read_text(encoding="utf-8", errors="replace")
            parts.append(f"\n{'='*60}\n# PATTERN: {pattern_file.name}\n{'='*60}\n\n{content}\n")
            print(f"  🔄 Pattern: {pattern_file.name} ({len(content)} bytes)")

    # Lưu memory bundle
    bundles = []
    if parts:
        bundle_path = collected_dir / "memory-bundle.md"
        bundle_path.write_text(header + "\n".join(parts), encoding="utf-8")
        bundles.append(bundle_path)
        total_size = sum(len(p.encode("utf-8")) for p in parts)
        print(f"\n  ✅ Memory bundle: {total_size // 1024} KB → {bundle_path.name}\n")
    else:
        print("  ⚠️ Không tìm thấy data nào để gộp\n")

    return bundles


def collect_all() -> dict[str, list[Path]]:
    """Thu thập tất cả: skills + memory."""
    config = load_config()
    print(f"\n  {'='*50}")
    print(f"  🧠 {BRAND} — NotebookLM Second Brain Collector")
    print(f"  {'='*50}")

    skill_bundles = collect_skills(config)
    memory_bundles = collect_memory(config)

    return {
        "skills": skill_bundles,
        "memory": memory_bundles,
    }


if __name__ == "__main__":
    result = collect_all()
    total = len(result["skills"]) + len(result["memory"])
    print(f"  📊 Tổng kết: {total} bundle(s) sẵn sàng upload")
    print(f"     Skills: {len(result['skills'])} bundle(s)")
    print(f"     Memory: {len(result['memory'])} bundle(s)")
