# Assertions Report: 02-what-tic-toc-does.md
**Date:** 2026-05-29
**Source file:** chapters/02-what-tic-toc-does.md
**Assertions flagged:** 6
**Breakdown:** STAT: 1 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 0

---
## ⚠️ Critical — Requires Immediate Expert Review
None found. (The one item worth an editorial note — the 10–100× defect-cost ratio being Boehm's figure rather than Curtis/Krasner/Iscoe's — is handled honestly by the chapter itself; see Full Findings.)

---
## Full Findings

### [EVIDENCE / STAT] — CONFIRMED (with attribution nuance)
**Assertion type:** POSITIVE / EMPHATIC-adjacent (named study + ratio)
**Sentence:** "In 1988, Bill Curtis, Herb Krasner, and Neil Iscoe published a study of seventeen large software projects in *Communications of the ACM*. ... defects introduced during requirements analysis ... cost roughly ten to a hundred times more to fix than defects introduced during implementation."
**Claim checked:** (a) Curtis/Krasner/Iscoe 1988 study of 17 projects in CACM; (b) the 10–100× requirements-defect cost ratio.
**Site visited:** https://cacm.acm.org/research/a-field-study-of-the-software-design-process-for-large-systems/ and https://stevemcconnell.com/articles/an-ounce-of-prevention/
**Finding:** The Curtis/Krasner/Iscoe paper is confirmed: "A Field Study of the Software Design Process for Large Systems," *Communications of the ACM* 31(11), 1268–1287, 1988, based on interviews across 17 large projects. Confirmed matches footnote [^curtis]. The 10–100× cost-escalation ratio, however, is canonically Barry Boehm's finding (Boehm 1981; "Software Defect Reduction Top 10 List," Boehm & Basili 2001), not a result of the Curtis study. The chapter does NOT claim Curtis et al. proved the ratio — it says the number "has been replicated in various forms across software engineering literature" and explicitly flags that the textbook-authorship analog is unproven. That framing is honest.
**Expert review needed:** No (optional: add a Boehm citation for the ratio itself)
**Suggested reference:** Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287. https://dl.acm.org/doi/10.1145/50087.50089 — and for the cost ratio: Boehm, B., & Basili, V. (2001). "Software Defect Reduction Top 10 List." *IEEE Computer*, 34(1), 135–137.
**Notes:** Consider attaching the cost-ratio claim explicitly to Boehm to remove any implication it came from the Curtis study.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named framework)
**Sentence:** "The canonical contemporary framework here is Wiggins and McTighe's *Understanding by Design*, first published in 1998. ... The right sequence is: start with the outcomes you want ... They call the first stage *Identify Desired Results*."
**Claim checked:** UbD first published 1998; Backward Design stage 1 = "Identify Desired Results."
**Site visited:** https://ascd.org/el/articles/backward-design-for-forward-action
**Finding:** Confirmed. *Understanding by Design* (Wiggins & McTighe, ASCD, 1998) defines Backward Design's three stages, beginning with "Identify Desired Results," then "Determine Acceptable Evidence," then "Plan Learning Experiences and Instruction." Footnote [^wiggins] cites the 2005 Expanded 2nd ed., which is correct for that edition; the "first published in 1998" in body text is also correct.
**Expert review needed:** No
**Suggested reference:** Wiggins, G., & McTighe, J. (1998/2005). *Understanding by Design.* ASCD.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named framework / list)
**Sentence:** "The Anderson-Krathwohl 2001 revision of Bloom's taxonomy provides the verb vocabulary: Remember, Understand, Apply, Analyze, Evaluate, Create."
**Claim checked:** Anderson-Krathwohl 2001 revision and its six verb levels.
**Site visited:** https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/blooms-taxonomy-of-educational-objectives/
**Finding:** Confirmed. The 2001 Anderson & Krathwohl revision recast Bloom's levels as verbs: Remember, Understand, Apply, Analyze, Evaluate, Create. Matches the chapter and footnote [^bloom] exactly.
**Expert review needed:** No
**Suggested reference:** Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing.* Longman.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named framework)
**Sentence:** "Robert Cooper formalized the logic in a 1990 paper in *Business Horizons*, calling it Stage-Gate ... Cooper's original model had five gates."
**Claim checked:** Cooper 1990 Stage-Gate paper in Business Horizons; original five-gate model.
**Site visited:** https://ideas.repec.org/a/eee/bushor/v33y1990i3p44-54.html
**Finding:** Confirmed. Cooper, "Stage-Gate Systems: A New Tool for Managing New Products," *Business Horizons* 33(3), 44–54, 1990. The classic Cooper Stage-Gate model runs through five gates (discovery/scoping through launch). Matches footnote [^cooper] and the "five gates" claim.
**Expert review needed:** No
**Suggested reference:** Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New Products." *Business Horizons*, 33(3), 44–54.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named work)
**Sentence:** "An older voice here is Hilda Taba, the Estonian-American curriculum theorist whose 1962 *Curriculum Development: Theory and Practice* argued for an inductive approach." (also repeated in AI Wayback — Hilda Taba)
**Claim checked:** Taba, Curriculum Development: Theory and Practice, 1962; inductive model.
**Site visited:** Verified via standard bibliographic record consistent with the search corpus; Taba's 1962 *Curriculum Development: Theory and Practice* (Harcourt, Brace & World) and her inductive ("Taba model") approach are well-attested.
**Finding:** The book, year, publisher, and the inductive-model characterization match the standard record. Footnote [^taba] is consistent.
**Expert review needed:** No
**Suggested reference:** Taba, H. (1962). *Curriculum Development: Theory and Practice.* Harcourt, Brace & World.
**Notes:** Title/year/publisher are canonical; no contradiction surfaced.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Robert Gagné's *Conditions of Learning*, first published in 1965, argued that different types of learning require different instructional sequences." | EVIDENCE | BASIC | Standard well-attested citation (Holt, Rinehart and Winston, 1965); not separately re-fetched. Low-risk; metadata matches footnote [^gagne]. |
| "Robert Mager's shorter work, *Preparing Instructional Objectives* ... argued that a learning objective must specify what the learner will *do*, not what they will *know*." | EVIDENCE | BASIC | Standard well-attested citation (1962, rev. 1997); not separately re-fetched. The "performance verb" thesis is Mager's central, well-documented claim. Low-risk. |
| "John Sweller's work on cognitive load theory argues that sustained working memory engagement ... is finite and fatiguing." | SPECIALIST | BASIC | Sweller 1988, *Cognitive Science* 12(2), 257–285 is standard; the specific "fatiguing" gloss is the author's paraphrase. Not separately re-fetched. Low-risk on citation; gloss is interpretive. |
| "Ericsson's deliberate-practice research supports focused sessions of sixty to ninety minutes." | EVIDENCE | BASIC | Ericsson, Krampe & Tesch-Römer 1993 is standard; the "60–90 minute session" gloss is a common but loose popularization. The chapter explicitly frames the two-hour timebox as "a defensible heuristic," not empirically derived — so the surrounding claim is appropriately hedged. Not re-fetched. |

---
## AI-Pass Flags
- The chapter is unusually careful with its own evidentiary claims: it openly states the textbook-authorship analog of the defect-cost ratio "has not been formally replicated" and that the two-hour timebox "is not empirically derived." No logical inconsistencies or wrong definitions noticed.
- Editorial suggestion (not a factual error): when citing the 10–100× defect-cost ratio, attach it to Boehm explicitly rather than leaving it adjacent to the Curtis/Krasner/Iscoe study, since the ratio is Boehm's, not a finding of that 1988 paper.
