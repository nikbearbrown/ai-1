# Research: Chapter 10 — Enrichment: The LLM Layer
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students run the enrichment pipeline to add domain-specific, hands-on LLM integration to every chapter and evaluate whether the result meets the AI+1 standard.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

**Paulo Freire. *Pedagogy of the Oppressed* (1968; English 1970).** Continuum. The text behind the phrase "education is never neutral." Freire's argument against the "banking model" of education (teacher deposits knowledge, student stores it) is the deep-source argument for why generic LLM exercises fail: they treat the learner as a container for transferable content rather than as a domain-situated practitioner. The AI+1 standard ("could this exercise appear in a different field's textbook unchanged? If yes, it fails.") is Freire's "banking model" critique translated to AI pedagogy.

**bell hooks. *Teaching to Transgress: Education as the Practice of Freedom* (1994).** Routledge. Extends Freire with the explicit claim that pedagogy must be *engaged* — must take the learner's specific context, body, history, profession seriously. hooks's "engaged pedagogy" is the closest direct match for what an AI+1 LLM Exercise is trying to be. (Wikipedia: "bell hooks" — substantial entry, page title lowercase per her stylization.)

**Maxine Greene. *Releasing the Imagination* (1995).** Jossey-Bass. American philosopher of education; argues that imagination — the capacity to see what is not yet — is the educable faculty. For Chapter 10, this is the argument for why LLM exercises must do more than test recall: they should prompt the student to *imagine* applications of AI in their own practice the textbook author has not anticipated.

**Doug Lemov. *Teach Like a Champion* (2010; 3.0 ed. 2021).** Jossey-Bass. The K–12 craft-of-teaching reference. Relevant techniques for Chapter 10: "No Opt Out" (every exercise has a path to a correct answer the student must traverse), "Stretch It" (good exercises produce follow-up questions), "Cold Call" (questions presume the student will answer). Translates to LLM exercises that *demand engagement* rather than offer optional enrichment.

**Howard Barrows and Robyn Tamblyn. *Problem-Based Learning: An Approach to Medical Education* (1980).** Springer. The canonical PBL text. Argument: students learn by working on problems that mirror the actual conditions of practice, not by abstract content delivery. For AI+1, the analogy is exact: an LLM exercise must mirror a real domain task the reader will face, not a stylized abstraction.

**Eric Mazur. *Peer Instruction: A User's Manual* (1997).** Prentice Hall. Mazur's concept-inventory research at Harvard physics produced the empirical case that traditional lecture pedagogy fails at the *application* layer — students who pass exams cannot apply concepts to novel situations. Concept Inventories (Force Concept Inventory, Hestenes Wells Swackhamer 1992) operationalize the assessment. Relevant to Chapter 10's "AI+1 standard": an exercise that the student can pass without domain knowledge does not measure the right thing.

**Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, Graham Neubig. "Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in NLP" (*ACM Computing Surveys*, 2023).** The survey paper for prompt engineering as a field. Establishes that *task-specific* prompts dramatically outperform generic ones for non-trivial work — empirical underpinning for the AI+1 "domain-specific or it fails" claim.

**Anthropic. "Prompt engineering overview" (Anthropic docs, anthropic.com/docs).** The current-state practitioner reference for Claude prompting. The "be specific" guidance, the "give Claude a role" guidance, and the "use examples (multishot prompting)" guidance are all directly applicable to LLM Exercise design. Cite as current-state; expect interface drift.

**Sara Ahmed. *Living a Feminist Life* (2017).** Duke. The "diversity work" chapter — the institutional reality of representation as labor, not gesture. Relevant to the *AI Wayback Machine*'s diversity tracking: representation in historical figures must do epistemic work in the chapter, not appear as a sidebar.

### Key empirical cases

**The Force Concept Inventory (Hestenes, Wells, Swackhamer 1992).** Empirical demonstration that students who passed traditional physics courses retained Aristotelian intuitions about force. Established the field of physics education research. The AI+1 analog: students who complete a textbook full of generic LLM exercises will retain *generic prompting habits* and fail to apply LLMs to their domain. The exercise has to test the domain integration, not the prompt syntax.

**Wiki Education ("Wikipedia in the Classroom" program, 2010–present).** WikiEdu.org. Empirical case for using Wikipedia editing as a graduated educational exercise — students do research, write for a public audience, get peer review through Wikipedia's processes. Directly applicable to the AI Wayback Machine: the exercise is *Wikipedia-instruction* not *Wikipedia-summary*, and the precedent for that pedagogy exists.

**Carnegie Mellon Open Learning Initiative (OLI).** Open educational platform with embedded formative assessments. Empirically demonstrated learning gains by surfacing student misconceptions early. Argument for placement: enrichment exercises must come *inside* chapters, not be banished to an appendix.

---

## 2. The Core Concept — State of the Field

### What is settled

- Hands-on practice with domain-specific examples produces transfer; abstract examples mostly do not (transfer research, 50+ years).
- Concept inventories detect application-layer failures that exams miss (Mazur, Hestenes lineage).
- Prompt engineering for non-trivial tasks requires task-specific structure (Liu et al survey).
- Generic AI-literacy curricula fail to produce domain-integrated practitioners (early findings, 2024–2025).
- Diversity of examples and historical figures changes who feels included as a potential practitioner (decades of representation research; Steele on stereotype threat is adjacent).

### What is disputed

- Whether LLM exercises should be *graded* (treated as assessment) or *ungraded enrichment* (treated as scaffolding). The AI+1 series picks "embedded enrichment" but this is one position among several.
- Whether students should be required to use a specific LLM (Claude, ChatGPT, Gemini) or be allowed to choose. Trade-off: reproducibility of the exercise vs. tool freedom.
- Whether the "AI+1" framing — domain expert plus AI fluency — names a real economic and pedagogical category or whether it will collapse as LLMs become more domain-aware out of the box. The book's position is the former. The latter is the most credible threat to the thesis.
- Whether decolonizing-the-curriculum work (representation in scientific lineage, broader epistemic base) is pedagogically necessary, ethically necessary, or politically motivated. The book treats it as pedagogically and ethically necessary.

### What has changed recently (last 5 years)

- LLMs have moved from novelty to integrated practitioner tool across knowledge-work professions (2022–2026). The empirical reality the book is responding to.
- "Prompt engineering" emerged, professionalized, and partially dissolved into "AI fluency" as a general literacy (2023–2025).
- Domain-tuned LLMs and RAG (retrieval-augmented generation) systems have started displacing general-chat use for professional work, which changes what an LLM exercise should look like.
- Textbooks with embedded LLM components have appeared (early examples, mostly low-quality) — the field is rapidly forming and the AI+1 series is positioning inside it.
- "Decolonizing the curriculum" movement has produced peer-reviewed methodology in education journals; no longer a fringe critique.

---

## 3. Application Domain Examples (graphic design)

1. **Brief intake with Claude — fluency trap edition.** The exercise: paste a real client brief into Claude and ask for a moodboard concept. Then audit the output for what's missing — the client's actual taste history, the unspoken constraints, the political dynamics inside the client organization. The point is not that Claude is bad; it is that the irreducibly human content is what the freelance designer *uniquely possesses*.

2. **Variant generation with Midjourney + judgment.** The exercise: produce eight variants of a logo concept with Midjourney. Then write 200 words on which two survive a real designer's review and why. Tests the *taste calibration* irreducibly human layer named in Chapter 1.

3. **Adobe Firefly Generative Fill as production tool, not concept tool.** The exercise: identify three places in a recent project where Firefly would have saved time at the *production* stage (background extension, object removal) versus zero places where it should have generated *concepts*. The AI+1 line in the practitioner's actual workflow.

4. **Figma AI Make and the design-system question.** The exercise: ask Figma AI to generate a sign-up form for a brand whose design system you've already built. Audit for design-system drift. Score on a 5-point scale: drift in type, drift in color, drift in spacing, drift in component vocabulary, drift in tone.

5. **The portfolio review LLM check.** The exercise: paste a portfolio site URL into Claude and ask "what does this designer claim to be good at?" The point: does Claude's read match the designer's intent? Where it diverges is the *positioning gap* the designer needs to close — the meta-skill the AI exposes.

---

## 4. The Book's Thesis Connection

This is the chapter where the book's central thesis returns at the pedagogical scale. Chapter 1 names the fluency trap in the reader's own domain. Chapter 10 demonstrates that the same fluency trap can poison the *teaching* of AI fluency if the textbook author isn't careful. A generic LLM exercise — "Ask Claude to explain X" — is itself a fluency-trap artifact. It looks pedagogical. It teaches nothing the reader couldn't get from the Claude documentation.

The AI+1 standard — "could this exercise appear in a different field's textbook unchanged? If yes, it fails." — is the *thesis enforcement mechanism* at the exercise layer. It is the same logic as Chapter 8's Combined Test, applied to LLM enrichment instead of prose.

This is also the chapter where *who is teaching* becomes a content choice. The AI Wayback Machine deliberately surfaces figures whose contributions have been historically under-credited. The reader who learned in Chapter 3 to combine three LLMs for triangulation now learns in Chapter 10 to triangulate historical credit. Both are anti-fluency-trap moves.

The strongest thesis connection: this chapter argues that *good pedagogy is local*. Freire and hooks make the philosophical argument. The AI+1 standard makes the operational argument. The TIKTOC.md session enforces it structurally — the chapter list, the reader profile, the contested claims, all feed into LLM exercise generation. The local-pedagogy thesis is what makes the TIKTOC.md the highest-leverage step, because a vague TIKTOC.md produces generic exercises and a sharp TIKTOC.md produces AI+1 exercises. The two artifacts are causally linked.

---

## 5. The AI Wayback Machine — Candidate Figures

**Candidate 1: bell hooks (Wikipedia: "bell hooks")** — STRONG. Substantial Wikipedia page. Substantive connection: *Teaching to Transgress* (1994) is the textbook for *why* local, engaged, domain-specific pedagogy works — which is the AI+1 standard's intellectual foundation. Satisfies criteria: Black woman (diversity on race and gender), undergrad-accessible (widely taught), lesser-known in *AI pedagogy* contexts even if well-known in education theory. Example prompt: *"Visit the Wikipedia page for bell hooks. Read about *Teaching to Transgress* and 'engaged pedagogy.' In 250 words, explain why hooks would predict that generic LLM exercises will fail to produce competent practitioners. Then revise one LLM Exercise in your draft to be more 'engaged' in hooks's sense — name the specific learner context you are now addressing."*

**Candidate 2: Paulo Freire (Wikipedia: "Paulo Freire")** — STRONG. Brazilian, non-Western, foundational education theorist. Substantive connection: the banking-vs-problem-posing model is the deep-source argument against generic AI exercises. Satisfies criteria: non-Western figure (diversity), undergrad-accessible (cited in any introductory education course), lesser-known in AI pedagogy specifically. Example prompt: *"Visit the Wikipedia page for Paulo Freire. Read about *Pedagogy of the Oppressed* and the 'banking model.' In 200 words, identify three LLM Exercises in current AI tutorials that exemplify the banking model. Then propose what their problem-posing versions would look like for your textbook's reader."*

**Candidate 3: Maxine Greene (Wikipedia: "Maxine Greene")** — Wikipedia page exists. Substantive connection: argued that imagination — seeing what does not yet exist — is the educable faculty. Directly relevant to the AI Wayback Machine, which uses historical figures to expand the reader's sense of who counts as a contributor to the field. Satisfies criteria: woman, lesser-known outside philosophy of education, undergrad-accessible. Example prompt: *"Visit the Wikipedia page for Maxine Greene. Read about her concept of 'releasing the imagination.' In 200 words, propose an LLM Exercise that does not test knowledge but trains imagination — the capacity to see an AI application in your domain no one has tried yet."*

**Recommendation:** Lead with bell hooks (strongest fit, name recognition, direct intellectual lineage). Freire as the non-Western alternate. Greene as the back-pocket option for chapters where imagination/futures framing is the right move.

**Diversity assessment for Chapter 10:** All three candidates are diverse — two women (hooks, Greene), one Black woman (hooks), one non-Western (Freire, Brazilian). This is the chapter that carries the diversity weight across Chs 9–11.

---

## 6. Pedagogical Delivery Research

Chapter 10's pedagogical structure must do three things at once: teach the reader to run the enrichment generator, teach the reader to *evaluate* its output by the AI+1 standard, and teach the reader to *revise* failing exercises. The TIKTOC.md exercise set (Apply, Evaluate, Apply) hits all three.

**Worked-example design (high-stakes for this chapter).** TIKTOC.md specifies "Two LLM Exercises for the same chapter — generic vs. AI+1." This is the figure that does the load-bearing work, analogous to the TIKTOC.md side-by-side in Chapter 4 or the Cowork-vs-rewrite side-by-side in Chapter 8. Production constraint: both versions must come from real exercise generation runs. The generic version cannot be a strawman.

**Pedagogical risk.** Readers will read the AI+1 standard and either (a) agree and apply it casually without internalizing why, or (b) over-apply it to the point that every exercise becomes hyper-specific and untransferable. Chapter must give a *bound* — the standard says "could this appear in a different field's textbook unchanged?" not "could this appear in a different *sub-specialty* of design unchanged?" The line is at field, not subspecialty.

**Bridge-question discipline.** Chapter 10's bridge to Chapter 11 must do work the chapter would otherwise have to do explicitly: "LLM layer in place. Book content-complete. One final check before the build." This is the structural commitment that 11 is the *check-and-publish* chapter, not a content-additions chapter.

---

## 7. Representation and Display Research

The AI Wayback Machine is itself a representation device. The chapter's job is to make that explicit rather than implicit. Three operating principles:

1. **Substantive connection only.** A figure included for representation but whose work does not connect to the chapter's argument *fails the AI+1 standard at the figure-selection layer*. The same anti-fluency-trap logic applies: a token figure is a tokenized chapter.
2. **Diverse on multiple axes.** Gender, geography, era, discipline. Across Chs 9–11 the targets are at least one woman and at least one non-Western figure. Chapter 10 carries the weight (hooks, Freire, Greene all satisfy).
3. **Wikipedia-page-exists check.** Every AI Wayback figure must have a substantial Wikipedia entry, because the example prompts send the reader there. A figure without a page (or with a stub) cannot anchor an exercise.

**Display question.** How is the Wayback figure introduced in the chapter? TIKTOC.md does not specify whether each chapter has *one* Wayback figure or whether they accumulate. Author decision required. Recommendation: one per chapter, surfaced inline at the moment its work bears on the argument, not as a sidebar biography.

**Representation in worked examples.** The graphic-design running example must itself represent the field's diversity. The "designer" archetype defaults to a particular cultural reference set; conscious work is required not to default to Bauhaus + Pentagram as the only lineage. Counter-examples to surface: Cipe Pineles (first woman art director at a mainstream US magazine), Sister Corita Kent (serigraph design as social practice), Saki Mafundikwa (*Afrikan Alphabets*).

---

## 8. Open Questions and Research Gaps

- **AI+1 standard sourcing.** The standard ("could this exercise appear in a different field's textbook unchanged?") is original to this book — no external citation. Strongest adjacent literature is PBL (Barrows & Tamblyn) and engaged pedagogy (hooks). The book is the source. Flag in metadata.
- **Wikipedia-as-textbook-source ethics.** The AI Wayback Machine sends students to Wikipedia. Wikipedia is an excellent starting point and an inadequate ending point. Chapter must handle this — probably with a *"verify a Wayback claim against a second source"* sub-exercise.
- **Exercise generation tooling.** TIKTOC.md mentions the "With LLMs Curriculum Enrichment Generator." Like CAJAL, this is internal AI+1 toolchain. Teach the function, not the tool — the function survives a toolchain refactor.
- **AI+1 standard at sub-field level.** Open question: should the standard test against *adjacent* fields (graphic design vs. product design) or only *distant* fields (graphic design vs. accounting)? The book's current position is "distant"; needs explicit defense.
- **What happens when LLMs become domain-aware out of the box.** Five-year aging risk: if Claude in 2030 is natively excellent at graphic-design judgment, does the AI+1 framing collapse? Counter-argument: the irreducibly human layer (client relationships, taste calibration) is not what LLMs are improving at. But the book should acknowledge the threat.

---

## 9. Sourcing Notes

- Freire: *Pedagogy of the Oppressed*, 30th-anniversary ed. (Continuum, 2000) is the standard reference; Wikipedia "Paulo Freire" is substantial.
- bell hooks: *Teaching to Transgress* (Routledge, 1994); Wikipedia "bell hooks" — note lowercase per her stylization.
- Greene: *Releasing the Imagination* (Jossey-Bass, 1995); Wikipedia "Maxine Greene."
- Lemov: *Teach Like a Champion 3.0* (Jossey-Bass, 2021).
- Barrows & Tamblyn: *Problem-Based Learning* (Springer, 1980).
- Mazur: *Peer Instruction* (Prentice Hall, 1997); Hestenes et al "Force Concept Inventory" *Physics Teacher* 1992.
- Liu et al "Pre-train, Prompt, and Predict": *ACM Computing Surveys* vol. 55, no. 9 (2023).
- Anthropic prompting docs: docs.anthropic.com — current-state, expect drift.
- Wiki Education: wikiedu.org — confirmed live, well-documented pedagogy.
- Ahmed: *Living a Feminist Life* (Duke, 2017).
- Pineles, Kent, Mafundikwa: cited for representation in graphic-design lineage; *Afrikan Alphabets* (Mark Batty Publisher, 2004).

**Flag — original framework:** The AI+1 standard, the AI Wayback Machine concept, and the fluency-trap-at-pedagogy-scale claim are original to this book series. They need internal sourcing (Chapters 1, 2, 4) but have no external citation. This is acceptable for a thesis-driven practitioner handbook; flag transparently.
