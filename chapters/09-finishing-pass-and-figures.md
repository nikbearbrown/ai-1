# Chapter 9 — Finishing Pass and Figures
*Where the book becomes visible — and the visual fluency trap arrives on schedule.*

**Capability:** Students run the finishing pipeline — subtitle pass, CAJAL figure intelligence, SVG generation, enrichment — and evaluate output against the AI+1 visual standard.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Run the Chapter Finishing Pass across your chapters and confirm each one has a subtitle that surfaces the chapter's central tension and at least two visual placeholder comments at the right moments in the prose.
2. **(Apply)** Run CAJAL Image Suggest and read the `cajal.md` files it produces — distinguishing Critical from Important from Supplementary figure candidates, and explaining which of MC, VG, or PQ triggered each one.
3. **(Apply)** Run the CAJAL SVG Generator and the enrichment pass, and verify that every chapter has at least one PNG in `images/` and at least one corresponding D3 file in `d3/`.
4. **(Evaluate)** Audit a generated SVG against the AI+1 visual standard — flat fills, no gradients, axes labeled, a `<title>` and `<desc>` for accessibility, and a figure that *makes the argument the text could not make as efficiently*.
5. **(Analyze)** Identify a visual fluency trap in a CAJAL-generated figure — a chart that looks correct but encodes the wrong claim — and name what to change.

---

## The chapter before and after — and the missing thing in both

Here is one paragraph from a draft of Chapter 7 of *ai-for-designers*, exactly as Cowork produced it:

> *Five things to watch for in the draft. Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.*

And here is the same paragraph after a finishing pass:

> ## Five failure modes — read in this order
> *The model is good at producing prose that reads correct and means nothing. Here is what to look for first.*
>
> Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.
>
> <!-- → [INFOGRAPHIC: Five Failure Modes — a 5-row table laid out as a vertical taxonomy. Left column: failure name. Middle column: how it sounds in a draft. Right column: rewrite move. Two-color (ink + ochre), no gradients.] -->

Same prose. Three additions. A heading that names what is coming. An italic subtitle under it that says *what this section is actually doing*. A visual placeholder comment at the moment the reader needs to see the taxonomy as a structure rather than a paragraph.

The "after" is still missing something. There is no figure yet. There is only a comment that says *a figure goes here, and here is what it should do*. That comment is a contract between the author and the finishing pipeline — it tells CAJAL where a figure belongs and what work it is supposed to do.

This is Chapter 9. Three things happen:

- Every chapter gets a subtitle that earns its place and at least a few honest visual placeholder comments embedded where they would help.
- CAJAL reads those chapters and proposes a structured set of figure candidates per chapter, ranked.
- The proposals become real SVGs, real PNGs, real D3 files. The book becomes visible.

You are also going to learn what the visual fluency trap looks like, because it is going to arrive — CAJAL can produce a chart that is technically a chart, semantically empty, and convincingly designed. You will catch it the same way you caught the verbal fluency trap in Chapter 1. The skill transfers.

---

## Sidebar — Installing Node.js (5 minutes, three commands)

CAJAL's SVG generator and the PNG converter at `SCRIPTS/svg-to-png.mjs` are Node.js programs. You need Node 18 or higher. If you do not already have it, this is a five-minute job.

**Mac (using Homebrew):**
```
brew install node
node --version
npm --version
```

**Windows (using winget):**
```
winget install OpenJS.NodeJS.LTS
node --version
npm --version
```

**Linux (Ubuntu/Debian):**
```
sudo apt update && sudo apt install -y nodejs npm
node --version
npm --version
```

**Verification:** Both `node --version` and `npm --version` should print a version number. If `node --version` prints anything below `v18.0.0`, upgrade — the SVG-to-PNG converter uses modern ECMAScript modules and will fail silently on older versions.

**One more thing.** The PNG converter uses a package called `sharp`. From inside your book directory:

```
cd SCRIPTS/
npm install sharp
```

That is the entire Node.js setup. You do not need to learn Node. You do not need to read any JavaScript. You do need it on your machine so the scripts run.

If `npm install sharp` fails — and on some Mac silicon machines it does, with a message about Python or libvips — re-run it with `npm install --include=optional sharp`. That is the only workaround you will ever need. [verify — `sharp` install paths can drift between major versions on macOS]

---

## Block one — The Chapter Finishing Pass

The Chapter Finishing Pass does exactly two things to each chapter file. It does not touch your prose. It inserts (1) an italic subtitle on the line below the main heading if one is missing, and (2) inline HTML comments at the places in the text where a table, image, infographic, or chart would genuinely help the reader.

That is it. Two passes. No rewrite. No reorganization.

This is intentional. The finishing pass runs after the human rewrite from Chapter 8. The prose is the author's at this point. The pass adds *navigational scaffolding* on top — the subtitle is a sub-promise to the reader about what the chapter is actually arguing, and the visual placeholder comments are a contract with the figure pipeline.

### The subtitle test — territory vs. tension

A topic heading names the territory. *"Color theory."* It is true. It is also the kind of thing a Wikipedia stub would say.

A subtitle surfaces the tension. *"Why every accessible palette starts with grayscale."* That second one is doing work — it tells the reader what the *argument* of the chapter is going to be. It commits the author to a position. It is closer to a journalistic deck than a chapter abstract.

Cole Knaflic, in *Storytelling with Data*, calls this "the so-what" — the move from naming a category to naming a claim (Knaflic, *Storytelling with Data*, 2015, Wiley). Robert Bringhurst, in *The Elements of Typographic Style*, treats it as a typographic move — the subtitle is a *different rank* of text and should look different on the page (Bringhurst, *Elements of Typographic Style*, 4th ed., 2013, Hartley & Marks).

Practical rules for a usable subtitle:

- **Less than fifteen words.** If you cannot say what the central tension is in fifteen words, the chapter does not yet know what its central tension is. Return to Chapter 4.
- **A claim, not a category.** If the subtitle could appear under a *different* chapter's heading without breaking, it is not doing chapter-specific work.
- **Italic in the rendered EPUB.** Reflowable EPUBs reliably honor italic styling. They do not reliably honor custom CSS classes. Italic is the safe contract.

Look at the chapters you have already drafted. If the subtitle for a chapter could be the subtitle for any other chapter in your book, the subtitle is not yet finished.

### Visual placeholder comments — the format that survives the pipeline

A visual placeholder comment looks like this:

```
<!-- → [INFOGRAPHIC: Five Failure Modes — a 5-row table laid out as a vertical taxonomy. Left column: failure name. Middle column: how it sounds in a draft. Right column: rewrite move. Two-color (ink + ochre), no gradients.] -->
```

The arrow `→` is the visual signal so you can grep for them later. The bracket type — `INFOGRAPHIC`, `CHART`, `TABLE`, `IMAGE`, `DIAGRAM` — tells the enrichment pass which generator to invoke. The description after the colon is the *brief* the figure-generation step will read.

The brief is what matters. Three rules for a brief that does not produce a generic figure:

- **Name the data, not the category.** Not "a chart of failure modes" but "a 5-row table, named columns, two-color." Generic briefs produce generic charts.
- **Name the constraint.** "No gradients. Two-color. Flat fills." The constraints are how you keep the visual style consistent across the book.
- **Name the load it has to carry.** "The reader should leave knowing what the rewrite move is, not just that there are five failure modes."

A brief that names data, constraint, and load is one that any reasonable figure generator — CAJAL, a junior designer, or a future tool none of us has seen yet — can execute.

---

## Block two — CAJAL Image Suggest: a candidate inventory, not a finished plan

CAJAL Image Suggest runs across every chapter and proposes figures. It does not generate any SVG yet. It writes one file per chapter at `pantry/{chapter-slug}-cajal.md`, listing every figure it thinks would help, ranked by priority, with a full SCOPE prompt for each.

You should think of `cajal.md` as a *menu*. You will reject some items. You will modify some. You will add candidates CAJAL missed. That is the point of having the proposals in their own file before any SVG is generated — you get an editorial pass between the candidate inventory and the rendered figure.

### What CAJAL detects — MC, VG, PQ

CAJAL scans chapter prose for three signal patterns:

- **MC — Mechanism Complexity.** The chapter describes a process with three or more interdependent steps. The pipeline overview in Chapter 5 is MC. The three-pass rewrite loop in Chapter 8 is MC. Most "and then this, and then this" passages are MC.
- **VG — Verification Gap.** The chapter makes a structural claim the reader cannot verify from the prose alone. "The Combined Test has fourteen items in two groups" is a VG signal — the reader has to be shown the structure to confirm it. "Cowork reads four files in order" is VG.
- **PQ — Proportional or Quantitative.** Any percentages, ratios, counts, or comparisons. "Steady workers complete in four to six weeks" is PQ. "Eighty percent of indie ebook units" is PQ. Anything that has a number that compares to another number.

Tamara Munzner's *Visualization Analysis and Design* (2014, CRC Press) calls the same idea the "what-why-how" framework: *what* data do you have, *why* is the reader looking, *how* should it be visually encoded. CAJAL's MC/VG/PQ is a coarser, faster version of the same diagnostic — a triage layer before the full what-why-how decision.

### Anatomy of a `cajal.md` file

Open `pantry/07-the-cowork-draft-run-cajal.md` after a run. You will see a structure something like this:

```
# Figure Plan — Chapter 7

## Figure 7.1 (Critical, MC)
**Title:** The eight-section Cowork chapter structure
**Trigger:** Chapter describes 8 sequential sections each Cowork chapter follows.
**SCOPE:**
  Specification: One-column vertical flow diagram, 8 boxes.
  Content: Section name + one-line "what it does" per box.
  Organization: Top-to-bottom, arrow between each.
  Presentation: Two-color (ink + ochre). No gradients. Flat fills.
  Exclusions: No icons. No screenshots. No decorative borders.

## Figure 7.2 (Important, VG)
**Title:** Five failure modes — taxonomy
... (continued)

## Figure 7.3 (Supplementary, PQ)
**Title:** [verify] count distribution
...
```

The structure is consistent across chapters: title, ranking (Critical / Important / Supplementary), MC/VG/PQ trigger, and a full SCOPE prompt (Specification, Content, Organization, Presentation, Exclusions). The SCOPE prompt is what the SVG Generator in the next step will read.

### How to read priority rankings before running the generator

Treat the rankings as defaults, not orders. A useful pass through a `cajal.md`:

- **Critical** figures should map directly to a primary learning outcome. Open the chapter. If the Critical figure does not encode the thing the reader is supposed to leave knowing, demote it and find one that does.
- **Important** figures support a key argument but are not load-bearing. These are usually safe.
- **Supplementary** figures are nice-to-have. The honest answer is often "skip this one." A textbook is not improved by having a figure on every page.

This is the editorial pass. Spend ten minutes per chapter on it. The next step generates real SVG files from whatever you leave in the `cajal.md` — what you do not edit, you ship.

---

## Block three — CAJAL SVG Generator and enrichment pass

The SVG Generator reads the `cajal.md` files you have edited and produces real SVG files in `images/`. The pipeline then:

1. Runs `node SCRIPTS/svg-to-png.mjs` to convert every new SVG to a 300-DPI PNG.
2. Runs the enrichment pass, which reads every chapter, finds the `<!-- → [...] -->` comments and the matching figures, and inserts a markdown image link at the right location — plus a corresponding D3 v7 HTML file in `d3/` for interactive exploration.

You do not write any JavaScript. You do not read any JavaScript. You read the `cajal-svg-log.md` file that is written at the end, and you open the PNGs.

### SVG → PNG and why both exist

PNG is the *publication* artifact. Kindle's reflow engine renders PNGs reliably across every device — Paperwhite, iPad, iPhone, Colorsoft, desktop Kindle app. SVG is the *source* artifact. You keep it because it is editable, version-controlled, and re-renderable at any resolution. PNG is what ships in the EPUB. SVG is what survives a redesign.

This is the same separation as `combined.md` → EPUB+PDF: the source is text, the build output is the binary thing the device renders. You do not edit the build output. You edit the source and rebuild.

### D3 in HTML — what the d3/ directory is for

For every figure that has data structure underneath it — anything CAJAL flagged as MC or PQ that could be interactive — the enrichment pass also generates an HTML file with a D3 v7 implementation. These files live in `d3/`.

What they are for, honestly:

- They are *not* in the published EPUB. EPUBs do not reliably execute JavaScript.
- They are an authorable artifact — when you want to update a chart in the next edition, you have the D3 source.
- They are a companion-web artifact. Some authors host them at a URL referenced from the book's back matter so readers can explore. That is optional, not required.

If you do not plan to host the D3 files anywhere, they still cost nothing to keep in the repo. The PNG is what the reader sees in the book.

### The AI+1 visual standard — applied to every figure CAJAL produces

The visual house style is the visual analogue of the Combined Test from Chapter 8. Stripped-down. Device-agnostic. The constraint exists so the *content* of the figure carries the load, not the chrome:

- **Two-color or three-color maximum** per figure. ColorBrewer "Set2" (qualitative) and "Blues" (sequential) are the safe defaults. Avoid red/green pairings (color blindness; about 8% of male readers). Every figure must read in grayscale.
- **Flat fills only.** No gradients. Gradients render as a smooth ramp on retina iPad and as a banded mess on e-ink Paperwhite. Flat fills degrade gracefully.
- **No rounded corners, no drop shadows.** Same reason. They look contemporary in Figma. They look pixelated at reflow.
- **Type matches the body type of the book.** Mixing typefaces inside a figure reads as amateurish. Bringhurst calls this the "rule of similars."
- **Every SVG has a `<title>` and `<desc>` element.** This is an EPUB 3 accessibility requirement (per the W3C EPUB Accessibility 1.1 specification, w3.org/TR/epub-a11y-11/). It is also a fact-checking aid — alt text that drifts from what the figure shows is a flag.
- **Axes are labeled. Units are declared. Source and date are present.** Edward Tufte's *Visual Display of Quantitative Information* (2nd ed., 2001, Graphics Press) is the canonical source for this rule and the next one.
- **The figure earns its place.** If the prose conveys the information as efficiently as the figure would, delete the figure. Tufte's data-ink ratio is the diagnostic — the proportion of a figure's ink devoted to non-redundant data. Generic decoration is what he called "chartjunk."

There is a contested edge to this last rule. Bateman et al published "Useful Junk?" at CHI 2010 with empirical evidence that embellished charts are *better remembered* than minimalist ones. Mona Chalabi's hand-drawn data illustrations in the Guardian US (2020 onward) make the same argument from data journalism — visual personality is itself a data-integrity move because it signals provenance and single-author accountability. Both are legitimate. Both are out of scope for the AI+1 series default. The reasoning: a $1 Kindle book is read across more devices than any other format, and the device-agnostic constraint wins until you have a specific reason to break it.

---

## Worked example — One chapter through the full pipeline

The running chapter for this walkthrough is Chapter 7 of *ai-for-designers* — *The Cowork Draft Run*. Here is what each step produced.

### Step 1 — Chapter Finishing Pass output

Before the pass, the chapter heading read:

```
# Chapter 7 — Running the Chapter Writer
```

After the pass:

```
# Chapter 7 — Running the Chapter Writer
*Why the first draft of a fourteen-chapter book takes one hour and three weeks of preparation.*
```

The subtitle surfaces the tension — the *real* runtime is not the model's hour but the author's preparation. The subtitle commits the chapter to an argument.

Three visual placeholder comments were inserted, one of which read:

```
<!-- → [INFOGRAPHIC: The eight-section Cowork chapter structure — 8 vertical boxes, top to bottom, ink + ochre. Each box has section name and one-line description. No icons.] -->
```

### Step 2 — `07-cowork-draft-run-cajal.md` output

Three figures proposed. The Critical one was Figure 7.1 — the eight-section structure flow diagram. The MC trigger fired because the chapter describes eight sequential sections each draft follows. The SCOPE prompt named the data (eight section names with one-line descriptions), the constraint (two-color, flat, no icons), and the load (the reader should leave knowing the *order* and the *function* of each section).

One Important figure (Figure 7.2 — the five failure modes taxonomy, VG trigger) was accepted as-is. One Supplementary figure (Figure 7.3 — a histogram of [verify] flag counts across draft runs, PQ trigger) was *modified* — the original SCOPE called for ten bars; the data only supported five distinct buckets, so the SCOPE was edited down before the SVG step.

### Step 3 — SVG and PNG output

Three SVG files were generated at `images/07-cowork-draft-run-fig-01.svg` through `fig-03.svg`. The SVG-to-PNG converter ran and produced three PNGs at 300 DPI. The enrichment pass inserted the markdown links into the chapter:

```
![The eight-section Cowork chapter structure](../images/07-cowork-draft-run-fig-01.png)
*Figure 7.1 — Eight sections, run in order, no skipping. CAJAL output, edited.*
```

A corresponding D3 file appeared at `d3/07-cowork-draft-run-fig-01.html` for the section-structure diagram. The histogram (Figure 7.3) got a D3 companion because its data structure invited interaction. The taxonomy figure (Figure 7.2) did not — it is a static structural diagram, and the D3 file would be over-engineered for it. The enrichment pass made that judgment automatically.

### What was used as-is, modified, rejected

Across the chapter's three CAJAL suggestions:

- **Figure 7.1** — used as-is. CAJAL's SCOPE was tight and the rendering needed no edits.
- **Figure 7.2** — minor edit. The SCOPE specified three columns; the rewrite added a fourth column (a worked example per row) because the chapter prose had evolved.
- **Figure 7.3** — modified before generation (bar count) and then accepted.
- *One CAJAL suggestion was rejected entirely* — a fourth proposal for a "wordcloud of common failure terms" that CAJAL had flagged as Supplementary. Wordclouds violate the AI+1 visual standard (no data-ink discipline). Deleted from the `cajal.md`.

This is what the editorial pass on `cajal.md` is for. Most of CAJAL's suggestions are honest; some of them are not. The author is the gate.

---

## Two pointer companions — *AI for Graphs* and *AI for Infographics*

CAJAL produces solid first-pass figures. For most handbook chapters that is enough. For chapters where the figure *is* the argument — where the page is dominated by a chart that the prose orbits around — you will want more than what CAJAL plus the enrichment pass produces by default.

Two companion books in this series cover that territory:

### *AI for Graphs* — when the chart carries the chapter

Companion handbook on chart-making with AI assistance for non-statisticians. Most relevant chapters for an AI+1 handbook author:

- **Chart selection by question.** Munzner's what-why-how applied as a decision flowchart. When is a small-multiples grid the right answer? When is a single dual-axis chart never the right answer? This is the chapter for any time CAJAL proposes a "PQ" figure and you are not sure of the chart type.
- **The reading-on-device pass.** Render a chart at iPad size, iPhone size, e-ink size, and PDF print size before committing. This is the practical follow-up to the AI+1 visual standard's "device-agnostic" rule.
- **Reading a chart for what it is hiding.** The Challenger O-ring case as a structural lesson — the same data plotted to surface the temperature dependence (the case Tufte uses as the canonical "figure that fails its argument"). This is the chapter for catching the visual fluency trap.

### *AI for Infographics* — when the figure is the spine

Companion handbook on instructional infographics — the figures that *replace* sections of prose rather than illustrating them. Most relevant chapters for a handbook author:

- **Taxonomy figures.** The structural diagram type that Figure 7.2 belongs to. How to design one that the reader can scan in twelve seconds. Williams's CRAP principles (Contrast, Repetition, Alignment, Proximity) from *The Non-Designer's Design Book* (4th ed., 2014, Peachpit) applied to instructional layout.
- **Process diagrams beyond linear flows.** MC-triggered figures often want a non-linear structure (parallel tracks, branches, feedback loops). This chapter covers when to leave a "flowchart" behind.
- **The accessibility audit.** Alt text, color-blind palettes, screen-reader-readable SVG structure. The EPUB 3 accessibility requirement made operational.

You do not need either of these companions to finish your handbook. You need them when you find yourself fighting CAJAL — when the default output is producing figures and you can see they are wrong but cannot say what would be right.

---

## Exercises

### Exercise 9.1 — (Apply) Run the Chapter Finishing Pass

Run the Chapter Finishing Pass on your book. Confirm:

- Every chapter has a one-line italic subtitle below the main heading.
- Every chapter has at least two visual placeholder comments in the prose.
- For each subtitle, write one sentence answering: *what argument does this subtitle commit the chapter to?* If you cannot answer in one sentence, the subtitle is a territory label, not a tension. Rewrite it.

Deliverable: a list of every chapter's subtitle and the one-sentence argument each one names. Flag any subtitle you could not answer for.

### Exercise 9.2 — (Apply) Run CAJAL Image Suggest, audit one cajal.md

Run CAJAL Image Suggest. Open the `cajal.md` for one chapter — pick the chapter you are most uncertain about visually. Confirm:

- The Critical-ranked figure for that chapter maps directly to one of the chapter's primary learning outcomes (from your TIKTOC.md /l2 outcomes map).
- If it does not, rewrite the SCOPE prompt for that figure until it does — or demote it and find one that does.
- Identify one Supplementary-ranked figure you will skip. Note the reason.

Deliverable: a single edited `cajal.md` with at least one SCOPE rewrite and at least one deletion, plus a one-paragraph note explaining the editorial decisions.

### Exercise 9.3 — (Apply) Run the CAJAL SVG Generator and enrichment pass

Run the CAJAL SVG Generator. Then run the enrichment pass. Confirm:

- At least one PNG per chapter exists in `images/`.
- At least one D3 file per chapter (where appropriate) exists in `d3/`.
- Every chapter file now contains markdown image links to the generated PNGs at the placeholder locations.
- The `cajal-svg-log.md` is written and lists every figure generated.

Then — and this is the part the pipeline cannot do — open three figures at random and audit them against the AI+1 visual standard. Two-color or three-color. Flat fills. Axes labeled, units declared, source and date present. `<title>` and `<desc>` in the SVG.

Deliverable: three audited figures with a one-line pass/fail per criterion, plus one identified fix.

---

## AI Wayback Machine — Florence Nightingale

Most readers know Florence Nightingale as the "lady with the lamp" — the nurse who reformed military hospital sanitation during the Crimean War. Fewer readers know that she designed the chart that did the reforming.

The figure was a polar-area diagram — the *Diagram of the Causes of Mortality in the Army in the East* (1858) — showing, month by month, that preventable disease killed many more British soldiers than battle wounds did. She designed it for Queen Victoria and the British Parliament, not for statisticians, and she designed it because the standard tables of mortality data were not changing anyone's mind. The chart did. Sanitary reform of military hospitals followed. She was, in 1859, elected the first female fellow of the Royal Statistical Society.

The chart earned its place by changing policy.

**Try this prompt:** *Visit the Wikipedia page for Florence Nightingale. Read the "Statistics and sanitary reform" section. In 200 words, explain why her Rose Diagram is a figure that earned its place by Tufte's criteria. Then propose one figure in your own textbook draft that could be redesigned in the same spirit — surfacing the argument the data already supports.*

To make the prompt sharper: name the specific chapter and figure you are testing. Ask the model to compare its proposed redesign to Nightingale's polar-area choice. Ask one follow-up about what *constraint* (audience, device, story) made Nightingale's choice the right one.

---

## Bridge — figures in place, one layer left

The book is now visually complete. Subtitles surface the arguments. Figures encode what the prose cannot encode efficiently. The PNGs render on every device. The SVGs are version-controlled and editable.

What is missing is the layer that makes this an *AI+1* textbook rather than a textbook about AI. The reader needs LLM Exercises and Dig Deeper prompts that are *only* useful in this domain, for this reader, at this career stage. Chapter 10 adds that layer — and the fluency trap returns one more time, this time at the pedagogy scale.

---

## Still puzzling

Open questions this chapter does not close:

1. **When does an instructional figure cross the line into McCandless-style information design — engagement over data density?** The AI+1 standard says: not in this book. But the McCandless argument is not stupid, and it might be the right call for a different series.
2. **What is the right number of figures per chapter?** CAJAL will gladly propose six. Two-to-four is the working default. The honest answer is *however many earn their place* — but that is recursive.
3. **Should the D3 files in `d3/` ship as a companion web property?** The book is content-complete without them. Hosting them costs something. Worth it? Author decision, not pipeline decision.
4. **CAJAL is part of the AI+1 toolchain.** What happens if a future version produces output structured differently — different `cajal.md` schema, different SCOPE prompts? Treat CAJAL output as *an instance* of figure-suggestion artifacts, not the only form. The function survives a tool refactor; the file format may not.

## What would change my mind

The strongest counter-argument to the AI+1 visual standard is the Mona Chalabi argument from data journalism: a hand-drawn, distinctive, single-authored visual style is itself a data-integrity move because it signals provenance and a human's accountability for the chart. If a body of evidence emerged — peer-reviewed, replicated — showing that AI+1-style flat-fill figures *consistently underperform* on retention or comprehension compared to embellished figures in instructional contexts, the visual standard would need to change. Bateman et al's "Useful Junk?" (CHI 2010) is the strongest existing piece of evidence in that direction; it is not strong enough to displace the device-agnostic constraint for a $1 Kindle handbook, but a stronger replication would do it. The hill I will die on is *device-agnostic rendering*, not *Swiss minimalism*. If those two ever decouple, the standard changes.
