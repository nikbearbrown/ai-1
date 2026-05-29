# Master Fact-Check Report

**Book folder:** ai-1 (*AI+1*, Nik Bear Brown)
**Date:** 2026-05-29
**Total chapters/files processed:** 24 (00-frontmatter, chapters 01–12, appendices 88–97, 99-back-matter)
**Total files read:** 24
**Total assertions flagged:** 109
**Breakdown by content category (approx.; Ch 12 items are dual-categorized APPROVAL/GUIDELINE + CURRENT):** STAT: 16 | GUIDELINE: 9 | APPROVAL: 6 | EVIDENCE: 63 | SPECIALIST: 6 | CURRENT: 16
**Breakdown by verdict:** CONFIRMED: 86 | OUTDATED: 1 | CONTRADICTED: 4 | UNVERIFIED: 14
**Assertion types:** predominantly BASIC and POSITIVE; one COMBINATION (Ch 7, the Cowork status sentence). I-LANGUAGE assertions were rare (the book attributes findings to named sources, not the author's own primary research).

*Verification note: sources were adapted from the prompt's biomedical defaults to this book's fields — AI-labor data (PwC, Lightcast, Stanford AI Index), Amazon KDP, US Copyright Office, Pandoc / W3C EPUB, Anthropic, color-vision (Okabe-Ito CUD), and the cited psychology/HCI papers via Scholar/DOI. Every CONFIRMED/OUTDATED/CONTRADICTED verdict rests on a source actually fetched; unreachable or unlocatable claims were marked UNVERIFIED rather than guessed.*

---

## Overall Critical Findings

Five items have verdict OUTDATED or CONTRADICTED. Sorted by priority (APPROVAL/GUIDELINE → EVIDENCE → CURRENT).

**File:** chapters/12-final-check-and-build.md
**Assertion type:** POSITIVE · **Category:** APPROVAL · **Verdict:** CONTRADICTED
**Sentence:** "…the AI-content disclosure, required since August 2023…"
**Finding:** Amazon/KDP announced the AI-content disclosure requirement on **September 7, 2023**, not August. Also, KDP requires disclosure of *AI-generated* content; *AI-assisted* content (the book's own category) is **not** required to be disclosed — so the sentence both misdates and slightly overstates the obligation.

**File:** chapters/96-appendix-cajal.md
**Assertion type:** BASIC · **Category:** GUIDELINE · **Verdict:** CONTRADICTED
**Sentence:** "Nature / Nature Reviews … Column widths: 88mm (single), 120mm (1.5), 180mm (double)"
**Finding:** Nature's current formatting guide specifies **90mm** single-column (double 180mm matches). The 88mm figure is off by 2mm. (This sits inside the reproduced CAJAL prompt's publisher-style reference.)

**File:** chapters/01-what-ai-plus-one-is.md
**Assertion type:** BASIC · **Category:** EVIDENCE · **Verdict:** CONTRADICTED
**Sentence:** "In 2021, Emily Bender, Timnit Gebru, Angelina McMillan-Major, and Margaret Mitchell published *On the Dangers of Stochastic Parrots* at the FAccT conference."
**Finding:** The published paper's fourth author appears under the pseudonym **"Shmargaret Shmitchell"** (Mitchell used it to mark Google's role in the affair). Year (2021), venue (FAccT), and pages (610–623) are correct. Name should be corrected or footnoted.

**File:** chapters/01-what-ai-plus-one-is.md
**Assertion type:** BASIC · **Category:** EVIDENCE · **Verdict:** CONTRADICTED
**Sentence:** Footnote dating Brynjolfsson's "The Turing Trap" to 2023.
**Finding:** "The Turing Trap: The Promise & Peril of Human-Like Artificial Intelligence" appeared in *Daedalus* 151(2), 272–287, in **2022**. Volume/issue/pages are correct; the year is wrong.

**File:** chapters/07-chapter-writing.md
**Assertion type:** COMBINATION (emphatic + positive) · **Category:** CURRENT · **Verdict:** OUTDATED
**Sentence:** "Cowork is, as of 2026, a feature inside Claude's desktop application — currently in research preview."
**Finding:** Cowork launched as a research preview but is, as of 2026-05-29, generally available across paid tiers (individual sub-features remain in preview). "Currently in research preview" reads as stale. This is the single fastest-aging sentence in the book and the chapter already flags the area as HIGH aging risk.

---

## Chapter-by-Chapter Summary

| File | Flagged | Critical | Outdated | Contradicted | Confirmed | Unverified |
|---|---|---|---|---|---|---|
| 00-frontmatter.md | 0 | 0 | 0 | 0 | 0 | 0 |
| 01-what-ai-plus-one-is.md | 9 | 2 | 0 | 2 | 7 | 0 |
| 02-what-tic-toc-does.md | 6 | 0 | 0 | 0 | 5 | 0 |
| 03-domain-research.md | 5 | 0 | 0 | 0 | 5 | 0 |
| 04-generating-your-tiktoc.md | 6 | 0 | 0 | 0 | 5 | 1 |
| 05-book-scaffold.md | 7 | 0 | 0 | 0 | 6 | 1 |
| 06-research-pass.md | 8 | 0 | 0 | 0 | 6 | 2 |
| 07-chapter-writing.md | 8 | 1 | 1 | 0 | 4 | 2 |
| 08-the-human-rewrite.md | 9 | 0 | 0 | 0 | 8 | 1 |
| 09-finishing-pass-and-figures.md | 8 | 0 | 0 | 0 | 8 | 0 |
| 10-enrichment-for-ai.md | 5 | 0 | 0 | 0 | 5 | 0 |
| 11-creating-figures.md | 8 | 0 | 0 | 0 | 8 | 0 |
| 12-final-check-and-build.md | 13 | 1 | 0 | 1 | 10 | 1 |
| 88-appendix-tiktoc.md | 1 | 0 | 0 | 0 | 1 | 0 |
| 89-appendix-domain-research.md | 1 | 0 | 0 | 0 | 1 | 0 |
| 90–95, 97 appendices | 0 | 0 | 0 | 0 | 0 | 0 |
| 96-appendix-cajal.md | 8 | 1 | 0 | 1 | 5 | 1 |
| 99-back-matter.md | 7 | 0 | 0 | 0 | 2 | 5 |

*Appendices 90, 91, 92, 93, 94, 95, 97 are reproduced tool prompts (imperative instructions) and yielded no verifiable assertions.*

---

## Non-critical issues worth author attention (CONFIRMED-but-imprecise / UNVERIFIED)

These are not OUTDATED/CONTRADICTED but the per-chapter reports flag them for an editorial pass:

- **Attribution — the "10–100×" defect-cost ratio (Ch 2, Ch 4).** Real and widely cited, but the canonical source is **Boehm**, not Curtis/Krasner/Iscoe 1988 (which the chapters cite). The book hedges honestly ("the ratio has been replicated"); consider attaching the ratio to Boehm explicitly.
- **Misattribution — "33% drop in graphic-design postings" (Ch 1).** The number is real (Bloomberry's analysis of ~180M postings) but the in-text verify-note credits PwC/Lightcast. Re-source.
- **Misattribution — Guo 2014 (Ch 5).** The paper is real and correctly cited for Python's rise as a teaching language, but the appended claim ("install friction was the single largest predictor of first-week disengagement") does not appear in it. Re-source or soften.
- **Unconfirmed magnitude — Padmakumar & He 2024 "10–20% lexical-diversity reduction" (Ch 6, Ch 8).** Paper and direction confirmed; the specific 10–20% figure was not located in fetched sources. Verify the exact number.
- **Precision — Figma "93% weekly use" (Ch 3).** The Figma report is real but the figure is **91%**; since the chapter uses this number to teach "verify the specific number," the example would survive a reader's spot-check better at the real value.
- **Superlative — "most cited paper in the history of psychology" (Ch 11, Miller 1956).** Unverifiable superlative; soften to "one of the most cited."
- **Citation metadata (Ch 8).** "Advaith Bhat" → **Advait** Bhat; Bhat and Lee subtitles are slightly off.
- **Author bio (99-back-matter).** Northeastern's faculty page confirms the Associate Teaching Professor title and the UCLA Ph.D., but lists the Information Design & Visualization degree as *in progress* (bio says "holds"); the Harvard postdoc, the MBA, and Humanitarians AI's 2019 founding / 501(c)(3) status could not be confirmed from an authoritative page (UNVERIFIED — not contradicted). Reconcile the degree wording before print.

**AI-Pass internal inconsistency (no web check needed):** Chapters 9 and 11 refer to the Combined Test as having "fourteen items in **two** groups." Chapter 8 — authoritative — defines **four** groups. Change "two groups" → "four groups" in Ch 9 and Ch 11.

---

## Recommended Next Steps

The book is in strong factual shape: 86 of 109 flagged assertions verified against fetched sources, only 5 critical items, and zero fabricated or invented claims. The urgent fixes are concentrated in the **fast-aging, high-authority categories the book itself warns about** — the APPROVAL claim about Amazon's AI-disclosure rule (date + scope) and the CURRENT claim that Cowork is "in research preview" are the two most likely to embarrass at publication and should be fixed first. The two EVIDENCE contradictions in Chapter 1 (the *Stochastic Parrots* pseudonym and the *Turing Trap* year) are quick citation corrections but matter because Chapter 1 sets the book's credibility. The largest cluster of remaining risk is **EVIDENCE** (citation accuracy across 63 named findings) and a handful of **attribution drift** cases where a real source is cited for a claim it does not quite make — exactly the failure mode the book teaches readers to catch. The single internal inconsistency ("two groups" vs "four groups") should be reconciled. Overall reliability: high, with a short, well-bounded fix list — recommend the author resolve the five critical items and the bio degree wording before the first KDP submission, and treat the attribution-drift items as a second editing pass.

---

## Resolution log

**2026-05-29 — the 5 critical items were fixed in the source chapters:**

1. Ch 12 — AI-disclosure: corrected to "introduced in September 2023" and clarified that *AI-assisted* content is not required to be disclosed (only *AI-generated*).
2. Ch 7 — Cowork: changed "currently in research preview" → "launched as a research preview and since made generally available on paid plans, though some sub-features remain in preview."
3. Ch 1 — *Stochastic Parrots*: noted the fourth author was credited under the pseudonym "Shmargaret Shmitchell."
4. Ch 1 — "The Turing Trap" footnote year corrected 2023 → 2022.
5. Appendix I (CAJAL) — Nature single-column width corrected 88mm → 90mm.

The corresponding inline OUTDATED/CONTRADICTED flags were removed from those chapters. Per-file reports above are retained as the audit record of the original run. UNVERIFIED items (e.g., the KDP market-share figure, the author-bio credentials) remain flagged for the author.
