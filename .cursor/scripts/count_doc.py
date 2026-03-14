"""Count characters and lines in a UTF-8 text file.

Used by .cursor/mcps doc-tools server and can be run as CLI:
    python3 .cursor/scripts/count_doc.py <path>
"""

import sys
from pathlib import Path


def count_file(path: str) -> dict[str, int]:
    """Count stats for a text file (UTF-8).

    Returns:
        total_chars: All characters including spaces and newlines.
        body_chars: Characters excluding newlines (正文字数).
        total_lines: Number of lines.
        non_empty_lines: Number of lines that are non-empty (strip() != "").
    """
    try:
        content = Path(path).read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        raise ValueError(f"File is not valid UTF-8: {e}") from e
    lines = content.splitlines()
    total_chars = len(content)
    body_chars = sum(len(line) for line in lines)
    total_lines = len(lines)
    non_empty_lines = sum(1 for line in lines if line.strip())
    return {
        "total_chars": total_chars,
        "body_chars": body_chars,
        "total_lines": total_lines,
        "non_empty_lines": non_empty_lines,
    }


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 .cursor/scripts/count_doc.py <path>", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    try:
        stats = count_file(path)
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"--- 字数统计 {path} ---")
    print(f"总字符数（含空格与换行）: {stats['total_chars']:,}")
    print(f"正文字数（不含换行）:     {stats['body_chars']:,}")
    print(f"行数: {stats['total_lines']:,}（其中非空行 {stats['non_empty_lines']:,}）")
    print("------------------")


if __name__ == "__main__":
    main()
