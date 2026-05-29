# Figure Plan — Chapter 11: Creating Figures

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mechanistic.*

## Figure 11.1 — The component ceiling: seven vs four (Critical, PQ)
**Trigger:** "Miller... fixed in everyone's mind that working memory holds about seven items. The number turned out to be optimistic. Nelson Cowan... put the real capacity at closer to four chunks... Not four thousand. Four." and "**six to eight labeled components per figure, and never more.**"
**Figure type:** statistical/quantitative (two-bar comparison against a shared zero-based axis)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 4 elements — bar for Miller's "7±2" working-memory claim, bar for Cowan's "≈4 chunks" revised capacity, a horizontal threshold line marking the 6-to-8 component ceiling, a shared zero-baseline count axis
- O: two vertical bars side by side on a shared count axis starting at zero; the ceiling threshold drawn as a horizontal reference line crossing both bars so the Cowan bar sits well under it and the Miller bar approaches it
- P: flat vector; Miller bar Sky Blue #56B4E9; Cowan bar Blue #0072B2; threshold line Vermillion #D55E00; axis Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text, no numerals)
- E: do NOT draw brains, heads, or memory-slot icons; no Sweller cognitive-load curve; no split-criteria content; no SCOPE frame; no decorative items
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 11.2 — The SCOPE frame, E carries the weight (Critical, MC)
**Trigger:** "SCOPE is the instrument... the five-part frame CAJAL builds every figure prompt around... S — Specification... C — Content... O — Organization... P — Presentation... E — Exclusions. And this is the parameter that does the work... the exclusion list is more important than the inclusion list."
**Figure type:** structural schematic (stacked five-band frame with one band emphasized)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 elements — five stacked bands, one per SCOPE letter (S, C, O, P, E), with the E band rendered visibly heavier/wider to encode its dominant weight relative to the other four
- O: vertical stack top-to-bottom in fixed S→C→O→P→E order; uniform band heights for S/C/O/P; the E band enlarged (taller or wider) to signal "the parameter that does the work" — proportional emphasis, not just color
- P: flat vector; S/C/O/P bands in a neutral single color Sky Blue #56B4E9; E band Orange #E69F00 for emphasis; band borders Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in letters or words)
- E: do NOT depict the silent/interactive mode gates (that is Figure 11.3); no example SCOPE block text; no palette swatches; no canvas-size diagrams; no arrows (this is a frame, not a flow)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 11.3 — Silent vs interactive mode gates (Important, VG)
**Trigger:** "In **silent mode**, CAJAL infers concept, audience, and components... and returns a clean SCOPE immediately — no questions... In **interactive mode**, it refuses to move until you have answered, in order: what chapter is this for; what is the concept...; what does the reader already know; what are the three-to-eight components; and... what must not appear. It will not generate output while the exclusion list is empty."
**Figure type:** comparison panels (two paths to the same output)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 7 elements — top path: one "silent" node flowing directly to the shared SCOPE-output node (1 node + 1 output); bottom path: five sequential gate nodes (chapter, one-sentence concept, prior knowledge, components, exclusions) flowing to the same shared output, with the final exclusions gate drawn as a hard stop/lock glyph
- O: two horizontal left-to-right tracks converging on one shared output node at the right; top track is a single direct arrow; bottom track passes through five gates in fixed order; the fifth (exclusions) gate is the held-hardest gate, drawn distinctly as a blocking lock (⊣ semantics) until satisfied
- P: flat vector; silent path node Sky Blue #56B4E9; interactive gate nodes Blue #0072B2; the exclusions lock-gate Vermillion #D55E00; shared output node Bluish Green #009E73; arrows Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT include the SCOPE band structure (that is Figure 11.2); no triage signals (MC/VG/PQ); no palette/grayscale content; no worked-example flow; no question prose inside gates
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 11.4 — The worked example: eight-section vertical process flow (Important, MC)
**Trigger:** "A vertical process flow — eight boxes, top to bottom, a single arrow between each... O — Top-to-bottom, one arrow between adjacent boxes. No branches, no loops." and "Eight is at the ceiling, which is the signal to check: is this one figure or two?"
**Figure type:** process flowchart (vertical, single linear sequence — this figure also *demonstrates* a figure at the ceiling)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 8 elements — eight identical section boxes stacked vertically, connected by a single downward arrow between each adjacent pair (the at-ceiling case, deliberately shown to embody the eight-component limit)
- O: strictly top-to-bottom; one arrow (→ rendered downward) between adjacent boxes; no branches, no loops, no return arrows; uniform box size to signal a flat linear sequence
- P: flat vector; first box accented Orange #E69F00 (sequence entry), remaining seven boxes Sky Blue #56B4E9, arrows Black #000000; uniform 1pt strokes; white background; unannotated (box names applied later as typography)
- E: do NOT add a ninth box (a ninth would force the split — that is the teaching point); no icons; no interface screenshots; no pantry or Chapter Writer depiction; no return/loop arrows; no word counts, runtimes, or example prose inside boxes
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. The chapter's lesson is about decided structure and held constraints, not about animating a transition; even the SCOPE process is a frame, not a temporal mechanism the reader must watch evolve.

## Notes
This chapter is self-referential — it teaches the very craft these plans apply — so the figures are chosen to *embody* the rules they illustrate: Figure 11.4 is intentionally exactly at the eight-component ceiling to demonstrate the split-point boundary, and every figure here is unannotated per the chapter's own "no text labels baked into the generated image" rule. The "Two palettes, one rule" section (Okabe-Ito vs Bear Brown/Brutalist D3, plus the grayscale-survival rule) is a strong candidate but was held back: it is genuinely two concepts (palette-selection logic + the luminance-band grayscale test), and a faithful figure would risk baking in color-system specifics that fight the unannotated rule; if added, split into (a) a publisher-neutral-to-house-skin layer diagram and (b) a luminance-ladder grayscale bar. Split point named there. Total: 4 figures.
