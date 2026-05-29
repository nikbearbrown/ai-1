# `pantry/cowork.md` — what relates to the chapters, what doesn't

The file is a 7,059-line bundle of reusable Cowork/Codex prompts, templates, and sample content for the textbook pipeline. Several blocks appear **twice**. Line numbers below point into `cowork.md`.

## Relate to the chapters (produce, edit, or verify chapter content)

These act *on the book's chapters* — drafting prose, generating exercises, or checking claims.

- **Chapter Research Gatherer** (L2816) — collects source material per chapter.
- **Chapter Research Pass** (L3184) — research workup per chapter; feeds the writer.
- **Attenborough × Feynman conversion + `/write` 8-section structure** (L1292–1649) — the rewrite engine: turns source subfolders into finished chapters. This is the core chapter-writing spec.
- **Chapter Writer** (L3661) — authors a chapter from research.
- **Running Project Exercise Generator** (L4769) — end-of-chapter running-project exercises.
- **"With LLMs" Curriculum Enrichment Generator** (L4909, dup L6131) — generates the end-of-chapter LLM exercises.
- **Add "A Note about AI" to a Chapter** (L6055) — inserts a chapter-level callout when warranted.
- **Assertions Report / Master Fact-Check Report** (L4163, L4234) — QA on chapter claims.

## Relate to chapters, but as the *visual/figure layer* (not the prose)

Chapter-bound, but about figures/tables/images rather than the writing itself.

- **"image suggest"** (L2, dup L1650) — generate a per-chapter CAJAL figure-suggestion report into `pantry/`.
- **Chapter Enrichment: Tables and Figures** (L2491, dup-variant L5733) — iterates `chapters/`, turning `[TABLE:]`/`[IMAGE:]` comments into rendered tables, SVG/PNG figures, and D3 HTML.

## Don't relate to the chapters (generic tooling or non-chapter content)

- **CAJAL — Figure Intelligence Command Set** (L10, dup L1658) — a discipline-agnostic figure-architect system prompt. Reusable across any book; not tied to AI+1's chapters.
- **SVG Style Guide, Okabe-Ito palette, publisher-style reference, PNG-conversion / build mechanics** (within L1124–1290, L2358–2490) — production styling and build plumbing.
- **Front/back-matter samples, not chapters:** `[BOOK TITLE]` copyright page (L4298), Introduction skeleton (L4364), Nik Bear Brown author bio (L4521), Errata (L4758), `[Book Title]` blurb template (L6381).
- **Pure templates / stubs** (output scaffolds, not prompts): Pantry (L1534), Figure briefs (L1562), Source map (L1580), Research Notes (L2985, L3274), Pantry Index (L3108).

## Notable: the file is duplicated

`image suggest`, `CAJAL`, the Tables-and-Figures enrichment, and the "With LLMs" generator each appear twice. Worth splitting this into separate prompt files (or at least de-duping) so the pantry is navigable.
