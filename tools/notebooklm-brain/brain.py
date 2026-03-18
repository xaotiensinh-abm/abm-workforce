"""
ABM - DũngTQ | NotebookLM Second Brain — CLI
=============================================
Entry point duy nhất cho tất cả chức năng.

Cách dùng:
    python brain.py collect              Thu thập skills + memory thành bundles
    python brain.py upload               Tạo notebooks + upload bundles
    python brain.py ask "câu hỏi"        Hỏi skill routing (tự detect)
    python brain.py skill "mô tả task"   Hỏi skill routing (chỉ Knowledge)
    python brain.py memory "câu hỏi"     Hỏi lịch sử (chỉ Memory)
    python brain.py status               Hiện trạng thái notebooks
    python brain.py refresh              Thu thập lại + upload mới
"""

import sys
from pathlib import Path

BRAND = "ABM - DũngTQ"


def print_banner():
    print(f"""
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║   🧠  {BRAND}  —  NotebookLM Second Brain     ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
""")


def print_help():
    print_banner()
    print("  LỆNH:")
    print("  ─────────────────────────────────────────────────")
    print("  collect              Thu thập skills + memory → bundles")
    print("  upload               Tạo notebooks + upload lên NotebookLM")
    print("  ask    \"câu hỏi\"     Hỏi brain (tự detect Knowledge/Memory)")
    print("  skill  \"mô tả\"      Hỏi skill nào phù hợp cho task")
    print("  memory \"câu hỏi\"    Tìm trong lịch sử task/session")
    print("  status               Trạng thái notebooks")
    print("  refresh              Collect lại + upload cập nhật")
    print("  ─────────────────────────────────────────────────")
    print()
    print("  VÍ DỤ:")
    print('  python brain.py ask "tôi cần viết email cho khách hàng mới"')
    print('  python brain.py skill "tạo landing page cho sản phẩm"')
    print('  python brain.py memory "task nào đã làm tuần trước?"')
    print()


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    args = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""

    if command in ("help", "--help", "-h"):
        print_help()

    elif command == "collect":
        from collector import collect_all
        collect_all()

    elif command == "upload":
        from uploader import upload_all
        upload_all()

    elif command == "ask":
        if not args:
            print("  ❌ Cần câu hỏi. Ví dụ: python brain.py ask \"câu hỏi\"")
            return
        from query import ask_brain
        answer = ask_brain(args)
        print(f"\n  💡 Trả lời:\n{answer}\n")

    elif command == "skill":
        if not args:
            print("  ❌ Cần mô tả task. Ví dụ: python brain.py skill \"viết email marketing\"")
            return
        from query import skill_lookup
        answer = skill_lookup(args)
        print(f"\n  💡 Skills đề xuất:\n{answer}\n")

    elif command == "memory":
        if not args:
            print("  ❌ Cần câu hỏi. Ví dụ: python brain.py memory \"task nào đã làm?\"")
            return
        from query import memory_search
        answer = memory_search(args)
        print(f"\n  💡 Memory:\n{answer}\n")

    elif command == "status":
        from query import show_status
        show_status()

    elif command == "refresh":
        print_banner()
        print("  🔄 Refreshing — Thu thập lại + Upload cập nhật...\n")
        from collector import collect_all
        collect_all()

        # Reset notebook IDs để tạo mới
        import yaml
        config_path = Path(__file__).parent / "config.yaml"
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        config["notebooks"]["knowledge"]["id"] = None
        config["notebooks"]["memory"]["id"] = None
        with open(config_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        from uploader import upload_all
        upload_all()
        print("  ✅ Refresh hoàn tất!\n")

    else:
        print(f"  ❌ Lệnh không hợp lệ: {command}")
        print("  Chạy: python brain.py help")


if __name__ == "__main__":
    main()
