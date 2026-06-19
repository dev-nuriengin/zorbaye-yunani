#!/usr/bin/env python3
"""Print the chapter-translation board. Read-only; safe to run anytime.

Scans board/ch*.md (one file per chapter, each owned by a single agent) and
prints a status table. No writes, so it never races with any agent.
"""
import re, pathlib

BOARD = pathlib.Path(__file__).resolve().parent / "board"
COLS = ["chapter", "status", "agent", "branch", "pdf_pages", "sentences", "verified", "updated"]

def parse(path):
    d = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z_]+):\s?(.*)$", line)
        if m and m.group(1) in COLS:
            d[m.group(1)] = m.group(2).strip()
    return d

def main():
    rows = [parse(f) for f in sorted(BOARD.glob("ch*.md"))]
    if not rows:
        print("(board empty — no board/ch*.md files yet)")
        return
    widths = {c: max(len(c), *(len(r.get(c, "-") or "-") for r in rows)) for c in COLS}
    line = lambda cells: "  ".join(str(v).ljust(widths[c]) for c, v in zip(COLS, cells))
    print(line(COLS))
    print(line(["-" * widths[c] for c in COLS]))
    for r in sorted(rows, key=lambda r: int(r.get("chapter", "0") or 0)):
        print(line([r.get(c, "-") or "-" for c in COLS]))

if __name__ == "__main__":
    main()
