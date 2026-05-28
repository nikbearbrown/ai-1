# Research: Chapter 09 — Finishing Pass and Figures
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students run the finishing pipeline — subtitle pass, CAJAL figure intelligence, SVG generation, enrichment — and evaluate output against the AI+1 visual standard.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

**Edward Tufte. *The Visual Display of Quantitative Information* (1983; 2nd ed. 2001).** Graphics Press. The book that turned chart-making into a discipline with rules. Tufte's central propositions for textbook figures: maximize the *data-ink ratio* (the proportion of a figure's ink devoted to non-redundant data information), eliminate "chartjunk" (decoration that does not encode data), and ensure graphical integrity (the visual representation of numbers must be proportional to the numbers themselves — the "lie factor" must approach 1.0). For Chapter 9, this is the canonical answer to "does this figure earn its place?"

**Edward Tufte. *Envisioning Information* (1990).** Graphics Press. Introduces the "small multiples" principle — variation in one parameter shown across a grid of identical-format panels — which is the strongest argument for the *consistent figure grammar* CAJAL is designed to enforce.

**Jacques Bertin. *Sémiologie graphique* (1967, English trans. *Semiology of Graphics* 1983).** The pre-Tufte foundational text. Introduces the "visual variables" (position, size, shape, value, color, orientation, texture) — the alphabet from which every static chart is built. Bertin's framework is what Tamara Munzner later formalizes for the SVG-and-D3 era.

**Tamara Munzner. *Visualization Analysis and Design* (2014).** CRC Press. The modern academic counterpart to Tufte for *interactive* and *encoded* visualizations. Munzner's "what-why-how" framework (what data, why is the user looking at it, how is it visually encoded) is the cleanest decision procedure for picking a chart type — directly relevant to CAJAL's MC/VG/PQ taxonomy.

**Cole Nussbaumer Knaflic. *Storytelling with Data* (2015).** Wiley. The practitioner bridge between Tufte and business audiences. Knaflic's "lessons" — declutter, focus attention, think like a designer — translate Tufte's data-ink ratio into operational moves a non-designer can apply: removing gridlines, demoting axis labels to gray, using bold color sparingly as a focal cue.

**Alberto Cairo. *The Truthful Art* (2016).** New Riders. Five qualities of a good visualization: truthful, functional, beautiful, insightful, enlightening. Cairo's "functional" criterion is what Chapter 9's "subtitle vs. topic heading" distinction is enforcing.

**Robin Williams. *The Non-Designer's Design Book* (1994; 4th ed. 2014).** Peachpit Press. CRAP — Contrast, Repetition, Alignment, Proximity. The accessible four-principle ruleset for a designer-author who already knows visual hierarchy but hasn't formalized it. Williams is the only book on this list a graphic-designer reader will already own.

**Robert Bringhurst. *The Elements of Typographic Style* (1992; 4th ed. 2013).** Hartley & Marks. The canonical typography reference. Relevant chapters for the AI+1 finishing pass: rhythm and proportion (Ch 2), choosing and combining type (Ch 6), the page (Ch 8). Bringhurst is *opinionated* about defaults — measure (line length) of 45–75 characters, generous leading, hung punctuation. These are the defaults the AI+1 build script must encode.

**Josef Müller-Brockmann. *Grid Systems in Graphic Design* (1981).** Niggli. The canonical Swiss/International Typographic Style text — the source of the modular grid, the use of sans-serif typefaces, the rejection of decoration. The "no rounded corners, no gradients" aesthetic the AI+1 series uses traces directly to this lineage.

### Key empirical cases

**Florence Nightingale's "Rose Diagram" (1858).** Nightingale's *Diagram of the Causes of Mortality in the Army in the East* — the polar-area chart she designed to show that preventable disease killed more British soldiers in the Crimean War than battle wounds — is the load-bearing empirical case for figure-as-argument. She designed it specifically for non-statistician readers (Parliament, Queen Victoria), and it worked: sanitary reform of military hospitals followed. The figure earned its place by changing policy.

**The Challenger O-ring chart (1986).** Tufte's recurring case study — the night before the launch, Morton Thiokol engineers showed NASA managers a chart of O-ring damage versus launch temperature that was *technically correct but visually inadequate*. The signal was buried in the noise. Tufte's reconstruction shows the same data plotted to surface the temperature dependence. Used in Chapter 9 as the negative case: a figure that fails its argument is worse than no figure.

**Mike Bostock's D3.js gallery (d3js.org).** The empirical case for what SVG-first, programmatically generated figures look like at the high end. Bostock's *Observable* notebooks are the model for D3 HTML files in `d3/`.

**Mona Chalabi's hand-drawn data illustrations (Guardian US, Instagram).** A live counter-example: data journalism where the visual language is deliberately *not* Tufte-clean. Chalabi's loose, sketched style argues that visual personality is itself a data-integrity move — it signals provenance and a single author's accountability. Useful as the contested case in Chapter 9.

---

## 2. The Core Concept — State of the Field

### What is settled

- A figure must earn its place by encoding information the text cannot convey as efficiently (Tufte, Bertin, Munzner — agreed across forty years).
- The data-ink ratio is a useful diagnostic, not a hard rule. The principle survives; the precise threshold does not.
- Small multiples beat dual-axis charts almost always.
- Sans-serif body type is acceptable on screen at 12pt+; serif is still preferred for long-form print at 10–11pt (settled in print design, contested on e-ink).
- Color should encode data, not decorate. Categorical palettes should be perceptually uniform (ColorBrewer is the default reference).
- Charts must declare their units, their source, and their date.

### What is disputed

- Whether interactive figures belong in books at all, or only in companion web artifacts. Tufte's position (interaction is mostly a substitute for thinking) is the minority view among working data journalists in 2026.
- The "chartjunk" critique versus the "engagement" critique (Bateman et al, "Useful Junk?" 2010 — found embellished charts were *better* remembered than minimalist ones). Settled enough that minimalism is the default but not the only defensible choice.
- Whether AI-generated figures (SVG-from-prompt) can be trusted without manual audit. State of the field in 2026: no, not yet — they hallucinate axis labels and miscount bars at non-trivial rates.

### What has changed recently (last 5 years)

- SVG-first workflows have displaced raster for almost all instructional figures. PNG export is a build artifact, not a source.
- D3 v7 (2021) and Observable Plot (2022) have made declarative chart generation accessible to non-programmers — the API surface is small enough that an author-instructor can read it.
- Vega-Lite (Wongsuphasawat, Moritz, Anand, Mackinlay, Howe, Heer — *IEEE TVCG* 2017) has become the de facto JSON grammar for charts that need to be generated by tools rather than humans. Directly relevant to CAJAL output.
- LLM-driven figure generation (2023–2025) has gone from novelty to working pipeline component, but only for *templated* charts where the visual grammar is fixed and only the data varies. Original infographic design remains human work.
- Accessibility — alt text, color-blind-safe palettes, screen-reader-readable SVG — has become a publishing requirement, not a niceties.

---

## 3. Application Domain Examples (graphic design)

1. **The Pentagram annual report grid.** Pentagram's annual reports for clients (Mastercard, Rolls-Royce) demonstrate the modular-grid discipline at production scale. Useful in Chapter 9 as the "what good looks like" reference for a designer reader.

2. **The Massimo Vignelli NYC Subway map (1972).** The most famous diagrammatic-vs-geographic argument in graphic design. Vignelli's diagrammatic map prioritized topological accuracy (connection structure) over geographic accuracy (true distances). Replaced in 1979, partially restored in 2008. The lesson Chapter 9 borrows: a figure makes an argument by what it *omits*.

3. **Information Is Beautiful (David McCandless).** The trade-press counter-example to Tufte. McCandless's charts privilege engagement over data density. For a designer-reader, this is the gravitational pull Chapter 9 must counteract: the temptation to make figures *look like McCandless* when the textbook needs them to *function like Tufte*.

4. **Stefan Sagmeister + Jessica Walsh, *Beauty* (2018).** The argument that visual beauty is itself a data point in design discourse. Useful as the "but designers will object to brutalist defaults" steelman.

5. **Mona Chalabi's COVID dashboards (Guardian, 2020–2021).** A working case where a designer-illustrator produced repeatable, weekly data graphics under deadline using a defined visual grammar — exactly the workflow a single-author AI+1 textbook author needs to model.

---

## 4. The Book's Thesis Connection

The AI+1 thesis is that the TIKTOC.md session is the highest-leverage step and that the human rewrite is the gate. Chapter 9 is where the thesis gets tested at the *visual* layer rather than the textual layer. The same fluency-trap risk applies: CAJAL can generate a plausible-looking SVG that encodes the wrong argument — axes wrong, the wrong variable on color, a "small multiples" grid where only one panel actually varies. The chapter's job is to teach the reader to *audit* the visual layer with the same scrutiny they brought to Chapter 8's prose rewrite.

This is also the first chapter of Act Three — the pipeline has stopped running automatically. The author is in charge. A bad figure that ships is the author's bad figure. The "no rounded corners, no gradients" house style is the visual analogue of the Combined Test from Chapter 8: a stripped-down spec that makes the *content* of the figure (the data, the argument) bear the load rather than the chrome.

The Tufte connection to thesis: a figure that fails the data-ink ratio is a *visual fluency trap*. It looks like a chart, but it does not encode an argument. The reader who learned to catch the verbal fluency trap in Chapter 1 has to learn the visual version here.

---

## 5. The AI Wayback Machine — Candidate Figures

**Candidate 1: Florence Nightingale (Wikipedia: "Florence Nightingale")** — STRONGLY PREFERRED. Wikipedia page exists and is substantial. Substantive connection: she invented (or at least popularized to the point of credit) the polar-area chart specifically to *change a policy decision* by making mortality data legible to non-statistician policymakers. Satisfies criteria: woman (diversity), undergrad-accessible (her name carries forward from nursing-history contexts even if the statistical contribution is less known), lesser-known *as a data visualizer* — most readers know "lady with the lamp" but not "first elected female fellow of the Royal Statistical Society." Example prompt: *"Visit the Wikipedia page for Florence Nightingale. Read the 'Statistics and sanitary reform' section. In 200 words, explain why her Rose Diagram is a figure that earned its place by Tufte's criteria. Then propose one figure in your own textbook draft that could be redesigned in the same spirit — surfacing the argument the data already supports."*

**Candidate 2: Mona Chalabi (Wikipedia: "Mona Chalabi")** — Wikipedia page exists. Substantive connection: working data journalist (Iraqi-British, diverse on two axes), known for hand-drawn data illustrations that defy Tufte minimalism. Useful precisely because she is contested — she lets Chapter 9 stage a real disagreement about what "earns its place" means. Satisfies criteria: woman, non-Western heritage, undergrad-accessible (Guardian US, Instagram presence). Example prompt: *"Visit the Wikipedia page for Mona Chalabi. Find one of her published data illustrations. Apply Tufte's data-ink ratio diagnostic. Then argue the opposite — that the illustration succeeds *because* of what Tufte would call chartjunk. Which case is stronger for your textbook's audience?"*

**Candidate 3: Muriel Cooper (Wikipedia: "Muriel Cooper")** — Wikipedia page exists. Substantive connection: MIT Media Lab Visible Language Workshop founder; designer who first articulated dynamic typography and information landscapes as design problems. The intellectual ancestor of every responsive book layout that exists now, including EPUB reflow. Satisfies criteria: woman, lesser-known (most designers don't know the name despite using her ideas daily), undergrad-accessible. Example prompt: *"Visit the Wikipedia page for Muriel Cooper. Read about the Visible Language Workshop. In 250 words, connect Cooper's idea that typography should respond to context to the EPUB reflow problem Chapter 11 will introduce. What does it mean to design a figure that survives reflow?"*

**Recommendation:** Lead with Nightingale (strongest fit, well-known name, lesser-known contribution). Use Chalabi or Cooper as the alternate.

---

## 6. Pedagogical Delivery Research

The chapter teaches a *tool sequence* (Finishing Pass → CAJAL Image Suggest → CAJAL SVG Generator → enrichment) and a *standard* (the AI+1 visual standard). Two pedagogical risks:

1. **Tool-sequence chapters age fast.** Mitigation: teach the *function* of each step (subtitle pass = "surface the central tension," CAJAL Image Suggest = "candidate figure inventory") so the chapter survives a CAJAL rename or refactor.
2. **Designers resist house style.** A graphic-designer reader will arrive with strong opinions about gradients, corner radii, and color choices. The chapter must concede the aesthetic argument *and* hold the line on the pedagogical one: the constraint is not "this is more beautiful" but "this is more legible across devices, more reproducible across rebuilds, and less likely to fail the fact-checking and accessibility passes."

Worked-example structure: show one chapter through the full pipeline with cajal.md, SVG, and enriched chapter side by side. Annotate which CAJAL suggestions were taken as-is, which were modified, which were rejected. This is the visual analogue of Chapter 8's three-pass rewrite worked example.

Exercise design: the three exercises in TIKTOC.md are all Apply-level. This is correct for an Act-Three execution chapter. The Evaluate-level work is *embedded* in Apply ("Confirm Critical-ranked figure matches chapter's primary learning outcome" — that's an evaluative check inside an applied step).

---

## 7. Representation and Display Research

**Brutalist / Swiss defaults rationale:** The Müller-Brockmann grid + Bringhurst typography defaults solve a publishing problem the AI+1 series faces specifically: figures must render correctly across Kindle Paperwhite (e-ink, grayscale, 300dpi, ~6"), iPad Kindle app (color, retina, ~10"), iPhone Kindle app (color, retina, ~6"), and PDF print (color or grayscale, 600dpi+). A gradient that renders as a smooth ramp on iPad becomes a banded mess on e-ink. A rounded-corner card that looks contemporary in Figma becomes pixelated at small reflow sizes. The minimalist defaults are *device-agnostic* — they degrade gracefully.

**Color:** Two-color or three-color palettes maximum for instructional figures. ColorBrewer "Set2" (qualitative) and "Blues" (sequential) are the safe defaults. Avoid red/green pairings (color blindness). All figures must work in grayscale.

**Type in figures:** Match the body type of the book. Mixing typeface families inside figures (one for axis labels, another for callouts) reads as amateurish — Bringhurst's "rule of similars."

**Alt text:** Every SVG must have a `<title>` and `<desc>` element. This is an EPUB 3 accessibility requirement and also a fact-checking aid (alt text that drifts from the figure is a flag).

**Subtitle pedagogy:** A topic heading names the territory ("Color theory"). A subtitle surfaces the tension ("Why every accessible palette starts with grayscale"). Chapter 9's "subtitle pass" is teaching the reader to write subtitles that do load-bearing work — a journalistic craft move (Jack Shafer at Slate is the contemporary reference; Carl Bernstein on headlines is the canonical-but-loose reference).

---

## 8. Open Questions and Research Gaps

- **CAJAL documentation gap.** CAJAL is proprietary to the AI+1 toolchain. The chapter must teach the function (figure-suggestion-by-AI) without producing a dependency on the specific tool — what happens when the reader is using a future version with different output? Treat CAJAL output as *an instance* of figure-suggestion artifacts, not the only form.
- **The "designer reader objects to defaults" problem.** Needs a sidebar or a worked example showing why the constraint helps the book. Empirical: pick one figure where the designer-author wanted a gradient, show the e-ink render that broke, show the flat-fill replacement that worked.
- **D3 in HTML companion files (d3/).** The chapter mentions D3 HTML files exist but does not specify what role they play in the published book. Are these companion-web artifacts? Print-only fallbacks? Unclear from TIKTOC.md. Author decision required before draft.
- **Subtitle-craft sourcing.** There is no canonical text on subtitle craft for instructional materials. The reference set is journalism (Bernstein, Shafer) by analogy. Either commission a short reference list or accept this as a chapter-internal craft argument.

---

## 9. Sourcing Notes

- Tufte: cited from *Visual Display of Quantitative Information* 2nd ed. (2001) and *Envisioning Information* (1990) — both Graphics Press, both widely available, both standard in design libraries.
- Bertin: trans. *Semiology of Graphics* (1983) is the accessible English edition; original French 1967.
- Knaflic, Cairo, Williams, Bringhurst: all in print in 2026, all available on Kindle (which is itself a relevant fact for an AI+1 author-reader).
- Munzner: CRC Press, 2014; supplemental material at tamaramunzner.com.
- Müller-Brockmann: *Grid Systems in Graphic Design* (Niggli, 1981) is the canonical bilingual edition.
- Nightingale: Wikipedia entry "Florence Nightingale" — confirmed substantial; cross-reference *Florence Nightingale: The Passionate Statistician* by Lynn McDonald for depth if needed.
- Chalabi: Wikipedia entry "Mona Chalabi"; supplemental — her *Mona Chalabi Draws the News* book (Workman, 2024).
- Cooper: Wikipedia entry "Muriel Cooper"; supplemental — *Muriel Cooper* (MIT Press, 2017) by David Reinfurt + Robert Wiesenberger.
- Vega-Lite: Wongsuphasawat et al, *IEEE TVCG* 2017; spec at vega.github.io/vega-lite.
- Bostock D3: d3js.org; observablehq.com.
- Bateman et al "Useful Junk?": CHI 2010 — confirms chartjunk debate has empirical complications.

**Flag — proprietary tooling:** CAJAL Image Suggest and CAJAL SVG Generator are AI+1 toolchain components. No external citation possible. Treat as instance-of-pattern, document the function rather than the specific tool.
