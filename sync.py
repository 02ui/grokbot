#!/usr/bin/env python3
"""Rebuild brain-content.js from your markdown files.

Run this whenever a .md file is created, edited, renamed, or deleted:

    python3 sync.py

Why this exists: index.html is opened straight from disk, and browsers do not
let a local page read other local files. So the browser view reads its text
from brain-content.js instead. This script keeps that file in step with the
markdown, so nobody has to copy anything across by hand.

No installation and no dependencies - it uses only what Python already ships
with. If you do not have Python, you can still edit brain-content.js yourself;
see grok.md.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "brain-content.js"

# The three foundation files, in the order they should appear in the sidebar.
STACK_FILES = ["who-you-are.md", "what-you-do.md", "what-you-want.md"]

FOLDERS = [
    ("01-ideas", "Raw thoughts and quick captures"),
    ("02-projects", "Active work with a finish line"),
    ("03-areas", "Ongoing responsibilities"),
    ("04-wiki", "Evergreen knowledge you look things up in"),
    ("05-resources", "Reference material you collect"),
    ("06-archive", "Finished or paused work"),
]

HEADING = re.compile(r"^\s*#\s+(.+?)\s*$")


def title_of(text, path):
    """First level-one heading, or a readable version of the filename."""
    for line in text.splitlines():
        found = HEADING.match(line)
        if found:
            return found.group(1)
    words = path.stem.replace("-", " ").replace("_", " ").strip()
    return words[:1].upper() + words[1:] if words else path.stem


def entry(path, section, folder=None):
    text = path.read_text(encoding="utf-8")
    item = {
        "id": "",  # filled in by build(), which handles duplicate names
        "title": title_of(text, path),
        "file": path.relative_to(ROOT).as_posix(),
    }
    if folder:
        item["folder"] = folder
    item["section"] = section
    item["content"] = text.rstrip("\n")
    return item


def build():
    stack, notes = [], []

    for name in STACK_FILES:
        path = ROOT / name
        if path.is_file():
            stack.append(entry(path, "stack"))
        else:
            print("  skipped (missing): " + name, file=sys.stderr)

    for folder, _ in FOLDERS:
        directory = ROOT / folder
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("."):
                continue
            notes.append(entry(path, "notes", folder=folder))

    # Two folders may hold the same filename, so fall back to a fuller id.
    seen = {}
    for item in stack + notes:
        path = Path(item["file"])
        wanted = path.stem
        if wanted in seen:
            wanted = path.as_posix()[: -len(path.suffix)].replace("/", "-")
        seen[wanted] = True
        item["id"] = wanted

    return stack, notes


def render(stack, notes):
    data = {
        "stack": stack,
        "notes": notes,
        "folders": [
            {"id": f, "label": f, "description": d} for f, d in FOLDERS
        ],
    }
    body = json.dumps(data, indent=2, ensure_ascii=False)
    # Valid in JSON, historically not in JavaScript source. Escape to be safe.
    body = body.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return (
        "/**\n"
        " * Brain content for the HTML index.\n"
        " *\n"
        " * GENERATED FILE - do not edit by hand.\n"
        " * Rebuild it after any .md change with:  python3 sync.py\n"
        " */\n"
        "window.BRAIN = " + body + ";\n"
    )


def main():
    stack, notes = build()
    OUTPUT.write_text(render(stack, notes), encoding="utf-8")
    print(
        "{0} stack file{1}, {2} note{3} -> brain-content.js".format(
            len(stack), "" if len(stack) == 1 else "s",
            len(notes), "" if len(notes) == 1 else "s",
        )
    )
    print("Close the index.html tab and open it again to see the changes.")


if __name__ == "__main__":
    main()
