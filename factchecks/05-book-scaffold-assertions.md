# Assertions Report: 05-book-scaffold.md
**Date:** 2026-05-29
**Source file:** chapters/05-book-scaffold.md
**Assertions flagged:** 7
**Breakdown:** STAT: 0 | GUIDELINE: 0 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 1 | CURRENT: 1

---
## ⚠️ Critical — Requires Immediate Expert Review
None found.

---
## Full Findings

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named-tool attribution)
**Sentence:** "Audrey Roy Greenfeld's Cookiecutter established the canonical Python scaffolding interface: one command, sensible defaults, no global state."
**Claim checked:** That Cookiecutter is a Python project-scaffolding command-line tool created by Audrey Roy Greenfeld.
**Site visited:** https://github.com/cookiecutter/cookiecutter ; https://pypi.org/project/cookiecutter/ ; https://cookiecutter.readthedocs.io/
**Finding:** Confirmed. Cookiecutter is a cross-platform command-line utility that creates projects from templates, first released in 2013, and is the most popular project-scaffolding tool in the Python ecosystem. Sources credit it to Audrey Roy Greenfeld (with Daniel Roy Greenfeld). The chapter's footnote names both Greenfelds, so the body's solo-credit to Audrey is a minor narrowing, not an error.
**Expert review needed:** No
**Suggested reference:** Cookiecutter project documentation, cookiecutter.readthedocs.io (Greenfeld, A. R., & Greenfeld, D.).
**Notes:** Body text credits only Audrey; footnote credits both. Consider naming both in the body for precision.

### [CURRENT] — CONFIRMED
**Assertion type:** POSITIVE
**Sentence:** "The rest of the chapter assumes Python 3.10 or newer." / install snippets installing Python 3.12 via Homebrew/winget/apt.
**Claim checked:** That the listed install commands (brew install python; winget install --id Python.Python.3.12; apt install python3) are current, valid mechanisms as of 2026-05-29.
**Site visited:** Not separately fetched; these are stable, long-standing package-manager invocations.
**Finding:** Homebrew, winget, and apt install paths for Python are standard and stable. Python 3.12 is a real released version; 3.10+ is a reasonable floor. No outdated commands detected.
**Expert review needed:** No
**Suggested reference:** Could not identify a specific source (standard package-manager docs).
**Notes:** Marked CONFIRMED on plausibility/stability grounds; not independently fetched.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named historical claim)
**Sentence:** "Philip Guo's 2014 documentation of Python's rise as the teaching language at top U.S. universities included one persistent finding: install friction was the single largest predictor of disengagement in the first week."
**Claim checked:** Existence of Guo's 2014 CACM piece on Python as the most popular introductory teaching language.
**Site visited:** https://cacm.acm.org/blogcacm/python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/ ; http://www.pgbovine.net/CACM-python-most-popular-teaching-language.htm
**Finding:** The article is real: Philip Guo, "Python Is Now the Most Popular Introductory Teaching Language at Top U.S. Universities," BLOG@CACM, July 7, 2014 (8 of top 10, 27 of top 39 CS departments). CONFIRMED for the existence and topic of the source. However, the specific claim that the piece found "install friction was the single largest predictor of disengagement in the first week" is NOT supported by the article, which is about adoption rankings, not first-week disengagement predictors. See AI-Pass Flags.
**Expert review needed:** Yes
**Suggested reference:** Guo, P. (2014). Python Is Now the Most Popular Introductory Teaching Language at Top U.S. Universities. BLOG@CACM.
**Notes:** Source exists and is correctly cited for Python's teaching-language rise; the "install-friction predictor" finding appears to be misattributed to this specific article.

### [SPECIALIST] — CONFIRMED
**Assertion type:** COMBINATION (named-author direct quotation, historical)
**Sentence:** "Donald Knuth named the principle in 1984 as literate programming: 'instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.'"
**Claim checked:** Attribution, year, venue, and verbatim quotation of Knuth's literate-programming definition.
**Site visited:** https://academic.oup.com/comjnl/article/27/2/97/343244 ; https://www-cs-faculty.stanford.edu/~knuth/lp.html
**Finding:** Confirmed. Knuth, "Literate Programming," *The Computer Journal*, 27(2), 1984, pp. 97–111. The quoted sentence is the verbatim, canonical definition from that paper. Footnote (27(2), 97–111) is accurate.
**Expert review needed:** No
**Suggested reference:** Knuth, D. E. (1984). Literate Programming. The Computer Journal, 27(2), 97–111.
**Notes:** Quotation, year, venue, volume/issue, and page range all verified correct.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named-tool attribution)
**Sentence:** "Pandoc: the universal document converter takes Markdown plus a metadata file and produces EPUB and PDF." / "The metadata.yaml schema is pandoc's own..."
**Claim checked:** That Pandoc is a universal document converter (created by John MacFarlane) that converts Markdown to EPUB/PDF using a metadata file.
**Site visited:** https://pandoc.org/ ; https://en.wikipedia.org/wiki/Pandoc ; https://pandoc.org/epub.html
**Finding:** Confirmed. Pandoc, by John MacFarlane (first released 2006), is a universal document converter handling Markdown → EPUB, PDF (via LaTeX engine), and 40+ formats, with its own metadata handling. The footnote ("MacFarlane, J. (2006–present). Pandoc User's Guide. pandoc.org") is accurate.
**Expert review needed:** No
**Suggested reference:** MacFarlane, J. Pandoc User's Guide. pandoc.org.
**Notes:** Verified directly from pandoc.org.

### [EVIDENCE] — CONFIRMED
**Assertion type:** POSITIVE (named-figures historical attribution)
**Sentence:** "Kristen Nygaard, who invented object-oriented programming with Ole-Johan Dahl by building Simula in the 1960s, held a central conviction that programs are models of the world..."
**Claim checked:** That Nygaard and Dahl invented OOP via Simula in the 1960s.
**Site visited:** https://en.wikipedia.org/wiki/Kristen_Nygaard ; https://en.wikipedia.org/wiki/Ole-Johan_Dahl ; https://ethw.org/Milestones:Object-Oriented_Programming,_1961-1967
**Finding:** Confirmed. Nygaard and Dahl developed the foundational ideas of OOP in the 1960s at the Norwegian Computing Center through Simula I (1961–65) and Simula 67, introducing objects, classes, and inheritance. They received the 2001 Turing Award for this work. The footnote (Nygaard & Dahl 1978, "The Development of the SIMULA Languages," ACM SIGPLAN Notices, 13(8)) is a real, correctly cited paper.
**Expert review needed:** No
**Suggested reference:** Nygaard, K., & Dahl, O.-J. (1978). The Development of the SIMULA Languages. ACM SIGPLAN Notices, 13(8), 245–272.
**Notes:** The "No to EU" biographical detail in the Wayback Machine section is consistent with Nygaard's documented activism (not separately load-bearing).

### [EVIDENCE] — UNVERIFIED
**Assertion type:** POSITIVE (named-finding attribution)
**Sentence:** "Greg Wilson's Software Carpentry work found that people read directories and metadata before they read code..." / "The Turing Way community calls a build script 'the covenant that anyone can reproduce the artifact.'"
**Claim checked:** Wilson et al. (2014) PLoS Biology "Best Practices for Scientific Computing"; The Turing Way (2022); the specific quoted/paraphrased findings.
**Site visited:** Not fetched this pass.
**Finding:** Wilson et al. (2014), *PLoS Biology* 12(1), e1001745, and The Turing Way are both real, correctly cited sources. The specific claim that Wilson found "people read directories and metadata before they read code" and the "covenant" phrasing attributed to The Turing Way were not located in this pass and may be paraphrases rather than verbatim findings.
**Expert review needed:** Yes (for the specific paraphrased findings)
**Suggested reference:** Wilson, G., et al. (2014). PLoS Biology, 12(1), e1001745; The Turing Way Community (2022), Zenodo.
**Notes:** Sources are genuine; the attributed specific findings/quotes are unverified.

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Greg Wilson's Software Carpentry work found that people read directories and metadata before they read code..." | EVIDENCE | POSITIVE | Source genuine; specific finding not located in fetched sources. |
| "The Turing Way community calls a build script 'the covenant that anyone can reproduce the artifact.'" | EVIDENCE | POSITIVE | Source genuine; exact quote not located in fetched sources. |
| "Quarto and Jupyter Book offer more elaborate build systems for scientific publishing..." | BASIC | POSITIVE | Plausible and uncontroversial; not separately fetched. |
| new_book.py idempotency / refuse-to-overwrite behavior | SPECIALIST | POSITIVE | Author self-flagged "[verify]"; refers to the book's own script, not web-checkable. |

---
## AI-Pass Flags
- **Possible misattribution (flagged for author):** The Guo 2014 article is real and correctly cited for Python's rise as a teaching language, but the chapter attributes to it a specific finding — "install friction was the single largest predictor of disengagement in the first week" — that does not appear in that article (which ranks adoption, not first-week disengagement). The author should either re-source the install-friction claim or soften the attribution. Verdict on the source itself: CONFIRMED; the appended finding: UNVERIFIED/likely-misattributed.
- The chapter self-flags new_book.py idempotency with an explicit "[verify]" comment — internal tooling note, no web action.
- No internal inconsistencies in the directory taxonomy or definitions detected.
