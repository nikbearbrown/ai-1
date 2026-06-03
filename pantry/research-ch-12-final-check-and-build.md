# Research: Chapter 12 — Final Check and Build: EPUB + PDF
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students run the final check sequence, build the EPUB and PDF, and submit to Kindle Direct Publishing — understanding the rebuild loop as normal finishing process.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

**David Gaughran. *Let's Get Digital: How to Self-Publish, and Why You Should* (2011; 4th ed. 2021).** The practitioner-canonical text for indie publishing on KDP and adjacent platforms. Covers the economic case for self-publishing (royalty structure, control, speed), the operational case (cover design, blurb craft, metadata), and the *post-launch* case (marketing, mailing lists, series strategy). Gaughran's central argument relevant to AI+1: the production discipline that produces a publishable indie book is closer to running a small business than to writing in the traditional sense. The author-instructor reader needs to internalize this.

**Joanna Penn. *How to Make a Living with Your Writing* (2015; 3rd ed. 2021).** Curl Up Press. Penn (Wikipedia: "Joanna Penn") is the longest-running practitioner voice on self-publishing-as-business. Her *Creative Penn* podcast (live since 2009) is the deepest archive of working-author interviews on the indie side. Penn's framework — multiple streams (book sales, audio, courses, speaking), platform-agnostic distribution, long-tail catalog over hit-driven thinking — directly informs Chapter 11's positioning of KDP as one channel, not the entire game.

**W3C. *EPUB 3.3 Specification* (Recommendation, 2023).** w3.org/TR/epub-33/. The current EPUB standard. Bill Kasdorf was a key editor on EPUB 3.0 and remains the publishing-industry voice on the spec. EPUB 3 introduced HTML5/CSS3 content, JavaScript support (Reading Systems may disable), MathML, scripted interactivity, and structural semantics for accessibility. EPUB 3.3 (2023) tightens accessibility requirements (WCAG 2.0 Level AA conformance is now a strong recommendation, mandatory for many distribution channels).

**John MacFarlane. Pandoc documentation (pandoc.org).** MacFarlane is pandoc's author and remains the active maintainer. Pandoc is the toolchain spine of the AI+1 build script: Markdown → combined.md → EPUB + PDF via `--epub-cover-image`, `--toc`, `--toc-depth`, `--metadata` flags. The pandoc User's Guide is the reference document. Citation: pandoc.org/MANUAL.html; canonical introduction is MacFarlane's "Pandoc: a universal document converter."

**Sarah Harrison Smith. *The Fact Checker's Bible* (2004).** Anchor. Smith was head of research at *The New York Times Magazine*. The book is the working procedure for verifying claims at scale: assertion taxonomy (named, dated, statistical, attributed, characterized), the triage rule that *contradicted* claims demand resolution before publication while *unverified* claims may travel with a flag, the discipline that the author and the fact-checker are separate roles even when the same person is doing both. Directly informs Chapter 11's "Fact-Checking Assistant" output triage (OUTDATED → CONTRADICTED → UNVERIFIED).

**Peter Canby and the *New Yorker* fact-checking department.** Canby was head of fact-checking at *The New Yorker* from 1994 to 2024. The *New Yorker* process is the gold standard the trade publishing world references: every assertable claim in every published piece is verified against primary sources; checkers read aloud against the source. Profiled in *Columbia Journalism Review* and elsewhere; Canby's own 2013 essay "Fact-Checking at *The New Yorker*" in *The New Yorker* archive is the accessible source.

**Tom Preston-Werner. "Semantic Versioning" (semver.org, 2011, revised through 2.0.0 in 2013).** The MAJOR.MINOR.PATCH spec that became the de facto versioning standard for software. Preston-Werner co-founded GitHub. The relevance to Chapter 11's "rebuild loop": treating a book as a versioned artifact — 1.0.0 at first launch, 1.1.0 when a new chapter or substantial revision ships, 1.0.1 for typo fixes — is the indie-publishing-as-software analogy that makes the rebuild loop legible to the reader.

**Hugh Howey. "The Author Earnings Reports" (authorearnings.com, 2014–2017) and *Wayfinder* (2024).** Howey's self-published *Wool* (2011) was the most prominent crossover from indie to traditional in the early KDP era. His Author Earnings reports — though discontinued — produced the first large-scale data on indie vs. traditional revenue distribution and remain the contested empirical baseline. Howey's argument is the pro side of the $1 Kindle debate.

**Authors Guild industry reports (authorsguild.org).** The Authors Guild publishes annual income surveys (most recent 2023 income survey) and policy positions on royalty structures. The Authors Guild is the con-side voice on $1 Kindle pricing: low-price-point strategies depress the perceived value of literary work and disadvantage authors who depend on book income.

**Mike Shatzkin. *The Shatzkin Files* (idealog.com, 2008–present).** Shatzkin is the longest-running industry analyst on the trade-vs-indie publishing transition. His blog archive is the most thorough record of how trade publishing has metabolized indie pressure since 2007. The pro-$1-Kindle position is articulated here in nuanced form: pricing is contextual, low price points work for specific book types (genre fiction, narrow professional handbooks — the AI+1 series target).

### Key empirical cases

**Beatrix Potter, *The Tale of Peter Rabbit* (1901, self-published; 1902, Frederick Warne).** Potter self-published 250 copies in December 1901 after being rejected by multiple publishers. Frederick Warne picked it up only after the self-published edition demonstrated demand. The book has sold an estimated 45+ million copies. The empirical case that self-publishing-as-demonstration-of-demand has a deep history.

**Aldus Manutius and the Aldine Press (1494–1515).** Manutius invented the portable book — the *enchiridion* or "handbook" — by producing octavo editions of Greek and Latin classics small enough to carry. He also commissioned the first italic typeface (from Francesco Griffo, c. 1500). The Aldine Press is the genealogical origin of mass-market publishing: format innovation as a distribution decision. Directly relevant to the $1 Kindle case — the AI+1 series is making a format-and-price decision in the spirit of Manutius's portable-book decision.

**Hugh Howey's *Wool* (2011, self-published).** Howey released the first *Wool* novella for $0.99 in July 2011. Word-of-mouth produced a series; the series produced an agent; the agent produced a print-and-foreign-rights deal that left Howey with digital rights — an inversion of the standard trade deal. The empirical case that a $0.99–$2.99 price point can launch a viable indie career.

**Andy Weir, *The Martian* (2011, self-published; 2014, Crown).** Released chapter-by-chapter on Weir's website, then $0.99 Kindle, then traditional, then film. Demonstrates the *layered release* indie strategy.

---

## 2. The Core Concept — State of the Field

### What is settled

- EPUB 3.3 is the current standard; reflowable EPUB is dominant for narrative content, fixed-layout EPUB for highly designed content.
- Pandoc is the de facto Markdown-to-everything toolchain.
- KDP is the dominant indie distribution platform by volume (estimated >80% of indie ebook units in the US, 2025).
- Indie publishing produces a non-trivial share of total ebook revenue and a majority share of unit sales in several genre categories.
- Fact-checking is more cost-effective than post-publication correction.
- Semantic versioning is the standard for software, and applies cleanly to documentation, courseware, and book series.
- Books should be read on the target device before submission. E-ink rendering reveals problems that desktop preview does not.

### What is disputed

- Whether KDP Select (90-day exclusivity to Amazon in exchange for higher royalty access and Kindle Unlimited inclusion) is worth the exclusivity for a given book. Strongly contested. Position depends on whether the author has an existing mailing list, whether the book has cross-platform demand, and whether the author plans to use Kindle Unlimited reads as a discovery mechanism.
- Whether $0.99–$2.99 pricing is a legitimate trade-publishing format or a category-degrading practice. The AI+1 book takes the pro position; Authors Guild takes the con position.
- Whether AI-generated text in a book must be disclosed at publication. KDP requires disclosure of AI-generated content as of 2023; the boundary between "AI-assisted" and "AI-generated" is unsettled and the operational impact is unclear.
- Whether print-on-demand paperback through KDP is a necessary companion to ebook release or an optional add-on.

### What has changed recently (last 5 years)

- KDP added AI-content disclosure requirements (2023).
- EPUB 3.3 (2023) raised accessibility expectations.
- Print-on-demand quality at KDP's Kindle Direct Publishing print arm has improved enough that the format is no longer a quality compromise.
- Amazon's Kindle device line has converged on color (Kindle Colorsoft, 2024) — adds color rendering as a relevant production consideration.
- AI-generated covers — used widely, contested for IP reasons, partially restricted by KDP policy.
- The fact-checking literature has expanded to address AI-hallucinated assertions specifically (Sara Harrison Smith's framework needs an addendum the field has not yet produced canonically).

---

## 3. Application Domain Examples (graphic design)

1. **The designer's portfolio-as-PDF problem.** Most designers maintain a portfolio PDF. The discipline transfer to a Kindle-ready book is uneven: portfolio PDFs are fixed-layout, designer-controlled, color-managed. EPUB reflows. Chapter 11 must surface this — the designer-reader's instinct will be to fight EPUB reflow rather than design for it.

2. **Cover design as the meta-skill the designer reader already has.** The KDP cover requirements (1600x2560 px minimum, JPEG, RGB) are a comfortable brief for a graphic designer. The chapter can lean into this: a designer can produce a better cover than 90% of indie authors. The advantage is real.

3. **The "design portfolio" book as adjacent category.** Many designers will be releasing what is essentially a teaching companion to a portfolio. The format conventions there (heavy figures, designed page layouts, distinctive type) make fixed-layout EPUB tempting — but Chapter 11 must hold the line: reflowable for the AI+1 series, designed companion PDF as the heavy-design artifact.

4. **Metadata as designer-disliked work.** Designers tend to resist metadata work (keywords, BISAC categories, A+ content). Chapter 11 must teach this as the *positioning* layer — the same conceptual move a designer applies to brand positioning, applied to the book's discoverability.

5. **The "AI for designers" $0.99 price test.** The running example will go live at the price point the book argues for. The chapter has the opportunity to model the live A/B — sales data after 30 days, 60 days, 90 days at $0.99 vs. a $2.99 lift. Empirical sourcing for the next edition.

---

## 4. The Book's Thesis Connection

This is the chapter where the thesis becomes a *shipped artifact*. The TIKTOC.md session's high leverage and the human rewrite's gating role both terminate in a real KDP submission with real metadata, a real cover, and a real $0.99 price point that the reader has now committed to defending.

The rebuild loop is the structural counter-claim to traditional publishing's "ship and forget" model. A traditional book is fixed at print. An AI+1 book is *versioned* — semver applies. New chapters can ship as 1.1.0. Errata can ship as 1.0.1. The book ages well because its production discipline anticipates aging.

The fact-checking step is the *fluency-trap final defense*. Chapter 1 introduces the fluency trap. Chapter 8 introduces the Combined Test. Chapter 10 introduces the AI+1 standard for exercises. Chapter 11 closes with the fact-checking pass — the last place where a confidently-asserted-but-wrong claim can be intercepted before it ships. The pipeline's three judgment layers — TIKTOC.md (Ch 4), human rewrite (Ch 8), final check (Ch 11) — together comprise the human-judgment infrastructure the thesis depends on.

The $1 Kindle thesis is contested in publishing (named explicitly in Hard Topics). Chapter 11 must make the *pedagogical* case: this price point makes the book accessible to a student or a workshop participant who can sample, decide, and commit at low risk. The book's audience (working freelancers, workshop fellows, peer instructors) is precisely the audience for whom a $20 textbook is friction and a $1 textbook is a one-click decision. The price is part of the pedagogy, not separate from it.

---

## 5. The AI Wayback Machine — Candidate Figures

**Candidate 1: Aldus Manutius (Wikipedia: "Aldus Manutius")** — STRONG. Substantial Wikipedia entry. Substantive connection: invented the portable book (octavo *enchiridion*) — the most direct historical analog of the $1 Kindle as a format-and-price decision rather than a quality compromise. Italic typeface commission, semicolon usage, Aldine anchor-and-dolphin device. Satisfies criteria: undergrad-accessible (named in any history-of-printing course), lesser-known (most readers know Gutenberg, not Manutius), pre-modern non-Anglo figure (Venetian). Example prompt: *"Visit the Wikipedia page for Aldus Manutius. Read about the octavo *enchiridion* and the Aldine Press's design choices. In 250 words, argue that Manutius's portable-book decision is the historical precedent for the $1 Kindle decision. What does each format decision say about who the book is for?"*

**Candidate 2: Beatrix Potter (Wikipedia: "Beatrix Potter")** — STRONG. Substantial Wikipedia entry. Substantive connection: self-published *Peter Rabbit* in 1901 after multiple traditional rejections, then leveraged the demonstrated-demand into a trade deal. The deep historical precedent for indie-as-demonstration-of-demand. Satisfies criteria: woman (diversity), undergrad-accessible (universally known by name and book), lesser-known *as a self-publisher* (most readers know her as an illustrator only). Example prompt: *"Visit the Wikipedia page for Beatrix Potter. Read about her first self-publication of *The Tale of Peter Rabbit*. In 200 words, identify three operational decisions Potter made in 1901 that an indie AI+1 author would recognize in 2026. What changed? What hasn't?"*

**Candidate 3: Joanna Penn (Wikipedia: "Joanna Penn")** — Wikipedia page exists (note: also published as J.F. Penn for fiction). Substantive connection: the practitioner who turned indie publishing into a documented profession via *The Creative Penn* podcast (2009–present) and a long catalog of how-to books. Modern, working, mid-career — the AI+1 reader can see themselves in the lineage. Satisfies criteria: woman, undergrad-accessible, lesser-known outside indie-publishing circles. Example prompt: *"Visit the Wikipedia page for Joanna Penn. Read about her publishing model — multiple streams, platform-agnostic distribution. In 200 words, sketch your own version of Penn's model: what are the two or three revenue streams your AI+1 textbook could anchor over the next three years?"*

**Recommendation:** Lead with Aldus Manutius — strongest connection to the chapter's contested $1 Kindle thesis, plus the visual and historical anchor of the Aldine Press is genuinely interesting. Potter is the alternate with the strongest narrative arc (rejection → self-publish → demand → deal). Penn as the contemporary practitioner anchor.

---

## 6. Pedagogical Delivery Research

Chapter 11 is short (TIKTOC.md says "short but not skippable") and has *four* assessable exercises rather than the standard three — reflecting that the chapter is execution-dense and check-dense. The exercise structure (Apply, Apply, Apply, Evaluate) is correct for an Act-Three closing chapter: do the work, do the work, do the work, assess the whole book.

**Worked-example design.** TIKTOC.md specifies "Complete KDP submission for ai-for-designers — dashboard, metadata, cover, pricing, KDP Select selected. EPUB validation report clean." Production constraint: this must be a real submission, not a screenshot mockup. Sourcing requirement from Part 10 of TIKTOC.md ("every artifact shown in the worked examples must be produced from a real run").

**Aging risk concentration.** This chapter has the highest aging risk in the book. KDP submission interface (HIGH risk per TIKTOC.md), pricing rules, AI-content disclosure policy, KDP Select terms — all are interface-layer content that will drift. Mitigation strategy: separate the *stable framework* (assertion taxonomy, the rebuild loop, semantic versioning, the four-checks sequence) from the *current-state* details (the specific KDP form fields). Current-state content goes in a clearly-marked sidebar; framework content is the chapter's load-bearing prose.

**Opening case design.** TIKTOC.md specifies "A Kindle rejection email — metadata missing, cover image wrong resolution, EPUB validation error." This is *problem-before-solution* in textbook craft. The reader meets the chapter's value proposition before its content. Production constraint: this rejection email should be either real (with permission) or a faithful reconstruction labeled as such.

**Closing-paragraph weight.** TIKTOC.md's specified closing — "The pipeline is waiting" — is doing work that is unusual for a textbook closing. It is *not* a summary. It is an open-ended invitation to recursion: the rebuild loop never closes; every course run feeds the next version. This is the architectural argument for treating books as software. The closing prose must earn this gesture by tying it to a concrete next step the reader can take Monday.

---

## 7. Representation and Display Research

**EPUB display realities.** The EPUB will be rendered by an unknown Reading System. Author has no guarantee that custom CSS will be honored. Author has guarantees that:
- Semantic HTML5 (h1, h2, figure, blockquote) will be honored.
- Embedded fonts may or may not be used (Kindle apps tend to honor; some smaller readers do not).
- Images will reflow at the Reading System's discretion.
- Tables wider than ~6 viewport-widths break on phones. Convert wide tables to lists or split.
- Footnotes should be EPUB popup footnotes (`<aside epub:type="footnote">`), not parenthetical inline.

**Cover image realities.** KDP requirements (verified against the official KDP help page on May 28, 2026, subject to drift): ideal dimensions 2560px high by 1600px wide; minimum dimensions 1000px high by 625px wide; JPG/JPEG or TIFF; RGB color space; file under 50MB; ideal height/width ratio at least 1.6:1. Covers that deviate can render poorly in thumbnail grids or on device.

**Metadata realities.** BISAC categories (subject codes) and KDP categories overlap but are not identical. Keyword optimization is its own micro-discipline (Kindlepreneur and Publisher Rocket are the practitioner references). The seven-keyword slots KDP allows are *positioning real estate*. Chapter 11 must treat them as such.

**Print-on-demand display.** Margins for KDP print are stricter than they feel: inner margin 0.75", outer margin 0.5" at book trim sizes around 6"x9". A designer's instinct to push to the gutter will produce a unreadable binding.

**Accessibility display.** EPUB Accessibility 1.1 conformance is now a meaningful certification (audited by Benetech and others). For a textbook claiming to be accessible to a broad audience, conformance is worth pursuing.

---

## 8. Open Questions and Research Gaps

- **Real KDP submission for ai-for-designers running example required.** This is Open Question 5 in TIKTOC.md (KDP Select screenshot currency). The chapter cannot be drafted with the level of authenticity TIKTOC.md demands until the live submission is done.
- **AI-content disclosure handling.** KDP's policy requires disclosure of "AI-generated content." The AI+1 series uses Cowork for drafting, then human rewrite. Where does this sit on the disclosure spectrum? Probably "AI-assisted" rather than "AI-generated," but the chapter needs to state the position and the reasoning explicitly.
- **The rebuild loop and Amazon's update behavior.** Kindle readers can receive updates to books they have already purchased, but Amazon's auto-update logic is undocumented in detail. Chapter must guide the author through requesting an update push, accepting that not all readers will receive the updated version, and treating major revisions as new editions (semver MAJOR increment).
- **Pandoc EPUB validation gaps.** Pandoc produces EPUB 3 output that is mostly valid but occasionally fails strict EPUBCheck. Sidebar required on running `epubcheck` against the output and the most common fixes (missing language metadata, image alt text, navigation document structure).
- **The price-point empirical case for AI+1.** Sourcing for $0.99–$2.99 is largely genre-fiction. The professional-handbook empirical case is weaker. Chapter must acknowledge this — the AI+1 series is making a *defensible bet* rather than citing settled data.
- **Format ladder for the AI+1 reader.** Should the same content ship as $1 Kindle + free paperback + paid course? The book's position is unclear. Author decision before final draft.

---

## 9. Sourcing Notes

- Gaughran: *Let's Get Digital* 4th ed. (2021), Arriba Arriba Books. Available on Kindle.
- Penn: *How to Make a Living with Your Writing* 3rd ed. (2021), Curl Up Press; *The Creative Penn* podcast at thecreativepenn.com; Wikipedia "Joanna Penn."
- W3C EPUB 3.3 Recommendation: w3.org/TR/epub-33/ (2023).
- MacFarlane / Pandoc: pandoc.org; manual at pandoc.org/MANUAL.html.
- Smith *Fact Checker's Bible*: Anchor (2004).
- Canby: "Fact-Checking at *The New Yorker*," *The New Yorker* archive (2013); Columbia Journalism Review profile (2015).
- Preston-Werner / Semantic Versioning: semver.org 2.0.0 (2013).
- Howey: authorearnings.com archive (2014–2017), *Wayfinder* (2024); his blog at hughhowey.com.
- Authors Guild: authorsguild.org, 2023 income survey.
- Shatzkin: idealog.com archive.
- Manutius: Wikipedia "Aldus Manutius"; supplemental — *The Aldine Press* (UCLA, 2001) catalog.
- Potter: Wikipedia "Beatrix Potter"; supplemental — *Beatrix Potter: A Life in Nature* by Linda Lear (2007).
- EPUB Accessibility: w3.org/TR/epub-a11y-11/.
- BISAC categories: bisg.org/page/BISACSubjectCodes.
- Kindlepreneur: kindlepreneur.com (Dave Chesson, practitioner reference for KDP keywords).

**Flag — interface drift:** All KDP-interface-specific content is current-state-only. Re-check KDP cover, EPUB upload, AI-content disclosure, KDP Select, and dashboard screenshots immediately before publication. Pandoc, EPUB 3.3 spec, BISAC are more stable. Build script details from the AI+1 toolchain are internal — teach the function, not the implementation.

**Flag — contested claim:** The $1 Kindle as legitimate publishing format is in Hard Topics. Chapter must hold the position with evidence (Manutius, Potter, Howey, Penn) while acknowledging the Authors Guild and trade-publishing counter-case.
