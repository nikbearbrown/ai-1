# Writing Guide with LLMs — Chapter Map

*Built 2026-05-10 from OpenStax *Writing Guide with Handbook* source modules in `chapters/*/`. Structural extraction only — no rewrite. Source totals are raw word counts before Feynman-voice synthesis. Each chapter will land at 5,000–8,000 words regardless of source length.*

---

## How the source is organized

OpenStax modules ship as numbered `.md` files inside each chapter folder. Most "anchor" chapters (the ones with a real student assignment) follow a 10-module pattern:

| Position | Module type | Typical length |
|---|---|---|
| 01 | Chapter intro | ~250 w |
| 02 | "Genre Trailblazer" — a writer or practitioner profile | ~400–2,000 w |
| 03 | "Reaching Across the Field" — case or example | ~500–1,000 w |
| 04 | Characteristics of the genre | ~800–2,000 w |
| 05 | Introduction to the assignment | ~1,000–3,000 w |
| 06 | **The big one** — assignment guide + student model | **3,500–8,500 w** |
| 07 | Grammar / style focus | ~500–1,800 w |
| 08 | Rubric | ~1,000–2,300 w |
| 09 | Publishing / extension | ~500–1,800 w |
| 10 | Reflective task | ~400–800 w |

Three chapters (1, 5, 18) are short **bridge chapters** — single intro modules under 300 words, designed as transitions between book parts.

A few chapters break the template: Ch 13 (Reasoning Strategies) has six modules; Ch 15 (Research Process) has seven; Ch 16 (Annotated Bibliography) has five; Ch 23 (Portfolio) has nine and reshuffles the order.

When a chapter is rewritten for this textbook, the module structure is **input, not output**. The synthesized chapter follows the workshop's 8-section structure (hook → three concept sections → integration → graduated exercises → summary → connections forward), not the OpenStax 10-module structure.

---

## Ch 00 — Claude Basics *(to be written)*

**Status:** Not yet drafted. Native-to-the-book framing (State B): the LLM layer is integral, not retrofitted. Audience: undergraduate + early-career professional writers.

**Core concepts (planned):**

- What LLMs do well for writers and where they fail (writing-specific, not generic)
- Two prompt types this book uses — Dig Deeper (inline detours) and LLM Exercises (running-project advances)
- When to reach for Claude chat vs. Claude Project vs. Claude Code vs. Cowork — decision rule, not feature tour
- How to recover when Claude's output is thin or wrong — iterate, don't abandon
- Field-specific failure modes the student will actually hit

**New capabilities:** student knows when to consult Claude, how to phrase the consultation, how to evaluate the response, how to carry output across exercises.

**Connection to running project:** sets up the project selected at end of Chapter Map review.

**Dig-deeper candidates:** the difference between *generating* and *thinking*; the politics of attribution when an LLM helps you write; what counts as "your" sentence in an LLM-assisted draft.

---

## Ch 01 — The Things We Carry: Experience, Culture, and Language

**Source:** 1 module, 170 w (bridge chapter — book opening only)

**Core concepts:** writing as carried experience; identity as input to writing; the textbook's organizing premise.

**New capabilities:** orientation — the student can name what they bring to the writing task before they pick up a pen.

**Key vocabulary:** *literacy*, *identity*, *discourse community*.

**Dig-deeper candidates:** how "voice" gets confused with "style"; whether AI changes what counts as carrying experience into your writing.

---

## Ch 02 — The Digital World: Building on What You Already Know to Respond Critically

**Source:** 9 modules, ~13,700 w. Anchor assignment: **Critical Response** to digital media.

**Core concepts:** rhetoric and rhetorical situation; authenticity as a rhetorical strategy; reading words and images together as one text.

**New capabilities:** the student can identify the rhetorical situation of any digital text — who's speaking, to whom, for what purpose, with what constraints — and write a structured critical response.

**Key vocabulary:** *rhetorical situation*, *purpose*, *audience*, *exigence*, *kairos*, *authenticity*, *ethos*.

**Dig-deeper candidates:** whether an LLM has a rhetorical situation; how "authenticity" gets manufactured; the brave-new-world classroom debate (m00017).

---

## Ch 03 — Language, Identity, and Culture: Exploring, Employing, Embracing

**Source:** 9 modules, ~12,500 w. Anchor assignment: **Cultural Artifact** essay.

**Core concepts:** culture as something you are inside, not something you observe from outside; English's many dialects as different tools, not better/worse versions; the colonized self.

**New capabilities:** the student can write about a cultural artifact in a voice that honors the artifact's own register rather than translating it away.

**Key vocabulary:** *idiolect*, *standard English*, *code-switching*, *colonization*, *cultural artifact*.

**Dig-deeper candidates:** whether LLMs reinforce "standard English" by default; how to prompt for dialectal authenticity without caricature.

---

## Ch 04 — Literacy Narrative: Building Bridges, Bridging Gaps **★ recommended for first write**

**Source:** 10 modules, ~17,053 w. Anchor assignment: **Independent Literacy Narrative**.

**Core concepts:** the literacy narrative as a genre; storytelling elements (scene, character, conflict, change) applied to one's own learning; sentence combining as a craft tool.

**New capabilities:** the student can draft a literacy narrative that uses scene rather than summary, places themselves inside a learning event rather than reporting it from outside, and combines sentences for rhythm.

**Key vocabulary:** *literacy narrative*, *DALN* (Digital Archive of Literacy Narratives), *idiolect*, *scene vs. summary*, *sentence combining*.

**Dig-deeper candidates:** Anzaldúa's *Borderlands / La Frontera* and the literacy narrative as resistance; the DALN as a corpus to mine for prompts; whether using an LLM is now part of every student's literacy story.

**Why this chapter first:** topic ("writing about your own learning") is naturally Feynman-friendly — his pedagogy is essentially literacy-narrative-style storytelling about understanding. Concrete people to anchor (Anzaldúa). Rich source. Sets the voice for the rest of the book.

---

## Ch 05 — Bridging the Divide Between Personal Identity and Academia

**Source:** 1 module, 138 w (bridge chapter — transition into academic register).

**Core concepts:** personal voice meeting institutional expectations; the transition every first-year writer makes.

**New capabilities:** the student can name what they're being asked to do when an instructor says "more academic."

**Key vocabulary:** *academic register*, *discourse community*, *audience expectation*.

**Dig-deeper candidates:** whether "academic voice" is one thing or many; how Claude can help you sound *more* like yourself, not less, in academic prose.

---

## Ch 06 — Memoir or Personal Narrative: Learning Lessons from the Personal

**Source:** 10 modules, ~13,353 w. Anchor assignment: **A Turning Point** narrative.

**Core concepts:** memoir vs. personal narrative (memoir = remembered angle on a life; personal narrative = single event); context and voice as a storyteller's tools; characterization in nonfiction.

**New capabilities:** the student can write a turning-point narrative where the reader experiences the turn rather than being told about it.

**Key vocabulary:** *memoir*, *personal narrative*, *context*, *voice*, *characterization*, *persona*.

**Dig-deeper candidates:** the truth-of-experience vs. accuracy-of-fact distinction (m00046); what an LLM can and can't do when your memory is the source.

---

## Ch 07 — Profile: Telling a Rich and Compelling Story

**Source:** 10 modules, ~17,287 w (Ch 07's module 06 is the heaviest in the book at 8,639 w). Anchor assignment: **A Profile in Courage or Other Admirable Trait**.

**Core concepts:** the subject's voice as the spine of the profile; angle as the writer's contribution; English varieties and verb choice as register tools.

**New capabilities:** the student can interview, listen for the spine, and write a profile that does not become a résumé.

**Key vocabulary:** *profile*, *angle*, *spine*, *quotation integration*.

**Dig-deeper candidates:** using Claude as an interview-prep partner; the ethics of LLM-assisted transcription; what an interviewer hears that a transcription misses.

---

## Ch 08 — Proposal: Writing About Problems and Solutions

**Source:** 10 modules, ~16,387 w. Anchor assignment: **A Proposal** (problem + solution + rhetorical situation).

**Core concepts:** problem-solving mindset (m00059); purpose as the proposal's organizing constraint; rhetorical situation applied to action-seeking writing.

**New capabilities:** the student can write a proposal where the problem is specific enough to be tractable and the solution is specific enough to be evaluable.

**Key vocabulary:** *problem definition*, *purpose*, *audience*, *feasibility*, *subject-verb agreement*.

**Dig-deeper candidates:** how Claude pushes a vague problem to specificity; the "medical problem solver" case (m00060) as a transferable framework.

---

## Ch 09 — Evaluation or Review: Would You Recommend It?

**Source:** 10 modules, ~14,559 w. Anchor assignment: **Review of a Primary Media Source**.

**Core concepts:** evidence-based judgment vs. taste assertion; consistent objectivity as a discipline; when quotation is the strongest evidence.

**New capabilities:** the student can write a review that survives a hostile reader — every claim earns its place.

**Key vocabulary:** *evaluation*, *criteria*, *judgment*, *primary source*, *offensive vs. artful language*.

**Dig-deeper candidates:** asking Claude to argue against your evaluation; the artful-language question (m00076) as a case study in critical reading.

---

## Ch 10 — Analytical Report: Writing from Facts

**Source:** 10 modules, ~16,973 w. Anchor assignment: **Analytical Report**.

**Core concepts:** fact vs. opinion as a working distinction (not a metaphysical one); defining purpose tight enough to choose what's relevant; nonessential vs. essential information.

**New capabilities:** the student can write an analytical report that earns its conclusion from the facts on the page, not from outside authority.

**Key vocabulary:** *analytical report*, *purpose*, *primary source*, *secondary source*, *essential vs. nonessential modifier*.

**Dig-deeper candidates:** the "myth-buster" framing (m00080) as a critical-thinking move; using Claude to stress-test whether a "fact" actually supports the claim you're making.

---

## Ch 11 — Rhetorical Analysis: Interpreting the Art of Rhetoric

**Source:** 10 modules, ~14,800 w. Anchor assignment: **Rhetorical Analysis** of a chosen text.

**Core concepts:** rhetorical strategies as moves a writer makes; "whose rhetoric" as a question that reframes analysis; the actual workings of rhetorical analysis (m00091).

**New capabilities:** the student can take a piece of public writing apart at the seams — naming each move and why it was made.

**Key vocabulary:** *ethos*, *pathos*, *logos*, *kairos*, *rhetorical strategy*, *rhetorical situation*.

**Dig-deeper candidates:** asking Claude to identify the rhetorical moves in a piece you've already analyzed — what does it catch you missed, what does it miss; the "*just because... doesn't mean*" construction (m00094).

---

## Ch 12 — Position Argument: Practicing the Art of Rhetoric

**Source:** 10 modules, ~16,244 w. Anchor assignment: **Position Argument**.

**Core concepts:** the position argument as a genre (claim, reasons, evidence, response to counter); the trendsetter case (m00100); citation types.

**New capabilities:** the student can write a position argument that anticipates the strongest objection rather than the easiest.

**Key vocabulary:** *claim*, *position*, *counterargument*, *concession*, *refutation*, *citation*.

**Dig-deeper candidates:** Claude as a sparring partner — generate the steel-manned opposing view; when an argument needs more evidence vs. more reasoning.

---

## Ch 13 — Reasoning Strategies: Improving Critical Thinking **★ second-strongest first-write candidate**

**Source:** 6 modules, ~13,385 w. No anchor assignment — this is the "thinking moves" chapter.

**Core concepts:** analogy as a reasoning tool (m00109); reasoning strategies in science; recognizing purpose in reasoning.

**New capabilities:** the student can name the reasoning move they're about to make — inductive, deductive, analogical, causal — and judge whether the move is doing the work it claims.

**Key vocabulary:** *induction*, *deduction*, *analogy*, *causal reasoning*, *purpose*.

**Dig-deeper candidates:** Pearl's three rungs of causation as a deepening; Bayesian updating as a reasoning-under-uncertainty move; whether LLMs reason or pattern-match (the chapter's reflexive question).

**Why this chapter is also strong as first write:** it's the most directly aligned with the workshop's own method — Feynman-style reasoning is *the* subject. A great fit for showing voice, but lower stakes than Ch 04 because there's no assignment to scaffold.

---

## Ch 14 — Argumentative Research: Enhancing the Art of Rhetoric with Evidence

**Source:** 10 modules, ~16,221 w. Anchor assignment: **Argumentative Research Paper**.

**Core concepts:** research as joining a scholarly conversation, not gathering decorations for a preformed view; the research process as iterative; quotation integration.

**New capabilities:** the student can run a research argument where the evidence shaped the claim, not the other way around.

**Key vocabulary:** *argumentative research*, *scholarly conversation*, *discussion question*, *language bias*.

**Dig-deeper candidates:** using Claude to find the strongest source against your claim; how language bias (m00122) sneaks into research writing.

---

## Ch 15 — Research Process: Accessing and Recording Information

**Source:** 7 modules, ~11,880 w. Anchor assignment: **Research Log**.

**Core concepts:** generating key words as a research skill (m00125); conducting field research; working with human subjects and IRB.

**New capabilities:** the student can run a real research process — find sources, judge sources, take notes that survive the gap between reading and drafting.

**Key vocabulary:** *keyword generation*, *field research*, *IRB*, *synthesis*, *research log*.

**Dig-deeper candidates:** asking Claude to brainstorm keyword sets you'd never reach alone; what an IRB protects that an LLM can't.

---

## Ch 16 — Annotated Bibliography: Gathering, Evaluating, and Documenting Sources

**Source:** 5 modules, ~11,395 w. Anchor assignment: **Annotated Bibliography**.

**Core concepts:** compiling sources as a critical act, not a clerical one; citation styles as register; evaluating source quality.

**New capabilities:** the student can build an annotated bibliography that argues — the choice and arrangement of sources is itself a claim.

**Key vocabulary:** *annotated bibliography*, *citation style*, *source evaluation*, *primary vs. secondary*.

**Dig-deeper candidates:** using Claude to draft annotation summaries and then *editing them down* (the editing as the real work); when Claude invents sources.

---

## Ch 17 — Case Study / Profile: What One Person Says About All

**Source:** 10 modules, ~13,765 w. Anchor assignment: **A Case Study**.

**Core concepts:** case study ethics; Ramachandran's phantom limb work as a model of the form (m00138); components of case studies.

**New capabilities:** the student can write a case study where one particular thing genuinely speaks to a general pattern — without overclaiming.

**Key vocabulary:** *case study*, *case study ethics*, *generalization*, *homonyms*.

**Dig-deeper candidates:** the n=1 problem and what it can and cannot show; the parallels between case study and clinical reasoning.

---

## Ch 18 — Navigating Rhetoric in Real Life

**Source:** 1 module, 136 w (bridge chapter — transition into "writing in the wild").

**Core concepts:** what carries from school writing into actual writing in workplaces, public forums, and online; rhetoric outside the classroom.

**New capabilities:** the student can name the shift between assignment-writing and audience-writing.

**Key vocabulary:** *real-world rhetoric*, *workplace writing*.

**Dig-deeper candidates:** whether Claude is itself "real-life rhetoric" — every prompt is a piece of audience-writing.

---

## Ch 19 — Print or Textual Analysis: What You Read

**Source:** 10 modules, ~17,808 w. Anchor assignment: **Textual Analysis**.

**Core concepts:** analyzing and interpreting as distinct moves; "talking back" to a text; interpretive communities.

**New capabilities:** the student can read a print text closely enough to argue about it from inside.

**Key vocabulary:** *textual analysis*, *interpretation*, *interpretive community*, *literary present tense*.

**Dig-deeper candidates:** Claude's interpretive defaults — what reading does it produce when you ask it to "analyze" something, and what does that tell you about its training; when literary present tense slips.

---

## Ch 20 — Image Analysis: What You See

**Source:** 10 modules, ~17,206 w. Anchor assignment: **Image Analysis**.

**Core concepts:** interpreting visual information as a teachable skill; reflecting on images (m00159); writing persuasively about images.

**New capabilities:** the student can write about an image without falling into mere description — naming what the image *does*, not just what it shows.

**Key vocabulary:** *visual rhetoric*, *hybridity*, *descriptive diction*, *camera angle*.

**Dig-deeper candidates:** showing Claude the same image and comparing readings — yours, the LLM's, a classmate's; the Sara Ludy case (m00158) on hybridity in digital art.

---

## Ch 21 — Multimodal and Online Writing: Creative Interaction Between Text and Image

**Source:** 9 modules, ~13,546 w. Anchor assignment: **Multimodal Composition**.

**Core concepts:** audience awareness in multimodal contexts; digital representations of embodiment and identity (m00003); digital deserts (m00008).

**New capabilities:** the student can compose for screen-and-page-together, choosing modes for what each does best.

**Key vocabulary:** *multimodal*, *embodiment*, *digital divide*, *audience awareness*.

**Dig-deeper candidates:** how Claude reads multimodal vs. text-only; what an LLM can't see in an image yet (and where that's changing fast — flag for date sensitivity).

---

## Ch 22 — Scripting for the Public Forum: Writing to Speak

**Source:** 9 modules, ~14,282 w. Anchor assignment: **A Scripted Speech / Talk**.

**Core concepts:** writing for and beyond the academy (m00167); writing for listeners vs. readers (m00169); the Disability Visibility Project as a forum case (m00168); speaking genres — spoken word, pulpit, YouTube, podcast, social media.

**New capabilities:** the student can write a script that reads well on the page *and* lives well in the mouth — different constraints, both honored.

**Key vocabulary:** *script*, *delivery*, *speaking genre*, *audience attention*.

**Dig-deeper candidates:** asking Claude to read your script aloud (or to suggest where it would stumble); how speaking-genre conventions differ from writing-genre conventions.

---

## Ch 23 — Portfolio Reflection: Your Growth as a Writer

**Source:** 9 modules, ~11,740 w. Anchor task: **Portfolio Reflection**.

**Core concepts:** finding a home in writing (m00177); areas of exploration; reference, antecedent, and case as a polish-level concern; eliminating gender bias.

**New capabilities:** the student can step back from a year's writing and see the writer they've become — and the one they're not yet.

**Key vocabulary:** *portfolio*, *reflection*, *antecedent*, *case*, *gender-neutral language*.

**Dig-deeper candidates:** what Claude notices about your writing across a semester that you don't notice yourself; the limit of LLM-assisted reflection (it can see patterns, not growth).

---

## Recommended first chapter to write: **Ch 04 — Literacy Narrative**

Four reasons.

1. **It's the first real assignment chapter.** Chapters 01–03 are framing. If the voice and structure work for Ch 04, the rest of the book scales from it. If they don't, we learn that before sinking effort into more.

2. **The topic is natively Feynman-friendly.** Literacy narrative is "writing about your own learning." Feynman's own pedagogy is essentially that — storytelling about understanding. The voice has somewhere to live.

3. **There are concrete people to anchor.** Anzaldúa's *Borderlands / La Frontera* gives the chapter a named primary source — exactly what hard rule #2 demands. The DALN is a real corpus the student can engage with.

4. **The LLM-writing angle is genuinely interesting.** A literacy narrative written in 2026 has to reckon with the fact that the student's literacy *now includes* working with LLMs. That's not retrofitting — it's the actual present.

**Alternative first chapter: Ch 13 — Reasoning Strategies.** Lower stakes (no anchor assignment), most reflexively aligned with the workshop's own method. Good fit for showcasing voice if the goal is to demonstrate the workshop's approach rather than scaffold a writing assignment.

---

## Source contamination flag

`pantry/01-what-is-anthropology.md` appears to be cross-book contamination from `introduction-anthropology-with-llms`. Ignored per session decision; flagged here for future cleanup.

## Voice-anchoring status

Root `style/` exists (`README.md`, `VOICE.md`). Per-book `books/writing-guide-with-llms/style/` does not exist yet. First chapter will be drafted from root style only — flag `voice-unanchored` for per-book purposes. Reviewer should calibrate voice deliberately on first chapter and seed `books/writing-guide-with-llms/style/` from the approved draft.
# Revision Notes

Track what you've added, removed, or rewritten here.

---

## 2026-05-10 — Chapter Map + Ch 04 draft (State B partial run)

**Book state at start:** State B — 23 numbered source subfolders in `chapters/`, no flat chapter files. OpenStax *Writing Guide with Handbook* modules.

**This session produced:**

- `_chapter-map.md` — structural map across all 24 chapters (Ch 00 planned + Ch 01–23 mapped from source). No prose rewrites in the map.
- `chapters/04-literacy-narrative-building-bridges-bridging-gaps.md` — full chapter draft. 7,352 words. Voice: Fry (Attenborough × Feynman) per root `style/VOICE.md`. Flagged `voice-unanchored` — per-book `style/` is empty; first chapter doubles as voice-setting exercise.
- `pantry/04-literacy-narrative.md` — 812 words. Reusable ingredients.
- `images/04-literacy-narrative.md` — 1,143 words. Seven figure briefs incl. hero (the well-house at Tuscumbia).
- `bookmaps/04-literacy-narrative.md` — 1,988 words. Module-by-module source map, hard-rule audit, deferred material flagged.

**Verification (B5):** PASS.

**B6 cleanup: DEFERRED.** Source subfolder `chapters/04-literacy-narrative-building-bridges-bridging-gaps/` left in place pending review.

---

## 2026-05-10 — Bear-approved Ch 04 revision + full first-pass drafting of all 23 chapters

**Trigger:** Bear submitted a revised Ch 04 ("Doing the Work the Live Human Won't Be There to Do") to use as the voice anchor for all chapters going forward. Instruction: "Use this voice for all chapters... take your time but don't pause for my approval... these are rough drafts that will be rewritten."

**What changed in Bear's Ch 04 revision (vs. my v1):**

- Cut: TL;DR, suggested titles, learning outcomes block, prerequisites, explicit 8-section numbering, 2 of the 3 Dig Deeper boxes, the graduated-exercises section (E1–E10), tags, the verbose section headers.
- Kept: cold open, the scene/summary mechanism, three turning points, finding-yours guidance, sentences/revision section, LLM Exercise, "What would change my mind," "Still puzzling."
- Added: "A note about AI" as a section (replacing Dig Deeper structure).
- Tighter, less workshop-formatted, more essay-chapter than apparatus-laden textbook chapter. ~4,800 words rather than ~7,350.

**Saved as voice anchor:** `style/voice-anchor-ch04-literacy-narrative.md`. Per-book `style/` folder created and seeded.

**This drafting pass produced (all 23 source chapters drafted as flat .md files in `chapters/`):**

| Ch | Filename | Words |
|---|---|---|
| 01 | `01-the-things-we-carry-experience-culture-and-language.md` | 2,369 |
| 02 | `02-the-digital-world-building-on-what-you-already-know-to-respond-critically.md` | 3,779 |
| 03 | `03-language-identity-and-culture-exploring-employing-embracing.md` | 3,464 |
| 04 | `04-literacy-narrative-building-bridges-bridging-gaps.md` | 4,785 (Bear's revision) |
| 05 | `05-bridging-the-divide-between-personal-identity-and-academia.md` | 2,396 (bridge) |
| 06 | `06-memoir-or-personal-narrative-learning-lessons-from-the-personal.md` | 3,333 |
| 07 | `07-profile-telling-a-rich-and-compelling-story.md` | 3,192 |
| 08 | `08-proposal-writing-about-problems-and-solutions.md` | 3,095 |
| 09 | `09-evaluation-or-review-would-you-recommend-it.md` | 3,343 |
| 10 | `10-analytical-report-writing-from-facts.md` | 3,252 |
| 11 | `11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md` | 3,508 |
| 12 | `12-position-argument-practicing-the-art-of-rhetoric.md` | 3,443 |
| 13 | `13-reasoning-strategies-improving-critical-thinking.md` | 3,600 |
| 14 | `14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence.md` | 3,636 |
| 15 | `15-research-process-accessing-and-recording-information.md` | 3,096 |
| 16 | `16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md` | 2,741 |
| 17 | `17-case-study-profile-what-one-person-says-about-all.md` | 3,590 |
| 18 | `18-navigating-rhetoric-in-real-life.md` | 2,383 (bridge) |
| 19 | `19-print-or-textual-analysis-what-you-read.md` | 2,950 |
| 20 | `20-image-analysis-what-you-see.md` | 3,181 |
| 21 | `21-multimodal-and-online-writing-creative-interaction-between-text-and-image.md` | 3,048 |
| 22 | `22-scripting-for-the-public-forum-writing-to-speak.md` | 3,148 |
| 23 | `23-portfolio-reflection-your-growth-as-a-writer.md` | 3,352 |

**Total: 74,684 words across 23 chapters.**

**Voice consistency:** every chapter follows Bear's Ch 04 structural template — title + subtitle, cold open with named primary source, descriptive section titles (lowercase), scene/specificity, named trade-offs, LLM Exercise at end, "What would change my mind," "Still puzzling," final boilerplate line about source modules.

**Source briefs:** generated by parallel Explore-agent subagents (kept main context manageable). Each brief covered through-line, named sources, key terms, assignment, worked examples, memorable passages, trade-offs, things to cut, and LLM angle for 2026. Briefs not preserved as files (used only for drafting).

**B5 verification (lightweight, per "rough draft" framing):**

- All 23 chapter files exist ✓
- All chapters use the voice-anchor structural shape ✓
- All chapters contain LLM Exercise + "What would change my mind" + "Still puzzling" ✓
- Word counts run lower than CLAUDE.md's 5,000–8,000 target — these are intentionally leaner rough drafts in Bear's voice ✓
- Companion files (pantry, images, bookmaps) NOT generated for chapters 01–03, 05–23. The CLAUDE.md State B procedure expects them. Per Bear's "rough drafts that will be rewritten" framing, this is deferred to the rewrite pass.

**B6 cleanup: NOT DONE.** All 23 source subfolders preserved in `chapters/[slug]/` pending Bear's review of the drafts. Cleanup waits for explicit instruction.

**Hard-rule compliance audit (preliminary):**

- No fabricated sources: every cited author, work, and quotation is from the OpenStax source modules or from established public record. Verified historical references (Helen Keller, Frederick Douglass, Tara Westover, Anzaldúa, Yousafzai, MLK, Truman, Selena Gomez, Plato, Broca, Cisneros, Kakutani, Talese, Hayden, Pronovost/Gawande, Twain). ✓
- Primary sources linked where available (Project Gutenberg, official archives, museum pages, journal URLs). ✓
- Calibrated uncertainty: every chapter's "What would change my mind" names what would revise the central claim; "Still puzzling" names what remains unresolved. ✓
- Reflexive method: every chapter engages with the limits of its own framework. ✓

**Composite teaching examples used:**

- Ch 04: "I have always been a reader" → *A Wrinkle in Time* student paragraph (preserved from Bear's revision).
- Ch 09: Restaurant review example (constructed).
- Ch 12: "Maya" student writing the AI-detection essay (constructed).
- Ch 17: "Mateo" student case study of bilingual code-switching (constructed).
- Ch 23: First-vs-late assignment opening contrast (constructed for illustration).

These are clearly framed as workshop examples, not real student quotations. If reviewer prefers explicit labeling, they can be tagged as "composite" or "illustrative."

**Open issues for the rewrite pass:**

1. Several chapters reference Lily Tran's "Food as Change" student essay from the OpenStax source. The essay is treated as a published model. If Bear wants to replace this with original examples, those chapters (Ch 14 especially) will need revision.

2. Chapter 18 (Navigating Rhetoric in Real Life) was light on source material (single 136-word bridge module). The bridge chapter draws on chapter-wide themes rather than source-specific material.

3. The OpenStax "Trailblazer" profiles (Selena Gomez, Cathy Park Hong, Coates, Bolatagici, etc.) are used as historical/cultural cases. Some are fresher than others — Selena Gomez circa 2017–2021, for instance, may feel dated by the time the book ships. Consider for the rewrite whether to refresh.

4. The LLM-tool naming throughout (Claude.ai, ChatGPT, Gemini, Cowork, Claude Code, Claude Project) reflects the 2026 tool ecosystem. This will date faster than other content. The rewrite pass should consider whether to abstract some references or keep them current.

5. Some chapters reference each other's content (Ch 4's hinge moments cited in Ch 6; Ch 2's seven elements cited throughout). The cross-references are intentional but should be audited for consistency in the rewrite.

**Not done this pass (intentionally deferred):**

- Chapter 00: Claude Basics. Still planned. Can be drafted once a running project is selected.
- Companion files (pantry, images, bookmaps) for chapters 01–03, 05–23.
- Running-project proposals (3–5 options as described in the original enrichment prompt).
- Dig Deeper inline prompts (Bear's revision cut these from the spec).
- Enrichment pass coordinating LLM Exercises around a single running project.
- Cleanup of `pantry/01-what-is-anthropology.md` (stray file, deferred).

**Recommended next moves:**

1. Bear reads through several chapters to check voice consistency.
2. If voice is right: decide what to keep, what to rewrite, what to expand. The rough-draft framing means the book is a draft of a draft.
3. If a running project is wanted (per the original curriculum-enrichment prompt), select one and draft Chapter 00.
4. Source subfolder cleanup waits for explicit approval. Once chapters are approved, the source folders can be removed (or moved to an archive).

---

*End of 2026-05-10 session log.*
# Table of Contents

*All 23 chapters drafted in voice anchored by Bear's Ch 04 revision (saved to `style/voice-anchor-ch04-literacy-narrative.md`). Source subfolders preserved pending review. Rough drafts — to be rewritten.*

## Chapter 1: The Things We Carry: Experience, Culture, and Language
- **Drafted:** [01-the-things-we-carry-experience-culture-and-language.md](chapters/01-the-things-we-carry-experience-culture-and-language.md) — 2,369 w
- Source: `chapters/01-the-things-we-carry-experience-culture-and-language/`

## Chapter 2: The Digital World: Building on What You Already Know to Respond Critically
- **Drafted:** [02-the-digital-world-building-on-what-you-already-know-to-respond-critically.md](chapters/02-the-digital-world-building-on-what-you-already-know-to-respond-critically.md) — 3,779 w
- Source: `chapters/02-the-digital-world-building-on-what-you-already-know-to-respond-critically/`

## Chapter 3: Language, Identity, and Culture: Exploring, Employing, Embracing
- **Drafted:** [03-language-identity-and-culture-exploring-employing-embracing.md](chapters/03-language-identity-and-culture-exploring-employing-embracing.md) — 3,464 w
- Source: `chapters/03-language-identity-and-culture-exploring-employing-embracing/`

## Chapter 4: Literacy Narrative: Building Bridges, Bridging Gaps
- **Drafted (voice anchor):** [04-literacy-narrative-building-bridges-bridging-gaps.md](chapters/04-literacy-narrative-building-bridges-bridging-gaps.md) — 4,785 w
- Source: `chapters/04-literacy-narrative-building-bridges-bridging-gaps/`

## Chapter 5: Bridging the Divide Between Personal Identity and Academia
- **Drafted:** [05-bridging-the-divide-between-personal-identity-and-academia.md](chapters/05-bridging-the-divide-between-personal-identity-and-academia.md) — 2,396 w (bridge chapter)
- Source: `chapters/05-bridging-the-divide-between-personal-identity-and-academia/`

## Chapter 6: Memoir or Personal Narrative: Learning Lessons from the Personal
- **Drafted:** [06-memoir-or-personal-narrative-learning-lessons-from-the-personal.md](chapters/06-memoir-or-personal-narrative-learning-lessons-from-the-personal.md) — 3,333 w
- Source: `chapters/06-memoir-or-personal-narrative-learning-lessons-from-the-personal/`

## Chapter 7: Profile: Telling a Rich and Compelling Story
- **Drafted:** [07-profile-telling-a-rich-and-compelling-story.md](chapters/07-profile-telling-a-rich-and-compelling-story.md) — 3,192 w
- Source: `chapters/07-profile-telling-a-rich-and-compelling-story/`

## Chapter 8: Proposal: Writing About Problems and Solutions
- **Drafted:** [08-proposal-writing-about-problems-and-solutions.md](chapters/08-proposal-writing-about-problems-and-solutions.md) — 3,095 w
- Source: `chapters/08-proposal-writing-about-problems-and-solutions/`

## Chapter 9: Evaluation or Review: Would You Recommend It?
- **Drafted:** [09-evaluation-or-review-would-you-recommend-it.md](chapters/09-evaluation-or-review-would-you-recommend-it.md) — 3,343 w
- Source: `chapters/09-evaluation-or-review-would-you-recommend-it/`

## Chapter 10: Analytical Report: Writing from Facts
- **Drafted:** [10-analytical-report-writing-from-facts.md](chapters/10-analytical-report-writing-from-facts.md) — 3,252 w
- Source: `chapters/10-analytical-report-writing-from-facts/`

## Chapter 11: Rhetorical Analysis: Interpreting the Art of Rhetoric
- **Drafted:** [11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md](chapters/11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md) — 3,508 w
- Source: `chapters/11-rhetorical-analysis-interpreting-the-art-of-rhetoric/`

## Chapter 12: Position Argument: Practicing the Art of Rhetoric
- **Drafted:** [12-position-argument-practicing-the-art-of-rhetoric.md](chapters/12-position-argument-practicing-the-art-of-rhetoric.md) — 3,443 w
- Source: `chapters/12-position-argument-practicing-the-art-of-rhetoric/`

## Chapter 13: Reasoning Strategies: Improving Critical Thinking
- **Drafted:** [13-reasoning-strategies-improving-critical-thinking.md](chapters/13-reasoning-strategies-improving-critical-thinking.md) — 3,600 w
- Source: `chapters/13-reasoning-strategies-improving-critical-thinking/`

## Chapter 14: Argumentative Research: Enhancing the Art of Rhetoric with Evidence
- **Drafted:** [14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence.md](chapters/14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence.md) — 3,636 w
- Source: `chapters/14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence/`

## Chapter 15: Research Process: Accessing and Recording Information
- **Drafted:** [15-research-process-accessing-and-recording-information.md](chapters/15-research-process-accessing-and-recording-information.md) — 3,096 w
- Source: `chapters/15-research-process-accessing-and-recording-information/`

## Chapter 16: Annotated Bibliography: Gathering, Evaluating, and Documenting Sources
- **Drafted:** [16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md](chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md) — 2,741 w
- Source: `chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources/`

## Chapter 17: Case Study Profile: What One Person Says About All
- **Drafted:** [17-case-study-profile-what-one-person-says-about-all.md](chapters/17-case-study-profile-what-one-person-says-about-all.md) — 3,590 w
- Source: `chapters/17-case-study-profile-what-one-person-says-about-all/`

## Chapter 18: Navigating Rhetoric in Real Life
- **Drafted:** [18-navigating-rhetoric-in-real-life.md](chapters/18-navigating-rhetoric-in-real-life.md) — 2,383 w (bridge chapter)
- Source: `chapters/18-navigating-rhetoric-in-real-life/`

## Chapter 19: Print or Textual Analysis: What You Read
- **Drafted:** [19-print-or-textual-analysis-what-you-read.md](chapters/19-print-or-textual-analysis-what-you-read.md) — 2,950 w
- Source: `chapters/19-print-or-textual-analysis-what-you-read/`

## Chapter 20: Image Analysis: What You See
- **Drafted:** [20-image-analysis-what-you-see.md](chapters/20-image-analysis-what-you-see.md) — 3,181 w
- Source: `chapters/20-image-analysis-what-you-see/`

## Chapter 21: Multimodal and Online Writing: Creative Interaction Between Text and Image
- **Drafted:** [21-multimodal-and-online-writing-creative-interaction-between-text-and-image.md](chapters/21-multimodal-and-online-writing-creative-interaction-between-text-and-image.md) — 3,048 w
- Source: `chapters/21-multimodal-and-online-writing-creative-interaction-between-text-and-image/`

## Chapter 22: Scripting for the Public Forum: Writing to Speak
- **Drafted:** [22-scripting-for-the-public-forum-writing-to-speak.md](chapters/22-scripting-for-the-public-forum-writing-to-speak.md) — 3,148 w
- Source: `chapters/22-scripting-for-the-public-forum-writing-to-speak/`

## Chapter 23: Portfolio Reflection: Your Growth as a Writer
- **Drafted:** [23-portfolio-reflection-your-growth-as-a-writer.md](chapters/23-portfolio-reflection-your-growth-as-a-writer.md) — 3,352 w
- Source: `chapters/23-portfolio-reflection-your-growth-as-a-writer/`

---

**Total drafted: 74,684 words across 23 chapters.**

**Voice anchor:** `style/voice-anchor-ch04-literacy-narrative.md` (Bear's revised Ch 04, used as the voice spec for chapters 1–3, 5–23)

**Status:** All chapters are rough first drafts in Bear's approved voice. Source subfolders preserved pending review. Rewrites expected. Companion files (pantry, images, bookmaps) per State B procedure only completed for Ch 04; pending for the remaining chapters.

**Planned but not yet drafted:** Chapter 00 — Claude Basics. Will be written after a running project is selected (per the original curriculum-enrichment prompt's design).
# Writing Guide With LLMs

**Author:** Nik Bear Brown

**Folder:** `books/writing-guide-with-llms/`

---

## Overview

_No `book.md` / `_notes.md` overview available yet. Add a one-sentence description and audience note to populate this section._

---

## Table of Contents

<!-- TOC sourced from `_toc.md` -->

*All 23 chapters drafted in voice anchored by Bear's Ch 04 revision (saved to `style/voice-anchor-ch04-literacy-narrative.md`). Source subfolders preserved pending review. Rough drafts — to be rewritten.*

## Chapter 1: The Things We Carry: Experience, Culture, and Language
- **Drafted:** [01-the-things-we-carry-experience-culture-and-language.md](chapters/01-the-things-we-carry-experience-culture-and-language.md) — 2,369 w
- Source: `chapters/01-the-things-we-carry-experience-culture-and-language/`

## Chapter 2: The Digital World: Building on What You Already Know to Respond Critically
- **Drafted:** [02-the-digital-world-building-on-what-you-already-know-to-respond-critically.md](chapters/02-the-digital-world-building-on-what-you-already-know-to-respond-critically.md) — 3,779 w
- Source: `chapters/02-the-digital-world-building-on-what-you-already-know-to-respond-critically/`

## Chapter 3: Language, Identity, and Culture: Exploring, Employing, Embracing
- **Drafted:** [03-language-identity-and-culture-exploring-employing-embracing.md](chapters/03-language-identity-and-culture-exploring-employing-embracing.md) — 3,464 w
- Source: `chapters/03-language-identity-and-culture-exploring-employing-embracing/`

## Chapter 4: Literacy Narrative: Building Bridges, Bridging Gaps
- **Drafted (voice anchor):** [04-literacy-narrative-building-bridges-bridging-gaps.md](chapters/04-literacy-narrative-building-bridges-bridging-gaps.md) — 4,785 w
- Source: `chapters/04-literacy-narrative-building-bridges-bridging-gaps/`

## Chapter 5: Bridging the Divide Between Personal Identity and Academia
- **Drafted:** [05-bridging-the-divide-between-personal-identity-and-academia.md](chapters/05-bridging-the-divide-between-personal-identity-and-academia.md) — 2,396 w (bridge chapter)
- Source: `chapters/05-bridging-the-divide-between-personal-identity-and-academia/`

## Chapter 6: Memoir or Personal Narrative: Learning Lessons from the Personal
- **Drafted:** [06-memoir-or-personal-narrative-learning-lessons-from-the-personal.md](chapters/06-memoir-or-personal-narrative-learning-lessons-from-the-personal.md) — 3,333 w
- Source: `chapters/06-memoir-or-personal-narrative-learning-lessons-from-the-personal/`

## Chapter 7: Profile: Telling a Rich and Compelling Story
- **Drafted:** [07-profile-telling-a-rich-and-compelling-story.md](chapters/07-profile-telling-a-rich-and-compelling-story.md) — 3,192 w
- Source: `chapters/07-profile-telling-a-rich-and-compelling-story/`

## Chapter 8: Proposal: Writing About Problems and Solutions
- **Drafted:** [08-proposal-writing-about-problems-and-solutions.md](chapters/08-proposal-writing-about-problems-and-solutions.md) — 3,095 w
- Source: `chapters/08-proposal-writing-about-problems-and-solutions/`

## Chapter 9: Evaluation or Review: Would You Recommend It?
- **Drafted:** [09-evaluation-or-review-would-you-recommend-it.md](chapters/09-evaluation-or-review-would-you-recommend-it.md) — 3,343 w
- Source: `chapters/09-evaluation-or-review-would-you-recommend-it/`

## Chapter 10: Analytical Report: Writing from Facts
- **Drafted:** [10-analytical-report-writing-from-facts.md](chapters/10-analytical-report-writing-from-facts.md) — 3,252 w
- Source: `chapters/10-analytical-report-writing-from-facts/`

## Chapter 11: Rhetorical Analysis: Interpreting the Art of Rhetoric
- **Drafted:** [11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md](chapters/11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md) — 3,508 w
- Source: `chapters/11-rhetorical-analysis-interpreting-the-art-of-rhetoric/`

## Chapter 12: Position Argument: Practicing the Art of Rhetoric
- **Drafted:** [12-position-argument-practicing-the-art-of-rhetoric.md](chapters/12-position-argument-practicing-the-art-of-rhetoric.md) — 3,443 w
- Source: `chapters/12-position-argument-practicing-the-art-of-rhetoric/`

## Chapter 13: Reasoning Strategies: Improving Critical Thinking
- **Drafted:** [13-reasoning-strategies-improving-critical-thinking.md](chapters/13-reasoning-strategies-improving-critical-thinking.md) — 3,600 w
- Source: `chapters/13-reasoning-strategies-improving-critical-thinking/`

## Chapter 14: Argumentative Research: Enhancing the Art of Rhetoric with Evidence
- **Drafted:** [14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence.md](chapters/14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence.md) — 3,636 w
- Source: `chapters/14-argumentative-research-enhancing-the-art-of-rhetoric-with-evidence/`

## Chapter 15: Research Process: Accessing and Recording Information
- **Drafted:** [15-research-process-accessing-and-recording-information.md](chapters/15-research-process-accessing-and-recording-information.md) — 3,096 w
- Source: `chapters/15-research-process-accessing-and-recording-information/`

## Chapter 16: Annotated Bibliography: Gathering, Evaluating, and Documenting Sources
- **Drafted:** [16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md](chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md) — 2,741 w
- Source: `chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources/`

## Chapter 17: Case Study Profile: What One Person Says About All
- **Drafted:** [17-case-study-profile-what-one-person-says-about-all.md](chapters/17-case-study-profile-what-one-person-says-about-all.md) — 3,590 w
- Source: `chapters/17-case-study-profile-what-one-person-says-about-all/`

## Chapter 18: Navigating Rhetoric in Real Life
- **Drafted:** [18-navigating-rhetoric-in-real-life.md](chapters/18-navigating-rhetoric-in-real-life.md) — 2,383 w (bridge chapter)
- Source: `chapters/18-navigating-rhetoric-in-real-life/`

## Chapter 19: Print or Textual Analysis: What You Read
- **Drafted:** [19-print-or-textual-analysis-what-you-read.md](chapters/19-print-or-textual-analysis-what-you-read.md) — 2,950 w
- Source: `chapters/19-print-or-textual-analysis-what-you-read/`

## Chapter 20: Image Analysis: What You See
- **Drafted:** [20-image-analysis-what-you-see.md](chapters/20-image-analysis-what-you-see.md) — 3,181 w
- Source: `chapters/20-image-analysis-what-you-see/`

## Chapter 21: Multimodal and Online Writing: Creative Interaction Between Text and Image
- **Drafted:** [21-multimodal-and-online-writing-creative-interaction-between-text-and-image.md](chapters/21-multimodal-and-online-writing-creative-interaction-between-text-and-image.md) — 3,048 w
- Source: `chapters/21-multimodal-and-online-writing-creative-interaction-between-text-and-image/`

## Chapter 22: Scripting for the Public Forum: Writing to Speak
- **Drafted:** [22-scripting-for-the-public-forum-writing-to-speak.md](chapters/22-scripting-for-the-public-forum-writing-to-speak.md) — 3,148 w
- Source: `chapters/22-scripting-for-the-public-forum-writing-to-speak/`

## Chapter 23: Portfolio Reflection: Your Growth as a Writer
- **Drafted:** [23-portfolio-reflection-your-growth-as-a-writer.md](chapters/23-portfolio-reflection-your-growth-as-a-writer.md) — 3,352 w
- Source: `chapters/23-portfolio-reflection-your-growth-as-a-writer/`

---

**Total drafted: 74,684 words across 23 chapters.**

**Voice anchor:** `style/voice-anchor-ch04-literacy-narrative.md` (Bear's revised Ch 04, used as the voice spec for chapters 1–3, 5–23)

**Status:** All chapters are rough first drafts in Bear's approved voice. Source subfolders preserved pending review. Rewrites expected. Companion files (pantry, images, bookmaps) per State B procedure only completed for Ch 04; pending for the remaining chapters.

**Planned but not yet drafted:** Chapter 00 — Claude Basics. Will be written after a running project is selected (per the original curriculum-enrichment prompt's design).

---

_Generated overview-and-TOC README. Source files (`book.md`, `outline.md`, etc.) remain the working documents._

---

## What This Book Is

<!-- TODO: populate from chapter content -->

---

## Who This Book Is For

reader's roadmap)

This file is a stub. Sections 1–10 and 12–13 are placeholders for a later pass.
Section 11 (A note about AI) is substantive and written.

A good model for the full version: Pearl's "The Mind Over Data" introduction,
Molnar's Interpretable ML introduction. Both are argument-first and tell the
reader exactly what to expect from each chapter.
-->

# Introduction

<!-- [1] COLD OPEN
     A specific named scene with real stakes.
     No "this book will...", no throat-clearing.

---

## How to Read It

<!-- TODO: populate from chapter content -->

---

## Signature Simulations

<!-- TODO: populate from chapter content -->

---

## About the Author

**Nik Bear Brown** teaches at Northeastern University and writes across several modes — technical, pedagogical, and creative. Through [Musinique LLC](https://www.musinique.net/) he produces music and writes ghost-artist material; through [Bear Brown & Company](https://www.bearbrown.co/) he writes a working blog on AI methods; through [Humanitarians AI](https://www.humanitarians.ai/) he edits and publishes the work of OPT fellows.

He is the author of *Irreducibly Human*, *Computational Skepticism for AI*, and the *with LLMs* textbook series. The writing questions this guide asks are questions he engages every day in different keys.

He works in Boston. [nikbearbrown.com](https://www.nikbearbrown.com) · [irreducibly.xyz](https://irreducibly.xyz) · [skepticism.ai](https://www.skepticism.ai)

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in
any form or by any means without the prior written permission of the publisher,
except in the case of brief quotations in critical reviews and certain other
noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

First edition: 2026

