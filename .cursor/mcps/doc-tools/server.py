"""MCP server exposing document word/character count tool.

Provides count_document(path) for reliable 字数 stats; paths are relative
to the workspace root (server is started with cwd=workspace).
"""

import sys
from pathlib import Path

# Workspace root: .cursor/mcps/doc-tools/server.py -> parent x4
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent.parent
# Import counting logic from .cursor/scripts
sys.path.insert(0, str(WORKSPACE_ROOT / ".cursor" / "scripts"))
from count_doc import count_file

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "doc-tools",
    instructions=(
        "Document statistics. Use count_document to get exact character count (字数), "
        "body character count (正文字数, excluding newlines), and line count for a text file. "
        "Path is relative to workspace root, e.g. novel/井中头七.md"
    ),
)


@mcp.tool()
def count_document(path: str) -> str:
    """Count characters and lines in a text file.

    Returns reliable 字数/字符数 statistics. Use this instead of estimating
    to avoid counting errors.

    Args:
        path: File path relative to workspace root (e.g. novel/井中头七.md)
              or absolute path. UTF-8 text files only.

    Returns:
        A short report with: 总字符数（含空格与换行）, 正文字数（不含换行）, 行数.
    """
    resolved = (
        Path(path).resolve()
        if Path(path).is_absolute()
        else (WORKSPACE_ROOT / path).resolve()
    )
    try:
        root = WORKSPACE_ROOT.resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            return f"Error: Path outside workspace: {path}"
        stats = count_file(str(resolved))
    except FileNotFoundError:
        return f"Error: File not found: {path}"
    except Exception as e:
        return f"Error: {e}"

    return (
        f"--- 字数统计 {path} ---\n"
        f"总字符数（含空格与换行）: {stats['total_chars']:,}\n"
        f"正文字数（不含换行）:     {stats['body_chars']:,}\n"
        f"行数: {stats['total_lines']:,}（其中非空行 {stats['non_empty_lines']:,}）\n"
        "------------------"
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
