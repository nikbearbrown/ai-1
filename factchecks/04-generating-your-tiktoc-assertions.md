# Assertions Report: 04-generating-your-tiktoc.md
**Date:** 2026-05-29
**Source file:** chapters/04-generating-your-tiktoc.md
**Assertions flagged:** 6
**Breakdown:** STAT: 1 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 0

---
## ⚠️ Critical — Requires Immediate Expert Review
None found.

---
## Full Findings

### [EVIDENCE] — CONFIRMED
**Assertion type:** COMBINATION (positive + named historical finding)
**Sentence:** "The Curtis, Krasner, and Iscoe 1988 study of large software projects found that defects introduced at the specification stage cost roughly ten to a hundred times more to fix downstream than defects introduced during implementation."
**Claim checked:** The paper exists as cited (Curtis, Krasner, Iscoe 1988, Communications of the ACM, 31(11), 1268–1287), and concerns the software design process for large systems.
**Site visited:** https://cacm.acm.org/research/a-field-study-of-the-software-design-process-for-large-systems/ ; https://dl.acm.org/doi/10.1145/50087.50089
**Finding:** The citation is accurate: B. Curtis, H. Krasner, N. Iscoe, "A Field Study of the Software Design Process for Large Systems," CACM 31(11), 1988, pp. 1268–1287. The paper studied 17 large projects and analyzed how application-domain knowledge, fluctuating requirements, and communication breakdowns affect software quality. The "10–100x" cost-to-fix ratio is a widely cited software-engineering finding, though this specific paper is best known for the three-problems/layered-behavioral-model framing rather than for originating the exact 10–100x figure; the chapter itself hedges ("roughly," "exact ratio is approximate").
**Expert review needed:** No
**Suggested reference:** Curtis, B., Krasner, H., & Iscoe, N. (1988). A Field Study of the Software Design Process for Large Systems. Communications of the ACM, 31(11), 1268–1287.
**Notes:** Citation venue, year, volume, issue, and page range all verified correct. The attribution of the specific 10–100x figure to this paper is a common shorthand in the field; the prose's hedging makes it defensible.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named framework attribution)
**Sentence:** "The Anderson-Krathwohl 2001 revision of Bloom's taxonomy supplies the vocabulary: Remember, Understand, Apply, Analyze, Evaluate, Create."
**Claim checked:** That the 2001 Anderson & Krathwohl revision of Bloom's taxonomy uses exactly these six cognitive-process levels in this order.
**Site visited:** https://scirp.org/reference/referencespapers?referenceid=1223916 ; https://www.quincycollege.edu/wp-content/uploads/Anderson-and-Krathwohl_Revised-Blooms-Taxonomy.pdf
**Finding:** Confirmed. Anderson, L. W., & Krathwohl, D. R. (Eds.) (2001), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives* (Longman) reorganizes the cognitive-process dimension into Remember, Understand, Apply, Analyze, Evaluate, Create — exactly as the chapter states.
**Expert review needed:** No
**Suggested reference:** Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). A Taxonomy for Learning, Teaching, and Assessing. Longman.
**Notes:** The footnote in the chapter matches the verified citation.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named criterion attribution)
**Sentence:** "Robert Mager's 1962 criterion gives the analytical foundation. ... A real learning outcome names three things: the performance ... the condition ... and the criterion ..."
**Claim checked:** That Robert Mager (1962, *Preparing Instructional Objectives*) is the source of the three-part learning-objective criterion (performance, condition, criterion).
**Site visited:** Not independently fetched (see Unverified table — partial). Cross-referenced against the verified Anderson/Krathwohl pedagogy literature only.
**Finding:** Mager's three-component objective (performance/behavior, condition, criterion) is a foundational and accurately attributed concept in instructional design; the chapter's description is standard. However, no Mager-specific source was directly fetched in this pass.
**Expert review needed:** No
**Suggested reference:** Mager, R. F. (1962). Preparing Instructional Objectives.
**Notes:** Reclassified to Unverified below pending a fetched source; the description itself is consistent with the well-established Mager framework.

### [STAT] — CONFIRMED
**Assertion type:** COMBINATION (emphatic "among the highest" + specific statistic)
**Sentence:** "Robert Marzano's 2001 meta-analysis of instructional strategies assigned the move of identifying similarities and differences an effect size of 1.61 — among the highest values in that study."
**Claim checked:** That Marzano, Pickering & Pollock (2001), *Classroom Instruction That Works*, reports an effect size of 1.61 for identifying similarities and differences.
**Site visited:** https://files.eric.ed.gov/fulltext/ED543521.pdf ; https://www.scirp.org/reference/ReferencesPapers?ReferenceID=741710
**Finding:** Confirmed. Marzano, Pickering & Pollock (2001) report an average effect size of 1.61 for "identifying similarities and differences" (≈45 percentile-point gain, from 31 studies) — among the highest of the nine strategies analyzed. The figure and attribution are accurate.
**Expert review needed:** No
**Suggested reference:** Marzano, R. J., Pickering, D. J., & Pollock, J. E. (2001). Classroom Instruction That Works. ASCD.
**Notes:** Effect-size value (1.61) verified exactly.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named-author argument attribution)
**Sentence:** "Wiggins and McTighe's Backward Design argument is that the most-skipped stage in curriculum design — Identify Desired Results — is also the highest-leverage one."
**Claim checked:** Existence/attribution of Wiggins & McTighe, *Understanding by Design* (2005).
**Site visited:** Not independently fetched this pass.
**Finding:** Wiggins & McTighe's *Understanding by Design* (Backward Design) is a real, well-established framework whose first stage is "Identify Desired Results." The chapter's characterization is standard and accurate, but no source was fetched in this pass.
**Expert review needed:** No
**Suggested reference:** Wiggins, G., & McTighe, J. (2005). Understanding by Design (Expanded 2nd ed.). ASCD.
**Notes:** Moved to Unverified pending a fetched source; framework attribution is uncontroversial.

### [EVIDENCE] — UNVERIFIED
**Assertion type:** POSITIVE (named-finding attributions in "Still puzzling")
**Sentence:** "Ericsson's 1993 deliberate-practice research supports sixty to ninety-minute focused sessions." / "Sweller's cognitive load theory predicts that holding a full book's design decisions in working memory simultaneously is infeasible..."
**Claim checked:** Existence and characterization of Ericsson, Krampe & Tesch-Römer (1993) and Sweller (1988).
**Site visited:** Not fetched this pass.
**Finding:** Both are real, foundational papers (Ericsson et al. 1993 in *Psychological Review*; Sweller 1988 in *Cognitive Science*). The chapter's claim that Ericsson "supports sixty to ninety-minute focused sessions" is a looser interpretive gloss than the paper's actual focus (deliberate practice and expert performance); this specific session-length framing should be checked against the source.
**Expert review needed:** Yes (for the Ericsson session-length interpretation specifically)
**Suggested reference:** Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). Psychological Review, 100(3), 363–406; Sweller, J. (1988). Cognitive Science, 12(2), 257–285.
**Notes:** Not web-verified in this pass; the Ericsson session-length gloss is the only interpretive risk.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Robert Mager's 1962 criterion gives the analytical foundation..." | EVIDENCE | POSITIVE | No Mager-specific source fetched; framework is well-established and description standard. |
| "Wiggins and McTighe's Backward Design argument is that the most-skipped stage... Identify Desired Results — is also the highest-leverage one." | EVIDENCE | POSITIVE | No source fetched; attribution uncontroversial. |
| "Ericsson's 1993 deliberate-practice research supports sixty to ninety-minute focused sessions." | EVIDENCE | POSITIVE | No source fetched; session-length gloss may overstate the paper's claim. |
| "Sweller's cognitive load theory predicts that holding a full book's design decisions in working memory simultaneously is infeasible..." | SPECIALIST | POSITIVE | No source fetched; interpretive application of CLT, not a direct quote. |
| Meadows "twelve leverage points," 1972 Limits to Growth, 2008 Thinking in Systems (Wayback Machine section). | EVIDENCE | POSITIVE | No source fetched; the section is an illustrative reading prompt, not a load-bearing factual claim. |

---
## AI-Pass Flags
- The chapter explicitly self-flags the "/g2 seven failure modes" list as needing verification against the current prompt ("[verify — exact seven-mode list...]"). This is an internal, author-acknowledged caveat about the book's own tooling, not a factual web-checkable claim — no action.
- The WEF "fastest-declining job" framing is referenced inside the worked example as a contested claim the book deliberately flags; it is presented as an illustrative diagnostic, not asserted as fact. No verification needed.
- No internal inconsistencies or wrong definitions detected.
