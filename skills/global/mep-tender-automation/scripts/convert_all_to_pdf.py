# -*- coding: utf-8 -*-
"""Batch convert all tender .md files → PDF using markdown + Playwright"""
import markdown
import os
import sys

# All MD files to convert
FILES = [
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\A. COMMERCIAL PART\5. Value Engineering\VE-Proposals-Core5-HP-II-MEP.md",
        "title": "VALUE ENGINEERING PROPOSALS",
        "subtitle": "MEP Works Package — Core5 Hai Phong II",
    },
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\A. COMMERCIAL PART\7. Name and address of provider of Advance Payment Security\TTC-Advance-Payment-Security.md",
        "title": "ADVANCE PAYMENT SECURITY",
        "subtitle": "Banking & Security Information",
    },
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\A. COMMERCIAL PART\8. Name and address of insurers and principal terms of the policy\TTC-Insurance-Information.md",
        "title": "INSURERS & POLICY",
        "subtitle": "Insurance Coverage Information",
    },
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\B. TECHNICAL PART\7. Method Statement\TTC-Method-Statement-MEP-Core5-HP-II.md",
        "title": "METHOD STATEMENT",
        "subtitle": "MEP Installation Procedures",
    },
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\B. TECHNICAL PART\8. Schedule of Goods  Material and Plants\TTC-Material-Schedule-MEP-Core5-HP-II.md",
        "title": "SCHEDULE OF GOODS,<br>MATERIALS AND PLANTS",
        "subtitle": "Major Equipment & Delivery Timeline",
    },
    {
        "md": r"D:\Thang tien\1. TT-CORE5-HP-TENDER DOCCUMENT (1st TIME)\B. TECHNICAL PART\10. Project Management Plan\TTC-Project-Management-Plan-MEP-Core5-HP-II.md",
        "title": "PROJECT MANAGEMENT PLAN",
        "subtitle": "Organization, QA/QC, HSE & Procurement",
    },
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

@page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
    @bottom-center {
        content: "Thang Tien JSC — Core5 HP II MEP";
        font-size: 7pt;
        color: #999;
    }
    @bottom-right {
        content: counter(page);
        font-size: 7pt;
        color: #999;
    }
}

* { box-sizing: border-box; }

body {
    font-family: 'Inter', 'Segoe UI', Tahoma, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1a1a2e;
    max-width: 100%;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

h1 {
    font-size: 18pt;
    font-weight: 700;
    color: #0f3460;
    border-bottom: 3px solid #e94560;
    padding-bottom: 6px;
    margin-top: 24px;
    page-break-after: avoid;
}

h2 {
    font-size: 13pt;
    font-weight: 600;
    color: #16213e;
    border-bottom: 2px solid #0f3460;
    padding-bottom: 4px;
    margin-top: 20px;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    font-weight: 600;
    color: #0f3460;
    margin-top: 14px;
    page-break-after: avoid;
}

h4 {
    font-size: 10pt;
    font-weight: 600;
    color: #16213e;
    margin-top: 10px;
    page-break-after: avoid;
}

blockquote {
    background: #f0f4ff;
    border-left: 4px solid #0f3460;
    padding: 8px 12px;
    margin: 10px 0;
    border-radius: 0 6px 6px 0;
    font-size: 9pt;
}

blockquote p { margin: 2px 0; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
    page-break-inside: auto;
}

thead {
    background: #0f3460;
    color: white;
}

th {
    padding: 6px 7px;
    text-align: left;
    font-weight: 600;
    font-size: 8pt;
}

td {
    padding: 4px 7px;
    border-bottom: 1px solid #e0e0e0;
    vertical-align: top;
}

tr:nth-child(even) { background: #f8f9fc; }

code {
    background: #f0f0f0;
    padding: 1px 3px;
    border-radius: 3px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
}

pre {
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 10px 14px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 8pt;
    line-height: 1.35;
    page-break-inside: avoid;
}

pre code {
    background: none;
    padding: 0;
    color: inherit;
}

hr {
    border: none;
    border-top: 2px solid #e0e0e0;
    margin: 16px 0;
}

strong { font-weight: 600; color: #16213e; }

ul, ol { padding-left: 16px; }
li { margin: 2px 0; }

li input[type="checkbox"] { margin-right: 5px; }

h2, h3 { page-break-after: avoid; }
table { page-break-inside: auto; }
tr { page-break-inside: avoid; }

.cover {
    text-align: center;
    padding: 80px 20px 40px;
    page-break-after: always;
}
.cover h1 {
    border: none;
    font-size: 24pt;
    margin-bottom: 10px;
    line-height: 1.3;
}
.cover .subtitle {
    font-size: 13pt;
    color: #16213e;
    margin: 10px 0;
}
.cover .meta {
    font-size: 10pt;
    color: #666;
    margin-top: 40px;
    line-height: 1.8;
}
.cover .logo-bar {
    background: linear-gradient(135deg, #0f3460, #16213e);
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    margin-top: 50px;
    font-size: 11pt;
    font-weight: 600;
}
"""


def convert_one(info):
    md_path = info["md"]
    pdf_path = md_path.replace(".md", ".pdf")
    html_path = md_path.replace(".md", ".html")
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "toc", "nl2br"],
        output_format="html5"
    )
    
    cover = f"""
    <div class="cover">
        <div class="logo-bar">CÔNG TY CP KỸ THUẬT THĂNG TIẾN</div>
        <h1>{info["title"]}</h1>
        <div class="subtitle">{info["subtitle"]}</div>
        <div class="meta">
            <p>Dự án: Core5 Hai Phong II — Ready Built Factory & Warehouse</p>
            <p>Gói thầu: MEP Works Package</p>
            <p>Tháng 02/2026</p>
        </div>
    </div>
    """
    
    html_doc = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>{info["title"]}</title>
    <style>{CSS}</style>
</head>
<body>
    {cover}
    {html_body}
</body>
</html>"""
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_doc)
    
    return html_path, pdf_path


# Convert all
from playwright.sync_api import sync_playwright

results = []
for info in FILES:
    html_path, pdf_path = convert_one(info)
    results.append((html_path, pdf_path, info["title"]))
    print(f"✅ HTML: {os.path.basename(html_path)}")

print(f"\n📄 Converting {len(results)} files to PDF via Playwright...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    for html_path, pdf_path, title in results:
        page = browser.new_page()
        page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        page.wait_for_load_state("networkidle")
        page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            print_background=True,
            display_header_footer=True,
            header_template='<span></span>',
            footer_template='<div style="font-size:7pt;width:100%;text-align:center;color:#999;">Thang Tien JSC — Core5 HP II MEP | <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
        )
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"  ✅ {os.path.basename(pdf_path)} ({size_kb:.0f} KB)")
        page.close()
    browser.close()

print(f"\n🎉 Done! {len(results)} PDFs created.")
