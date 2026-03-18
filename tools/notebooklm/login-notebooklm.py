"""
ABM - DũngTQ | Login NotebookLM (Workaround)
=============================================
Script đăng nhập Google cho notebooklm-py với timeout mở rộng (120s).
Dùng khi lệnh `notebooklm login` bị lỗi navigation timeout trên Windows.

Cách dùng:
    python login-notebooklm.py
"""

import sys
from pathlib import Path

BRAND = "ABM - DũngTQ"

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print(f"\n  ❌ [{BRAND}] Playwright chưa cài đặt.")
    print("  Chạy: pip install \"notebooklm-py[browser]\" && playwright install chromium\n")
    sys.exit(1)

NOTEBOOKLM_URL = "https://notebooklm.google.com/"
GOOGLE_ACCOUNTS_URL = "https://accounts.google.com/"

storage_path = Path.home() / ".notebooklm" / "storage_state.json"
browser_profile = Path.home() / ".notebooklm" / "browser_profile"

storage_path.parent.mkdir(parents=True, exist_ok=True)
browser_profile.mkdir(parents=True, exist_ok=True)

print(f"""
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║     🔐  {BRAND}  —  NotebookLM Login           ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
""")
print(f"  📁 Profile : {browser_profile}")
print(f"  📁 Auth    : {storage_path}")
print("  🌐 Mở trình duyệt Chromium...\n")

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=str(browser_profile),
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--password-store=basic",
        ],
        ignore_default_args=["--enable-automation"],
    )

    page = context.pages[0] if context.pages else context.new_page()
    page.goto(NOTEBOOKLM_URL, timeout=120000)

    print("  ┌─────────────────────────────────────────────┐")
    print("  │  HƯỚNG DẪN:                                 │")
    print("  │  1. Đăng nhập Google trên trình duyệt       │")
    print("  │  2. Đợi trang chủ NotebookLM xuất hiện      │")
    print("  │  3. Nhấn ENTER ở đây để lưu                 │")
    print("  └─────────────────────────────────────────────┘")
    print()

    input("  [Nhấn ENTER khi đã đăng nhập xong] ")

    print("\n  ⏳ Đang lưu cookie xác thực...")
    page.goto(GOOGLE_ACCOUNTS_URL, wait_until="load", timeout=60000)
    page.goto(NOTEBOOKLM_URL, wait_until="load", timeout=60000)

    context.storage_state(path=str(storage_path))
    context.close()

print(f"""
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║     ✅  ĐĂNG NHẬP THÀNH CÔNG  —  {BRAND}      ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝

  📁 Cookie đã lưu tại: {storage_path}

  Xác minh: notebooklm auth check --test
""")
