#!/usr/bin/env python3
"""
Merge Parts — Ghép nhiều file Markdown thành một file duy nhất.
Đảm bảo encoding UTF-8 chuẩn (không BOM) cho tiếng Việt.

Thuộc dự án: Viết Chuyên Nghiệp v3.1 — Tòa Soạn AI
Worker: merge-worker.md

Cách dùng:
  python merge-parts.py --dir <thư_mục> --pattern <tên> --output <file>
  python merge-parts.py --files file1.md file2.md file3.md --output merged.md

Ví dụ:
  python merge-parts.py --dir ./output --pattern bsr-bai1-voiceover --output bsr-bai1-voiceover-full.md
  python merge-parts.py --files part1.md part2.md part3.md --output final.md
"""

import argparse
import glob
import os
import re
import sys


def find_parts(directory: str, pattern: str) -> list[str]:
    """Tìm tất cả file part theo pattern, sắp xếp theo số thứ tự."""
    search = os.path.join(directory, f"{pattern}-part*.md")
    files = glob.glob(search)

    if not files:
        # Thử pattern khác: pattern_part*.md
        search = os.path.join(directory, f"{pattern}_part*.md")
        files = glob.glob(search)

    if not files:
        # Thử pattern không có dấu nối: patternpart*.md
        search = os.path.join(directory, f"{pattern}*part*.md")
        files = glob.glob(search)

    # Sắp xếp theo số trong tên file
    def extract_number(f):
        match = re.search(r'part[_-]?(\d+)', os.path.basename(f), re.IGNORECASE)
        return int(match.group(1)) if match else 0

    files.sort(key=extract_number)
    return files


def merge_files(file_list: list[str], output_path: str) -> dict:
    """Ghép danh sách file thành một file duy nhất với UTF-8 chuẩn."""
    content = ""
    stats = {
        "input_files": [],
        "total_chars": 0,
        "total_lines": 0,
        "encoding": "utf-8-no-bom",
        "tieng_viet": "OK",
    }

    for filepath in file_list:
        if not os.path.exists(filepath):
            print(f"⚠️  Không tìm thấy file: {filepath}", file=sys.stderr)
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            # Loại bỏ BOM nếu có
            if text.startswith("\ufeff"):
                text = text[1:]

            content += text
            stats["input_files"].append(os.path.basename(filepath))
            print(f"  ✓ {os.path.basename(filepath)} — {len(text)} chars")
        except UnicodeDecodeError:
            # Thử đọc với encoding khác
            try:
                with open(filepath, "r", encoding="utf-8-sig") as f:
                    text = f.read()
                content += text
                stats["input_files"].append(os.path.basename(filepath))
                print(f"  ✓ {os.path.basename(filepath)} — {len(text)} chars (utf-8-sig)")
            except Exception as e:
                print(f"  ✗ {os.path.basename(filepath)} — LỖI: {e}", file=sys.stderr)
                stats["tieng_viet"] = "LOI"

    if not content:
        print("❌ Không có nội dung nào để merge!", file=sys.stderr)
        sys.exit(1)

    # Ghi file output — UTF-8 without BOM
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    stats["total_chars"] = len(content)
    stats["total_lines"] = content.count("\n")
    stats["output_file"] = os.path.basename(output_path)

    # Verify encoding
    with open(output_path, "rb") as f:
        raw = f.read(3)
        if raw[:3] == b"\xef\xbb\xbf":
            stats["encoding"] = "utf-8-with-bom"
            print("⚠️  File output có BOM — cần kiểm tra!", file=sys.stderr)

    # Verify tiếng Việt cơ bản
    viet_chars = "àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ"
    has_viet = any(c in content.lower() for c in viet_chars)
    if not has_viet and len(content) > 100:
        stats["tieng_viet"] = "CANH_BAO"
        print("⚠️  Không phát hiện ký tự tiếng Việt — kiểm tra encoding!", file=sys.stderr)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Ghép nhiều file Markdown thành một — UTF-8 chuẩn cho tiếng Việt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  python merge-parts.py --dir ./output --pattern bsr-bai1 --output bsr-bai1-full.md
  python merge-parts.py --files ch1.md ch2.md ch3.md --output book.md
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--files", nargs="+", help="Danh sách file cần merge (theo thứ tự)")
    group.add_argument("--pattern", help="Pattern tên file (vd: bsr-bai1-voiceover)")

    parser.add_argument("--dir", default=".", help="Thư mục chứa file parts (mặc định: .)")
    parser.add_argument("--output", "-o", required=True, help="Tên file output")

    args = parser.parse_args()

    print("=" * 50)
    print("📄 MERGE PARTS — Viết Chuyên Nghiệp v3.1")
    print("=" * 50)

    if args.files:
        file_list = args.files
    else:
        file_list = find_parts(args.dir, args.pattern)
        if not file_list:
            print(f"❌ Không tìm thấy file nào với pattern '{args.pattern}' trong '{args.dir}'")
            sys.exit(1)

    print(f"\n📂 Input: {len(file_list)} file(s)")
    stats = merge_files(file_list, args.output)

    print(f"\n✅ Output: {args.output}")
    print(f"   Chars: {stats['total_chars']:,}")
    print(f"   Lines: {stats['total_lines']:,}")
    print(f"   Encoding: {stats['encoding']}")
    print(f"   Tiếng Việt: {stats['tieng_viet']}")

    # Ước tính thời lượng đọc (170-200 từ/phút tiếng Việt)
    # Tiếng Việt trung bình ~5 chars/từ
    est_words = stats["total_chars"] // 5
    est_min_low = est_words // 200
    est_min_high = est_words // 170
    print(f"   Ước tính: ~{est_words:,} từ ≈ {est_min_low}-{est_min_high} phút đọc")
    print("=" * 50)


if __name__ == "__main__":
    main()
