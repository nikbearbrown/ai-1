# Figure Plan — Chapter 6: Research Pass: Pantry Population

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mechanistic.*

## Figure 6.1 — The Gatherer pipeline and where the human re-enters (Critical, MC)
**Trigger:** "For every chapter ... it does three things in order: reads the capability statement ... consults any shared library files in pantry/ ... then runs web research and writes a nine-section notes file" — mapped onto Cooper's five-stage review (problem formulation, data collection, evaluation, analysis, presentation) where "The Gatherer compresses Cooper's first three stages ... The two it cannot compress are evaluation and analysis. Those are yours." A multi-step process with an explicit hand-off boundary the reader must see.
**Figure type:** process flowchart
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 6 stages left-to-right along Cooper's chain — (1) problem formulation, (2) data collection, (3) presentation/draft notes [these three inside a "Gatherer / machine" band], then a dividing boundary, then (4) evaluation, (5) analysis [these two inside a "human / four-questions" band], (6) draft-ready pantry file (terminal). 6 stages + 1 boundary marker.
- O: horizontal left-to-right →; a vertical dividing line ("the seam") between stage 3 and stage 4 marking the machine→human hand-off; machine stages tinted one color, human stages another
- P: flat vector, Okabe-Ito — machine/Gatherer stages Blue #0072B2, the seam/boundary Black #000000, human evaluation+analysis stages Orange #E69F00, draft-ready terminal Bluish Green #009E73; uniform 1pt strokes; white background; unannotated
- E: do NOT enumerate the nine notes sections here (that is the structural subject of the file, kept as text); do NOT show the four questions individually (Figure 6.2); do NOT depict citation-fabrication mechanism; do NOT show the _lib_ shared-library wiring (Figure 6.3)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 6.2 — Thin-pantry triage: three causes, three responses (Critical, VG)
**Trigger:** The chapter prints an explicit decision tree — "Pantry file thin? ├── Topic is hard → Supplement by hand (45 min) ├── Field evidence thin → Accept with flag ... └── TIKTOC.md vague → Return to /c1" — plus the existing four-question rubric TABLE comment. This is a branching/decision claim (three mutually exclusive causes each routing to one response) that is much clearer as a tree than as prose, and "picking the wrong response wastes either an hour ... or weeks."
**Figure type:** systems diagram (decision tree / branch)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 1 root decision node ("pantry thin?") branching to 3 cause nodes (topic hard / field evidence thin / TIKTOC.md vague), each terminating in 1 response node (supplement 45 min / accept-with-flag → risks.md / return-to-/c1 → rerun Gatherer). 7 nodes total (1 root + 3 causes + 3 responses).
- O: left-to-right branch — root on the left, three parallel branches fanning out, each branch a single → arrow to its paired response on the right; the "return-to-/c1" response carries a back-loop arrow (upstream fix)
- P: flat vector, Okabe-Ito — root node Black #000000, cause nodes Yellow #F0E442, response "supplement" Sky Blue #56B4E9, response "accept-with-flag" Orange #E69F00, response "return-to-/c1" Vermillion #D55E00 with a back-loop arc; uniform 1pt strokes; white background; unannotated
- E: do NOT bake in the cause/response text; do NOT show the four evaluation questions (Figure 6.1's human band covers the evaluate step; the questions stay as a TABLE); do NOT depict the risks.md file contents; do NOT show the annotated pantry example
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 6.3 — The _lib_ shared library: one authoritative home (Important, MC)
**Trigger:** "every piece of knowledge has a single authoritative home ... that home is any file in pantry/ whose name starts with `_lib_` ... The Gatherer reads `_lib_` files before generating chapter-specific notes ... it references the definition ... When you update a definition once, every subsequent run sees the update." A DRY-principle hub-and-spoke claim: one shared file referenced by many chapter pantry files, contrasted with the drift of duplicated definitions.
**Figure type:** systems diagram (hub-and-spoke / single-source-of-truth)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 1 central _lib_ hub node, 4–5 chapter pantry-file nodes around it connected by reference arrows pointing INTO each chapter from the hub (the definition flows out, single source). 6 elements (1 hub + 5 spokes). Optionally one small "drift" counter-icon is EXCLUDED (see E).
- O: radial hub-and-spoke; hub centered, chapter files arranged around it; arrows from hub → each chapter file (read-before-drafting direction); a single update on the hub implied to propagate along all arrows
- P: flat vector, Okabe-Ito — hub Bluish Green #009E73, chapter pantry nodes Blue #0072B2, reference arrows Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT draw the "duplicated definition drift" failure as a second diagram (keep this figure to the single-source-of-truth structure only); do NOT bake in filenames (_lib_glossary etc.); do NOT show what belongs vs. does-not-belong as a table inside the figure; do NOT depict the Gatherer pipeline (Figure 6.1)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 6.4 — Three note layers: literature notes vs. permanent notes (Important, MC)
**Trigger:** "Niklas Luhmann's Zettelkasten ... had three layers: fleeting notes ... literature notes recording what a source actually said ... and permanent notes carrying the writer's own argued claim. Pantry files are Ahrens's literature notes. Chapter drafts are permanent notes. Treating literature notes as if they were already permanent ... is what produces ... hallucinated citations." A three-layer structural mapping (Zettelkasten layer → AI+1 artifact) the reader must hold to understand "pantry is not citation."
**Figure type:** conceptual map (three-tier mapping with a blocked shortcut)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 3 stacked layer bands (fleeting / literature = pantry / permanent = chapter draft), a → arrow showing the correct path literature→primary-source→permanent, and a ⊣ blocked arrow showing the forbidden direct cut literature→permanent (the AI-laundered citation shortcut). 5–6 elements (3 bands + correct arrow + blocked arrow + primary-source waypoint).
- O: vertical three-tier stack bottom-to-top (fleeting at base, permanent at top); a correct path arrow routing through a small primary-source waypoint; a second arrow attempting to skip the waypoint, terminated with a ⊣ blockage glyph
- P: flat vector, Okabe-Ito — fleeting layer Sky Blue #56B4E9, literature/pantry layer Blue #0072B2, permanent/draft layer Bluish Green #009E73, primary-source waypoint Black #000000, blocked-shortcut arrow Vermillion #D55E00 ending in ⊣; uniform 1pt strokes; white background; unannotated
- E: do NOT include the 90,000-card / 70-books biographical figures; do NOT depict the moodboard analogy as a separate image; do NOT show the annotated good/bad pantry section (that is the existing IMAGE editorial spread, not a CAJAL figure); do NOT use red-green
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. Figure 6.2's triage and Figure 6.4's blocked shortcut are logical relations, not time-based mechanisms; the ⊣ blockage glyph carries the "do not do this" learning target without animation.

## Notes
- The two existing IMAGE comments (bad-vs-good pantry Section 1 spread, line 249; and the broader annotated-pantry block) are editorial/typographic side-by-side text comparisons, NOT diagrams — deliberately left out of the CAJAL figure set. Same reasoning as Chapter 4's prose-spread.
- Two TABLE comments (four-question rubric, line 85; _lib_ file taxonomy, line 133) are genuine tables; Figure 6.3 visualizes the _lib_ *structure* (hub-and-spoke), which is complementary to the taxonomy table, not a replacement.
- One concept that is arguably two: Figure 6.1 fuses the Gatherer's 3-step procedure with Cooper's 5-stage review. They are aligned (Gatherer = Cooper stages 1–3; human = stages 4–5), so a single 6-stage chain with a hand-off seam is faithful; if it crowds, the split point is the seam itself.
- Figure 6.4 includes one inferred element — the explicit "primary-source waypoint" on the correct path — which the chapter implies ("trace the claim through the pantry to the original source") but does not draw as a node. Labeled here as an inferred relationship per the no-fabrication rule.
- Total CAJAL figure count: 4.
