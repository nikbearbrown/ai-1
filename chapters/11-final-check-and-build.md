# Chapter 11 — Final Check and Build: EPUB + PDF
*Where the book ships — and discovers what the pipeline could not check on your behalf.*

**Capability:** Students run the final check sequence, build the EPUB and PDF, and submit to Kindle Direct Publishing — understanding the rebuild loop as normal finishing process.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Run the Fact-Checking Assistant across your book, triage its output in the order OUTDATED → CONTRADICTED → UNVERIFIED, and resolve at least one OUTDATED or CONTRADICTED finding before building.
2. **(Apply)** Run `./build.sh`, produce a valid EPUB and PDF from `combined.md`, open the EPUB on a real Kindle device or the Kindle app, and identify three things to fix on the device read.
3. **(Apply)** Submit the book to Kindle Direct Publishing — title and metadata, cover image, manuscript upload, pricing, KDP Select decision — and produce a clean EPUB validation result.
4. **(Evaluate)** Assess the finished book against the AI+1 standard: domain-specific exercises, professional identity preserved, no fluency trap surviving in the pedagogy.
5. **(Analyze)** Treat the rebuild loop as a versioned-software workflow — semantic-versioning revisions, errata pushes, edition increments — rather than a one-shot publish event.

---

## A rejection email

This is the opening of an email a designer-author received from KDP in April 2026:

> Dear [name],
> Thank you for your submission. Your title, *AI for Designers: A Practitioner's Guide*, has been temporarily blocked from publishing for the following reasons:
> – Required metadata fields are incomplete. (Keywords: only 3 of 7 slots used. BISAC category: missing.)
> – Cover image does not meet specifications. Submitted file is 1200 × 1920 pixels; minimum height is 2560 pixels.
> – EPUB validation failed. Errors: 4 critical, 12 warnings. (Missing language metadata in OPF. Three images missing alt text. Navigation document structure violates EPUB 3.3 spec.)
> Please address the items above and resubmit. Submissions block additional review until corrected.

The author did not write a bad book. The author wrote a book and skipped the final check sequence. Each of the three blockers takes a few minutes to fix and zero minutes to *prevent*. This chapter is the prevention sequence.

There are four things to do, in order:

1. Run the Fact-Checking Assistant. Triage. Resolve at minimum the contradicted claims.
2. Run `./build.sh`. Produce the EPUB and the PDF.
3. Read the EPUB on a device. Not on a desktop. On an actual Kindle, or in the Kindle app on your phone.
4. Submit to KDP. Metadata, cover, pricing, KDP Select decision.

Then accept that you will rebuild. You will rebuild because the device read produced three issues you could not have seen on the desktop. You will rebuild because the fact-checker caught something on its second pass. You will rebuild because the cover thumbnail looks wrong at 200 pixels even though it looked fine at 2560. The rebuild loop is not a failure of the pipeline. It is the pipeline.

---

## Block one — Fact-Checking Assistant

The Fact-Checking Assistant scans every chapter file and classifies every assertion in two dimensions: assertion *type* and content *category*.

### Assertion types

Five types, drawn from Sarah Harrison Smith's *The Fact Checker's Bible* (2004, Anchor) — the procedure Smith built as head of research at the *New York Times Magazine*:

- **Basic** — a plain factual claim. *"Pandoc converts Markdown to EPUB."* Rarely fails.
- **Emphatic** — a basic claim with a strength qualifier. *"Pandoc is the de facto Markdown-to-EPUB toolchain."* The emphasis is what needs verifying.
- **Positive** — an affirmative claim against an implied alternative. *"Pandoc beats Calibre for reproducible builds."* The comparison is the assertable thing.
- **I-Language** — first-person assertions. Hard to verify externally; usually flagged for caveat language.
- **Combination** — a sentence carrying two or more assertions. The checker decomposes them before verifying.

### Content categories

Six categories, drawn from professional fact-checking (Peter Canby's *New Yorker* department, profiled in *Columbia Journalism Review* 2015, is the gold standard):

- **STAT** — statistical claims. Verify against the primary source, not a derivative summary.
- **GUIDELINE** — best-practice claims attributed to a standards body. Verify against its current published guidance.
- **APPROVAL** — a claim about authority approval. Verify against the authority's published policy as of a named date.
- **EVIDENCE** — claims that evidence supports a conclusion. Verify against the cited study; check strength.
- **SPECIALIST** — claims attributed to a named expert. Verify against the expert's published work.
- **CURRENT** — claims true *now*. The most aging-prone. Flag the verification date.

### The triage order

The Fact-Checking Assistant flags every assertion as one of four statuses: VERIFIED, OUTDATED, CONTRADICTED, or UNVERIFIED. You triage in this order:

1. **OUTDATED first.** A claim that was true at writing time but is no longer true. *"KDP requires a 1600x2400 minimum cover" → as of 2026 the minimum is higher.* These are the fastest to fix — replace the number, re-verify, move on. They are also the most embarrassing if they ship.

2. **CONTRADICTED second.** A claim where the cited or implied source actually says something different from what the chapter claims. *"Pandoc supports EPUB 3.3 natively" → Pandoc supports much of EPUB 3.3; some features require post-processing.* These take longer because they require rewriting. They are the most important to catch — a contradicted claim is the kind that gets quoted back at you in a one-star review.

3. **UNVERIFIED third.** A claim the checker could not verify in either direction. *"About 80% of indie ebook units in the US are sold through KDP" → no single authoritative source confirms this number.* These have two resolutions: find a source and upgrade to VERIFIED, or rewrite to make the uncertainty visible. *"Probably the largest share of indie ebook units in the US, though no single authoritative source confirms a precise figure"* is honest in a way the original was not.

The pipeline does not require you to resolve every UNVERIFIED claim. It requires you to make a *deliberate decision* on each one — keep with caveat language, find a source, or remove the claim. The Fact-Checking Assistant writes its output to `factchecks/MASTER_REPORT.md` and inserts inline `<!-- FACT-CHECK FLAG -->` comments at every claim that did not return VERIFIED. The flags travel with the chapter file until you resolve them.

### Smith's procedure adapted for AI-assisted drafting

Two disciplines from *The Fact Checker's Bible*, sharpened by AI-drafted realities:

- **The author and the fact-checker are separate roles, even when the same person.** When you wear the fact-checker hat, you read as a stranger looking for what could be wrong. The hat-switching is the discipline.
- **Read aloud against the source.** Smith's *New Yorker* procedure catches paraphrase drift — assertions that *summarize* the source in a direction the source does not actually go. AI-drafted text drifts this way often.

The fact-check is the *fluency-trap final defense*. Chapter 1 introduced the fluency trap. Chapter 8 introduced the Combined Test. Chapter 10 introduced the AI+1 standard for exercises. Chapter 11 closes with the fact-check.

---

## Block two — `./build.sh` and the pandoc pipeline

The build script runs the toolchain that produces the EPUB and the PDF. It is one command. You will run it many times before the book is finished.

### What `./build.sh` actually does

The script, in plain language:

1. Reads every chapter file from `chapters/` in numerical order. Reads the front matter and the back matter.
2. Concatenates them into a single file at `output/combined.md`. This is the canonical source the pandoc command reads from. You do not edit `combined.md` directly. You edit chapter files and rebuild.
3. Runs `pandoc` with flags that produce a valid EPUB 3 and a PDF. The relevant flags include `--epub-cover-image`, `--toc`, `--toc-depth=2`, `--metadata-file=metadata.yaml`, and a few output-format-specific tweaks.
4. Writes `output/[book-slug].epub` and `output/[book-slug].pdf`.
5. Logs the build to `logs/build.log` with timestamps and file sizes.

The `output/` directory is gitignored. The build artifacts are not the source of truth. The source of truth is the chapter files plus `metadata.yaml` plus the images.

### Pandoc — the toolchain spine

Pandoc, written and maintained by John MacFarlane, is the de facto Markdown-to-everything converter. The User's Guide (pandoc.org/MANUAL.html) is the reference. Two things to know:

- **Pandoc reads pandoc-flavored Markdown** — slightly extended GitHub-Flavored. Footnotes, block-quotes, tables, code fences, and inline HTML (including the `<!-- FACT-CHECK FLAG -->` comments) all work.
- **Pandoc's EPUB output is mostly EPUB 3 valid.** Three things break regularly: missing `<language>` metadata (fix in `metadata.yaml`), images without alt text (fix in chapter files), and navigation-document structure for chapters with no h1. EPUBCheck (github.com/w3c/epubcheck) catches all three.

### What can go wrong, and how to diagnose

The build script fails in a handful of recognizable ways:

1. **Pandoc command not found.** Pandoc is not installed or not on PATH. Install with `brew install pandoc` (Mac), `winget install JohnMacFarlane.Pandoc` (Windows), or `sudo apt install pandoc` (Linux). [verify — package names current as of May 2026]
2. **EPUBCheck errors.** Run `epubcheck output/[book-slug].epub` to see them all. Address in order: missing metadata first, then image alt text, then navigation. The errors usually trace to two or three chapter files; fix and rebuild.
3. **PDF rendering errors.** Often a font issue — pandoc's PDF output uses LaTeX by default, which expects fonts to be present on the system. The fix is either to install the font or to pass `--pdf-engine=weasyprint` (which uses CSS-based rendering and is more permissive). [verify — pdf-engine flag values can drift]
4. **Build produces a file but the file is mostly empty.** The combined.md step concatenated nothing — usually because the chapter filenames don't sort the way the script expects. Confirm chapter files start with two-digit prefixes (`01-`, `02-`, ... `11-`) and that the script's glob pattern matches them.

The diagnosis pattern is: read the error message, find which step failed, fix the input file, rerun. Do not rebuild blindly hoping the error goes away.

---

## Block three — Reading the EPUB on a device

This step is not optional. It is the step every author resists and every author needs.

### Why desktop preview is not the same

Pandoc's EPUB looks acceptable in Apple Books on a desktop, in any code-editor preview, in any browser-based reader. None of those are what your reader will use. Your reader will use one of: Kindle Paperwhite or Basic (e-ink, 6", grayscale, slow refresh), Kindle Colorsoft (e-ink with limited color), iPad Kindle app (color, retina), iPhone Kindle app (color, narrow column), Android Kindle app (varies), or PDF on any device.

E-ink Paperwhite is the cruel test. Gradients become bands. Subtle grays become indistinguishable. Custom fonts the Reading System ignored fall back to a default weight that breaks the design. Color encoding becomes pure structural encoding — your blue-vs-red distinction becomes light-gray-vs-medium-gray, and if you relied on color to carry the difference, the chart now carries nothing.

### The three most common rendering issues

After running `./build.sh` and side-loading onto a Kindle or opening in the Kindle app, scroll through every chapter. Three things go wrong on every first-pass build:

1. **A figure is too small to read.** The PNG was generated at 300 DPI but at small physical dimensions; on a 6" e-ink device it shrinks past legibility. Fix: redraw with larger type and fewer elements, or split into two figures. Not: upscale the PNG.
2. **A table is wider than the column.** Reflowable EPUBs cannot render wide tables on narrow screens. Tables wider than ~6 viewport-widths break on phones. Fix: convert wide tables to bulleted lists or split. The W3C EPUB 3.3 spec (w3.org/TR/epub-33/, 2023) does not require horizontal scrolling for wide content.
3. **A footnote rendered inline as parenthetical text.** Inline `(see footnote 1)` clutters small screens. EPUB has popup footnotes via `<aside epub:type="footnote">` that pandoc generates from Markdown footnote syntax (`[^1]`). Convert inline parentheticals and rebuild.

You will find others specific to your book. Read every chapter on the device. Note three things to fix per chapter. Fix. Rebuild. Read again. The rebuild loop has started.

---

## Block four — KDP submission

Kindle Direct Publishing (kdp.amazon.com) is Amazon's self-publishing platform. As of May 2026 it accounts for the dominant share of indie ebook units in the US. [verify — share estimates from 2025 Authors Guild and industry analyst sources, subject to drift]

The submission flow has five parts. Each one is straightforward. The whole thing takes about forty-five minutes the first time.

> **Important [verify].** Every screenshot, every form field name, every dropdown option, every price-tier rule, and every program-eligibility requirement described in this block is *current-state as of May 2026* and is subject to the highest aging risk in this book (TIKTOC.md Part 11). The KDP dashboard interface changes meaningfully every six to twelve months. Re-check every detail against kdp.amazon.com directly before submitting. The *structural framework* of submission (account, metadata, cover, manuscript, pricing) is stable. The specific *fields* are not.

### Step 1 — Account setup

You need a KDP account (free) and a US bank account or a foreign equivalent that Amazon's payment system supports. The first time you create an account you will complete a tax interview (W-9 for US residents, W-8BEN for non-US) and a banking information form. Both take about fifteen minutes and you will not have to repeat them for future books.

### Step 2 — Title and metadata

From the KDP dashboard, *Create New Title* → *Kindle eBook*. Fill in:

- **Title and subtitle.** Subtitles count toward search relevance.
- **Series name** (optional). Links related books on the author's KDP page.
- **Author name.** Use the name you want associated in perpetuity. Pen names accepted.
- **Description.** Up to 4,000 characters. The back-cover blurb. Write it as carefully as Chapter 1.
- **Keywords.** Seven slots. Use all seven. Each can be a phrase. Dave Chesson's *Kindlepreneur* (kindlepreneur.com) is the practitioner reference. [verify — slot count and field rules subject to change]
- **Categories.** Two from KDP's hierarchy. BISAC subject codes (bisg.org) inform the taxonomy. Pick the *most specific* category that fits.
- **AI-content disclosure.** KDP requires disclosure of AI-generated content (since August 2023). AI+1 books use AI-assisted drafting (Cowork drafts, human rewrites) — *AI-assisted* rather than *AI-generated* per Amazon's distinction. [verify — disclosure boundaries unsettled and shifted multiple times since 2023]

### Step 3 — Cover image

Upload a JPEG or TIFF cover, RGB color space, ideally 2560 pixels high by 1600 pixels wide, minimum 1000 × 625. File under 50MB. Ideal ratio at least 1.6:1. [verify — cover spec is the single most aging-prone detail in this section]

The cover is the part of this submission where a designer-reader has a real advantage. The graphic designer's first instinct will be correct: design the cover at the recommended size, in a sans-serif typeface that survives thumbnail rendering, with the title legible at 200-pixel preview width. If the title is illegible at thumbnail size, the cover is wrong — Amazon's discovery surfaces show 200-pixel thumbnails primarily, and the cover that wins is the one that reads at that scale.

### Step 4 — Manuscript upload

Upload the EPUB at `output/[book-slug].epub`. KDP runs its own EPUB validation and previews the result in their Online Previewer. The Online Previewer is the *minimum* device check. Side-loading onto an actual Kindle is the real check, and you have already done it (Block three). If the Online Previewer flags issues, fix them in the chapter files and rebuild.

### Step 5 — Pricing and KDP Select

This is where the AI+1 series' contested-thesis decision lives.

**Price.** The AI+1 series ships at **$0.99**. Contested. The Authors Guild's position (authorsguild.org) is that low price points depress perceived value. Mike Shatzkin (idealog.com), in nuanced form, argues pricing is contextual and low points work for narrow professional handbooks. Hugh Howey's *Wool* (2011, $0.99) is the cited indie-success case. Joanna Penn, in *How to Make a Living with Your Writing* (3rd ed., 2021, Curl Up Press), frames pricing as one variable inside a multi-stream income model.

The AI+1 case for $0.99 is pedagogical, not commercial: the audience is freelance professionals and workshop participants who can sample, decide, and commit at low risk. A $20 textbook is friction. A $1 textbook is a one-click decision. The price is part of the pedagogy. Defensible bet, not settled strategy.

The KDP royalty structure: books between $2.99 and $9.99 earn 70%. Outside that range — including $0.99 — 35%. At $0.99 you keep about $0.35 per sale. The economic case is volume, not margin.

**KDP Select.** Enrollment grants Amazon **90-day exclusivity** — no distribution through Apple Books, Kobo, your own website. In exchange: Kindle Unlimited inclusion (Amazon pays per page read), promotional pricing windows, and (debated) higher discoverability in Amazon's recommendation systems. [verify — 90-day exclusivity term, KU page-read economics, and Countdown Deal rules are current-state and subject to drift; Amazon has modified KDP Select terms multiple times since 2014]

The decision is contested. Pro (Howey, Penn early-career advice): KU access dwarfs the cross-platform reach you would have built otherwise. Con (Penn more recent, indie-authors with mailing lists): exclusivity locks you out of platforms where your audience already exists, and KU economics favor genre-fiction series over handbooks.

For the AI+1 series the decision was **enroll in KDP Select**. Reasoning: audience is on Amazon, workshop distribution is well-served by KU, cross-platform loss is acceptable at the series' current scale. Defensible, not the only defensible position.

After all five steps, click *Publish*. The book enters review. Approval typically arrives within 24–72 hours. Then the book is live.

---

## Worked example — ai-for-designers on KDP

The complete submission for *ai-for-designers: A Practitioner's Guide* — captured from the KDP dashboard on May 14, 2026. **[verify — interface and form fields as of May 2026, subject to drift per Open Question 5 in TIKTOC.md; re-verify against the live KDP dashboard before submitting.]**

- **Title / subtitle:** *AI for Designers* / *A Practitioner's Guide*. Series: *AI+1*, volume 1. Author: Nik Bear Brown.
- **Description:** *A working handbook for freelance graphic designers integrating AI into client practice. From brief intake to portfolio positioning, this book teaches AI+1 fluency — the AI literacy that makes you more valuable to your clients, not interchangeable with the model.*
- **Keywords (all seven slots used):** AI for designers; graphic design workflow; Claude for creatives; freelance design business; AI tools for designers; Adobe Firefly Midjourney Figma; design practitioner handbook.
- **Categories:** Computers & Technology → AI & Semantics; Arts & Photography → Graphic Design → Commercial.
- **AI-content disclosure:** AI-assisted (Cowork-drafted, human-rewritten).
- **Cover image:** 2560 × 1600 pixels JPEG, RGB. Flat fills, ink + ochre on cream, title legible at 200-pixel thumbnail. **[verify — pixel specs subject to drift]**
- **Manuscript:** `output/ai-for-designers.epub`. EPUBCheck: 0 critical errors, 2 informational warnings. KDP Online Previewer rendered all 11 chapters cleanly.
- **Pricing:** $0.99 USD. Royalty tier: 35%.
- **KDP Select:** Enrolled. 90-day exclusivity from publish date. **[verify — KDP Select 90-day term subject to Amazon policy change]**
- **Status:** *In review* on submit. Approved 27 hours later, May 15, 2026. Live on Amazon.com and every regional storefront.

EPUB validation: clean. PDF rendered correctly. Cover thumbnail legible at 200 pixels.

---

## Block five — The rebuild loop

After the device read, the fact-check resolution, and the KDP submission, the book is live. The reader who picks it up tomorrow morning reads version 1.0.0.

You will rebuild. The rebuild is normal.

### Why rebuilds happen

Most common reasons: the device read after submission catches something you missed; a reader reports an error (more often right than wrong); a current-state claim has aged (KDP screenshot, Cowork prompt name, statistic); a new chapter is ready.

The mental model is *book-as-software*. Tom Preston-Werner's Semantic Versioning (semver.org, 2.0.0 in 2013): **MAJOR.MINOR.PATCH**. For a versioned book:

- **MAJOR** — substantial rewrites, restructured TOC, new chapters. 1.x → 2.0.0 = second edition.
- **MINOR** — new chapter or substantial revision. 1.0.0 → 1.1.0.
- **PATCH** — typo fixes, errata, current-state updates. 1.0.0 → 1.0.1.

KDP supports updates through the dashboard. Auto-update logic is undocumented; existing readers may or may not receive the new version. You can request a manual push for substantive updates via KDP support. Treat PATCH as routine; MINOR and MAJOR as occasions to consider whether the new content warrants a push.

### The fast rebuild cycle

1. Open the chapter file. 2. Make the change. 3. Run `./build.sh`. 4. Run `epubcheck` if the change touched structure. 5. Open on device. 6. Upload to KDP — the form recognizes the existing book and treats the new EPUB as an update. 7. Bump the version in `metadata.yaml` per semver. Commit.

About thirty minutes the first time. Fifteen after the first half-dozen.

### The AI+1 final assessment

Before each MAJOR or MINOR version push, run a four-question audit against the AI+1 standard:

1. **Domain-specificity.** Does every LLM Exercise still pass the three-question audit from Chapter 10? (Test, requires-bringing-something-only-they-have, judgment-not-generation.)
2. **Professional identity preserved.** Does the book still treat the reader as a domain expert acquiring AI fluency, not a generic-AI-user acquiring domain content? The fluency trap creeps back in over revisions.
3. **No pedagogical fluency trap.** Pick three exercises at random. If any one of them reads as "ask Claude to explain X," the trap is back. Revise.
4. **Voice intact.** Read one chapter aloud. Does it sound like you, or does it sound like a Cowork dump? Drift happens. Revise.

A book that passes all four is shippable. A book that fails one is fixable. A book that fails three is in trouble — the rewrite from Chapter 8 was not held over enough revisions.

---

## Exercises

### Exercise 11.1 — (Apply) Run the Fact-Checking Assistant and resolve one finding

Run the Fact-Checking Assistant across your book. Open `factchecks/MASTER_REPORT.md`. Triage the output in the order OUTDATED → CONTRADICTED → UNVERIFIED.

- Identify at least one OUTDATED finding. Resolve it by updating the relevant chapter file. Rerun the checker against that chapter to confirm.
- OR — if no OUTDATED findings exist — identify at least one CONTRADICTED finding and resolve it. Document the original claim, the contradicting source, and the rewrite.

Deliverable: the resolved finding, with original claim, source, and revised text shown side by side.

### Exercise 11.2 — (Apply) Build and read on a device

Run `./build.sh`. Confirm `output/[book-slug].epub` and `output/[book-slug].pdf` are produced. Open the EPUB on a Kindle device or in the Kindle app on your phone (not on a desktop). Scroll through every chapter.

- Note three specific things to fix. At minimum: one figure rendering issue, one table or list issue, and one footnote or sidebar issue.
- For each, record the chapter, the location in the chapter, and what specifically you want to change.

Deliverable: a list of three issues with chapter, location, and proposed fix.

### Exercise 11.3 — (Apply) Fix, rebuild, confirm

Apply the three fixes from Exercise 11.2 to the relevant chapter files. Run `./build.sh` again. Open the EPUB on the device again. Confirm all three issues are resolved.

Deliverable: a one-paragraph note per fix confirming resolution, plus the new build's `output/[book-slug].epub` file.

### Exercise 11.4 — (Evaluate) AI+1 final assessment

Run the four-question AI+1 final assessment against the finished book:

1. Does every LLM Exercise still pass the three-question AI+1 audit from Chapter 10? Pull three at random. Score each.
2. Is the reader still being treated as a domain expert acquiring AI fluency rather than a generic AI user acquiring domain content? Read the introduction and one mid-book chapter and answer.
3. Pick three exercises at random. Are any of them in the form "ask Claude to explain X"? If so, the pedagogical fluency trap is back.
4. Read one chapter aloud. Does it sound like you? Or does it sound like a Cowork dump?

Deliverable: a one-paragraph assessment per question, with concrete evidence from the manuscript. Identify the strongest passing dimension and the weakest one. State whether the book is shippable, fixable, or in trouble.

---

## AI Wayback Machine — Aldus Manutius

Aldus Manutius was a printer working in Venice between 1494 and 1515. Most readers who know the history of printing know Gutenberg. Fewer know Manutius — and what Manutius did is the more direct precedent for the AI+1 series' $1 Kindle decision.

Gutenberg invented the movable-type press. Manutius invented the *portable book*. He produced octavo editions — small enough to carry in one hand — of Greek and Latin classics that previously existed only as heavy folios for institutional libraries. He called the format the *enchiridion* — "handbook." He commissioned the first italic typeface (Francesco Griffo, c. 1500) to fit more text on a smaller page without sacrificing legibility. He standardized punctuation, including a recognizable semicolon.

What Manutius understood, that the AI+1 series tries to inherit: the *format* of a book is a *decision about who the book is for*. A heavy folio is for an institution. A portable octavo is for a reader who wants the text close at hand, on the road, between meetings. The format is the access strategy. The price follows the access strategy. The $1 Kindle is the same move at a different turn of the wheel.

**Try this prompt:** *Visit the Wikipedia page for Aldus Manutius. Read about the octavo enchiridion format and the Aldine Press's design choices. In 250 words, argue that Manutius's portable-book decision is the historical precedent for the $1 Kindle decision. What does each format decision say about who the book is for?*

Sharper: ask Claude to identify *three* specific Manutius decisions and pair each with an analogous AI+1 decision. Then verify Claude's claims against the Wikipedia sources — the Aldine Press catalog at UCLA is one canonical secondary source.

---

## Closing — the pipeline is waiting

The book is live on KDP. The reader who just finished this chapter is an author-instructor with a Kindle-ready AI+1 textbook in their hands. The TIKTOC.md session that started everything was two hours, three months ago. The Cowork draft was rewritten chapter by chapter. The figures encode arguments. The LLM Exercises pass the AI+1 standard. The fact-check ran. The build ran. The submission cleared.

The book sits on Amazon. Someone, somewhere, is about to download it.

And the rebuild loop is already starting. You will read your own book on a Kindle next week and find three things you missed. A reader will email about a fourth. A new client engagement will give you a worked example you wish you had included. KDP will change a form field — the cover spec, the disclosure policy, a new keyword slot — and you will rebuild to keep current.

This is not failure. This is the pipeline at work. A book is not finished the way a building is finished. It is finished the way software is finished — versioned, patched, occasionally re-edited.

Every course run produces new cases. Every workshop produces new failure modes. Every new model release produces new AI capabilities to integrate. The TIKTOC.md is still on disk. The chapters/ directory still exists. The build script still runs.

Monday morning, you will look at the next book you want to build. You will open Tic TOC. You will run /i1. The next pipeline is ready when you are.

---

## Still puzzling

Open questions this chapter does not close:

1. **The KDP interface will change.** Open Question 5 in TIKTOC.md flagged this. Every screenshot in Block four was current as of May 2026 and is subject to drift. The honest framing: the *structure* of submission (account, metadata, cover, manuscript, pricing) is stable; the *fields* are not. Re-verify against the live dashboard before submitting.
2. **The AI-content disclosure boundary is unsettled.** KDP's distinction between "AI-assisted" and "AI-generated" is operationally fuzzy in 2026. The AI+1 series treats Cowork-drafted-then-human-rewritten as AI-assisted. A future tightening of the policy could reclassify; the chapter would need an update.
3. **The $1 Kindle case is empirically thin for professional handbooks.** Most cited successes (Howey's *Wool*, Andy Weir's *The Martian*) are genre fiction. The professional-handbook case is a defensible bet, not a settled finding. Five years of AI+1 sales data would settle it.
4. **Kindle Unlimited page-read economics may shift.** Amazon has adjusted KU pages-read payouts multiple times since 2014. The KDP Select recommendation in this chapter assumes 2026-era economics. A material shift in the per-page rate would change the recommendation.
5. **The rebuild loop assumes Amazon supports book updates indefinitely.** This is true now. It might not be true in five years. A loss of update-push capability would shift the AI+1 series toward MAJOR edition increments rather than PATCH updates.

## What would change my mind

The strongest counter-argument to the entire AI+1 production pipeline this book has taught is that *the pipeline is too disciplined for what most author-instructors will actually do*. A handbook reader who skips the human rewrite, skips the device read, skips the fact-checking pass, and ships a Cowork dump may still produce a book that sells acceptably at $1 because the floor for $1 nonfiction is low. If a body of evidence emerged — five years of AI+1-series sales data and reader-review data — showing that books built through the full pipeline did not measurably outperform books built by skipping the human-judgment steps, the thesis of this book would have to update. The bet I am making, in writing this, is that they will outperform — that the TIKTOC.md session and the human rewrite are the high-leverage steps and the device read is the gate, and that books missing those steps will accumulate one-star reviews faster than they accumulate readers. I do not have the five-year data. I have the argument and a working pipeline. The next five years are the test.
