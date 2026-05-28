# Research: Chapter 05 — Book Scaffold: new_book.py
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students run new_book.py to scaffold their book directory and understand what each generated file does and who reads it.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

- **Knuth, Donald E. (1984). "Literate Programming." The Computer Journal, 27(2), 97–111.** The founding text for the idea that a program is a document that humans read first and machines execute second. AI+1's directory is a literate scaffold — `vision.md`, `architecture.md`, `chapters-spec.md` are read by humans; `TIKTOC.md`, `book.md`, `pantry/` are read by Cowork. Knuth's claim that "instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do" is the philosophical license for separating human-facing and machine-facing files in the scaffold.

- **Greenfeld, Daniel Roy and Audrey Roy Greenfeld. *Two Scoops of Django* (multiple editions) and the Cookiecutter project (2013–present).** Cookiecutter is the canonical Python project scaffolder. Its core idea — a templated directory tree filled in by Jinja2 variables — is exactly what new_book.py does. Audrey Roy Greenfeld's design choices in Cookiecutter (one command, sensible defaults, no global state) are the reference design.

- **Hunt, Andrew and David Thomas (1999). *The Pragmatic Programmer.*** Source of "DRY" (Don't Repeat Yourself) and of the idea that the project layout itself is a contract. The shared library / `_lib_` pattern in AI+1's pantry directly inherits from this.

- **MacFarlane, John. Pandoc (2006–present).** Pandoc is the document converter that AI+1 calls in `build.sh`. The `metadata.yaml` file in the scaffold exists because pandoc reads it. Worth citing because the metadata.yaml schema is not invented — it is pandoc's.

- **Wilson, Greg et al. (2014). "Best Practices for Scientific Computing." PLoS Biology 12(1).** And Wilson's Software Carpentry curriculum more broadly. The argument that filesystem layout is the first reproducibility artifact — that "people read directories before they read code" — undergirds the chapter's claim that the scaffold is itself instructional.

- **Jupyter Book project (Executable Books community, 2019–present)** and **Quarto (Posit/RStudio, 2022–present).** Both are executable-book frameworks that ship opinionated scaffolds. They are the most direct contemporary cousins of new_book.py and worth one-paragraph comparison.

### Key empirical cases

- **Guo, Philip J. (2014). "Python is Now the Most Popular Introductory Teaching Language at Top U.S. Universities." CACM blog**, and Guo's later HCI work at UCSD (e.g., the *Online Python Tutor* project, Guo 2013 SIGCSE). Guo documented Python installation as a primary teaching obstacle — students could not run code in the first week. This is the empirical license for the "Python install sidebar" being on page one of the chapter rather than appendix.

- **Ko, Andrew J. et al. (2011). "The State of the Art in End-User Software Engineering." ACM Computing Surveys 43(3).** Surveys the friction non-programmers hit when programming infrastructure leaks. Useful for framing why the chapter must teach the scaffold without teaching Python.

- **The Cookiecutter Data Science template (drivendata, 2016)** — most-imitated data-science scaffold. Their `README.md` doctrine ("the data is immutable, code reproduces analysis, directory layout signals intent") maps cleanly to AI+1's "TIKTOC.md is the spec, build.sh reproduces the book."

---

## 2. The Core Concept — State of the Field

### What is settled

- Project scaffolders are now language-default: `cargo new` (Rust), `npm init` / `yarn create` (Node), `dotnet new` (C#), `cookiecutter` (Python). Every modern ecosystem ships one. The argument that scaffolding is overhead is over.
- Directory layout is a form of documentation. The Maven convention (`src/main/java`, `src/test/java`), the Rails layout, the Python `src/` layout — all settled as defaults their communities defend.
- Convention-over-configuration is the dominant idiom for solo and small-team projects. DHH's framing has won in practice even where his terminology hasn't.
- Pandoc is the de facto Markdown-to-EPUB/PDF converter for solo publishers. There is no live competitor at the same maturity for this workflow.

### What is disputed

- **Where opinion ends and lock-in begins.** Cookiecutter is criticized for producing scaffolds users cannot maintain because they don't understand the generated files. The same risk applies to new_book.py. The chapter must mitigate this by explaining every file, not by hiding them.
- **Whether `src/` layout or flat layout is correct for small Python projects.** Mostly settled in favor of `src/` for libraries; for single-script tools like new_book.py, flat is fine. Worth one footnote.
- **Whether `metadata.yaml` is the right metadata home, vs. `book.toml` (mdBook) or front matter in the first chapter (Jekyll-style).** YAML won in pandoc's ecosystem. The book should not relitigate this.

### What has changed recently (last 5 years)

- **Quarto (2022)** unified the R Markdown / Jupyter Book / pandoc world for scientific publishing. It is now plausible competition for any hand-rolled scaffold. The chapter should acknowledge it as an alternative the reader could legitimately choose, then explain why AI+1 needs its own scaffold (the pantry/, the Cowork-reads-this-vs-human-reads-this split).
- **AI-assisted project scaffolding.** Tools like GitHub's `create-next-app` and now LLM-driven project generators have made the scaffold itself a moving target. New_book.py's stability is a feature.
- **The "build.sh as covenant" pattern.** Modern reproducible-research norms (Turing Way, 2022) treat the build script as a promise that anyone can reproduce the artifact. This is the frame the chapter should use for `build.sh`.

---

## 3. Application Domain Examples

1. **The graphic designer's Figma file structure.** Designers already understand "files-as-architecture" — a well-organized Figma file has pages for design system, components, screens, archive. The scaffold is the same idea for a book. Use this analogy.
2. **A brand identity package handoff.** When a designer ships a brand to a client, they ship a folder: logo/ (svg + png + favicon), typography/, color/, guidelines.pdf. Each subdirectory is for a different reader (developer, printer, social media manager). new_book.py creates the same kind of handoff package — some files for the human, some for Cowork.
3. **InDesign book templates.** The designer's existing intuition: a template gives you master pages, paragraph styles, and a TOC structure before you write a word. new_book.py is the InDesign book template for an AI+1 textbook.
4. **A studio's project intake folder.** Most freelance designers have a `_template_project/` they duplicate for each new client — with empty `brief/`, `research/`, `concepts/`, `final/`. new_book.py automates this for a textbook.
5. **The export preset.** When a designer hits Export with a preset, they trust years of defaults. The reader should treat new_book.py the same way: trust the defaults, learn what they do, change them only with reason.

---

## 4. The Book's Thesis Connection

The thesis: the TIKTOC.md session is the highest-leverage step. Everything downstream is execution.

Chapter 5 is the first proof of that thesis in code. The scaffold reads the TIKTOC.md and lays out a directory that is structurally committed to it — `chapters-spec.md` mirrors the chapter list, `pantry/` will hold one file per chapter, `metadata.yaml` is pre-populated from the TIKTOC vision section. If the TIKTOC.md is vague, the scaffold reveals it immediately: blank capability statements, missing chapter titles, empty bridge questions.

This is the chapter's load-bearing argument: the scaffold is not setup — it is the first time the TIKTOC.md is forced through a deterministic process. A weak TIKTOC.md produces a weak scaffold. A strong TIKTOC.md produces a directory the human can read and recognize as their book.

It also sets up the "directory-as-API" frame for the rest of Act Two. Chapters 6 and 7 are about specific files inside this scaffold. Chapter 8 is about the human reading and rewriting files inside this scaffold. Chapter 11 is about `build.sh` turning this scaffold into an EPUB. The directory is the spine of the second half of the book.

Connection backward: Chapter 4's TIKTOC.md is the input. Connection forward: Chapter 6's pantry/ population is the next file to populate; Chapter 11's build.sh is the same shell script introduced here, run for real.

---

## 5. The AI Wayback Machine — Candidate Figures

**Candidate A — Kristen Nygaard (1926–2002).** Wikipedia page title: **"Kristen Nygaard."** Norwegian computer scientist, co-creator with Ole-Johan Dahl of Simula and of object-oriented programming. Substantive connection: Nygaard's central conviction was that programs are models of the world, and that the *structure* of the program — the objects and their relationships — must mirror the structure of what is being modeled. new_book.py's directory mirrors the structure of a book. Lesser-known to designers, undergrad-accessible, non-American (Norwegian), strong human-rights legacy (Nygaard led the "No to EU" campaign in Norway — adds dimension). Example prompt for the AI Wayback box: *"Ask Claude: What did Kristen Nygaard mean when he said programming is modeling? How does that idea show up in a directory layout for a book?"*

**Candidate B — Audrey Roy Greenfeld.** Wikipedia page title: **"Audrey Roy Greenfeld"** (page exists, modest length). Creator of Cookiecutter, co-founder of PyLadies. Substantive connection: she built the most-used project scaffolder in Python; new_book.py is in that direct lineage. Diversity contribution (woman in software infrastructure, often invisible). Undergrad-accessible. Example prompt: *"Ask Claude: Read the Cookiecutter README. What does Audrey Roy Greenfeld assume about her users that lets her ship a one-command scaffolder?"*

**Candidate C — Donald Knuth (1938– ).** Wikipedia page title: **"Donald Knuth."** Literate Programming as the framework: a project is a document for humans first. Strong intellectual link but widely-known and male; use only if a more lesser-known figure is preferred elsewhere. Example prompt: *"Ask Claude: Read Knuth's 1984 'Literate Programming' essay. Argue whether AI+1's directory scaffold is literate programming or its opposite."*

**Diversity flag:** Default skews male. Recommend Nygaard (lead) + Greenfeld (sidebar) as the pair, with Knuth as fallback only.

---

## 6. Pedagogical Delivery Research

- **The first-five-minutes rule.** Guo's Python work and Ko's end-user programming surveys both find that learners who cannot execute something in the first five minutes disengage. The chapter's opening — "thirty seconds, forty lines of output" — is doing exactly this work. Keep it.
- **Failure-first opening.** The TIKTOC.md template requires it; the chapter's natural failure-first opening is the Python install failure (wrong version, PATH not set, "command not found"). The Python install sidebar should be staged as the *anticipated* failure the chapter solves before the reader hits it.
- **Naming every file.** Research on technical onboarding (Begel & Simon 2008 on novice software engineers) shows that unnamed artifacts in a generated tree create silent anxiety. Every file must be one-line described in the worked example table.
- **Two-column "who reads this" table.** A simple table — File | Read by Cowork / Read by Human / Read by build script — does most of the chapter's cognitive work. This is the figure to commission.

---

## 7. Representation and Display Research

- **Tree-style directory diagram.** ASCII tree (`tree` command output) is the standard and readable. Do not invent a custom diagram.
- **Annotated terminal output.** Show the actual `new_book.py` run as a code block, with margin annotations (callouts) for the key lines. Carpentries' style guide is the model.
- **Color-coded file map.** Two colors: human-facing files (vision.md, architecture.md, chapters-spec.md, risks.md, outline.md) and Cowork-facing files (TIKTOC.md, book.md, pantry/). One color per audience. This is also good practice for the visual designer reader — they will immediately read it as an information design problem.
- **metadata.yaml shown fully populated.** Don't show a template with `<your-title-here>`. Show the ai-for-designers values. Designers respect populated artifacts.

---

## 8. Open Questions and Research Gaps

- **What does new_book.py actually do today?** The chapter cannot be drafted without inspecting the current new_book.py. Need to read the actual script and document its arguments and outputs.
- **Does the chapter handle the case where a reader runs new_book.py twice?** Idempotency matters. What happens to existing files?
- **Is the Python install sidebar load-bearing or recoverable?** If the chapter assumes the reader has Python and they don't, the chapter fails. The sidebar must be *before* the first command, not parallel to it.
- **What is the relationship between `chapters-spec.md` and `TIKTOC.md`?** Both contain chapter information. Which one is canonical? The chapter must answer this in the "Cowork reads first" section.
- **Is there a `make` / Justfile alternative to build.sh worth naming?** Probably not for this reader, but flag.

---

## 9. Sourcing Notes

Primary technical sources (Knuth 1984, Cookiecutter docs, pandoc docs, Quarto docs) are stable and citation-ready. Guo 2014 is a blog post but widely cited — use as evidence, not as proof; pair with Guo's peer-reviewed SIGCSE 2013 paper on Online Python Tutor. Pragmatic Programmer is canonical practitioner literature; cite the 20th-anniversary edition (2019). Wilson's Software Carpentry materials are CC-BY and directly citable. Nygaard's Wikipedia page is solid; the *Communications of the ACM* obituary (2002) is a good secondary source for the AI Wayback box. Audrey Roy Greenfeld's contributions are best sourced from the Cookiecutter README and her PyCon talks; cite talk title and year. Avoid citing Substack posts or LLM-generated tutorials as primary evidence for design decisions.

No paywalled sources in the primary set. PRISMA-style systematic review is not appropriate here — this is a design-research chapter, not a synthesis chapter.
