# Figure Plan — Chapter 5: Book Scaffold: `new_book.py`

*CAJAL Image Suggest (silent /scan). Density: 3 figures recommended — Mixed.*

## Figure 5.1 — The scaffold directory tree by audience (Critical, VG)
**Trigger:** The chapter prints a full directory tree for `ai-for-designers/` with every file tagged [Cowork], [Human], or [Build], and the existing comment "<!-- → [TABLE: three-audience directory map ...] -->". This is the strongest VG candidate in all three chapters: a hierarchical/spatial claim (which files nest where, and which of three audiences owns each) that prose cannot verify. The chapter explicitly says "Commit the three-color taxonomy to memory."
**Figure type:** hierarchy/taxonomy (annotated directory tree, color-coded by audience)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: a file tree with the root folder plus its top-level entries, color-coded into exactly 3 audience classes. To stay under 8 visible components, GROUP rather than enumerate all 19 entries: (1) root node, (2) Cowork-facing cluster (TIKTOC.md, book.md, pantry/), (3) Human-facing cluster (vision/architecture/chapters-spec/risks/outline/README), (4) Build-facing cluster (metadata.yaml, build.sh, images/, d3/, styles/, output/, _working/), (5) chapters/ as a shared node (Cowork-writes / Build-reads). 5 grouped components.
- O: vertical tree, root at top, indented children; nodes grouped and tinted by audience; a small dual-tint marker on the chapters/ node to show it is read by two audiences
- P: flat vector, Okabe-Ito — Cowork files Blue #0072B2, Human files Bluish Green #009E73, Build files Orange #E69F00, root/structure lines Black #000000, the dual-audience chapters/ node split Blue #0072B2 + Orange #E69F00; uniform 1pt strokes; white background; unannotated (filenames applied later in typesetting)
- E: do NOT bake in filenames; do NOT show the inner chapter .md files (00-frontmatter … 99-back-matter) — that internal numbering is Figure 5.3's subject; do NOT depict metadata.yaml field contents; do NOT use red-green; do NOT show the new_book.py command syntax here
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 5.2 — TIKTOC.md → new_book.py → directory (Important, MC)
**Trigger:** "`--tiktoc` points to the TIKTOC.md ... The script reads it ... These become the scaffold's structural commitments" and "The directory is not the output of the script; it is the output of the conversation with Tic TOC, made legible as a filesystem." Two-argument interface (--tiktoc, --slug) producing a directory. This is a 3-stage transform the reader must see as input → process → structured output.
**Figure type:** process flowchart
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: exactly 5 elements left-to-right — (1) TIKTOC.md spec document (input), (2) the --tiktoc and --slug arguments as two small input prongs feeding (3) the new_book.py process node, arrow to (4) the generated directory (folder node), plus (5) a small "refuses to overwrite" guard loop marked on the process node. 5–6 elements.
- O: horizontal left-to-right; solid → arrows for the main flow; the two arguments enter the process node from below as short prongs; the idempotency guard shown as a small self-return arc on the process node
- P: flat vector, Okabe-Ito — TIKTOC.md input Blue #0072B2, the two argument prongs Sky Blue #56B4E9, process node Black #000000, generated directory Bluish Green #009E73, guard arc Vermillion #D55E00; uniform 1pt strokes; white background; unannotated
- E: do NOT show the directory contents in detail (that is Figure 5.1); do NOT depict the Python install steps (Mac/Windows/Linux); do NOT show the build.sh pipeline (Chapter 12 / not this figure); do NOT include the Cookiecutter reference visual
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Figure 5.3 — Chapter filename order = EPUB build order (Important, VG)
**Trigger:** "The numbering prefix is not decoration: `01-`, `02-`, `03-` is the concatenation order that becomes the EPUB's chapter order. Change the number, change the position in the book." Reinforced by build.sh: "`cat chapters/*.md > _working/combined.md` ... every file in chapters/ is glued together in filename order." This is a sequence/ordering claim — that lexical filename order deterministically maps to final book position — that prose states but cannot show.
**Figure type:** structural schematic (ordered sequence → concatenation)
**SCOPE**
- S: single-column 89mm, 300 DPI, flat vector
- C: 6 ordered file tiles (00-frontmatter, 01, 02, ... , 99-back-matter — use 5 numbered tiles + 1 ellipsis tile to imply the full set) on the left, an arrow into a single concatenated stack/document on the right representing combined.md → EPUB. 6–7 elements.
- O: vertical ordered list of numbered tiles on the left (top-to-bottom = ascending prefix), a → arrow into a single stacked-page block on the right; the stack's internal divisions mirror the tile order to make the order-preservation visible
- P: flat vector, Okabe-Ito — file tiles Bluish Green #009E73, the ellipsis/implied-set tile lower-saturation Sky Blue #56B4E9, concatenation arrow Black #000000, output EPUB stack Orange #E69F00; uniform 1pt strokes; white background; unannotated
- E: do NOT bake in filenames or numbers; do NOT show pandoc flags or metadata.yaml; do NOT depict the PDF/xelatex branch (keep to the order-preservation idea only); do NOT show the three-audience coloring here (that is Figure 5.1 — chapters/ is one audience-node there, expanded into sequence here)
**Negative prompt:** text labels, words, gibberish letters, titles, captions, decorative borders, drop shadows, gradient backgrounds, 3D perspective, red-green combinations, rainbow scales, hand-drawn styles, watermarks

## Video candidates
None — all figures are well-served static. The TIKTOC → directory generation (Figure 5.2) is a one-shot transform with no intermediate states worth animating; the before/after (no folder → folder) is fully carried by the static input→output flow.

## Notes
- Figure 5.1 is the chapter's spine and the highest-priority figure across all three chapters: the entire chapter's thesis ("once you can see the three audiences, the rest reads itself") is a taxonomy that is far easier to verify visually than in a printed tree. Grouping (not enumerating all 19 entries) is the named split point that keeps it under the 6–8 component cap.
- The metadata.yaml (11 fields) and build.sh (code block) are code/config listings, not figure candidates — left as typeset code. No CAJAL figure for them.
- The Nygaard "programs are models of the world" idea and the literate-programming split are conceptual framings already embodied by Figure 5.1's audience coloring; no separate conceptual-map figure needed (would duplicate 5.1).
- Split point: chapters/ deliberately appears as a single grouped node in 5.1 and is expanded into an ordered sequence in 5.3 — this is the intended division of one concept (the chapters folder) across two figures, each making a different claim (audience vs. order).
- Total CAJAL figure count: 3.
