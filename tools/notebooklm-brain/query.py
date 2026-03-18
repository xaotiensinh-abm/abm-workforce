"""
ABM - DũngTQ | NotebookLM Second Brain — Query
===============================================
Hỏi đáp với Knowledge Notebook (skill routing) và Memory Notebook (history).
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


async def _ask_notebook(notebook_id: str, question: str) -> str:
    """Hỏi notebook và trả về câu trả lời."""
    from notebooklm import NotebookLMClient

    async with await NotebookLMClient.from_storage() as client:
        result = await client.chat.ask(notebook_id, question)
        return result.answer


def skill_lookup(task_description: str) -> str:
    """
    Hỏi Knowledge Notebook: task này cần dùng skill nào?
    
    Args:
        task_description: Mô tả task cần routing
    
    Returns:
        Câu trả lời từ notebook gợi ý skills phù hợp
    """
    config = load_config()
    notebook_id = config["notebooks"]["knowledge"].get("id")

    if not notebook_id:
        return "❌ Knowledge Notebook chưa được tạo. Chạy: python brain.py upload"

    prompt = (
        f"Dựa trên danh sách skills trong nguồn, hãy đề xuất TOP 3 skills phù hợp nhất cho task sau:\n\n"
        f"TASK: {task_description}\n\n"
        f"Trả lời theo format:\n"
        f"1. [tên-skill] — lý do\n"
        f"2. [tên-skill] — lý do\n"
        f"3. [tên-skill] — lý do\n\n"
        f"Chỉ chọn skills có trong nguồn. Ưu tiên skill phù hợp nhất."
    )

    print(f"\n  🔍 [{BRAND}] Hỏi Knowledge Brain...")
    print(f"  📝 Task: {task_description}\n")

    answer = asyncio.run(_ask_notebook(notebook_id, prompt))
    return answer


def memory_search(question: str) -> str:
    """
    Hỏi Memory Notebook: tìm thông tin từ lịch sử làm việc.
    
    Args:
        question: Câu hỏi về lịch sử task, session, patterns
    
    Returns:
        Câu trả lời từ notebook về lịch sử
    """
    config = load_config()
    notebook_id = config["notebooks"]["memory"].get("id")

    if not notebook_id:
        return "❌ Memory Notebook chưa được tạo. Chạy: python brain.py upload"

    prompt = (
        f"Dựa trên lịch sử task, session logs, và patterns trong nguồn, "
        f"hãy trả lời câu hỏi sau bằng tiếng Việt:\n\n"
        f"CÂU HỎI: {question}\n\n"
        f"Trả lời chi tiết, trích dẫn cụ thể từ nguồn nếu có."
    )

    print(f"\n  🧠 [{BRAND}] Hỏi Memory Brain...")
    print(f"  📝 Câu hỏi: {question}\n")

    answer = asyncio.run(_ask_notebook(notebook_id, prompt))
    return answer


def ask_brain(question: str, target: str = "auto") -> str:
    """
    Hỏi brain thông minh — tự detect hỏi Knowledge hay Memory.
    
    Args:
        question: Câu hỏi
        target: "knowledge", "memory", hoặc "auto" (tự detect)
    """
    if target == "knowledge":
        return skill_lookup(question)
    elif target == "memory":
        return memory_search(question)
    else:
        # Auto-detect: nếu hỏi về skill/task type → knowledge, còn lại → memory
        skill_keywords = ["skill", "dùng gì", "cần gì", "phù hợp", "routing", "task type", "công cụ"]
        is_skill_question = any(kw in question.lower() for kw in skill_keywords)
        
        if is_skill_question:
            return skill_lookup(question)
        else:
            return memory_search(question)


def show_status():
    """Hiện trạng thái notebooks."""
    config = load_config()

    print(f"\n  {'='*50}")
    print(f"  📊 {BRAND} — NotebookLM Second Brain Status")
    print(f"  {'='*50}\n")

    for name, nb in config["notebooks"].items():
        nb_id = nb.get("id")
        status = "✅ Online" if nb_id else "❌ Chưa tạo"
        print(f"  {nb['name']}:")
        print(f"    Trạng thái : {status}")
        print(f"    ID         : {nb_id or 'N/A'}")
        print(f"    Mô tả      : {nb['description']}")
        print()

    # Kiểm tra collected bundles
    collected_dir = SCRIPT_DIR / config["paths"]["collected_dir"]
    if collected_dir.exists():
        bundles = list(collected_dir.glob("*.md"))
        total_size = sum(b.stat().st_size for b in bundles)
        print(f"  📦 Collected bundles: {len(bundles)} file(s), {total_size // 1024} KB")
        for b in sorted(bundles):
            print(f"     → {b.name} ({b.stat().st_size // 1024} KB)")
    else:
        print(f"  📦 Collected bundles: chưa có (chạy `collect` trước)")

    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_status()
    else:
        question = " ".join(sys.argv[1:])
        answer = ask_brain(question)
        print(f"\n  💡 Trả lời:\n{answer}\n")
