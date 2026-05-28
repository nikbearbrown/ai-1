# AI+1: AI Native Personalized Textbooks
## Learning Outcomes — /l1 output

---

## CHAPTER 1 — What AI+1 Is and Why It Works
*The domain research chapter. What AI is doing to the reader's profession. What remains irreducibly human. Why AI+1 preserves professional identity instead of replacing it.*

1. (Understand) Explain the difference between an AI+1 practitioner — someone who keeps their domain identity and adds AI fluency — and a generic AI user who loses it.
2. (Analyze) Run the three-LLM domain research prompt (Claude + GPT + Gemini) for their own field and identify the Tier 1 tasks AI handles well vs. the irreducibly human tasks AI cannot perform.
3. (Evaluate) Identify the fluency trap in their own domain — where AI output looks like professional-grade work but lacks the judgment that makes it defensible.
4. (Evaluate) Assess how AI is affecting the labor market and professional identity in their field, using the research output as evidence.

---

## CHAPTER 2 — What Tic TOC Does and Why You Spend Two Hours Here First
*The TIKTOC.md is not a form. It is the product. This chapter explains what Tic TOC is, how to deploy it, what the three disciplines enforce, and why the two-hour session is the highest-leverage step in the entire pipeline.*

1. (Understand) Explain what Tic TOC's three disciplines — curriculum theorist, acquisitions pragmatist, instructional designer — each contribute to a TIKTOC.md that a Cowork run can actually execute.
2. (Apply) Deploy Tic TOC: copy the system prompt, create a Claude Project, paste into Instructions, type /help, and begin /i1.
3. (Analyze) Distinguish between a TIKTOC.md that is ready for Cowork and one that has unresolved phase gate questions — and name what happens downstream when you skip a gate.
4. (Evaluate) Explain to a colleague why spending two hours in a structured Tic TOC session before any writing produces a better book faster than starting with a Cowork prompt.

---

## CHAPTER 3 — Domain Research: The Chapter Before the Chapter
*Before Tic TOC, you need to know how AI is affecting your field. This chapter produces that knowledge through a structured multi-LLM research prompt sent to Claude, GPT, and Gemini and combined.*

1. (Apply) Write and run a domain research prompt structured around: AI tool adoption by role, AI failure modes, the irreducibly human taxonomy, and the fluency trap — for a specific professional domain.
2. (Analyze) Combine outputs from three LLMs into a single synthesized research document, noting where the models agree, where they diverge, and where the divergence reveals a contested claim.
3. (Evaluate) Assess the research output for fluency trap examples — AI-generated content that looks authoritative but would not survive expert review.
4. (Create) Produce a domain research brief that is ready to bring into a Tic TOC /i1 session as the primary input.

---

## CHAPTER 4 — Tic TOC: Generating Your TIKTOC.md
*The two-hour session. This chapter walks through the full Tic TOC pipeline — /i1 through /g1 — using ai-for-designers-a-practitioners-guide as the running example.*

1. (Apply) Complete the full Tic TOC intake sequence (/i1–/i4) for a real book project, producing a confirmed Book Concept Summary with thesis, learner profile, and deployment context.
2. (Apply) Build the learning architecture (/l1–/l4): outcomes in Bloom's format, sequencing model, three-act arc, prerequisite dependency map.
3. (Apply) Document every chapter (/c1–/c4): capability statement, opening strategy, worked example, assessable exercises, bridge question.
4. (Evaluate) Run the 7 Adoption Failure Mode diagnostic (/g2) on a completed TIKTOC.md draft and identify the highest-risk structural problem before handing off to Cowork.
5. (Create) Produce a TIKTOC.md that is complete enough for Cowork to run without a clarifying conversation.

---

## CHAPTER 5 — Book Scaffold: new_book.py
*One command. The directory structure, the metadata, the build script, the Tic TOC planning files — all generated in under a minute. This chapter explains what gets created and why each piece exists.*

1. (Apply) Run `new_book.py` with correct arguments to scaffold a new book directory for their project.
2. (Understand) Explain the purpose of each generated file and directory: `book.md`, `TIKTOC.md`, `vision.md`, `architecture.md`, `chapters-spec.md`, `risks.md`, `pantry/`, `chapters/`, `images/`, `d3/`, `SCRIPTS/`, `build.sh`.
3. (Apply) Populate `metadata.yaml` correctly: title, subtitle, author, publisher, ISBN placeholder, series fields.
4. (Analyze) Identify which scaffold files Cowork reads at runtime vs. which are for the human author's reference only.

---

## CHAPTER 6 — Research Pass: Pantry Population
*Cowork reads the TIKTOC.md, scans a shared markdown library, does deep web research per chapter, and saves structured notes to pantry/. This chapter explains what gets generated and how to evaluate whether the pantry is ready for drafting.*

1. (Apply) Run the Chapter Research Gatherer prompt against a book directory with a populated TIKTOC.md and confirm the pantry output.
2. (Analyze) Evaluate a pantry research file for quality: primary sources vs. aggregators, settled vs. contested claims, domain examples appropriate for the target reader.
3. (Evaluate) Identify thin-pantry chapters — chapters where research is too sparse to support a full draft — and decide whether to supplement manually or accept the flag.
4. (Understand) Explain what the pantry is for: it is reference material for drafting, not citation — chapter claims still require primary sources.

---

## CHAPTER 7 — Chapter Writing: The Cowork Draft Run
*Cowork reads the TIKTOC.md and pantry, audits which chapters are missing, and drafts every unwritten chapter in the Attenborough × Feynman voice. This chapter explains what to expect from the run and how to read the output.*

1. (Apply) Run the Chapter Writer prompt against a populated book directory and confirm the draft output in `chapters/`.
2. (Understand) Explain what the Attenborough × Feynman voice produces: scene-first openings, first-principles explanations, named trade-offs, scale oscillation — and why it is the default for AI+1 books.
3. (Analyze) Read a Cowork chapter draft and identify: what the prompt did well, what it got wrong, where it padded, and where domain expertise is missing.
4. (Evaluate) Assess whether a chapter draft is a solid foundation for human rewrite or a thin draft that needs pantry supplementation before the rewrite is worthwhile.

---

## CHAPTER 8 — The Human Rewrite: The Seam
*Everything before this step is AI-driven. Everything after it depends on this step being done. The human rewrite is not polish — it is the gate. This chapter explains what to look for, what Cowork reliably gets wrong, and what the human author must supply.*

1. (Analyze) Identify the five things Cowork reliably gets wrong in a chapter draft: voice drift, fabricated specificity, missing domain judgment, padded middle sections, and bridge questions that don't actually bridge.
2. (Evaluate) Apply the Combined Test checklist to a chapter draft before beginning the rewrite: cold open, trade-off named, scale shift present, exercises graduated, no forbidden phrases.
3. (Apply) Use the writing-guide companion book as the primary rewrite reference — this chapter points there explicitly for craft instruction.
4. (Create) Produce a revised chapter that passes the Combined Test and reads in the author's voice, not the model's.

---

## CHAPTER 9 — Finishing Pass and Figures
*Subtitles, visual placeholders, CAJAL figure intelligence, SVG generation, enrichment. This chapter explains the finishing pipeline and when to run each step — and points to ai-for-graphs and ai-for-infographics for the craft of figures.*

1. (Apply) Run the Chapter Finishing Pass to insert italic subtitles and visual placeholder comments across all chapters.
2. (Apply) Run CAJAL Image Suggest to generate a figure intelligence plan — one `*-cajal.md` file per chapter in `pantry/`.
3. (Apply) Run the CAJAL SVG Generator to produce static SVGs and convert to 300 DPI PNG via `node SCRIPTS/svg-to-png.mjs`.
4. (Apply) Run the Chapter Enrichment pass (NEU or Brutalist variant) to convert table and figure comments into rendered content, D3 HTML files, and populated Prompts sections.
5. (Evaluate) Use ai-for-graphs-a-practitioners-guide and ai-for-infographics-a-practitioners-guide as the primary references for figure craft decisions — this chapter points there explicitly.

---

## CHAPTER 10 — Enrichment: The LLM Layer
*Dig Deeper prompts, LLM Exercises, AI Wayback Machine, Running Project. This chapter adds the AI+1 interactive layer that makes the book native to the format.*

1. (Apply) Run the "With LLMs" Curriculum Enrichment Generator to add Dig Deeper prompts and LLM Exercises to every chapter.
2. (Understand) Explain the difference between a Dig Deeper prompt (optional rabbit hole, no deliverable) and an LLM Exercise (project-advancing, produces a concrete artifact).
3. (Apply) Run the AI Wayback Machine Section Generator to add one historical figure per chapter, with copy-paste-ready prompts and Wikipedia instructions.
4. (Evaluate) Review the enriched chapters against the AI+1 standard: is every LLM Exercise domain-specific and hands-on, or does it produce generic output that could belong to any book?

---

## CHAPTER 11 — Final Check and Build: EPUB + PDF
*The build script produces a Kindle-ready EPUB and PDF. This chapter explains the final check sequence, the rebuild loop, and what Kindle Direct Publishing requires.*

1. (Apply) Run the Fact-Checking Assistant across all chapters and triage the output: OUTDATED and CONTRADICTED findings first, UNVERIFIED second.
2. (Apply) Run `./build.sh` to produce `output/{slug}.epub` and the HTML version, confirming the build completes without errors.
3. (Apply) Upload the EPUB to Kindle Direct Publishing, selecting KDP Select for 90-day ebook exclusivity, and confirm the metadata from `metadata.yaml` populates correctly.
4. (Analyze) Identify which changes after a human review require a full rebuild vs. which can be made in the chapter files and rebuilt immediately — understanding the rebuild loop as a normal part of the process, not a failure.
5. (Evaluate) Assess the finished book against the AI+1 standard: does it preserve the author's domain identity, add genuine AI fluency, and avoid the fluency trap in its own exercises?

---

## OUTCOME MAP

| Chapter | Title | Bloom's Ceiling | Assessable? | Maps to Pipeline Stage |
|---------|-------|----------------|-------------|------------------------|
| 1 | What AI+1 Is and Why It Works | Evaluate | Yes | Domain research |
| 2 | What Tic TOC Does | Evaluate | Yes | TIKTOC.md session |
| 3 | Domain Research | Create | Yes | Pre-Tic TOC input |
| 4 | Generating Your TIKTOC.md | Create | Yes | Tic TOC → TIKTOC.md |
| 5 | Book Scaffold | Apply | Yes | new_book.py |
| 6 | Research Pass | Evaluate | Yes | Pantry population |
| 7 | Chapter Writing | Evaluate | Yes | Cowork draft run |
| 8 | The Human Rewrite | Create | Yes | The seam |
| 9 | Finishing Pass and Figures | Evaluate | Yes | CAJAL + enrichment |
| 10 | Enrichment: The LLM Layer | Evaluate | Yes | With LLMs pass |
| 11 | Final Check and Build | Evaluate | Yes | Build → Kindle |

**Bloom's distribution:**
- Understand: Chapters 1, 2, 5, 6, 7, 10 (supporting outcomes)
- Apply: Chapters 3, 4, 5, 6, 7, 9, 10, 11 (primary pipeline execution)
- Analyze: Chapters 1, 3, 6, 7, 8, 9, 11
- Evaluate: Chapters 1, 2, 3, 6, 7, 8, 9, 10, 11
- Create: Chapters 3, 4, 8 (the three highest-judgment steps)

**No chapter has an outcome below Apply as its ceiling.**
**Create-level outcomes are concentrated at the three highest-judgment steps: domain research brief, TIKTOC.md, and human rewrite.**
**Every outcome is assessable — each maps to a concrete deliverable the author-instructor can hold in their hand.**
