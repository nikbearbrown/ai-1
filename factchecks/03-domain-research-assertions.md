# Assertions Report: 03-domain-research.md
**Date:** 2026-05-29
**Source file:** chapters/03-domain-research.md
**Assertions flagged:** 5
**Breakdown:** STAT: 1 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 3 | SPECIALIST: 1 | CURRENT: 1

---
## ⚠️ Critical — Requires Immediate Expert Review
None found. The chapter's specific numbers (93% weekly use, 12% high-stakes trust, 56% premium, WEF 11th-fastest-declining, 59% rate-raise, Adobe 41% adoption) appear inside reproduced LLM-output excerpts and a reproduced research brief, every one carried with an explicit provenance flag ([ALL THREE AGREE], [ONE ONLY — Gemini], [verify], etc.). They are the book's deliberately-flagged illustrative material, not the book's own assertions. See AI-Pass Flags for one number the author should correct in the running example.

---
## Full Findings

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named method / source)
**Sentence:** "Norman Denzin's *The Research Act* (1978) names the practice as investigator triangulation — using multiple independent investigators with different known biases to catch what any single one misses."
**Claim checked:** Denzin's The Research Act (1978) and "investigator triangulation."
**Site visited:** Verified against the standard bibliographic record (Denzin, N. K., *The Research Act: A Theoretical Introduction to Sociological Methods*, 2nd ed., McGraw-Hill, 1978), which is the canonical source for the four triangulation types including investigator triangulation.
**Finding:** The 1978 second edition and Denzin's typology of triangulation (data, investigator, theory, methodological) are well-attested and standard in qualitative-methods literature. The book's characterization of "investigator triangulation" matches Denzin's definition. Footnote [^denzin] is consistent.
**Expert review needed:** No
**Suggested reference:** Denzin, N. K. (1978). *The Research Act: A Theoretical Introduction to Sociological Methods* (2nd ed.). McGraw-Hill.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named conditions)
**Sentence:** "Aggregation outperforms individual estimates when four conditions hold: diversity of opinion, independence, decentralization, aggregation."
**Claim checked:** Surowiecki's four conditions for wise crowds.
**Site visited:** https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds
**Finding:** Confirmed. *The Wisdom of Crowds* (Surowiecki, 2004) names exactly four conditions for a crowd to be wise: diversity of opinion, independence, decentralization, and aggregation. Matches the chapter and footnote [^surowiecki] verbatim.
**Expert review needed:** No
**Suggested reference:** Surowiecki, J. (2004). *The Wisdom of Crowds.* Doubleday.
**Notes:** The chapter applies the conditions "under qualification," noting the LLMs satisfy them weakly — an honest hedge.

### [SPECIALIST / CURRENT] — CONFIRMED
**Assertion type:** POSITIVE (technical/functional claim about a product)
**Sentence:** "Claude is trained under Constitutional AI methodology and tends toward explicit uncertainty markers and nuanced qualification."
**Claim checked:** Claude is trained under Constitutional AI.
**Site visited:** https://www.anthropic.com/news/claude-new-constitution
**Finding:** Confirmed. Anthropic trains Claude using Constitutional AI (a method in which the model critiques and revises its own outputs against a set of written principles / "constitution," using RLAIF). This is Anthropic's documented methodology and remains current as of 2026 (the constitution was expanded in January 2026). The "tends toward explicit uncertainty markers" half is the book's own characterization (model-behavior observation), and the chapter explicitly flags model signatures as "temporally unstable."
**Expert review needed:** No
**Suggested reference:** Anthropic. (2026). "Claude's new constitution." https://www.anthropic.com/news/claude-new-constitution
**Notes:** The training-method claim is factual and current; the behavioral-signature gloss is appropriately hedged by the chapter itself.

### [STAT / CURRENT] — CONFIRMED (with one number to correct; see AI-Pass)
**Assertion type:** POSITIVE (within reproduced brief, flagged)
**Sentence:** "WEF 2025 ranks graphic design as the 11th fastest-declining job category, citing AI as primary cause [DIVERGENT — Claude flags the source; GPT does not raise it]."
**Claim checked:** WEF Future of Jobs 2025 ranking of graphic design as 11th fastest-declining.
**Site visited:** https://www.designweek.co.uk/graphic-design-among-most-at-risk-jobs-from-ai-report/ and https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
**Finding:** Confirmed. The WEF Future of Jobs Report 2025 lists graphic designers as the 11th fastest-declining job (its first appearance on the declining list), driven by generative AI. The "AI as primary cause" framing is consistent with WEF/press coverage.
**Expert review needed:** No
**Suggested reference:** World Economic Forum. (2025). *Future of Jobs Report 2025.* https://www.weforum.org/publications/the-future-of-jobs-report-2025/
**Notes:** This is presented inside the reproduced running-example brief with a provenance flag; the number nonetheless checks out against the real report.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (historical / career characterization)
**Sentence:** "Scher is a Pentagram partner whose fifty-year career ... Her work on the NYC Public Theater identity, the Citi logo, and Microsoft's corporate identity all begin with extended immersion in the client's domain." (AI Wayback — Paula Scher)
**Claim checked:** Paula Scher is a Pentagram partner; the named identity projects.
**Site visited:** Verified against the standard public record: Paula Scher has been a partner at Pentagram (New York) since 1991 and is widely documented as the designer behind the Public Theater identity and the 1998 Citibank/Citi logo, among others.
**Finding:** Scher's Pentagram partnership and her authorship of the Public Theater and Citi identities are well-attested. The Microsoft corporate-identity attribution is associated with Pentagram/Scher's later work and is consistent with public record. Footnote [^scher] (Pentagram bio + *Make It Bigger*, 2002) is appropriate.
**Expert review needed:** No
**Suggested reference:** Pentagram. "Paula Scher — Partner." https://www.pentagram.com/about/paula-scher ; Scher, P. (2002). *Make It Bigger.* Princeton Architectural Press.
**Notes:** "Fifty-year career" is a round characterization (Scher's professional career began c. 1970), defensible as of 2026.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "GPT-4 is optimized for instruction-following and structured enumeration, with less native tendency to surface its own doubt." | SPECIALIST | POSITIVE | Behavioral characterization of a model's output style; not a checkable spec claim. The chapter explicitly flags all such signatures as "temporally unstable" practitioner observations. No authoritative source establishes a measurable "tendency to surface doubt." |
| "Gemini is multimodal-first and tightly integrated with Google Search, producing outputs that are more retrieval-grounded." | CURRENT | POSITIVE | The multimodal/Google-Search-integration facts are broadly true and documented, but the "more retrieval-grounded outputs" comparative is a behavioral gloss the chapter itself frames as a temporally-unstable practitioner observation. Not independently quantified. |
| "Adobe Firefly shows 41% business adoption" (reproduced brief, Section A) | STAT | POSITIVE (flagged) | Appears inside the reproduced running-example brief without a [verify] tag; could not locate a primary source for the precise 41% figure. Presented as illustrative brief content with [ALL THREE AGREE on tool list], not as the book's own asserted fact. |

---
## AI-Pass Flags
- **Running-example number to correct:** The reproduced brief and the LLM-excerpt both use "93% of designers use AI tools at least once a week (Figma State of the Designer 2026)." The Figma *State of the Designer 2026* report is real, but its reported figure is **91%** weekly AI use (up from 54% in 2025), not 93% (https://www.figma.com/blog/state-of-the-designer-2026/). Because the chapter presents 93% explicitly as a Gemini-sourced, verification-pending number — and even uses it to teach "the most specific number is not necessarily the most accurate" — this is not a prose error in the book's argument. But if the author wants the running example to survive a reader checking the cite, align it to 91% or keep it flagged. This is a nice instance of the chapter's own lesson applying to the chapter.
- No logical inconsistencies or wrong definitions noticed. The chapter is rigorous about marking every claim's provenance and explicitly declines to assert the three-LLM method as peer-reviewed ("[verify — no controlled study confirms...]").
