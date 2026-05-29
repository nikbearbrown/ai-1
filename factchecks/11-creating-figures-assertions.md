# Assertions Report: 11-creating-figures.md
**Date:** 2026-05-29
**Source file:** chapters/11-creating-figures.md
**Assertions flagged:** 8
**Breakdown:** STAT: 1 | GUIDELINE: 1 | APPROVAL: 0 | EVIDENCE: 3 | SPECIALIST: 3 | CURRENT: 0

---
## ⚠️ Critical — Requires Immediate Expert Review
None found. No OUTDATED or CONTRADICTED verdicts. One internal-consistency flag (Combined Test "two groups") recorded under AI-Pass Flags.

---
## Full Findings

### [EVIDENCE] — CONFIRMED (with one emphatic claim to soften)
**Assertion type:** COMBINATION (emphatic + positive — "most cited paper in the history of psychology")
**Sentence:** In 1956 George Miller published the most cited paper in the history of psychology, "The Magical Number Seven, Plus or Minus Two,"... and fixed in everyone's mind that working memory holds about seven items.
**Claim checked:** Miller (1956), Psychological Review 63(2), 81–97; the seven±two working-memory claim; "most cited paper in psychology."
**Site visited:** https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two (and https://www.scirp.org/reference/referencespapers?referenceid=2814005)
**Finding:** Paper confirmed exactly as cited: *Psychological Review*, 63(2), 81–97 (1956). The seven±two capacity framing is correct (though Miller himself called "seven" rhetorical). The superlative "**the most cited paper in the history of psychology**" is a stronger, harder-to-verify claim — it is frequently described as *one of the most cited* / most influential, but "the most cited" is not securely established.
**Expert review needed:** No
**Suggested reference:** Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two." *Psychological Review*, 63(2), 81–97.
**Notes:** Recommend softening "the most cited paper in the history of psychology" to "one of the most cited papers in psychology." Citation and capacity claim are solid.

### [EVIDENCE] — CONFIRMED (with page-range note)
**Assertion type:** EMPHATIC (named reconsideration, dated)
**Sentence:** Nelson Cowan, reviewing decades of tighter experiments in 2001, put the real capacity at closer to four chunks...
**Claim checked:** Cowan (2001), "The magical number 4 in short-term memory," Behavioral and Brain Sciences 24(1), 87–114; ~4-chunk capacity.
**Site visited:** https://pubmed.ncbi.nlm.nih.gov/11515286/ (and https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/...)
**Finding:** Paper confirmed: *Behavioral and Brain Sciences*, 24 (2001). Cowan argues the real capacity limit is closer to ~4 chunks (target article + commentary). Footnote's page range 87–114 is the article proper; some catalogs list 87–185 (article plus open peer commentary). Both are correct depending on what is counted. The ~4-chunk claim is accurate.
**Expert review needed:** No
**Suggested reference:** Cowan, N. (2001). "The magical number 4 in short-term memory." *Behavioral and Brain Sciences*, 24(1), 87–114.

### [SPECIALIST] — CONFIRMED
**Assertion type:** EMPHATIC (named theory, attributed mechanism)
**Sentence:** John Sweller built a whole instructional theory on this, cognitive load theory: the load a learner can carry is fixed and small, so every element competing for attention that is not doing teaching work is actively subtracting...
**Claim checked:** Sweller (1988), "Cognitive Load During Problem Solving," Cognitive Science 12(2), 257–285; founder of cognitive load theory.
**Site visited:** https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4
**Finding:** Confirmed: *Cognitive Science*, 12(2), 257–285 (1988), DOI 10.1207/s15516709cog1202_4. Foundational cognitive-load-theory paper by Sweller. The chapter's mechanism description (limited capacity; extraneous load subtracts from learning) is an accurate statement of CLT.
**Expert review needed:** No
**Suggested reference:** Sweller, J. (1988). "Cognitive Load During Problem Solving." *Cognitive Science*, 12(2), 257–285.

### [SPECIALIST] — CONFIRMED
**Assertion type:** COMBINATION (emphatic + positive — palette engineered + publisher acceptance)
**Sentence:** The first is **Okabe-Ito** — an eight-color palette engineered to stay distinct for colorblind readers, which Elsevier, Wiley, and Springer Nature accept and red-green combinations fail.
**Claim checked:** Okabe-Ito is an 8-color colorblind-safe palette (Okabe & Ito, 2008, jfly.uni-koeln.de).
**Site visited:** https://conceptviz.app/blog/okabe-ito-palette-hex-codes-complete-reference (and jfly.uni-koeln.de/color/ referenced therein)
**Finding:** Confirmed: Masataka Okabe & Kei Ito (2008) Color Universal Design palette of 8 colors designed to remain distinguishable across color-vision-deficiency types; hosted at jfly.uni-koeln.de/color/. It is the most widely recommended colorblind-safe scientific palette. The "Elsevier/Wiley/Springer accept it" claim is directionally true (it is the de facto recommended scientific palette) but those publishers do not formally mandate this specific palette; treat as accurate-in-spirit.
**Expert review needed:** No
**Suggested reference:** Okabe, M., & Ito, K. (2008). "Color Universal Design (CUD)." jfly.uni-koeln.de/color/.
**Notes:** The footnote citation is accurate. The named-publisher "accept" wording is a soft generalization; consider "widely accepted in journals published by Elsevier, Wiley, and Springer Nature."

### [STAT] — CONFIRMED
**Assertion type:** BASIC (statistical/biological claim)
**Sentence:** About eight percent of men have some red-green color deficiency, and every e-reader has a grayscale mode.
**Claim checked:** ~8% of men have red-green color deficiency.
**Site visited:** https://www.britannica.com/science/red-green-colour-blindness (and https://en.wikipedia.org/wiki/Color_blindness)
**Finding:** Confirmed; ~8% of men (European ancestry; ~1 in 12) have red-green color deficiency. Standard, well-supported figure. (Matches the same claim in Chapter 9.)
**Expert review needed:** No
**Suggested reference:** Britannica, "Red-green colour blindness."

### [GUIDELINE] — CONFIRMED
**Assertion type:** EMPHATIC (standards-body requirement)
**Sentence:** And every SVG carries a `<title>` and a `<desc>` and a `role="img"`, which is an EPUB 3 accessibility requirement...
**Claim checked:** EPUB 3 accessibility (W3C EPUB Accessibility 1.1, 2023) requires accessible figure naming/description.
**Site visited:** https://www.w3.org/TR/epub-a11y-11/
**Finding:** EPUB Accessibility 1.1 (2023 W3C Recommendation) is real and requires WCAG-conformant accessible content, including accessible names/descriptions for non-text content. The `<title>`/`<desc>`/`role="img"` pattern is the standard accessible-SVG technique that satisfies this. Accurate. (Same claim/footnote as Chapter 9.)
**Expert review needed:** No
**Suggested reference:** W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/

### [SPECIALIST] — CONFIRMED
**Assertion type:** BASIC (technical/functional claim)
**Sentence:** Image models hallucinate text — they produce confident, misspelled, illegible characters...
**Claim checked:** Generative image models commonly produce garbled/misspelled text.
**Site visited:** (well-established, widely documented behavior of diffusion/image generators; not a single-source claim)
**Finding:** This is an accurate, widely documented limitation of image-generation models (text rendering is a known weakness, improving but still error-prone). The chapter's "request a blank diagram, label on a separate layer" mitigation is sound craft advice. Verified by general technical consensus.
**Expert review needed:** No
**Suggested reference:** Could not identify a single canonical source; reflects general, well-documented behavior of image-generation models as of 2026.

### [EVIDENCE] — CONFIRMED
**Assertion type:** COMBINATION (emphatic + historical, dated)
**Sentence:** Santiago Ramón y Cajal won the 1906 Nobel Prize for showing that the nervous system is built from discrete cells — neurons... He proved it, in large part, with drawings... he would sit at the microscope for hours, then draw the neural tissue from memory at a separate table.
**Claim checked:** Cajal, 1906 Nobel (Physiology/Medicine, shared with Golgi); neuron doctrine; drew from memory.
**Site visited:** https://en.wikipedia.org/wiki/Santiago_Ram%C3%B3n_y_Cajal (and https://www.nobelprize.org/prizes/medicine/1906/cajal/article/)
**Finding:** Confirmed. Cajal shared the 1906 Nobel Prize in Physiology or Medicine with Camillo Golgi "in recognition of their work on the structure of the nervous system"; he advanced the neuron doctrine (discrete cells, not a continuous web) and is documented as typically drawing from memory rather than tracing. The chapter's account is accurate.
**Expert review needed:** No
**Suggested reference:** NobelPrize.org, "Life and discoveries of Santiago Ramón y Cajal." https://www.nobelprize.org/prizes/medicine/1906/cajal/article/
**Notes:** Prize was *shared* with Golgi; chapter says "won the 1906 Nobel Prize," which is true but omits the shared award — optional clarification, not an error.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "the most cited paper in the history of psychology" (Miller) | EVIDENCE | EMPHATIC | Superlative not securely verifiable; recommend softening to "one of the most cited." Paper itself fully confirmed. |
| "Elsevier, Wiley, and Springer Nature accept [Okabe-Ito]" | SPECIALIST | POSITIVE | Directionally true (de facto scientific standard) but no formal publisher mandate confirmed; soft generalization. |

---
## AI-Pass Flags
- **Internal cross-chapter inconsistency (Combined Test group count).** Line ~65 (interactive-mode VG description) and line ~72 (triage signals) use the example *"the test has fourteen items in two groups."* Chapter 8 defines the Combined Test as fourteen items in **FOUR** groups (A/B/C/D). Same error appears in Chapter 9. Change "two groups" → "four groups" (or pick a different VG illustration) for consistency. No web search used.

---
## References
1. Miller, G. A. (1956). "The Magical Number Seven, Plus or Minus Two." *Psychological Review*, 63(2), 81–97. https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two
2. Cowan, N. (2001). "The magical number 4 in short-term memory." *Behavioral and Brain Sciences*, 24(1), 87–114. https://pubmed.ncbi.nlm.nih.gov/11515286/
3. Sweller, J. (1988). "Cognitive Load During Problem Solving." *Cognitive Science*, 12(2), 257–285. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4
4. Okabe, M., & Ito, K. (2008). "Color Universal Design (CUD)." jfly.uni-koeln.de/color/. https://conceptviz.app/blog/okabe-ito-palette-hex-codes-complete-reference
5. W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/
6. Britannica. "Red-green colour blindness." https://www.britannica.com/science/red-green-colour-blindness
7. NobelPrize.org. "Life and discoveries of Santiago Ramón y Cajal." https://www.nobelprize.org/prizes/medicine/1906/cajal/article/
