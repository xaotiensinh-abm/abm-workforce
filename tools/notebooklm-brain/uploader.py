"""
ABM - DũngTQ | NotebookLM Second Brain — Uploader
==================================================
Tạo notebooks trên Google NotebookLM và upload collected bundles làm sources.
"""

import asyncio
import sys
import yaml
from pathlib import Path

BRAND = "ABM - DũngTQ"
SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_config(config: dict):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


async def create_and_upload(notebook_name: str, description: str, bundle_files: list[Path]) -> str:
    """Tạo notebook mới và upload bundle files làm sources."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        # Tạo notebook
        print(f"  📓 Tạo notebook: {notebook_name}...")
        nb = await client.notebooks.create(notebook_name)
        notebook_id = nb.id
        print(f"  ✅ Notebook ID: {notebook_id}")

        # Upload từng bundle file
        for bundle_file in bundle_files:
            if not bundle_file.exists():
                print(f"  ⚠️ File không tồn tại: {bundle_file}")
                continue

            print(f"  📤 Upload: {bundle_file.name} ({bundle_file.stat().st_size // 1024} KB)...")
            try:
                content = bundle_file.read_text(encoding="utf-8")
                source_title = bundle_file.stem

                # API signature: add_text(notebook_id, title, content, wait=True)
                await client.sources.add_text(
                    notebook_id,
                    source_title,
                    content,
                    wait=True
                )
                print(f"  ✅ Upload thành công: {source_title}")
            except Exception as e:
                # Fallback: thử add_file
                try:
                    await client.sources.add_file(notebook_id, str(bundle_file), wait=True)
                    print(f"  ✅ Upload thành công (file): {bundle_file.name}")
                except Exception as e2:
                    print(f"  ❌ Lỗi upload: {e} / fallback: {e2}")

        return notebook_id


def upload_knowledge(config: dict) -> str | None:
    """Tạo Knowledge Notebook và upload skill bundles."""
    collected_dir = SCRIPT_DIR / config["paths"]["collected_dir"]
    bundles = sorted(collected_dir.glob("skills-bundle-*.md"))

    if not bundles:
        print("  ❌ Không tìm thấy skill bundles. Chạy `python brain.py collect` trước.")
        return None

    nb_config = config["notebooks"]["knowledge"]
    notebook_id = asyncio.run(
        create_and_upload(nb_config["name"], nb_config["description"], bundles)
    )
    return notebook_id


def upload_memory(config: dict) -> str | None:
    """Tạo Memory Notebook và upload memory bundles."""
    collected_dir = SCRIPT_DIR / config["paths"]["collected_dir"]
    bundles = sorted(collected_dir.glob("memory-bundle*.md"))

    if not bundles:
        print("  ❌ Không tìm thấy memory bundles. Chạy `python brain.py collect` trước.")
        return None

    nb_config = config["notebooks"]["memory"]
    notebook_id = asyncio.run(
        create_and_upload(nb_config["name"], nb_config["description"], bundles)
    )
    return notebook_id


def upload_all():
    """Upload tất cả bundles lên NotebookLM."""
    config = load_config()

    print(f"\n  {'='*50}")
    print(f"  🚀 {BRAND} — NotebookLM Second Brain Uploader")
    print(f"  {'='*50}\n")

    # Upload Knowledge
    print(f"  {'─'*40}")
    print(f"  📚 KNOWLEDGE NOTEBOOK")
    print(f"  {'─'*40}")

    existing_knowledge_id = config["notebooks"]["knowledge"].get("id")
    if existing_knowledge_id:
        print(f"  ℹ️ Notebook đã tồn tại: {existing_knowledge_id}")
        print(f"  ℹ️ Bỏ qua. Xoá ID trong config.yaml để tạo mới.")
    else:
        knowledge_id = upload_knowledge(config)
        if knowledge_id:
            config["notebooks"]["knowledge"]["id"] = knowledge_id
            save_config(config)
            print(f"  💾 Đã lưu Knowledge ID vào config.yaml\n")

    # Upload Memory
    print(f"  {'─'*40}")
    print(f"  🧠 MEMORY NOTEBOOK")
    print(f"  {'─'*40}")

    existing_memory_id = config["notebooks"]["memory"].get("id")
    if existing_memory_id:
        print(f"  ℹ️ Notebook đã tồn tại: {existing_memory_id}")
        print(f"  ℹ️ Bỏ qua. Xoá ID trong config.yaml để tạo mới.")
    else:
        memory_id = upload_memory(config)
        if memory_id:
            config["notebooks"]["memory"]["id"] = memory_id
            save_config(config)
            print(f"  💾 Đã lưu Memory ID vào config.yaml\n")

    # Reload config để show kết quả
    config = load_config()
    print(f"\n  {'='*50}")
    print(f"  📊 KẾT QUẢ")
    print(f"  {'='*50}")
    print(f"  Knowledge: {config['notebooks']['knowledge'].get('id', '❌ chưa tạo')}")
    print(f"  Memory   : {config['notebooks']['memory'].get('id', '❌ chưa tạo')}")
    print()


if __name__ == "__main__":
    upload_all()
