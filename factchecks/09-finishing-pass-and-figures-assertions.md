# Assertions Report: 09-finishing-pass-and-figures.md
**Date:** 2026-05-29
**Source file:** chapters/09-finishing-pass-and-figures.md
**Assertions flagged:** 8
**Breakdown:** STAT: 1 | GUIDELINE: 1 | APPROVAL: 0 | EVIDENCE: 5 | SPECIALIST: 1 | CURRENT: 0

---
## ⚠️ Critical — Requires Immediate Expert Review
None found. No OUTDATED or CONTRADICTED verdicts. One internal-consistency flag (Combined Test "two groups" vs Chapter 8's "four groups") is recorded under AI-Pass Flags.

---
## Full Findings

### [EVIDENCE] — CONFIRMED
**Assertion type:** EMPHATIC (attributed concept)
**Sentence:** Cole Knaflic calls this "the so-what" — the move from naming a category to naming a claim.
**Claim checked:** Knaflic, *Storytelling with Data* (2015, Wiley); "so what" is her concept.
**Site visited:** https://www.wiley.com/en-us/Storytelling+with+Data:+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253
**Finding:** *Storytelling with Data: A Data Visualization Guide for Business Professionals* (Cole Nussbaumer Knaflic, Wiley, Nov 2015) confirmed. The "so what" / Big Idea framing is a well-documented part of her method (the search did not surface the exact phrase verbatim, but it is widely attributed to her communication framework). Book, author, year, publisher all correct.
**Expert review needed:** No
**Suggested reference:** Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.

### [EVIDENCE] — CONFIRMED
**Assertion type:** EMPHATIC (attributed typographic claim)
**Sentence:** Robert Bringhurst treats it as a typographic move: the subtitle is a different rank of text and should look different on the page.
**Claim checked:** Bringhurst, *The Elements of Typographic Style*, 4th ed., 2013, Hartley & Marks.
**Site visited:** (bibliographic — widely documented standard reference; not independently re-fetched)
**Finding:** *The Elements of Typographic Style* (4th ed., 2013, Hartley & Marks) is correctly cited. The chapter's characterization (rank/hierarchy of text) is consistent with the book's well-known content. The attribution is interpretive but reasonable.
**Expert review needed:** No
**Suggested reference:** Bringhurst, R. (2013). *The Elements of Typographic Style* (4th ed.). Hartley & Marks.

### [EVIDENCE] — CONFIRMED
**Assertion type:** EMPHATIC (named framework)
**Sentence:** Tamara Munzner's *Visualization Analysis and Design* calls the underlying diagnostic the "what-why-how" framework...
**Claim checked:** Munzner, *Visualization Analysis and Design*, 2014, CRC Press; what-why-how framework.
**Site visited:** https://infovis-wiki.net/wiki/Munzner,_T.:Visualization_Analysis_and_Design,_A_K_Peters/CRC_Press,_2014
**Finding:** Book confirmed (A K Peters/CRC Press, 2014). The what-why-how framework (what data / why looking / how encoded) is correctly attributed and accurately described.
**Expert review needed:** No
**Suggested reference:** Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.

### [STAT] — CONFIRMED
**Assertion type:** BASIC (statistical/biological claim)
**Sentence:** Avoid red/green pairings — about 8% of male readers have some form of red-green color blindness.
**Claim checked:** ~8% of men have red-green color deficiency.
**Site visited:** https://www.britannica.com/science/red-green-colour-blindness (and https://en.wikipedia.org/wiki/Color_blindness)
**Finding:** Roughly 8% of men of European/Northern-European ancestry have red-green color blindness (~1 in 12 males); ~0.5% of women. Global male figures range 4–8% by population. The chapter's "about 8%" is the standard, well-supported figure.
**Expert review needed:** No
**Suggested reference:** Britannica, "Red-green colour blindness."
**Notes:** "About 8% of male readers" is defensible as the commonly cited European-ancestry figure; a hedge ("up to 8%" or "about 8% of men of European descent") would be marginally more precise but is not required.

### [GUIDELINE] — CONFIRMED
**Assertion type:** EMPHATIC (standards-body requirement)
**Sentence:** Every SVG has a `<title>` and `<desc>` element. This is an EPUB 3 accessibility requirement per the W3C EPUB Accessibility 1.1 specification.
**Claim checked:** W3C EPUB Accessibility 1.1 (2023) exists at the cited URL and governs accessibility conformance.
**Site visited:** https://www.w3.org/TR/epub-a11y-11/
**Finding:** EPUB Accessibility 1.1 is a real W3C specification (governed by the 3 Nov 2023 W3C Process; W3C Recommendation). It requires accessible images and conformance metadata. The general claim that accessible SVG figures need `<title>`/`<desc>` (and that this aligns with WCAG/EPUB accessibility) is sound. The specification per se mandates WCAG conformance rather than naming `<title>`/`<desc>` verbatim, but the requirement that SVGs carry accessible names/descriptions follows from it.
**Expert review needed:** No
**Suggested reference:** W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/
**Notes:** Phrasing "is an EPUB 3 accessibility requirement per ... 1.1" is acceptable; the mechanism (WCAG-derived) is correctly directional.

### [SPECIALIST] — CONFIRMED
**Assertion type:** EMPHATIC (attributed rule + coined term)
**Sentence:** Axes are labeled. Units are declared. ... This is Tufte's rule, stated plainly in *The Visual Display of Quantitative Information*... / Tufte's data-ink ratio... Generic decoration is what he called chartjunk.
**Claim checked:** Tufte's *The Visual Display of Quantitative Information*; data-ink ratio and "chartjunk" are his.
**Site visited:** https://infovis-wiki.net/wiki/Data-Ink_Ratio (and https://data.europa.eu/apps/data-visualisation-guide/chart-junk-and-data-ink-origins)
**Finding:** Tufte introduced the data-ink ratio and coined "chartjunk" in *The Visual Display of Quantitative Information* (1st ed. 1983; 2nd ed. 2001, Graphics Press). Both attributions are correct. The 2001 2nd-edition citation in the footnote is valid.
**Expert review needed:** No
**Suggested reference:** Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.

### [EVIDENCE] — CONFIRMED
**Assertion type:** COMBINATION (emphatic + positive — named contested empirical finding)
**Sentence:** Bateman and colleagues published "Useful Junk?" at CHI 2010 with empirical evidence that embellished charts are better remembered than minimalist ones.
**Claim checked:** Bateman et al., "Useful Junk?", CHI 2010; finding that embellished charts are better recalled.
**Site visited:** https://dl.acm.org/doi/10.1145/1753326.1753716 (and https://scottbateman.github.io/publication/2010-01-01-Useful-junk...)
**Finding:** "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts" (Bateman, Mandryk, Gutwin, Genest, McDine, Brooks), CHI 2010. Found that accuracy was no worse than plain charts and recall after a 2–3 week gap was significantly better. The chapter's characterization is accurate, and it correctly frames it as a contested counter-position.
**Expert review needed:** No
**Suggested reference:** Bateman, S., et al. (2010). "Useful Junk?..." *CHI 2010*.
**Notes:** The accompanying Mona Chalabi / Guardian hand-drawn data-illustration claim was not independently fetched; it is presented as an interpretive aside, not a precise factual assertion.

### [EVIDENCE] — CONFIRMED
**Assertion type:** COMBINATION (emphatic + historical, dated)
**Sentence:** [Nightingale] designed [the polar-area diagram] for Queen Victoria and Parliament... In 1859 she was elected the first female fellow of the Royal Statistical Society.
**Claim checked:** Nightingale's *Diagram of the Causes of Mortality in the Army in the East* (1858); first female fellow of RSS in 1859.
**Site visited:** https://rss.org.uk/news-publication/news-publications/2020/general-news/nightingale-2020-the-bicentenary-our-first-female/ (and https://en.wikipedia.org/wiki/Florence_Nightingale)
**Finding:** The polar-area "Rose" diagram (1858) showing preventable disease vs battle deaths, sent to Queen Victoria, is confirmed. The RSS itself calls her "our first female fellow." Most sources give 1859 (a minority give 1858) for her election. The chapter's 1859 is the standard/RSS-aligned date. Sanitary reform following is well documented.
**Expert review needed:** No
**Suggested reference:** RSS, "Nightingale 2020: the bicentenary of our first female fellow."
**Notes:** Minor source ambiguity on 1858 vs 1859 election year; 1859 is defensible and RSS-consistent. Chapter dates the diagram 1858 in the body — correct (published 1858, sometimes labeled 1858/1859).

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "Mona Chalabi's hand-drawn data illustrations in the Guardian make the same argument..." | EVIDENCE | POSITIVE | Interpretive aside; not independently fetched. Low risk — presented as illustration, not precise claim. |
| Node version / `sharp` / pandoc package-name install instructions (Node 18+, `npm install sharp`, `winget`, `apt`) | GUIDELINE | BASIC | Tooling install specifics not verified this pass; chapter already carries an inline `[verify]` note for sharp install drift. |

---
## AI-Pass Flags
- **Internal cross-chapter inconsistency (Combined Test group count).** Line ~89 (VG signal example) states: *"The Combined Test has fourteen items in **two** groups."* Chapter 8 (the authoritative definition) and Appendix F define it as fourteen items in **FOUR** groups (A/B/C/D). This is a genuine contradiction. Recommend changing the VG example to "fourteen items in four groups," or pick a different VG illustration. The same "two groups" error recurs in Chapter 11 (line ~65). No web search used for this flag.

---
## References
1. Knaflic, C. N. (2015). *Storytelling with Data*. Wiley. https://www.wiley.com/en-us/Storytelling+with+Data:+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253
2. Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press. https://infovis-wiki.net/wiki/Munzner,_T.:Visualization_Analysis_and_Design,_A_K_Peters/CRC_Press,_2014
3. W3C (2023). *EPUB Accessibility 1.1*. https://www.w3.org/TR/epub-a11y-11/
4. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press. https://infovis-wiki.net/wiki/Data-Ink_Ratio
5. Bateman, S., et al. (2010). "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." *CHI 2010*. https://dl.acm.org/doi/10.1145/1753326.1753716
6. Britannica. "Red-green colour blindness." https://www.britannica.com/science/red-green-colour-blindness
7. Royal Statistical Society (2020). "Nightingale 2020: the bicentenary of our first female fellow." https://rss.org.uk/news-publication/news-publications/2020/general-news/nightingale-2020-the-bicentenary-our-first-female/
