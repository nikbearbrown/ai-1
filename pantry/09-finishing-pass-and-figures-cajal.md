# Figure Plan — Chapter 9: Finishing Pass and Figures

*CAJAL Image Suggest (silent /scan). Density: 3 figures recommended — Mixed.*

> Note on scope: this chapter is itself about figure-making. Its `images/07-cowork-draft-run-fig-01..03` references are a *worked example* of ai-for-designers' Chapter 7 output — those are not figures for THIS chapter and are not re-proposed here. The chapter also contains four embedded placeholder comments; three are folded in below as Fig 9.1–9.3, and the fourth is deliberately not promoted (see Notes).

## Figure 9.1 — Anatomy of a visual placeholder comment (Important, VG)
**Trigger:** Embedded comment `<!-- → [TABLE: visual placeholder comment anatomy — three columns: element (arrow / bracket type / brief), what it does, example...] -->` plus "The arrow is a grep target... The bracket type... tells the enrichment pass which generator to invoke. The description after the colon is the brief." The three-part decomposition of the comment syntax (arrow / bracket / brief) and what each part feeds downstream cannot be verified from the inline prose.
**Figure type:** annotated example (structural schematic / callout decomposition)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 3 labeled segments of a single comment string — (1) the arrow (grep target), (2) the bracket type (generator selector), (3) the brief after the colon (figure brief). Each segment has one downward callout cell reserved for its downstream role.
- O: one horizontal "comment string" bar at top, segmented into 3 regions left-to-right; one callout line dropping from each region to a reserved role-cell below
- P: flat vector, Okabe-Ito — comment bar Black #000000, the three segments tinted Orange #E69F00 / Sky Blue #56B4E9 / Bluish Green #009E73 respectively, callout lines Black #000000; uniform 1pt strokes; white background; unannotated (segments and role-cells blank for later typography)
- E: do NOT include the subtitle/heading distinction (separate concept), the three brief-writing rules, or the MC/VG/PQ triage; no screenshot chrome; no actual code text baked in
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 9.2 — CAJAL figure-priority decision path (Important, MC)
**Trigger:** Embedded comment `<!-- → [INFOGRAPHIC: CAJAL figure priority decision tree — three nodes: Critical (does it map to a primary outcome?), Important (does it support a key argument?), Supplementary (skip unless time allows)...] -->` plus the editorial-pass prose. A 3-node decision sequence with a yes/no test at each node and a terminal "skip" outcome — a process the reader applies during the ten-minute editorial pass.
**Figure type:** process flowchart (decision tree)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 3 decision nodes — Critical ("maps to a primary outcome?"), Important ("supports a key argument?"), Supplementary ("skip unless time allows") — plus 2 terminal outcomes (keep / skip). The "demote" path off the Critical node is shown as one redirect arrow.
- O: top-to-bottom decision flow; each node has a pass-through arrow (→) to the next test and a side outcome; the Supplementary node terminates in a skip glyph; the Critical node's failed test shows one demote redirect arrow
- P: flat vector, Okabe-Ito — Critical node Vermillion #D55E00, Important node Orange #E69F00, Supplementary node Black #000000, keep-outcome Bluish Green #009E73, skip-outcome with a blockage glyph (⊣); uniform 1pt strokes; white background; unannotated
- E: do NOT include the MC/VG/PQ signal definitions (separate figure), the SCOPE five-field structure, or the visual-standard rules; no decorative tree foliage; no icons
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 9.3 — The CAJAL pipeline: prose to publication artifact (Critical, MC)
**Trigger:** "This chapter runs three operations in sequence" and the detailed flow: Finishing Pass (subtitle + placeholder comments) → CAJAL Image Suggest (writes cajal.md, ranked) → SVG Generator (images/*.svg) → svg-to-png.mjs (300-DPI PNG) → enrichment pass (inserts markdown links) → D3 companion files (d3/). Also "PNG is the publication artifact... SVG is the source artifact." A 5+ step interdependent pipeline with a source/output split that is the chapter's spine and cannot be verified from scattered prose.
**Figure type:** systems diagram / process flowchart (with branch)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 6 nodes — (1) Finishing Pass, (2) CAJAL Image Suggest → cajal.md, (3) SVG Generator → SVG source, (4) svg-to-png converter → PNG, (5) enrichment pass → markdown links inserted, (6) D3 companion (branch, for MC/PQ figures only). The source-vs-output split marked once: SVG = source, PNG = ships.
- O: horizontal left-to-right main flow nodes 1→5 with single arrows; node 6 (D3) as one downward branch off the SVG/data stage; a single divider glyph distinguishing "source artifacts" (SVG, D3) from "ships in EPUB" (PNG)
- P: flat vector, Okabe-Ito — main pipeline nodes Blue #0072B2, the PNG/ships node Bluish Green #009E73, the D3 branch Orange #E69F00, source-vs-output divider Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT depict the Node-install instructions, the visual-standard audit rules, the AI for Graphs / AI for Infographics companion content, or the MC/VG/PQ triage; do NOT bake in the worked-example file paths; no terminal/screenshot imagery
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
FIGURE 9.3 — VIDEO CANDIDATE — transition mechanism is the learning target — the pipeline's value is the *handoff* at each stage (prose → cajal.md → SVG → PNG → inserted link), so an animated walk-through showing each artifact being produced and passed on teaches the sequence better than a static chain. Static is the publication default (EPUB cannot execute JS); flag only as optional companion-web asset.

## Notes
- Total: 3 figures, all folded from the chapter's own embedded comments (the TABLE-anatomy comment, the priority decision-tree comment) plus the spine pipeline ("three operations in sequence"). No fully-novel figures proposed — the chapter is densely self-aware about its own visuals.
- Do NOT re-propose the chapter's worked-example figures (ai-for-designers Fig 7.1 eight-section structure, Fig 7.2 five-mode taxonomy, Fig 7.3 verify-flag histogram) — those are illustrative of another book's output, already specified in-text, and proposing them as new would duplicate.
- The fourth embedded comment in the chapter is the opening "before/after" INFOGRAPHIC for ai-for-designers' five failure modes — that is part of the worked demonstration of the finishing-pass output, not a Chapter 9 figure. Deliberately not promoted (also overlaps Chapter 7's Fig 7.1 taxonomy).
- Two-concepts watch: MC/VG/PQ signal triage is a real candidate (3 parallel definitions) but was NOT promoted — it is three definitional labels with no process flow or quantity, and Munzner's what-why-how reference is prose-served; promoting it would yield a weak 3-box figure that duplicates the prose. Named here as the strongest rejected candidate.
- The visual-standard rules (two-color max, flat fills, no rounded corners, title/desc, axes labeled) are a checklist, not a structure/process/quantity — best as a prose list or appendix scorecard, not a figure. Not proposed.
- Split point: Fig 9.3 is at the 6-node ceiling. If the D3 branch and the source/output divider crowd it, split into two figures — "the three-operation sequence" (Finishing→Suggest→Generate) and "the source-vs-output artifact split" (SVG/D3 vs PNG).
