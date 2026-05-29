# Figure Plan — Chapter 10: Enrichment for AI

*CAJAL Image Suggest (silent /scan). Density: 4 figures recommended — Mixed.*

## Figure 10.1 — The three-question audit scorecard (Critical, MC)
**Trigger:** "For any LLM Exercise in the book, three questions determine whether it passes... First: could this appear in a different field's textbook unchanged? ... Second: does it require the reader to bring something only they have? ... Third: is the deliverable a judgment the reader produces, not just LLM output?" (plus the existing `<!-- → [TABLE: Three-question audit scorecard ...] -->`)
**Figure type:** statistical/quantitative (decision-gate flow, left-to-right pass/fail)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 elements — three sequential gate nodes (Q1 transplant-test, Q2 reader-brings-something, Q3 deliverable-is-judgment), one "PASS — AI+1 work" terminal node, one "FAIL — generic" sink node
- O: horizontal left-to-right chain of three gates; a passing arrow (→) continues rightward through all three to the PASS terminal; each gate also has a downward blockage stub (⊣) draining to the single shared FAIL sink below the chain. Arrow semantics: rightward = passes that question; downward = fails that question
- P: flat vector; three gate nodes Blue #0072B2; PASS terminal Bluish Green #009E73; FAIL sink Vermillion #D55E00; arrows/strokes Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text)
- E: do NOT show the worked graphic-design examples (those live in the table cells, not this diagram); no Bloom's labels; no Dig Deeper material; no Freire/hooks/Mazur citations; no enrichment-generator phases
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 10.2 — Dig Deeper vs LLM Exercise (Important, VG)
**Trigger:** "A **Dig Deeper** prompt is a short, copy-paste-ready prompt embedded in the chapter prose... It is not optional. It produces a deliverable the reader will reference in a later chapter... Same chapter. Same client brief. Different scaffolding."
**Figure type:** comparison panels (two side-by-side)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 6 elements — two labeled panels (Dig Deeper / LLM Exercise), each carrying three contrast attribute rows aligned across a shared axis: placement (inline vs chapter-end block), obligation (optional vs required), output (no enforced deliverable vs saved artifact feeding the running project)
- O: two panels side by side against a shared horizontal attribute axis so the three rows align for direct row-by-row comparison; left panel = Dig Deeper, right panel = LLM Exercise
- P: flat vector; Dig Deeper panel Sky Blue #56B4E9; LLM Exercise panel Orange #E69F00; shared axis and dividers Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text)
- E: do NOT include the actual prompt prose; no word counts ("250 words") as numerals; no running-project timeline; no chapter-number references; no Bloom's taxonomy
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 10.3 — The enrichment generator, three phases (Critical, MC)
**Trigger:** "It runs in three phases and pauses for judgment between them. **Phase one** detects the book's state... **Phase two** generates Chapter 00... **Phase three** proposes three to five candidate *running projects*... and asks the author to pick one."
**Figure type:** process flowchart (horizontal, with author-judgment pause gates)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 6 elements — three phase nodes (Phase 1 state-detection, Phase 2 Chapter-00 generation, Phase 3 running-project + insertions), two author-judgment pause markers sitting on the arrows between phases, one terminal node (AI+1 textbook at pedagogy layer)
- O: horizontal left-to-right; phase node → pause marker → phase node → pause marker → phase node → terminal. Arrow (→) = progression; the pause markers are distinct small interrupt glyphs on the connecting arrows signalling "stop for judgment"
- P: flat vector; three phase nodes Blue #0072B2; pause markers Yellow #F0E442; terminal node Bluish Green #009E73; arrows Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text)
- E: do NOT enumerate the three state possibilities inside Phase 1 (flat/subfolder/elsewhere); no failure-mode callouts; no Chapter 00 internal sections; no TOC depiction; no Dig-Deeper-vs-Exercise distinction (that is Figure 10.2)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 10.4 — Audit pattern table (Important, VG)
**Trigger:** Existing `<!-- → [TABLE: Audit pattern table — columns: Pattern name, Diagnostic symptom, Diagnosis, Fix — rows for interchangeable, Claude-documentation, no-deliverable] -->`, supported by "Three failure patterns become visible that are invisible chapter by chapter."
**Figure type:** annotated example (matrix / structured table — render as blank ruled grid only)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 7 elements — one header row band + three labeled pattern rows (interchangeable, Claude-documentation, no-deliverable), each row visually tagged by a left-edge color swatch to distinguish the three patterns; the grid carries four empty column slots (symptom/diagnosis/fix populated later as typography)
- O: vertical stack of three rows under one header band; columns run left-to-right; the diagnostic→diagnosis→fix columns read as a left-to-right resolution progression
- P: flat vector; row tags use Reddish Purple #CC79A7 (interchangeable), Sky Blue #56B4E9 (Claude-documentation), Orange #E69F00 (no-deliverable); grid lines and header band Black #000000; uniform 1pt strokes; white background; unannotated (no baked-in text)
- E: do NOT bake in the cell prose; no example exercises; no three-question audit content (that is Figure 10.1); no enrichment-generator phases
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. Each maps to a structural or comparative state, not a transition mechanism the reader must watch unfold.

## Notes
The Chapter 00 four-section breakdown (with the 80/15/5/Cowork tool distribution) is a genuine PQ candidate but was held back to keep the chapter at 4 figures and avoid competing with Figure 10.3's generator focus; if a fifth figure is wanted, a four-bar tool-distribution chart (Claude-chat 80%, Project 15%, Code 5%, Cowork) is the strongest Supplementary add, y-axis from zero. The "two kinds of LLM-integrated content" section is genuinely two concepts braided (placement + the running-project handoff); Figure 10.2 deliberately splits off only the placement/obligation/output contrast and excludes the running-project chain. Total: 4 figures.
