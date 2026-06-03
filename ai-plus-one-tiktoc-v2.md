# AI+1: AI Native Personalized Textbooks
## Full TOC Draft — compiled from all phase outputs

**Working title:** AI+1: AI Native Personalized Textbooks
**Author:** Nik Bear Brown · ni.brown@neu.edu · Bear Brown & Company
**Series:** AI+1 · Bear Brown & Company
**Document:** Full TOC Draft — compiled from all phase outputs
**Version:** 3.0
**Status:** Drafting — Part One (Ch 1–12) is the pipeline; Part Two
(Ch 13–20) is the enriched layer, drafted from tested build scripts
(`build-imscc-standard.py`, `build-anki.py`, `build-react-site.py`).
Live Canvas/Anki imports, the React deploy, and Medhavy LTI
registration remain reader- or institution-side steps.

---

## Document structure

1. Book Concept and Thesis
2. Learner Profile
3. Book Type and Deployment Specification
4. Field Positioning
5. Three-Act Learning Arc
6. Prerequisite Map
7. Learning Outcomes by Chapter
8. Chapter-by-Chapter TOC
9. Chapter Anatomy Template
10. Case Study Strategy
11. Hard Topics, Contested Claims, Aging Risk
12. Open Questions

---

# PART 1 — BOOK CONCEPT AND THESIS

## Book concept summary

> This book teaches **author-instructors to build an AI+1 style
> textbook** — domain-specific, AI-native, and shippable to every
> surface a learner uses — in two parts. **Part One** walks them
> through a structured pipeline that starts with a two-hour Tic TOC
> session to produce a TIKTOC.md, hands off to Cowork (or Codex)
> for automated drafting, repositions the human as editor making
> small refinements until a production-quality EPUB and PDF comes
> off the build script, and ships the book to Kindle. **Part Two**
> shows that the same single markdown source carries an *enriched
> layer* — quizzes, case studies, glimmers, and spaced-repetition
> cards — and compiles to every surface from one source: a Canvas
> course (`.imscc`), an Anki deck (`.apkg`), a React/Next.js site,
> and the Medhavy AI-tutor layer — with an Ask-AI loop on each. It
> fills the gap left by generic AI writing tools (undifferentiated
> output) and traditional textbook publishing (slow, expensive,
> institution-bound). It succeeds if **the reader finishes with
> their own AI+1 textbook live on KDP, the enriched artifacts
> generated from the same source, and at least one course surface
> deployed — understanding exactly where their judgment is required
> and where the pipeline runs without them.**

**One-sentence logline:**
The TIKTOC.md session is not overhead — it is the product;
everything downstream is execution.

**Part Two logline:**
Enrich once, ship everywhere — one source becomes a book, a course,
a deck, a site, and a tutor, and the human+AI loop survives on each.

## Central thesis

"This book argues that the TIKTOC.md session — two hours of
structured conversation with Tic TOC before any writing begins —
is the highest-leverage step in building an AI+1 textbook, which
means that author-instructors who skip it and go straight to
Cowork are producing Cowork dumps rather than books, and this
matters because an AI+1 textbook built on a vague outline teaches
students to produce the same kind of generic output the fluency
trap produces in every other domain."

## Thesis test

The TOC reflects the thesis at every act:

- ACT ONE: The fluency trap is felt before it is named. The
  reader catches what the model missed in their own domain.
  The Tic TOC architecture is explained as the structural
  response to that failure. ✓
- ACT TWO: Every pipeline chapter shows what happens when
  the step is done well vs. done badly. The TIKTOC.md
  comparison in Chapter 4 is the thesis made concrete. ✓
- ACT THREE: The human rewrite is the seam. The AI+1
  standard is the final check. The book ships to Kindle. ✓
- PART TWO: The same source carries the enriched layer and
  compiles to every surface. The fluency trap returns one last
  time in Chapter 20 — now on the *student's* side of the desk —
  and the reader's job becomes keeping a human+AI loop, not a
  vending machine, on each surface. ✓

**Thesis test: PASS**

---

# PART 2 — LEARNER PROFILE

## Primary reader

An author-instructor — a domain expert in a freelance profession
with one primary client relationship who wants to build a
Kindle-ready AI+1 textbook for their students or peers, using
Claude and a structured pipeline, without institutional backing
or a technical co-author.

**Specific person:** A graphic designer with ten years of
client work who teaches workshops or courses on the side,
has heard that AI is changing their field, wants to build
a short practical textbook for their students, and has never
written a textbook before.

## Prior knowledge assumed

- Deep domain expertise in a specific field
- Basic Claude or ChatGPT familiarity (can run a prompt,
  read output, iterate once)
- GitHub or file system comfort at the basic level

## Prior knowledge NOT assumed

- Python or Node.js installed or familiar
- Markdown fluency
- Instructional design background
- Prior textbook writing experience
- Publishing knowledge
- LMS administration experience

## Prior misconceptions

1. "I can start with a Cowork prompt and clean it up later" —
   the TIKTOC.md comparison in Chapter 4 shows what this
   produces and why it is harder to fix than to prevent
2. "The AI does the writing" — the human rewrite is the gate;
   the pipeline produces a draft worth rewriting, not a
   finished book
3. "Figures and enrichment come first" — the pipeline
   enforces text stability before figures; adding figures
   to unstable text is waste
4. "A $1 Kindle book is not a real book" — the AI+1 series
   is specifically designed for this format; the price point
   is a pedagogical and distribution decision, not a quality signal
5. "Canvas deployment requires IgniteAI or the API" — the
   .imscc build compiles a single file the professor uploads
   via Settings → Import Course Content; no API access required.
   IgniteAI is the *refinement* tool used after import, not the
   build tool
6. "A book is enough" — a printed/EPUB book is a one-way
   surface; the enriched layer (quizzes, cases, glimmers,
   recall cards, Ask-AI loop) is what makes the student
   practice, retrieve, and defend their thinking
7. "Medhavy is another export I run myself" — Medhavy is a
   hosted AI-tutor layer Canvas launches into via LTI 1.3;
   it is the one target the author specifies and hands to a
   developer and the institution, not a file they build alone

## Motivation type

Professional (wants to teach their domain effectively) and
intellectual (curious about what AI+1 means for their field).
The pipeline is designed for a solo author-instructor who is
also running a practice or teaching load — it respects their
time by front-loading judgment and automating execution.

---

# PART 3 — BOOK TYPE AND DEPLOYMENT SPECIFICATION

## Book type

**PRIMARY TYPE:** Practitioner handbook — chapters organized
by pipeline stage, each chapter self-contained enough to
return to, the book usable as a reference after the first
build is complete.

**NOT:** Course textbook (chapters are not week-by-week
lessons), field-defining monograph (the argument is made
in two chapters; the rest is execution).

## Deployment specification

**Primary adoption context:**
Self-directed build project. The author-instructor works
through the pipeline at their own pace — steady workers
complete in 4–6 weeks; those also teaching may take a semester.

**Secondary adoption context:**
Humanitarians AI workshops — fellows learning the pipeline
use this book as the workshop companion. The domain research
chapter (Chapter 3) and the Tic TOC chapter (Chapter 4)
are the workshop's primary focus.

**What the book is explicitly NOT designed for:**
Undergraduate courses, PhD seminars, readers who want to
understand AI+1 theoretically without building anything,
readers who want a co-author rather than a pipeline.

**How the TOC signals book type:**
Twenty chapters in two parts. Part One (1–12) is the build
sequence — each chapter ends with a concrete deliverable and
begins with the problem the step solves. Part Two (13–20) is
the enriched layer — each chapter explains one artifact or
surface and ends by pointing at the script or prompt that
produces it. A reader scanning the titles sees a build
sequence and a deployment matrix, not a curriculum. The
running example (ai-for-designers) appears in every chapter
as a completed artifact beside the reader's own in-progress work.

---

# PART 4 — FIELD POSITIONING

## The gap this book fills

No book currently teaches the complete AI+1 textbook
production pipeline — from domain research brief through
Tic TOC session through Cowork draft through human rewrite
through Kindle submission — *and then* the enriched layer
that ships the same source to a Canvas course, an Anki deck,
a React site, and an AI-tutor layer — to a solo
author-instructor with deep domain expertise and no technical
background.

Generic AI writing guides teach prompt engineering, not
instructional architecture. Traditional textbook writing
guides assume institutional support, co-authors, and a
multi-year timeline. The pipeline this book teaches produces
a Kindle-ready rough draft in 4–6 weeks and — from the same
single source — a course, a deck, a site, and a tutor layer,
each carrying quizzes, cases, glimmers, and recall.

## Positioning statements

**vs. generic AI writing guides:**
"Unlike AI writing guides that teach prompt engineering
for general content, this book teaches the structured
pipeline — from TIKTOC.md through Cowork through human
rewrite — that produces a domain-specific, AI-native
textbook rather than a Cowork dump."

**vs. traditional textbook writing guides:**
"Unlike traditional textbook writing guides that assume
institutional backing and multi-year timelines, this book
produces a Kindle-ready rough draft in 4–6 weeks and — from
the same source — a course, a deck, a site, and a tutor layer."

**vs. tool-first / IgniteAI-first workflows:**
"Unlike clicking IgniteAI inside Canvas to generate a course
one prompt at a time, this book produces the *specification*
first — outcome-aligned, enriched, single-source — so the
course is built from a design, not assembled by guesswork.
IgniteAI then refines what the source already built."

---

# PART 5 — THREE-ACT LEARNING ARC

## The arc statement

This book takes the reader from **domain expert who has
heard of AI but hasn't built anything with it** to
**author-instructor who has a Kindle-ready AI+1 textbook
live on KDP and the same source deployed across course,
deck, site, and tutor surfaces** in two parts. PART ONE
(the three-act pipeline) first establishes what AI is doing
to their profession and why the AI+1 architecture protects
their identity (Act One), walks them through the pipeline
that produces a rough draft (Act Two), and repositions them
as the editor and publisher who takes that draft to a
Kindle-ready book (Act Three). PART TWO then shows that the
finished source is not just a book: it carries an enriched
layer (quizzes, cases, glimmers, recall cards) and compiles
to every surface — Canvas, Anki, a React site, and the
Medhavy tutor — with an Ask-AI loop on each.

## Act One — Establish (Chapters 1–2)

**Starting state:** Domain expert. Curious about AI.
No textbook writing experience.

**Ending state:** Reader can explain what AI+1 is, name
the irreducibly human layer in their domain, deploy Tic TOC,
and explain why the TIKTOC.md session comes before any
Cowork prompt runs.

**Inciting question:** I understand what this is and why
it works. How do I actually build one?

**Act One → Act Two transition condition:**
Reader can look at a TIKTOC.md and name what each section
does and what would go wrong downstream if it were vague.

## Act Two — Build (Chapters 3–7)

**Starting state:** Reader understands the AI+1 architecture.
Ready to execute the pipeline.

**Ending state:** Complete Cowork rough draft in chapters/.
Every chapter drafted. No BLOCKED chapters unresolved.
Reader has read two chapters against the Combined Test.

**Hardest moment:** Chapter 4 — the two-hour Tic TOC session.
The only chapter in Act Two that cannot be executed as a
command. Requires sustained judgment.

**Act Two → Act Three transition condition:**
Complete Cowork draft exists. Reader has read two chapters
against the Combined Test and knows what the draft is and
what it is not.

## Act Three — Apply (Chapters 8–12)

**Starting state:** Rough draft exists. Reader is ready
to stop executing the pipeline and start owning the book.

**Ending state:** Kindle-ready EPUB and PDF live on KDP.
Reader understands the rebuild loop and has assessed the
finished book against the AI+1 standard. Part One is complete.

## Part Two — Enrich and Deploy (Chapters 13–20)

**Starting state:** A finished, single-source book exists —
a one-way surface.

**Ending state:** The same source carries the enriched layer
and is compiled to the surfaces the reader chose — a Canvas
course (`.imscc`), an Anki deck (`.apkg`), a React site, and/or
the Medhavy tutor layer — each with an Ask-AI loop. The reader
can name which deployment targets they can finish alone (Canvas,
Anki), which need a developer (React), and which need the
institution (Medhavy/LTI).

## The running example across the arc

| Chapter | Running example artifact |
|---------|--------------------------|
| 1 | AI-generated design brief — fluency trap annotated |
| 2 | ai-for-designers TIKTOC.md excerpt — product before process |
| 3 | Domain research brief for design — full prompt output |
| 4 | Complete ai-for-designers TIKTOC.md — built live |
| 5 | ai-for-designers directory — scaffold output annotated |
| 6 | One pantry notes file — ai-for-designers Chapter 3 |
| 7 | One Cowork chapter draft — annotated before/after |
| 8 | Two versions of one paragraph — Cowork vs. human rewrite |
| 9 | One chapter before and after finishing pipeline |
| 10 | Bad LLM Exercise vs. good LLM Exercise — same chapter |
| 11 | One CAJAL figure — decided out loud |
| 12 | KDP dashboard — ai-for-designers submission |
| 13 | One ai-for-designers chapter shown as page, quiz, case, glimmer, and recall card |
| 14 | A teaching case generated for ai-for-designers — client AI-disclosure dilemma |
| 15 | A glimmer that makes a student defend a layout decision against an AI |
| 16 | ai-for-designers recall deck — Q:/A: cards compiled to .apkg |
| 17 | ai-for-designers .imscc — modules/pages from build-imscc-standard.py (15 modules, 32 pages) |
| 18 | ai-for-designers React scaffold — build-react-site.py (41 files → 89 generated) |
| 19 | The Medhavy launch from a Canvas module item — student lands in the tutor, already in context |
| 20 | The same question across IgniteAI, Medhavy, a parallel LLM, and the React panel |

---

# PART 6 — PREREQUISITE MAP

| Prerequisite | Safe to Assume? | Where Addressed |
|---|---|---|
| Domain expertise | Yes | — |
| Basic Claude familiarity | Probably | Chapter 1 |
| File system comfort | Probably | Chapter 5 |
| Python installed | No | Chapter 5 sidebar |
| Node.js installed | No | Chapter 9 sidebar (figures); needed again Ch 18 (React, developer) |
| Markdown fluency | No | Chapter 5 sidebar |
| Cowork (or Codex) access | No | Chapter 7 |
| Instructional design background | Explicitly not required | Tic TOC handles it |
| Prior textbook experience | Explicitly not required | Pipeline handles it |
| Canvas access (a sandbox) | No | Chapter 17 sidebar |
| A developer (React site) | No | Chapter 18 — hand-off chapter |
| Institutional LTI registration / IT | No | Chapter 19 — institution's step |

**Front-loading decision:** Python, Node.js, Markdown, and
Canvas access addressed at first use via one-page sidebars.
The book's single-source pipeline (Part One) needs nothing
beyond Python and a browser. Part Two's surfaces escalate in
who must act: Canvas and Anki the author finishes alone; the
React site needs a developer (Ch 18); the Medhavy tutor needs
the institution (Ch 19). No Ruby anywhere — the dropped
`canvas_cc` path is gone.

**Load-bearing chapters:**
- Chapter 4 (TIKTOC.md): FATAL to skip. All downstream
  Cowork runs depend on it.
- Chapter 7 (Cowork Draft): FATAL to skip. Human rewrite
  cannot happen without a draft.
- Chapter 8 (Human Rewrite): No automated enforcement.
  Author's judgment is the only gate.
- Chapter 12 (KDP): closes Part One. The book ships here.
- Part Two (Ch 13–20): each deployment chapter is optional and
  independent — pick the surfaces your students use. Chapter 13
  (the enriched-layer opener) is the one Part Two chapter worth
  reading regardless of which surfaces you ship to.

---

# PART 7 — LEARNING OUTCOMES BY CHAPTER

| Chapter | Title | Bloom's Ceiling | Create-level outcome |
|---------|-------|----------------|----------------------|
| 1 | What AI+1 Is and Why It Works | Evaluate | — |
| 2 | What Tic TOC Does | Evaluate | — |
| 3 | Domain Research | Create | Domain research brief |
| 4 | Generating Your TIKTOC.md | Create | Complete TIKTOC.md |
| 5 | Book Scaffold | Apply | — |
| 6 | Research Pass | Evaluate | — |
| 7 | Chapter Writing | Evaluate | — |
| 8 | The Human Rewrite | Create | Revised chapter, Combined Test passed |
| 9 | Finishing Pass and Figures | Apply | — |
| 10 | Enrichment: The LLM Layer | Evaluate | — |
| 11 | Creating Figures | Apply | — |
| 12 | Final Check and Build: EPUB + PDF | Evaluate | — |
| 13 | The Enriched Layer: Beyond the Book | Understand | — |
| 14 | Case Studies | Create | A vetted teaching case |
| 15 | Glimmers: AI-Interrogated Prompts | Create | A runnable glimmer |
| 16 | Spaced Repetition: Anki | Create | A built .apkg deck |
| 17 | Canvas Course Export: .imscc | Create | Working .imscc imported into Canvas |
| 18 | The React Site: .mdx + .tsx | Apply | Scaffold generated + hand-off brief |
| 19 | Medhavy: AI-Tutor Layer via LTI | Evaluate | — (spec + developer hand-off) |
| 20 | Ask AI Everywhere | Evaluate | — |

Create-level outcomes concentrated at the three
highest-judgment Part One steps (domain research brief Ch 3,
TIKTOC.md Ch 4, human rewrite Ch 8) and the Part Two artifacts
the reader authors and ships (case Ch 14, glimmer Ch 15, deck
Ch 16, course Ch 17).

---

# PART 8 — CHAPTER-BY-CHAPTER TOC

---

# PART ONE — MAKE THE BOOK (Chapters 1–12)
*The pipeline: from domain research and a Tic TOC session, through
the Cowork (or Codex) draft and the human rewrite, to a finished
book live on Kindle. Three acts.*

---

## ACT ONE — ESTABLISH (Chapters 1–2)
*Establishes the AI+1 framework and the Tic TOC architecture
before the pipeline begins.*

---

### CHAPTER 1 — What AI+1 Is and Why It Works

**One-line:** Students learn to identify what AI is doing
to their profession, name the irreducibly human layer, and
explain why AI+1 preserves professional identity rather
than replacing it.

**Opening:** An AI-generated design brief — polished,
professional-looking, wrong about the client relationship.
The reader catches what the model missed. Framework arrives
after the reader has already demonstrated the irreducibly
human layer.

**Core content blocks:**
1. The fluency trap — what it looks like in a freelance
   design context; why it is dangerous because it is convincing
2. The AI+1 frame — domain expert plus AI fluency; the PwC
   wage premium as evidence the frame is economically real
3. The irreducibly human taxonomy for freelance professions —
   client judgment, taste calibration, relationship continuity,
   creative accountability
4. The three-LLM research prompt — structure, how to run it,
   how to combine outputs
5. What to do with the research output — the domain research
   brief as primary input to the Tic TOC session

**Worked example:** Three-LLM research prompt run for
graphic design — full synthesized output annotated.

**Assessable exercises (3):**
1. (Apply) Run the three-LLM domain research prompt for
   your own field.
2. (Analyze) Identify three fluency trap examples in your
   domain from the research output.
3. (Evaluate) Assess whether AI is creating a wage premium
   or displacement risk in your field.

**Bridge:** The fluency trap is felt and named. The Tic TOC
architecture is the structural response. Chapter 2 explains
why two hours there is the right first move.

---

### CHAPTER 2 — What Tic TOC Does and Why You Spend Two Hours Here First

**One-line:** Students learn what Tic TOC's three disciplines
enforce, how to deploy it, and why the TIKTOC.md session is
the highest-leverage step in the pipeline.

**Opening:** The ai-for-designers TIKTOC.md shown in full
before the chapter explains how it was produced. The reader
sees the product. The chapter works backward.

**Core content blocks:**
1. What a TIKTOC.md is and is not — instructional architecture
   vs. author's outline
2. The three disciplines — curriculum theorist, acquisitions
   pragmatist, instructional designer; what each catches
3. The phase gates — why each exists, what breaks if skipped,
   what confirming actually means
4. How to deploy Tic TOC — copy prompt, Claude Project,
   Instructions, /help, /i1; five-minute setup
5. What the session feels like — conversation not form;
   pushback, reframe, direct disagreement; what to do
   when Tic TOC asks for a capability statement

**Worked example:** One phase gate conversation from the
ai-for-designers session — /i3 audience intake, pushback
on vague learner profile, resolution.

**Assessable exercises (3):**
1. (Apply) Deploy Tic TOC. Confirm /help appears. Begin /i1.
2. (Analyze) Identify two phase gate decisions in the
   TIKTOC.md excerpt. Name what Cowork would produce
   differently if each were vague.
3. (Evaluate) Write 200 words responding to: "I don't
   need Tic TOC — I know what my book is about."

**Bridge:** Tic TOC is deployed. Before /i1 is productive,
domain research must be in hand. Chapter 3 produces it.

---

## ACT TWO — BUILD (Chapters 3–7)
*Walks the pipeline from domain research to Cowork draft,
one step per chapter, running example live throughout.*

---

### CHAPTER 3 — Domain Research: The Chapter Before the Chapter

**One-line:** Students write, run, and synthesize a
structured domain research prompt across three LLMs,
producing a brief ready for the Tic TOC intake session.

**Opening:** Three LLM responses to the same domain
research prompt — same question, three different answers.
Agreement, divergence, contested claims visible immediately.

**Core content blocks:**
1. Why three LLMs — what each does differently; why
   synthesis is stronger; where each overreaches
2. The domain research prompt structure — eight sections;
   how to adapt to any freelance profession
3. How to combine outputs — agreement as settled,
   divergence as contested, gaps as research holes
4. The fluency trap check — how to read LLM research
   for authoritative-sounding claims that fail expert review
5. What makes a brief ready for /i1 — the four things
   Tic TOC will ask that the brief must already answer

**Worked example:** Complete domain research brief for
ai-for-designers — synthesized from three LLM outputs,
annotated to show provenance of each claim.

**Assessable exercises (3):**
1. (Apply) Adapt the template to your field. Run in
   Claude, GPT, and Gemini. Save all three outputs.
2. (Analyze) Produce a 600–800 word synthesis. Mark each
   claim: ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY.
3. (Create) Produce a domain research brief in four-section
   format ready for /i1.

**Bridge:** Domain research brief exists. Chapter 4 walks
through the complete Tic TOC session with this brief as
primary input.

---

### CHAPTER 4 — Tic TOC: Generating Your TIKTOC.md

**One-line:** Students complete the full Tic TOC pipeline
and produce a TIKTOC.md that Cowork can execute without
a clarifying conversation.

**Opening:** The question Tic TOC asks at /i1 Question 2:
"In one sentence — not a paragraph — what does the reader
LEARN?" Most authors discover here they do not yet know
what their book is.

**Core content blocks:**
1. Phase One walkthrough (/i1–/i4) — annotated transcript
   excerpts; what Tic TOC looks for; what weak answers
   look like; what pushback sounds like
2. Phase Two walkthrough (/l1–/l4) — outcomes in Bloom's;
   sequencing model; three-act arc; prerequisites resolved
3. Phase Three walkthrough (/c1–/c4) — one chapter
   documented in full; keyword audit; capability statement
   vs. topic heading; bridge question as structural commitment
4. The /g2 diagnostic — run on ai-for-designers TIKTOC.md;
   what it found; what was fixed before Cowork handoff
5. What "ready for Cowork" means — specific checklist;
   BLOCKED item in /p2; when to resolve, when to flag

**Worked example:** Side-by-side comparison of two TIKTOC.md
chapter specs — one after a rushed session, one after a
full session with pushback honored. Cowork output for each
shown. The difference is the argument.

**Assessable exercises (5):**
1. (Apply) Complete /i1–/i4. Share confirmed Book Concept
   Summary.
2. (Apply) Complete /l1–/l4. Produce outcome map table.
3. (Apply) Document three chapters using /c1. Each must
   have capability statement and bridge question.
4. (Evaluate) Run /g2. Name highest-risk failure mode
   and one structural change that mitigates it.
5. (Create) Produce complete TIKTOC.md — all chapters
   documented, /g2 passed, /p2 current.

**Bridge:** TIKTOC.md exists. Cowork needs a directory
to write into. Chapter 5 creates it in thirty seconds.

---

### CHAPTER 5 — Book Scaffold: new_book.py

**One-line:** Students run new_book.py to scaffold their
book directory and understand what each generated file
does and who reads it.

**Opening:** The terminal command and its output — forty
lines, thirty seconds. Then: what just happened and why
each piece matters.

**Core content blocks:**
1. Python install sidebar — three commands, five minutes,
   Mac/Windows/Linux; move on
2. The command and its arguments — what each controls
3. What Cowork reads at runtime — TIKTOC.md, book.md,
   pantry/; must be populated before Cowork runs
4. What the human uses — vision.md, architecture.md,
   chapters-spec.md, risks.md, outline.md
5. The build script — what build.sh does; output/;
   why gitignored

**Worked example:** Complete directory output for
ai-for-designers — every file listed with one-line
description and who reads it. metadata.yaml shown
fully populated.

**Assessable exercises (3):**
1. (Apply) Run new_book.py for your book. Confirm
   directory created and structure matches diagram.
2. (Apply) Populate metadata.yaml. Confirm title,
   subtitle, author, publisher correct.
3. (Analyze) Open TIKTOC.md. Confirm chapter list
   from Tic TOC session is present. Name which file
   Cowork reads first.

**Bridge:** Directory exists. TIKTOC.md in place.
Cowork needs research notes per chapter. Chapter 6
populates the pantry.

---

### CHAPTER 6 — Research Pass: Pantry Population

**One-line:** Students run the Chapter Research Gatherer
and evaluate the pantry output — distinguishing
research-ready chapters from thin ones needing supplementation.

**Opening:** A pantry notes file that looks thorough and
isn't — aggregator summaries, no primary sources, wrong
domain examples. Then the same chapter's notes after a
proper research pass. The reader learns the difference.

**Core content blocks:**
1. What the Chapter Research Gatherer does — reads TIKTOC.md,
   scans shared library, web research per chapter, nine-section
   notes file
2. How to evaluate a notes file — four questions before
   accepting as draft-ready
3. Thin-pantry chapters — causes, options (supplement,
   accept flag, return to Tic TOC)
4. The shared markdown library — what it is, _lib_ prefix,
   what gets copied
5. What pantry is not — reference not citation; primary
   sources still required in chapter drafts

**Worked example:** Complete pantry notes file for
ai-for-designers Chapter 3 — all nine sections,
strong vs. weak entries annotated.

**Assessable exercises (3):**
1. (Apply) Run Chapter Research Gatherer. Confirm one
   notes file per chapter in pantry/.
2. (Analyze) Read two notes files. For each: strongest
   primary source, one claim needing verification, whether
   domain examples match target reader.
3. (Evaluate) Flag thin-pantry chapters. For each:
   supplement / accept / return to Tic TOC with reasoning.

**Bridge:** Pantry populated. Cowork can draft. Chapter 7
runs the draft and explains how to read what comes back.

---

### CHAPTER 7 — Chapter Writing: The Cowork Draft Run

**One-line:** Students run the Chapter Writer prompt and
evaluate the rough draft output — identifying what it did
well, what it got wrong, and what the human rewrite must supply.

**Opening:** The log.csv after a complete run — fourteen
chapters, everything green. The reader opens one chapter
and reads it. What they find is the real opening.

**Core content blocks:**
1. What the Chapter Writer does — reads TIKTOC.md and
   book.md, audits chapters/, reads pantry, drafts in
   Attenborough × Feynman voice; eight-section structure
2. The Attenborough × Feynman voice — scene-first,
   first-principles, named trade-offs, scale oscillation;
   why it is the default
3. Five things Cowork reliably gets wrong — voice drift,
   fabricated specificity, missing domain judgment, padded
   middle, bridge questions that don't bridge
4. The [verify] flag — what triggers it, what to do,
   why it is honesty not failure
5. BLOCKED chapters — causes, resolution, when to proceed
   with flag

**Worked example:** One complete Cowork chapter draft for
ai-for-designers — five failure modes annotated where they
appear. Then: human rewrite of opening paragraph. Reader
sees exactly what Chapter 8 asks.

**Assessable exercises (3):**
1. (Apply) Run Chapter Writer. Confirm one .md per chapter,
   logged in log.csv.
2. (Analyze) Read two drafts. Annotate five failure modes.
   Count [verify] flags.
3. (Evaluate) Rate each draft: SOLID FOUNDATION or NEEDS
   PANTRY WORK. For NEEDS PANTRY WORK, identify the pantry
   gap that caused it.

**Bridge:** Rough draft exists. The pipeline hands off to
the human author now. Chapter 8 is different. There is
no command to run.

---

## ACT THREE — APPLY (Chapters 8–12)
*Repositions the reader as author and publisher.
The pipeline stops running automatically. The book ships to Kindle.*

---

### CHAPTER 8 — The Human Rewrite: The Seam

**One-line:** Students learn to read a Cowork draft as
an author, identify what requires human judgment, and
produce a revised draft that passes the Combined Test
in their own voice.

**Opening:** Two versions of the same paragraph — Cowork
draft and author's rewrite — side by side. No explanation.
The reader identifies what changed. Then: the chapter names
what they just noticed and explains why the model could not
have produced the second version.

**Core content blocks:**
1. What the seam means — why this chapter is different;
   pipeline does not enforce this gate; what happens to
   Chapters 9–13 if it is skipped
2. Five failure modes as rewrite targets — not diagnostic
   now but prescriptive; what to replace each with
3. The Combined Test — fourteen items; what each tests;
   what pass vs. fail looks like; two hardest to self-assess
4. Pointer to writing-guide — what it covers; when to reach
   for it; most relevant chapters for practitioner handbook
5. The rewrite loop — how many passes typically; when to
   stop; finished vs. avoided

**Worked example:** One chapter rewrite in three passes —
Cowork draft, first-pass (structure fixed, voice generic),
second-pass (voice present, Combined Test passed). Delta
between each annotated.

**Assessable exercises (3):**
1. (Evaluate) Apply Combined Test to one chapter. Score
   all fourteen items. Identify three lowest-scoring.
2. (Apply) Rewrite opening section of one chapter. Must
   pass items 1, 2, 3, and 13 of Combined Test.
3. (Create) Produce complete revised chapter passing all
   fourteen Combined Test items. Note passes required.

**Bridge:** Text is the author's. Figures can now be added
to stable text. Chapter 9 runs the finishing pipeline.

---

### CHAPTER 9 — Finishing Pass and Figures

**One-line:** Students run the finishing pipeline —
subtitle pass, CAJAL figure intelligence, SVG generation,
enrichment — and evaluate output against the AI+1 visual
standard.

**Opening:** A chapter before and after the finishing
pipeline — same prose, but the after version has a
subtitle surfacing the chapter's central tension, visual
comments at the right moments, and figures that serve
the argument.

**Core content blocks:**
1. Node.js install sidebar — three commands, five minutes,
   Mac/Windows/Linux; move on
2. The Chapter Finishing Pass — subtitles and visual
   placeholder comments; good subtitle vs. topic heading
3. CAJAL Image Suggest — what it detects (MC, VG, PQ);
   what a cajal.md file contains; how to read priority
   rankings before running SVG generator
4. CAJAL SVG Generator + enrichment — SVG → PNG;
   enrichment pass; D3 HTML files in d3/
5. Pointer to ai-for-graphs and ai-for-infographics —
   what they cover; when to reach for them

**Worked example:** One chapter through full finishing
pipeline — cajal.md shown, SVG shown, enriched chapter
shown. Annotated for which CAJAL suggestions were used
as-is vs. modified.

**Assessable exercises (3):**
1. (Apply) Run Chapter Finishing Pass. Confirm each chapter
   has subtitle and at least two visual placeholder comments.
2. (Apply) Run CAJAL Image Suggest. Open one cajal.md.
   Confirm Critical-ranked figure matches chapter's primary
   learning outcome.
3. (Apply) Run CAJAL SVG Generator and enrichment pass.
   Confirm at least one PNG per chapter and d3/ populated.

**Bridge:** Figures in place. Book visually complete.
Chapter 10 adds the AI+1 layer that makes this a native
AI textbook.

---

### CHAPTER 10 — Enrichment: The LLM Layer

**One-line:** Students run the enrichment pipeline to add
domain-specific, hands-on LLM integration to every chapter
and evaluate whether the result meets the AI+1 standard.

**Opening:** Two LLM Exercises for the same chapter —
generic (could appear anywhere) vs. AI+1 (only makes
sense for this domain, this reader, this career stage).
The fluency trap returns at the pedagogy scale. Again.

**Core content blocks:**
1. The AI+1 standard for LLM Exercises — domain-specific,
   hands-on; the test: could this appear in a different
   field's textbook unchanged? If yes, it fails.
2. Dig Deeper vs. LLM Exercises — placement, purpose,
   deliverable
3. The "With LLMs" Curriculum Enrichment Generator —
   three phases: detect state, generate Chapter 00,
   propose running projects, enrich all chapters
4. The AI Wayback Machine — why historical figures matter;
   diversity tracking; Wikipedia instruction
5. Fluency trap at pedagogy scale — how to audit for
   generic exercises; failure patterns; how to revise

**Worked example:** Chapter 00: Claude Basics for
ai-for-designers — full onboarding chapter annotated
for what makes it AI+1 vs. what would make it generic.

**Assessable exercises (3):**
1. (Apply) Run enrichment generator. Select running project.
   Confirm Chapter 00 generated.
2. (Evaluate) Read three LLM Exercises. Apply AI+1 test
   to each. Flag any that fail.
3. (Apply) Revise one failing LLM Exercise. Name the
   domain knowledge added and why no generic prompt
   could supply it.

**Bridge:** LLM layer in place. Book content-complete.
Chapter 11 addresses the figure craft underneath the
pipeline.

---

### CHAPTER 11 — Creating Figures

**One-line:** Students learn to decide what a single figure
is allowed to contain — using the SCOPE framework and the
component ceiling — so that every figure teaches rather
than clutters.

**Opening:** A designer-author types a prompt and gets a
beautiful, unusable 14-component diagram. The chapter works
backward from the failure to the discipline that prevents it.

**Core content blocks:**
1. The component ceiling — Cowan's four-chunk limit;
   why six-to-eight is the working budget; the
   comprehensiveness vs. comprehension trade-off
2. SCOPE — five parameters; why the exclusion list is more
   important than the inclusion list; silent vs. interactive
   mode; the gate CAJAL holds hardest
3. The two palettes — Okabe-Ito for publication-neutral
   figures; Bear Brown / Brutalist D3 for the series house
   style; one rule that governs both (grayscale test)
4. What the pipeline produces — SVG as source, PNG as
   publication artifact, D3 HTML as authorable source;
   no text labels in the generated image
5. Worked example decided out loud — one figure, all five
   SCOPE decisions made explicit, exclusion list written

**Worked example:** Chapter 7 of ai-for-designers through
a complete CAJAL interactive session — SCOPE built live,
figure generated, output evaluated.

**Assessable exercises (3):**
1. (Apply) Write the exclusion list for one figure before
   generating it. Minimum five items with one-clause
   justifications.
2. (Apply) Run one figure through the five SCOPE gates.
   Produce complete SCOPE block. Confirm component count
   is eight or fewer.
3. (Apply) Test one rendered figure in grayscale. For each
   data-encoding color: name luminance band, confirm
   distinguishability, add secondary encoding if needed.

**Bridge:** Figures decided. Book visually and pedagogically
complete. Chapter 12 is the first build target: Kindle.

---

### CHAPTER 12 — Final Check and Build: EPUB + PDF

**One-line:** Students run the final check sequence,
build the EPUB and PDF, and submit to Kindle Direct
Publishing — understanding the rebuild loop as normal
finishing process.

**Opening:** A Kindle rejection email — metadata missing,
cover image wrong resolution, EPUB validation error.
Then: the final check sequence that prevents each failure.

**Core content blocks:**
1. The Fact-Checking Assistant — assertion types, content
   categories, triage order: OUTDATED → CONTRADICTED →
   UNVERIFIED; what to do with each
2. The build script — what build.sh does; combined.md;
   pandoc command; what can go wrong and how to diagnose
3. Reading the EPUB on a device — why not optional; three
   most common rendering issues
4. KDP submission — account setup, metadata, cover image
   requirements, KDP Select decision, $1 pricing rationale
5. The rebuild loop — why changes after reading on device
   are normal; fast rebuild cycle; AI+1 final assessment

**Worked example:** Complete KDP submission for
ai-for-designers — dashboard, metadata, cover, pricing.
EPUB validation report clean.

**Assessable exercises (4):**
1. (Apply) Run Fact-Checking Assistant. Triage output.
   Resolve at least one OUTDATED or CONTRADICTED finding.
2. (Apply) Run ./build.sh. Open EPUB on Kindle app.
   Note three things to fix.
3. (Apply) Fix, rebuild, confirm resolved.
4. (Evaluate) Assess finished book against AI+1 standard.

**Bridge:** The Kindle book is live — and it is a one-way
surface. It cannot ask the reader anything back. The same
source can carry quizzes, cases, glimmers, and recall cards,
and ship to Canvas, Anki, the web, and a tutor. Part Two
begins where the book ends.

---

# PART TWO — THE ENRICHED LAYER (Chapters 13–20)
*One enriched source, shipped to every surface. Each chapter
explains what an artifact is and why it matters; its script or
prompt lives in a matching appendix (90–97). The human+AI loop
is preserved on every surface. Chapters are independent — read
13 first, then take the surfaces your students use.*

---

### CHAPTER 13 — The Enriched Layer: Beyond the Book

**One-line:** Students learn why one markdown source should
carry not just a book but quizzes, case studies, glimmers, and
spaced-repetition cards — plus an Ask-AI loop on every surface —
and why a one-way book is not enough.

**Opening:** The $0.99 Kindle book is live on Amazon. The reader
is holding a surface that cannot ask them anything back.

**Core content blocks:**
1. The one-way-surface problem — a book teaches; it cannot make
   the student retrieve, practice, or defend
2. The five enriched artifacts — quizzes (familiar; little
   defense needed), case studies, glimmers, spaced-repetition
   cards, and the Ask-AI loop
3. Enrich once, ship everywhere — the content-type × surface
   matrix; the single source of truth holds (every output is a
   build artifact the author never hand-writes)
4. The four surfaces — Canvas, Anki, React site, Medhavy — and
   who must act to finish each
5. Map of Part Two — what chapters 14–20 cover and in what order

**Worked example:** One ai-for-designers chapter shown five
ways — as a book page, a quiz item, a case seed, a glimmer, and
a recall card — all from the same source.

**Assessable exercises (4):** apply (identify enrichable
material) → analyze (matrix one chapter) → evaluate (which
surfaces fit your students) → challenge (defend "a book is not
enough").

**Bridge:** A quiz needs no defense. A case does. Chapter 14.

---

### CHAPTER 14 — Case Studies

**One-line:** Students learn what a teaching case is, why it
drives transfer better than a worked example, and how to
generate and vet one from domain material.

**Opening:** A designer faces a client who wants AI-generated
work passed off as hand-craft. No clean answer. The reader is
inside the decision before any framework arrives.

**Core content blocks:**
1. Case vs. worked example — a worked example shows the
   solution; a case puts the student inside an unresolved
   decision with incomplete information
2. Why cases drive transfer — judgment under ambiguity, not
   pattern-matching
3. The anatomy of a good case — situation, tension, decision
   point(s), the data the student has and lacks, the debrief
4. Generating a case in the pipeline — the generator prompt
   (Appendix 91) and the human vetting that follows
5. The trade-off — cases cost more author vetting than quizzes
   and mislead if the domain facts are wrong

**Worked example:** A vetted case generated for ai-for-designers
— the client AI-disclosure dilemma.

**Assessable exercises (4):** apply → analyze ×2 → evaluate.

**Bridge:** A case makes the student decide. A glimmer makes
them defend the decision to an AI. Chapter 15.

---

### CHAPTER 15 — Glimmers: AI-Interrogated Prompts

**One-line:** Students learn the most novel artifact — a prompt
that makes the AI interrogate the *student*, forcing them to
defend their reasoning rather than receive an answer.

**Opening:** Maya asks Claude to fix her layout. Claude fixes
it. Maya learns nothing. The chapter names what just went wrong.

**Core content blocks:**
1. What a glimmer is — the AI as Socratic adversary, not a tutor
   that solves; the inversion of the usual help direction
2. Glimmer vs. quiz — a quiz checks a known answer; a glimmer
   surfaces the quality of the student's thinking
3. Why it works — retrieval, self-explanation, desirable
   difficulty; it targets the fluency trap directly
4. The mechanism — role ("you interrogate, you do not answer"),
   objective tied to an outcome, escalating probes, stop condition
5. Trade-offs — frustration, guardrail drift, hard to grade

**Worked example:** A glimmer that makes a student defend a
layout decision against an AI's probing (ai-for-designers).

**Assessable exercises (3):** apply → analyze → evaluate.

**Bridge:** Cases and glimmers build judgment. Recall keeps the
facts that judgment stands on. Chapter 16.

---

### CHAPTER 16 — Spaced Repetition: Anki and the Forgetting Curve

**One-line:** Students learn why massed re-reading fails for
durable memory, and how to author a recall layer and compile it
into an Anki deck with `build-anki.py`.

**Opening:** Wednesday-night cramming — recognition mistaken for
retrieval. The chapter lands on the distinction.

**Core content blocks:**
1. Why rereading fails — the forgetting curve; recognition vs.
   retrieval
2. The spacing effect and desirable difficulty — and what Anki's
   scheduler does on a forgetting curve
3. Authoring the recall layer — atomic Q:/A: cards in `recall/`
   or a `## Recall` section
4. `build-anki.py` — pure Python (sqlite3 + zipfile); reads the
   cards, writes a valid Anki schema-11 `.apkg`; the double-click
   import is the reader's step (Appendix 94)
5. Trade-offs — atomic authoring discipline; deck rot when the
   source drifts; recall rewards facts, not synthesis

**Worked example:** Three ai-for-designers cards through the
pipeline to a built, structurally validated `.apkg`.

**Assessable exercises (4):** apply (write atomic cards) → apply
(build the deck) → analyze (audit card quality) → create.

**Bridge:** Cards, cases, and glimmers all live in one source.
Now ship that source to where students already are — the LMS.
Chapter 17.

---

### CHAPTER 17 — Canvas Course Export: .imscc

**One-line:** Students compile the enriched source into a
Canvas-importable .imscc package — same source that produced
the Kindle book, no Canvas API access required.

**Opening:** The professor uploads one file. Settings → Import
Course Content → Choose File. A complete course appears. The
chapter works backward to explain what the file contains.

**Core content blocks:**
1. What .imscc is — a ZIP-like IMS Common Cartridge package;
   `imsmanifest.xml` as the course index; standard (portable)
   CC vs. Canvas-flavored CC (the two trigger files
   `course_settings/syllabus.html` and
   `course_settings/course_settings.xml`)
2. How the single source maps to a course — chapters → modules,
   pages → pages, exercises → assignment/discussion shells, and
   the enriched artifacts riding along
3. `build-imscc-standard.py` — the pure-Python path, standard
   library only; what it reads and produces (Appendix 90)
4. IgniteAI is the *refinement* tool, not the build tool — the
   .imscc builds the baseline in one upload; IgniteAI refines
   after
5. Import is not publication — the post-import diff review is the
   human gate

**Worked example:** The real ai-for-designers/AI+1 package built
by the tested script — 15 modules, 32 pages, a manifest validated
by an XML parser and `xmllint`, no dangling references. The live
Canvas import is the reader's step (a sandbox is fine).

**Assessable exercises (4):** apply (build, confirm manifest) →
apply (import to a Canvas sandbox) → analyze (diff vs. spec) →
create (correct and re-import).

**Bridge:** Canvas is the LMS surface. The open web is another —
and the only one that needs a developer. Chapter 18.

---

### CHAPTER 18 — The React Site: .mdx + .tsx

**One-line:** Students scaffold a Next.js site from the same
source — running one Python command, then handing the result to
a developer.

**Opening:** Thursday morning: the reader wants the book public
on the open web, not behind an LMS login. One command starts it.

**Core content blocks:**
1. Source stays `.md` — `.mdx` (markdown + JSX) and `.tsx`
   (typed page components) are build outputs the author never
   hand-writes
2. `build-react-site.py` — scaffolds content, routes, layout,
   configs, and an `AskAI` placeholder (Appendix 95)
3. The hand-off — what the author does (run the script, write a
   brief) vs. what the developer does (npm install, build, deploy)
4. The `AskAI` placeholder — the web surface's version of the
   Ask-AI loop, wired in Chapter 20
5. Trade-off — the most flexible and most public surface, but the
   only target the author cannot finish alone

**Worked example:** The tested scaffold — 41 chapter/appendix
files in, 89 files out (one `.mdx` + one `.tsx` route each, plus
layout, TOC, AskAI, and configs); valid JSON and default exports.

**Assessable exercises (4):** apply (scaffold, spot-check) →
analyze → evaluate (write the developer hand-off brief) →
audit dependency versions.

**Bridge:** A site serves content. A tutor serves the student —
and that needs the institution. Chapter 19.

---

### CHAPTER 19 — Medhavy: the AI-Tutor Layer via LTI

**One-line:** Students learn what the Medhavy tutor adds on top
of the Canvas course, and what to specify and hand to a developer
and the institution — *not* a file they build alone.

**Opening:** A student clicks a Medhavy link inside Canvas and
lands — no second login — in a tutor that already knows where they
are in the book.

**Core content blocks:**
1. Medhavy is not a file export — it is a hosted system Canvas
   launches into via LTI 1.3 + LTI Advantage
2. What it adds — an AI tutor with course memory, learning
   analytics, formative activities
3. The launch named, not taught — OIDC launch, NRPS roster sync,
   Deep Linking, AGS grade/completion passback (Appendix 96)
4. The system-of-record split — Canvas owns enrollment and grades;
   Medhavy owns tutor interaction, progress, analytics
5. The honest gate — institutional LTI registration, a Canvas
   sandbox, and FERPA/privacy/security review; this is the one
   deployment target the reader cannot do alone

**Worked example:** The student launch experience end to end,
from Canvas module item into the tutor — described at
author-instructor altitude.

**Assessable exercises (4):** apply (draft the spec) → analyze →
evaluate → create (the developer + institution hand-off).

**Bridge:** Five surfaces, five AIs. The last chapter makes them
one argument. Chapter 20.

---

### CHAPTER 20 — Ask AI Everywhere

**One-line:** Students learn to keep the same designed question a
human+AI *loop* — not an answer vending machine — across every
surface, and the book closes on the fluency trap from Chapter 1,
now on the student's side of the desk.

**Opening:** A student with one decision-tree question, four
surfaces, four different AIs. Same question, four answers.

**Core content blocks:**
1. The surface map — Canvas/IgniteAI, Medhavy Ask AI, a parallel
   LLM for Kindle/PDF (a companion prompt), an embedded model on
   the React site
2. The thesis — a tool that answers without a loop produces
   fluent, decision-free mush: the fluency trap, now aimed at
   students
3. What the author controls on each surface — and what they
   cannot (memory, guardrails, trust model differ)
4. The parallel-LLM companion prompt — the "+1" a static format
   cannot host (Appendix 97)
5. The capstone — building a loop, not a vending machine; the
   designer's brief of Chapter 1 and the student's decision tree
   are the same trap on opposite sides of the desk

**Worked example:** The same question answered across IgniteAI,
Medhavy, the parallel-LLM companion prompt, and the React panel —
the loop preserved or lost in each.

**Assessable exercises (3):** paste-ready LLM prompts — apply →
analyze → evaluate.

**Closing:** One source became a book, a course, a deck, a site,
and a tutor. The pipeline is not done — it is waiting for the next
semester, the next edition, the next domain. The reader ends where
Chapter 1 began: catching the fluency trap, now on behalf of their
students.

---

# PART 9 — CHAPTER ANATOMY TEMPLATE

Every chapter follows this structure:

1. Chapter title and italic subtitle (surfacing central tension)
2. One-line capability description
3. Learning objectives (Bloom's level explicit, 3–5 outcomes)
4. Opening case or problem (failure-first; problem before solution)
5. Core content blocks (4–5 per chapter)
6. Worked example (running example artifact from ai-for-designers
   shown beside reader's own in-progress equivalent)
7. Assessable exercises (minimum 3; at least one at Apply or above;
   at least one requiring the reader to produce something)
8. Chapter closing and bridge question (names what the next chapter
   answers)
9. Sidebars where applicable (Python install Ch 5; Node.js Ch 9
   and again Ch 18; Canvas access Ch 17)
10. Pointer chapters (Ch 8 → writing-guide; Ch 9 →
    ai-for-graphs + ai-for-infographics; Ch 19 → Medhavy SDD)

**Enforcement:** A draft chapter missing items 4, 6, or 8
is an incomplete draft. The cold open, worked example, and
bridge question are load-bearing in every chapter.

---

# PART 10 — CASE STUDY STRATEGY

## Running example: ai-for-designers-a-practitioners-guide

One book. Built in full. Shown at every stage.

Every chapter shows one concrete artifact from the
ai-for-designers build — at the stage that chapter covers.
The reader sees a complete book being built from domain
research brief to KDP dashboard (Part One), then the same
source enriched and shipped to course, deck, site, and tutor
surfaces (Part Two) — across 20 chapters.

**Why ai-for-designers:**
- Freelance profession with one primary client relationship —
  high irreducibly human content
- AI is visibly disrupting the field (Midjourney, Figma AI,
  Adobe Firefly, Canva AI)
- The fluency trap is vivid — AI output looks like design
  but lacks craft judgment
- Solo practitioner mirrors the author-instructor reader

**Domain coverage:** All 20 chapter worked examples draw
from the design profession. No domain rotation.

**Sourcing requirement:** Every artifact shown in the
worked examples must be produced from a real run, not
invented. The three Part Two build scripts
(`build-imscc-standard.py`, `build-anki.py`,
`build-react-site.py`) have been written and tested against
real source and produce structurally validated output. The
steps that remain reader/institution-side — the live Canvas
import, the Anki import, the React deploy, the Medhavy LTI
registration — must be performed against a real instance
before those worked examples are finalized, and are marked as
such in the drafts.

---

# PART 11 — HARD TOPICS, CONTESTED CLAIMS, AGING RISK

## Contested claims

| Claim | Status | Book's position |
|---|---|---|
| TIKTOC.md session is the highest-leverage step | Argued, not settled | Central thesis — the side-by-side comparison in Ch 4 is the evidence |
| Human rewrite is the gate | Argued | Made concrete in Ch 8 via Combined Test and three-pass worked example |
| $1 Kindle is a serious publishing format | Contested in publishing | Named explicitly as a pedagogical and distribution decision |
| Cowork produces publishable first drafts | Disputed | Named explicitly as producing drafts worth rewriting, not finished books |
| .imscc is sufficient for Canvas deployment without IgniteAI | Factual, may surprise readers | Demonstrated in Ch 17 worked example; the import works at all Canvas tiers; IgniteAI refines after |
| One source can serve book, course, deck, site, and tutor | The book's Part Two claim | Demonstrated by three tested build scripts; the single-source matrix is the strength |
| A glimmer (AI interrogates the student) teaches more than a quiz | Argued, not settled | Made concrete in Ch 15; grounded in retrieval/self-explanation mechanisms, not effect-size claims |

## Hard chapters

**Chapter 4 (TIKTOC.md):** Hardest to draft. Annotated
transcript excerpts must come from real sessions.

**Chapter 8 (Human Rewrite):** Must not read as a
checklist chapter. The two-paragraph opening is
load-bearing.

**Chapter 17 (Canvas Export):** One path now — the standard
Python builder (`build-imscc-standard.py`), written and tested.
The Ruby `canvas_cc` path was dropped. The worked example still
needs a real Canvas sandbox import to be finalized.

**Chapter 19 (Medhavy/LTI):** The one Part Two chapter that is a
hand-off, not a build the reader runs. It must stay at
author-instructor altitude and say plainly that it is gated
behind institutional LTI registration, a Canvas sandbox, and
FERPA review. Easy to over-scope into a developer tutorial —
keep the protocol detail in Appendix 96 and the Medhavy SDD.

**Chapter 20 (Ask AI Everywhere):** The capstone. Must land the
argument and close the loop to Chapter 1, not just describe a
feature. The least script-like, most argumentative chapter.

## Aging risk

| Content | Risk | Mitigation |
|---|---|---|
| KDP submission interface | HIGH | Flag as current-state; stable framework described |
| Canvas import interface | HIGH | Flag as current-state; Settings → Import path is stable |
| IgniteAI / Canvas Insights features | HIGH | Refinement tool only; describe behavior generically, flag as current-state |
| Medhavy LTI registration / Canvas Developer Key UI | HIGH | Keep in Appendix 96; key to 1EdTech LTI 1.3 spec, flag Canvas-specific fields |
| Next.js / @next/mdx versions (React site) | HIGH | Pin versions in the generated package.json; note Next major versions move fast |
| Cowork / Codex prompt syntax | HIGH | Flag as current-state; point to online prompt library |
| LLM model names | MEDIUM | Use model-agnostic framing where possible |
| AI tool adoption rates in design | MEDIUM | Cite year of data; flag as current-state |
| Anki .apkg schema (currently 11) | MEDIUM | Schema 11 is long-stable; note Anki could bump it |
| new_book.py / build script syntax | LOW | Stable Python, standard library only |
| Tic TOC phase gate structure | LOW | Architecture is stable |
| imsmanifest.xml format | LOW | IMS CC 1.3 spec is stable; Canvas supports 1.x |
| LTI 1.3 + LTI Advantage standard | LOW | Mature 1EdTech standard |
| Pipeline sequence | LOW | Extremely stable — logic is build-sequence |

---

# PART 12 — APPENDIX MAP

All appendices contain prompts or scripts the reader
copies or runs directly. Numbered from 80; 99 is always back
matter. Appendices 80–89 carry the Part One pipeline tools;
90–97 carry the Part Two scripts and prompts.

| File | Number | Contents |
|------|--------|----------|
| 80-appendix-tiktoc.md | 80 | Tic TOC prompt |
| 81-appendix-domain-research.md | 81 | Domain research prompt |
| 82-appendix-scaffold.md | 82 | new_book.py scaffold script |
| 83-appendix-research-pass.md | 83 | Research pass prompts |
| 84-appendix-chapter-writer.md | 84 | Chapter Writer prompt |
| 85-appendix-combined-test.md | 85 | Combined Test checklist |
| 86-appendix-finishing-figures.md | 86 | Finishing pass + image suggest prompts |
| 87-appendix-enrichment.md | 87 | Enrichment prompts |
| 88-appendix-cajal.md | 88 | CAJAL figure command set |
| 89-appendix-factcheck.md | 89 | Fact-checking prompt |
| 90-appendix-imscc-standard.md | 90 | build-imscc-standard.py — pure-Python .imscc builder (Ch 17) ✅ tested |
| 91-appendix-case-generator.md | 91 | Case Study Generator prompt (Ch 14) |
| 92-appendix-glimmer-generator.md | 92 | Glimmer Generator prompt (Ch 15) |
| 93-appendix-spaced-repetition-generator.md | 93 | Spaced-Repetition Card Generator prompt (Ch 16) |
| 94-appendix-anki-build.md | 94 | build-anki.py — .apkg builder (Ch 16) ✅ tested |
| 95-appendix-react-site.md | 95 | build-react-site.py — .mdx + .tsx scaffold (Ch 18) ✅ tested |
| 96-appendix-medhavy-lti.md | 96 | Medhavy LTI 1.3 setup guide + SDD pointer (Ch 19) |
| 97-appendix-ask-ai.md | 97 | Per-surface Ask-AI config + parallel-LLM companion prompt (Ch 20) |
| 99-back-matter.md | 99 | Back matter (always 99) |

Slot 98 reserved for future appendices. The dropped Ruby
`canvas_cc` builder no longer has a slot.

---

# PART 13 — OPEN QUESTIONS

| # | Question | Stakes | Deadline | Owner |
|---|---------|--------|----------|-------|
| 1 | ai-for-designers running example must be built from a real run before Chapter 4 can be drafted | All chapter worked examples depend on it | Before drafting begins | Author |
| 2 | Annotated Tic TOC transcript excerpts for Chapter 4 — which session to use? | Chapter 4 authenticity | Before Ch 4 draft | Author |
| 3 | writing-guide companion — which chapters specifically to point to in Ch 8? | Chapter 8 pointer accuracy | Before Ch 8 draft | Author |
| 4 | ai-for-graphs and ai-for-infographics — which chapters to point to in Ch 9? | Chapter 9 pointer accuracy | Before Ch 9 draft | Author |
| 5 | KDP Select screenshot currency — interface may change | Ch 12 accuracy | Before publication | Author |
| 6 | Python and Node.js sidebars — need testing on Mac, Windows, Linux | Ch 5 and Ch 9 accessibility | Before final draft | Author |
| 7 | build-imscc-standard.py — write and test before Ch 17 draft | Ch 17 and Appendix 90 | ✅ DONE — tested, valid CC 1.3.0 (15 modules, 32 pages) | Author |
| 8 | build-anki.py — write and test before Ch 16 draft | Ch 16 and Appendix 94 | ✅ DONE — tested, valid Anki schema-11 .apkg | Author |
| 9 | build-react-site.py — write and test before Ch 18 draft | Ch 18 and Appendix 95 | ✅ DONE — tested, 41 → 89 files, valid configs | Author |
| 10 | Canvas sandbox — live .imscc import for the Ch 17 worked example | Ch 17 authenticity | Open — reader step | Author |
| 11 | Anki import — load the built .apkg to finalize the Ch 16 worked example | Ch 16 authenticity | Open — reader step | Author |
| 12 | React deploy — a built/deployed example site for the Ch 18 worked example | Ch 18 authenticity | Open — developer step | Author + dev |
| 13 | Medhavy LTI registration with Northeastern IT — will they allow it? | Ch 19 scope | Open — institution step | Author + NEU IT |
| 14 | FERPA / privacy / security review for the Medhavy tutor data | Ch 19 accuracy | Open | Institution |
| 15 | Confirm the two trigger files still cause Canvas-flavored CC | Ch 17 technical accuracy | Open — verify before publish | Author |
| 16 | Voice variance across the eight Part Two drafts (parallel-drafted) | Part Two consistency | Resolve in the human rewrite | Author |
| 17 | Where the enriched artifacts are *authored* — expand Ch 10, or a dedicated generation chapter? | Source-of-truth story | Decide before final structure | Author |

---

*Full TOC Draft v3.0 — two parts, twenty chapters*
*Part One (Ch 1–12): the pipeline, drafted. Part Two (Ch 13–20):*
*the enriched layer, drafted from three tested build scripts.*
*Primary blocker before publication: ai-for-designers running*
*example must be produced from real runs (Open Question 1), and the*
*reader/institution-side imports finalized (OQ 10–15).*
