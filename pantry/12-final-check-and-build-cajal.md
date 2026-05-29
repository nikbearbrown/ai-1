# Figure Plan — Chapter 12: Final Check and Build: EPUB + PDF

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mixed.*

## Figure 12.1 — The four-step ship sequence (Critical, VG)
**Trigger:** "Four things, in order. Run the Fact-Checking Assistant... Run `./build.sh`... Read the EPUB on a device... Submit to KDP. Then accept that you will rebuild. The rebuild loop is not a failure of the pipeline. It is the pipeline."
**Figure type:** process flowchart (horizontal sequence closing into a rebuild loop)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 elements — four sequential step nodes (fact-check, build, device-read, submit) plus one return arc from the end back to an earlier step encoding the rebuild loop
- O: horizontal left-to-right through the four steps with a single forward arrow (→) between each; one curved return arc from the final node back to the build step, drawn distinctly to mark the loop is intentional, not an error
- P: flat vector; four step nodes Blue #0072B2; the rebuild return arc Orange #E69F00; forward arrows Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT show fact-check claim types or statuses (that is Figure 12.2/12.3); no KDP form fields; no version numbers; no device illustrations; the loop is a single arc only — do not multiply it into a tangle
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 12.2 — Fact-check classification: claim type × content category (Important, VG)
**Trigger:** "The Fact-Checking Assistant scans every chapter file and classifies every assertion along two dimensions: what kind of claim it is, and what the claim is about." (five claim types: basic, emphatic, positive, I-language, combination; six content categories: STAT, GUIDELINE, APPROVAL, EVIDENCE, SPECIALIST, CURRENT)
**Figure type:** structural schematic (two-axis classification grid — render as blank ruled matrix)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector — NOTE: 5×6 = 30 cells exceeds the component ceiling for *labeled* parts; render as an empty two-axis grid (5 row slots × 6 column slots) where only the two axes and the grid are the components, not 30 labeled cells. Labels applied later as typography.
- C: exactly 3 structural elements — one vertical axis band (5 claim-type rows), one horizontal axis band (6 content-category columns), and the empty intersection grid they define
- O: claim types stacked as rows down the left vertical axis; content categories as columns across the top horizontal axis; the body is an empty intersection matrix (the cross-classification space)
- P: flat vector; row axis band Sky Blue #56B4E9; column axis band Bluish Green #009E73; grid lines Black #000000; uniform 1pt strokes; white background; unannotated (no category names or cell content baked in)
- E: do NOT pre-fill any cells; no example claims; no four-status triage (that is Figure 12.3); no citations (Smith/Canby); do not attempt to label all 30 cells — this is the split point, the matrix stays blank
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 12.3 — The four-status triage order (Important, MC)
**Trigger:** "Every assertion returns one of four statuses: VERIFIED, OUTDATED, CONTRADICTED, or UNVERIFIED. You triage in that exact order, because the order tracks both urgency and effort. OUTDATED first... CONTRADICTED second... UNVERIFIED third..."
**Figure type:** timeline/progression (ordered priority queue, left-to-right)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 4 elements — the four status nodes in triage order: OUTDATED, CONTRADICTED, UNVERIFIED, and VERIFIED (VERIFIED set aside as the no-action terminal). Arranged so the three actionable statuses sit in the priority sequence and VERIFIED is visually separated
- O: horizontal left-to-right priority order OUTDATED → CONTRADICTED → UNVERIFIED, each connected by a progression arrow; VERIFIED placed off the action track (e.g., to the side or below) as the resolved state requiring no triage
- P: flat vector; OUTDATED Vermillion #D55E00 (fastest/most embarrassing), CONTRADICTED Orange #E69F00, UNVERIFIED Yellow #F0E442, VERIFIED Bluish Green #009E73; arrows Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT include the example claims (KDP cover spec, Pandoc EPUB 3.3, 80% indie units); no claim-type/content-category matrix (Figure 12.2); no `<!-- FACT-CHECK FLAG -->` depiction; no urgency/effort axes drawn as gradients — order is encoded by left-to-right position only
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 12.4 — KDP royalty tiers by price (Important, PQ)
**Trigger:** "The KDP royalty structure: books priced between $2.99 and $9.99 earn 70%. Outside that range — including $0.99 — 35%. At $0.99 you keep about $0.35 per sale." and the $0.99 series-price decision.
**Figure type:** statistical/quantitative (step function of royalty rate across price, zero-based)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 elements — a royalty-rate y-axis (starting at zero), a price x-axis, the 35% band below $2.99, the 70% band between $2.99 and $9.99, the 35% band above $9.99, and a single marker at the $0.99 series price sitting in the low band
- O: x-axis = list price increasing rightward; y-axis = royalty percentage from zero; a step-function profile rising from 35% into the 70% middle band then dropping back to 35%; the $0.99 decision marked as a point in the leftmost low band
- P: flat vector; 70% middle band Bluish Green #009E73; the two 35% bands neutral Sky Blue #56B4E9; the $0.99 marker Vermillion #D55E00; axes Black #000000; uniform 1pt strokes; white background; unannotated (no numerals baked in)
- E: do NOT depict KDP Select exclusivity, KU page-reads, or Countdown Deals; no SemVer/version content; no submission-checklist fields; no Authors Guild/Penn/Shatzkin debate; no 3D
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. The rebuild loop (Figure 12.1) is the closest to a "transition" but its learning target is the *structure* of the loop (it returns; that is normal), not an animated state change, so the single return arc carries it.

## Notes
Two strong candidates were deliberately held back to keep to 4 and avoid weak figures. (1) The existing `<!-- → [TABLE: KDP submission checklist ...] -->` is a real candidate but is a five-row reference table best served as native typography, not a vector schematic — flagged here as a typeset table, not a CAJAL image. (2) SemVer (MAJOR.MINOR.PATCH with the patch/minor/major examples) is a clean PQ/VG candidate but is well-served by prose plus the eventual checklist; if a fifth figure is wanted, a three-tier version-bump ladder is the strongest add. Figure 12.2 is the chapter's one component-ceiling pressure point: 5 claim types × 6 content categories = 30 intersections, which is why it is scoped as a *blank two-axis grid* (3 structural components) with all 30 cells left empty for later typography — the split point is "do not label the cells in the image." Total: 4 figures.
