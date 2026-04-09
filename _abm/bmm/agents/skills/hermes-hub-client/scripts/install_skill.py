#!/usr/bin/env python3
"""
Install Skill — Download, Convert, và Import từ Hermes Hub vào ABM-Workforce

Workflow:
  1. Download SKILL.md từ source (GitHub/URL)
  2. Convert Hermes → ABM format (via format_adapter)
  3. Đặt vào quarantine directory
  4. CEO approve → di chuyển vào skills/ chính thức
  5. Đăng ký vào skill-manifest.csv

Usage:
  python install_skill.py --source "github:openai/skills/k8s" --quarantine
  python install_skill.py --approve "k8s"
  python install_skill.py --reject "k8s" --reason "trùng skill"
  python install_skill.py --list-quarantine
"""

import argparse
import csv
import json
import shutil
import sys
from datetime import date
from pathlib import Path

import urllib.request
import urllib.error
import ssl

_SSL_CTX = ssl.create_default_context()

# Import format_adapter from same directory
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
from format_adapter import convert_hermes_to_abm

# --- Paths ---
ABM_ROOT = Path(__file__).parent.parent.parent.parent.parent  # _abm/bmm/agents/skills/hermes-hub-client/scripts → root
SKILLS_DIR = ABM_ROOT / "_abm" / "bmm" / "agents" / "skills"
QUARANTINE_DIR = SKILLS_DIR / "_quarantine"
MANIFEST_PATH = ABM_ROOT / "_abm" / "_config" / "skill-manifest.csv"


def resolve_abm_root():
    """Try to find ABM root dynamically."""
    # Walk up to find _abm directory
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / "_abm").is_dir():
            return current
        current = current.parent
    return ABM_ROOT


def download_skill(source: str) -> tuple:
    """Download SKILL.md from a source reference.

    Returns (content, skill_name)
    """
    if source.startswith("github:"):
        # github:owner/repo/path
        ref = source[7:]
        parts = ref.split("/")
        if len(parts) < 2:
            raise ValueError(f"Invalid GitHub reference: {ref}. Use owner/repo/path")

        owner = parts[0]
        repo = parts[1]
        path = "/".join(parts[2:]) if len(parts) > 2 else ""
        skill_name = parts[-1] if path else repo

        # Try SKILL.md at path
        skill_md_path = f"{path}/SKILL.md" if path else "SKILL.md"
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{skill_md_path}"

        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
                return resp.read().decode("utf-8"), skill_name
        except urllib.error.HTTPError as e:
            raise FileNotFoundError(f"Không tìm thấy SKILL.md tại {url} (HTTP {e.code})")
        except urllib.error.URLError as e:
            raise ConnectionError(f"Lỗi kết nối: {e}")

    elif source.startswith("url:"):
        # Direct URL
        url = source[4:]
        skill_name = Path(url).parent.name or "imported-skill"
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
                return resp.read().decode("utf-8"), skill_name
        except urllib.error.HTTPError as e:
            raise FileNotFoundError(f"HTTP {e.code}: {url}")

    elif source.startswith("file:"):
        # Local file
        file_path = Path(source[5:])
        if not file_path.exists():
            raise FileNotFoundError(f"File không tồn tại: {file_path}")
        skill_name = file_path.parent.name
        return file_path.read_text(encoding="utf-8"), skill_name

    else:
        raise ValueError(f"Unsupported source type: {source}. Use github:, url:, or file:")


def install_to_quarantine(source: str, skill_name: str = None, dry_run: bool = False) -> dict:
    """Download, convert, and install to quarantine."""

    print(f"📥 Downloading từ {source}...")
    content, auto_name = download_skill(source)
    name = skill_name or auto_name

    print(f"🔄 Converting {name} → ABM format...")
    abm_content = convert_hermes_to_abm(content, source=source)

    # Create quarantine directory
    root = resolve_abm_root()
    quarantine = root / "_abm" / "bmm" / "agents" / "skills" / "_quarantine"
    skill_dir = quarantine / name
    skill_file = skill_dir / "SKILL.md"

    if dry_run:
        print(f"\n🔍 [DRY RUN] Would install to: {skill_dir}")
        print(f"{'='*60}")
        print(abm_content[:500])
        if len(abm_content) > 500:
            print(f"... ({len(abm_content) - 500} bytes more)")
        return {"status": "dry_run", "name": name, "path": str(skill_dir)}

    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(abm_content, encoding="utf-8")

    # Save original for reference
    (skill_dir / "ORIGINAL_HERMES.md").write_text(content, encoding="utf-8")

    # Save metadata
    meta = {
        "name": name,
        "source": source,
        "imported_date": date.today().isoformat(),
        "status": "quarantine",
        "original_format": "hermes",
        "converted_format": "abm",
    }
    (skill_dir / "import_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"✅ Installed to quarantine: {skill_dir}")
    print(f"   📋 SKILL.md: {len(abm_content)} bytes")
    print(f"   📋 ORIGINAL_HERMES.md: {len(content)} bytes")
    print(f"   📋 import_meta.json")
    print(f"\n   Tiếp theo: python install_skill.py --approve '{name}'")

    return {"status": "quarantine", "name": name, "path": str(skill_dir)}


def approve_skill(skill_name: str) -> dict:
    """Move skill from quarantine to active skills directory."""
    root = resolve_abm_root()
    quarantine_path = root / "_abm" / "bmm" / "agents" / "skills" / "_quarantine" / skill_name
    target_path = root / "_abm" / "bmm" / "agents" / "skills" / skill_name

    if not quarantine_path.exists():
        return {"error": f"Skill '{skill_name}' không có trong quarantine"}

    if target_path.exists():
        return {"error": f"Skill '{skill_name}' đã tồn tại trong skills directory. Dùng tên khác."}

    # Move to active
    shutil.move(str(quarantine_path), str(target_path))

    # Update metadata
    meta_file = target_path / "import_meta.json"
    if meta_file.exists():
        meta = json.loads(meta_file.read_text())
        meta["status"] = "approved"
        meta["approved_date"] = date.today().isoformat()
        meta_file.write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    # Remove quarantine warning from SKILL.md
    skill_file = target_path / "SKILL.md"
    if skill_file.exists():
        content = skill_file.read_text()
        content = content.replace(
            "> ⚠️ **IMPORTED FROM HERMES HUB**",
            "> ✅ **IMPORTED FROM HERMES HUB** (CEO Approved)"
        )
        skill_file.write_text(content)

    # Register in manifest
    manifest = root / "_abm" / "_config" / "skill-manifest.csv"
    if manifest.exists():
        with open(manifest, "a", encoding="utf-8") as f:
            f.write(f"\n{skill_name},Hermes Hub Import,1.0.0,{date.today().isoformat()}")

    print(f"✅ Skill '{skill_name}' approved và activated!")
    print(f"   📁 Path: {target_path}")
    print(f"   📋 Đã đăng ký vào skill-manifest.csv")

    return {"status": "approved", "name": skill_name, "path": str(target_path)}


def reject_skill(skill_name: str, reason: str = "") -> dict:
    """Remove skill from quarantine."""
    root = resolve_abm_root()
    quarantine_path = root / "_abm" / "bmm" / "agents" / "skills" / "_quarantine" / skill_name

    if not quarantine_path.exists():
        return {"error": f"Skill '{skill_name}' không có trong quarantine"}

    shutil.rmtree(quarantine_path)
    print(f"❌ Skill '{skill_name}' rejected và xóa khỏi quarantine")
    if reason:
        print(f"   Lý do: {reason}")

    return {"status": "rejected", "name": skill_name, "reason": reason}


def list_quarantine() -> list:
    """List all skills in quarantine."""
    root = resolve_abm_root()
    quarantine = root / "_abm" / "bmm" / "agents" / "skills" / "_quarantine"

    if not quarantine.exists():
        print("📋 Quarantine trống — không có skill nào đang chờ review")
        return []

    skills = []
    for skill_dir in sorted(quarantine.iterdir()):
        if skill_dir.is_dir() and not skill_dir.name.startswith("."):
            meta_file = skill_dir / "import_meta.json"
            meta = {}
            if meta_file.exists():
                meta = json.loads(meta_file.read_text())

            skills.append({
                "name": skill_dir.name,
                "source": meta.get("source", "unknown"),
                "imported_date": meta.get("imported_date", "unknown"),
                "status": meta.get("status", "quarantine"),
            })

    if skills:
        print(f"📋 Quarantine: {len(skills)} skill(s) đang chờ review")
        for s in skills:
            print(f"   📦 {s['name']} — từ {s['source']} ({s['imported_date']})")
    else:
        print("📋 Quarantine trống")

    return skills


def main():
    parser = argparse.ArgumentParser(description="Install Hermes Skills → ABM-Workforce")
    parser.add_argument("--source", "-s", help="Source reference (github:owner/repo/path, url:..., file:...)")
    parser.add_argument("--name", "-n", help="Override skill name")
    parser.add_argument("--quarantine", "-q", action="store_true", help="Install to quarantine (default)")
    parser.add_argument("--approve", "-a", help="Approve skill from quarantine")
    parser.add_argument("--reject", "-r", help="Reject skill from quarantine")
    parser.add_argument("--reason", help="Reason for rejection")
    parser.add_argument("--list-quarantine", "-l", action="store_true", help="List quarantine skills")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")

    args = parser.parse_args()

    if args.list_quarantine:
        list_quarantine()
    elif args.approve:
        result = approve_skill(args.approve)
        if "error" in result:
            print(f"❌ {result['error']}")
            sys.exit(1)
    elif args.reject:
        reject_skill(args.reject, args.reason or "")
    elif args.source:
        install_to_quarantine(args.source, args.name, args.dry_run)
    else:
        parser.error("Cần --source, --approve, --reject, hoặc --list-quarantine")


if __name__ == "__main__":
    main()
