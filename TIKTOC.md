# AI+1: AI Native Personalized Textbooks
## Full TOC Draft — compiled from all phase outputs

**Working title:** AI+1: AI Native Personalized Textbooks
**Author:** Nik Bear Brown · ni.brown@neu.edu · Bear Brown & Company
**Series:** AI+1 · Bear Brown & Company
**Document:** Full TOC Draft — compiled from all phase outputs
**Version:** 1.0
**Status:** Pre-draft — Chapter 4 transcript examples and
ai-for-designers running example must be produced before drafting begins

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
> textbook** — domain-specific, AI-native, and Kindle-ready —
> by **walking them through a structured pipeline that starts with
> a two-hour Tic TOC session to produce a TIKTOC.md, hands off to
> Cowork for automated drafting, and repositions the human as editor
> making small refinements until a production-quality EPUB and PDF
> comes off the build script**. It fills the gap left by generic
> AI writing tools (which produce undifferentiated output) and
> traditional textbook publishing (which is slow, expensive, and
> inaccessible to domain experts without institutional backing).
> It succeeds if **the reader finishes with a rough draft of their
> own AI+1 textbook in hand, understands exactly where their
> judgment is required and where the pipeline runs without them,
> and can explain to a colleague why the TIKTOC.md session is the
> highest-leverage two hours in the entire process.**

**One-sentence logline:**
The TIKTOC.md session is not overhead — it is the product;
everything downstream is execution.

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
  standard is the final check. The reader ends by assessing
  their own book for the fluency trap they caught in Chapter 1. ✓

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
Eleven chapters, each ending with a concrete deliverable,
each beginning with the problem the step solves. A reader
scanning the chapter titles sees a build sequence, not a
curriculum. The running example (ai-for-designers) appears
in every chapter as a completed artifact beside the reader's
own in-progress work.

---

# PART 4 — FIELD POSITIONING

## The gap this book fills

No book currently teaches the complete AI+1 textbook
production pipeline — from domain research brief through
Tic TOC session through Cowork draft through human rewrite
through Kindle submission — to a solo author-instructor
with deep domain expertise and no technical background.

Generic AI writing guides teach prompt engineering, not
instructional architecture. Traditional textbook writing
guides assume institutional support, co-authors, and a
multi-year timeline. The pipeline this book teaches
produces a Kindle-ready rough draft in 4–6 weeks.

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
produces a Kindle-ready rough draft in 4–6 weeks using
a pipeline designed for a solo author-instructor with
domain expertise and no technical co-author."

**vs. the Medhavy book:**
"The Medhavy book explains what AI+1 is. This book
explains how to build one. They are designed to be
read in sequence — concept first, then pipeline."

---

# PART 5 — THREE-ACT LEARNING ARC

## The arc statement

This book takes the reader from **domain expert who has
heard of AI but hasn't built anything with it** to
**author-instructor who has a Kindle-ready AI+1 textbook
in their hands** by first establishing what AI is doing
to their profession and why the AI+1 architecture protects
their identity (Act One), then walking them through the
pipeline that produces a rough draft (Act Two), then
repositioning them as the editor and publisher who takes
that draft to finished product (Act Three).

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

## Act Three — Apply (Chapters 8–11)

**Starting state:** Rough draft exists. Reader is ready
to stop executing the pipeline and start owning the book.

**Ending state:** Kindle-ready EPUB and PDF. Book live on
KDP. Reader understands the rebuild loop.

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
| 11 | KDP dashboard — ai-for-designers submission |

---

# PART 6 — PREREQUISITE MAP

| Prerequisite | Safe to Assume? | Where Addressed |
|---|---|---|
| Domain expertise | Yes | — |
| Basic Claude familiarity | Probably | Chapter 1 |
| File system comfort | Probably | Chapter 5 |
| Python installed | No | Chapter 5 sidebar |
| Node.js installed | No | Chapter 9 sidebar |
| Markdown fluency | No | Chapter 5 sidebar |
| Cowork access | No | Chapter 7 |
| Instructional design background | Explicitly not required | Tic TOC handles it |
| Prior textbook experience | Explicitly not required | Pipeline handles it |

**Front-loading decision:** Python, Node.js, and Markdown
addressed at first use via one-page sidebars. No Chapter 0
or prerequisite appendix. Stating these as prerequisites
upfront would misrepresent the book's target reader.

**Load-bearing chapters:**
- Chapter 4 (TIKTOC.md): FATAL to skip. All downstream
  Cowork runs depend on it.
- Chapter 7 (Cowork Draft): FATAL to skip. Human rewrite
  cannot happen without a draft.
- Chapter 8 (Human Rewrite): No automated enforcement.
  Author's judgment is the only gate.

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
| 11 | Final Check and Build | Evaluate | — |

Create-level outcomes concentrated at the three
highest-judgment steps: domain research brief (Ch 3),
TIKTOC.md (Ch 4), and human rewrite (Ch 8).

---

# PART 8 — CHAPTER-BY-CHAPTER TOC

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

## ACT THREE — APPLY (Chapters 8–11)
*Repositions the reader as author and publisher.
The pipeline stops running automatically.*

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
   Chapters 9–11 if it is skipped
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
One final check before the build. Chapter 11 is short
but not skippable.

---

### CHAPTER 11 — Final Check and Build: EPUB + PDF

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
   requirements, KDP Select (90-day, what it costs, what
   it provides), $1 pricing rationale
5. The rebuild loop — why changes after reading on device
   are normal; fast rebuild cycle; AI+1 final assessment

**Worked example:** Complete KDP submission for
ai-for-designers — dashboard, metadata, cover, pricing,
KDP Select selected. EPUB validation report clean.

**Assessable exercises (4):**
1. (Apply) Run Fact-Checking Assistant. Triage output.
   Resolve at least one OUTDATED or CONTRADICTED finding.
2. (Apply) Run ./build.sh. Open EPUB on Kindle app.
   Note three things to fix.
3. (Apply) Fix, rebuild, confirm resolved.
4. (Evaluate) Assess finished book against AI+1 standard:
   domain-specific exercises, professional identity
   preserved, no fluency trap in the pedagogy.

**Closing:** The book is live on KDP. The reader is an
author-instructor with a Kindle-ready AI+1 textbook.
The rebuild loop never fully closes — every course run
produces new cases, new failure modes, new AI capabilities
to add. The pipeline is waiting.

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
9. Sidebars where applicable (Python install Ch 5; Node.js Ch 9;
   Cowork access Ch 7)
10. Pointer chapters (Ch 8 → writing-guide; Ch 9 →
    ai-for-graphs + ai-for-infographics)

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
research brief to KDP dashboard across 11 chapters.

**Why ai-for-designers:**
- Freelance profession with one primary client relationship —
  high irreducibly human content
- AI is visibly disrupting the field (Midjourney, Figma AI,
  Adobe Firefly, Canva AI)
- The fluency trap is vivid — AI output looks like design
  but lacks craft judgment
- Solo practitioner mirrors the author-instructor reader

**Domain coverage:** All 11 chapter worked examples draw
from the design profession. No domain rotation. Consistency
is more valuable than variety for a pipeline handbook —
the reader needs to see the same book across all 11 stages.

**Sourcing requirement:** Every artifact shown in the
worked examples must be produced from a real run, not
invented. This is the highest-priority production constraint.

---

# PART 11 — HARD TOPICS, CONTESTED CLAIMS, AGING RISK

## Contested claims

| Claim | Status | Book's position |
|---|---|---|
| TIKTOC.md session is the highest-leverage step | Argued, not settled | Central thesis — the side-by-side comparison in Ch 4 is the evidence |
| Human rewrite is the gate | Argued | Made concrete in Ch 8 via Combined Test and three-pass worked example |
| $1 Kindle is a serious publishing format | Contested in publishing | Named explicitly as a pedagogical and distribution decision |
| Cowork produces publishable first drafts | Disputed | Named explicitly as producing drafts worth rewriting, not finished books |

## Hard chapters

**Chapter 4 (TIKTOC.md):** Hardest to draft. Annotated
transcript excerpts must come from real sessions. The
side-by-side TIKTOC.md comparison is the most important
figure in the book. Cannot be invented.

**Chapter 8 (Human Rewrite):** Must not read as a checklist
chapter. The two-paragraph side-by-side opening is
load-bearing. The three-pass worked example must show
genuine improvement, not polished before/after.

## Aging risk

| Content | Risk | Mitigation |
|---|---|---|
| KDP submission interface | HIGH | Stable framework + current-state clearly separated |
| Cowork prompt syntax | HIGH | Flag as current-state; point to online prompt library |
| LLM model names (Claude, GPT, Gemini) | MEDIUM | Use model-agnostic framing where possible |
| AI tool adoption rates in design | MEDIUM | Cite year of data; flag as current-state |
| new_book.py command syntax | LOW | Stable Python; unlikely to change |
| Tic TOC phase gate structure | LOW | Architecture is stable |
| Pipeline sequence | LOW | Extremely stable — logic is build-sequence |

---

# PART 12 — OPEN QUESTIONS

| # | Question | Stakes | Deadline | Owner |
|---|---------|--------|----------|-------|
| 1 | ai-for-designers running example must be built from a real run before Chapter 4 can be drafted | All chapter worked examples depend on it | Before drafting begins | Author |
| 2 | Annotated Tic TOC transcript excerpts for Chapter 4 — which session to use? | Chapter 4 authenticity | Before Ch 4 draft | Author |
| 3 | writing-guide companion — which chapters specifically to point to in Ch 8? | Chapter 8 pointer accuracy | Before Ch 8 draft | Author |
| 4 | ai-for-graphs and ai-for-infographics — which chapters specifically to point to in Ch 9? | Chapter 9 pointer accuracy | Before Ch 9 draft | Author |
| 5 | KDP Select screenshot currency — interface may change between writing and publication | Ch 11 accuracy | Before publication | Author |
| 6 | Python and Node.js sidebars — need testing on Mac, Windows, Linux before final draft | Ch 5 and Ch 9 accessibility | Before final draft | Author |

---

*Full TOC Draft v1.0 — compiled from all phase outputs*
*All phases complete: Vision (i1–i4), Learning Architecture (l1–l4),*
*Chapter Architecture (c1), Build (g1)*
*Primary blocker before drafting: ai-for-designers running example*
*must be produced from a real Cowork run (Open Question 1)*
