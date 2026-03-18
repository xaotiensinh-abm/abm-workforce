# 🧠 ABM - DũngTQ | NotebookLM Second Brain

> Biến Google NotebookLM thành **bộ não thứ 2** — skill routing thông minh + bộ nhớ dài hạn cho ABM Workforce.

## ⚡ Quick Start

```bash
# 1. Thu thập skills + session logs
python brain.py collect

# 2. Upload lên Google NotebookLM
python brain.py upload

# 3. Hỏi brain!
python brain.py ask "tôi cần viết email marketing cho khách hàng mới"
python brain.py memory "task nào đã hoàn thành tuần trước?"
```

## 📋 Yêu cầu

- Python >= 3.9
- `notebooklm-py[browser]` đã cài và đăng nhập (`notebooklm login`)
- `pyyaml` (`pip install pyyaml`)

## 🔧 Lệnh CLI

| Lệnh | Mô tả |
|---|---|
| `python brain.py collect` | Thu thập SKILL.md + session logs → bundles |
| `python brain.py upload` | Tạo notebooks NotebookLM + upload bundles |
| `python brain.py ask "..."` | Hỏi brain (tự chọn Knowledge/Memory) |
| `python brain.py skill "..."` | Hỏi skill routing (Knowledge Notebook) |
| `python brain.py memory "..."` | Tìm lịch sử (Memory Notebook) |
| `python brain.py status` | Trạng thái notebooks |
| `python brain.py refresh` | Collect lại + tạo notebooks mới |

## 📁 Cấu trúc

```
tools/notebooklm-brain/
├── brain.py           # CLI entry point
├── collector.py       # Thu thập và gộp files
├── uploader.py        # Tạo notebooks + upload
├── query.py           # Hỏi đáp skill routing + memory
├── config.yaml        # Cấu hình (notebook IDs tự động lưu)
├── README.md          # Tài liệu này
└── _collected/        # Bundles đã gộp (auto-generated)
    ├── skills-bundle-01.md
    ├── skills-bundle-02.md
    └── memory-bundle.md
```

## 🧠 Kiến trúc

```
┌─────────────────────────────────────────────────────┐
│                   brain.py (CLI)                     │
├─────────┬──────────────┬────────────┬───────────────┤
│ collect │    upload     │    ask     │    memory     │
│         │              │            │               │
│ ┌─────┐ │  ┌────────┐  │ ┌────────┐ │  ┌─────────┐  │
│ │79   │ │  │NotebookLM│ │ │Knowledge│ │  │Memory   │  │
│ │SKILLs│→│  │  API    │ │ │Notebook │ │  │Notebook │  │
│ │+logs│ │  │         │ │ │(skills) │ │  │(history)│  │
│ └─────┘ │  └────────┘  │ └────────┘ │  └─────────┘  │
└─────────┴──────────────┴────────────┴───────────────┘
```

## 🔍 Ví dụ sử dụng

### Skill Routing
```bash
$ python brain.py skill "tôi cần viết email cho khách hàng đang rời bỏ"

  🔍 [ABM - DũngTQ] Hỏi Knowledge Brain...
  📝 Task: tôi cần viết email cho khách hàng đang rời bỏ

  💡 Skills đề xuất:
  1. churn-prevention — chuyên xử lý khách hàng có nguy cơ rời bỏ
  2. email-marketing — viết email sequence giữ chân
  3. cold-email — kỹ thuật viết email cá nhân hóa cao
```

### Memory Search
```bash
$ python brain.py memory "task marketing nào đã làm gần đây?"

  🧠 [ABM - DũngTQ] Hỏi Memory Brain...
  📝 Câu hỏi: task marketing nào đã làm gần đây?

  💡 Memory:
  Theo lịch sử, có 2 task marketing đã hoàn thành:
  - TG-002-W1: Email sequence 4 bước giới thiệu sản phẩm mới
  - TG-005-W1: Content calendar tháng 4 — 30 posts Facebook + LinkedIn
```

---

<div align="center">

**ABM - DũngTQ** | Prototype v0.1 | Powered by [notebooklm-py](https://github.com/teng-lin/notebooklm-py)

</div>
