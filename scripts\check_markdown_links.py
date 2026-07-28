#!/usr/bin/env python3
"""Check local Markdown links and Obsidian wikilinks without network access."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\((?:<([^>]+)>|([^) \t]+))\)")
WIKILINK = re.compile(r"!?\[\[([^]|#]+)(?:#[^]|]+)?(?:\|[^\]]+)?\]\]")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def markdown_files() -> list[Path]:
    return [
        *sorted(ROOT.glob("*.md")),
        *sorted((ROOT / "content").rglob("*.md")),
    ]


def strip_code_blocks(text: str) -> str:
    visible: list[str] = []
    fence_marker: str | None = None
    for line in text.splitlines():
        match = FENCE.match(line)
        if match:
            marker = match.group(1)[0]
            if fence_marker is None:
                fence_marker = marker
            elif marker == fence_marker:
                fence_marker = None
            continue
        if fence_marker is None:
            visible.append(line)
    return "\n".join(visible)


def resolve_markdown_link(source: Path, raw_target: str) -> Path | None:
    target = unquote(raw_target.split("#", 1)[0].split("?", 1)[0]).strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
        return None
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return source.parent / target


def resolve_wikilink(source: Path, raw_target: str, all_notes: list[Path]) -> Path | None:
    target = unquote(raw_target.strip()).replace("\\", "/")
    candidates = [target, f"{target}.md"] if not target.endswith(".md") else [target]

    for candidate in candidates:
        direct = source.parent / candidate
        if direct.exists():
            return direct
        from_root = ROOT / "content" / candidate
        if from_root.exists():
            return from_root

    target_name = Path(target).stem.casefold()
    matches = [path for path in all_notes if path.stem.casefold() == target_name]
    return matches[0] if len(matches) == 1 else ROOT / ".__missing_wikilink__"


def main() -> int:
    files = markdown_files()
    missing: list[str] = []

    for source in files:
        if not source.exists():
            missing.append(f"{source.relative_to(ROOT)}: file is missing")
            continue

        text = strip_code_blocks(source.read_text(encoding="utf-8"))
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1) or match.group(2)
            target = resolve_markdown_link(source, raw_target)
            if target is not None and not target.exists():
                missing.append(
                    f"{source.relative_to(ROOT)}: {raw_target} -> "
                    f"{target.resolve(strict=False)}"
                )

        for match in WIKILINK.finditer(text):
            raw_target = match.group(1)
            target = resolve_wikilink(source, raw_target, files)
            if target is not None and not target.exists():
                missing.append(f"{source.relative_to(ROOT)}: [[{raw_target}]]")

    if missing:
        print("Broken internal Markdown links:")
        for item in missing:
            print(f"- {item}")
        return 1

    print(f"Checked {len(files)} Markdown files: all internal links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
