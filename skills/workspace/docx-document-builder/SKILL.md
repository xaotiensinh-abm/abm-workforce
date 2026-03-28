---
name: docx-document-builder
description: Generate professional-grade Word DOCX files from Markdown using python-docx with full style control — cover pages, TOC, headers/footers, page numbers, styled tables, code blocks, Vietnamese-safe typography. Use when converting MD to DOCX, creating Word documents, building professional reports, or generating printable documentation.
---

# Goal

> **Use this skill when:** generating Word DOCX files from Markdown

Biến bất kỳ file Markdown nào thành tài liệu Word (DOCX) chất lượng **design-grade** — ngang hàng với output của MS Word Template — bằng cách dùng `python-docx` thao tác trực tiếp trên XML, không qua converter trung gian nào (không htmldocx, không Pandoc).

**Tại sao không dùng converter?** Vì:
- `htmldocx` → bảng biểu vỡ layout, code blocks mất format
- `pypandoc` → styling mặc định quá basic, không custom được
- `python-docx trực tiếp` → 100% control mọi pixel, font, border, spacing

---

# Instructions

## Bước 0: Phân Tích Đầu Vào

Trước khi viết code, **đọc file Markdown** và phân loại các element:

```
Markdown Element    → python-docx Method
────────────────────────────────────────
# H1               → doc.add_heading(level=1) + Cover Page title
## H2               → doc.add_heading(level=2) + Section Break
### H3              → doc.add_heading(level=3)
| table |           → doc.add_table() + custom styling
```code```          → 1-cell table with gray background
> blockquote        → paragraph with left-indent + blue left-border
- bullet            → List Bullet style
1. numbered         → List Number style
**bold** *italic*   → run-level formatting
`inline code`       → Consolas font + pink color
---                 → decorative divider line
```

## Bước 1: Tạo Document + Page Setup

```python
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

doc = Document()
section = doc.sections[0]
section.page_width = Cm(21)       # A4
section.page_height = Cm(29.7)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2)
```

## Bước 2: Thiết Lập Theme Config

**BẮT BUỘC** tách theme ra config dict để dễ thay đổi:

```python
THEME = {
    'primary':    RGBColor(0x1B, 0x2A, 0x4A),  # Navy
    'secondary':  RGBColor(0x2C, 0x3E, 0x6B),  # Dark Blue
    'accent':     RGBColor(0x34, 0x98, 0xDB),   # Accent Blue
    'text':       RGBColor(0x33, 0x33, 0x33),   # Dark Gray
    'muted':      RGBColor(0x66, 0x66, 0x66),   # Medium Gray
    'bg_code':    'F5F5F5',                      # Code block bg
    'bg_table_header': '1B2A4A',                 # Table header
    'bg_table_alt':    'F0F4FA',                 # Alternating rows
    'font_main':  'Arial',
    'font_code':  'Consolas',
    'font_size':  Pt(11),
    'code_size':  Pt(9),
}
```

> **Template khác:** Evernote green, Notion cream, hoặc company brand colors — chỉ cần đổi dict này.

## Bước 3: Custom Styles

```python
def setup_styles(doc, theme):
    styles = doc.styles
    # Normal
    normal = styles['Normal']
    normal.font.name = theme['font_main']
    normal.font.size = theme['font_size']
    normal.font.color.rgb = theme['text']
    normal.paragraph_format.line_spacing = 1.15

    # Headings — 3 levels with distinct colors
    heading_config = [
        (1, Pt(22), theme['primary'], True),    # H1: Navy, center
        (2, Pt(16), theme['secondary'], False),  # H2: Dark Blue
        (3, Pt(13), theme['accent'], False),     # H3: Accent
    ]
    for level, size, color, center in heading_config:
        h = styles[f'Heading {level}']
        h.font.name = theme['font_main']
        h.font.size = size
        h.font.color.rgb = color
        h.font.bold = True
        h.paragraph_format.space_before = Pt(18 if level <= 2 else 12)
        h.paragraph_format.space_after = Pt(8)
        # ★ CRITICAL: Set outline level for TOC + Navigation Pane
        h.paragraph_format.outline_level = level - 1
        if center:
            h.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
```

## Bước 4: Document Properties (Metadata)

```python
from docx.opc.constants import RELATIONSHIP_TYPE as RT

core = doc.core_properties
core.title = 'HƯỚNG DẪN SỬ DỤNG — ABM-WORKFORCE v3.0'
core.author = 'ABM-Workforce Team'
core.subject = 'User Guide'
core.keywords = 'ABM, AI, Multi-Agent, Workforce'
core.language = 'vi-VN'
```

## Bước 5: Cover Page (Trang Bìa Chuyên Nghiệp)

```python
def add_cover_page(doc, theme, title, subtitle, taglines):
    # ─── Accent bar (colored strip at top) ───
    bar_table = doc.add_table(rows=1, cols=1)
    bar_cell = bar_table.rows[0].cells[0]
    set_cell_shading(bar_cell, theme['bg_table_header'])
    bar_cell.text = ''
    # Set height to 1cm accent bar
    tr = bar_table.rows[0]._tr
    trPr = tr.get_or_add_trPr()
    trHeight = parse_xml(f'<w:trHeight {nsdecls("w")} w:val="567" w:hRule="exact"/>')
    trPr.append(trHeight)

    # Spacer
    for _ in range(3):
        doc.add_paragraph('')

    # Title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(36)
    run.font.color.rgb = theme['primary']
    run.font.name = theme['font_main']
    run.bold = True

    # Subtitle
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(subtitle)
    run.font.size = Pt(28)
    run.font.color.rgb = theme['accent']
    run.font.name = theme['font_main']
    run.bold = True

    # Divider
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('━' * 40)
    run.font.color.rgb = theme['accent']

    # Taglines
    for line in taglines:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(line)
        run.font.size = Pt(14)
        run.font.color.rgb = theme['muted']
        run.italic = True

    doc.add_page_break()
```

## Bước 6: Table of Contents (TOC) ★ CRITICAL

TOC trong python-docx phải dùng XML field code — Word sẽ auto-update khi mở:

```python
def add_toc(doc, theme):
    """Thêm Table of Contents tự động — Word sẽ populate khi mở file."""
    # TOC Title
    p = doc.add_heading('MỤC LỤC', level=1)

    # TOC Field
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run._r.append(fldChar1)

    run2 = paragraph.add_run()
    instrText = parse_xml(
        f'<w:instrText {nsdecls("w")} xml:space="preserve"> '
        f'TOC \\o "1-3" \\h \\z \\u </w:instrText>'
    )
    run2._r.append(instrText)

    run3 = paragraph.add_run()
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    run3._r.append(fldChar2)

    # Placeholder text (Word replaces this on open)
    run4 = paragraph.add_run('(Nhấn Ctrl+A → F9 để cập nhật Mục Lục)')
    run4.font.color.rgb = theme['muted']
    run4.font.size = Pt(10)
    run4.font.italic = True

    run5 = paragraph.add_run()
    fldChar3 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run5._r.append(fldChar3)

    doc.add_page_break()
```

> **Lưu ý:** Khi user mở file trong Word → Right-click TOC → "Update Field" → chọn "Update entire table" → TOC tự điền.

## Bước 7: Headers & Footers + Page Numbers ★ CRITICAL

```python
def add_header_footer(doc, theme, doc_title):
    """Thêm header (tiêu đề) + footer (page numbers) cho mọi section."""
    for section in doc.sections:
        # ─── Header ───
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = hp.add_run(doc_title)
        run.font.size = Pt(8)
        run.font.color.rgb = theme['muted']
        run.font.name = theme['font_main']
        run.italic = True

        # Thin line under header
        pPr = hp._p.get_or_add_pPr()
        pBdr = parse_xml(
            f'<w:pBdr {nsdecls("w")}>'
            f'  <w:bottom w:val="single" w:sz="4" w:space="4" w:color="CCCCCC"/>'
            f'</w:pBdr>'
        )
        pPr.append(pBdr)

        # ─── Footer with page number ───
        footer = section.footer
        footer.is_linked_to_previous = False
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # "Trang X / Y" format
        run = fp.add_run('Trang ')
        run.font.size = Pt(8)
        run.font.color.rgb = theme['muted']

        # Current page number field
        fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
        run1 = fp.add_run()
        run1._r.append(fldChar1)
        run2 = fp.add_run()
        instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
        run2._r.append(instrText)
        run3 = fp.add_run()
        fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
        run3._r.append(fldChar2)

        run = fp.add_run(' / ')
        run.font.size = Pt(8)
        run.font.color.rgb = theme['muted']

        # Total page number field
        fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
        run1 = fp.add_run()
        run1._r.append(fldChar1)
        run2 = fp.add_run()
        instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> NUMPAGES </w:instrText>')
        run2._r.append(instrText)
        run3 = fp.add_run()
        fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
        run3._r.append(fldChar2)
```

## Bước 8: Styled Tables (Full-Width + Professional)

```python
def add_styled_table(doc, theme, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # ★ Set table to full page width
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblW = parse_xml(f'<w:tblW {nsdecls("w")} w:w="5000" w:type="pct"/>')
    tblPr.append(tblW)

    # Header row styling
    for idx, header_text in enumerate(headers):
        cell = table.rows[0].cells[idx]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(clean_markdown(header_text))
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.font.name = theme['font_main']
        run.font.size = Pt(10)
        set_cell_shading(cell, theme['bg_table_header'])
        set_cell_borders(cell, color=theme['bg_table_header'], sz=6)

    # Data rows with alternating colors
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.rows[row_idx + 1].cells[col_idx]
            write_rich_text_to_cell(cell, cell_text, theme)
            if row_idx % 2 == 1:
                set_cell_shading(cell, theme['bg_table_alt'])
            set_cell_borders(cell, color='CCCCCC', sz=4)

    # ★ Mark first row as header (accessibility)
    tblHeader = parse_xml(f'<w:tblHeader {nsdecls("w")}/>')
    table.rows[0]._tr.get_or_add_trPr().append(tblHeader)

    doc.add_paragraph('')  # spacer
```

## Bước 9: Code Blocks (Gray Background)

```python
def add_code_block(doc, theme, code_text):
    """1-cell table = visual code block with gray bg and border."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Full width
    tbl = table._tbl
    tblW = parse_xml(f'<w:tblW {nsdecls("w")} w:w="5000" w:type="pct"/>')
    tbl.tblPr.append(tblW)

    cell = table.rows[0].cells[0]
    cell.text = ''
    set_cell_shading(cell, theme['bg_code'])
    set_cell_borders(cell, color='CCCCCC', sz=4)

    for line in code_text.split('\n'):
        p = cell.add_paragraph()
        run = p.add_run(line)
        run.font.name = theme['font_code']
        run.font.size = theme['code_size']
        run.font.color.rgb = theme['text']
        set_paragraph_spacing(p, before=0, after=0)

    # Remove first empty paragraph
    if cell.paragraphs[0].text == '':
        cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
```

## Bước 10: Blockquotes (Left Blue Border)

```python
def add_blockquote(doc, theme, text):
    """Blockquote with colored left border — like Notion callout."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.5)

    # ★ Blue left border
    pPr = p._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:left w:val="single" w:sz="18" w:space="12" w:color="3498DB"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)

    # Parse inline formatting
    add_rich_runs(p, text, theme, italic=True, color=theme['muted'])
```

## Bước 11: Section Breaks (New Page per Major Section)

```python
def add_section_break(doc):
    """Chèn section break — ## mới sẽ bắt đầu ở trang mới."""
    from docx.enum.section import WD_ORIENT
    new_section = doc.add_section()
    new_section.start_type = 2  # New page
    # Copy margins from first section
    first = doc.sections[0]
    new_section.page_width = first.page_width
    new_section.page_height = first.page_height
    new_section.left_margin = first.left_margin
    new_section.right_margin = first.right_margin
    new_section.top_margin = first.top_margin
    new_section.bottom_margin = first.bottom_margin
```

## Bước 12: Helper Functions

```python
import re

def clean_markdown(text):
    """Remove markdown markers from text."""
    return text.replace('**', '').replace('`', '').strip()

def set_cell_shading(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}" w:val="clear"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_borders(cell, color='AAAAAA', sz=4):
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tcBorders>'
    )
    cell._tc.get_or_add_tcPr().append(tcBorders)

def set_paragraph_spacing(p, before=0, after=0):
    pPr = p._p.get_or_add_pPr()
    spacing = parse_xml(f'<w:spacing {nsdecls("w")} w:before="{before}" w:after="{after}"/>')
    pPr.append(spacing)

def add_rich_runs(paragraph, text, theme, italic=False, color=None):
    """Parse **bold**, *italic*, `code` inline formatting."""
    pattern = r'(\*\*.*?\*\*|\*[^*]+\*|`[^`]+`)'
    parts = re.split(pattern, text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith('*') and part.endswith('*'):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        elif part.startswith('`') and part.endswith('`'):
            run = paragraph.add_run(part[1:-1])
            run.font.name = theme['font_code']
            run.font.size = theme['code_size']
            run.font.color.rgb = RGBColor(0xC7, 0x25, 0x4E)
            continue
        else:
            if not part:
                continue
            run = paragraph.add_run(part)
        run.font.name = theme['font_main']
        run.font.size = theme['font_size']
        run.font.color.rgb = color or theme['text']
        if italic:
            run.italic = True
```

## Bước 13: Main Parser (Markdown → DOCX)

Đọc file Markdown line-by-line, dispatch mỗi element đến đúng function:

```python
def parse_and_build(md_path, output_path, theme, doc_title):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = Document()
    # Page setup (Bước 1)
    setup_page(doc)
    # Styles (Bước 3)
    setup_styles(doc, theme)
    # Document properties (Bước 4)
    set_properties(doc, doc_title)
    # Cover page (Bước 5)
    add_cover_page(doc, theme, ...)
    # TOC (Bước 6)
    add_toc(doc, theme)

    # Parse loop
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # --- Headings ---
        if line.startswith('## '):
            add_section_break(doc)  # New page per H2
            doc.add_heading(clean_heading(line[3:]), level=2)
        elif line.startswith('### '):
            doc.add_heading(clean_heading(line[4:]), level=3)
        elif line.startswith('# '):
            doc.add_heading(clean_heading(line[2:]), level=1)

        # --- Code blocks ---
        elif line.strip().startswith('```'):
            code_lines, i = collect_code_block(lines, i)
            add_code_block(doc, theme, code_lines)

        # --- Tables ---
        elif '|' in line and is_table_start(lines, i):
            headers, rows, i = collect_table(lines, i)
            add_styled_table(doc, theme, headers, rows)

        # --- Blockquotes ---
        elif line.startswith('>'):
            add_blockquote(doc, theme, line.lstrip('>').strip())

        # --- Bullets ---
        elif line.startswith('- '):
            add_rich_bullet(doc, theme, line[2:])

        # --- Numbered ---
        elif re.match(r'^\d+\.\s', line):
            add_rich_numbered(doc, theme, line)

        # --- Horizontal rule ---
        elif line.strip() == '---':
            add_divider(doc, theme)

        # --- Regular text ---
        elif line.strip():
            add_rich_paragraph(doc, theme, line)

        i += 1

    # Headers/Footers (Bước 7) — must be AFTER all sections created
    add_header_footer(doc, theme, doc_title)
    # Page border
    add_page_border(doc, theme)

    doc.save(output_path)
```

---

# Examples

## Ví dụ 1: Chuyển đổi MD → DOCX cơ bản

**Input:** `"Chuyển file ABM-Workforce-HDSD.md thành Word"`

**Output:** AI tạo script Python sử dụng architecture ở trên, chạy 1 lần, sinh file DOCX 7+ trang với:
- ✅ Cover page (accent bar + title + subtitle)
- ✅ Table of Contents (auto-update khi mở Word)
- ✅ Page numbers "Trang X / Y" ở footer
- ✅ Header với tên tài liệu
- ✅ Tables với header Navy, alternating rows
- ✅ Code blocks với nền xám
- ✅ Blockquotes với viền xanh bên trái

---

## Ví dụ 2: Tùy chỉnh Theme

**Input:** `"Chuyển sang Word nhưng dùng màu xanh lá cho thương hiệu"`

**Output:** AI đổi THEME config:
```python
THEME = {
    'primary': RGBColor(0x1B, 0x5E, 0x20),    # Forest Green
    'accent':  RGBColor(0x4C, 0xAF, 0x50),     # Green
    'bg_table_header': '1B5E20',
    # ... rest stays same
}
```

---

## Ví dụ 3: Tài liệu doanh nghiệp có watermark

**Input:** `"Tạo Word cho báo cáo nội bộ, thêm watermark NỘI BỘ"`

**Output:** AI thêm watermark text vào header:
```python
# Watermark via header shape (simplified)
header = section.header
wp = header.paragraphs[0]
run = wp.add_run('NỘI BỘ')
run.font.size = Pt(48)
run.font.color.rgb = RGBColor(0xE0, 0xE0, 0xE0)  # Very light gray
```

---

# Constraints

## Dependencies
- **BẮT BUỘC:** `python-docx` (pip install python-docx)
- **Không cần:** pandoc, htmldocx, LibreOffice, wkhtmltopdf

## Typography
- Font chính: **Arial** (system font, an toàn trên mọi OS)
- Font code: **Consolas** (Windows) hoặc **Courier New** (fallback)
- **TUYỆT ĐỐI KHÔNG** dùng font cần cài đặt riêng (Roboto, Inter) — file sẽ hiển thị sai trên máy khác

## Vietnamese Safety
- python-docx ghi trực tiếp Unicode XML → 100% an toàn tiếng Việt
- **KHÔNG** đọc file qua `txt` hoặc console stream → chỉ dùng `open(path, 'r', encoding='utf-8')`
- Emoji (📘, ⚡, 🎨) → có thể replace bằng text tương đương nếu target là in ấn B&W

## Quality Checklist (Trước khi giao file)
- [ ] Mở file → TOC hiển thị (dù là placeholder)
- [ ] Footer có "Trang X / Y"
- [ ] Header có tên tài liệu
- [ ] Tất cả bảng có header row đậm + viền đầy đủ
- [ ] Code blocks có nền xám + font monospace
- [ ] Không có emoji bị vỡ (nếu target là print)
- [ ] Document Properties đã điền (title, author)

## Performance
- File Markdown dưới 500 dòng → script chạy <3 giây
- File trên 1000 dòng → cân nhắc tách thành nhiều DOCX
- Output file nên dưới 500 KB (không embed ảnh nặng)

## Anti-Patterns (KHÔNG làm)
- ❌ KHÔNG dùng `htmldocx` — bảng biểu sẽ vỡ
- ❌ KHÔNG dùng `pypandoc` mặc định — styling quá basic
- ❌ KHÔNG hardcode đường dẫn file — dùng argument hoặc biến
- ❌ KHÔNG tạo file mà thiếu TOC cho tài liệu >5 trang
- ❌ KHÔNG dùng `doc.add_paragraph()` cho heading — mất Outline Level

<!-- Generated by Skill Creator Ultra v2.0 -->
