#!/usr/bin/env python3
"""Combine parallel chapter branches into one generator, rebuild, verify.

GATED: only run this once the user confirms every listed chapter is `verified`.

Each chapter's real contribution is a self-contained `CHnn = r\"\"\"...\"\"\"` block
plus one `build_article(nn, CHnn)` on the ARTICLE line. Naive git-merging would
fight over that single line and over generated index.html. Instead we collect
each chapter's block from its worktree and reassemble deterministically.

For each chapter NN we look for its block in (first match wins):
  1. .claude/worktrees/chNN/_RESOURCES/build_zorba.py   (the agent's worktree)
  2. _RESOURCES/build_zorba.py                          (main, if already present)

Usage:
  python3 combine.py 20 21 22 23            # dry run -> staging file, touches nothing
  python3 combine.py 20 21 22 23 --in-place # rewrite main generator + rebuild
"""
import re, sys, subprocess, pathlib

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]                       # chapter-tracker -> _claude-files -> repo root
GEN = ROOT / "_RESOURCES" / "build_zorba.py"
STAGE = HERE.parent / "build_zorba.combined.py"   # dry-run output, never executed
BASE_CHAPTERS = list(range(10, 20))          # 10..19 are frozen in the base generator

def block_re(n):
    return re.compile(r'^CH%d = r"""\n.*?\n"""' % n, re.M | re.S)

def find_block(n):
    wt = ROOT / ".claude" / "worktrees" / f"ch{n}" / "_RESOURCES" / "build_zorba.py"
    for src in (wt, GEN):
        if src.exists():
            m = block_re(n).search(src.read_text(encoding="utf-8"))
            if m:
                return m.group(0)
    return None

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    in_place = "--in-place" in sys.argv
    extra = sorted({int(a) for a in args})
    if not extra:
        sys.exit("give chapter numbers, e.g.  combine.py 20 21 22 23 [--in-place]")

    base = GEN.read_text(encoding="utf-8")

    # Strip any already-merged chapters >= 20 from the base so we rebuild cleanly.
    for n in range(20, 100):
        base = block_re(n).sub("", base)
    base = re.sub(r"\n{3,}", "\n\n", base)

    # Collect the extra chapter blocks.
    blocks, missing = [], []
    for n in extra:
        b = find_block(n)
        (blocks.append((n, b)) if b else missing.append(n))
    if missing:
        sys.exit("ERROR: could not find CH block(s) for chapter(s): %s" % missing)

    # Insert collected blocks immediately before `def esc(s):`.
    anchor = "\ndef esc(s):"
    inject = "\n" + "\n\n".join(b for _, b in blocks) + "\n\n"
    out = base.replace(anchor, inject + anchor, 1)

    # Rebuild the ARTICLE line in full numeric order.
    order = BASE_CHAPTERS + [n for n, _ in blocks]
    article = "ARTICLE = " + ' + "\\n" + '.join("build_article(%d, CH%d)" % (n, n) for n in order)
    out = re.sub(r"^ARTICLE = .*$", article.replace("\\", "\\\\"), out, count=1, flags=re.M)

    target = GEN if in_place else STAGE
    target.write_text(out, encoding="utf-8")
    print("chapters combined: %s" % order)
    print("written: %s%s" % (target, "" if in_place else "  (dry run — main untouched)"))

    if not in_place:
        # Static, side-effect-free verification only. The generator hard-writes
        # repo-root index.html, so we must NOT execute it during a dry run —
        # that would clobber the live index.html the other agents depend on.
        import py_compile
        try:
            py_compile.compile(str(target), doraise=True)
            print("staging compiles: OK")
        except py_compile.PyCompileError as e:
            sys.exit("STAGING COMPILE ERROR:\n%s" % e)
        pairs = sum(1 for ln in out.splitlines() if "|||" in ln)
        m = re.search(r"^ARTICLE = .*$", out, re.M)
        art_order = re.findall(r"build_article\((\d+),", m.group(0)) if m else []
        print("KU/EN pairs in combined source: %d" % pairs)
        print("ARTICLE order: %s" % " ".join(art_order))
        print("(dry run complete — no build executed, index.html untouched)")
        return

    # --in-place is the real combine: run it only when the user confirms all
    # listed chapters are verified AND no agent is still editing main.
    res = subprocess.run([sys.executable, str(target)], cwd=str(ROOT),
                         capture_output=True, text=True)
    sys.stdout.write(res.stdout)
    sys.stderr.write(res.stderr)
    if res.returncode != 0:
        sys.exit("BUILD FAILED")
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    ku = html.count('class="ku"')
    orig = html.count('class="orig"')
    nums = re.findall(r'class="chapter-num">(\d+)', html)
    print("ku == orig: %s (%d / %d)" % (ku == orig, ku, orig))
    print("chapter order: %s" % " ".join(nums))

if __name__ == "__main__":
    main()
