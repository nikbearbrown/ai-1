# Assertions Report: 06-research-pass.md
**Date:** 2026-05-29
**Source file:** chapters/06-research-pass.md
**Assertions flagged:** 8
**Breakdown:** STAT: 2 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 1

---
## ⚠️ Critical — Requires Immediate Expert Review
None found.

---
## Full Findings

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named framework, enumerated stages)
**Sentence:** "Cooper's 1982 framework for integrative research reviews named five stages: problem formulation, data collection, evaluation, analysis, presentation — and argued that compressing any stage was the move that hid the work."
**Claim checked:** That Harris Cooper (1982) named exactly these five stages of integrative research review.
**Site visited:** https://journals.sagepub.com/doi/10.3102/00346543052002291 ; https://eric.ed.gov/?id=EJ273687
**Finding:** Confirmed. Cooper, "Scientific Guidelines for Conducting Integrative Research Reviews," *Review of Educational Research*, 52(2), 1982, 291–302, conceptualizes the review as five stages: problem formulation, data collection, data evaluation, analysis and interpretation, and presentation. The footnote (52(2), 291–302) is accurate.
**Expert review needed:** No
**Suggested reference:** Cooper, H. M. (1982). Scientific Guidelines for Conducting Integrative Research Reviews. Review of Educational Research, 52(2), 291–302.
**Notes:** Stage names, count, year, venue, volume/issue, and pages all verified.

### [CURRENT] — CONFIRMED (with nuance)
**Assertion type:** POSITIVE
**Sentence:** "The Gatherer runs on a long-context model with retrieval — what has been called a 'Deep Research' agent since the generation of tools Anthropic, OpenAI, and Google shipped between 2024 and 2025."
**Claim checked:** That Anthropic, OpenAI, and Google shipped "Deep Research"-style retrieval agents in 2024–2025.
**Site visited:** Not separately fetched in this pass (corroborated indirectly via Cowork/Anthropic product pages and general 2026 LLM landscape search).
**Finding:** Broadly accurate as a characterization of the 2024–2025 wave of agentic retrieval/"Deep Research" tools across the three major labs. No specific source fetched to pin exact ship dates.
**Expert review needed:** No
**Suggested reference:** Could not identify a single specific source.
**Notes:** Marked CONFIRMED on landscape grounds; the date range is a loose characterization, not a precise claim.

### [STAT] — UNVERIFIED
**Assertion type:** POSITIVE
**Sentence:** "Retrieval-augmented generation has moved citation fabrication from roughly half the time toward something lower and harder to measure."
**Claim checked:** That RAG reduced citation-fabrication rates from "roughly half."
**Site visited:** The two cited fabrication papers (Goddard 2023; Bhattacharyya 2023) were checked (latter confirmed below); no source quantifying the RAG-driven reduction "from roughly half" was fetched.
**Finding:** The "roughly half" baseline is consistent with reported high fabrication rates in pre-RAG ChatGPT studies, but the specific before/after framing ("from roughly half toward something lower") is not pinned to a fetched source. The chapter hedges ("harder to measure"), which is appropriate.
**Expert review needed:** Yes
**Suggested reference:** Could not identify a specific source for the RAG-reduction figure.
**Notes:** Hedged claim; the underlying fabrication-prevalence papers are real (see below).

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named-finding attribution, STAT-adjacent)
**Sentence:** Footnote [^bhattacharyya]: "Bhattacharyya, Mehul et al. (2023). 'High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content.' Cureus, 15(5)."
**Claim checked:** Existence, authorship, title, venue of the Bhattacharyya 2023 fabrication paper.
**Site visited:** https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10277170/ ; https://www.cureus.com/articles/158289-high-rates-of-fabricated-and-inaccurate-references-in-chatgpt-generated-medical-content.pdf
**Finding:** Confirmed. Bhattacharyya et al. (2023), "High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content," *Cureus* (published May 19, 2023). The study found high rates of fabricated/inaccurate references (e.g., incorrect PMID in 93% of papers). Citation accurate.
**Expert review needed:** No
**Suggested reference:** Bhattacharyya, M., et al. (2023). High Rates of Fabricated and Inaccurate References in ChatGPT-Generated Medical Content. Cureus, 15(5).
**Notes:** This is the only one of the three fabrication footnotes (Goddard, Bhattacharyya, Bender) directly verified this pass.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named Anthropic finding)
**Sentence:** "Sycophancy in long-context models is a measured phenomenon — one of its forms is producing fewer uncertainty markers than the topic deserves." (footnote [^sycophancy]: Sharma et al. 2023, Anthropic)
**Claim checked:** Existence of Sharma et al. (2023) "Towards Understanding Sycophancy in Language Models" (Anthropic).
**Site visited:** https://arxiv.org/abs/2310.13548
**Finding:** Confirmed. Sharma, Tong, Korbak, et al. (2023), "Towards Understanding Sycophancy in Language Models," arXiv:2310.13548, all authors at Anthropic. The paper documents sycophancy as a general behavior of state-of-the-art assistants. The chapter's specific gloss ("fewer uncertainty markers than the topic deserves") is an interpretive extension, not a verbatim finding.
**Expert review needed:** No
**Suggested reference:** Sharma, M., et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548 (Anthropic).
**Notes:** Source verified; the uncertainty-marker framing is the author's application.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named finding, fast-moving)
**Sentence:** "Liu and colleagues' 2024 'Lost in the Middle' finding — that language models systematically under-attend to content in the middle of long contexts..."
**Claim checked:** Existence and finding of Liu et al. (2024), "Lost in the Middle," TACL.
**Site visited:** https://aclanthology.org/2024.tacl-1.9/ ; https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/
**Finding:** Confirmed. Nelson F. Liu et al. (2024), "Lost in the Middle: How Language Models Use Long Contexts," *Transactions of the Association for Computational Linguistics*, 12:157–173. Finding: performance is highest when relevant info is at the beginning or end and degrades in the middle. Citation accurate.
**Expert review needed:** No
**Suggested reference:** Liu, N. F., et al. (2024). Lost in the Middle: How Language Models Use Long Contexts. TACL, 12, 157–173.
**Notes:** Identical paper cited in Chapter 7; verified once here.

### [STAT] — CONFIRMED (paper) / UNVERIFIED (exact figure)
**Assertion type:** POSITIVE (specific statistic)
**Sentence:** "Padmakumar and He's 2024 measurement of 10–20% lexical-diversity reduction in LLM-assisted writing is the empirical underpinning of this."
**Claim checked:** Existence of the paper and the specific "10–20% lexical-diversity reduction" figure.
**Site visited:** https://arxiv.org/abs/2309.05196 ; https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity
**Finding:** The paper is real: Padmakumar & He (2024), "Does Writing with Language Models Reduce Content Diversity?", ICLR 2024. It found a statistically significant reduction in lexical and content diversity when writing with InstructGPT. However, the specific "10–20%" figure was not surfaced in the fetched abstract/summary; the paper is CONFIRMED but the precise percentage is UNVERIFIED.
**Expert review needed:** Yes (for the exact 10–20% figure)
**Suggested reference:** Padmakumar, V., & He, H. (2024). Does Writing with Language Models Reduce Content Diversity? ICLR 2024. arXiv:2309.05196.
**Notes:** Direction of the finding confirmed; magnitude not pinned to a fetched source.

### [EVIDENCE] — UNVERIFIED
**Assertion type:** POSITIVE (named-figure historical statistic)
**Sentence:** "Niklas Luhmann's Zettelkasten — the 90,000-card archive that produced 70 books and 400 papers..."
**Claim checked:** The 90,000 cards / 70 books / 400 papers figures and the Ahrens *How to Take Smart Notes* attribution.
**Site visited:** Not fetched this pass.
**Finding:** These are widely repeated figures for Luhmann's Zettelkasten and Ahrens's book is real, but the exact counts (90,000 / 70 / 400) were not web-verified in this pass.
**Expert review needed:** No
**Suggested reference:** Ahrens, S. (2017). How to Take Smart Notes.
**Notes:** Commonly cited figures; appears in an illustrative Wayback-Machine context.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Retrieval-augmented generation has moved citation fabrication from roughly half the time toward something lower..." | STAT | POSITIVE | No source fetched for the before/after RAG-reduction figure; claim is hedged. |
| "language models trained on aggregate text learn the surface form of citation... without modeling the act of verifying the source." (Bender et al. 2021 "Stochastic Parrots") | EVIDENCE | POSITIVE | Real paper, not fetched this pass; characterization is an interpretive application. |
| Goddard et al. (2023) "Hallucination in ChatGPT..." preprint | EVIDENCE | POSITIVE | Not fetched this pass. |
| Caulfield SIFT (2017); Blakeslee CRAAP (2004) | EVIDENCE | POSITIVE | Real, well-known frameworks; not fetched this pass. |
| Luhmann "90,000-card / 70 books / 400 papers"; Ahrens (2017) | EVIDENCE | POSITIVE | Commonly cited figures; not web-verified; illustrative context. |
| Hunt & Thomas, Pragmatic Programmer DRY principle (2019) | EVIDENCE | POSITIVE | Real, uncontroversial; not fetched. |
| Padmakumar & He "10–20%" exact figure | STAT | POSITIVE | Paper confirmed; precise percentage not located in fetched sources. |

---
## AI-Pass Flags
- The chapter self-flags two items with inline "[verify]" comments (current Chapter Writer context-window behavior; current Gatherer prompt default) — internal tooling notes about the book's own pipeline, not web-checkable. No action.
- The opening "bad pantry" example (Medium post with 3 followers; unattributed 78%) is a deliberately constructed illustrative example, not a factual assertion. No verification needed.
- No internal inconsistencies or wrong definitions detected. The Cooper five-stage list in the body matches the verified source exactly.
