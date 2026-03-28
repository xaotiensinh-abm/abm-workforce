import mammoth
import markdownify
import argparse
import os
import sys

def convert_docx_to_md(docx_path, md_path=None):
    if not os.path.exists(docx_path):
        print(f"Error: File {docx_path} not found.")
        sys.exit(1)
    
    if md_path is None:
        md_path = os.path.splitext(docx_path)[0] + ".md"

    print(f"Converting {docx_path} to {md_path}...")

    # Convert DOCX to HTML using mammoth
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value
        messages = result.messages
        if messages:
            for message in messages:
                print(f"Mammoth Message: {message}")

    # Convert HTML to Markdown using markdownify
    # Use standard options for cleaner output
    md = markdownify.markdownify(html, heading_style="ATX")

    # Save Markdown to file with UTF-8 encoding
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(md)

    print(f"SUCCESS: Markdown file created at {md_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .docx to .md locally.")
    parser.add_argument("--input", required=True, help="Input .docx file path")
    parser.add_argument("--output", help="Output .md file path (optional)")
    
    args = parser.parse_args()
    convert_docx_to_md(args.input, args.output)
