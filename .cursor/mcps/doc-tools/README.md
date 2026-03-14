# doc-tools MCP Server

提供文档字数统计的 MCP 工具，供 Cursor Agent 调用，避免口头估算字数出错。

## 工具

- **count_document(path)**  
  统计指定文本文件的字符数、正文字数（不含换行）、行数。  
  `path` 为相对工作区根目录的路径，如 `novel/井中头七.md`。

工具描述由 Cursor 在**用户维度**通过 MCP 协议从本 server 拉取，无需在工作区存放描述文件。

## 依赖

```bash
pip install -r .cursor/mcps/doc-tools/requirements.txt
# 或
pip install "mcp[cli]>=1.0.0"
```

## 配置

已在 `.cursor/mcp.json` 中注册为 `doc-tools`。重启 Cursor 或重新加载 MCP 后生效。

## 本地测试（可选）

```bash
# 统计逻辑与 CLI 一致
python3 .cursor/scripts/count_doc.py novel/井中头七.md
```
