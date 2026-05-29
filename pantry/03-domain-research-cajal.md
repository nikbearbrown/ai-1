# Figure Plan — Chapter 3: Domain Research — The Chapter Before the Chapter

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mixed.*

## Figure 3.1 — Three LLM signatures on the same question (Critical, VG)
**Trigger:** Existing comment — "<!-- → [INFOGRAPHIC: three-column side-by-side of the three LLM opening paragraphs, annotated to show the uncertainty-explicit signature (Claude), the confident-enumeration signature (GPT), and the retrieval-grounded signature (Gemini)...] -->" — plus the three quoted opening paragraphs and "Three responses. Same question. Three signatures."
**Figure type:** comparison panels (three-column)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 3 equal columns (Claude / GPT / Gemini), each a text-block panel rendered as bars, with a distinguishing visual signature mark per column: Claude column carries hollow "hedge" markers (uncertainty flags), GPT column carries uniform solid enumerated bars (confident lists, no source ticks), Gemini column carries solid bars with attached source-pin marks (retrieval-grounded). One shared "same question" node feeding all three at top.
- O: one input node at top splitting via three arrows (→) into three side-by-side panels; each panel's distinguishing markers placed in its margin (hedge rings / list ticks / source pins) so the three signatures are visually contrastable without reading text.
- P: flat vector, Okabe-Ito — Claude panel + hedge rings Orange #E69F00, GPT panel + list ticks Sky Blue #56B4E9, Gemini panel + source pins Bluish Green #009E73, shared input node and connectors Black #000000 1pt; white background, unannotated (the quoted paragraph text is NOT reproduced)
- E: do NOT bake in the actual paragraph prose or the model names; do NOT reproduce the 93%/90%/"substantial majority" numbers as legible figures here (that is Fig 3.4 territory / fluency-trap check); do NOT show the four synthesis markers (that is Fig 3.3); do NOT depict the convergence/synthesis step — this panel is signatures only
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 3.2 — Eight-section prompt mapped to Tic TOC intake (Important, VG)
**Trigger:** Existing comment — "<!-- → [TABLE: eight-section prompt schema — three columns: section number, what it asks for, what Tic TOC intake question it feeds — showing how each research section maps to /i2, /i3, /i4, /l1, /m1] -->" — plus the enumerated eight sections and the per-section "what it is for" prose.
**Figure type:** structural schematic (mapping / crosswalk)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 8 source rows (the 8 prompt sections) on the left + their mapping connectors to the named Tic TOC intake targets on the right (/i2, /i3, /i4, /l1, /m1 — 5 targets). 8 left nodes + 5 right nodes = 13 nodes; this exceeds the per-figure component ceiling, so SPLIT POINT named below. Render as a left-column of 8 small uniform section blocks, a right-column of 5 intake-target nodes, and crosswalk lines between them.
- O: left-to-right crosswalk — 8 section blocks stacked on the left, 5 intake-target nodes stacked on the right, thin connector lines (→) showing which section feeds which intake question (a many-to-some mapping; the chapter only loosely specifies these, so any non-stated link is INFERRED — see exclusions).
- P: flat vector, Okabe-Ito — section blocks Blue #0072B2, intake-target nodes Orange #E69F00, crosswalk connectors Black #000000 1pt; white background, unannotated
- E: INFERRED-RELATIONSHIP FLAG: the chapter names the target set (/i2, /i3, /i4, /l1, /m1) but does NOT give a complete section-to-target mapping; the connector lines must be drawn only for mappings the author confirms — do NOT fabricate specific section→gate links beyond what the chapter states. Do NOT bake in section text or gate codes; do NOT reproduce the full prompt; do NOT show the synthesis markers or the funnel (other figures).
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 3.3 — The four synthesis markers (Critical, VG)
**Trigger:** Existing comment — "<!-- → [TABLE: synthesis marker table — four rows, three columns: marker, meaning, what to do...] -->" — plus the defined four markers (ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY) and their overlap semantics across three sources.
**Figure type:** conceptual map (3-source overlap / decision key)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 4 marker states shown as the four distinct regions of a 3-circle overlap: (1) ALL THREE AGREE = central triple-overlap; (2) TWO AGREE = a pairwise-overlap lens; (3) ONE ONLY = a single-circle-only crescent; (4) DIVERGENT = circles drawn with conflicting fill in the same conceptual slot (shown as a separate split/forked marker since divergence is disagreement, not absence of overlap). Use the three source circles as the substrate (4 elements + 3 substrate circles = 7).
- O: three overlapping circles centered; the four marker regions called out with small leader dots to their region (triple-overlap, pairwise lens, single crescent) and a fourth forked-arrow marker beside the cluster for DIVERGENT to show "all positions stated, not merged."
- P: flat vector, Okabe-Ito — source circle A Orange #E69F00, B Sky Blue #56B4E9, C Bluish Green #009E73 (all outline/low-fill so overlaps read); marker leader dots and DIVERGENT fork Black #000000 1pt; white background, unannotated
- E: do NOT bake in marker names or the "what to do" column text; do NOT show the running-example claims (fluency-trap definition, wage premium, junior-pipeline, nemo dat) as content; do NOT depict the funnel compression (Fig 3.4); do NOT label the circles with model names — this is the abstract marker key, source-agnostic
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 3.4 — Compression funnel: 3 outputs → synthesis → /i1 brief (Important, PQ)
**Trigger:** Existing comment — "<!-- → [INFOGRAPHIC: funnel diagram showing the three-LLM outputs (3,000+ words each) compressing into the 600–800 word synthesis, then into the 700–1,400 word four-section /i1 brief...] -->" — plus prose word counts (1,500–3,200 each → 600–800 synthesis → 700–1,400 four-section brief).
**Figure type:** statistical/quantitative + process (proportional funnel)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 4 proportional stages — (1) three input slabs sized to ~3,000+ words each (largest aggregate volume); (2) synthesis stage sized to ~600–800 words (sharp reduction); (3) four-section /i1 brief stage sized to ~700–1,400 words; (4) the four Tic TOC intake questions shown as four small endpoint nodes the brief feeds. Sizes must be honestly proportional to word counts (proportional/quantitative).
- O: left-to-right funnel (→) — three stacked input slabs on the left narrowing into one synthesis block, then into one brief block, then fanning to four question endpoints; widths/areas scaled to the stated word counts so the compression is visually truthful.
- P: flat vector, Okabe-Ito — three input slabs Sky Blue #56B4E9, synthesis block Orange #E69F00, /i1 brief block Bluish Green #009E73, four question endpoints Blue #0072B2, flow lines Black #000000 1pt; white background, unannotated (word-count numbers applied later as typography)
- E: do NOT bake in word-count numbers or the four question texts; do NOT show the 9,000-word source brief as a stage (the chapter explicitly distinguishes it from the /i1 brief — keep it out to avoid conflation); do NOT depict the four synthesis markers inside the funnel (Fig 3.3); do NOT show the fluency-trap verification pass as a stage — it is a check, not a compression step
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. (Fig 3.4 shows compression as proportional area, which a static funnel conveys fully; no transition mechanism needs animating.)

## Notes
- Total figure count: 4.
- SPLIT POINT (Fig 3.2): the eight-section → five-intake-target crosswalk is at/over the component ceiling (13 nodes). If it reads as cluttered, split into two stacked sub-panels (sections 1–4 / sections 5–8) sharing the same right-hand intake-target column, OR demote to the existing markdown table. Also flagged: the section→target mapping is only partially specified in prose — connectors beyond stated links are INFERRED and must be author-confirmed, not fabricated.
- Two-concepts-in-one watch: Fig 3.3 (the abstract four-marker key) and the running-example illustrations of those markers (fluency-trap def, wage premium, junior pipeline, nemo dat — lines 100–110) are distinct. The example claims are best left as prose/the existing Section A–D brief table; do NOT build a second marker figure from them.
- Section A–D distilled brief (lines 142–148) is already richly typeset with inline provenance flags; it is NOT promoted to a figure — it is text whose value is the flags-in-line, and a graphic would lose that.
- The five-minute / three-pattern fluency-trap check (invented citation / conflated finding / precision illusion) is a 3-item list, text-navigable, not figure-worthy.
