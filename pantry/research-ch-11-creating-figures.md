# Research: Chapter 11 — Creating Figures
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students learn to decide what a single figure is allowed to contain — using the SCOPE framework and the component ceiling — so that every figure teaches rather than clutters.
**Research date:** 2026-06-02

---

## 1. Chapter Summary from TIKTOC.md

**Opening:** A designer-author types a prompt and gets a beautiful, unusable 14-component diagram. The chapter works backward from the failure to the discipline that prevents it.

**Core content blocks:**
1. The component ceiling — Cowan's four-chunk limit; why six-to-eight is the working budget; the comprehensiveness vs. comprehension trade-off
2. SCOPE — five parameters; why the exclusion list is more important than the inclusion list; silent vs. interactive mode; the gate CAJAL holds hardest
3. The two palettes — Okabe-Ito for publication-neutral figures; Bear Brown / Brutalist D3 for the series house style; one rule that governs both (grayscale test)
4. What the pipeline produces — SVG as source, PNG as publication artifact, D3 HTML as authorable source; no text labels in the generated image
5. Worked example decided out loud — one figure, all five SCOPE decisions made explicit, exclusion list written

**Worked example:** Chapter 7 of ai-for-designers through a complete CAJAL interactive session — SCOPE built live, figure generated, output evaluated.

---

## 2. Primary Sources and References

**Nelson Cowan, "The magical number 4 in short-term memory: a reconsideration of mental storage capacity" (Behavioral and Brain Sciences, 2001).** Cowan argues that working memory capacity is closer to four chunks than Miller's famous seven-plus-or-minus-two. This is the core cognitive justification for the chapter's component ceiling. Source: PubMed abstract (https://pubmed.ncbi.nlm.nih.gov/11515286/); open discussion in Cowan's later "Magical Mystery Four" article (https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/).

**Journal of Cognition, "Modelling Working Memory Capacity: Is the Magical Number Four, Seven, or Does it Depend on What You Are Counting?" (2024).** Useful current-state update: the field still debates exact capacity because "item," "chunk," and task structure matter, but Cowan's four-chunk framing remains a strong teaching simplification. Source: https://journalofcognition.org/articles/10.5334/joc.387

**Masataka Okabe and Kei Ito / Color Universal Design.** The Okabe-Ito palette is the canonical colorblind-safe palette for scientific and technical graphics. It supports the chapter's claim that publication-neutral figures should start from accessibility rather than decoration. Secondary source with attribution and palette discussion: https://vizcept.com/blog/okabe-ito-palette-guide

**W3C WAI Images Tutorial.** The chapter should treat figures as accessibility artifacts, not only visual artifacts. Decorative images need empty alt text; informative and complex images need text alternatives or adjacent explanations. Source: W3C decorative images tutorial (https://www.w3.org/WAI/tutorials/images/decorative/); WAI image decision tree (https://w3c.github.io/wai-tutorial-images/tutorials/images/decision-tree/).

**Edward Tufte, *The Visual Display of Quantitative Information* (1983/2001).** Tufte's data-ink ratio and chartjunk critique give a vocabulary for why a beautiful 14-component diagram can fail pedagogically: it may maximize visual production while minimizing visual explanation. Use carefully: Tufte is about quantitative displays, but the discipline of removing non-teaching elements transfers to diagrams.

**Alberto Cairo, *How Charts Lie* (2019).** Cairo is a contemporary bridge from data visualization to public understanding. Useful for teaching that charts are claims and that visual choices alter interpretation.

**Local library cross-reference: `_lib_tic-toc-v2.md`.** Relevant because Tic TOC's instructional architecture rules require learning outcome before content. Chapter 11 should require figure purpose before figure generation.

---

## 3. Conceptual Foundations

### Concept 1: A figure has a job, not a topic

The clearest teaching move is to separate topic from task. "A diagram of the AI+1 pipeline" is a topic. "Show why the human rewrite is the gate between draft and publishable book" is a job. A figure that knows its job can omit most of the topic. A figure that only knows the topic tends to include everything.

**Common misconception:** Learners assume a figure should summarize everything in the section. That produces encyclopedic diagrams whose visual density defeats the learning outcome.

**Worked example:** For Chapter 7, do not ask for "a diagram of chapter writing." Ask for "a five-step diagram showing where the author-instructor intervenes after Cowork produces a draft." That automatically excludes publishing, Canvas, KDP, figures, and enrichment.

**Source(s):** Local Tic TOC principle in `_lib_tic-toc-v2.md`; Tufte and Cairo on visual claims.

### Concept 2: The component ceiling is a cognitive budget

Cowan's four-chunk limit is not a literal rule that every figure may contain only four visual objects. It is a warning that working memory is small and that "chunking" does real labor. In a technical figure, six to eight components can work only if they are grouped into a small number of meaningful chunks. Fourteen unrelated components usually means the author has outsourced decision-making to the reader.

**Common misconception:** "More complete" means "more educational." Correct version: completeness in the book can be distributed across prose, captions, examples, and multiple figures. A single figure should carry one teaching burden.

**Worked example:** A 12-step pipeline can become three chunks: "Plan," "Draft," "Ship." Each chunk may show two or three internal elements, but the visual hierarchy must make the chunking obvious.

**Source(s):** Cowan 2001 (https://pubmed.ncbi.nlm.nih.gov/11515286/); Cowan 2010 discussion (https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/); 2024 capacity review (https://journalofcognition.org/articles/10.5334/joc.387).

### Concept 3: SCOPE is a pre-generation contract

SCOPE should be taught as a contract before prompting CAJAL, not as a post-hoc critique. The five gates should specify subject, claim, objects/components, presentation constraints, and exclusions. The exclusion list is the most important part because AI image tools tend to over-complete the scene unless told what not to include.

**Common misconception:** A better prompt is a longer prompt. Correct version: a better prompt has a sharper exclusion boundary and a visible teaching claim.

**Worked example:** "Exclude code windows, robot icons, generic magic sparkle visuals, decorative gradients, and text labels inside the image." This keeps the figure from becoming a generic AI stock image.

**Source(s):** TIKTOC.md Chapter 11 entry; local CAJAL figure pipeline files in pantry.

### Concept 4: Palettes are accessibility decisions

The palette is part of the figure's argument because it determines what distinctions are visible. Okabe-Ito is appropriate when the goal is publication-neutral clarity and color-vision-deficiency resilience. Bear Brown / Brutalist D3 can be appropriate as house style, but it must still pass grayscale and secondary-encoding tests.

**Common misconception:** "Colorblind-safe" means the figure is accessible. Correct version: color is only one channel. Accessible figures need contrast, shape, position, labels/captions, and text alternatives.

**Worked example:** If two categories differ only by blue and green, add shape, line style, direct labeling in caption/prose, or spatial separation. Then view in grayscale.

**Source(s):** Okabe-Ito palette discussion (https://vizcept.com/blog/okabe-ito-palette-guide); W3C WAI image guidance (https://www.w3.org/WAI/tutorials/images/decorative/).

### Concept 5: SVG, PNG, and D3 have different jobs

SVG is a source artifact: inspectable, editable, scalable. PNG is a publication artifact: stable, predictable, easy to include in EPUB/PDF. D3 HTML is an authorable/interactive artifact: useful for exploration and web companion material, but it should not be the only artifact used in a Kindle/PDF build.

**Common misconception:** The prettiest rendered output is the source of truth. Correct version: the source of truth is the editable representation plus the documented decision logic that produced it.

**Worked example:** Generate `chapter-07-figure.svg`, render `chapter-07-figure.png`, and keep `chapter-07-figure.html` only if interaction adds teaching value beyond the static figure.

**Source(s):** Local AI+1 pipeline files and TIKTOC.md Chapter 11.

---

## 4. Domain Examples and Cases

### Case 1: The 14-component AI pipeline diagram

A designer-author asks an image model for the whole AI+1 pipeline and receives an impressive diagram with icons, arrows, clouds, books, robots, dashboards, code, students, and text labels. The failure is not aesthetic; it is instructional. The figure has too many components, no clear claim, and no exclusion discipline.

### Case 2: Okabe-Ito scientific palette

Scientific visualization communities use Okabe-Ito because it survives common color-vision deficiencies better than default rainbow palettes. The AI+1 lesson: choose the palette for perceptual reliability first, house style second.

### Case 3: D3 as authorable source

D3 is useful because it makes structure explicit: data, scales, marks, interactions. But for a Kindle/PDF book, D3 must be rendered to a static asset. The author-instructor needs to know which artifact is for authoring and which artifact is for publishing.

### Failure case: Text labels inside generated images

Generated images often mangle text labels or create illegible pseudo-text. The TIKTOC rule "no text labels in the generated image" is sound: put explanatory language in the caption or surrounding prose, where it can be edited, searched, translated, and read by assistive technology.

---

## 5. Connections and Dependencies

**Prerequisites:**
- Chapter 4 TIKTOC discipline — the reader must know that architecture precedes generation.
- Chapter 9 finishing pipeline — the reader must understand where CAJAL suggestions, SVGs, PNGs, and D3 files enter the build.
- Basic accessibility literacy — the reader must know that visual assets need text alternatives and contrast checks.

**Unlocks:**
- Chapter 12 final build — figures must be stable before EPUB/PDF validation.
- Chapter 13 Canvas export — Canvas pages and assignments need accessible images and stable static assets.
- Future AI+1 editions — a documented SCOPE block makes figure revision repeatable.

**Adjacent chapter connections:**
- Chapter 10: Enrichment adds LLM exercises; Chapter 11 prevents the visual layer from becoming generic or overloaded.
- Chapter 12: Final check depends on figures that render cleanly and carry alt/caption decisions.

---

## 6. Current State of the Field

**Settled:**
- Working memory is limited; exact capacity varies by task, but four chunks is a defensible teaching anchor. Source: Cowan 2001 (https://pubmed.ncbi.nlm.nih.gov/11515286/).
- Accessible images need author judgment: decorative images can use empty alt text, but informative/complex images need alternatives. Source: W3C WAI (https://www.w3.org/WAI/tutorials/images/decorative/).
- Color alone should not carry critical information.

**Contested or emerging:**
- Exact component ceilings are design heuristics, not laws. A well-grouped complex figure can work; a poorly grouped six-component figure can fail.
- Generative image systems are improving at typography, but production textbooks should still avoid relying on generated text inside images because editability and accessibility remain poor.
- Visual style systems for AI-native textbooks are still emerging; the AI+1 house style should be treated as a repeatable design language, not decoration.

**Recent changes to acknowledge:**
- AI image generation has made it easy to produce polished diagrams before the author has decided what the diagram should teach.
- Accessibility expectations for digital instructional materials are rising; figure decisions now have compliance and inclusion implications, not only design implications.
- Browser and tooling support makes SVG/D3 authoring easier, but Kindle/PDF deployment still rewards stable static images.

---

## 7. Teaching Considerations

Students get stuck because they judge figures by beauty before usefulness. The chapter should make them evaluate a figure in this order: learning claim, component count, grouping, exclusion list, accessibility, then style.

Effective analogy: "A figure is a whiteboard moment, not a poster." It should help the reader understand one move at the moment they need it.

Best exercises:
1. Take an overloaded generated diagram and write a SCOPE exclusion list.
2. Reduce a 12-component figure to six components without losing the learning claim.
3. Convert a colorful figure to grayscale and identify which distinctions fail.
4. Write alt text and a caption for the same figure, explaining the different job each performs.

---

## 8. Open Questions and Production Risks

- The exact SCOPE acronym expansion should be standardized before drafting.
- The Bear Brown / Brutalist D3 palette should be documented in one palette file and checked against grayscale and color-vision simulations.
- The Chapter 7 worked example should be a real CAJAL session, not a reconstructed one.
- If D3 HTML appears in the book repo, the build script must clearly distinguish source, rendered PNG, and optional web companion artifact.

