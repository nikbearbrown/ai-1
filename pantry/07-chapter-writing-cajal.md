# Figure Plan — Chapter 7: Chapter Writing — The Cowork Draft Run

*CAJAL Image Suggest (silent /scan). Density: 3 figures recommended — Mechanistic.*

## Figure 7.1 — The five Cowork failure modes (Important, VG)
**Trigger:** "The Chapter Writer does five things... The five failure modes below are what happens when the voice slips." Each mode is named with a diagnostic test and an upstream signal (the chapter's own embedded comment requests this as a TABLE). The reader cannot see the parallel three-part structure (mode / diagnostic / upstream signal) from prose spread across five separate sections.
**Figure type:** hierarchy/taxonomy
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 stacked rows — (1) Voice drift, (2) Fabricated specificity, (3) Missing domain judgment, (4) Padded middle, (5) Bridge questions that don't bridge. Each row has three cells corresponding to the three named attributes per mode (mode / diagnostic test / upstream signal). The sixth "sycophancy" mode is excluded — see E.
- O: vertical stack of 5 rows, three columns left-to-right within each row; uniform row height; thin rules between rows only (no column chrome)
- P: flat vector, two-color subset of Okabe-Ito — row labels/structure in Black #000000, the right-most "upstream signal" column tinted Orange #E69F00; uniform 1pt strokes; white background; unannotated (no baked-in text — blank cells sized to receive typography later)
- E: do NOT include the sixth (sycophancy) mode — it is explicitly off the official list; do NOT include the `[verify]` flag mechanism, the BLOCKED-chapter causes, or the worked-example annotations; no icons or illustrative imagery per mode
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 7.2 — The Chapter Writer's five-step read-then-draft sequence (Important, MC)
**Trigger:** "The Chapter Writer does five things for every undrafted chapter, in order." The chapter then lists: reads TIKTOC.md → reads book.md → audits chapters/ (idempotency, leaves finished work alone) → reads the chapter pantry file → drafts in Attenborough × Feynman voice. This is a 5-step interdependent process whose ordering and idempotency check cannot be verified from the run-on prose sentence.
**Figure type:** process flowchart
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 sequential nodes — (1) read TIKTOC.md, (2) read book.md, (3) audit chapters/ + skip existing, (4) read pantry file, (5) draft. One branch glyph at node 3 indicating the idempotency skip (existing chapter → left untouched).
- O: horizontal left-to-right flow, single arrow (→) between each node; node 3 has one short downward branch arrow representing "skip / leave alone" returning out of the main flow
- P: flat vector, Okabe-Ito — main-flow nodes Blue #0072B2, the read-source nodes (1,2,4) Black #000000 outlines, the idempotency-skip branch Vermillion #D55E00; uniform 1pt strokes; white background; unannotated
- E: do NOT depict the four-move voice spec (scene/first-principles/trade-offs/scale) — that is a separate concept; do NOT show the failure modes, the `[verify]` flag, or the three-layer Skills/Plugins/folder architecture; no model-internal "attention" depiction
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 7.3 — The three responses to a `[verify]` flag (Supplementary, MC)
**Trigger:** "When you find a `[verify]` flag, you do one of three things: verify and replace... verify and remove... or leave for later with a note. What you do not do is delete the flag and keep the sentence." A branch decision with three valid outputs plus one explicitly forbidden output — the forbidden branch is the load-bearing claim and is hard to see in prose.
**Figure type:** process flowchart (branch/decision)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 1 decision node (flag found) → 3 valid output branches (replace with citation / remove sentence / convert to tracked note) + 1 forbidden branch (delete flag, keep sentence) shown with a blockage glyph (⊣)
- O: single source node on the left; four branches fanning right; the three valid branches as plain arrows (→), the fourth branch terminated with a blockage symbol (⊣) to mark it forbidden
- P: flat vector, Okabe-Ito — source node Black #000000, three valid branches Bluish Green #009E73, the forbidden branch Vermillion #D55E00 ending in the ⊣ blockage; uniform 1pt strokes; white background; unannotated
- E: do NOT depict why zero flags is suspect (separate claim), the Bansal uncertainty-annotation finding, or the BLOCKED-chapter logic; no example draft text
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. The failure-mode taxonomy and the verify-flag branch are state/structure, not transition mechanisms; the five-step sequence is a fixed order, not an animated process whose timing is the learning target.

## Notes
- Total: 3 figures (1 from the chapter's own embedded TABLE comment, 2 newly detected).
- The chapter's embedded comment `<!-- → [TABLE: five failure modes summary...] -->` is folded in as Figure 7.1; its requested third column ("upstream signal") is honored.
- Two-concepts-in-one watch: the failure-mode list (Fig 7.1) and the Attenborough×Feynman four-move voice spec are distinct concepts and must not be merged into one figure. The four-move voice spec was triaged but NOT proposed — it is four parallel testable attributes with no process ordering or quantity, so prose plus the existing scene/first-principles labels carries it; promoting it would be a weak figure.
- Split point if Fig 7.1 grows: if the sycophancy note is ever added as a sixth row, split into "official five" and "additional one" rather than a 6-row table.
- The `log.csv` of 14 green rows is quantitative-looking but is an artifact reproduced verbatim in the prose; a figure would duplicate it (chartjunk). Deliberately not proposed.
