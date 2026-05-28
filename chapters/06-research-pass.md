# Chapter 6 — Research Pass: Pantry Population

*The pantry is not a draft and it is not a citation list. It is the only thing standing between Cowork and an authoritative-sounding lie.*

**Capability — one line:** Students run the Chapter Research Gatherer and evaluate the pantry output — distinguishing research-ready chapters from thin ones needing supplementation.

**Learning objectives**

- (Apply) Run the Chapter Research Gatherer so one notes file lands in `pantry/` for every chapter in your TIKTOC.md.
- (Analyze) Read a notes file against four sharp questions and identify the strongest primary source, one claim that needs verification, and whether the domain examples match your reader.
- (Evaluate) Triage every chapter as draft-ready, thin (supplement), or thin (return to Tic TOC) with a stated reason.

---

## Opening — a pantry file that looks thorough and isn't

You ran the Chapter Research Gatherer last night. This morning you open `pantry/ch-03-domain-research.md`. It looks substantial. Nine sections, three pages, dozens of bullet points. Here is what the first four sections actually contain.

> **1. Primary Sources.**
> - According to a 2024 article, "AI is transforming graphic design" — most designers will need to adopt new tools or face displacement. *(source: a Medium post by an account with 3 followers; no further citation)*
> - "Studies show 78% of design firms are integrating AI." *(no study named; no year; no methodology)*
> - The McKinsey Global Institute has reported significant productivity gains from generative AI. *(no specific McKinsey report; no page; no figure)*

> **3. Application Domain Examples.**
> - Consider a marketing team using AI to write blog posts.
> - A small business owner could use ChatGPT to design a logo.
> - Educators are exploring how AI changes lesson planning.

> **9. Sourcing Notes.**
> Sources include articles from Forbes, Medium, LinkedIn, and a number of industry blogs. Primary sources were prioritized.

Read it again. There is one primary source — a McKinsey reference too vague to find. The percentage is unattributed. The "Studies show" construction is the tell. Section 3 has no graphic designers in it. Section 9 claims primary sources were prioritized while citing four aggregators.

This is the pantry the Gatherer produced for a chapter on AI's impact on graphic design. Cowork will read this file in two days. It will draft an authoritative-sounding chapter about AI and graphic design that cites no graphic designers, references percentages no one can check, and uses examples from marketing, small business, and education — every domain except the one the book is about.

This is what the chapter exists to prevent.

Compare to the same chapter's pantry after the four-questions evaluation pass. Section 1 names the Adobe Firefly 3 release notes (March 2024, version-specific feature list), the Hoffmann & Wallace 2023 *Journal of Design Research* paper on AI-augmented studio workflows, and the Adobe Creative Cloud 2024 customer report (cited by document title, section, and date). Section 3 has five examples drawn from graphic design — brand identity, editorial layout, motion design, packaging, product lockups. Section 9 names specifically what was filtered out: aggregator summaries, undated trend reports, and posts that quoted unidentified studies.

The first pantry is a fluency-trap delivery vehicle. The second is research infrastructure. Same chapter, same TIKTOC.md, same Gatherer run. The difference is what you did after the script finished.

---

## What the Chapter Research Gatherer does

The Gatherer is a Cowork prompt, not a separate piece of software. You give it your TIKTOC.md and your `chapters-spec.md`. It does three things, in order, for every chapter on the list.

1. **It reads the chapter spec.** The capability statement, the learning outcomes, the bridge question, the application domain. This determines what it is looking for.
2. **It scans your shared library.** Any file in `pantry/` whose name starts with `_lib_` is treated as shared context — glossary, recurring framework definitions, your house position on contested claims. The Gatherer consults but does not duplicate.
3. **It runs web research and writes a nine-section notes file.** One file per chapter, saved as `pantry/research-ch-XX-<chapter-slug>.md`. The nine sections are: (1) Primary Sources, (2) State of the Field, (3) Application Domain Examples, (4) Book's Thesis Connection, (5) AI Wayback Machine Candidates, (6) Pedagogical Delivery Research, (7) Representation and Display Research, (8) Open Questions and Research Gaps, (9) Sourcing Notes.

This is a research synthesis task in Cooper's sense [Cooper, Harris M., 1982, "Scientific Guidelines for Conducting Integrative Research Reviews," *Review of Educational Research* 52(2)]. Cooper named five stages — problem formulation, data collection, evaluation, analysis, presentation — and argued that compressing them was the move that hid the work. The Gatherer compresses Cooper's first three stages into one prompt. The two it cannot compress are *evaluation* and *analysis*. Those are yours. The four-questions pass below is where Cooper's missing stages get re-added by hand.

A note on technology. The Gatherer is built on a long-context model with retrieval — what the literature now calls a "Deep Research" agent (a generation of tools shipped by Anthropic, OpenAI, and Google between 2024 and 2025). Retrieval-augmented generation has moved citation fabrication from "about half the time" [Goddard, Joel et al., 2023, "Hallucination in ChatGPT: A Cross-Disciplinary Investigation of References and Bibliographies"; Bhattacharyya, Mehul et al., 2023, "High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content," *Cureus* 15(5)] to "fabricated when retrieval misses or the source is poorly indexed." The improvement is real. The risk is not gone.

There is also a structural reason fabrication persists: language models trained on aggregate text model the *surface form* of citation — author-year-title shapes — without modeling the act of citing [Bender, Emily M. et al., 2021, "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?", FAccT '21]. Citation-shaped text is cheap. Verified citation is not. The pantry must be evaluated by someone who can tell the difference. That is the chapter's load-bearing claim.

---

## How to evaluate a notes file — four questions before draft-ready

You will read each pantry file once. Mike Caulfield's SIFT method [Caulfield, Mike, 2017, *Web Literacy for Student Fact-Checkers*, CC-BY] gave undergraduates four moves — Stop, Investigate the source, Find better coverage, Trace claims. The CRAAP test [Blakeslee, Sarah, 2004, CSU Chico Meriam Library] gave them five — Currency, Relevance, Authority, Accuracy, Purpose. Both are too many to apply to fifteen pantry files in one sitting. The four below are adapted from SIFT, sharpened for AI-generated research notes, and small enough to be habitual.

**Question 1 — Is the strongest source primary or secondary?**

Open Section 1. Find the source the Gatherer is leaning on most heavily. Is it a primary source — a study, a release note, a dataset, a court ruling, an organization's own publication? Or is it a secondary source — an article *about* a study, a blog post summarizing a report, a trend piece? If the strongest source in Section 1 is a Medium post or a Forbes article, the chapter is thin even if every other section looks full. Section 1 is the load-bearing slot. A thin Section 1 means Cowork will draft on summaries of summaries.

**Question 2 — Do the domain examples match your reader?**

Open Section 3. Count the examples. Count the ones in your actual domain. If your book is for graphic designers and Section 3 contains marketing, small business, and education examples, the Gatherer found related content but missed the target. This is the most common failure pattern and the easiest to miss because the examples *sound* relevant — they're about creative work, or visual content, or working with clients. They are not about graphic design. The "neighborhood drift" is the version of the fluency trap that runs at the example level.

**Question 3 — Is anything flagged `[verify]` or `[contested]`?**

Search the file. The Gatherer is instructed to flag any claim it could not source confidently. If the file contains zero flags, that is a yellow flag in itself. Either the chapter is on extremely well-trodden ground (cite indexing, basic typography, well-documented historical events) or the Gatherer is being more confident than the evidence warrants. Sycophancy in long-context models is real [Sharma, Mrinank et al., 2023, Anthropic, "Towards Understanding Sycophancy in Language Models"]; one of its forms is "fewer flags than the topic deserves." Trust files with flags more than files without.

**Question 4 — Would a peer in your domain recognize the sources?**

This is the read-aloud version of the test. If you texted your most demanding colleague this file's Section 1, would they nod or wince? If wince, the chapter is thin. Designers can tell instantly whether a "designer source" was written by a designer; clinicians can tell instantly whether a "medical source" was written by a clinician. You have this instinct. Use it.

Four questions. Five to seven minutes per pantry file. Fifteen chapters in a couple of hours.

If all four answers are good, the file is **draft-ready**. Move on. If any answer fails, the chapter is **thin**, and the next section gives you the options.

---

## Thin-pantry chapters — three responses

Thin pantry has three causes, and the cause determines the response.

**Cause A — the research was hard.** The topic is recent, niche, or contested. The Gatherer did its best. Section 1 has two reasonable sources and a flagged third. Section 3 has three good domain examples and two stretches. This is a *supplementable* chapter. Spend forty-five minutes — open Google Scholar, your professional association's publications, the trade press in your domain. Add two primary sources to Section 1 by hand. Replace the stretched examples in Section 3 with examples you have lived. The pantry becomes draft-ready by the end of the hour.

**Cause B — the chapter is genuinely under-researched in the field.** This happens. AI's effect on a specific freelance niche may be reported only in trade newsletters; case law on a contested claim may be too recent. The Gatherer cannot find what does not yet exist. This is an *accept-with-flag* chapter. Add a banner to the pantry file:

```
[contested — see pantry flag]
Field evidence on this topic is thin. The chapter
will rely on the author's domain experience and
will be flagged in risks.md as a contested claim.
```

Cowork will draft. The draft will be careful. The author will know to be especially careful in the human rewrite (Chapter 8). The chapter ships with eyes open.

**Cause C — the TIKTOC.md was vague.** The Gatherer prompt couldn't fix what the spec didn't ask for. Section 1 wanders. Section 3 is generic. Section 8 (Open Questions) is short — the Gatherer didn't even know what was missing. This is a *return-to-Tic-TOC* chapter. Open `/c1` again. Rewrite the capability statement to be specific. Add the missing learning outcome. Sharpen the application domain. Then rerun the Gatherer for just that chapter. The pantry quality is a downstream signal of TIKTOC.md quality. When the pantry is hopeless, the spec is what's broken.

The flowchart is small enough to memorize:

```
Pantry file thin?
   ├── Topic is hard       → Supplement by hand (45 min)
   ├── Field evidence thin → Accept with flag, mark in risks.md
   └── TIKTOC.md vague     → Return to /c1, sharpen spec, rerun Gatherer
```

Three branches. Pick one per thin chapter. Write the choice in `risks.md` so future-you remembers.

---

## The shared markdown library — `_lib_` files

Some content recurs across chapters. The glossary. The recurring framework definitions. The book's house position on contested claims. The author bio. Repeating this content in every pantry file is waste, and worse, it lets the content drift — two chapters citing the same definition with one-word differences that confuse the reader.

The Pragmatic Programmer's DRY principle [Hunt, Andrew and David Thomas, 2019, *The Pragmatic Programmer*, 20th Anniversary Edition] applies: every piece of knowledge has a single, authoritative home. In the AI+1 scaffold, that home is any file in `pantry/` whose name starts with `_lib_`. Examples: `_lib_glossary.md`, `_lib_ai-plus-one-frame.md`, `_lib_contested-claims.md`.

The Chapter Research Gatherer reads `_lib_` files before generating chapter-specific notes. Anything in `_lib_` is shared context. The Gatherer does not duplicate `_lib_` content into chapter pantry files; it references the definition and moves on. When the Chapter Writer runs in Chapter 7, it consults `_lib_` files the same way.

**What goes in `_lib_`:**

- The glossary (every term used in more than two chapters).
- Framework definitions (e.g., the AI+1 frame, the irreducibly human taxonomy).
- The book's position on contested claims (so chapters don't relitigate).
- Style notes that apply across chapters (voice section, capitalization rules).
- Author bio, publication credits.

**What does not go in `_lib_`:**

- Chapter-specific examples.
- Citations specific to one chapter's topic.
- Per-chapter image briefs.

The mechanism, currently, is a direct read by the Gatherer prompt. The author updates a `_lib_` file once; every subsequent Gatherer run sees the update. Symlinks would be cleaner; direct read is more portable across operating systems. [verify — confirm current `_lib_` mechanism in `SCRIPTS/` against the Gatherer prompt]

---

## What pantry is *not*

This is the section the chapter is sometimes mistaken for. The pantry is *reference, not citation*. The distinction matters and a designer's existing intuition makes it land.

Pantry is the moodboard, the competitor audit, the customer interview folder, the Pinterest board. It is what you consult while you work. It is not what the client sees. When you are drafting a logo, you may have looked at hundreds of references; you cite none of them in the deliverable. The reference shaped your judgment; the deliverable carries your judgment, not the reference.

The pantry plays the same role for chapter drafting. Cowork consults it while drafting. The chapter draft does not cite the pantry. Chapter drafts cite primary sources. If a chapter draft references "according to a 2024 article" without naming the article, that draft is citing the pantry — which means the human rewrite (Chapter 8) must trace the claim back through the pantry to the original source and either cite it properly or remove the claim. Pantry-as-citation is the AI-laundered citation pattern; this is the structural defense against it.

The brand archaeology analogy may land harder. If you were doing a serious rebrand for a hundred-year-old company, you would not source the new identity from Wikipedia summaries of the company's history. You would go to the archives. Pantry files are Wikipedia-grade context for the drafting model. The chapter draft itself must reach further. The Goddard 2023 and Bhattacharyya 2023 findings — roughly half of GPT-3.5's medical citations were fabricated; GPT-4 reduced but did not eliminate — are the empirical reason. Even when retrieval works, citation-shaped text is cheap.

Sönke Ahrens's *How to Take Smart Notes* [Ahrens, Sönke, 2017] describes the same distinction in a different vocabulary. Niklas Luhmann's Zettelkasten — the legendary 90,000-card archive that produced 70 books — had three layers: fleeting notes (raw, in-the-moment), literature notes (what a source actually said), and permanent notes (the writer's own argued claim). Pantry files are roughly Ahrens's literature notes. Chapter drafts are permanent notes. Treating literature notes as if they were already permanent is what produces academic embarrassment in human writers and hallucinated citations in language models. The structural fix is the same in both cases: separate the layers.

---

## Worked example — the `ai-for-designers` Chapter 3 pantry

This is the pantry file for `ai-for-designers` Chapter 3 (Domain Research) after the Gatherer ran and after a forty-five-minute supplementation pass. Strong entries and weak entries are annotated.

```
# Research: Chapter 03 — Domain Research
# AI+1: AI Native Personalized Textbooks
Chapter one-line: Students write, run, and synthesize a structured
domain research prompt across three LLMs.
Research date: 2026-05-28

## 1. Primary Sources

[STRONG] Adobe Firefly 3 release notes, March 2024 — Adobe Inc.
Specific features named with version numbers; sourced from Adobe's
own release page. URL preserved.

[STRONG] Hoffmann, M. and Wallace, B. (2023). "Generative AI in
Studio Workflows: An Ethnography of Three Design Practices."
Journal of Design Research, 17(2). Peer-reviewed.

[WEAK — REPLACE] "According to a 2024 trend report, AI adoption
in design is growing." [no source named, percentage unattributed —
removed during supplementation pass]

[STRONG, ADDED MANUALLY] AIGA (American Institute of Graphic Arts)
2024 Design Census. URL, methodology, sample size all named.

## 2. State of the Field

[STRONG] What is settled: generative tools are now in every major
design software suite (Adobe, Figma, Canva). What is disputed:
whether AI augments or displaces senior designers. Cite Hoffmann
& Wallace 2023 (augmentation) and Davis 2024 op-ed (displacement).
[verify — Davis op-ed publication venue]

## 3. Application Domain Examples

[STRONG] Five examples, all from graphic design:
(1) Brand identity system for a regional law firm — designer used
Midjourney for moodboarding only, hand-drew the final mark.
(2) Editorial layout for a quarterly magazine — Adobe Firefly used
for stock image generation; layout decisions human.
(3) Motion design for a product launch — AI-assisted storyboarding,
hand-crafted final animation.
(4) Packaging redesign — Figma AI used for variation generation,
typography hand-set.
(5) Product lockup system — generative tools for exploration;
production all manual.

[WEAK — REMOVED] Marketing teams using AI for blog posts.
Small business owners using ChatGPT for logos.
[Wrong domain — removed during evaluation pass.]

## 4. Book's Thesis Connection

The fluency trap is most visible in Section 3 examples. AI tools
produce design-shaped output without design judgment. The
chapter's domain research must surface this distinction by
example, not by claim.

## 5. AI Wayback Machine Candidates

[STRONG] Lead: Paula Scher (1948–). Pentagram partner. Known for
City Opera, MoMA identities. Substantive connection: Scher's
career is the case that design is judgment, not output.

Alternate: Massimo Vignelli (1931–2014). Italian-American
designer. The NYC Subway map. Quote: "If you can design one
thing, you can design everything." Counter-position to AI's
generic competence.

## 6. Pedagogical Delivery Research

[STRONG] Three-LLM comparison as cognitive contrasting case
(Schwartz & Bransford 1998). Reading three drafts side by side
makes divergence visible.

## 7. Representation and Display Research

[STRONG] Three-column side-by-side of LLM outputs. Color-coded
agreement/divergence. Designers read color-coded tables natively.

## 8. Open Questions and Research Gaps

- Does Hoffmann & Wallace 2023 have a follow-up study? [verify]
- AIGA 2025 census not yet published; cite 2024 with date stamp.
- Davis op-ed venue uncertain. [verify before draft]

## 9. Sourcing Notes

Primary: Adobe release notes, Hoffmann & Wallace 2023, AIGA 2024.
Avoided: Medium trend pieces, LinkedIn posts, "best AI tools for
designers" listicles. The chapter's source list is the chapter's
seriousness.
```

Read the file twice. Notice what is *missing* that the bad version had: percentages no one can check, "Studies show" constructions, examples from wrong domains. Notice what is present: specific titles, version numbers, peer-reviewed citations, [verify] flags where confidence wavered. This is a literature-notes layer in Ahrens's sense. Cowork can draft from this without inventing.

---

## AI Wayback Machine — Niklas Luhmann

Wikipedia: "Niklas Luhmann."

Luhmann (1927–1998) was a German sociologist who built, over thirty years, a personal note-taking system of roughly 90,000 paper slips, indexed by a numeric code he invented and cross-referenced by hand. The Zettelkasten. From it he produced 70 books and 400 papers — an output that has never been credibly explained by anything other than the system itself.

The pantry is a Zettelkasten for one chapter. Luhmann's claim was that thinking happens in the notes, not in the head and not in the draft. The reason you cannot tell, looking at his finished books, where the work happened is that all the work happened in the notes. The same is the structural claim for the pantry: the chapter is downstream of the file. A thin pantry produces a thin chapter, no matter how hard the human rewrites later.

Luhmann is worth knowing about for a second reason: his system was *boring*. Index cards, a wooden cabinet, a numbering scheme. No magic. The infrastructure was simple and the practice was relentless. The same is true of the pantry. The technology is unimpressive; the discipline of evaluating each file before letting Cowork read it is the entire game.

**Try it:** Ask Claude: "Read about Luhmann's Zettelkasten. Argue whether AI+1's pantry is a Zettelkasten or only resembles one. What is the strongest disanalogy?"

---

## Exercises

**Exercise 6.1 (Apply).** Run the Chapter Research Gatherer against your TIKTOC.md. Confirm that `pantry/` contains exactly one notes file per chapter on your chapter list. If any chapter is missing a notes file, identify why (Gatherer error, chapter not in spec, slug mismatch) and rerun.

**Exercise 6.2 (Analyze).** Pick any two pantry files. For each, answer the four questions in writing:

1. What is the strongest primary source? (Cite by title.)
2. What is one claim that needs verification? (Quote the claim. Name what would settle it.)
3. Do the Section 3 examples match your reader's domain? (Count: how many of N examples are in your actual domain?)
4. Would a respected peer in your field recognize the sources in Section 1? (Yes / no, with reason.)

Two files. Four questions each. About ten minutes total.

**Exercise 6.3 (Evaluate).** Read every pantry file. For each, write one line in `risks.md`:

```
ch-03: DRAFT-READY
ch-04: THIN — supplement (45 min, AIGA report missing)
ch-05: THIN — accept-with-flag (field evidence sparse on Python install for designers)
ch-06: THIN — return-to-Tic-TOC (capability statement too vague)
...
```

This list is the input to Chapter 7. Cowork will draft every chapter on it. Chapters marked `return-to-Tic-TOC` should not be drafted until you have reopened `/c1` and resharpened the spec.

---

## Still puzzling

- **Is there a recommended maximum pantry size per chapter?** The "lost in the middle" finding [Liu, Nelson F. et al., 2024, "Lost in the Middle: How Language Models Use Long Contexts," TACL] suggests very long pantry files are under-attended in the middle. Empirically, three to five pages per chapter pantry file seems to hit the sweet spot. Longer files should be split into multiple `_lib_` references plus a thinner chapter-specific file. [verify — exact context-window behavior of the current Chapter Writer]
- **Does the Gatherer cite with URLs or with full bibliographic entries?** Currently a mix. Authors who plan to publish on Substack alongside Kindle benefit from URLs; authors planning print citations benefit from full entries. The Gatherer can be instructed to prefer one. [verify — current default]
- **Should the Gatherer be told the reader's domain explicitly, or does it infer from TIKTOC.md?** Currently it infers. Authors in niche subfields (medical illustration, scientific publishing, motion design) sometimes get better Section 3 results by adding an explicit domain hint to the Gatherer prompt.
- **What is the cost of running the Gatherer twice?** Idempotent at the file level (it warns before overwriting) but not at the source level — a second run may surface different sources because the web changes. Save a copy of the first run if you want to compare.

---

## What would change my mind

If a single AI tool ever closed the gap between literature notes and primary citation reliably — if retrieval became good enough that the Gatherer could be trusted to write draft-grade prose — the four-questions pass would become decorative. We are not there. Padmakumar and He's [2024, "Does Writing with Language Models Reduce Content Diversity?", ICLR 2024] measurement of 10–20% lexical-diversity reduction in LLM-assisted writing tells us the model's tendency is still to converge on cheap citation forms when allowed to. Until that number is near zero, the pantry must be evaluated by hand. The chapter is a bet on the necessity of human evaluation. If that bet ever becomes obsolete, the chapter becomes obsolete with it — and that would be excellent news for everyone.

---

## Bridge to Chapter 7

The pantry is populated. The Gatherer has done its work, and you have done yours — four questions per file, three responses for thin chapters. Cowork can now read every chapter's spec and consult every chapter's evaluated notes. It has what it needs to draft.

The next thing that happens is fourteen chapters appear in `chapters/` over the course of a long afternoon. The `log.csv` will show everything green. You will open one chapter and read it.

What you find on that page is Chapter 7.
