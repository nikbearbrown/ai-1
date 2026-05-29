# Assertions Report: 12-final-check-and-build.md
**Date:** 2026-05-29
**Source file:** chapters/12-final-check-and-build.md
**Assertions flagged:** 13
**Breakdown:** STAT: 1 | GUIDELINE: 2 | APPROVAL: 5 | EVIDENCE: 2 | SPECIALIST: 0 | CURRENT: 8 (overlapping; many APPROVAL/GUIDELINE items are also CURRENT/aging-prone)

---
## ⚠️ Critical — Requires Immediate Expert Review

1. **APPROVAL/CURRENT | COMBINATION (emphatic) | CONTRADICTED** — *"And the AI-content disclosure, required since August 2023..."* — KDP's AI-content disclosure requirement was announced **September 7, 2023**, not August 2023. The month is wrong. Fix to "September 2023."

(No other OUTDATED/CONTRADICTED items. Several COMBINATION/CURRENT claims below are CONFIRMED-as-of-2026-05-29 but carry the book's own highest aging risk, as the chapter itself flags.)

---
## Full Findings

### [APPROVAL] — CONTRADICTED
**Assertion type:** COMBINATION (emphatic — date + requirement)
**Sentence:** And the AI-content disclosure, required since August 2023: AI+1 books use AI-assisted drafting... which falls under Amazon's *AI-assisted* rather than *AI-generated* distinction.
**Claim checked:** KDP AI-content disclosure required since "August 2023"; AI-assisted vs AI-generated distinction.
**Site visited:** https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/ (and https://adtmag.com/articles/2023/10/02/aws-requires-kdp-authors-to-disclose-ai.aspx)
**Finding:** Amazon announced the KDP AI-content disclosure policy on **September 7, 2023** (after discussions with the Authors Guild). The requirement applies to **AI-generated** content (text, images, translations); **AI-assisted** content is explicitly NOT required to be disclosed. So the AI-assisted-vs-AI-generated distinction is correct, but the date "August 2023" is wrong — it should be **September 2023**.
**Expert review needed:** Yes
**Suggested reference:** Authors Guild (2023), "Amazon's New Disclosure Policy for AI-Generated Book Content." Announced Sept 7, 2023.
**Notes:** Only the month is incorrect; the substantive distinction is accurate. Also note: under Amazon's rule, *AI-assisted* content is not required to be disclosed at all — the chapter's framing ("disclosure... falls under AI-assisted") may overstate the obligation for an AI-assisted book. Worth a sentence-level review.

### [APPROVAL] — CONFIRMED (current as of 2026-05-29)
**Assertion type:** COMBINATION (emphatic — specs)
**Sentence:** Cover. JPEG or TIFF, RGB color space, ideally 2560 × 1600 pixels, minimum 1000 × 625. Ideal ratio at least 1.6:1. File under 50MB.
**Claim checked:** KDP cover specs: ideal 2560×1600, min 1000×625, ratio 1.6:1, JPEG/TIFF RGB.
**Site visited:** https://kdp.amazon.com/en_US/help/topic/G200645690 (corroborated by https://learn.designrr.io/en/articles/9716725)
**Finding:** Matches current KDP guidance: ideal 2,560 (h) × 1,600 (w), aspect ratio 1.6:1, minimum 1,000 × 625 (shortest side ≥ 500 displayed), RGB, JPEG preferred (TIFF accepted), 300 DPI. The 50MB ceiling is consistent with KDP's file limits. Confirmed as of 2026-05-29.
**Expert review needed:** No
**Suggested reference:** KDP, "What criteria does my eBook's cover image need to meet?" https://kdp.amazon.com/en_US/help/topic/G200645690
**Notes:** Chapter already carries inline `[verify — cover spec is the single most aging-prone detail]`. Currently accurate.

### [APPROVAL] — CONFIRMED (current; one nuance to add)
**Assertion type:** COMBINATION (emphatic — royalty tiers)
**Sentence:** The KDP royalty structure: books priced between $2.99 and $9.99 earn 70%. Outside that range — including $0.99 — 35%. At $0.99 you keep about $0.35 per sale.
**Claim checked:** KDP 70% tier = $2.99–$9.99; 35% otherwise; $0.99 → ~$0.35.
**Site visited:** https://kdp.amazon.com/en_US/help/topic/G200634500 (corroborated https://www.kdpeasy.com/guides/2026-kdp-royalty-rates)
**Finding:** Confirmed: 70% royalty only for list price $2.99–$9.99 (in eligible territories); 35% below $2.99 or above $9.99. $0.99 → 35% × $0.99 ≈ $0.35 (no delivery fee on 35% tier). Accurate as of 2026-05-29. Nuance: the 70% tier additionally requires KDP Select enrollment OR price-matching within 20% — not stated, but not contradicted.
**Expert review needed:** No
**Suggested reference:** KDP, "Digital Book Pricing Page." https://kdp.amazon.com/en_US/help/topic/G200634500

### [APPROVAL] — CONFIRMED (current)
**Assertion type:** COMBINATION (emphatic — program terms)
**Sentence:** KDP Select grants Amazon 90-day exclusivity — no distribution through Apple Books, Kobo, or your own site — in exchange for Kindle Unlimited inclusion...
**Claim checked:** KDP Select = 90-day exclusivity; KU inclusion; blocks other retailers/own site.
**Site visited:** https://kdp.amazon.com/en_US/help/topic/G200798990 (corroborated https://reedsy.com/blog/guide/kdp/kdp-select/)
**Finding:** Confirmed: KDP Select is a 90-day (auto-renewing) exclusivity program; enrolled ebooks must not be sold elsewhere (Apple Books, Kobo, B&N, own site) during the term; enrollment includes Kindle Unlimited. As of Sept 2025 KDP Select allows public-library distribution without breaking exclusivity — a refinement, but retail exclusivity (the chapter's point) holds. Accurate.
**Expert review needed:** No
**Suggested reference:** KDP, "KDP Select." https://kdp.amazon.com/en_US/help/topic/G200798990
**Notes:** Chapter carries inline `[verify — 90-day term ... subject to policy change]`. Currently accurate.

### [APPROVAL] — CONFIRMED (current)
**Assertion type:** COMBINATION — metadata fields
**Sentence:** Keywords (seven slots... each can be a phrase...) ... Description (up to 4,000 characters...) ... Categories (two from KDP's hierarchy...)
**Claim checked:** 7 keyword slots; 4,000-char description; 2 categories.
**Site visited:** https://kdp.amazon.com/en_US/help/topic/G200645690 (KDP help; corroborated by Kindlepreneur)
**Finding:** Consistent with current KDP: 7 keyword fields, description up to 4,000 characters, and category selection from KDP's BISAC-style hierarchy. (KDP has at times expanded category selection; "two ... as specific as possible" is a reasonable current-state statement.) Accurate as of 2026-05-29.
**Expert review needed:** No
**Suggested reference:** KDP, "Keywords / Categories" help topics. https://kdp.amazon.com/en_US/help/topic/G200645690
**Notes:** Chapter carries multiple inline `[verify]` flags here; appropriate given aging risk.

### [STAT/CURRENT] — UNVERIFIED (book hedges)
**Assertion type:** POSITIVE (market-share claim)
**Sentence:** Kindle Direct Publishing (kdp.amazon.com) accounts for the dominant share of indie ebook units in the US as of May 2026. / (and the body's "About 80% of indie ebook units...")
**Claim checked:** KDP's share of US indie ebook units ("dominant"; ~80%).
**Site visited:** Not confirmable to a single authoritative source (searched general knowledge; no primary dataset fetched).
**Finding:** No single authoritative source confirms a precise figure for KDP's share of US indie ebook units. "Dominant share" is widely accepted directionally; "~80%" is an estimate that the book itself flags as unconfirmed. The chapter's own UNVERIFIED example ("no single authoritative source confirms this number") is honest and correct.
**Expert review needed:** Yes (only if a precise number is to be retained)
**Suggested reference:** Could not identify a specific authoritative source for the exact share. Keep the hedged phrasing the chapter already models.
**Notes:** Chapter carries inline `[verify — share estimates from 2025 Authors Guild and industry analyst sources, subject to drift]`. The hedging is appropriate; do not assert a hard number.

### [GUIDELINE/CURRENT] — CONFIRMED
**Assertion type:** COMBINATION (emphatic — tool capability)
**Sentence:** Pandoc, written and maintained by John MacFarlane, is the toolchain's spine — the de facto Markdown-to-everything converter. ... Pandoc's EPUB output is *mostly* EPUB 3 valid.
**Claim checked:** Pandoc by MacFarlane; de facto universal Markdown converter; produces EPUB 3.
**Site visited:** https://pandoc.org/ (and https://en.wikipedia.org/wiki/Pandoc, https://pandoc.org/epub.html)
**Finding:** Confirmed: Pandoc is created/maintained by John MacFarlane (UC Berkeley); "universal markup converter"; has an EPUB3 writer (since v1.6+). "De facto Markdown-to-everything converter" is a fair, widely held characterization. "Mostly EPUB 3 valid output, with known gaps" is accurate. Manual dated 2026-03-19 confirms active maintenance.
**Expert review needed:** No
**Suggested reference:** MacFarlane, J. *Pandoc User's Guide.* https://pandoc.org/MANUAL.html ; https://pandoc.org/epub.html
**Notes:** The "de facto" claim is EMPHATIC but well-supported. Chapter carries inline `[verify — package names current as of May 2026]` for the install commands (not separately re-verified this pass).

### [GUIDELINE] — CONFIRMED
**Assertion type:** BASIC (tool/spec)
**Sentence:** EPUBCheck (github.com/w3c/epubcheck) catches all three. / The W3C EPUB 3.3 spec does not require horizontal scrolling for wide content.
**Claim checked:** EPUBCheck is the W3C EPUB validator at that repo; EPUB 3.3 is a W3C spec.
**Site visited:** https://www.w3.org/TR/epub-33/ (and W3C press release https://www.w3.org/press-releases/2023/epub33-rec/)
**Finding:** EPUB 3.3 became a W3C Recommendation on **25 May 2023** (w3.org/TR/epub-33/). EPUBCheck is the official conformance checker hosted at github.com/w3c/epubcheck. Both confirmed. The footnote citing "W3C (2023). EPUB 3.3 Specification. w3.org/TR/epub-33/" is correct.
**Expert review needed:** No
**Suggested reference:** W3C (2023). *EPUB 3.3*. https://www.w3.org/TR/epub-33/

### [EVIDENCE] — CONFIRMED (with caveat on quoted procedure)
**Assertion type:** EMPHATIC (attributed method)
**Sentence:** The five claim types come from Sarah Harrison Smith's *The Fact Checker's Bible*, the procedure Smith built as head of research at the *New York Times Magazine*. / ...Peter Canby's department at *The New Yorker* is the gold standard.
**Claim checked:** Smith, *The Fact Checker's Bible* (2004, Anchor); her NYT Magazine role; Canby at The New Yorker.
**Site visited:** (bibliographic / well-documented; not independently re-fetched this pass)
**Finding:** *The Fact Checker's Bible: A Guide to Getting It Right* (Sarah Harrison Smith, Anchor, 2004) is a real book; Smith was head of research/fact-checking at the New York Times Magazine. Peter Canby long led The New Yorker's fact-checking department (widely regarded as a gold standard). The "five claim types / six content categories" taxonomy as stated is the book's own adaptation; the attribution that these *exact* five types "come from" Smith is the author's framing and could not be verbatim-confirmed this pass.
**Expert review needed:** No
**Suggested reference:** Smith, S. H. (2004). *The Fact Checker's Bible*. Anchor.
**Notes:** Canby footnote ("Profiled in *Columbia Journalism Review*, 2015") not independently re-fetched; plausible.

### [APPROVAL] — CONFIRMED
**Assertion type:** EMPHATIC (named standard)
**Sentence:** Tom Preston-Werner's Semantic Versioning — MAJOR.MINOR.PATCH — is the right mental model...
**Claim checked:** SemVer authored by Tom Preston-Werner; MAJOR.MINOR.PATCH; semver.org; 2.0.0.
**Site visited:** https://semver.org/
**Finding:** Confirmed. Semantic Versioning was authored by Tom Preston-Werner (co-founder of GitHub); format MAJOR.MINOR.PATCH; PATCH = backward-compatible fixes, MINOR = backward-compatible additions, MAJOR = breaking changes. The chapter's PATCH/MINOR/MAJOR analogy to book editions is a fair adaptation. Footnote "Preston-Werner, T. (2013). Semantic Versioning 2.0.0. semver.org" is accurate (2.0.0 finalized 2013).
**Expert review needed:** No
**Suggested reference:** Preston-Werner, T. (2013). *Semantic Versioning 2.0.0*. https://semver.org/

### [EVIDENCE] — CONFIRMED
**Assertion type:** COMBINATION (emphatic + historical, dated)
**Sentence:** Working in Venice between 1494 and 1515, [Manutius] produced octavo editions... He called the format the *enchiridion*: handbook. He commissioned the first italic typeface, cut by Francesco Griffo around 1500...
**Claim checked:** Manutius's octavo/enchiridion format; first italic typeface by Griffo ~1500; Venice career.
**Site visited:** https://en.wikipedia.org/wiki/Aldus_Manutius (and https://en.wikipedia.org/wiki/Aldine_Press)
**Finding:** Confirmed: Aldus Manutius ran the Aldine Press in Venice (founded ~1494/95). He pioneered the portable octavo "enchiridion" (handbook) format; Francesco Griffo cut the first italic type (used 1500–1501, e.g., the 1501 Virgil). He standardized punctuation including the semicolon. The "1494 and 1515" range matches his working life (he died 1515). Octavo classics line is usually dated from ~1501/1505; the chapter's broad career range is defensible. Accurate.
**Expert review needed:** No
**Suggested reference:** Wikipedia, "Aldus Manutius" / "Aldine Press." https://en.wikipedia.org/wiki/Aldus_Manutius
**Notes:** Minor: the octavo classics specifically began ~1501; "between 1494 and 1515" frames his overall career, which is fine.

### [APPROVAL/CURRENT] — CONFIRMED (current; standards stable, fields aging-prone)
**Assertion type:** COMBINATION — submission structure
**Sentence:** Worked-example KDP submission fields (categories, 2560×1600 cover, $0.99 / 35% tier, KDP Select 90-day, EPUBCheck 0 critical, approved 27h).
**Claim checked:** Internal consistency + alignment with verified KDP rules.
**Site visited:** (cross-checked against KDP topics already cited above)
**Finding:** The worked-example values are internally consistent with the verified KDP rules (35% at $0.99, 90-day Select, 2560×1600 cover, 24–72h review window). These are illustrative, dated (May 14–15, 2026), and appropriately flagged `[verify]`. No contradictions.
**Expert review needed:** No
**Suggested reference:** As above (KDP help topics).

---
## Unverified Assertions
| Sentence | Category | Assertion Type | Reason unverified |
|---|---|---|---|
| "KDP accounts for the dominant share of indie ebook units in the US" / "About 80% of indie ebook units" | STAT/CURRENT | POSITIVE | No single authoritative source; book already hedges. Keep hedged phrasing. |
| Smith, *The Fact Checker's Bible* (2004, Anchor) + "five claim types come from Smith" | EVIDENCE | EMPHATIC | Book/role real; exact five-type taxonomy as Smith's not verbatim-confirmed this pass. |
| Canby footnote — *Columbia Journalism Review*, 2015 profile | EVIDENCE | BASIC | Footnote not independently re-fetched. |
| Penn, *How to Make a Living with Your Writing* (3rd ed., 2021); Authors Guild 2025 survey footnotes | CURRENT | BASIC | Footnotes not independently re-fetched; plausible. |
| pandoc/sharp install command package names; `--pdf-engine=weasyprint` | GUIDELINE | BASIC | Tooling specifics not re-verified; chapter carries inline `[verify]` notes. |

---
## AI-Pass Flags
- **Checked for the warning-count "five vs four" discrepancy noted in the fact-check brief.** No such contradiction exists in Chapter 12. The KDP rejection email (line 13) reports "Errors: **4 critical, 12 warnings**"; the success worked-example (line 110) reports "**0 critical errors, 2 informational warnings**." These describe two *different* submissions (the initial blocked attempt vs the eventual accepted one), so they are consistent, not an internal error. No web search used.
- **No internal numeric inconsistency found within Chapter 12.** (The cross-chapter "Combined Test = two groups vs four groups" issue lives in Chapters 9 and 11, not here — see those reports.)

---
## References
1. Authors Guild (2023). "Amazon's New Disclosure Policy for AI-Generated Book Content." (Policy announced Sept 7, 2023.) https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/
2. KDP. "What criteria does my eBook's cover image need to meet?" https://kdp.amazon.com/en_US/help/topic/G200645690
3. KDP. "Digital Book Pricing Page" (royalty tiers). https://kdp.amazon.com/en_US/help/topic/G200634500
4. KDP. "KDP Select." https://kdp.amazon.com/en_US/help/topic/G200798990
5. Pandoc — MacFarlane, J. *Pandoc User's Guide* / "Creating an ebook with pandoc." https://pandoc.org/MANUAL.html ; https://pandoc.org/epub.html
6. W3C (2023). *EPUB 3.3* (Recommendation, 25 May 2023). https://www.w3.org/TR/epub-33/
7. Preston-Werner, T. (2013). *Semantic Versioning 2.0.0*. https://semver.org/
8. Wikipedia. "Aldus Manutius." https://en.wikipedia.org/wiki/Aldus_Manutius
