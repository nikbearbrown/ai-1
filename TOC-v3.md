# AI+1 — TOC v3 (two-part structure)

*Placeholders are on disk. Rename, cut, or reorder freely — nothing here is drafted yet except where noted.*

**Source of truth:** `chapters/*.md`. Every output (`.epub`, `.pdf`, `.imscc`, `.apkg`, `.mdx`/`.tsx`, Medhavy) is a build artifact. The author never hand-writes any of them.

---

## Front matter
- `00-frontmatter.md` · `00-introduction.md`

## PART 1 — Make the Book
*How to use Cowork or Codex to produce a new AI+1 book — or adapt an existing one. The pipeline, unchanged. (Two threads to weave in: Codex as an alternative to Cowork, and the "adapt an existing AI+1 book" path. Neither needs a new chapter unless you want one.)*

| # | Chapter | Status |
|---|---|---|
| 1 | What AI+1 Is and Why It Works | drafted |
| 2 | What Tic TOC Does | drafted |
| 3 | Domain Research | drafted |
| 4 | Generating Your TIKTOC.md | drafted |
| 5 | Book Scaffold | drafted |
| 6 | Research Pass | drafted |
| 7 | Chapter Writing: the Cowork (or Codex) Draft Run | drafted |
| 8 | The Human Rewrite | drafted |
| 9 | Finishing Pass and Figures | drafted |
| 10 | Enrichment: The LLM Layer | drafted |
| 11 | Creating Figures | drafted |
| 12 | Final Check and Build: EPUB + PDF → Kindle | drafted |

Part 1 ends where the book ships to Kindle.

## PART 2 — The Enriched Layer
*What these things are and why you should care. Heavy on the unfamiliar artifacts, light on the familiar ones. Each chapter stays at author-instructor altitude; the script or prompt that produces the artifact lives in its appendix.*

| # | Chapter | What it covers | Verifiable here? |
|---|---|---|---|
| 13 | The Enriched Layer: Beyond the Book | Why one source should carry quizzes, cases, glimmers, recall cards, and an Ask-AI loop — and why a quiz needs no defense but a glimmer does | n/a (argument) |
| 14 | Case Studies | What a teaching case is, why it beats a worked example for transfer, how it's generated | prompt — yes |
| 15 | Glimmers: AI-Interrogated Prompts | The novel one — a prompt that makes the *student* defend their thinking to an AI; why it's not a quiz | prompt — yes |
| 16 | Spaced Repetition: Anki and the Forgetting Curve | "Space-based reasoning" — recall on a forgetting curve; why massed re-reading fails | build + prompt — **yes** |
| 17 | Canvas Course Export: `.imscc` | The LMS surface — pages, quizzes, cases, glimmers, syllabus in one upload; then refine with IgniteAI | **script tested** |
| 18 | The React Site: `.mdx` + `.tsx` | The public-web surface; author runs the script, hands the rest to a developer | to scaffold line |
| 19 | Medhavy: the AI-Tutor Layer via LTI | What Medhavy adds on top of Canvas; student experience; developer hand-off | **no — pointer** |
| 20 | Ask AI Everywhere | Capstone: the same question across Ignite, Medhavy, a parallel LLM for Kindle/PDF, and the web — kept a human+AI loop, not a vending machine | prompt — partly |

Ch 20 closes the book on the fluency trap of Chapter 1, now on the student's side of the desk.

## PART 2 appendices — the scripts and prompts

| File | Carries |
|---|---|
| `90-appendix-imscc-standard.md` | `build-imscc-standard.py` — **written & tested** |
| `91-appendix-case-generator.md` | Case Study Generator (prompt) |
| `92-appendix-glimmer-generator.md` | Glimmer Generator (prompt) |
| `93-appendix-spaced-repetition-generator.md` | Spaced-Repetition Card Generator (prompt) |
| `94-appendix-anki-build.md` | `build-anki.py` — `.apkg` builder |
| `95-appendix-react-site.md` | `build-react-site.py` — `.mdx` + `.tsx` scaffold |
| `96-appendix-medhavy-lti.md` | Medhavy LTI 1.3 setup guide (Sri's sequence) + SDD pointer |
| `97-appendix-ask-ai.md` | Per-surface Ask AI config + the parallel-LLM companion prompt |
| `99-back-matter.md` | Back matter |

Appendices `80–89` remain the Part 1 pipeline prompts/scripts (unchanged).

---

## Where the enriched artifacts get authored
You said placeholder chapters are fine for this, so it's parked — but the open
question stays: quizzes/cases/glimmers/cards must exist in the source before any
surface can ship them. Cleanest answer remains *generate them in/after Chapter
10 (Enrichment) and have the Part 2 surface chapters format them*. The Part 2
concept chapters (14–16) can double as the "here's how this artifact is
authored" chapters, each pointing to its generator appendix.

## What's buildable now vs. gated
- **Now:** Ch 17 Canvas (script done) · Ch 16 Anki (`.apkg` is a documented format) · the Ch 20 parallel-LLM prompt.
- **To the scaffold line:** Ch 18 React (`.mdx`/`.tsx` generated, Next.js build confirmed; deployed site is yours).
- **Gated, hand-off only:** Ch 19 Medhavy/LTI — needs NEU IT registration, a Canvas sandbox, FERPA review. Ships as a pointer; the chapter should say so.
