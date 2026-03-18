# 🤖 ABM - DũngTQ | NotebookLM-py Setup

> **Bộ cài đặt tự động** cho [notebooklm-py](https://github.com/teng-lin/notebooklm-py) — Unofficial Python API cho Google NotebookLM.

## 📋 Tổng quan

| Thành phần | Mô tả |
|---|---|
| `notebooklm-py` | Python API + CLI cho Google NotebookLM |
| Playwright Chromium | Browser engine để đăng nhập Google |
| Agent Skill | Tích hợp với Claude Code / AI agents |

### Tính năng chính

- 🎙️ **Tạo Podcast** — Audio Overview từ nguồn tài liệu
- 🎬 **Tạo Video** — Whiteboard, cinematic video
- 📝 **Quiz & Flashcards** — Bài kiểm tra, thẻ ghi nhớ
- 📊 **Slide Deck, Mind Map, Data Table** — Xuất nhiều định dạng
- 💬 **Hỏi đáp** — Chat trực tiếp với nguồn tài liệu
- 📥 **Tải về** — MP3, MP4, PDF, JSON, CSV, Markdown

---

## ⚡ Cài đặt nhanh (1 lệnh)

### Windows (PowerShell)

```powershell
.\setup-notebooklm.ps1
```

### Tùy chọn

```powershell
# Cài đặt không đăng nhập (đăng nhập sau)
.\setup-notebooklm.ps1 -SkipLogin

# Cài bản dev mới nhất từ GitHub
.\setup-notebooklm.ps1 -DevInstall

# Xem trợ giúp
.\setup-notebooklm.ps1 -Help
```

---

## 🔧 Cài đặt thủ công

Nếu script tự động không chạy được, làm theo các bước sau:

### Bước 1: Kiểm tra Python

```bash
python --version
# Yêu cầu: Python >= 3.9
```

Chưa có? Tải tại [python.org](https://www.python.org/downloads/) — **nhớ tick "Add Python to PATH"**.

### Bước 2: Cài thư viện

```bash
pip install "notebooklm-py[browser]"
```

### Bước 3: Cài Playwright Chromium

```bash
playwright install chromium
```

### Bước 4: Cài Agent Skill (tuỳ chọn)

```bash
notebooklm skill install
```

### Bước 5: Đăng nhập Google

```bash
# Cách 1: CLI (có thể bị timeout trên Windows)
notebooklm login

# Cách 2: Script workaround (khuyến nghị trên Windows)
python login-notebooklm.py
```

> ⚠️ **Lưu ý quan trọng**: Sau khi đăng nhập Google trên trình duyệt, **phải nhấn Enter trong terminal** để lưu cookie.

### Bước 6: Xác minh

```bash
notebooklm auth check --test
```

---

## 🚀 Sử dụng

### Lệnh CLI cơ bản

```bash
# Tạo notebook mới
notebooklm create "Nghiên cứu AI"

# Thêm nguồn
notebooklm source add "https://en.wikipedia.org/wiki/AI"
notebooklm source add "./tài-liệu.pdf"

# Hỏi đáp
notebooklm ask "Tóm tắt nội dung chính?"

# Tạo nội dung
notebooklm generate audio "tạo podcast hấp dẫn" --wait
notebooklm generate video --style whiteboard --wait
notebooklm generate quiz --difficulty hard
notebooklm generate slide-deck

# Tải về
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
```

### Python API

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with await NotebookLMClient.from_storage() as client:
        # Tạo notebook
        nb = await client.notebooks.create("Nghiên cứu")

        # Thêm nguồn
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Hỏi đáp
        result = await client.chat.ask(nb.id, "Tóm tắt nội dung")
        print(result.answer)

        # Tạo podcast
        status = await client.artifacts.generate_audio(nb.id, instructions="hấp dẫn")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

asyncio.run(main())
```

---

## 🔍 Xử lý sự cố

| Vấn đề | Giải pháp |
|---|---|
| `notebooklm login` timeout | Dùng `python login-notebooklm.py` (timeout 120s) |
| `playwright install` lỗi | Chạy PowerShell với quyền Admin |
| Cookie hết hạn | Chạy lại `notebooklm login` hoặc `python login-notebooklm.py` |
| Python không tìm thấy | Cài Python và thêm vào PATH |
| Permission denied | Chạy terminal với quyền Administrator |

---

## 📁 Cấu trúc file

```
tools/notebooklm/
├── README.md                  # Tài liệu này
├── setup-notebooklm.ps1      # Script cài đặt tự động (Windows)
└── login-notebooklm.py       # Script đăng nhập (workaround timeout)
```

---

## 📖 Tài liệu gốc

- [CLI Reference](https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md)
- [Python API](https://github.com/teng-lin/notebooklm-py/blob/main/docs/python-api.md)
- [Troubleshooting](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md)

---

<div align="center">

**ABM - DũngTQ** | Powered by [notebooklm-py](https://github.com/teng-lin/notebooklm-py)

</div>
