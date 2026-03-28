---
description: Chuyển đổi Markdown sang EPUB ebook chuyên nghiệp
---

Workflow chuyển đổi Markdown thành EPUB3 ebook files chuyên nghiệp.

---

## Quick Start

```bash
# Install dependencies
pip install -r D:\Antigravity\Skill\claude-skills\epub-converter\markdown-to-epub\requirements.txt
```

```python
from markdown_to_epub.scripts.epub_generator import create_epub_from_markdown

create_epub_from_markdown(
    markdown_content,
    output_path="output.epub",
    title="My Book",
    author="Author Name"
)
```

---

## Project Structure

```
markdown-to-epub/
├── SKILL.md                    # Skill definition
├── requirements.txt            # ebooklib, markdown2
├── scripts/
│   ├── markdown_processor.py   # Markdown parsing
│   └── epub_generator.py       # EPUB creation
```

---

## Workflow

1. **Prepare Markdown**: Đảm bảo markdown có structure tốt (headings, paragraphs)

2. **Convert**:
```python
from markdown_to_epub.scripts.epub_generator import create_epub_from_markdown

with open("input.md", "r") as f:
    content = f.read()

create_epub_from_markdown(
    content,
    output_path="book.epub",
    title="Book Title",
    author="Author Name"
)
```

3. **Test**: Mở file EPUB trong reader (Apple Books, Calibre)

---

## Supported Features

- Headings (H1-H6)
- Paragraphs and line breaks
- Bold, italic, strikethrough
- Links and images
- Code blocks
- Lists (ordered/unordered)
- Blockquotes
- Tables

---

## Testing

```bash
# Run test suite
python D:\Antigravity\Skill\claude-skills\epub-converter\test_epub_skill.py

# Manual test
python -c "
from markdown_to_epub.scripts.epub_generator import create_epub_from_markdown
create_epub_from_markdown('# Test\n\nContent', 'test.epub', 'Test', 'Author')
"
```

---

## Best Practices

- **Headings**: Dùng H1 cho title, H2 cho chapters
- **Metadata**: Luôn cung cấp title, author, language
- **Images**: Dùng relative paths
- **Test**: Verify trong nhiều EPUB readers

---

## Resources

// turbo
- Full skill: `D:\Antigravity\Skill\claude-skills\epub-converter\markdown-to-epub\SKILL.md`
- EPUB 3 Standard: https://www.w3.org/publishing/epub32/
