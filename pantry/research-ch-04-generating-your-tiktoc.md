# Research: Chapter 04 — Tic TOC: Generating Your TIKTOC.md
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students complete the full Tic TOC pipeline and produce a TIKTOC.md that Cowork can execute without a clarifying conversation.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

- **Alexander, C. (1977). *A Pattern Language: Towns, Buildings, Construction* (with Ishikawa & Silverstein).** Oxford University Press.
  Alexander's argument that design specifications are themselves a creative product — that the description of a pattern *is* the design — is the deep intellectual ancestor of the TIKTOC.md as artifact. *A Pattern Language* is structured almost identically to a TIKTOC.md: explicit problem statement, context, the pattern in a single declarative sentence, then the elaboration. The chapter should name this lineage. It positions the TIKTOC.md not as documentation-of-the-real-work but as the real work.

- **Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.).** ASCD.
  Stage 1 of Backward Design — "Identify Desired Results" — is the analytical task the TIKTOC.md session executes. Wiggins & McTighe describe Stage 1 as the most-skipped and highest-leverage step in curriculum design. The TIKTOC.md session is Stage 1 with a forcing function. The chapter should make this connection explicit: the two-hour Tic TOC session is Backward Design's Stage 1 enforced by software.

- **Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning."** *Cognitive Science*, 12(2), 257–285.
  Cognitive Load Theory — the empirical foundation for why the Tic TOC session is divided into phases. Holding all the design decisions of a book (audience, outcomes, sequence, chapter content) in working memory simultaneously is cognitively impossible for non-specialists. Phasing the conversation is what makes it tractable. Sweller's framework gives the chapter the vocabulary to explain *why* the phase structure exists, not merely that it does.

- **Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance."** *Psychological Review*, 100(3), 363–406.
  The source of the "deliberate practice" framework and the empirical case for sustained focused sessions of roughly 60–90 minutes as the practical upper bound for high-quality cognitive work. Ericsson's research is the closest published anchor for the two-hour timebox the chapter argues for — interpreted as one extended deliberate-practice session with appropriate breaks. Use this carefully; Ericsson did not study textbook design.

- **Cirillo, F. (2006/2018). *The Pomodoro Technique*.** Currency.
  The popular treatment of focused-work session structure. Less rigorous than Ericsson but more widely known to the target reader. Use briefly to justify the within-two-hours pacing pattern (work-break-work) the chapter recommends for the Tic TOC session.

- **Marzano, R. J. (2007). *The Art and Science of Teaching: A Comprehensive Framework for Effective Instruction*.** ASCD.
  Marzano's research-based instructional strategies include identifying similarities and differences (i.e., comparison) as among the highest-effect-size instructional moves (Marzano, Pickering & Pollock 2001 meta-analysis put it at an effect size of 1.61). This is the empirical justification for the chapter's most important pedagogical move: the side-by-side comparison of two TIKTOC.md chapter specs (one rushed, one done well) and the corresponding Cowork outputs. The whole chapter pivots on this comparison; Marzano gives it research grounding.

- **The TIKTOC.md document itself (Bear Brown & Company, the running compilation).** The book's own running example. Cited from `/Users/bear/Documents/CoWork/bear-textbooks/books/ai+1/TIKTOC.md`. Primary source for what a complete TIKTOC.md looks like.

### Key empirical cases

- **The ai-for-designers TIKTOC.md (in production at the time of writing).** The book's running example. Must be produced from a real Tic TOC session per TIKTOC.md Open Question #1 — this is the highest-priority production constraint for the entire book. The side-by-side comparison in Chapter 4 cannot be invented.

- **Software requirements engineering field studies (Curtis, Krasner & Iscoe 1988; Carmel & Becerra-Fernandez subsequent work).** Empirical research on what happens when requirements are skipped: 10–100x downstream rework cost. The analog for textbooks is documented less rigorously but practitioners report the same pattern. Use Curtis et al. as the empirical anchor; flag the textbook analogy as inference.

- **The "vibe coding" phenomenon (2024–2026).** Documented across the practitioner community (Karpathy 2025, Simon Willison's blog, Hacker News discussions): the failure mode of going straight to AI code generation without specification. Direct analog of the Cowork dump. Useful as a reader-recognition case.

---

## 2. The Core Concept — State of the Field

### What is settled

- Specification quality predicts implementation quality. Settled across software (Curtis et al. 1988), product development (Cooper 1990 Stage-Gate), and curriculum design (Wiggins & McTighe).
- Cognitive load is bounded; complex specification tasks must be phased. Settled in Sweller's tradition and subsequent decades of CLT research.
- Comparison (side-by-side examination of similar artifacts) is among the highest-effect-size instructional strategies (Marzano et al. 2001 meta-analysis).
- Pattern languages — and structured specification artifacts more broadly — are themselves creative products, not preparation for the creative product (Alexander 1977).
- A capability statement ("students will produce X") is more useful than a topic statement ("we will cover X") for guiding both writing and assessment (Mager 1962; Wiggins & McTighe 2005).

### What is disputed

- **Whether a structured AI conversation can substitute for a human collaborator at the specification stage.** Skeptics argue the discovery happens in the interaction between the AI's pushback and the author's response — but only a human collaborator (a curriculum committee, an editor, a co-author) can do the actual disagreeing. The chapter should be honest: Tic TOC is the best available proxy for the solo author-instructor; it does not equal a human collaborator.
- **Whether two hours is the right timebox.** Heuristic, not empirically derived. Ericsson supports 60–90 min focused sessions; Cirillo's Pomodoro structure supports 25-min cycles. Two hours is a defensible composite; not optimized.
- **Whether all the load-bearing decisions can be made in one session.** Some authors will need multiple sessions. The chapter should treat one session as the design target while acknowledging that BLOCKED items (per /p2) can be resolved later.
- **Whether the three-discipline framing (curriculum theorist / acquisitions pragmatist / instructional designer) is the right partition.** Editorial choice; defensible but not validated against alternatives.

### What has changed recently (last 5 years)

- 2020–2022: Curriculum specification was paper or whiteboard work; AI tools were used post-specification for content generation.
- 2023: ChatGPT and Claude made "conversational" specification feasible. Custom GPTs (Nov 2023) and Claude Projects (mid-2024) made phased structured-prompt workflows deployable in minutes by non-engineers.
- 2024: Spec-driven development emerged in software (Karpathy's "Software 3.0," Geoffrey Litt's writings, GitHub's Spec Kit). The pattern of "specification-as-artifact" gained discourse mass.
- 2025: Long-context models (Claude with 200k+ token context, Gemini's 1M+ tokens) made it possible for a single conversation to hold an entire book's specification. The TIKTOC.md session became technically feasible only in the last 18 months from this draft's writing.
- 2026: The discipline of "spec-first AI work" is now mainstream in software. Tic TOC is the instructional-design version of a now-recognized methodology. The chapter is intellectually contemporary, not novel.

---

## 3. Application Domain Examples

For the graphic design / freelance design profession (the running domain):

- **The brand identity strategy document.** Designers producing a brand strategy doc (positioning, audience, voice, visual principles) before any visual work. The strategy doc is the TIKTOC.md of brand identity. Skipping it produces logos that look fine but miss the brand's actual market position. Documented standard practice in design strategy texts (Wheeler's *Designing Brand Identity*).

- **The wireframing-then-mockup discipline in UX.** Wireframes are explicitly low-fidelity and structural; mockups are visual execution. A UX team that conflates them produces beautiful mockups that fail on information architecture. Exact analog: TIKTOC.md is the wireframe; Cowork draft is the mockup. Documented in any UX textbook (Garrett's *The Elements of User Experience*).

- **The design brief as forcing function.** A senior designer requiring a junior to produce a brief before any visual work — the brief catches the junior's vague thinking before it becomes expensive visual work. Same logic, same gate.

- **The pattern library or design system specification.** A design system spec is the TIKTOC.md of a multi-product design effort. Without it, each product team produces aesthetically inconsistent work that costs more to harmonize later than to specify up front. Documented at companies that publish their design systems (IBM Carbon, Google Material, Salesforce Lightning).

- **The "AI-assisted moodboard rejection" case.** A designer using Midjourney to produce 50 moodboards and presenting all 50 to a client — the client cannot choose because the designer has not done the strategic narrowing. The narrowing is the spec; the moodboards are the draft. Without spec, draft is overload. Illustrative.

---

## 4. The Book's Thesis Connection

The book's thesis: **the TIKTOC.md session is the highest-leverage step.** Chapter 4 is where the thesis becomes the chapter. This is the chapter the entire book exists to deliver.

Per TIKTOC.md Part 11, Chapter 4 is named explicitly as "the hardest to draft" and "cannot be invented." The side-by-side TIKTOC.md comparison is "the most important figure in the book." This is the chapter where the thesis is *demonstrated*, not argued.

Chapter 4's specific contributions:

1. **It makes the thesis concrete.** Chapter 1 made the fluency trap visceral. Chapter 2 argued architecturally for the TIKTOC.md. Chapter 4 *shows* — via the side-by-side comparison — exactly what changes when the session is done well vs. done badly. The reader sees two Cowork outputs for the same chapter spec, where the only difference is the upstream specification quality. The difference is the argument.

2. **It produces the highest-leverage deliverable in the book.** Per TIKTOC.md Part 7, only three chapters produce Create-level outcomes: Ch 3, Ch 4, Ch 8. Of these, Ch 4 produces the TIKTOC.md itself — the artifact that determines every downstream chapter's quality. The reader leaves Chapter 4 with the document that determines the next eight chapters' value.

3. **It operationalizes the thesis at the chapter scale.** The /g2 diagnostic is the thesis as procedure — the explicit check that the TIKTOC.md is ready for Cowork. Until /g2 passes, the thesis remains untested; once /g2 passes, the rest of the pipeline runs from a foundation the thesis predicts will produce a book worth rewriting.

4. **It teaches the difference between capability statement and topic heading.** This is the thesis at the sentence scale. A topic heading ("Color theory") produces a Cowork draft about color theory. A capability statement ("Students will select a color palette for a brand identity and justify each choice against the brand's audience and positioning") produces a Cowork draft that teaches a skill. The book's whole argument lives in this distinction.

5. **It introduces the "what would Cowork do with this?" reading discipline.** Once the reader can look at a TIKTOC.md section and predict what Cowork will produce from it, they have internalized the thesis. This skill carries through Chapters 5–11 — every downstream chapter asks the reader to evaluate output by reference to specification quality. Chapter 4 is where the skill is built.

6. **It defines "ready for Cowork."** This is the chapter's load-bearing line. Without this definition, the pipeline cannot run; with it, the pipeline runs and the human is repositioned as editor. The thesis becomes operative at this line.

Chapter 4 seeds Chapters 5–11 in a specific way: every later chapter's failure modes trace back to TIKTOC.md weaknesses. Chapter 7's "five things Cowork reliably gets wrong" — voice drift, fabricated specificity, missing domain judgment, padded middle, bridge questions that don't bridge — are each diagnosable as a specific TIKTOC.md gap. The reader who completes Chapter 4 well experiences these failures less; the reader who rushes Chapter 4 experiences them as the dominant problem. Chapter 4 is where the book's downstream difficulty is set.

---

## 5. The AI Wayback Machine — Candidate Figures

- **Donella Meadows.** Wikipedia page title: "Donella Meadows." Environmental scientist, lead author of *The Limits to Growth* (1972), author of *Thinking in Systems: A Primer* (posthumous 2008). Meadows is the canonical figure for "the structure of a system determines its behavior" — which is exactly the argument the chapter makes about TIKTOC.md. The TIKTOC.md is the book's structural specification; the chapter outputs reflect the structure. Female, American, lesser-known to undergraduates. Strong candidate on both intellectual fit and gender diversity. *Example prompt:* "Read the Wikipedia article on Donella Meadows. Summarize her concept of 'leverage points' in systems. Identify which of her twelve leverage points the TIKTOC.md session operates at — and explain why this matches the book's claim about the session being the 'highest-leverage step.'"

- **Christopher Alexander.** Wikipedia page title: "Christopher Alexander." Architect, mathematician, author of *A Pattern Language* (1977) and *The Timeless Way of Building* (1979). Alexander's career was an argument that specifications can themselves be creative artifacts — that a well-written pattern is the design, not its preparation. Direct intellectual ancestor of the TIKTOC.md philosophy. Anglo-Austrian-American, male — does not contribute to diversity but is the strongest intellectual fit. *Example prompt:* "Read the Wikipedia article on Christopher Alexander. In 300 words, explain how his concept of a 'pattern language' maps onto what a TIKTOC.md is — and identify one feature of his patterns that the TIKTOC.md schema lacks."

- **John Seely Brown.** Wikipedia page title: "John Seely Brown." Former Chief Scientist at Xerox PARC; author of *The Social Life of Information* (with Paul Duguid, 2000) and influential work on situated learning and "learning ecologies." Brown is the figure for "learning environments are designed, and the design determines what is learned." Strong fit for Chapter 4's argument that the TIKTOC.md is the book's learning architecture. American, male — does not add diversity. *Example prompt:* "Read the Wikipedia article on John Seely Brown. Identify one principle of his 'learning ecologies' framework. Explain how a well-built TIKTOC.md operationalizes that principle for a textbook."

- **Lera Boroditsky.** Wikipedia page title: "Lera Boroditsky." Cognitive scientist; researcher on linguistic relativity. Boroditsky's work establishes that the structures we use to specify shape what we can think — which is the argument for capability statements vs. topic headings. Non-Anglo by origin (born in Belarus), female, contemporary. Optional alternative for diversity considerations. *Example prompt:* "Read the Wikipedia article on Lera Boroditsky. Explain how her research on language and cognition supports the chapter's argument that a capability statement produces different downstream content than a topic heading."

**Diversity assessment:** Meadows provides gender diversity. Boroditsky provides both gender and non-Western origin (Belarusian). Alexander is the strongest pure intellectual fit but adds no diversity. Recommendation: lead with Meadows (gender diversity + the leverage-point framing is a near-perfect match for the chapter's "highest-leverage step" thesis); flag Boroditsky as alternative if Chapters 1–3 already use a female figure (Suchman in Ch 1, Taba in Ch 2, Scher in Ch 3) and the book needs non-Western breadth.

---

## 6. Pedagogical Delivery Research

**Prior knowledge required:** Chapter 3's deliverable (a four-section domain research brief) in hand. Chapter 2's vocabulary (phase gates, three disciplines, capability statement, pushback) in active memory. Without Chapter 3, /i1 cannot run productively. Without Chapter 2's vocabulary, the chapter's transcript excerpts will feel opaque.

**Common misconceptions in the target reader (solo author-instructor / graphic designer):**

1. "Once I open the Tic TOC prompt, the AI does the work." It does not. Tic TOC's value is the pushback; if the reader accepts the first answer Tic TOC offers, they have produced a Cowork dump's worth of preparation in two hours instead of two days. The chapter must teach pushback-receiving as a skill.
2. "I should be able to finish in 30 minutes if I really know my book." Counter-intuitive. The authors who finish fastest are typically those who do not yet realize how vague their thinking is. The chapter must reframe: the value of the session is found in the friction, not the speed.
3. "My answers should be polished." They should not. The session is dialogue, not deliverable. Polished answers often paper over weak specification. The chapter should encourage messy, exploratory answers — Tic TOC's job is to push them toward precision.
4. "If Tic TOC challenges my answer, I should defend it." Sometimes. Often the challenge is finding what the author didn't yet know. The chapter must teach a triage move: when to defend (Tic TOC misunderstands the domain), when to accept (Tic TOC caught real vagueness), when to ask Tic TOC to elaborate (the challenge is unclear).

**Instructional sequences that work:**

- **Question-first opening.** The chapter's specified opening — quoting the /i1 Q2 question ("In one sentence — not a paragraph — what does the reader LEARN?") — is the right move. The reader feels the difficulty of the question before the chapter explains the methodology behind it. Most readers cannot answer Q2 well on first attempt; this is the productive entry point.
- **Annotated transcript excerpts.** Showing real session transcript with annotations about what Tic TOC was looking for and what the author's responses revealed. This is the chapter's only way to teach pushback-receiving as a skill. The transcripts must be real (per TIKTOC.md Open Question #2).
- **Side-by-side comparison.** Two TIKTOC.md chapter specs and their Cowork outputs. The chapter's load-bearing figure. The Marzano effect-size data justifies it as the dominant instructional move.
- **/g2 walkthrough as final synthesis.** Running /g2 on the running example TIKTOC.md and seeing what it caught — this is the chapter's culminating move. It demonstrates the diagnostic as concrete, not abstract, and shows the author what "ready for Cowork" looks like in practice.

**Teaching failure modes:**

- Treating the chapter as a software walkthrough. It is not — it is a chapter about a conversation. The phases and commands are scaffolding for the conversation; the chapter's heart is the conversational texture.
- Showing only successful sessions. Readers learn pushback-receiving by seeing pushback they recognize as productive. The chapter should show at least one transcript excerpt where the author resisted Tic TOC's challenge initially and then conceded.
- Over-specifying the deliverable. The TIKTOC.md is large; the chapter cannot walk the reader through every section. The chapter must teach the *moves* (capability statement vs. topic heading, bridge question as structural commitment, /g2 as diagnostic) and let readers transfer those moves to their own session.

**What makes understanding vs. memorization:** A reader who has memorized can run /i1–/c4 and produce a TIKTOC.md file. A reader who understands can look at any section of their TIKTOC.md and predict what Cowork will produce from it — and rewrite the section if the prediction is "a generic chapter." The /g2 diagnostic operationalizes this comprehension, but the reader must be able to perform the prediction without /g2's prompting for the chapter to have succeeded.

---

## 7. Representation and Display Research

**Required display 1: The side-by-side TIKTOC.md comparison.** Per TIKTOC.md Part 11, this is "the most important figure in the book." Two chapter specs and their resulting Cowork outputs. Must be real, must be from the ai-for-designers running example.

**Format suggestion:** Four-quadrant layout (2×2):
- Top-left: TIKTOC.md chapter spec — rushed session (vague capability statement, missing learning outcomes, generic bridge question).
- Top-right: TIKTOC.md chapter spec — full session with pushback honored (specific capability statement, Bloom's-labeled outcomes, structurally committed bridge question).
- Bottom-left: Cowork output produced from top-left spec — annotated to show generic phrasing, missing domain specificity, padded middle.
- Bottom-right: Cowork output produced from top-right spec — annotated to show domain-anchored opening, named trade-offs, bridge that actually bridges.

The reader's eye should travel L-R across the top (spec quality differs) and then T-B in each column (spec quality propagates downstream). This is the visual realization of the thesis.

**Required display 2: The /g2 diagnostic output on the running example.** A structured table showing each category /g2 evaluates and what it found for ai-for-designers — including the items that were flagged and fixed before Cowork handoff. This makes the diagnostic concrete and gives the reader a checklist they can compare their own /g2 output against.

**Required display 3: Capability statement vs. topic heading — paired examples.** A small comparison table showing 5–6 paired examples (Topic: "Color theory" → Capability: "Students will select a color palette for a brand identity and defend each choice against the brand's audience and positioning"; Topic: "AI tools for designers" → Capability: "Students will compare three AI image generators on the same brief and identify which is suited to each phase of their workflow"; etc.). This is the chapter's most reusable artifact for the reader's own session.

**Source material:** All displays draw from the actual ai-for-designers TIKTOC.md and a paired "rushed-session" version that must be produced specifically for this chapter (per TIKTOC.md Open Question #2). The rushed version cannot be fully invented — but a real session's first draft (before /g2 fixes) may be sufficient if such an artifact was retained.

---

## 8. Open Questions and Research Gaps

- **The rushed-session TIKTOC.md spec for the side-by-side comparison.** This is the single highest-priority research gap. The comparison cannot be invented. The most defensible source: the early draft of the actual ai-for-designers TIKTOC.md before /g2 was run — if version control retained it. If not, the chapter's load-bearing figure is at risk. Flag this as a production constraint to the author.
- **The exact Tic TOC phase commands (/i1, /l1, /c1, /g2, /p2).** These are proprietary Cowork/Bear Brown syntax. The chapter must reference them as they exist at draft time; flag as current-state and pipe to "online prompt library" for the canonical reference. Aging risk: medium-high.
- **The two-hour timebox.** No empirical study supports two hours specifically. The chapter's defense draws on Ericsson (deliberate practice), Cirillo (Pomodoro), and Sweller (cognitive load) — but the synthesis is editorial. Acknowledge.
- **The "three disciplines" framing.** Editorial. Defensible as a synthesis but not a recognized triad in any field.
- **Tic TOC's pushback behavior.** Will vary across model versions of Claude (the underlying model). The chapter's transcript excerpts will age in tone if not in substance. Flag as current-state.
- **Whether the entire workflow generalizes beyond solo author-instructors.** Untested for collaborative authoring teams. The book scopes itself to the solo case; the chapter should not overclaim.

---

## 9. Sourcing Notes

- **Alexander 1977 *A Pattern Language*:** Out of print in original hardcover but widely available used and through Oxford University Press reprints. Quotations of the pattern format are well-documented in subsequent design and software literature; cite Alexander directly for the foundational claim.
- **Wiggins & McTighe 2005:** See Chapter 2 sourcing notes. Backward Design's Stage 1 is the key citation for this chapter.
- **Sweller 1988:** *Cognitive Science* journal article; available through institutional libraries. CLT is widely summarized in textbook treatments (Sweller's own subsequent books are accessible).
- **Ericsson, Krampe & Tesch-Römer 1993:** *Psychological Review*; widely accessible. The "deliberate practice" framing is famous; cite the original paper for the empirical claim about session structure, not the popular Gladwell-mediated "10,000 hours" version.
- **Cirillo 2006/2018 Pomodoro Technique:** Trade book; quotable. Use only for the within-session pacing claim, not as research authority.
- **Marzano, Pickering & Pollock 2001 *Classroom Instruction That Works*:** ASCD book. The meta-analytic effect sizes are the cited result; the 1.61 effect size for identifying similarities and differences is the specific number to cite.
- **TIKTOC.md itself:** Cite the project's own running TIKTOC.md as `/Users/bear/Documents/CoWork/bear-textbooks/books/ai+1/TIKTOC.md` (or its published equivalent).
- **TikTOC_prompt.md:** Cite as "Bear Brown & Company, Cowork Tic TOC prompt, 2025–2026, proprietary."
- **Fact-checking priority for this chapter:** The transcript excerpts from the ai-for-designers session — every quoted exchange must be verifiable against the actual session log. The /g2 output for the running example must match the actual /g2 run. These are the highest-stakes facts in the chapter; they cannot be paraphrased loosely.
- **AI Wayback figures:** Meadows's Wikipedia article is substantive; the *Thinking in Systems* leverage-points chapter is widely summarized online. Alexander's article is comprehensive. Boroditsky's is shorter but adequate. Verify all three at draft time.
- **Production constraint (per TIKTOC.md Open Questions #1 and #2):** This chapter cannot be drafted until the ai-for-designers TIKTOC.md is built from a real session and the rushed-session counterpart exists. Flag prominently to the author before drafting begins.
