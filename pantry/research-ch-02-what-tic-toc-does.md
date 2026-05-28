# Research: Chapter 02 — What Tic TOC Does and Why You Spend Two Hours Here First
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students learn what Tic TOC's three disciplines enforce, how to deploy it, and why the TIKTOC.md session is the highest-leverage step in the pipeline.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

- **Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.).** ASCD. (First edition 1998.)
  The Backward Design framework — start with desired learning outcomes, then design assessments that would demonstrate those outcomes, then design instruction. Tic TOC's three-phase structure (intake → learning architecture → chapter architecture) is the Backward Design pipeline operationalized as a structured conversation. Where Wiggins & McTighe describe the workflow, Tic TOC enforces it via phase gates. Critically: "Stage 1: Identify Desired Results" in Backward Design is essentially what Tic TOC's /l1–/l4 produce, and Tic TOC's refusal to advance past /i4 without a confirmed Book Concept Summary is Backward Design's Stage 1 enforced as a software constraint.

- **Mager, R. F. (1962, revised 1997). *Preparing Instructional Objectives*.** Center for Effective Performance.
  The canonical text on behavioral learning objectives. Mager's three-part criterion — performance, condition, criterion — is the analytic foundation for Tic TOC's insistence on capability statements over topic headings. "Students will understand AI+1" is not a Mager objective; "Students will produce a TIKTOC.md that Cowork can execute without a clarifying conversation" is. Tic TOC's /c1 pushback ("rewrite as capability statement") is Mager applied in real time.

- **Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives*.** Longman.
  The revised Bloom's taxonomy (Remember, Understand, Apply, Analyze, Evaluate, Create) is the explicit vocabulary used in TIKTOC.md's "Learning Outcomes by Chapter" table — see Part 7 of the running TIKTOC.md, which lists each chapter's "Bloom's Ceiling." This source establishes the legitimacy of the practice; the chapter should cite it once and move on, because the reader doesn't need a course in educational psychology to use it.

- **Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New Products."** *Business Horizons*, 33(3), 44–54.
  The foundational text on phase-gated processes. Cooper's argument — that work flows through clearly bounded phases with explicit decision gates between them, and that compressing or skipping a gate produces compounding downstream cost — is exactly the architecture of Tic TOC. The chapter should name this lineage. It elevates Tic TOC from "another AI prompt" to "the application of forty years of operations research on phased work to instructional design."

- **Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems."** *Communications of the ACM*, 31(11), 1268–1287.
  The empirical foundation for "skipping requirements analysis is catastrophic." Curtis et al. document that defects introduced in requirements (the analog of the TIKTOC.md session) cost 10–100x more to fix downstream than defects introduced in implementation. This is the empirical case for the two-hour timebox: two hours up front saves dozens of hours of rewriting later. The chapter can quote the cost ratio directly.

### Key empirical cases

- **The "vibe coding" failure mode in software development (2024–2025 discourse).** Documented across X/Twitter, Hacker News threads, and posts by Simon Willison and others: developers who skip specification and prompt AI directly produce code that compiles, runs, and is structurally wrong. The fix-cost matches Curtis et al.'s ratio. This is the exact analog of "going straight to Cowork without a TIKTOC.md" — and many readers will have seen or felt it. Useful illustrative case.

- **The "RFP that produces a wrong proposal" case in agency work.** Documented anecdotally across design and consulting industry press: agencies that respond to vague RFPs produce technically competent proposals that miss the client's actual need, and the rework costs more than discovery would have. Mirrors the TIKTOC.md argument exactly. Illustrative composite.

- **The TIKTOC_prompt.md document (Bear Brown & Company, proprietary, 2025–2026).** This is the actual Tic TOC prompt. Present in the pantry at `/Users/bear/Documents/CoWork/bear-textbooks/books/ai+1/pantry/TikTOC_prompt.md`. Primary source for what Tic TOC literally does — should be referenced for any specific phase gate or command syntax. Flag as proprietary tooling.

---

## 2. The Core Concept — State of the Field

### What is settled

- Backward Design (Wiggins & McTighe) is the dominant framework in K-12 and increasingly in higher education for curriculum design. Few credentialed instructional designers would argue against it.
- Phase-gated processes outperform unstructured workflows in domains with high downstream rework cost (Cooper 1990; subsequent product development literature).
- Behavioral learning objectives in some form (Mager, or the Bloom's-revised Anderson-Krathwohl) are the standard analytic unit for curriculum specification. Pure topic-listing without learning outcomes is regarded as substandard practice.
- Specification quality predicts implementation quality. This is settled in software (Curtis et al.), product development (Cooper), and instructional design (Wiggins & McTighe).

### What is disputed

- **How rigid behavioral objectives should be.** A long tradition — Eisner's "expressive objectives" (1969), constructivist pedagogy generally — argues that pre-specified outcomes constrain genuine learning. Tic TOC's hard line on capability statements is closer to Mager's behaviorism than to constructivism. The chapter should acknowledge this tension rather than pretend it isn't there.
- **Whether AI-mediated discovery can substitute for human discovery.** Tic TOC is itself a hybrid — structured AI conversation. Some instructional designers may argue that authentic discovery requires human-to-human dialogue. The chapter's position is pragmatic: this works for solo author-instructors who do not have a curriculum committee.
- **The two-hour timebox.** Not empirically established. It is a heuristic — long enough for sustained judgment, short enough that a working professional will actually commit. The book should be honest that the number is a defensible heuristic, not a research finding.

### What has changed recently (last 5 years)

- 2020–2023: Backward Design was a paper-and-whiteboard exercise. AI tools were used for content generation, not specification.
- 2023–2024: Custom GPTs (OpenAI) and Claude Projects (Anthropic) made structured-conversation AI workflows practical. A specialized prompt with phase gates is now technically deployable in five minutes by a non-engineer.
- 2024–2025: The "AI-as-collaborator-on-specification" pattern emerged in software (Cursor's planning mode, Claude Code, Anthropic's "spec-driven development" framing). Tic TOC is the instructional-design version of this pattern.
- 2025–2026: The discourse has crystallized into "specs are the bottleneck" — see Karpathy 2025 "Software 3.0" framing, Geoffrey Litt's writing on prompt-as-spec, and Anthropic's own guidance for Claude Code. The chapter is therefore intellectually contemporary, not novel.

---

## 3. Application Domain Examples

For the graphic design / freelance design profession:

- **The brand identity brief.** A designer specifying a brand system before designing the logo — the brief enforces decisions about voice, audience, and constraints. Designers without a brief produce logos that look fine but miss the brand's actual position. The TIKTOC.md is the textbook's equivalent of a brand brief. Documented practice (any design management text).
- **The wireframe before the mockup.** A UX designer producing wireframes — explicitly low-fidelity — before any visual design. Skipping wireframes produces beautiful mockups that fail on information architecture. Same logic, same failure mode. Documented standard practice.
- **The discovery workshop.** A designer running a structured 90-minute discovery session with a client — pre-specified questions, agreed deliverables, decision gates — versus a designer who "kicks off" with a loose conversation. The first produces a workable brief in 90 minutes; the second produces three meetings of clarification. Illustrative; widespread practice.
- **The style guide as architecture.** A senior designer building a style guide for a junior designer to execute against. The style guide is the TIKTOC.md of brand work — it makes the system reproducible without the senior in the room. This is exactly the architectural function the chapter is teaching. Illustrative.
- **The "agency that skipped strategy" failure case.** Common in design industry press: agencies that move straight to creative without strategy produce work that wins client praise initially and fails on metrics. Mirrors the Cowork-dump failure mode at the agency scale. Illustrative.

---

## 4. The Book's Thesis Connection

The book's thesis: **the TIKTOC.md session is the highest-leverage step in the AI+1 pipeline; everything downstream is execution.** Chapter 1 made the fluency trap visceral. Chapter 2 is where the thesis becomes operative — where the reader sees the architectural response to the fluency trap and understands why two hours of structured conversation is not overhead but the product.

Chapter 2's specific contribution to the thesis:

1. **It locates the TIKTOC.md inside a forty-year research tradition.** By naming Wiggins & McTighe, Mager, and Cooper, the chapter establishes that Tic TOC is not a novel invention but the application of well-validated phased-design methodology to a new domain (AI-native textbooks). This protects the thesis from the "you're just selling a prompt" objection.

2. **It makes the cost ratio concrete.** Curtis et al.'s 10–100x downstream-fix-cost ratio is the empirical anchor. The chapter can say: in software, defects introduced at requirements cost 10–100x more to fix later. There is no reason to believe books are different. Two hours up front saves dozens of hours of rewriting. This is the thesis as arithmetic.

3. **It introduces the "product before process" pedagogical move.** Chapter 2's specified opening shows the ai-for-designers TIKTOC.md in full *before* explaining how it was produced. This works backward from the artifact to the method. It is the same move the book makes structurally — Chapters 1–2 show what AI+1 is; Chapters 3–11 show how to produce one. The chapter is the book in miniature.

4. **It seeds Chapter 4.** Every concept introduced in Chapter 2 (phase gates, three disciplines, capability statements, pushback) becomes operational in Chapter 4's worked walkthrough. Chapter 2 is the theory; Chapter 4 is the practice. If Chapter 2 is unclear, Chapter 4 cannot land.

5. **It defangs the "I already know my book" objection.** Exercise 3 explicitly asks the reader to write 200 words against this objection. The objection must be named and answered in the chapter body — it is the single most likely reason a domain expert will skip the TIKTOC.md session and produce a Cowork dump.

---

## 5. The AI Wayback Machine — Candidate Figures

- **Hilda Taba.** Wikipedia page title: "Hilda Taba." Estonian-American curriculum theorist; author of *Curriculum Development: Theory and Practice* (1962). Taba developed the inductive model of curriculum design — start from the specifics of student need and build the curriculum from the ground up — which is precisely the move Tic TOC enforces (start from the actual reader, work toward the book). Taba is non-Anglo (Estonian-born), female, and one of the most important curriculum theorists most students have never heard of. She is the strongest candidate for this chapter on both intellectual fit and diversity grounds. *Example prompt:* "Read the Wikipedia article on Hilda Taba. In 300 words, explain how her inductive curriculum model maps onto what Tic TOC's /i1 (audience intake) phase tries to enforce — and identify one place where Tic TOC departs from Taba's approach."

- **Madeline Hunter.** Wikipedia page title: "Madeline Hunter." Influential American educator (1916–1994); creator of the Instructional Theory into Practice (ITIP) model that systematized lesson planning into discrete gated phases (anticipatory set, objectives, input, modeling, checking, practice, closure). The phase-gate logic of Tic TOC is descended from Hunter's lesson-design model. *Example prompt:* "Read the Wikipedia article on Madeline Hunter. Identify three of her ITIP phases and map each to a Tic TOC phase or move."

- **Robert M. Gagné.** Wikipedia page title: "Robert M. Gagné." Author of *The Conditions of Learning* (1965) and the Nine Events of Instruction. Gagné is the canonical source for "different types of learning require different instructional sequences" — the analytical move Tic TOC makes when it asks the author what *kind* of capability the chapter produces (Apply vs. Evaluate vs. Create per Bloom). *Example prompt:* "Read the Wikipedia article on Robert M. Gagné. Pick one of his Nine Events of Instruction and explain how Tic TOC's chapter architecture phase (/c1) enforces it."

**Diversity assessment:** Taba provides both gender diversity and non-Anglo origin (Estonian). Hunter is American and female. Gagné is Anglo-American and male. Taba is the strongest single candidate. Recommendation: lead with Taba.

---

## 6. Pedagogical Delivery Research

**Prior knowledge required:** The reader needs Chapter 1 in hand — the fluency trap as a felt experience. Without that, Chapter 2's phase-gate argument sounds like bureaucratic process. With Chapter 1 in place, the phase gates read as "what catches the fluency trap before it becomes a chapter."

**Common misconceptions in the target reader (solo author-instructor / graphic designer):**

1. "Tic TOC is just a fancy outline." It is not. An outline is a list; the TIKTOC.md is an architecture with explicit learning outcomes, sequencing constraints, and downstream-execution requirements. The chapter must distinguish.
2. "I'll do my TIKTOC.md in my head and skip the conversation." This is the central failure mode the book argues against. Tic TOC's value is the pushback — the moments where the author discovers they don't yet know what they thought they knew. A solo head-conversation cannot produce pushback against itself.
3. "Two hours is too long for a conversation with an AI." The reader's prior experience with AI is short-form (chat). Two hours sounds like a meeting. The chapter must reframe: this is the entire book's discovery phase, not "a long chat."
4. "Phase gates feel rigid for creative work." This is the constructivist objection. The chapter should answer it: gates structure the work, they don't constrain the content. The author can write any book they want; the gates ensure they have *decided* what they want before drafting.

**Instructional sequences that work:**

- **Product before process.** The chapter's specified opening — show the finished TIKTOC.md before explaining the session that produced it — is the right move. The reader needs to see what the conversation produces before the chapter justifies the time investment.
- **Cost-comparison framing.** The Curtis et al. 10–100x ratio, ported to writing, makes the timebox argument visceral. "Two hours now versus twenty hours of rewriting later" is the line.
- **The three-discipline frame.** Curriculum theorist, acquisitions pragmatist, instructional designer — three roles, one prompt. Naming the disciplines (rather than calling them "modes" or "personas") connects to the broader literature and gives the reader something to look up.

**Teaching failure modes:**

- Lecturing on Bloom's taxonomy. The reader will glaze. Reference it, define the ceiling for each chapter, move on.
- Treating the phase gates as administrative. They are diagnostic. Each gate catches a specific failure mode. The chapter must name what each gate catches.
- Skipping the "what the session feels like" content block. The conversational texture is unfamiliar to most readers; without preparation, they will quit the session at the first piece of pushback.

**What makes understanding vs. memorization:** A reader who has memorized can name the three disciplines. A reader who understands can look at a vague book idea and predict which phase gate it will fail at — and what kind of pushback Tic TOC will give them. Exercise 2 (identifying two phase gate decisions in the TIKTOC.md excerpt and naming what Cowork would produce differently if each were vague) is the operationalized comprehension check.

---

## 7. Representation and Display Research

**Required display:** A structural diagram of the Tic TOC three-phase architecture. Each phase contains its sub-commands (/i1–/i4, /l1–/l4, /c1–/c4); each phase has explicit gates that prevent advancement until confirmation. This diagram should appear once in the chapter and be referenced by future chapters.

**Format suggestion:** A horizontal flow with three columns (Phase 1: Intake / Phase 2: Learning Architecture / Phase 3: Chapter Architecture). Each column lists its sub-commands. Between columns, draw explicit "gate" markers with the gate question ("Has the Book Concept Summary been confirmed?" "Have learning outcomes been mapped to Bloom's levels?" "Has every chapter received a capability statement?"). Cross-references to Cooper's Stage-Gate diagrams from the 1990 paper for visual lineage.

**Required display 2:** A multi-column comparison table — three disciplines × what each enforces × what Cowork produces if missing. Example row: "Curriculum theorist | Sequencing and prerequisite map | Chapters that demand knowledge the reader doesn't yet have."

**Source material:**

- The actual Tic TOC prompt (TikTOC_prompt.md, in pantry) is the primary source for command names and gate questions.
- For the diagram style, reference Cooper 1990 Figure 1 (the original Stage-Gate diagram).
- For the discipline-comparison table, draw on Wiggins & McTighe (curriculum theorist), publishing industry texts on acquisitions (e.g., Greco's *The Book Publishing Industry*), and ATD/ID literature for the instructional designer column.

---

## 8. Open Questions and Research Gaps

- **The TIKTOC.md format is proprietary.** It is a Bear Brown & Company / Cowork convention. There is no academic literature on the specific TIKTOC.md schema. The chapter must position it as "Cowork's implementation of a specification document," referencing the broader literature for legitimacy without overclaiming the schema's universality.
- **The two-hour timebox is heuristic.** It draws loosely on Ericsson-style deliberate-practice session lengths and the Pomodoro literature (Cirillo 2006), but no formal study establishes two hours as optimal for instructional-design conversation. Flag as practitioner heuristic.
- **The three-discipline framing is editorial.** Tic TOC's "curriculum theorist / acquisitions pragmatist / instructional designer" is a useful conceptual frame but is not a recognized triad in any field. The chapter should present it as a synthesis Tic TOC enforces, not as a citation-backed taxonomy.
- **Constructivist counterargument.** Eisner's "expressive objectives" (1969) and related literature push against behavioral objectives. The chapter does not need to settle this debate but must acknowledge it exists.
- **"Phase gates work better than no gates" — but is two phases enough? Five? Twelve?** The product-development literature gives no clean answer. Cooper's original Stage-Gate had five gates; modern lean-startup work has fewer. Three is defensible but not optimized.

---

## 9. Sourcing Notes

- **Wiggins & McTighe *Understanding by Design*:** ASCD book; not open access. The framework is widely summarized in free articles; for direct quotes, the ASCD edition is the citation. The Backward Design template is freely reproducible.
- **Mager *Preparing Instructional Objectives*:** Center for Effective Performance; commercially published. Mager's three-part criterion is widely paraphrased; cite Mager 1962/1997 for the framework but expect to paraphrase rather than quote.
- **Anderson & Krathwohl 2001:** Longman / Pearson; commercially published. The taxonomy table is widely reproduced under fair use.
- **Cooper 1990:** *Business Horizons* article. Available through institutional libraries; abstract is open. Worth tracking down the original for the Stage-Gate diagram.
- **Curtis, Krasner & Iscoe 1988:** *CACM* — available open access via the ACM Digital Library archive. Key paper to cite directly.
- **TIKTOC_prompt.md:** In pantry. Internal source — cite as "Bear Brown & Company, Cowork Tic TOC prompt, 2025–2026, proprietary."
- **Fact-checking priority for this chapter:** Curtis et al.'s exact cost-ratio language ("10–100x" vs. "10–200x" — different sources give different ranges). Pull from the original CACM paper.
- **AI Wayback figures:** Taba's Wikipedia article is shorter than Hunter's or Gagné's — verify before committing. May need to supplement with one of her books on first principles.
