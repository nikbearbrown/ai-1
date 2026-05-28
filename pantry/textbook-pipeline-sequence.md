# Textbook Production Pipeline — Prompt Sequence Guide

These prompts form an end-to-end pipeline for building, enriching, and finishing textbooks in the bear-textbooks workshop. Below they are sequenced in the order you'd run them on a new book, with a plain-language description of what each does and when to use it.

---

## Phase 0 — Book Structure Setup

These run once, at the start, before any writing happens.

---

### 0.1 TIKTOC-Driven Write or Rewrite
*Trigger: you have source chapters OR a TIKTOC.md but no structured book yet*

Reads the book's `TIKTOC.md` (the table of contents and chapter brief) and either writes every chapter from scratch or rewrites existing ones using the Attenborough × Feynman voice. If `97-fundamental-themes.md` exists, it weaves those themes through all chapters and then converts that file into a proper appendix. If no TIKTOC.md exists, it builds one from whatever chapters are already in `chapters/`. This is the master writing pass — the one that actually drafts the book.

**Use when:** starting a new book, doing a full rewrite, or promoting a draft collection to a coherent manuscript.

---

### 0.2 Book Chapter Conversion Workflow — Attenborough × Feynman
*Trigger: source material lives in numbered subfolders inside `chapters/`*

Walks each subfolder (e.g., `chapters/03-probability/01-source.md`, `02-source.md`…), merges the source files, rewrites them in the Attenborough × Feynman style, saves a flat chapter file, and removes the subfolder only after verification passes. Also generates three companion files per chapter: a `pantry/` file of reusable ingredients, an `images/` file of figure briefs, and a `bookmaps/` file tracing which source contributed what. Ends with a word-count report and flags chapters that are too thin.

**Use when:** source material arrived as chunked subfolders (e.g., from an OpenStax import, a student submission batch, or a prior conversion pass that left raw sources in place).

---

### 0.3 Front Matter, Back Matter, and README Templates
*Trigger: first edition setup*

Writes three files from templates: `00-frontmatter.md` (title page, copyright, dedication, preface), `00-introduction.md` (the reader's roadmap — cold open, central argument, chapter-by-chapter map, note about AI), and `99-back-matter.md` (acknowledgments, author bio, notes, references, glossary). After writing the introduction, it uses the introduction + TOC + copyright to generate a `README.md`, and uses the front matter + copyright to generate a `LICENSE.md`.

**Use when:** creating a new book for the first time, or standardizing front/back matter on an existing one.

---

### 0.4 README Generator (batch, all books)
*Trigger: periodic maintenance across all books*

Walks every subdirectory under `books/`, qualifies books with 10 or more chapter files, and creates or updates the `README.md` at each book's root. Uses a standard template: title, author, what the book is, who it's for, how to read it, a dynamic table of contents from actual chapter files, a simulations/exercises table, companion resources, author bio, copyright. Appends missing sections to existing READMEs without touching sections already present.

**Use when:** a book is missing a README, or after a writing pass that added chapters.

---

## Phase 1 — Research

These run before or during writing to populate the `pantry/` with source material.

---

### 1.1 Chapter Research Gatherer
*Trigger: TIKTOC.md exists, pantry is empty*

Reads `TIKTOC.md`, extracts the chapter list, scans a shared markdown library at `/Users/bear/Documents/CoWork/bear-textbooks/MD` for any already-existing relevant files (copies them to `pantry/` prefixed `_lib_`), then does deep web research per chapter — conceptual foundations, real-world cases, field consensus vs. contested claims, key references, teaching considerations, AI Wayback Machine figure candidates — and saves one structured notes file per chapter to `pantry/`. Ends with a pantry index and a terminal summary.

**Use when:** starting research for a new book before drafting begins.

---

### 1.2 Chapter Research Pass (generic)
*Trigger: TIKTOC.md exists; more detailed pass than 1.1*

Similar to 1.1 but generates more detailed per-chapter research files with nine sections: primary sources, state of the field (settled vs. contested vs. recent), application domain examples, connection to book thesis, AI Wayback Machine candidates, pedagogical delivery research, representation/display research, open questions, and sourcing notes. Runs in chapter order so later chapters can reference what earlier chapters established.

**Use when:** you need deeper source scaffolding, especially for contested or rapidly evolving fields.

---

## Phase 2 — Chapter Writing

---

### 2.1 Chapter Writer (TIKTOC-driven, generic)
*Trigger: TIKTOC.md + pantry are populated*

Reads `TIKTOC.md` and `book.md`, audits which chapters are already in `chapters/` (skips them), reads the pantry notes for each missing chapter, and drafts every unwritten chapter using the book's voice and a default eight-section structure: learning objectives, opening case, core concept, worked example, common misconceptions, exercises, "what would change my mind," and "still puzzling." Logs each chapter to `logs/log.csv` with word count, source count, and `[verify]` flag count.

**Use when:** pantry research is done and you're ready for a first full draft pass.

---

### 2.2 Case Textbook Refresh (theory spine + student cases)
*Trigger: student project files are in pantry, new semester*

Specialized for case-layer books. Reads the syllabus and catalogs student project files from `pantry/`, presents a batch plan, then writes one case chapter per project (seven-section structure: situation, architecture, design rationale, trade-offs, outcomes, pattern connection, transfer prompts) plus a hero-image brief. Reports failed project targets honestly — no flattery. Writes `00-introduction.md` last, after all cases are drafted, naming every student author.

**Use when:** refreshing a rotating case layer on a stable theory-spine textbook each semester.

---

### 2.3 Branding and AI Chapter Writer (book-specific)
*Trigger: outline.md exists for `branding-and-ai` book*

Walks the book's outline, finds every chapter marked `to write`, reads `book.md` + `CLAUDE.md` + pantry, does web research (5–10 primary sources minimum per chapter), drafts using the Feynman voice plugin and eight-section format, saves dated drafts to `chapters/`, updates `outline.md` status, and logs to `logs/log.csv`. Handles path-fork chapters (personal brand vs. startup brand variants) as two separate files. Keeps going until every `to write` chapter is drafted or genuinely blocked.

**Use when:** working specifically on the `branding-and-ai` book with its outline-driven structure.

---

## Phase 3 — Finishing and Polish

These run on completed chapter files before the visual layer.

---

### 3.1 Chapter Finishing Pass
*Trigger: chapters drafted, pre-enrichment cleanup*

Applies two additions to each chapter file without touching any prose: (1) inserts an italic subtitle on the line below the main heading, if one is missing — compressed to a single hook phrase that surfaces the chapter's central tension; (2) inserts inline HTML comments marking where tables, images, infographics, or charts would belong, with specific descriptions (not generic category labels). Saves the modified file back in place.

**Use when:** chapters are drafted but need subtitle hooks and visual placeholders before the enrichment pass.

---

### 3.2 Visual Suggestion Scan
*Trigger: chapters drafted, looking specifically for D3/SVG opportunities*

Reads each chapter and inserts `<!-- → [TYPE: description] -->` HTML comments at every location where a data visualization (infographic or chart) would genuinely serve comprehension. Types are `INFOGRAPHIC` (structured diagram, flow, or taxonomy) and `CHART` (quantitative or relational). Descriptions must name the specific content, not the generic category. Only suggests visuals that would be rendered as SVG or D3.

**Use when:** you want a targeted visual-opportunity pass before CAJAL or the enrichment step.

---

### 3.3 Add "A Note about AI" (if warranted)
*Trigger: chapters written; book has an LLM layer*

Evaluates each chapter to decide whether a short voice-bearing essai (250–500 words) about what an LLM can and cannot do for this specific craft is warranted. Does NOT insert a generic AI disclaimer — only writes the section when the chapter teaches a craft that an LLM can simulate in texture but not in substance (e.g., the profile, the literacy narrative). Uses two structural templates: one for confident readings (what the model helps with, what it damages, one unifying rule) and one for genuinely unsettled questions (names the tension, refuses to issue a rule). Places the section immediately above the exercises heading.

**Use when:** preparing a writing-craft or methods textbook for the LLM layer; skip for purely technical chapters.

---

## Phase 4 — Figure Intelligence (CAJAL)

These generate and manage illustration suggestions and actual SVG/PNG figures.

---

### 4.1 CAJAL Image Suggest
*Trigger: chapters complete; need illustration plan*

Runs CAJAL in silent mode on every chapter file. For each chapter, detects three types of figure opportunities: MC (mechanism/process complexity — 3+ interdependent steps), VG (verification gap — structural claims that can't be verified from text alone), and PQ (proportional/quantitative — any percentages, ratios, or comparative data). Generates full SCOPE prompts (Specification, Content, Organization, Presentation, Exclusions) for every recommended figure, ranked Critical / Important / Supplementary. Runs a video candidate pass at the end. Saves one `{chapter-slug}-cajal.md` file per chapter to `pantry/`.

**Use when:** chapters are written and you need a systematic illustration plan before generating any actual SVGs.

---

### 4.2 CAJAL SVG Generator
*Trigger: `pantry/*-cajal.md` files exist*

Reads every `*-cajal.md` file from `pantry/`, parses all figure entries, generates a real static SVG for each (no placeholder text — every label inferred from content), embeds full metadata (book, chapter, figure title, type, source file, date) in a non-rendering metadata block, saves to `images/{chapter-slug}-fig-{NN}.svg`, then runs `node SCRIPTS/svg-to-png.mjs` to convert all new SVGs to 300 DPI PNG. Logs everything to `pantry/cajal-svg-log.md`. Does NOT touch chapter files.

**Use when:** CAJAL suggestions exist and you want actual SVG/PNG files before the enrichment pass.

---

## Phase 5 — Chapter Enrichment

These are the main enrichment passes that transform placeholder comments into rendered content and insert LLM integration.

---

### 5.1 Chapter Enrichment: Tables and Figures — Bear Brown / Brutalist
*Trigger: chapters have `<!-- → [TABLE:` and `<!-- → [IMAGE:` comments*

The main enrichment pass for Brutalist-branded books. Three passes: (1) converts all TABLE comments into complete GitHub-Flavored Markdown tables with real content; (2) converts all IMAGE/FIGURE/DIAGRAM/INFOGRAPHIC/CHART comments into a static SVG (saved to `images/`), an interactive D3 v7 HTML file (saved to `d3/`), a markdown image link inserted in the chapter, and a structured Prompts entry; (3) checks `pantry/` for CAJAL-generated PNGs not yet referenced in the chapter and inserts them at the best semantic location. Ends by running `node SCRIPTS/svg-to-png.mjs`. Uses the Brutalist D3 color palette (ink `#2a1a0e`, red `#C8102E`, ochre `#C8860E`) and EB Garamond + Inter + JetBrains Mono font stack.

**Use when:** building Bear Brown / Brutalist-branded books.

---

### 5.2 Chapter Enrichment: Tables and Figures — Northeastern University (NEU)
*Trigger: same as 5.1, but for NEU-branded books*

Identical pipeline to 5.1 but uses Northeastern University brand: red `#C8102E`, gold `#A4804A` (decorative only, 3% proportion), ink `#000000`, and Real Head Pro / FF Real / Lato font stack throughout. White chart area (not tinted). No JetBrains Mono for chart text — Real Head Pro for everything except code blocks.

**Use when:** building books for Northeastern University courses.

---

### 5.3 Walk All Books and Add Images (batch)
*Trigger: periodic enrichment across all books*

Walks all book subdirectories under `books/`, applies the enrichment pass (using NEU guidelines from `/Users/bear/Documents/Cowork or Codex/bear-textbooks/NEU`) to every chapter in every book. Overwrites any existing graphics.

**Use when:** doing a sweep enrichment pass across the full textbook library.

---

### 5.4 "With LLMs" Series — Curriculum Enrichment Generator
*Trigger: chapters complete; adding LLM layer to an existing textbook*

Three-phase enrichment specifically for the "with LLMs" book series. First, detects book state (A: written flat chapters / B: source subfolders / C: external/OpenStax source) and writes chapters if needed. Then generates **Chapter 00: Claude Basics** — a full onboarding chapter explaining both prompt types (Dig Deeper and LLM Exercises), when to use Claude vs. Claude Project vs. Claude Code vs. Cowork, a worked example, and Claude's field-specific failure modes. Proposes 3–5 candidate running projects (pauses for selection), then enriches every chapter with 2–4 inline **Dig Deeper** prompts (optional rabbit holes) and one **LLM Exercise** at chapter end (advancing the running project). Updates the TOC and `_notes.md`.

**Use when:** adapting any existing textbook to the "with LLMs" series format, or building a new one from scratch.

---

### 5.5 Running Project Exercise Generator
*Trigger: "FIELD and AI" textbook; chapters written*

Simpler version of 5.4's exercise layer. Reads all chapters, builds a Chapter Map, proposes 3–5 running projects (pauses for selection), then generates one end-of-chapter LLM Exercise per chapter that advances the selected project — copy-paste ready, with adaptation notes for different domains, tools, and LLMs. No Dig Deeper prompts (that's the "with LLMs" version above).

**Use when:** adding LLM exercises to a "FIELD and AI" textbook without the full "with LLMs" enrichment pass.

---

### 5.6 AI Wayback Machine Section Generator
*Trigger: chapters enriched; adding historical-figure layer*

For each chapter, identifies one lesser-known historical figure (diverse by gender, nationality, discipline, era) whose work substantively connects to the chapter's concept. Inserts a `## AI Wayback Machine` section after the LLM Exercise block: a one-sentence framing, a copy-paste-ready Claude prompt to learn about the figure, a Wikipedia search instruction, and 2–3 specific suggestions for making the prompt better. Maintains a diversity tracker across all chapters and produces a summary of gender, national, era, and discipline representation at the end.

**Use when:** the book has an LLM Exercise layer and you want to add the historical-figure prompting practice.

---

## Phase 6 — Quality Control

---

### 6.1 Fact-Checking Assistant
*Trigger: chapters complete, pre-publication review*

Scans all chapter files and classifies every assertion by type (Basic, Emphatic, Positive, I-Language, Combination) and content category (STAT, GUIDELINE, APPROVAL, EVIDENCE, SPECIALIST, CURRENT). For each flagged sentence, visits authoritative sites (PubMed, FDA, NCCN, SEER, GLOBOCAN, WHO, field-specific equivalents) and records what was found. Writes one `factchecks/{chapter}-assertions.md` file per chapter and inserts inline `<!-- FACT-CHECK FLAG -->` comments into chapter files for any OUTDATED, CONTRADICTED, or UNVERIFIED assertions. Writes a `factchecks/MASTER_REPORT.md` with all critical findings sorted by priority.

**Use when:** the manuscript is nearing completion and claims need verification before publication.

---

## Pipeline Order Summary

```
0.1  TIKTOC-Driven Write / Rewrite         ← if starting from scratch
0.2  Conversion Workflow (A×F)             ← if source is in subfolders
0.3  Front Matter / Back Matter / README   ← once per book edition
0.4  README Generator (batch)              ← periodic maintenance

1.1  Research Gatherer                     ← before drafting
1.2  Research Pass (detailed)              ← for contested/evolving fields

2.1  Chapter Writer (generic)              ← main draft pass
2.2  Case Textbook Refresh                 ← semester case layer
2.3  Branding and AI Writer                ← book-specific

3.1  Chapter Finishing Pass                ← subtitles + visual placeholders
3.2  Visual Suggestion Scan                ← D3/SVG opportunity scan
3.3  Add "A Note about AI"                 ← craft/methods books only

4.1  CAJAL Image Suggest                   ← illustration plan
4.2  CAJAL SVG Generator                   ← actual SVG/PNG files

5.1  Enrichment: Bear Brown / Brutalist    ← tables + figures + D3 + prompts
5.2  Enrichment: NEU                       ← NEU brand version
5.3  Walk All Books (batch enrichment)     ← library sweep
5.4  "With LLMs" Curriculum Enrichment     ← full LLM layer
5.5  Running Project Exercise Generator    ← exercises only (lighter)
5.6  AI Wayback Machine Generator          ← historical-figure layer

6.1  Fact-Checking Assistant               ← pre-publication QC
```

---

## A Few Notes on Flexibility

**The phases are not all required.** A lean path for a new book might be: 0.3 → 1.1 → 2.1 → 3.1 → 4.1 → 5.1 (or 5.2) → 6.1.

**The "with LLMs" enrichment (5.4) subsumes 5.5.** Use 5.4 for the full series format; use 5.5 if you only want exercises without Dig Deeper prompts or Chapter 00.

**CAJAL is two-step.** Step 4.1 (Image Suggest) writes a plan to `pantry/`. Step 4.2 (SVG Generator) reads that plan and makes actual files. You can run 4.1, review and edit the CAJAL files, then run 4.2 — giving you editorial control over the figure selection before any SVGs are generated.

**Brand variants matter.** The enrichment passes in 5.1 (Brutalist) and 5.2 (NEU) are not interchangeable — they use different color palettes, font stacks, and chart area treatments. Always run the one that matches the book's brand spec.
