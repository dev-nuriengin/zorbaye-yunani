# Chapter Tracker — Parallel Translation Protocol

This is the coordination system for translating *Zorba the Greek* into Kurmanji
**one chapter per agent, in parallel**. Read this fully before touching anything.

The whole point: **N agents work at the same time without ever disturbing each
other's work**, and a single **gated combine** step merges everything only after
you (the user) confirm.

---

## 0. The mental model

- The real source is `_RESOURCES/build_zorba.py`. Every chapter is a frozen
  `CHnn = r"""..."""` block in it, plus ONE token on the `ARTICLE = ...` line.
- `index.html` is **generated** — never merged, always rebuilt.
- Chapters 10–19 are done and frozen. Each new chapter (20, 21, 22, …) is one
  agent's whole job.
- **Golden rule:** only YOUR chapter is real work. Never re-translate or touch
  any other chapter's block. Never edit a file outside your own worktree.

## 1. Isolation — every agent works in its own git worktree

This is non-negotiable and is what makes parallel safe. **Do not edit
`build_zorba.py` in the main checkout** — if two agents do that, they clobber
each other.

```
EnterWorktree(name="ch<NN>")        # creates worktree-ch<NN>, branched from main
```
Your edits now live only in `.claude/worktrees/ch<NN>/`. They are invisible to
every other agent until combine. (If you have no EnterWorktree tool:
`git worktree add .claude/worktrees/ch<NN> -b worktree-ch<NN>`.)

## 2. Claim your chapter FIRST (race-free)

Before translating, **create your board file** so no one else takes your chapter:

```
_claude-files/chapter-tracker/board/ch<NN>.md
```
(Absolute path — always reachable, in the MAIN dir, regardless of your worktree.)
Each agent writes **only its own** `ch<NN>.md`. Never edit another chapter's file.
That single rule means there are zero write-races on the tracker.

Use the template in §7. Set `status: claimed` immediately, then start work.

## 3. The per-chapter job

1. Find chapter boundaries with pdfplumber: a chapter marker is a line whose
   stripped text is exactly the number `<NN>`. Your chapter runs from the `<NN>`
   marker to the `<NN+1>` marker. (Markers can sit mid-page; split there.)
2. Extract the English between markers. For each PDF page that *starts* inside
   the chapter, note its first sentence boundary → that becomes a `##PG <page>`
   marker (page = pdfplumber index `i` + 1).
3. Clean OCR junk (stray accented letters like `í`, footnote marks, `standing.
   behind` artifacts). Convert em-dashes **on the English side** to ` -- `.
4. Translate sentence-by-sentence into Hawar-Latin Kurmanji, Behdini-leaning,
   ~1:1 alignment. Match the register and quote style of existing chapters:
   `«` `»` outer speech, `‹` `›` nested. NO Turkish/Cyrillic glyphs (ı İ ğ ü …).
5. Append `CH<NN> = r"""..."""` **before** `def esc(s):`. Start it with
   `##PG <startpage>` then `##FIRST` (drop-cap). Use `##VERSE` for songs/poems.
6. Add `+ "\n" + build_article(<NN>, CH<NN>)` to the `ARTICLE = ...` line.
   (In your isolated branch this appends after the last existing block; final
   ordering is fixed at combine — see §6. That's expected, not a bug.)
7. Build: `python3 _RESOURCES/build_zorba.py`

## 4. Verification checklist (all must pass before `status: verified`)

- `class="ku"` count **==** `class="orig"` count.
- `<article>` open count == `</article>` close count.
- Your chapter's `data-page` markers ascend.
- No forbidden glyphs (`ı İ ğ ü`, Cyrillic, Arabic) in your CH block.
- No raw `—` on the English side (all ` -- `).
- `chapter-num` values are in order (gaps are fine pre-combine — see §6).

## 5. Status lifecycle (update YOUR board file as you go)

```
claimed      → you staked the chapter, starting
in-progress  → translating
built        → block appended, builds clean
verified     → passed the full checklist; AWAITING user confirmation to merge
merged       → integrated into main by the combine step
```

When you reach `verified`: **present `index.html` to the user and STOP.**
Do not commit, push, or merge. Wait for explicit confirmation (project rule:
questions ≠ instructions; nothing goes to git without an explicit "yes").

## 6. Combine — GATED, runs only on user confirmation

Because every chapter touches the same `ARTICLE` line and the same insertion
region, branches *will* conflict if naively git-merged — and `index.html` would
produce huge spurious conflicts. So we **don't git-merge**. Instead:

`combine.py` collects each chapter's `CH<NN>` block straight from its worktree,
assembles all blocks in numeric order onto a fresh copy of the generator,
rebuilds the `ARTICLE` line in order, regenerates `index.html`, and verifies.

```
# dry run (writes to a staging file, touches nothing):
python3 _claude-files/chapter-tracker/combine.py 20 21 22 23

# apply for real (only after you confirm every listed chapter is verified):
python3 _claude-files/chapter-tracker/combine.py 20 21 22 23 --in-place
```

After `--in-place`: review the diff, confirm ku==orig and chapter order
`…19 20 21 22 23`, then commit (one commit, personal account) per the user's
go-ahead. Worktrees can then be removed.

## 7. Board file template (`board/ch<NN>.md`)

```
chapter: <NN>
status: claimed
agent: <who you are / session label>
branch: worktree-ch<NN>
worktree: .claude/worktrees/ch<NN>
pdf_pages: r.<start>-r.<end>
sentences: -
verified: no
updated: <YYYY-MM-DD>
notes: |
  short free text — blockers, decisions, where you stopped
```

`python3 _claude-files/chapter-tracker/status.py` prints the whole board.

## 8. Ready-to-paste agent briefing (copy this per chapter)

> Project: /Users/nuriengin/Desktop/Dev/_Personal/zorbaye-yunani
> Read CLAUDE.md, then `_claude-files/chapter-tracker/PROTOCOL.md`. GIT_SCOPE: personal.
>
> You are translating **Chapter <NN>** only. Follow the protocol exactly:
> 1. `EnterWorktree(name="ch<NN>")` — work ONLY inside that worktree. Never edit
>    the main checkout's build_zorba.py; never touch any other chapter's block.
> 2. Create `_claude-files/chapter-tracker/board/ch<NN>.md` (template in §7),
>    status: claimed. Update only this file as you progress.
> 3. Find the `<NN>`→`<NN+1>` markers with pdfplumber; extract; clean OCR;
>    record `##PG` page markers.
> 4. Translate sentence-by-sentence (Hawar-Latin, Behdini-leaning, ~1:1, « »/‹ ›,
>    no Turkish/Cyrillic glyphs). Append `CH<NN>` block; add build_article(<NN>,
>    CH<NN>) to the ARTICLE line.
> 5. `python3 _RESOURCES/build_zorba.py`; run the §4 checklist; set status: verified.
> 6. Present index.html and STOP. Do NOT commit/merge. Wait for the user.
