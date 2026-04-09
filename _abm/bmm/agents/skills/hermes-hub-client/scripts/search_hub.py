#!/usr/bin/env python3
"""
Hermes Hub Client — Search Skills từ Open-Source Ecosystem
Tìm kiếm skills từ: skills.sh, GitHub taps, well-known endpoints

Usage:
  python search_hub.py --query "kubernetes"
  python search_hub.py --query "react" --source skills-sh
  python search_hub.py --inspect "openai/skills/k8s"
  python search_hub.py --compare "skill-name" --manifest path/to/manifest.csv
"""

import argparse
import json
import sys
import csv
from pathlib import Path

import urllib.request
import urllib.parse
import urllib.error
import ssl

# SSL context for HTTPS
_SSL_CTX = ssl.create_default_context()


def _http_get(url: str, headers: dict = None, timeout: int = 15) -> tuple[int, str]:
    """Simple HTTP GET using urllib (stdlib). Returns (status_code, body)."""
    req = urllib.request.Request(url)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except (urllib.error.URLError, OSError) as e:
        return 0, str(e)


# --- Sources Registry ---

GITHUB_TAPS = [
    {"owner": "openai", "repo": "skills", "label": "OpenAI Official"},
    {"owner": "anthropics", "repo": "skills", "label": "Anthropic Official"},
    {"owner": "VoltAgent", "repo": "awesome-agent-skills", "label": "VoltAgent Community"},
    {"owner": "garrytan", "repo": "gstack", "label": "Garry Tan Stack"},
    {"owner": "NousResearch", "repo": "hermes-agent", "path": "skills", "label": "Hermes Bundled"},
    {"owner": "NousResearch", "repo": "hermes-agent", "path": "optional-skills", "label": "Hermes Optional"},
]

SKILLS_SH_API = "https://skills.sh/api/search"
WELL_KNOWN_ENDPOINTS = [
    "https://mintlify.com/docs/.well-known/skills/index.json",
    "https://docs.stripe.com/.well-known/skills/index.json",
]


def search_github_tap(query: str, tap: dict) -> list:
    """Search a GitHub repo for SKILL.md files matching query."""
    results = []
    owner = tap["owner"]
    repo = tap["repo"]
    path = tap.get("path", "")

    q = urllib.parse.quote(f"{query} filename:SKILL.md repo:{owner}/{repo}" + (f" path:{path}" if path else ""))
    search_url = f"https://api.github.com/search/code?q={q}"

    status, body = _http_get(search_url, headers={"Accept": "application/vnd.github.v3+json"})

    if status == 200 and body:
        try:
            data = json.loads(body)
            for item in data.get("items", [])[:10]:
                skill_path = item.get("path", "")
                skill_name = Path(skill_path).parent.name
                results.append({
                    "name": skill_name,
                    "source": f"github:{owner}/{repo}",
                    "path": skill_path,
                    "url": item.get("html_url", ""),
                    "tap_label": tap["label"],
                    "score": item.get("score", 0),
                })
        except json.JSONDecodeError:
            pass
    elif status == 403:
        print(f"  ⚠️  GitHub API rate limit — thử lại sau hoặc set GITHUB_TOKEN", file=sys.stderr)
    elif status == 0:
        print(f"  ⚠️  Lỗi kết nối {owner}/{repo}: {body}", file=sys.stderr)

    return results


def search_skills_sh(query: str) -> list:
    """Search skills.sh directory."""
    results = []
    q = urllib.parse.quote(query)
    status, body = _http_get(f"{SKILLS_SH_API}?q={q}", timeout=10)
    if status == 200 and body:
        try:
            data = json.loads(body)
            for item in (data if isinstance(data, list) else data.get("results", [])):
                results.append({
                    "name": item.get("name", item.get("slug", "unknown")),
                    "description": item.get("description", ""),
                    "source": "skills-sh",
                    "url": item.get("url", ""),
                    "author": item.get("author", ""),
                })
        except json.JSONDecodeError:
            pass
    elif status == 0:
        print(f"  ⚠️  skills.sh không phản hồi", file=sys.stderr)
    return results


def search_well_known(query: str) -> list:
    """Search well-known skill endpoints."""
    results = []
    for endpoint in WELL_KNOWN_ENDPOINTS:
        status, body = _http_get(endpoint, timeout=10)
        if status == 200 and body:
            try:
                data = json.loads(body)
                skills = data if isinstance(data, list) else data.get("skills", [])
                for skill in skills:
                    name = skill.get("name", "")
                    desc = skill.get("description", "")
                    if query.lower() in name.lower() or query.lower() in desc.lower():
                        results.append({
                            "name": name,
                            "description": desc,
                            "source": f"well-known:{endpoint.split('//')[1].split('/')[0]}",
                            "url": skill.get("url", endpoint),
                        })
            except json.JSONDecodeError:
                continue
    return results


def inspect_skill(skill_ref: str) -> dict:
    """Inspect a skill from GitHub by reference (owner/repo/path or owner/repo)."""
    parts = skill_ref.split("/")
    if len(parts) < 2:
        return {"error": f"Invalid skill reference: {skill_ref}. Use owner/repo/path"}

    owner = parts[0]
    repo = parts[1]
    path = "/".join(parts[2:]) if len(parts) > 2 else ""
    skill_md_path = f"{path}/SKILL.md" if path else "SKILL.md"

    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{skill_md_path}"
    status, body = _http_get(url)
    if status == 200 and body:
        return {
            "name": parts[-1] if path else repo,
            "source": f"github:{owner}/{repo}",
            "path": skill_md_path,
            "content": body,
            "content_length": len(body),
            "lines": body.count("\n"),
        }
    elif status == 0:
        return {"error": f"Lỗi kết nối: {body}"}
    else:
        return {"error": f"Không tìm thấy SKILL.md tại {url} (HTTP {status})"}


def compare_with_manifest(skill_name: str, manifest_path: str) -> dict:
    """Check if a skill name conflicts with existing ABM skills."""
    conflicts = []
    try:
        with open(manifest_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing = row.get("name", row.get("skill_name", "")).strip()
                if not existing:
                    continue
                # Exact match
                if existing.lower() == skill_name.lower():
                    conflicts.append({"name": existing, "type": "exact_match"})
                # Partial match
                elif skill_name.lower() in existing.lower() or existing.lower() in skill_name.lower():
                    conflicts.append({"name": existing, "type": "partial_match"})
    except FileNotFoundError:
        return {"error": f"Manifest không tồn tại: {manifest_path}"}

    return {
        "skill_name": skill_name,
        "has_conflicts": len(conflicts) > 0,
        "conflicts": conflicts,
        "recommendation": "REJECT — skill trùng tên" if any(c["type"] == "exact_match" for c in conflicts)
                          else "REVIEW — có tên gần giống" if conflicts
                          else "OK — không trùng",
    }


def main():
    parser = argparse.ArgumentParser(description="Hermes Hub Client — Search Skills")
    parser.add_argument("--query", "-q", help="Từ khóa tìm kiếm")
    parser.add_argument("--source", "-s", choices=["github", "skills-sh", "well-known", "all"],
                        default="all", help="Nguồn tìm kiếm")
    parser.add_argument("--tap", help="GitHub tap cụ thể (owner/repo)")
    parser.add_argument("--inspect", "-i", help="Xem chi tiết skill (owner/repo/path)")
    parser.add_argument("--compare", "-c", help="So sánh skill với ABM manifest")
    parser.add_argument("--manifest", "-m", default="_abm/_config/skill-manifest.csv",
                        help="Đường dẫn tới skill-manifest.csv")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    parser.add_argument("--dry-run", action="store_true", help="Chạy test không kết nối thật")

    args = parser.parse_args()

    if args.dry_run:
        print("🔍 [DRY RUN] Hermes Hub Client")
        print(f"   Query: {args.query or 'N/A'}")
        print(f"   Source: {args.source}")
        print(f"   Manifest: {args.manifest}")
        print("   ✅ Cấu hình hợp lệ — sẵn sàng search khi bỏ --dry-run")
        return

    # --- Inspect mode ---
    if args.inspect:
        result = inspect_skill(args.inspect)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                print(f"📋 Skill: {result['name']}")
                print(f"   Source: {result['source']}")
                print(f"   Lines: {result['lines']}")
                print(f"   Size: {result['content_length']} bytes")
                print(f"\n{'='*60}")
                lines = result["content"].split("\n")[:50]
                print("\n".join(lines))
                if result["lines"] > 50:
                    print(f"\n... ({result['lines'] - 50} dòng còn lại)")
        return

    # --- Compare mode ---
    if args.compare:
        result = compare_with_manifest(args.compare, args.manifest)
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                icon = "🔴" if result["has_conflicts"] else "✅"
                print(f"{icon} {result['recommendation']}")
                for c in result["conflicts"]:
                    print(f"   ⚠️  Trùng với: {c['name']} ({c['type']})")
        return

    # --- Search mode ---
    if not args.query:
        parser.error("Cần --query hoặc --inspect hoặc --compare")

    all_results = []

    if args.source in ("github", "all"):
        print(f"🔍 Searching GitHub taps for '{args.query}'...")
        if args.tap:
            parts = args.tap.split("/")
            custom_tap = {"owner": parts[0], "repo": parts[1], "label": f"Custom: {args.tap}"}
            results = search_github_tap(args.query, custom_tap)
            all_results.extend(results)
        else:
            for tap in GITHUB_TAPS:
                results = search_github_tap(args.query, tap)
                all_results.extend(results)
                if results:
                    print(f"   ✅ {tap['label']}: {len(results)} kết quả")

    if args.source in ("skills-sh", "all"):
        print(f"🔍 Searching skills.sh for '{args.query}'...")
        results = search_skills_sh(args.query)
        all_results.extend(results)
        if results:
            print(f"   ✅ skills.sh: {len(results)} kết quả")

    if args.source in ("well-known", "all"):
        print(f"🔍 Searching well-known endpoints for '{args.query}'...")
        results = search_well_known(args.query)
        all_results.extend(results)
        if results:
            print(f"   ✅ well-known: {len(results)} kết quả")

    # Output
    if args.json:
        print(json.dumps(all_results, indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*60}")
        print(f"📊 Tổng: {len(all_results)} skills tìm thấy cho '{args.query}'")
        print(f"{'='*60}")
        for i, r in enumerate(all_results[:20], 1):
            name = r.get("name", "unknown")
            source = r.get("source", "")
            desc = r.get("description", r.get("tap_label", ""))
            url = r.get("url", "")
            print(f"\n  {i}. {name}")
            print(f"     Source: {source}")
            if desc:
                print(f"     Mô tả: {desc[:80]}")
            if url:
                print(f"     URL: {url}")

        if len(all_results) > 20:
            print(f"\n  ... và {len(all_results) - 20} kết quả khác (dùng --json để xem hết)")


if __name__ == "__main__":
    main()
