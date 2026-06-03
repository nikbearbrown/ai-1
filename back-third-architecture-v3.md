# AI+1 — Back-Third Architecture (proposed TikTOC v3.0)

*Planning doc. What the deployment chapters and their appendices look like once
the Canvas export carries quizzes, case studies, glimmers, and Anki decks, and
the "Ask AI" loop is added to every surface.*

**Book dir:** `books/ai-1` · **Source of truth:** `chapters/*.md` (unchanged)

---

## The reframe — two axes, not one

The earlier plan treated the back third as a list of *export formats*. That
undersells it and makes it look like scope creep. The real structure is a
matrix: **content types** (authored once, in the source) projected onto
**surfaces** (produced by build scripts).

| Content type ↓ / Surface → | Kindle / PDF | Canvas (.imscc) | Anki | React site | Medhavy |
|---|---|---|---|---|---|
| Reading (chapter prose) | ✓ | page | — | page | page |
| Quizzes | inline | QTI quiz | cloze cards | component | tutor quiz |
| Case studies | inline | page/assignment | — | component | tutor case |
| Glimmers (AI-interrogated prompts) | inline | discussion/assignment | — | component | tutor activity |
| Spaced-repetition cards | appendix list | file resource | `.apkg` deck | component | scheduler |
| **Ask AI loop** | parallel LLM | IgniteAI | Ask AI (native) | embedded model | Ask AI (native) |

The book's claim becomes: **enrich once, ship everywhere, and the human stays in
the loop on every surface.** That last row — the Ask AI loop — is the thesis of
the whole book applied to the reader's own students.

**The one principle that must not break:** `chapters/*.md` stays the single
source. `.mdx`, `.tsx`, `.apkg`, `.imscc`, QTI XML — all are *build outputs*.
The author-instructor never hand-writes any of them.

---

## The structural fork to decide first

The content types in the matrix (quizzes, cases, glimmers, spaced-repetition
cards) have to **exist in the source** before any script can export them.
Two ways to author them:

- **Option A — Expand Chapter 10 (Enrichment).** Enrichment already generates
  the "With LLMs" layer. Widen its job to produce the full assessable + study
  set as structured blocks in the source. The deployment chapters then only
  *format* what already exists. Cleanest source-of-truth story; one new
  appendix of generators.
- **Option B — New generation chapter in Act Two.** A dedicated "Assessment &
  Study Layer" chapter between enrichment and deployment. More explicit, but
  adds a chapter and splits enrichment across two homes.

**Recommendation: A.** It keeps the spine intact — every deployment chapter
becomes a pure projection, which is exactly what makes the matrix teachable.
This doc assumes A below.

---

## Verifiability tiers (the honest part)

The book's rule — *scripts written and tested before the chapter is drafted* —
applies to every new deployment chapter. Not all of them can be tested in-house
to the same degree:

| Chapter | Build artifact | Can I test it here? |
|---|---|---|
| 13 Canvas | `build-imscc-standard.py` | **Yes — done.** Valid CC 1.3 package built from real source; manifest validated. Live Canvas import = your placeholder. |
| 14 Anki | `build-anki.py` | **Yes.** `.apkg` is a documented SQLite-in-zip format; I can build and validate a deck end-to-end. |
| 15 React | `build-react-site.py` | **Partly.** I can generate `.mdx`/`.tsx` and confirm a Next.js build compiles. A *deployed* example site is your step. |
| 16 Medhavy LTI | LTI 1.3 setup guide | **No.** Needs NEU IT registration, a Canvas sandbox, and FERPA review. This chapter is a pointer, not a tested build. |
| 17 Ask AI | per-surface config | **Partly.** The parallel-LLM prompt and config are testable; the in-platform behaviors (Ignite, Medhavy) are demonstrable, not unit-testable. |

Chapters 13, 14, and 17(prompt) are buildable now. 15 is buildable to the
scaffold line. 16 is the one chapter that is structurally a hand-off — which is
why its technical weight lives in the appendix and the Medhavy SDD, not the
chapter.

---

## Proposed chapter list (full book)

Front matter · Introduction unchanged. Acts One and Two (Ch 1–11) unchanged
**except** Ch 10 expands per the fork above.

**Act Three — Ship to every surface**

| # | Title | One-line | Status |
|---|---|---|---|
| 12 | Final Check & Build: EPUB + PDF | The book ships to Kindle; the build surfaces what the pipeline couldn't check. | Exists |
| 13 | Canvas Course Export: `.imscc` | Compile the enriched source into a Canvas course — pages, quizzes, cases, glimmers, syllabus — as one uploadable file, then refine with IgniteAI. | Script done; draft next |
| 14 | Spaced-Repetition Export: Anki | Compile the source's recall layer into Anki decks students study on a forgetting curve. | New |
| 15 | React Site Export: `.mdx` + `.tsx` | Compile the source into a Next.js-ready site scaffold — author runs the script, hands the rest to a developer. | New |
| 16 | Medhavy: the AI-Tutor Layer via LTI | What Medhavy adds on top of the Canvas course, the student experience, and what to hand a developer to wire the LTI 1.3 launch. | New (pointer) |
| 17 | Ask AI Everywhere | The same student question answered by whatever AI each surface provides — Ignite, Medhavy Ask AI, a parallel LLM for Kindle/PDF, an embedded model on the web — and how to keep it a human+AI loop, not an answer vending machine. | New (capstone) |

That's a 17-chapter book. Ch 17 is deliberately the capstone: it's the least
script-like and most argumentative chapter, and it closes the book on the same
note it opens — the fluency trap, now on the student's side of the desk.

---

## Proposed appendix map (80–99)

Appendices 80–89 are the existing pipeline tools (renumbered, Option C).
Deployment scripts take 90+:

| File | # | Contents | Status |
|---|---|---|---|
| 80–89 | 80–89 | Existing pipeline prompts/scripts (tiktoc … factcheck) | Renamed, stable |
| `90-appendix-imscc-standard.md` | 90 | `build-imscc-standard.py` — pure-Python `.imscc` builder | **Script written & tested** |
| `91-appendix-enrichment-artifacts.md` | 91 | Generators for quizzes, cases, glimmers, spaced-repetition cards (the Ch 10 expansion) | New |
| `92-appendix-anki.md` | 92 | `build-anki.py` — source recall layer → `.apkg` deck | New |
| `93-appendix-react-site.md` | 93 | `build-react-site.py` — `.md` → `.mdx` + `.tsx` scaffold | New |
| `94-appendix-medhavy-lti.md` | 94 | Medhavy LTI 1.3 setup guide (Sri's minimal viable sequence) + SDD pointer | New |
| `95-appendix-ask-ai.md` | 95 | Per-surface Ask AI config + the parallel-LLM prompt for Kindle/PDF | New |
| 96–98 | — | Reserved | — |
| `99-back-matter.md` | 99 | Back matter | Always 99 |

This drops the old `91-appendix-imscc-canvas.md` (the dead Ruby `canvas_cc`
path) and resolves the 91/92 contradiction from the prior summary by giving
each new script its own slot in chapter order.

> Note the difference from your June 3 summary: that map put Medhavy at 91/93
> and had no Anki, no Ask AI, and no enrichment-artifacts appendix. This map
> reorders to follow the new chapter sequence and the enriched-export strength
> you just named.

---

## The two new chapters that need the most thought

### Ch 17 — Ask AI Everywhere (the capstone)

The point isn't "every platform has an AI button." It's that the *same designed
question* gets a different engine per surface, and the author's job is to make
each one a human+AI loop rather than an answer dispenser:

- **Canvas → IgniteAI.** Already embedded. The author's lever is the course
  structure and the prompts seeded into pages — Ignite answers better when the
  `.imscc` gave it outcomes and context to stand on.
- **Medhavy → Ask AI (native).** Tutor with course memory; the richest loop.
- **Kindle / PDF → a parallel LLM.** No embedded AI in an EPUB. The book ships
  a *companion prompt* (Appendix 95) the reader pastes into Claude/ChatGPT/
  Gemini alongside the chapter — the "+1" the static format can't host.
- **React site → embedded model.** A chat component wired to an API; the
  developer's job, the author specifies the system prompt and guardrails.

The chapter's spine is the AI+1 argument turned outward: a tool that answers
without a loop produces fluent, decision-free mush — the same trap Chapter 1
named, now aimed at students. Verifiable parts: the parallel-LLM prompt, the
React system-prompt spec. Demonstrable-not-testable parts: Ignite/Medhavy
behavior.

### Ch 16 — Medhavy via LTI (the honest hand-off)

This is the one chapter that is *not* a build the reader runs. It stays at the
author-instructor altitude — what Medhavy adds, what the student sees, what to
hand the developer — and sends the OIDC/JWT/JWKS/NRPS/AGS detail to Appendix 94
and the Medhavy SDD. Gated behind NEU IT registration and a Canvas sandbox; it
ships as the only deployment chapter without an in-house-tested artifact, and
the chapter should say so plainly.

---

## Open decisions (yours)

1. **The fork:** expand Ch 10 to author the assessable/study layer (Option A,
   recommended), or add a dedicated generation chapter (Option B)?
2. **Anki scope:** standalone `.apkg` export only, or also attach the deck as a
   file resource *inside* the `.imscc` (you said the Canvas export should
   "include Anki files")? The second is a few lines added to the builder I
   already wrote.
3. **17 chapters** — does that count feel right, or should Anki fold into Ch 13
   as a section (it's the smallest of the new chapters)?
4. **Ch 16 altitude:** confirmed pointer-only, or does this book need to carry
   enough LTI that a developer could implement from it (which changes the
   reader)?

Once these are settled I produce TikTOC v3.0 against this map, then draft Ch 13
(already unblocked — script tested) and build/test the Anki and React scripts
before their chapters.
