# Assertions Report: 01-what-ai-plus-one-is.md
**Date:** 2026-05-29
**Source file:** chapters/01-what-ai-plus-one-is.md
**Assertions flagged:** 9
**Breakdown:** STAT: 3 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 0 | CURRENT: 1

---
## ⚠️ Critical — Requires Immediate Expert Review

- **EVIDENCE | BASIC | CONTRADICTED** — "In 2021, Emily Bender, Timnit Gebru, Angelina McMillan-Major, and Margaret Mitchell published *On the Dangers of Stochastic Parrots* at the FAccT conference." — The fourth author is listed in the published paper as "Shmargaret Shmitchell," a pseudonym Margaret Mitchell used; the footnote [^bender] also names "Mitchell, M." The real human is Margaret Mitchell, but the paper's byline does not read "Margaret Mitchell." Year (2021), venue (FAccT '21), and page range (610–623) are all correct.
- **EVIDENCE | BASIC | CONTRADICTED (citation-year error)** — Footnote [^brynjolfsson] dates "The Turing Trap" to 2023; the *Daedalus* article (vol. 151, issue 2, pp. 272–287) was published in **2022**, not 2023. Volume/issue/pages are correct.

---
## Full Findings

### [EVIDENCE] — CONTRADICTED
**Assertion type:** BASIC (positive, named-finding)
**Sentence:** "In 2021, Emily Bender, Timnit Gebru, Angelina McMillan-Major, and Margaret Mitchell published *On the Dangers of Stochastic Parrots* at the FAccT conference."
**Claim checked:** Authorship, year, and venue of the Stochastic Parrots paper.
**Site visited:** https://dl.acm.org/doi/10.1145/3442188.3445922
**Finding:** The paper was published at FAccT '21 (2021), pp. 610–623 — year, venue, and page range confirmed. However, the published author list is "Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell." The fourth author appears under the pseudonym "Shmargaret Shmitchell" (widely understood to be Margaret Mitchell, then at Google). Naming her as "Margaret Mitchell" in the byline does not match the paper of record.
**Expert review needed:** Yes
**Suggested reference:** Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *Proceedings of the 2021 ACM FAccT Conference*, 610–623. https://dl.acm.org/doi/10.1145/3442188.3445922
**Notes:** Author intent (crediting Margaret Mitchell) is defensible, but the byline-as-published should be noted. Body text and footnote disagree with the canonical byline.

### [EVIDENCE] — CONTRADICTED
**Assertion type:** BASIC (citation metadata)
**Sentence:** Footnote [^brynjolfsson]: "Brynjolfsson, E. (2023). \"The Turing Trap...\" *Daedalus*, 151(2), 272–287."
**Claim checked:** Publication year of "The Turing Trap."
**Site visited:** https://direct.mit.edu/daed/article/151/2/272/110622/The-Turing-Trap-The-Promise-amp-Peril-of-Human
**Finding:** MIT Press lists the article in *Daedalus* 151(2), pp. 272–287, published 2022 (Spring 2022 issue). The volume, issue, and page numbers in the footnote are correct; the year "2023" is wrong and should read 2022.
**Expert review needed:** Yes
**Suggested reference:** Brynjolfsson, E. (2022). "The Turing Trap: The Promise & Peril of Human-Like Artificial Intelligence." *Daedalus*, 151(2), 272–287. https://doi.org/10.1162/daed_a_01915
**Notes:** Minor but verifiable metadata error.

### [STAT] — CONFIRMED
**Assertion type:** POSITIVE (specific figure, attributed)
**Sentence:** "PwC's 2025 *AI Jobs Barometer* reports that revenue per employee in AI-exposed industries grew nearly four times faster than in less-exposed sectors, and that workers with advanced AI skills command a wage premium of roughly 56% in PwC's US data."
**Claim checked:** PwC 2025 56% wage premium and ~4x productivity figure.
**Site visited:** https://www.pwc.com/gx/en/news-room/press-releases/2025/ai-linked-to-a-fourfold-increase-in-productivity-growth.html
**Finding:** PwC's 2025 Global AI Jobs Barometer reports a 56% average wage premium for jobs requiring AI skills (up from 25% the prior year) and a roughly fourfold increase in productivity growth in AI-exposed industries. Confirmed. PwC's framing is "average premium across industries hit 56%"; the book's "US/advanced-AI-skills cut" qualifier is consistent with the report's segmentation.
**Expert review needed:** No
**Suggested reference:** PwC. (2025). *The Fearless Future: 2025 Global AI Jobs Barometer.* https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html
**Notes:** The book's caveat about selection bias is its own honest editorializing, appropriately hedged.

### [STAT] — CONFIRMED
**Assertion type:** POSITIVE (specific figure, attributed)
**Sentence:** "Lightcast's 2025 job-posting analysis found that postings mentioning AI skills offered approximately 28% higher salaries — roughly $18,000 more per year — than comparable postings without."
**Claim checked:** Lightcast 28% / $18,000 AI-skills salary premium.
**Site visited:** https://www.prnewswire.com/news-releases/new-lightcast-report-ai-skills-command-28-salary-premium-as-demand-shifts-beyond-tech-industry-302511141.html
**Finding:** Lightcast's July 2025 report "Beyond the Buzz" found AI-skill job postings command a 28% salary premium — about $18,000/year more — across an analysis of 1.3 billion+ postings. Both the percentage and the dollar figure are confirmed verbatim.
**Expert review needed:** No
**Suggested reference:** Lightcast. (2025). *Beyond the Buzz: Developing the AI Skills Employers Actually Need.* https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23
**Notes:** None.

### [STAT / CURRENT] — CONFIRMED (number) / source-misattributed in flag
**Assertion type:** POSITIVE
**Sentence:** "The 33% drop in graphic design job postings reported in 2025 [verify — pull current cite from PwC AI Jobs Barometer 2025 or Lightcast] is happening whether you use the tools or not."
**Claim checked:** Is there a reported ~33% drop in graphic design job postings in 2025?
**Site visited:** https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/
**Finding:** Bloomberry's analysis of 180 million job postings found computer graphic-artist postings dropped 33% in 2025 (on top of a 12% decline in 2024). The 33% figure is real and current as of 2025–2026. However, the in-text verify-flag points the author to PwC or Lightcast; the figure actually traces to Bloomberry's job-posting analysis, not PwC/Lightcast.
**Expert review needed:** Yes (to fix the source attribution before publication)
**Suggested reference:** Bloomberry. (2025). "I analyzed 180M jobs to see what jobs AI is actually replacing today." https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/
**Notes:** The number survives; the suggested source in the bracketed note does not. WEF Future of Jobs 2025 separately ranks graphic design as 11th fastest-declining, a corroborating directional finding.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named finding)
**Sentence:** "Reber, Schwarz, and Winkielman documented this in 2004; Alter and Oppenheimer extended it in 2009."
**Claim checked:** Reber/Schwarz/Winkielman 2004 processing-fluency paper exists with that metadata.
**Site visited:** https://journals.sagepub.com/doi/10.1207/s15327957pspr0804_3
**Finding:** "Processing Fluency and Aesthetic Pleasure: Is Beauty in the Perceiver's Processing Experience?" by Reber, Schwarz & Winkielman appeared in *Personality and Social Psychology Review*, 2004, vol. 8(4), pp. 364–382. Matches footnote [^reber] exactly. (Alter & Oppenheimer 2009, *PSPR* 13(3), 219–235, is a standard well-attested citation consistent with footnote [^alter].)
**Expert review needed:** No
**Suggested reference:** Reber, R., Schwarz, N., & Winkielman, P. (2004). "Processing Fluency and Aesthetic Pleasure." *Personality and Social Psychology Review*, 8(4), 364–382. https://journals.sagepub.com/doi/10.1207/s15327957pspr0804_3
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named finding)
**Sentence:** "Frey and Osborne's 2017 paper on the automation of jobs identified three durable bottlenecks where machines still fail: perception and manipulation in unstructured environments, creative intelligence, and social intelligence."
**Claim checked:** The three Frey-Osborne automation bottlenecks.
**Site visited:** http://reparti.free.fr/freyosborne17.pdf
**Finding:** Frey & Osborne (2017), "The Future of Employment," *Technological Forecasting and Social Change* 114, 254–280, identify exactly three engineering bottlenecks to computerisation: perception and manipulation, creative intelligence, and social intelligence. Confirmed, including page range in footnote [^frey].
**Expert review needed:** No
**Suggested reference:** Frey, C. B., & Osborne, M. A. (2017). "The Future of Employment." *Technological Forecasting and Social Change*, 114, 254–280.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (named finding)
**Sentence:** "The intellectual ancestor is Daugherty and Wilson's *Human + Machine* (2018), which named \"the missing middle\"..."
**Claim checked:** Daugherty & Wilson coined "the missing middle" in Human + Machine (2018).
**Site visited:** https://www.accenture.com/us-en/insights/technology/human-plus-machine
**Finding:** Confirmed. Human + Machine: Reimagining Work in the Age of AI (Harvard Business Review Press, 2018) introduces the "missing middle" — the collaborative human-machine space few firms exploit. Matches footnote [^daugherty].
**Expert review needed:** No
**Suggested reference:** Daugherty, P. R., & Wilson, H. J. (2018). *Human + Machine: Reimagining Work in the Age of AI.* Harvard Business Review Press.
**Notes:** None.

### [EVIDENCE] — CONFIRMED
**Assertion type:** BASIC (historical / named-work)
**Sentence:** "Her 1987 book *Plans and Situated Actions* is the intellectual ancestor of the AI+1 frame." (AI Wayback — Lucy Suchman)
**Claim checked:** Suchman, Plans and Situated Actions, 1987, Cambridge University Press.
**Site visited:** https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/plans-and-situated-actions-the-problem-of-human-machine-communication-by-lucy-a-suchman-203-pages-cambridge-university-press-1987-2250-hardback-795-paperback/432867178C0DD2315F3C21989AA9A1DA
**Finding:** Confirmed: *Plans and Situated Actions: The Problem of Human-Machine Communication*, Lucy A. Suchman, Cambridge University Press, 1987. Footnote [^suchman] (incl. 2007 second edition as *Human-Machine Reconfigurations*) matches.
**Expert review needed:** No
**Suggested reference:** Suchman, L. A. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication.* Cambridge University Press.
**Notes:** None.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Michael Polanyi wrote in 1966 that \"we can know more than we can tell.\"" | EVIDENCE | BASIC | Standard, well-attested citation (*The Tacit Dimension*, 1966); not separately re-fetched. The quotation and year match the canonical source; treated as low-risk. |
| "Donald Schon picked up the same thread in 1983 and named it *reflection-in-action*." | EVIDENCE | BASIC | Standard well-attested citation (*The Reflective Practitioner*, 1983); not separately re-fetched. Low-risk. |
| "This is investigator triangulation in Norman Denzin's 1978 vocabulary." | EVIDENCE | BASIC | Denzin, *The Research Act*, 1978 is standard; not separately re-fetched here (verified in Ch.3 report). Low-risk. |

---
## AI-Pass Flags
- The 93% / 82% / 12% adoption figures attributed to Gemini and flagged "[verify — Figma State of the Designer 2026]" are presented BY THE BOOK as unverified candidate numbers and explicitly as a teaching example ("the most specific number is not necessarily the most accurate"). They are not the book's own assertions, so they are not flagged as prose errors. For the author's information: the Figma *State of the Designer 2026* report does exist, but its weekly-AI-usage figure is **91%** (up from 54% in 2025), not 93% (https://www.figma.com/blog/state-of-the-designer-2026/). The book's instinct to treat the 93% as needs-verification is correct.
- The "Margaret Mitchell" / "Shmargaret Shmitchell" issue (above) is an internal-consistency item worth one editorial note: the body text and footnote both name Margaret Mitchell, which is the correct human but not the published byline.
