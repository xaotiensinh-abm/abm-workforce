---
description: Xử lý Word documents: tạo mới, edit, tracked changes
---

Workflow cho DOCX: đọc/phân tích, tạo mới (docx-js), chỉnh sửa (OOXML), redlining.

---

## Decision Tree

| Task | Workflow |
|------|----------|
| **Đọc/Phân tích** | Text extraction hoặc Raw XML |
| **Tạo mới** | docx-js (JavaScript) |
| **Edit đơn giản** | Basic OOXML editing |
| **Edit document của người khác** | **Redlining workflow** |
| **Legal/Academic/Business docs** | **Redlining workflow** (bắt buộc) |

---

## Reading & Analyzing

### Text Extraction với Pandoc
```bash
# Convert to markdown với tracked changes
pandoc --track-changes=all file.docx -o output.md
# Options: --track-changes=accept/reject/all
```

### Raw XML Access
```bash
# Unpack DOCX để xem XML
python D:\Antigravity\Skill\claude-skills\docx\ooxml\scripts\unpack.py <file.docx> <output_dir>
```

Key files:
- `word/document.xml` - Main content
- `word/comments.xml` - Comments
- `word/media/` - Embedded media

---

## Creating New Documents (docx-js)

// turbo
**MANDATORY**: Đọc file `D:\Antigravity\Skill\claude-skills\docx\docx-js.md` trước khi viết code.

```javascript
import { Document, Packer, Paragraph, TextRun } from "docx";
import * as fs from "fs";

const doc = new Document({
  sections: [{
    children: [
      new Paragraph({
        children: [
          new TextRun("Hello World"),
          new TextRun({ text: "Bold text", bold: true })
        ]
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("output.docx", buffer);
});
```

---

## Editing Existing Documents (OOXML)

// turbo
**MANDATORY**: Đọc file `D:\Antigravity\Skill\claude-skills\docx\ooxml.md` trước khi edit.

### Workflow
1. Unpack: `python ooxml/scripts/unpack.py <file.docx> <dir>`
2. Edit bằng Python script (Document library)
3. Pack: `python ooxml/scripts/pack.py <dir> <output.docx>`

---

## Redlining Workflow (Tracked Changes)

Dùng cho document review với tracked changes.

### Steps

1. **Get markdown**:
   ```bash
   pandoc --track-changes=all file.docx -o current.md
   ```

2. **Identify changes**: Group 3-10 related changes per batch

3. **Read ooxml.md** và unpack document

4. **Implement changes** in batches

5. **Pack document**:
   ```bash
   python ooxml/scripts/pack.py unpacked reviewed.docx
   ```

6. **Verify**:
   ```bash
   pandoc --track-changes=all reviewed.docx -o verification.md
   ```

### Minimal Edits Principle

```python
# BAD - Replace entire sentence
'<w:del>...<w:delText>The term is 30 days.</w:delText>...</w:del>'

# GOOD - Only mark what changed
'<w:r>...<w:t>The term is </w:t></w:r><w:del>...<w:delText>30</w:delText>...</w:del><w:ins>...<w:t>60</w:t>...</w:ins><w:r>...<w:t> days.</w:t></w:r>'
```

---

## Convert to Images

```bash
# Step 1: DOCX to PDF
soffice --headless --convert-to pdf document.docx

# Step 2: PDF to JPEG
pdftoppm -jpeg -r 150 document.pdf page
# Output: page-1.jpg, page-2.jpg, etc.
```

---

## Dependencies

```bash
# pandoc
sudo apt-get install pandoc

# docx (npm)
npm install -g docx

# LibreOffice (PDF conversion)
sudo apt-get install libreoffice

# Poppler (pdftoppm)
sudo apt-get install poppler-utils
```
