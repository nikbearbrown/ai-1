# Chapter 4 — Tic TOC: Generating Your TIKTOC.md

*The two hours you spend here decide what the next two months produce.*

**One-line capability:** Students complete the full Tic TOC pipeline and produce a TIKTOC.md that Cowork can execute without a clarifying conversation.

---

## Learning objectives

By the end of this chapter you will be able to:

- (Apply) Complete the full Tic TOC intake sequence (/i1–/i4) for a real book project, producing a confirmed Book Concept Summary with thesis, learner profile, and deployment context.
- (Apply) Build the learning architecture (/l1–/l4): outcomes in Bloom's format, sequencing model, three-act arc, prerequisite dependency map.
- (Apply) Document every chapter (/c1–/c4): capability statement, opening strategy, worked example, assessable exercises, bridge question.
- (Evaluate) Run the 7 Adoption Failure Mode diagnostic (/g2) on a completed TIKTOC.md draft and identify the highest-risk structural problem before handing off to Cowork.
- (Create) Produce a TIKTOC.md that is complete enough for Cowork to run without a clarifying conversation.

---

## Opening — the question most authors cannot answer

Tic TOC's intake phase has four commands. The first is `/i1`. The second is `/i2`. The third is `/i3`. The fourth is `/i4`.

Each command asks several questions. The exact wording shifts across model versions; the substance does not. Here is one question that appears in every full Tic TOC session, somewhere in `/i1` or `/i2`:

> *In one sentence — not a paragraph — what does the reader LEARN?*

Read that question. Stop. Try to answer it for your own book.

If you can answer it in one sentence in under thirty seconds, you are in the small minority of authors who have already done the work this chapter teaches. Most cannot. Most authors discover, when they hit this question, that they do not yet know what their book *is*.

They have a topic. They have an outline. They have a strong sense that they have something to say. They have not yet compressed it into one sentence — and the act of compression turns out to be the hardest cognitive work in the entire pipeline.

Here is what the discovery feels like in practice. The author hesitates. Types a draft. Reads it back. Deletes it. Tries again. After five attempts, the draft reads: *"The reader learns how to use AI in their design practice."* That is a topic. Not a learning outcome.

Tic TOC will not let it stand. It will respond with something like:

> *That's a topic. A learning outcome names what the reader can do
> after the book that they cannot do before. "Use AI" is a category.
> What specific capability? "Defend an AI-assisted brand identity to
> a sceptical client without losing the account"? "Triage AI-generated
> moodboards into a workable presentation in ninety minutes"? Pick
> the one that, if your reader masters it, justifies the book.*

The author hesitates again. Now it is harder. Now they have to *choose* — to commit to one capability over another. The book they were going to write was about everything AI-related in their field. The book Tic TOC is about to help them write is about one specific thing the reader cannot do today and can do at the end.

That commitment is the chapter's whole point.

You will spend two hours on this. You will spend most of those two hours discovering what you did not yet know. This is the most cognitively expensive chapter in the book. It is also the chapter that, done well, saves you twenty or more hours of rewriting later. The 10–100x cost ratio from Curtis, Krasner, and Iscoe's 1988 software-engineering study applies here — defects introduced at specification cost an order of magnitude or two more to fix downstream.[^curtis] You are at specification.

Begin.

[^curtis]: Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287.

---

## 1. Phase One walkthrough — /i1 through /i4

Phase One is **Intake**. Four commands. Roughly forty-five minutes of session time when done well. The output is a confirmed Book Concept Summary — the document that anchors everything downstream.

Open your Claude Project with the Tic TOC prompt loaded (deployment in Chapter 2). Type `/i1`. Begin.

### /i1 — Book Intake

The first command asks the foundation questions. *What is the working title? What is the book about, in a paragraph the author would actually speak aloud? What does the reader learn — in one sentence? What is the central thesis — in one sentence?*

The questions are simple. The answers are not. The Phase One pushback pattern is identifiable across every full Tic TOC session this book has access to:

- **Vague topic answer** → Tic TOC asks for a specific capability.
- **List of topics** → Tic TOC asks which one is load-bearing.
- **Capability statement without a measurable outcome** → Tic TOC asks how you would know the reader could do it.
- **Thesis that anyone in the field would agree with** → Tic TOC asks what your book argues that competing books do not.

The fourth pushback is the hardest. A thesis that no one disagrees with is not a thesis — it is a topic restated. The acquisitions pragmatist discipline (introduced in Chapter 2) is asking: *what is your book's argument*, and the question is sharper than most authors expect.

Here is an annotated transcript fragment from the running example's `/i1`:

> **Tic TOC:** What does the reader learn — in one sentence?
>
> **Author:** The reader learns to use AI in their freelance design
> practice.

> **Tic TOC:** That is a topic. Not a learning outcome. Try: "The
> reader learns to [verb] [specific object] under [specific
> condition]." What is the one capability that, if mastered, justifies
> the book?

> **Author:** The reader learns to deploy AI in their design practice
> without losing the decisions their clients pay them to make.

> **Tic TOC:** Closer. "Deploy" is still vague. What does "deploy"
> look like as an action a reader could demonstrate?

> **Author:** The reader learns to identify which design decisions
> must stay human and which can be delegated to AI — and to defend
> that delegation map to a client.

> **Tic TOC:** Confirmed. That is a capability statement. Note: this
> statement now constrains every downstream chapter. Every chapter
> must contribute to either identification (which decisions stay
> human) or defense (how to articulate the delegation). Chapters that
> do neither are out of scope.

That last note is the *forcing function*. Once the capability statement is committed, the chapter list narrows. Topics that seemed essential ("intro to Midjourney") may no longer fit. Topics that seemed peripheral ("the disclosure conversation") may now be load-bearing.

### /i2 — Book Type and Deployment Context

`/i2` asks what *kind* of book this is and where the reader will use it. Practitioner handbook vs. course textbook vs. field-defining monograph vs. trade book. Self-directed read vs. workshop companion vs. course adoption.

The honest answer for most readers of *this* book — author-instructors building an AI+1 textbook — is **practitioner handbook**. Chapters organized by pipeline stage, each self-contained, the book usable as reference after first build. This determines downstream sequencing decisions in `/l2`.

Tic TOC will push back on misclassification. If you answer "trade book" but your chapters end with assessable exercises, the answer is wrong — trade books do not have assessable exercises. If you answer "course textbook" but your reader is a self-directed solo practitioner, the answer is also wrong.

### /i3 — Audience Intake (Learner Profile)

`/i3` is the gate where most authors lose the most time. The Chapter 2 worked example showed one full `/i3` exchange — the Maya conversation. The pattern is the same in every session: the author starts with a category and Tic TOC pushes for a person.

Phase One pushback typology, applied to `/i3`:

- "Designers" → Who, specifically? Name one.
- "Designers who use AI" → How long have they used it? What do they use it for? What have they avoided?
- "Mid-career designers" → What is the specific tenure? What is the specific client situation? What is the specific worry?

When the answer reaches a *person* — name, tenure, current client, current toolset, current worry — `/i3` is ready to mark passed.

### /i4 — Central Argument and Field Positioning

`/i4` is where the thesis gets sharp. You stated a thesis sentence in `/i1`; now Tic TOC asks it harder. *What is your book's specific argument? What do you argue that competing books do not? Where does this book sit on a shelf between which existing titles?*

The positioning move is borrowed from publishing acquisitions practice — the *vs.* statement. *Unlike X, which does Y, this book does Z.* If you cannot fill in X and Y, your book does not have positioning yet, and `/i4` will not pass.

The output of `/i4` is the gate to Phase Two. Tic TOC will explicitly state: *Phase One complete. Book Concept Summary ready for confirmation. Confirm, or revise?* Confirm. Move on.

---

## 2. Phase Two walkthrough — /l1 through /l4

Phase Two is **Learning Architecture**. Four commands. Roughly thirty to forty-five minutes when Phase One is solid. The output is the pedagogical spine — outcomes, sequence, arc, prerequisites.

### /l1 — Learning Outcomes (Bloom's-tagged)

`/l1` is the chapter where the curriculum theorist takes over. Tic TOC asks you to produce 3–5 learning outcomes *per chapter*, each tagged with a Bloom's level (Remember, Understand, Apply, Analyze, Evaluate, Create).

The Anderson-Krathwohl 2001 revision of Bloom's is the vocabulary.[^anderson] The verbs matter. *Understand* is a low-ceiling verb (the reader can explain). *Apply* is the working floor of a useful textbook (the reader can do it once, in a constrained context). *Evaluate* and *Create* are the high-judgment ceilings (the reader can assess, the reader can build).

A practitioner handbook should have **no chapter with an outcome below Apply as its ceiling**. The reader has not read a textbook to *understand* something — they read it to *do* something. If you write an outcome at Understand level, Tic TOC will push you to raise it.

Robert Mager's 1962 three-part criterion is the analytical foundation.[^mager] A real learning outcome names: the *performance* (what the reader does), the *condition* (under what circumstances), and the *criterion* (what counts as success). "The reader will understand the fluency trap" fails all three parts. "The reader will identify three fluency trap examples in their domain from research output, distinguishing the pattern of expert-detectable failure from generic AI errors" satisfies them.

Tic TOC's pushback on `/l1` follows a predictable shape:

- *Outcome at Understand only* → Tic TOC asks what the reader could *do* with the understanding.
- *Outcome verb too vague* → Tic TOC asks for a more specific verb (e.g., not "use" but "deploy under client questioning").
- *Outcome without condition or criterion* → Tic TOC asks how the reader would demonstrate mastery.

This is also where the *Create-level concentration* happens. The TIKTOC.md for ai-for-designers has three Create-level outcomes: domain research brief (Ch 3), TIKTOC.md itself (Ch 4), human rewrite (Ch 8). Same three for *this* book. The pattern is intentional — Create-level outcomes are concentrated at the three highest-judgment steps, and the rest of the chapters work toward and from them.

### /l2 — Sequencing Logic

`/l2` asks: in what order do the chapters appear, and why? Is the order chronological, conceptual, build-sequence, or by complexity? What dependencies exist between chapters?

For a practitioner handbook organized around a pipeline, the answer is build-sequence: each chapter produces an artifact that the next chapter consumes. This is what makes the bridge questions structurally load-bearing.

### /l3 — Three-Act Learning Arc

`/l3` is borrowed from narrative structure but applied pedagogically. Act One establishes; Act Two builds; Act Three applies. Each act has a *starting state* (what the reader knows entering) and an *ending state* (what the reader can do exiting), and the transition between acts has a specific condition.

For the ai-for-designers running example, the arc looks like this:

| Act | Starting state | Ending state | Transition condition |
|---|---|---|---|
| Establish (Ch 1–2) | Designer with AI curiosity, no framework. | Can identify fluency trap, name irreducibly human layer. | Reader can articulate the delegation principle. |
| Build (Ch 3–7) | Has framework, no working practice. | Has worked through IP, disclosure, client conversation, brand stewardship. | Reader has produced a defensible delegation map. |
| Apply (Ch 8–11) | Has working practice, no portfolio context. | Can defend AI-assisted work to a client; has a sustainable practice. | Reader can run the practice on the next live project. |

This is the pedagogical equivalent of three-act structure in screenwriting — Field's *Screenplay* (1979) is the canonical popular treatment, though the framework predates Field by millennia.[^field] What matters here is the *transition condition*. Without explicit conditions, the acts blur and the reader cannot tell when they are done with one and ready for the next.

### /l4 — Prerequisite Mapping

`/l4` asks what the reader must already know to start, what is addressed at first use via sidebars, and what is explicitly out of scope. The output is a small table — exactly the kind that appears in Part 6 of any complete TIKTOC.md.

The forcing function: anything you list as a prerequisite, the reader must *actually* have. Anything you list as "addressed at first use" requires you to write that sidebar somewhere. Anything you list as "explicitly out of scope" must be defended as out of scope (the *power of No*, in publishing acquisitions vocabulary).

For ai-for-designers: domain expertise (assumed); basic Claude familiarity (assumed); GitHub or file-system comfort (probably-assumed); Python and Markdown (not assumed, addressed at first use); legal training (explicitly not required, out of scope but pointed to qualified counsel).

Phase Two passes when these four outputs exist as documents Tic TOC can reference. The gate from /l4 to /c1 closes when learning outcomes are mapped to Bloom's levels with a defensible distribution.

[^anderson]: Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing*. Longman.
[^mager]: Mager, R. F. (1962, revised 1997). *Preparing Instructional Objectives*. Center for Effective Performance.
[^field]: Field, S. (1979). *Screenplay: The Foundations of Screenwriting*. Delta. The three-act frame is older than Field; modern Hollywood-canonical treatment.

---

## 3. Phase Three walkthrough — /c1 through /c4

Phase Three is **Chapter Architecture**. Four commands. Roughly forty-five minutes to an hour. The output is one TIKTOC.md entry per chapter, fully documented.

### /c1 — Chapter-by-Chapter Documentation

`/c1` is the engine room. For *every chapter* in your book, Tic TOC produces (or you produce, with Tic TOC pushing back) a structured entry with the following sections:

- **One-line capability** (what the reader learns to do)
- **Opening strategy** (typically failure-first; problem before solution)
- **Core content blocks** (4–5 per chapter)
- **Worked example** (the running example artifact at this stage)
- **Assessable exercises** (minimum three; Bloom's-tagged)
- **Bridge question** (what does the next chapter answer)

The capability statement is where most chapters fail and where `/c1` does its hardest work. Topic headings produce drift. Capability statements force commitment.

Here is the side-by-side comparison that is the heart of this chapter. Both versions are real entries from the same chapter of the ai-for-designers TIKTOC.md — one from the first-pass session (before /g2 was run), one from the revised version after pushback was honored. The comparison is the visualization of the chapter's central argument.

**Rushed-session entry — Chapter 3 (first-pass draft, pre-/g2):**

> ### CHAPTER 3 — The Fluency Trap
>
> **One-line:** Students learn about the fluency trap in graphic design.
>
> **Opening:** Discussion of how AI tools produce output that looks
> professional.
>
> **Core content blocks:** Examples of fluency trap; common patterns;
> how to recognize fluency trap; what to do about it.
>
> **Worked example:** AI-generated logo case study.
>
> **Exercises:** Identify a fluency trap example; reflect on
> implications; discuss with peer.
>
> **Bridge:** Now that you understand the fluency trap, we move on
> to copyright issues.

Read it. Notice what is *not* here.

The capability is at Understand level ("learn about"). The opening is described as a "discussion" — a topic, not a scene. The core content blocks are unordered topics, not sequenced moves. The worked example is named but not specified. The exercises are not Bloom's-tagged and "reflect" and "discuss" are sub-Apply verbs. The bridge is mechanical ("now that you understand X, we move on to Y") and does not commit to anything Chapter 4 must deliver.

**Full-session entry — Chapter 3 (revised, post-/g2 pushback honored):**

> ### CHAPTER 3 — The Fluency Trap in Design
>
> **One-line:** Readers learn to identify the seven fluency trap
> patterns in their own AI-assisted design work and to predict
> which patterns will collapse under specific kinds of client
> questioning.
>
> **Opening:** A senior designer's portfolio review — five pieces
> presented, four AI-assisted, the reviewer's pen pauses at the
> third. The reader reads the same five pieces and tries to predict
> which one the pen will land on.
>
> **Core content blocks:**
> 1. The fluency trap defined — Oppenheimer's processing fluency
>    framing, applied to design specifically
> 2. The seven patterns (typographic, brand-like-not-brand, additive
>    overload, polished-empty, variation overload, portfolio
>    misrepresentation, presentation collapse)
> 3. The three client-questioning failure modes (why-this-typeface,
>    revision-of-one-element, defend-the-rationale)
> 4. The pattern × question matrix — which patterns collapse under
>    which questions
> 5. The five-minute self-audit — running the patterns against
>    your own recent work
>
> **Worked example:** Three AI-assisted brand identities, all
> presented as finished, each demonstrating one or more fluency
> trap pattern. Side-by-side critique against the seven-pattern
> taxonomy.
>
> **Assessable exercises:**
> 1. (Analyze) Identify three fluency trap patterns in a piece of
>    your own AI-assisted work from the last six months.
> 2. (Evaluate) For each pattern, predict the client question that
>    would expose it.
> 3. (Create) Draft a 200-word defense-or-acknowledgment statement
>    for one piece of AI-assisted work you might present this week.
>
> **Bridge:** The fluency trap is now diagnosable in your own work.
> Identifying the trap is not enough — at some point the work must
> be presented and assigned to a client, and the legal question
> arrives. Chapter 4 addresses what you can actually assign.

Now read the two entries again, in order. The difference is the chapter's central argument made operational.

The Cowork outputs produced from these two entries differ accordingly. The rushed-session entry produces a Cowork draft that is roughly 3,000 words, organized around generic AI examples, with a discussion-style opening and exercises asking the reader to "reflect" and "consider." The full-session entry produces a draft that is roughly 4,500 words, scene-opens with a portfolio review, executes the seven-pattern taxonomy specifically, ends with a defense-rubric exercise the reader actually completes. **The difference is the spec.**

This is the most important figure in this book. [verify — the rushed-session source material may not exist in version history; if not retained, the comparison above is reconstructed from before-and-after fragments and should be flagged accordingly to the author. Per the highest-priority gap surfaced in the research pass for this chapter, the rushed-session counterpart for the running example needs to be confirmed against actual session logs.]

If you remember nothing else from this chapter, remember that the difference between those two TIKTOC.md entries is one hour of session time and one round of /g2 pushback — and that difference, propagated downstream across eleven chapters, is the difference between a book worth rewriting and a Cowork dump.

### /c2 — Chapter Anatomy Template

`/c2` formalizes what every chapter must contain. The default anatomy (used in this book) has ten items: title with italic subtitle, one-line capability, learning objectives, opening case, core content blocks, worked example, assessable exercises, bridge question, sidebars where applicable, pointer chapters where applicable. Three of these (opening case, worked example, bridge question) are load-bearing — a chapter missing them is incomplete and Cowork will be flagged at draft time.

### /c3 — Case Study and Worked Example Strategy

`/c3` decides the running-example strategy. The choice is between *one domain consistently* (the ai-for-designers strategy this book follows) vs. *rotating domains across chapters* (broader but with less narrative compounding). For practitioner handbooks, consistency typically wins.

### /c4 — Edge Cases, Contested Claims, Coverage Gaps

`/c4` is the honesty pass. What does the book claim that is *contested* in the field? What does it skip? What is the *aging risk* — content that will be wrong in two years? Everything in this section gets flagged for monitoring and for inclusion in the /p2 Open Questions Log.

Phase Three passes when every chapter has a `/c1` entry, the anatomy template is set, the running example strategy is committed, and contested claims are catalogued.

---

## 4. The /g2 diagnostic

`/g2` (or `/critique`) runs the 7 Adoption Failure Mode diagnostic on the completed TIKTOC.md. It is the chapter's culminating move and the gate to Cowork handoff.

The seven failure modes Tic TOC's `/g2` evaluates against are roughly: audience drift; missing prerequisites; over-claimed outcomes; under-specified deliverables; contested claims unflagged; bridge questions that do not bridge; capability statements that are actually topics [verify — exact seven-mode list against current TikTOC_prompt.md; the categories shift across prompt versions].

Each chapter's entry is read against each failure mode. Tic TOC produces a structured table: failure mode × chapter, with a status flag (PASS / WARNING / FAIL) and a one-line diagnostic per cell.

Here is a fragment of the `/g2` output run on the running example TIKTOC.md, lightly trimmed:

> | Failure Mode | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 7 |
> |---|---|---|---|---|---|---|---|
> | Audience drift | PASS | PASS | PASS | PASS | WARN | PASS | PASS |
> | Missing prerequisites | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
> | Over-claimed outcomes | PASS | PASS | WARN | PASS | PASS | PASS | PASS |
> | Under-specified deliverables | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
> | Contested claims unflagged | WARN | PASS | PASS | PASS | PASS | PASS | PASS |
> | Bridge fails to bridge | PASS | PASS | PASS | PASS | PASS | WARN | PASS |
> | Capability statement is topic | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
>
> *Five WARNINGS. Zero FAILs. Recommend resolving the Ch 3
> over-claim, the Ch 1 contested-claims flag, the Ch 6 bridge,
> and the Ch 5 audience-drift before Cowork handoff. Ch 1's
> contested claim is high-priority: the WEF "fastest-declining
> job" framing is genuinely contested in the literature and the
> chapter should flag it explicitly.*

This is what `/g2` looks like. Five WARNINGS. Each one is addressable in 10–20 minutes of focused revision. The chapter's argument for `/g2` is concrete here: the diagnostic catches problems that, propagated downstream, would each cost an hour or more of rewriting time at Chapter 7 (Cowork draft) or Chapter 8 (human rewrite).

After resolving the WARNINGS, you re-run `/g2`. If the second pass returns clean (all PASS), Cowork handoff is ready. If WARNINGS persist, you have two choices: resolve, or log to `/p2` as BLOCKED with explicit rationale. *Logged BLOCKED items are acceptable — unaddressed WARNINGS are not.*

The Marzano effect-size data for *identifying similarities and differences* gives the comparison move at the core of `/g2` an empirical anchor — Marzano, Pickering, and Pollock's 2001 meta-analysis assigned this instructional move an effect size of 1.61, among the highest in the meta-analysis.[^marzano] The `/g2` diagnostic is structured comparison at scale. It works.

[^marzano]: Marzano, R. J., Pickering, D. J., & Pollock, J. E. (2001). *Classroom Instruction That Works: Research-Based Strategies for Increasing Student Achievement*. ASCD.

---

## 5. What "ready for Cowork" means

Cowork is a downstream automated system. It reads your TIKTOC.md and your book directory and produces a complete rough draft of every chapter. It cannot ask you to clarify what you meant.

This is the practical implication. *Every section of your TIKTOC.md must be specific enough that a model reading it can produce a chapter without needing your judgment for any structural decision*. Voice can drift. Examples can be generic. Bridge questions can fail. But the *spec* itself cannot be ambiguous.

The checklist for "ready for Cowork":

1. **Every chapter has a capability statement at Apply level or above.** No "understand X" outcomes. Verbs are concrete and demonstrable.
2. **Every chapter has a Bloom's ceiling explicit in the outcome map.** Cowork uses this to calibrate cognitive demand.
3. **Every chapter has at least one Apply or above exercise.** Cowork uses these to structure the closing section of the draft.
4. **Every chapter has a bridge question that commits to the next chapter's content.** Cowork uses these for chapter handoffs.
5. **Every chapter has either a worked example specified or a placeholder with `[verify]` flag.** Cowork will not invent a worked example; if there is no instruction, the chapter will end without one.
6. **Every contested claim is flagged.** Cowork will write contested claims as if settled if you do not flag them. Then Chapter 11's Fact-Checking Assistant will catch the problem, expensively.
7. **`/g2` returns clean OR every WARNING is logged as BLOCKED in `/p2` with rationale.**
8. **`/p2` is current.** All open questions are catalogued; none are forgotten.

When all eight conditions are met, the TIKTOC.md is ready for Cowork. You can run Chapter 5's `new_book.py` confident that Cowork will have what it needs.

When any condition is unmet, *resolve before proceeding*. The 10–100x cost ratio applies. Every BLOCKED item that propagates to Chapter 7 (Cowork draft) costs roughly an hour of rewriting. Every BLOCKED item that propagates to Chapter 11 (final check) costs roughly a day.

---

## Worked example — the side-by-side comparison

The single most important visualization in this book is the side-by-side comparison of two TIKTOC.md chapter specs and their corresponding Cowork outputs. The rushed-session version came from the first pass of the ai-for-designers Tic TOC session; the full-session version came after `/g2` pushback was honored and the chapter entry was rewritten.

The Chapter 3 entries themselves appear in section 3 of this chapter above. What follows is the *Cowork output fragment* produced from each spec, lightly trimmed for the page.

**Cowork output from rushed-session entry — Chapter 3 opening:**

> ## Chapter 3 — The Fluency Trap
>
> In this chapter we will discuss the fluency trap in graphic design.
> AI tools have become widely used in design workflows, and one of
> the challenges designers face is that AI output often looks
> professional and finished, even when it lacks the strategic depth
> or craft judgment that defines high-quality design work. This
> chapter explores what the fluency trap is, why it matters, and
> what designers can do about it.
>
> Many designers report being surprised by how good AI-generated
> work looks at first glance. They also report that closer inspection
> often reveals problems. Understanding this dynamic is important
> for any designer working with AI tools.
>
> [continues for ~2,800 more words in similar register]

Generic register. *"In this chapter we will discuss"* is exactly the phrase a practitioner-handbook chapter must not begin with. No scene. No specific reader. No specific designer in a specific moment. The chapter is *about* the fluency trap without ever *demonstrating* it.

**Cowork output from full-session entry — Chapter 3 opening:**

> ## Chapter 3 — The Fluency Trap in Design
>
> *The dangerous AI output is not ugly. It is attractive enough to
> stop your judgment too early.*
>
> A senior brand director leans over a portfolio review at a London
> agency, 2026. Five pieces on the table. Four were assisted by AI
> in some part of the workflow; the reviewer does not know which.
> Her pen pauses at the third piece — a healthcare consulting
> identity. She points to a single decision in the wordmark and
> asks: "Why did you choose this terminal stroke weight?"
>
> The designer hesitates.
>
> The reader reads the same five pieces, on the following pages, and
> tries to predict before turning each page which one the pen will
> land on. The exercise is at the chapter's spine because the
> diagnostic skill it builds is the spine: you will learn to see
> the fluency trap before your reviewer does.
>
> [continues into the seven-pattern taxonomy]

Scene first. Specific moment. Specific reader-task. The chapter is *demonstrating* the fluency trap in the act of opening with it.

**This is the chapter's argument made concrete.** One hour of Tic TOC pushback, honored. Eleven chapters of compounded downstream effect. The whole book turns on the diff between those two openings.

If the rushed-session source material does not exist in your own version history, you can produce an approximate comparison by writing a deliberately-vague chapter entry, running it through Cowork, then writing the version-with-pushback-honored, running *that* through Cowork, and comparing. The exercise is reproducible. **[verify — the actual rushed-session TIKTOC.md for the running example must be confirmed against session logs; the comparison above is the most defensible reconstruction.]**

---

## Exercises

### Exercise 1 (Apply) — Complete /i1–/i4. Share confirmed Book Concept Summary.

With the brief from Chapter 3 loaded into your Claude Project, run `/i1` through `/i4`. Answer every question. Honor the pushback. Do not advance through a gate until Tic TOC explicitly confirms the gate has passed.

**Time required:** 45–75 minutes.

**Deliverable:** A confirmed Book Concept Summary saved to a file. Includes working title, capability statement (one sentence), central thesis (one sentence), reader profile, deployment context, positioning vs. comparable texts.

### Exercise 2 (Apply) — Complete /l1–/l4. Produce outcome map table.

Continue the session into Phase Two. Produce 3–5 learning outcomes per chapter, each Bloom's-tagged. Document the sequencing logic. Map the three-act arc. Resolve prerequisites.

**Time required:** 30–45 minutes.

**Deliverable:** A complete outcome map table (chapter × Bloom's ceiling × Create-level outcome). Three-act arc documented. Prerequisite table complete.

### Exercise 3 (Apply) — Document three chapters using /c1. Each must have capability statement and bridge question.

Use `/c1` to document *three* chapters of your book in full. Each must include: capability statement (Apply or above), opening case, core content blocks (4–5), worked example, assessable exercises (≥3, Bloom's-tagged), bridge question.

**Time required:** 30–60 minutes (10–20 minutes per chapter, with pushback).

**Deliverable:** Three complete `/c1` entries. The bridge questions must be structurally committed — each must name what the next chapter will deliver.

### Exercise 4 (Evaluate) — Run /g2. Name highest-risk failure mode and one structural change.

Run `/g2` on your three-chapter TIKTOC.md fragment. Read the diagnostic output. Identify:

- The single highest-risk failure mode flagged across your three chapters.
- One concrete structural change to your TIKTOC.md that would mitigate it.

**Time required:** 15–25 minutes.

**Deliverable:** A 200–400 word memo naming the failure mode, the chapter it affects, the predicted downstream cost if unaddressed, and the proposed structural change.

### Exercise 5 (Create) — Produce complete TIKTOC.md — all chapters, /g2 passed, /p2 current.

Complete the full Tic TOC session for your book. Document every chapter via `/c1`. Run `/g2`. Resolve every WARNING — or log to `/p2` as BLOCKED with rationale. Run `/g1` to compile the full TOC into one document.

**Time required:** 60–120 minutes for the remaining chapters; total session time across all five exercises will be 3–4 hours, typically across two sittings.

**Deliverable:** A complete TIKTOC.md file saved at `TIKTOC.md` in your book directory (Chapter 5 creates the directory; for now save anywhere). Every chapter documented. `/g2` returns clean or all WARNINGS logged. `/p2` current. **This is the Create-level deliverable for this chapter and the highest-leverage artifact in the entire book.**

---

## Still puzzling

- *Is two hours the right timebox?* It is heuristic. Ericsson's 1993 deliberate-practice literature supports 60–90 minute focused sessions;[^ericsson] Cirillo's Pomodoro literature supports 25-minute cycles within longer work blocks.[^cirillo] Sweller's Cognitive Load Theory predicts that holding all of a book's design decisions in working memory simultaneously is infeasible, which is what makes the phase structure necessary regardless of total time.[^sweller] Two hours is a defensible composite but not optimized.
- *Can Tic TOC be replaced by a human collaborator?* For a solo author-instructor without a curriculum committee or co-author, Tic TOC is the best available proxy. It is not equal to a human collaborator with relevant expertise. A practicing acquisitions editor or instructional designer reading your draft TIKTOC.md will catch things Tic TOC misses (and miss things Tic TOC catches). Both is best. One is workable. Zero is the Cowork-dump path.
- *Will Tic TOC's pushback behavior age well across model versions?* The transcripts in this chapter were captured against Claude as of May 2026. The *structural moves* (gates, capability statements, bridge questions) are stable. The *texture* of the pushback shifts as the underlying model updates. The chapter's transcripts will read as period pieces in eighteen months even if the methodology survives.
- *How much of the TIKTOC.md schema is universally portable?* The instructional-architecture principles (Backward Design, Bloom's, phase-gating) are widely accepted in instructional design. The specific TIKTOC.md file format is Bear Brown / Cowork convention. A different publishing toolchain could adopt different conventions; the underlying moves remain.

[^ericsson]: Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance." *Psychological Review*, 100(3), 363–406.
[^cirillo]: Cirillo, F. (2006/2018). *The Pomodoro Technique*. Currency.
[^sweller]: Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 12(2), 257–285.

---

## What would change my mind

I would revise this chapter's central claim — that the TIKTOC.md session is the highest-leverage step in the AI+1 pipeline — if a controlled comparison emerged showing that authors who skipped the formal session and went straight to Cowork-with-pantry produced final drafts of equivalent quality after human rewrite, with comparable or lower total time investment. Such a study does not exist. The chapter's confidence rests on three converging analogs: Curtis-Krasner-Iscoe's 1988 software-engineering cost ratio (10–100x downstream rework cost for upstream defects); Wiggins and McTighe's Backward Design Stage 1 argument that the most-skipped step is the highest-leverage one; and the practitioner experience of authors who have completed both paths and report the same pattern. If those analogs fail — if textbook drafting turns out to be structurally unlike software development or curriculum design in some unexpected way — then the two-hour upfront investment loses its arithmetic justification, and the pipeline reorganizes around a different gate.

A second condition: I would revise if Cowork itself evolved sufficient context-handling that it could conduct the structured-conversation step *during* drafting rather than as a separate phase, collapsing the spec-and-execute distinction into a single longer dialogue. This is plausible in 18–36 months. The chapter remains current under May 2026 conditions; the pipeline reorganizes when the underlying capability does.

---

## AI Wayback Machine — Donella Meadows

> **Prompt to run in Claude or ChatGPT:**
>
> "Read the Wikipedia article on Donella Meadows. Summarize her concept
> of 'leverage points' in systems. Identify which of her twelve
> leverage points the TIKTOC.md session operates at — and explain why
> this matches the book's claim about the session being the 'highest-
> leverage step.'"

Meadows was an environmental scientist and systems theorist whose 1972 *Limits to Growth* and posthumous 2008 *Thinking in Systems* established the vocabulary for analyzing *where* in a system intervention matters most. Her twelve leverage points run from least powerful (changing parameters) to most powerful (transcending paradigms). Her argument — *the structure of a system determines its behavior* — is the deep intellectual ancestor of this chapter's argument that the TIKTOC.md, as the book's structural specification, determines downstream chapter outputs. The Wikipedia article is substantive; the prompt asks you to read it once and write a 300-word memo. [^meadows]

[^meadows]: Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green. Posthumous; edited by Diana Wright. The original 1999 essay *Leverage Points: Places to Intervene in a System* is also widely available online.

---

## Bridge — Chapter 5

The TIKTOC.md exists. It sits in a markdown file on your disk, or in your Claude Project, or in both. Every chapter is documented. `/g2` returned clean — or every WARNING was resolved or logged as BLOCKED with explicit rationale. `/p2` is current.

The highest-leverage step in the AI+1 pipeline is now complete. Two hours, give or take. The rest of the pipeline is execution. You will be the editor of what comes back from Cowork — not the writer of the first draft.

But Cowork needs somewhere to write. It needs a directory structure, a metadata file, a build script, and the TIKTOC.md sitting where it can read it. None of that exists yet on your disk.

Chapter 5 creates the directory. The command is one line. The output is forty files. It takes thirty seconds.

Then the pipeline runs.
