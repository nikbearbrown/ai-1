# Figure Plan — Chapter 4: Tic TOC: Generating Your TIKTOC.md

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mechanistic.*

## Figure 4.1 — The three-phase Tic TOC pipeline (Critical, MC)
**Trigger:** The chapter is structured as three sequential phases gating into the /g2 handoff — "Phase One: what you actually know" (four commands /i1–/i4), "Phase Two: the pedagogical spine" (/l1–/l4), "Phase Three: the chapter that Cowork will actually draft" (/c1–/c4), feeding the /g2 diagnostic gate to Cowork. The reader must see that the commands are not a flat menu but three gated stages each producing an artifact the next consumes.
**Figure type:** process flowchart
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 nodes left-to-right — (1) Phase One block, (2) Phase Two block, (3) Phase Three block, (4) /g2 diagnostic gate (diamond), (5) Cowork handoff terminal. Each phase block carries 4 small command sub-ticks (i1–i4, l1–l4, c1–c4) as plain unlabeled marks.
- O: horizontal left-to-right flow; solid arrows between phases (→ progression); the /g2 gate is a decision diamond with a return-loop arrow back to the relevant phase (re-run path) and a forward arrow to handoff
- P: flat vector, Okabe-Ito palette — Phase One block Blue #0072B2, Phase Two block Bluish Green #009E73, Phase Three block Orange #E69F00, /g2 gate Vermillion #D55E00, Cowork terminal Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text)
- E: do NOT show the contents of any single command's exchange; do NOT depict the Cowork drafting internals; do NOT show the downstream book-scaffold directory (Chapter 5); do NOT include the 10–100x cost-ratio concept here
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 4.2 — Capability statement: topic vs. demonstrable outcome (Important, MC)
**Trigger:** The /i1 exchange iteratively sharpens "The reader learns to use AI in their freelance design practice" (topic) through four turns into "identify which design decisions must stay human and which can be delegated to AI — and to defend that delegation map to a client" (confirmed capability). Reinforced by Mager's three-part criterion: performance, condition, criterion. This is a sequence claim — a refinement ladder — that prose alone makes hard to track.
**Figure type:** timeline/progression
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 4 stacked refinement rungs ascending left-to-right (vague topic → adds constraint → adds action → confirmed capability), plus 3 small criterion checkmarks attached to the final rung representing Mager's performance / condition / criterion. 5–7 elements total.
- O: ascending staircase progression left-to-right; each rung connected by a → arrow; the three Mager criteria branch off the top rung as short stubs
- P: flat vector, Okabe-Ito — rung 1 (topic) Reddish Purple #CC79A7, intermediate rungs Yellow #F0E442 then Sky Blue #56B4E9, final confirmed rung Bluish Green #009E73, the three Mager stubs Black #000000; uniform 1pt strokes; white background; unannotated
- E: do NOT render the actual sentence text; do NOT show the /i2–/i4 commands; do NOT include the reader-persona (Maya) discussion from /i3; do NOT depict Bloom's levels here (that is Figure 4.3)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 4.3 — Bloom's verb ceiling for a practitioner handbook (Important, PQ)
**Trigger:** "/l1 ... three to five learning outcomes per chapter, each tagged with a Bloom's level ... Remember, Understand, Apply, Analyze, Evaluate, Create." The chapter makes a quantitative/ordinal claim: Understand is a "low-ceiling verb," Apply is "the working floor," Evaluate and Create are "high-judgment ceilings," and "no chapter with an outcome below Apply as its ceiling." This is a ranked threshold claim the reader cannot verify from prose order alone.
**Figure type:** statistical/quantitative
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 6 vertical bars of increasing height, one per Bloom's level (Remember, Understand, Apply, Analyze, Evaluate, Create), with a single horizontal threshold line drawn at the Apply level marking the "working floor." 7 elements (6 bars + 1 floor line).
- O: 6 bars left-to-right in taxonomy order, ascending height = cognitive ceiling; y-axis baseline at zero; one horizontal rule across all bars at the Apply position; bars below the floor line visually distinct (lower saturation) from bars at/above
- P: flat vector, Okabe-Ito — bars below floor (Remember, Understand) Sky Blue #56B4E9; bars at/above floor (Apply, Analyze, Evaluate, Create) Blue #0072B2; threshold floor line Vermillion #D55E00; uniform 1pt strokes; white background; y-axis starts at zero; unannotated
- E: do NOT bake in the verb names; do NOT show the per-chapter Create-level distribution table (that is a separate TABLE candidate noted below); do NOT depict the ai-for-designers chapter titles; no 3D bars
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 4.4 — The /g2 failure-mode × chapter diagnostic grid (Critical, VG)
**Trigger:** Existing comment "<!-- → [TABLE: The /g2 failure mode table ... all seven failure modes × all seven chapters, with warning cells highlighted ...] -->" plus the in-text 7×7 PASS/WARN matrix showing "Five WARNINGS. Zero FAILs." This is a structural/spatial claim — seven failure modes read against seven chapters, five specific warning cells — that cannot be verified from prose.
**Figure type:** structural schematic (heatmap-style grid, status-coded)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: a 7-row × 7-column grid (49 cells); 5 cells flagged as WARN, the remaining 44 as PASS, zero FAIL. Two cell states only (PASS vs WARN). The 5 WARN cells positioned per the chapter's table: Audience-drift×Ch5, Over-claimed×Ch3, Contested-claims×Ch1, Bridge-fails×Ch6, and one additional per source (note: source text lists 5 warnings but the prose summary names 4 — see Notes).
- O: matrix layout, rows = failure modes (top to bottom), columns = chapters (left to right); WARN cells filled solid, PASS cells outline-only; thin grid rules
- P: flat vector, Okabe-Ito — PASS cells white fill / Black #000000 1pt outline; WARN cells Orange #E69F00 fill; grid lines Black #000000 uniform 1pt; white background; unannotated (no row/column headers baked in)
- E: do NOT bake in failure-mode names or chapter numbers; do NOT use red or green for status (per palette rule); do NOT show the one-line diagnostics; do NOT depict the resolution/re-run loop (that is captured in Figure 4.1's gate)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. The /g2 re-run loop in Figure 4.1 is a state transition, but the learning target is the gate logic (resolve-or-log), not an animated mechanism; a static decision diamond carries it.

## Notes
- Discrepancy flagged for the author, NOT invented in the figure: the chapter's /g2 table caption says "Five WARNINGS" and the cells show five WARN entries (Ch5 audience-drift, Ch3 over-claim, Ch1 contested, Ch6 bridge, Ch3 over-claimed appears once) — but the resolution sentence and Exercise 3 enumerate only four warnings. Figure 4.4 should follow the matrix cells (five), and the count mismatch is a text issue, not a figure decision.
- The "rushed vs. honored" Cowork-output spread (existing IMAGE comment at line 160) is intentionally NOT promoted to a CAJAL figure: it is two prose paragraphs side by side, i.e. typographic/editorial content, not a diagram. Same for the side-by-side spec entries. These are layout calls, not figure-intelligence calls.
- Two TABLE comments (Phase One output summary, line 63; Bloom's ceiling distribution, line 88) are genuine tables, not figures — left to the author's typesetting, not rendered as vector art.
- One concept that is arguably two: Figure 4.2 fuses the refinement ladder with Mager's three criteria. If it crowds past 7 elements in production, split at the Mager stubs into a tiny separate inset.
- Total CAJAL figure count: 4.
