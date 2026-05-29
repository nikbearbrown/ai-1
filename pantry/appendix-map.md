# AI+1 — Chapter → Appendix Map

The book is a pipeline. Each chapter teaches one stage, and each stage runs on a concrete artifact — a **prompt** you paste into a project, or a **script** you run. The appendices hold those artifacts so a reader can copy the tool instead of reconstructing it from the prose.

Numbering runs in chapter order and starts at **88**, so the last appendix lands before `99-back-matter.md` (99 is reserved for back matter; 98 is left spare).

## The map

| Ch | Chapter | Tool it teaches | Kind | Appendix (file) | Source |
|----|---------|-----------------|------|-----------------|--------|
| 1 | What AI+1 Is | the whole pipeline (no single tool) | — | *none* — points to the appendix list / `textbook-pipeline-sequence.md` | — |
| 2 | What Tic TOC Does | Tic TOC | prompt | **A** (`88-appendix-tiktoc.md`) ✅ exists | Appendix A |
| 3 | Domain Research | Domain Research Prompt (multi-LLM) | prompt | **B** (`89-appendix-domain-research.md`) | `pantry/ai-for-designers-research-prompt.md` (worked example → generalize) |
| 4 | Generating Your TIKTOC.md | Tic TOC | prompt | **A** (shared with Ch 2) ✅ | Appendix A |
| 5 | Book Scaffold | `new_book.py` | **script** | **C** (`90-appendix-scaffold.md`) | `pantry/new_book.py` |
| 6 | Research Pass | Research Gatherer + Research Pass | prompt(s) | **D** (`91-appendix-research-pass.md`) | `cowork.md` L2816, L3184 |
| 7 | Chapter Writing | Chapter Writer (+ A×F conversion) | prompt | **E** (`92-appendix-chapter-writer.md`) | `cowork.md` L3661 |
| 8 | The Human Rewrite | Combined Test checklist — **no generator** | checklist + cross-ref | **F** (`93-appendix-combined-test.md`) | Ch 8 / `_lib_combined-test.md`; cross-references the **AI for Writing** companion book |
| 9 | Finishing Pass & Figures | Finishing Pass + CAJAL Image Suggest | prompt(s) | **G** (`94-appendix-finishing-figures.md`) | `cowork.md` finishing pass + image suggest |
| 10 | Enrichment: LLM Layer | "With LLMs" Enrichment + Running Project + AI Wayback generators | prompt(s) | **H** (`95-appendix-enrichment.md`) | `cowork.md` L4769, L4909 + Deep Research & When-to-Use prompts |
| 11 | Creating Figures | CAJAL Figure Intelligence Command Set + SVG Style Guide | prompt | **I** (`96-appendix-cajal.md`) | `cowork.md` L10 + SVG style guide L1134 |
| 12 | Final Check & Build | Fact-Checking Prompt | prompt | **J** (`97-appendix-factcheck.md`) ✅ exists — *move from `91-`, retitle B→J* | Appendix B today |

```
88  A — Tic TOC                    (Ch 2, 4)   ✅ exists (renamed from 90)
89  B — Domain Research            (Ch 3)
90  C — Scaffold script new_book.py(Ch 5)
91  D — Research Gatherer + Pass   (Ch 6)
92  E — Chapter Writer             (Ch 7)
93  F — Combined Test checklist    (Ch 8)      + AI for Writing cross-ref
94  G — Finishing Pass + Image Suggest (Ch 9)
95  H — LLM Enrichment generators  (Ch 10)
96  I — CAJAL + SVG Style Guide    (Ch 11)
97  J — Fact-Checking Prompt       (Ch 12)     ✅ exists (move from 91)
98  (spare)
99  back matter
```

## Notes

**Chapter 8 is the deliberate gap.** It is the one stage with no generator — the human rewrite is the book's whole argument in miniature. Its appendix is the fourteen-item Combined Test *checklist* (canonical list belongs in `_lib_combined-test.md`), and it points readers to the **AI for Writing: A Practitioner's Guide** companion for the craft itself — the same move Ch 9 makes toward *AI for Graphs* and *AI for Infographics*.

**Scripts: list-and-explain, don't dump.** `new_book.py` (Ch 5) is the one script central enough to reproduce. The shared utilities — `SCRIPTS/svg-to-png.mjs` and `graphs.sh` (Chs 9, 11) and `build.sh` (Ch 12) — are better given a short "what it does / how to run it / repo path" entry than pasted in full, since code ages faster than prose. These can ride inside their chapters' appendices (G, I, J) rather than taking their own slots.

**Each appendix follows the Appendix A pattern:** a short intro (what it is, which chapter sends you here, where the maintained copy lives online), then the verbatim artifact with headings demoted one level so the EPUB TOC stays clean.

## Current state

- **A (Tic TOC)** — exists, renamed `90-` → `88-`. ✅
- **J (Fact-Checking)** — exists as `91-appendix-factcheck.md`, titled "Appendix B." On full build it moves to `97-` and is retitled **Appendix J**, and Ch 12's "Appendix B" reference updates to "Appendix J."
- **B–I** — not yet built. Sources identified above.
