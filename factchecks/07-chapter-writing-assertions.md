# Assertions Report: 07-chapter-writing.md
**Date:** 2026-05-29
**Source file:** chapters/07-chapter-writing.md
**Assertions flagged:** 8
**Breakdown:** STAT: 1 | GUIDELINE: 0 | APPROVAL: 1 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 2

---
## ⚠️ Critical — Requires Immediate Expert Review

**[CURRENT/APPROVAL] — OUTDATED.** Sentence: "Cowork is, as of 2026, a feature inside Claude's desktop application — currently in research preview."
One-line finding: Cowork launched as a research preview in January 2026 but is, as of the current claude.com/product/cowork page, **generally available** across Pro/Max/Team/Enterprise plans — so "currently in research preview" is outdated as of 2026-05-29.

---
## Full Findings

### [CURRENT / APPROVAL] — OUTDATED
**Assertion type:** COMBINATION (positive product-status claim, fast-moving)
**Sentence:** "Cowork is, as of 2026, a feature inside Claude's desktop application — currently in research preview."
**Claim checked:** Whether Cowork is "currently in research preview" as of 2026-05-29.
**Site visited:** https://claude.com/product/cowork
**Finding:** The official product page now states "Claude Cowork is generally available" and the pricing section confirms Cowork is included in Pro, Max, Team, and Enterprise plans. The page's own news items (Enterprise deployment Apr 8, 2026; Dispatch/computer-use Mar 23, 2026) post-date a research-preview status. Cowork launched as a research preview in January 2026 but has since reached general availability. The "currently in research preview" framing is therefore OUTDATED. (Note: some sub-features — phone Dispatch, computer use — remain in research preview, but Cowork itself is GA.)
**Expert review needed:** Yes
**Suggested reference:** Claude Cowork product page, https://claude.com/product/cowork ("Claude Cowork is generally available").
**Notes:** The chapter rightly flags Cowork as HIGH aging risk and includes a "[verify — confirm current Cowork access path before publication]" note. Recommend updating to: "Cowork launched as a research preview in January 2026 and is now generally available across paid Claude plans." The rest of the architectural description (runtime, project folder, read/write files, isolated shell) remains accurate.

### [CURRENT / STAT] — CONFIRMED
**Assertion type:** POSITIVE (specific range, fast-moving)
**Sentence:** "Long-context models in 2026 (context windows in the 100k–1M token range) make full-chapter generation viable in a way it was not five years ago."
**Claim checked:** Whether 2026 frontier LLM context windows fall in the 100k–1M token range.
**Site visited:** Search results from codingscape.com, elvex.com, ofox.ai (2026 context-window comparisons).
**Finding:** Confirmed. As of 2026, Claude (200K standard, 1M GA on Opus/Sonnet 4.x), Gemini 3/3.1 (1M), and GPT-5.x (272K standard, expandable to 1M) all fall within or span the stated 100k–1M range. The range is accurate.
**Expert review needed:** No
**Suggested reference:** Context-length comparisons, e.g., https://www.elvex.com/blog/context-length-comparison-ai-models-2026
**Notes:** Effective (vs. advertised) context performance degrades past ~200K — which is precisely the "lost in the middle" point the chapter goes on to make.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named finding, cited twice in book)
**Sentence:** "Liu and colleagues' 'lost in the middle' finding documents that long-context models attend disproportionately to context beginnings and ends..." (footnote [^liu]: Liu et al. 2024, TACL, 12, 157–173)
**Claim checked:** Existence and finding of Liu et al. (2024) "Lost in the Middle," and the page range 157–173.
**Site visited:** https://aclanthology.org/2024.tacl-1.9/ ; https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/
**Finding:** Confirmed. Nelson F. Liu et al. (2024), "Lost in the Middle: How Language Models Use Long Contexts," TACL, 12:157–173. Both the finding (U-shaped attention favoring beginnings/ends) and the page range are accurate.
**Expert review needed:** No
**Suggested reference:** Liu, N. F., et al. (2024). Lost in the Middle. TACL, 12, 157–173.
**Notes:** Page range 157–173 verified exactly; matches the footnote.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named Anthropic finding)
**Sentence:** "...sycophancy. Cowork-drafted chapters tend to agree too easily with the TIKTOC.md's framings..." (footnote [^sharma]: Sharma et al. 2023, Anthropic)
**Claim checked:** Existence of Sharma et al. (2023) sycophancy paper (Anthropic).
**Site visited:** https://arxiv.org/abs/2310.13548
**Finding:** Confirmed. Sharma et al. (2023), "Towards Understanding Sycophancy in Language Models," arXiv:2310.13548, Anthropic. Real paper, correctly attributed.
**Expert review needed:** No
**Suggested reference:** Sharma, M., et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548.
**Notes:** Same source verified in Chapter 6.

### [EVIDENCE] — UNVERIFIED
**Assertion type:** POSITIVE (named-finding attributions, multiple)
**Sentence:** Footnotes for failure-mode causes — Bender et al. 2021 (Stochastic Parrots, FAccT); Lee et al. 2022 (CoAuthor, CHI); Ji et al. 2023 (Survey of Hallucination, ACM Computing Surveys); Lin et al. 2022 (TruthfulQA, ACL); Bansal et al. 2021 (CHI); Strunk & White; Zinsser.
**Claim checked:** Existence and accurate attribution of these NLP/writing references.
**Site visited:** Not fetched this pass.
**Finding:** All are real, well-known papers/books and the chapter's attributions match their established content (Stochastic Parrots on corpus-average regression; TruthfulQA on measurable falsehood imitation; Ji et al. on hallucination taxonomy incl. extrinsic hallucination; Lee et al. CoAuthor on convergence in collaborative writing; Bansal et al. on uncertainty annotation improving team performance). None individually web-verified in this pass.
**Expert review needed:** No
**Suggested reference:** As cited in the chapter footnotes.
**Notes:** Citations are plausible and standard; not directly fetched.

### [EVIDENCE] — UNVERIFIED
**Assertion type:** POSITIVE (named-author voice attributions)
**Sentence:** Attenborough opening style; Feynman *Lectures on Physics* Vol. I Ch. 1 "what single sentence would you preserve"; Pinker "classic style"; Baldwin "The Creative Process" / "test-tube of the artist"; Didion "Why I Write" / "grammar is a piano I play by ear."
**Claim checked:** Existence and accuracy of these literary/scientific references.
**Site visited:** Not fetched this pass.
**Finding:** All are real works correctly attributed; the Feynman "single sentence" framing and Didion "piano I play by ear" quote are well-known and accurately characterized. Used as illustrative voice anchors, not load-bearing factual claims. Not web-verified this pass.
**Expert review needed:** No
**Suggested reference:** As cited in the chapter footnotes.
**Notes:** Illustrative/voice context; low verification priority.

### [APPROVAL / CURRENT] — CONFIRMED
**Assertion type:** POSITIVE (product architecture)
**Sentence:** "The pipeline this book teaches is built from three layers: Skills... Plugins... and the project folder."
**Claim checked:** That Claude/Cowork's architecture includes Skills and Plugins (connectors) as described.
**Site visited:** https://claude.com/product/cowork
**Finding:** Confirmed. The Cowork product page describes Plugins that bundle "skills, connectors, and sub-agents," matching the chapter's Skills + Plugins + project-folder framing. Architecture description is accurate as of 2026-05-29.
**Expert review needed:** No
**Suggested reference:** https://claude.com/product/cowork (Plugins/Skills/Connectors sections).
**Notes:** The chapter advises treating architecture as stable and exact menu paths as current-state — sound guidance.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| Bender et al. 2021; Lee et al. 2022; Ji et al. 2023; Lin et al. 2022; Bansal et al. 2021 (failure-mode footnotes) | EVIDENCE | POSITIVE | Real, standard NLP references; not individually fetched this pass. |
| Attenborough / Feynman / Pinker / Baldwin / Didion voice references | EVIDENCE | POSITIVE | Illustrative voice anchors; real and accurately characterized; not fetched. |
| "It succeeds roughly 70% of the time" (voice-move success rate) | STAT | POSITIVE | The book's own empirical observation about its tooling; not externally verifiable. |
| Strunk & White "omit needless words"; Zinsser "Bits and Pieces" | EVIDENCE | POSITIVE | Real, uncontroversial; not fetched. |

---
## AI-Pass Flags
- **Primary flag:** "Cowork ... currently in research preview" is OUTDATED — Cowork is now generally available (see Critical above). The chapter's own "[verify — confirm current Cowork access path before publication]" note anticipates exactly this; resolve it before publication.
- The "70% of the time" voice-success figure is the book's internal observation, not an external claim — flagged as non-verifiable, not as an error.
- The worked-example draft (the "bad" Cowork opening with "78% of design firms," "small business owner") is a deliberately fabricated illustrative example, correctly framed as such. No verification needed.
- No internal inconsistencies or wrong definitions detected.

---
<!-- Annotation note: the OUTDATED Cowork sentence is flagged inline in the source per instructions. -->
