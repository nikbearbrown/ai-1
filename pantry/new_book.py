#!/usr/bin/env python3
"""
new_book.py — scaffold a new book project

Usage:
    python new_book.py "My Book Title" "Author Name"
    python new_book.py "Essais on Learning" "Nik Bear Brown" --subtitle "The Evidence Problem" --volume 1 --chapters 14
    python new_book.py "My Book Title" "Author Name" --dir ~/Documents
    python new_book.py "My Book Title" "Author Name" --publisher "My Press"

python ~/Documents/BEAR/new_book.py "The Reallocation Engine" "Nik Bear Brown" --dir /Users/bear/Documents/CoWork/bear-textbooks/books --chapters 1

File structure produced:
    book.md                 ← book description and high-level outline (planning)
    outline.md              ← starter table of contents (planning)
    vision.md               ← Tic TOC Phase 1: vision and positioning
    architecture.md         ← Tic TOC Phase 2: learning architecture
    chapters-spec.md        ← Tic TOC Phase 3: chapter specifications
    risks.md                ← Tic TOC Phase 4: scope, market, risks
    pantry/                 ← scratch storage for fragments, snippets, leftovers
    chapters/
        00-frontmatter.md   ← copyright, dedication, preface
        01-introduction.md  ← Chapter 0 / Introduction
        02-chapter-01.md    ← Chapter 1
        ...
        NN-chapter-XX.md    ← Chapter N
        99-back-matter.md   ← acknowledgments, about the author, notes, references, index
    images/                 ← all figures as PNG (book uses these)
    d3/                     ← D3 HTML files — interactive browser-runnable versions
    SCRIPTS/
        svg-to-png.mjs      ← converts images/**/*.svg to 300dpi PNG
"""

import argparse
import sys
from datetime import date
from pathlib import Path


def slugify(text):
    return text.lower().replace(" ", "-").replace("'", "").replace('"', "")


FRONTMATTER_TEMPLATE = """\
<!--
    00-frontmatter.md
    FRONT MATTER — everything that appears before Chapter 1.

    This file contains four sections in order:
      1. Copyright page
      2. Dedication (optional — delete if not using)
      3. Preface

    Do not number these sections. They use roman numerals in print
    and appear before the body in the compiled EPUB.
-->

# {title}

{subtitle_line}**{author}**

---

## Copyright

Copyright © {year} {author}. All rights reserved.

Published by {publisher}.

No part of this publication may be reproduced, distributed, or transmitted
in any form or by any means without the prior written permission of the
publisher, except in the case of brief quotations in critical reviews and
certain other noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

---

## Dedication

<!-- Optional. Delete this section if not using. -->

*[For — ]*

---

## Preface

<!-- The preface is written in the author's voice.
     It answers three questions:
       - Why does this book exist? (the gap it fills)
       - Why now? (what changed that makes this urgent)
       - Why you? (what credentials or experience qualify you to write it)
     It is NOT a summary of the book — that belongs in the Introduction.
     Typical length: 2–5 pages. -->

[PREFACE PLACEHOLDER]

<!-- Suggested elements:
     - The moment or problem that prompted this book
     - What the book argues that hasn't been said before
     - Who it is written for
     - Any biographical context that establishes credibility
     - Brief acknowledgment of what the book does NOT cover
-->
"""

INTRODUCTION_TEMPLATE = """\
<!--
    01-introduction.md
    INTRODUCTION — Chapter 0 / roadmap chapter.

    The Introduction does different work than the Preface:
      - Preface  = why the book exists, why you wrote it (author's voice)
      - Introduction = what the book argues and how it is organized (reader's roadmap)

    This chapter is fully numbered in the body and can be as long as needed.
    Pearl's "The Mind Over Data" and Molnar's Introduction are good models:
    both are substantive, argument-first, and tell the reader exactly what
    to expect from each subsequent chapter.
-->

# Introduction

<!-- Opening: state the central problem or claim in the first paragraph.
     Do not throat-clear. Do not say "In this book I will..." -->

[INTRODUCTION PLACEHOLDER]

<!-- Suggested structure:
     1. The central claim — what this book argues
     2. Why it matters — stakes for the reader
     3. How the book is organized — a brief tour of each chapter
        (one sentence per chapter is enough; readers need a map, not a summary)
     4. How to read it — linear vs. jump-around, prerequisites, etc.
-->

## How This Book Is Organized

<!-- Walk through each chapter in one sentence.
     Example pattern: "Chapter 1 establishes X. Chapter 2 applies that
     framework to Y. Chapters 3–6 examine..." -->

[CHAPTER MAP PLACEHOLDER]
"""

BACK_MATTER_TEMPLATE = """\
<!--
    99-back-matter.md
    BACK MATTER — everything that appears after the final chapter.

    Sections in order:
      1. Acknowledgments
      2. About the Author
      3. Notes (by chapter, if using endnotes rather than footnotes)
      4. References / Bibliography
      5. Index (omit for online/free release; include for print/press)

    Back matter continues the arabic page numbering from where
    the final chapter ended. No page restart.
-->

---

## Acknowledgments

<!-- Keep it short. Name the people who materially helped the book exist:
     readers of drafts, researchers, editors, collaborators.
     One paragraph is enough unless the debt is substantial.
     Avoid laundry lists. -->

[ACKNOWLEDGMENTS PLACEHOLDER]

---

## About the Author

<!-- Third person. 100–200 words. Credentials that are relevant to THIS book.
     Not a full CV. End with a line about where to find you online. -->

[AUTHOR BIO PLACEHOLDER]

---

## Notes

<!-- Use this section for endnotes if you prefer them over footnotes.
     Group by chapter. Format:

     ### Chapter 1

     1. [Citation or explanatory note]
     2. [Citation or explanatory note]

     ### Chapter 2
     ...

     If using footnotes in-line (pandoc [^1] syntax), delete this section.
-->

[NOTES PLACEHOLDER]

---

## References

<!-- Full bibliography. Alphabetical by author last name, or grouped by chapter.
     Use a consistent citation style throughout (Chicago, APA, or a hybrid).

     Example entry (Chicago author-date):
     Pearl, Judea, and Dana Mackenzie. *The Book of Why*. Basic Books, 2018.
-->

[REFERENCES PLACEHOLDER]

---

## Index

<!-- For online/free release: delete this section.
     For print/press: compile after all other content is final.
     Pandoc does not auto-generate an index; use dedicated indexing software
     (e.g., indexd, Word indexing tools) or a professional indexer. -->

[INDEX PLACEHOLDER — omit for online release]
"""


BOOK_TEMPLATE = """\
<!--
    book.md
    BOOK DESCRIPTION & HIGH-LEVEL OUTLINE — your planning document.

    This file is for YOU, not the reader. It does not get compiled into
    the EPUB. Use it to think clearly about what the book is before you
    write it, and to keep yourself honest as you draft.

    Update freely as the book takes shape. Earlier versions belong in
    git history, not in this file.
-->

# {title}

{subtitle_line}**Author:** {author}

---

## One-Sentence Pitch

<!-- If you can't say what the book is in one sentence, you don't
     yet know what the book is. Force the constraint. -->

[ONE SENTENCE]

## The Argument

<!-- What does this book claim that isn't already obvious or settled?
     What changes in the reader's head between page one and the end?
     2–4 paragraphs. -->

[ARGUMENT PLACEHOLDER]

## The Gap

<!-- Why does this book need to exist? What does it do that no other
     book in the field already does? Name 2–3 books in the same space
     and say briefly how yours differs. -->

[GAP PLACEHOLDER]

## The Reader

<!-- Who is this book FOR? Be specific — not "anyone interested in X."
     What do they already know? What are they trying to do?
     What will they be able to do after reading it? -->

[READER PLACEHOLDER]

## High-Level Outline

<!-- Three to five acts / parts / movements. Not chapters yet — those
     live in outline.md. This is the shape of the argument at altitude. -->

**Part I — [Title]**
[What this part establishes]

**Part II — [Title]**
[What this part does with what Part I established]

**Part III — [Title]**
[Where the argument lands]

## Open Questions

<!-- Things you don't yet know how to handle. Update as you draft.
     Don't pretend they're solved. -->

- [ ]
- [ ]
- [ ]
"""


OUTLINE_TEMPLATE = """\
<!--
    outline.md
    TABLE OF CONTENTS — your chapter-level planning document.

    This is NOT the auto-generated TOC that appears in the EPUB
    (pandoc handles that via --toc in build.sh). This file is YOUR
    working outline: chapter titles, one-line descriptions, and the
    order of arguments before you start drafting.

    Keep it in sync with the actual chapter files in chapters/.
    When the outline diverges from the drafts, update one or the other —
    don't let them drift.
-->

# {title} — Outline

{subtitle_line}**Author:** {author}

---

## Front Matter

- **Copyright**
- **Dedication** *(optional)*
- **Preface** — why this book exists, in the author's voice

## Introduction

[One-sentence description of what the introduction argues and the map it gives the reader]

## Chapters

{chapter_outline_rows}
## Back Matter

- **Acknowledgments**
- **About the Author**
- **Notes** *(if using endnotes)*
- **References**
- **Index** *(print only)*

---

## Notes on Order

<!-- Why are the chapters in THIS order? What does each chapter
     assume the reader has already read? If you can swap two chapters
     without breaking anything, ask whether the order is doing real work. -->

[ORDER NOTES PLACEHOLDER]
"""


# ─────────────────────────────────────────────────────────────────────────────
# Tic TOC planning file templates
# ─────────────────────────────────────────────────────────────────────────────

VISION_TEMPLATE = """\
<!--
    vision.md
    Tic TOC Phase 1: Vision and Positioning.
-->

# {title} — Vision

{subtitle_line}**Author:** {author}

*Phase 1 output from Tic TOC. Generated by /scaffold or built through /i1–/i4.*

---

## Book Concept Summary

[NEEDS HUMAN INPUT — Tic TOC reasoning: book.md not yet filled in]

This book teaches [WHAT CAPABILITY] to [WHO], by [HOW — method or
structure], filling the gap left by [EXISTING ALTERNATIVES]. It succeeds
if the reader can [MEASURABLE OUTCOME] after completing it.

## Book Type and Deployment Specification

**Book type:** [ ] Course Textbook / [ ] Practitioner Handbook / [ ] Field-Defining Monograph

**Primary adoption context:** [NEEDS HUMAN INPUT]

**Secondary adoption context:** [NEEDS HUMAN INPUT]

**What the book is explicitly NOT designed for:** [NEEDS HUMAN INPUT]

**How the TOC will signal book type to a reviewing faculty member:** [NEEDS HUMAN INPUT]

## Learner Profile

**Primary reader (one specific person, not a category):** [NEEDS HUMAN INPUT]

**Prior knowledge (safe to assume):** [NEEDS HUMAN INPUT]

**Prior misconceptions:** [NEEDS HUMAN INPUT]

**Current capability gap:** [NEEDS HUMAN INPUT]

**Motivation type:** [ ] Academic / [ ] Professional / [ ] Intellectual

## Prerequisite Map

| Prerequisite | Safe to Assume? (Yes/Probably/No) | Where Introduced |
|---|---|---|
| [NEEDS HUMAN INPUT] | | |

**Front-loading decision:** [NEEDS HUMAN INPUT]

## Central Argument

[NEEDS HUMAN INPUT]

## Field Positioning

### Comparable Text 1
- **Title / Author / Year:** [NEEDS HUMAN INPUT]
- **What it covers that this book also covers:**
- **What it misses that this book addresses:**
- **What it gets wrong that this book corrects:**
- **Why a faculty member would choose this book over it:**

### Comparable Text 2
[NEEDS HUMAN INPUT]

### Comparable Text 3
[NEEDS HUMAN INPUT]

### Positioning Statements

[NEEDS HUMAN INPUT]

### Thesis Test

Does the proposed TOC structure reflect the thesis?
[NEEDS HUMAN INPUT]
"""

ARCHITECTURE_TEMPLATE = """\
<!--
    architecture.md
    Tic TOC Phase 2: Learning Architecture.
-->

# {title} — Learning Architecture

{subtitle_line}**Author:** {author}

*Phase 2 output from Tic TOC. Generated by /scaffold or built through /l1–/l4.*

---

## Learning Outcomes

### Chapter 1
1. [NEEDS HUMAN INPUT — outcome at Bloom's level X]
2.
3.

### Chapter 2
[NEEDS HUMAN INPUT]

## Outcome Map

| Chapter | Bloom's Level | Assessable? | Maps to Course Need? |
|---|---|---|---|
| 1 | | | |

## Sequencing Model and Justification

**Primary model:** [ ] Simple→Complex / [ ] Concrete→Abstract / [ ] Historical→Contemporary / [ ] Problem→Solution / [ ] Spiral

**Justification against learner profile:** [NEEDS HUMAN INPUT]

**Most likely break-down chapter:** [NEEDS HUMAN INPUT]

**Transition chapter (foundation→advanced pivot):** [NEEDS HUMAN INPUT]

## Three-Act Learning Arc

**Act One — Establish:** [NEEDS HUMAN INPUT]

**Act Two — Build:** [NEEDS HUMAN INPUT]

**Act Three — Apply:** [NEEDS HUMAN INPUT]

**Arc statement:** [NEEDS HUMAN INPUT]

## Prerequisite Dependency Map

| Chapter | Depends On (chapters or assumed knowledge) |
|---|---|
| 1 | |

**Broken sequences:** [NEEDS HUMAN INPUT]

**Load-bearing chapters:** [NEEDS HUMAN INPUT]
"""

CHAPTERS_SPEC_TEMPLATE = """\
<!--
    chapters-spec.md
    Tic TOC Phase 3: Chapter Specifications.
-->

# {title} — Chapter Specifications

{subtitle_line}**Author:** {author}

*Phase 3 output from Tic TOC. Generated by /scaffold or built through /c1–/c4.*

---

## Chapter 1 — [TITLE]

**One-line description (capability built, not topics covered):** [NEEDS HUMAN INPUT]

**Learning outcomes (cross-reference architecture.md):**
1.

**Problem the chapter solves for the learner:** [NEEDS HUMAN INPUT]

**Chapter opening strategy:** [NEEDS HUMAN INPUT]

**Core content blocks (4–6):**
1.
2.
3.

**Worked example or case study:** [NEEDS HUMAN INPUT]

**Assessable exercises (minimum 3, at least one at Apply level or above):**
1.
2.
3.

**Chapter closing / bridge to next chapter:** [NEEDS HUMAN INPUT]

---

## Chapter 2 — [TITLE]

[NEEDS HUMAN INPUT — repeat structure]

---

## Coverage Gaps

| Topic | Why Excluded | Acknowledged in Preface? |
|---|---|---|

## Hard Chapters

[NEEDS HUMAN INPUT]

## Aging Risk Audit

[NEEDS HUMAN INPUT]
"""

RISKS_TEMPLATE = """\
<!--
    risks.md
    Tic TOC Phase 4: Scope, Market, and Risk.
-->

# {title} — Scope, Market, and Risk

{subtitle_line}**Author:** {author}

*Phase 4 output from Tic TOC. Generated by /scaffold or built through /m1–/m4.*

---

## Comparable Texts Analysis

### Comparable Text 1
- **Title / Author / Publisher / Year / Edition:** [NEEDS HUMAN INPUT]
- **Target reader and deployment context:**
- **Strongest chapters:**
- **Weakest chapters:**
- **Why a faculty member might choose IT over THIS book:**
- **Why a faculty member might choose THIS book over IT:**

### Comparable Text 2
[NEEDS HUMAN INPUT]

### Comparable Text 3
[NEEDS HUMAN INPUT]

## Differentiation Statements

[NEEDS HUMAN INPUT]

## Market Size Estimate

- **Courses per year that could adopt:** [NEEDS HUMAN INPUT]
- **Copies per adoption:**
- **Primary or supplementary text?** [ ] Primary / [ ] Supplementary

## Feature List with Priority Tags

| Feature | Priority | Outcome Served | Production Effort | Producer | Dependency |
|---|---|---|---|---|---|

## Out of Scope

| Topic | Reason for Exclusion | Decided By | Reopen Condition | Acknowledge in Preface? |
|---|---|---|---|---|

## Adoption Risk Register

| Risk | Category | Likelihood | Impact | Trigger | Mitigation | Contingency |
|---|---|---|---|---|---|---|

## Top 3 Adoption Risks

1. [NEEDS HUMAN INPUT]
2. [NEEDS HUMAN INPUT]
3. [NEEDS HUMAN INPUT]
"""

# ─────────────────────────────────────────────────────────────────────────────
# SCRIPTS/svg-to-png.mjs — written into every new book scaffold
# ─────────────────────────────────────────────────────────────────────────────

SVG_TO_PNG_SCRIPT = """\
import sharp from 'sharp';
import { glob } from 'glob';
import { statSync } from 'fs';

// Converts every SVG in images/ to a 300dpi PNG.
// Idempotent: skips any PNG that is already newer than its SVG source.
// Run from the book root: node SCRIPTS/svg-to-png.mjs

const files = await glob('images/**/*.svg');

if (files.length === 0) {
  console.log('No SVG files found in images/');
  process.exit(0);
}

let converted = 0;
let skipped = 0;

for (const file of files) {
  const out = file.replace('.svg', '.png');

  try {
    const svgMtime = statSync(file).mtimeMs;
    try {
      const pngMtime = statSync(out).mtimeMs;
      if (pngMtime > svgMtime) {
        console.log(`skipped (up to date): ${out}`);
        skipped++;
        continue;
      }
    } catch {
      // PNG doesn't exist yet — proceed
    }

    await sharp(file, { density: 300 }).png().toFile(out);
    console.log(`${file} → ${out}`);
    converted++;
  } catch (err) {
    console.error(`ERROR: ${file} — ${err.message}`);
  }
}

console.log(`\\nDone. Converted: ${converted}, Skipped: ${skipped}`);
"""


def create_book(title, author, subtitle="", volume=None, num_chapters=14,
                base_dir=None, publisher="Bear Brown, LLC"):

    slug = slugify(title)
    if volume:
        slug = f"{slug}-vol{volume}"

    root = Path(base_dir).expanduser() / slug if base_dir else Path.cwd() / slug

    if root.exists():
        print(f"Error: {root} already exists.")
        sys.exit(1)

    # ── Directory structure ──────────────────────────────────────────────────
    dirs = [
        root / ".github" / "workflows",
        root / "styles",
        root / "chapters",
        root / "images",
        root / "d3",
        root / "SCRIPTS",
        root / "output",
        root / "pantry",
        root / "_working",
    ]
    for d in dirs:
        d.mkdir(parents=True)

    # ── SCRIPTS/svg-to-png.mjs ───────────────────────────────────────────────
    (root / "SCRIPTS" / "svg-to-png.mjs").write_text(SVG_TO_PNG_SCRIPT)

    # ── SCRIPTS/README.md ────────────────────────────────────────────────────
    (root / "SCRIPTS" / "README.md").write_text(
        """\
# SCRIPTS

Helper scripts run from the book root directory.

## svg-to-png.mjs

Converts every `images/**/*.svg` to a 300dpi PNG. Idempotent — skips
PNGs that are already newer than their SVG source.

```bash
node SCRIPTS/svg-to-png.mjs
```

**Requires:** `sharp` and `glob`

```bash
npm install sharp glob
```

`sharp` depends on `librsvg` for SVG rendering. All SVGs generated by
Cowork embed their fonts as base64 — no system font dependency.
"""
    )

    # ── d3/README.md ─────────────────────────────────────────────────────────
    (root / "d3" / "README.md").write_text(
        """\
# D3 Figures

Interactive browser-runnable D3 v7 versions of every figure in the book.

Each file is a standalone HTML file — open directly in a browser, no build step.

## Naming convention

```
{chapter-slug}-fig-{figure-number-zero-padded}.html
```

Examples:
- `02-chapter-01-fig-01.html`
- `07-comparison-charts-fig-05.html`

## Relationship to images/

The `images/` directory holds static PNG versions of the same figures,
used by the compiled EPUB. The D3 HTML files are the living source —
readers can open, inspect, and modify them.

## Regenerating

D3 HTML files are generated by Cowork during enrichment passes.
To regenerate, re-run the Cowork enrichment prompt against the chapter.

SVG → PNG conversion:
```bash
node SCRIPTS/svg-to-png.mjs
```
"""
    )

    # ── .gitignore ───────────────────────────────────────────────────────────
    (root / ".gitignore").write_text(
        "output/\n*.epub\n*.pdf\n*.docx\n.DS_Store\nnode_modules/\n"
    )

    # ── package.json ─────────────────────────────────────────────────────────
    (root / "package.json").write_text(
        f"""\
{{
  "name": "{slug}",
  "version": "1.0.0",
  "type": "module",
  "description": "{title}",
  "scripts": {{
    "svg-to-png": "node SCRIPTS/svg-to-png.mjs"
  }},
  "dependencies": {{
    "sharp": "^0.33.0",
    "glob": "^10.0.0"
  }}
}}
"""
    )

    # ── metadata.yaml ────────────────────────────────────────────────────────
    series_fields = ""
    if volume:
        series_fields = (
            f"\n# Series\nbelongs-to-collection: \"{title}\"\n"
            f"group-position: {volume}\n"
        )

    (root / "metadata.yaml").write_text(
        f"""---
title: "{title}"
subtitle: "{subtitle}"
author: "{author}"
language: en-US
rights: "Copyright © {date.today().year} {author}"
publisher: "{publisher}"
date: "{date.today().isoformat()}"
cover-image: cover.jpg
stylesheet: styles/kindle.css
toc: true
toc-depth: 2
{series_fields}---
"""
    )

    # ── styles/kindle.css ────────────────────────────────────────────────────
    (root / "styles" / "kindle.css").write_text(
        """\
body {
  font-size: 1em;
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

h1, h2, h3 {
  font-weight: bold;
  margin-top: 2em;
  margin-bottom: 0.5em;
  page-break-after: avoid;
}

h1 { font-size: 1.6em; }
h2 { font-size: 1.3em; }
h3 { font-size: 1.1em; }

p {
  margin: 0;
  text-indent: 1.5em;
}

h1 + p, h2 + p, h3 + p {
  text-indent: 0;
}

blockquote {
  margin-left: 2em;
  margin-right: 2em;
  font-style: italic;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
}

figure { margin: 1.5em 0; }
figcaption { font-size: 0.85em; text-align: center; }

table.infographic-table,
table.comparison-table,
table.data-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 0.9em;
  page-break-inside: avoid;
}

table.infographic-table thead tr {
  background-color: #1a1814;
  color: #f5f0e8;
}
table.infographic-table thead th {
  padding: 0.6em 0.8em;
  text-align: left;
  font-weight: bold;
  font-size: 0.95em;
  border: none;
}
table.infographic-table tbody tr {
  border-bottom: 1px solid #c8bfaa;
}
table.infographic-table tbody tr:last-child {
  border-bottom: 2px solid #1a1814;
}
table.infographic-table tbody td {
  padding: 0.65em 0.8em;
  vertical-align: top;
  line-height: 1.5;
}
table.infographic-table tbody td:first-child {
  font-weight: bold;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  white-space: nowrap;
  padding-right: 1em;
}

table.comparison-table thead tr {
  border-bottom: 2px solid #1a1814;
}
table.comparison-table thead th {
  padding: 0.6em 0.8em;
  text-align: left;
  font-weight: bold;
}
table.comparison-table tbody tr:nth-child(even) {
  background-color: #f0ebe0;
}
table.comparison-table tbody td {
  padding: 0.6em 0.8em;
  vertical-align: top;
  line-height: 1.5;
  border-bottom: 1px solid #c8bfaa;
}

table.data-table thead tr {
  border-bottom: 2px solid #1a1814;
}
table.data-table thead th {
  padding: 0.5em 0.75em;
  text-align: right;
  font-weight: bold;
}
table.data-table thead th:first-child {
  text-align: left;
}
table.data-table tbody td {
  padding: 0.45em 0.75em;
  text-align: right;
  border-bottom: 1px solid #c8bfaa;
  font-variant-numeric: tabular-nums;
}
table.data-table tbody td:first-child {
  text-align: left;
}
table.data-table tbody tr:last-child td {
  border-bottom: 2px solid #1a1814;
  font-weight: bold;
}

p.figure-kicker {
  font-size: 0.75em;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6b6254;
  margin-bottom: 0.25em;
  text-indent: 0;
}

/* Prompts section — appears at chapter end, not compiled into EPUB body */
.prompts-section {
  border-top: 2px solid #1a1814;
  margin-top: 3em;
  padding-top: 1.5em;
}
"""
    )

    # ── styles/kindle-book.css ───────────────────────────────────────────────
    (root / "styles" / "kindle-book.css").write_text(
        f"""\
/* ─────────────────────────────────────────────
   kindle-book.css — book-specific overrides
   Title: {title}
   Author: {author}
   ───────────────────────────────────────────── */
"""
    )

    # ── cover placeholder ────────────────────────────────────────────────────
    (root / "cover.jpg.placeholder").write_text(
        "Replace with cover.jpg — minimum 2560x1600px, 72dpi\n"
    )

    # ── chapters ─────────────────────────────────────────────────────────────
    subtitle_line = f"*{subtitle}*\n\n" if subtitle else ""

    (root / "chapters" / "00-frontmatter.md").write_text(
        FRONTMATTER_TEMPLATE.format(
            title=title,
            subtitle_line=subtitle_line,
            author=author,
            year=date.today().year,
            publisher=publisher,
        )
    )

    (root / "chapters" / "01-introduction.md").write_text(
        INTRODUCTION_TEMPLATE
    )

    for i in range(num_chapters):
        chapter_num = i + 1
        file_num = i + 2
        fname = f"{file_num:02d}-chapter-{chapter_num:02d}.md"
        (root / "chapters" / fname).write_text(
            f"# Chapter {chapter_num}\n\n"
            f"<!-- Chapter {chapter_num} draft.\n"
            f"     Replace this placeholder with your content.\n"
            f"     Use <!-- → [TYPE: description] --> comments to mark figures.\n"
            f"-->\n\n"
            f"[CHAPTER {chapter_num} CONTENT PLACEHOLDER]\n\n"
            f"---\n\n"
            f"## Prompts\n\n"
            f"<!-- This section is populated automatically by the Cowork enrichment\n"
            f"     pass. Each D3 figure generated in this chapter gets an entry here:\n"
            f"     the figure number, a short title, and a ready-to-paste prompt\n"
            f"     that produces a close approximation of that figure.\n\n"
            f"     Prerequisites: paste CLAUDE.md and DESIGN.md from the brutalist/\n"
            f"     folder before each prompt, or load them into your Claude project\n"
            f"     context once and reference them by name.\n"
            f"-->\n\n"
            f"*No figures have been generated for this chapter yet.*\n"
            f"*Run the Cowork enrichment pass to populate this section.*\n"
        )

    (root / "chapters" / "99-back-matter.md").write_text(
        BACK_MATTER_TEMPLATE
    )

    # ── book.md ───────────────────────────────────────────────────────────────
    (root / "book.md").write_text(
        BOOK_TEMPLATE.format(
            title=title,
            subtitle_line=subtitle_line,
            author=author,
        )
    )

    # ── outline.md ────────────────────────────────────────────────────────────
    chapter_outline_rows = ""
    for i in range(num_chapters):
        chapter_num = i + 1
        chapter_outline_rows += (
            f"{chapter_num}. **[Chapter {chapter_num} title]** — "
            f"[one-line description of the argument or move]\n"
        )

    (root / "outline.md").write_text(
        OUTLINE_TEMPLATE.format(
            title=title,
            subtitle_line=subtitle_line,
            author=author,
            chapter_outline_rows=chapter_outline_rows,
        )
    )

    # ── Tic TOC planning files ────────────────────────────────────────────────
    (root / "vision.md").write_text(
        VISION_TEMPLATE.format(
            title=title, subtitle_line=subtitle_line, author=author,
        )
    )
    (root / "architecture.md").write_text(
        ARCHITECTURE_TEMPLATE.format(
            title=title, subtitle_line=subtitle_line, author=author,
        )
    )
    (root / "chapters-spec.md").write_text(
        CHAPTERS_SPEC_TEMPLATE.format(
            title=title, subtitle_line=subtitle_line, author=author,
        )
    )
    (root / "risks.md").write_text(
        RISKS_TEMPLATE.format(
            title=title, subtitle_line=subtitle_line, author=author,
        )
    )

    # ── images placeholder ────────────────────────────────────────────────────
    (root / "images" / ".gitkeep").write_text("")

    # ── d3 placeholder ────────────────────────────────────────────────────────
    (root / "d3" / ".gitkeep").write_text("")

    # ── pantry ────────────────────────────────────────────────────────────────
    (root / "pantry" / ".gitkeep").write_text("")
    (root / "pantry" / "README.md").write_text(
        """\
# Pantry

Scratch storage for fragments, snippets, half-finished paragraphs,
quotes you might use, ideas you can't yet place, and anything else
that doesn't yet belong in a chapter.

Nothing in here gets compiled into the book. Move material into
`chapters/` when you're ready to use it.
"""
    )

    # ── build.sh ──────────────────────────────────────────────────────────────
    (root / "build.sh").write_text(
        f"""\
#!/bin/bash
set -e

BOOK_SLUG="{slug}"
METADATA="metadata.yaml"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

cat $METADATA chapters/*.md > "$OUTPUT_DIR/combined.md"

pandoc "$OUTPUT_DIR/combined.md" \\
  --from markdown \\
  --to epub3 \\
  --epub-cover-image=cover.jpg \\
  --css=styles/kindle.css \\
  --css=styles/kindle-book.css \\
  --toc --toc-depth=2 \\
  --output="$OUTPUT_DIR/$BOOK_SLUG.epub"

pandoc "$OUTPUT_DIR/combined.md" \\
  --from markdown \\
  --to html5 \\
  --standalone \\
  --css=styles/kindle.css \\
  --css=styles/kindle-book.css \\
  --toc \\
  --output="$OUTPUT_DIR/$BOOK_SLUG.html"

echo "Built: $OUTPUT_DIR/$BOOK_SLUG.epub"
echo "Built: $OUTPUT_DIR/$BOOK_SLUG.html"
"""
    )
    (root / "build.sh").chmod(0o755)

    # ── graphs.sh ─────────────────────────────────────────────────────────────
    (root / "graphs.sh").write_text(
        r"""#!/bin/bash
# graphs.sh — process <!-- → [TYPE: description] --> comments in chapters/
# Always run from repo root.
# For D3/SVG figures, Cowork enrichment handles generation.
# This script handles placeholder image creation and table rendering
# for rapid local iteration without Cowork.
#
# Usage:
#   ./graphs.sh                      # process all chapters
#   ./graphs.sh chapters/01-foo.md   # process one chapter
set -e

CHAPTERS_DIR="chapters"
IMAGES_DIR="images"
STYLES_DIR="styles"
KINDLE_BOOK_CSS="$STYLES_DIR/kindle-book.css"

for dir in "$CHAPTERS_DIR" "$IMAGES_DIR" "$STYLES_DIR"; do
  if [[ ! -d "$dir" ]]; then
    echo "Error: expected directory '$dir' not found." >&2
    exit 1
  fi
done

touch "$KINDLE_BOOK_CSS"

FILES=()
if [[ -n "$1" ]]; then
  FILES=("$1")
else
  while IFS= read -r -d '' f; do
    FILES+=("$f")
  done < <(find "$CHAPTERS_DIR" -maxdepth 1 -name "*.md" -print0 | sort -z)
fi

IMG_W=1600
IMG_H=900
IMG_BG="#d0cec8"
IMG_FG="#1a1814"
IMG_ACCENT="#9a7d3a"

uppercase() { echo "$1" | tr '[:lower:]' '[:upper:]'; }

ucfirst() {
  local str="$1"
  local first
  first=$(echo "${str:0:1}" | tr '[:lower:]' '[:upper:]')
  echo "${first}${str:1}"
}

truncate_desc() {
  local desc="$1"
  local first
  first=$(echo "$desc" | sed 's/ — .*//')
  if [[ ${#first} -lt ${#desc} && ${#first} -gt 10 ]]; then echo "$first"; return; fi
  if [[ ${#desc} -gt 80 ]]; then echo "${desc:0:77}..."; return; fi
  echo "$desc"
}

make_placeholder() {
  local filepath="$1"
  local fig_label="$2"
  local type_tag="$3"
  local short_desc="$4"
  local wrapped
  wrapped=$(echo "$short_desc" | fold -s -w 40)

  convert \
    -size ${IMG_W}x${IMG_H} xc:"$IMG_BG" \
    -font "Helvetica" \
    -pointsize 28 -fill "$IMG_ACCENT" -gravity North \
    -annotate +0+80 "${fig_label} — PLACEHOLDER" \
    -pointsize 18 -fill "$IMG_FG" -gravity North \
    -annotate +0+140 "$type_tag" \
    -pointsize 22 -fill "$IMG_FG" -gravity Center \
    -annotate +0-40 "$wrapped" \
    -strokewidth 3 -stroke "$IMG_ACCENT" -fill none \
    -draw "rectangle 40,40 $((IMG_W-40)),$((IMG_H-40))" \
    "$filepath" 2>/dev/null

  echo "    → image: $(basename "$filepath")" >&2
}

classify() {
  local type_tag
  type_tag=$(uppercase "$1")
  local description="$2"

  case "$type_tag" in
    TABLE)
      if echo "$description" | grep -qi "contrast\|vs\|versus\|comparison"; then
        echo "infographic-table"
      elif echo "$description" | grep -qi "data\|results\|measure\|count\|number\|rate\|score"; then
        echo "data-table"
      else
        echo "comparison-table"
      fi
      ;;
    INFOGRAPHIC)
      if echo "$description" | grep -qi "contrast\|vs\|versus\|comparison\|columns\|rows\|side.by.side\|properties"; then
        echo "infographic-table"
      else
        echo "image"
      fi
      ;;
    CHART)
      if echo "$description" | grep -qi "columns\|rows\|comparison\|vs"; then
        echo "data-table"
      else
        echo "image"
      fi
      ;;
    IMAGE|DIAGRAM|*)
      echo "image"
      ;;
  esac
}

render_table() {
  local description="$1"
  local fig_label="$2"
  local css_class="$3"

  local col1="Property"
  local col2="Value"

  if echo "$description" | grep -qi " vs\.* "; then
    col1=$(echo "$description" | sed 's/.*contrast of //i' | sed 's/ vs\.* .*//i' | sed 's/^ *//;s/ *$//')
    col2=$(echo "$description" | sed 's/.* vs\.* //i' | sed 's/ —.*//;s/ -.*//' | sed 's/^ *//;s/ *$//')
    col1=$(ucfirst "$col1")
    col2=$(ucfirst "$col2")
  fi

  echo ""
  echo "*${fig_label}*"
  echo ""
  echo "| | **${col1}** | **${col2}** |"
  echo "|---|---|---|"
  echo "| **Row 1** | _fill in_ | _fill in_ |"
  echo "| **Row 2** | _fill in_ | _fill in_ |"
  echo ""
  echo ": {.${css_class}}"
  echo ""
}

TOTAL_IMAGES=0
TOTAL_TABLES=0
TOTAL_SKIPPED=0
CSS_LOG=""

for CHAPTER_FILE in "${FILES[@]}"; do

  if ! grep -qE '<!-- → \[' "$CHAPTER_FILE"; then
    BASENAME=$(basename "$CHAPTER_FILE" .md)
    echo "Skipping: $BASENAME (no figure comments)" >&2
    TOTAL_SKIPPED=$((TOTAL_SKIPPED + 1))
    continue
  fi

  BASENAME=$(basename "$CHAPTER_FILE" .md)
  CHAPTER_SLUG="${BASENAME#chapter-}"
  CHAPTER_NUM=$(echo "$CHAPTER_SLUG" | grep -oE '^[0-9]+' | sed 's/^0*//')
  [[ -z "$CHAPTER_NUM" ]] && CHAPTER_NUM="0"

  OUT_FILE="${CHAPTERS_DIR}/${BASENAME}-updated.md"
  FIG_COUNT=0

  echo "" >&2
  echo "Processing: $BASENAME" >&2

  while IFS= read -r line; do
    if echo "$line" | grep -qE '<!-- → \['; then
      COMMENT_CONTENT=$(echo "$line" | sed 's/.*<!-- → \[//;s/\].*//')
      TYPE_TAG=$(echo "$COMMENT_CONTENT" | sed 's/:.*//' | tr -d ' ')
      DESCRIPTION=$(echo "$COMMENT_CONTENT" | sed 's/^[^:]*: *//')
      FIG_COUNT=$((FIG_COUNT + 1))
      FIG_LABEL="Figure ${CHAPTER_NUM}.${FIG_COUNT}"
      RENDER_AS=$(classify "$TYPE_TAG" "$DESCRIPTION")
      SHORT_DESC=$(truncate_desc "$DESCRIPTION")
      TYPE_UPPER=$(uppercase "$TYPE_TAG")

      if [[ "$RENDER_AS" == "image" ]]; then
        IMG_FILENAME="${CHAPTER_SLUG}-fig-$(printf "%02d" $FIG_COUNT).jpg"
        make_placeholder "${IMAGES_DIR}/${IMG_FILENAME}" \
          "$FIG_LABEL" "$TYPE_UPPER" "$SHORT_DESC"
        TOTAL_IMAGES=$((TOTAL_IMAGES + 1))
        echo "$line"
        echo ""
        echo "![${FIG_LABEL} — ${SHORT_DESC}](images/${IMG_FILENAME})"
        echo ""
        CSS_LOG="${CSS_LOG}\n/* ${FIG_LABEL} (${BASENAME}): image — replace ${IMG_FILENAME} */"
      else
        TOTAL_TABLES=$((TOTAL_TABLES + 1))
        echo "$line"
        render_table "$DESCRIPTION" "$FIG_LABEL" "$RENDER_AS"
        CSS_LOG="${CSS_LOG}\n/* ${FIG_LABEL} (${BASENAME}): .${RENDER_AS} */"
        echo "    → table (${RENDER_AS}): ${FIG_LABEL}" >&2
      fi
    else
      echo "$line"
    fi
  done < "$CHAPTER_FILE" > "$OUT_FILE"

  echo "  Written: $OUT_FILE" >&2
done

if [[ -n "$CSS_LOG" ]]; then
  {
    echo ""
    echo "/* ── graphs.sh run: $(date '+%Y-%m-%d %H:%M') ── */"
    printf "$CSS_LOG\n"
  } >> "$KINDLE_BOOK_CSS"
fi

echo "" >&2
echo "────────────────────────────────────────────" >&2
echo "Done." >&2
echo "  Skipped (no comments) : $TOTAL_SKIPPED" >&2
echo "  Tables rendered       : $TOTAL_TABLES" >&2
echo "  Images generated      : $TOTAL_IMAGES" >&2
echo "" >&2
echo "Review -updated.md files, then promote:" >&2
echo '  for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done' >&2
echo "────────────────────────────────────────────" >&2
"""
    )
    (root / "graphs.sh").chmod(0o755)

    # ── GitHub Actions workflow ───────────────────────────────────────────────
    (root / ".github" / "workflows" / "build.yml").write_text(
        f"""\
name: Build EPUB

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Pandoc
        run: sudo apt-get install -y pandoc

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Node dependencies
        run: npm install

      - name: Convert SVGs to PNG
        run: node SCRIPTS/svg-to-png.mjs

      - name: Build EPUB
        run: |
          mkdir -p output
          cat metadata.yaml chapters/*.md > output/combined.md
          pandoc output/combined.md \\
            --from markdown \\
            --to epub3 \\
            --epub-cover-image=cover.jpg \\
            --css=styles/kindle.css \\
            --css=styles/kindle-book.css \\
            --toc --toc-depth=2 \\
            --output=output/{slug}.epub

      - name: Upload EPUB as artifact
        uses: actions/upload-artifact@v4
        with:
          name: book-epub
          path: output/{slug}.epub
"""
    )

    # ── README.md ──────────────────────────────────────────────────────────────
    display_title = f"{title}: {subtitle}" if subtitle else title
    volume_line = f"**Volume:** {volume}\n" if volume else ""

    chapter_rows = "| 00-frontmatter.md | Front Matter | ☐ |\n"
    chapter_rows += "| 01-introduction.md | Introduction | ☐ |\n"
    for i in range(num_chapters):
        chapter_num = i + 1
        file_num = i + 2
        chapter_rows += f"| {file_num:02d}-chapter-{chapter_num:02d}.md | Chapter {chapter_num} | ☐ |\n"
    chapter_rows += "| 99-back-matter.md | Back Matter | ☐ |\n"

    (root / "README.md").write_text(
        f"""\
# {display_title}

**Author:** {author}
**Publisher:** {publisher}
{volume_line}**Status:** Draft
**Started:** {date.today().isoformat()}

## Structure

```
book.md                 ← book description and high-level outline
outline.md              ← chapter-level TOC
vision.md               ← Tic TOC Phase 1
architecture.md         ← Tic TOC Phase 2
chapters-spec.md        ← Tic TOC Phase 3
risks.md                ← Tic TOC Phase 4
pantry/                 ← scratch fragments
chapters/               ← markdown source
images/                 ← PNGs used by the EPUB (generated by Cowork/SCRIPTS)
d3/                     ← interactive D3 HTML figures (browser-runnable)
SCRIPTS/
    svg-to-png.mjs      ← converts images/**/*.svg to 300dpi PNG
```

## Chapters

| File | Title | Status |
|------|-------|--------|
{chapter_rows}
## Figures

Each chapter ends with a **Prompts** section containing ready-to-paste
prompts for recreating its D3 figures. Load `brutalist/CLAUDE.md` and
`brutalist/DESIGN.md` into your Claude project context before using them.

Cowork enrichment generates:
- `images/{slug}-fig-NN.svg` — static SVG (→ PNG for EPUB)
- `d3/{slug}-fig-NN.html` — interactive D3 HTML

Then convert SVGs to PNG:
```bash
node SCRIPTS/svg-to-png.mjs
```

Or via npm:
```bash
npm run svg-to-png
```

## Build

```bash
npm install        # first time only
./build.sh
```

Output goes to `output/` (gitignored).
"""
    )

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n✓ Created: {root}")
    print(f"  book.md, outline.md, vision.md, architecture.md")
    print(f"  chapters-spec.md, risks.md, pantry/")
    print(f"  chapters/00–99 ({num_chapters} body chapters + front/back matter)")
    print(f"  images/          (PNG figures — generated by Cowork)")
    print(f"  d3/              (interactive D3 HTML figures)")
    print(f"  SCRIPTS/svg-to-png.mjs")
    print(f"  package.json     (sharp + glob dependencies)")
    print(f"  Publisher: {publisher}")
    if volume:
        print(f"  Series: {title}, Volume {volume}")
    print(f"\nNext steps:")
    print(f"  cd {root}")
    print(f"  npm install")
    print(f"  git init && git add -A && git commit -m 'scaffold'")
    print(f"  # Fill in book.md and outline.md")
    print(f"  # Run Cowork enrichment to generate figures and populate Prompts sections")
    print(f"  # Run ./build.sh to produce EPUB\n")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new book project.")
    parser.add_argument("title",   help="Series or book title")
    parser.add_argument("author",  help="Author name")
    parser.add_argument("--subtitle",  default="",
                        help="Volume subtitle")
    parser.add_argument("--volume", type=int, default=None,
                        help="Volume number for a series")
    parser.add_argument("--chapters", type=int, default=14,
                        help="Number of body chapters (default: 14)")
    parser.add_argument("--dir", default=None,
                        help="Parent directory (default: current directory)")
    parser.add_argument("--publisher", default="Bear Brown, LLC",
                        help="Publisher name (default: Bear Brown, LLC)")
    args = parser.parse_args()
    create_book(args.title, args.author, args.subtitle, args.volume,
                args.chapters, args.dir, args.publisher)


if __name__ == "__main__":
    main()
