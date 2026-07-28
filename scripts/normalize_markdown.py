#!/usr/bin/env python3
"""Normalize this vault for readable GitHub and Quartz rendering."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
HEADING = re.compile(r"^(#{1,6})\s*(.+?)\s*$")
WIKILINK = re.compile(r"\[\[([^]|#]+)(#[^]|]+)?(?:\|([^\]]+))?\]\]")
ZERO_WIDTH = re.compile("[\u200b\u200c\u200d\ufeff]")


def title_for(path: Path) -> str:
    title = path.stem.strip()
    return re.sub(r"^\d+(?:\.\d+)*[.、]?\s*", "", title) or title


def split_display_math(text: str) -> str:
    """Put every $$ expression on dedicated lines."""
    parts = text.split("$$")
    if len(parts) == 1:
        return text
    if len(parts) % 2 == 0:
        return text

    output: list[str] = []
    for index, part in enumerate(parts):
        cleaned = part.strip()
        if index % 2:
            output.extend(["", "$$", cleaned, "$$", ""])
        elif cleaned:
            output.append(cleaned)
    return "\n".join(output)


def normalize_note(path: Path) -> None:
    text = ZERO_WIDTH.sub("", path.read_text(encoding="utf-8")).replace("\r\n", "\n")
    text = split_display_math(text)
    lines = text.splitlines()

    in_fence = False
    heading_levels: list[int] = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and (match := HEADING.match(line)):
            level = len(match.group(1))
            if level > 1:
                heading_levels.append(level)

    minimum = min(heading_levels, default=2)
    shift = 2 - minimum
    output: list[str] = []
    in_fence = False
    in_math = False

    for line in lines:
        stripped = line.rstrip()
        if stripped.lstrip().startswith("```"):
            if in_fence:
                while output and output[-1] == "":
                    output.pop()
                output.extend(["```", ""])
                in_fence = False
            else:
                fence = stripped.strip()
                if fence == "```":
                    fence = "```text"
                if output and output[-1] != "":
                    output.append("")
                output.append(fence)
                in_fence = True
            continue

        if not in_fence and stripped == "$$":
            if in_math:
                while output and output[-1] == "":
                    output.pop()
                output.extend(["$$", ""])
                in_math = False
            else:
                if output and output[-1] != "":
                    output.append("")
                output.append("$$")
                in_math = True
            continue

        if not in_fence and not in_math and (match := HEADING.match(stripped)):
            original_level = len(match.group(1))
            level = 1 if original_level == 1 else max(2, min(6, original_level + shift))
            heading_text = re.sub(r"^(\d+[.)])\s*", r"\1 ", match.group(2).strip())
            stripped = f"{'#' * level} {heading_text}"
            if output and output[-1] != "":
                output.append("")
            output.extend([stripped, ""])
            continue

        output.append(stripped)

    if in_fence:
        while output and output[-1] == "":
            output.pop()
        output.append("```")

    if in_math:
        while output and output[-1] == "":
            output.pop()
        output.append("$$")

    while output and output[-1] == "":
        output.pop()

    body = "\n".join(output).strip()
    if not re.match(r"^#\s+", body):
        body = f"# {title_for(path)}\n\n{body}"

    body = re.sub(r"\n{3,}", "\n\n", body)
    path.write_text(body + "\n", encoding="utf-8", newline="\n")


def relative_github_link(target: str, alias: str | None) -> str:
    clean_target = target.strip().replace("\\", "/")
    if not clean_target.endswith(".md"):
        clean_target += ".md"
    label = (alias or Path(target).name).strip()
    return f"[{label}](<content/{clean_target}>)"


def normalize_readme() -> None:
    path = ROOT / "README.md"
    text = (
        ZERO_WIDTH.sub("", path.read_text(encoding="utf-8"))
        .replace("\r\n", "\n")
        .replace("\u00a0", " ")
    )
    text = WIKILINK.sub(
        lambda match: relative_github_link(match.group(1), match.group(3)),
        text,
    )

    if not text.lstrip().startswith("# "):
        header = """# 动手学深度学习笔记

[![在线阅读](https://img.shields.io/badge/在线阅读-Quartz-2563eb?style=for-the-badge&logo=github)](https://lan-007.github.io/Notes-of-Dive-into-DeepLearning/)
[![Markdown 链接检查](https://github.com/Lan-007/Notes-of-Dive-into-DeepLearning/actions/workflows/markdown-links.yml/badge.svg)](https://github.com/Lan-007/Notes-of-Dive-into-DeepLearning/actions/workflows/markdown-links.yml)

基于 PyTorch 的《动手学深度学习》学习笔记，涵盖基础知识、神经网络训练、注意力机制、Transformer 与 NLP 预训练应用。

> [!TIP]
> 推荐访问 **[在线阅读版](https://lan-007.github.io/Notes-of-Dive-into-DeepLearning/)**，可使用全文搜索、章节目录、公式渲染和深色模式。

## 学习路线

"""
        text = header + text.lstrip()

    text = text.replace(
        "NLP预训练NLP应用",
        "NLP 预训练 → NLP 应用",
    )
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"(?<!\n)\n(#{2,6}\s)", r"\n\n\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    for note in sorted(CONTENT.rglob("*.md")):
        normalize_note(note)
    normalize_readme()
    print(f"Normalized {len(list(CONTENT.rglob('*.md')))} notes and README.md")


if __name__ == "__main__":
    main()
