# Research: Chapter 07 — Chapter Writing: The Cowork Draft Run
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students run the Chapter Writer prompt and evaluate the rough draft output — identifying what it did well, what it got wrong, and what the human rewrite must supply.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

- **Feynman, Richard P. (1963–1965, reissued continuously). *The Feynman Lectures on Physics*, vols. I–III, with Robert Leighton and Matthew Sands.** The reference work for "first-principles clarity." The lectures' opening — "If, in some cataclysm, all of scientific knowledge were to be destroyed, and only one sentence passed on... what statement would contain the most information in the fewest words?" — is the rhetorical posture AI+1 calls "Feynman voice." Cite the Caltech online edition (free, current).

- **Attenborough, David (1979–present).** *Life on Earth* (1979) is the foundational text; *Planet Earth* (2006), *Blue Planet II* (2017) are the contemporary references. There is no single "paper" — the citation is the body of work. The voice is narrative explanation: scene first, mechanism second, scale shift third. The book's "Attenborough × Feynman" voice combines narrative documentary with first-principles physics.

- **Pinker, Steven (2014). *The Sense of Style: The Thinking Person's Guide to Writing in the 21st Century.*** Pinker's "classic style" — the writer points at something in the world; the reader looks. This is the operative model for what Cowork is *trying* to produce and what it fails at. Pinker's chapter on the "curse of knowledge" is essential for the chapter's diagnosis of why LLMs over-explain.

- **Strunk, William and E. B. White (1959, revised 2000). *The Elements of Style.*** "Omit needless words." The chapter's "padded middle" failure mode is a direct application. Strunk & White is the rule set the human rewrite enforces and that Cowork systematically violates.

- **Zinsser, William (1976, 7th ed. 2006). *On Writing Well.*** The handbook of nonfiction prose. Zinsser's "the secret of good writing is to strip every sentence to its cleanest components" is the surgical move the human rewrite makes. Especially relevant: Zinsser's chapter "Bits and Pieces" on transitions — what Cowork's bridge questions get wrong.

- **Didion, Joan (1976). "Why I Write." New York Times Book Review.** "Grammar is a piano I play by ear." Useful one-line citation in the chapter's discussion of voice as something you *recognize* but cannot fully specify. Voice drift in LLMs is failure to play by ear.

### Key empirical cases — LLM failure modes

- **Ji, Ziwei et al. (2023). "Survey of Hallucination in Natural Language Generation." ACM Computing Surveys 55(12).** The most-cited survey of LLM hallucination types. Distinguishes intrinsic hallucination (contradicts source) from extrinsic (cannot be verified from source). The chapter's "fabricated specificity" failure mode is extrinsic hallucination.

- **Lin, Stephanie, Jacob Hilton, and Owain Evans (2022). "TruthfulQA: Measuring How Models Mimic Human Falsehoods." ACL 2022.** Foundational benchmark for the kind of plausible-but-wrong output Cowork produces when domain knowledge is thin. Cite as evidence that "fabricated specificity" is measurable and persistent.

- **Bender, Emily M. et al. (2021). "On the Dangers of Stochastic Parrots." FAccT '21.** The "voice drift" failure mode has its theoretical home here. LLMs trained on aggregate corpora regress to corpus-average voice unless conditioned otherwise — and even with conditioning, regression happens in long generations.

- **Liu, Nelson F. et al. (2024). "Lost in the Middle: How Language Models Use Long Contexts." TACL.** Documents that LLMs attend disproportionately to context beginnings and ends. The "padded middle" of a Cowork chapter is partly explained by this: middle context is under-attended in the prompt, so middle content is under-conditioned in the output.

- **Bansal, Gagan et al. (2021). "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance." CHI 2021.** Empirical case for uncertainty annotation in human-AI teams. The [verify] flag is in this tradition. Cite as license for the flag being a feature, not an apology.

- **Sycophancy literature: Sharma, Mrinank et al. (Anthropic, 2023). "Towards Understanding Sycophancy in Language Models."** Documents that RLHF-trained models systematically tell users what they want to hear. Sycophancy is the failure mode the chapter doesn't list but should — Cowork drafts often agree too easily with the TIKTOC.md's framings. Worth a sentence.

---

## 2. The Core Concept — State of the Field

### What is settled

- LLMs hallucinate. Rate is task-dependent; presence is universal.
- Long-form generation degrades faster than short-form. Voice drift, repetition, and middle-padding all worsen at length.
- RLHF-trained models exhibit sycophancy. Documented across labs.
- Style transfer is partial. "Write in Hemingway's voice" produces a recognizable but flattened pastiche.
- Uncertainty annotation improves downstream human accuracy when humans engage with the annotations and degrades it when they don't.

### What is disputed

- **Whether "voice" is a measurable property.** Stylometry says partially yes; literary critics say no. The chapter should treat voice operationally — recognized by readers in the author's domain — not as a metric.
- **Whether Cowork-style long-context generation is the right architecture or whether multi-pass / agentic generation produces better drafts.** Active research area (2024–2026). The chapter should not relitigate this; it teaches the pipeline the book is built on.
- **Whether "Attenborough × Feynman" is a defensible house style or a metaphor.** This is contested *within the book*. The chapter must defend it operationally: cold open, mechanism, scale shift, named trade-off.

### What has changed recently (last 5 years)

- **Long-context models (100k+, then 1M+ tokens).** Made full-chapter generation viable. Cowork could not exist five years ago. Changed the failure profile from "ran out of context" to "ran out of attention."
- **Specification prompting / "system prompts as architecture."** TIKTOC.md as input to a single chapter generation is now a stable pattern. Was experimental in 2022.
- **The fluency-vs-accuracy tradeoff is now well-named.** Designers and writers have language for it. Three years ago, "the writing is good but the facts are wrong" was a surprise; now it's the default expectation.
- **AI-assisted writing studies have shifted from "does it help?" to "what does it cost?"** CoAuthor (Lee et al. 2022), and follow-ups, have shown homogenization effects: writers using LLMs converge on similar phrasings. The "voice drift" failure mode is also a *reader-side* problem now.

---

## 3. Application Domain Examples

1. **The portfolio case study Cowork would write for a designer.** Generic structure (problem, process, solution, impact) with plausible client names and fabricated metrics. The designer recognizes the failure instantly — there is no specific client memory in the text.
2. **A Cowork-drafted "About" page for a design studio.** Reads professional, says nothing distinctive. Voice drift in its purest form.
3. **A capability statement for a brand identity service.** Padded middle: three paragraphs where one paragraph is the work. The designer who has written this kind of copy by hand sees it immediately.
4. **A design critique Cowork writes.** Often technically right and useless — names principles (hierarchy, contrast) without the specific judgment that makes critique useful. Missing domain judgment.
5. **A workshop description.** Bridge questions that don't bridge: "In this workshop, we'll explore..." with no commitment to what the next session delivers. The same failure Cowork makes between chapters.

---

## 4. The Book's Thesis Connection

The thesis: TIKTOC.md is the highest-leverage step; the human rewrite is the gate.

Chapter 7 is the moment the thesis becomes empirical. The reader runs Cowork. They get back fourteen chapters. They open one. What they read is *either* a draft worth rewriting or a draft that exposes a vague TIKTOC.md.

The chapter's load-bearing argument is the five failure modes. They are not a catalog of LLM bugs. They are *diagnostics for the reader's own TIKTOC.md*. Voice drift = TIKTOC.md voice section was thin. Fabricated specificity = pantry didn't anchor the chapter. Missing domain judgment = capability statements were vague. Padded middle = chapter scope was over-broad. Bridge questions that don't bridge = inter-chapter logic was assumed, not specified.

This is also the chapter that earns Chapter 8 — the human rewrite. Without this chapter's evidence (here is what Cowork produces; here is exactly where it fails), Chapter 8 reads as preference. With this chapter's evidence, Chapter 8 reads as necessity.

Connection backward: TIKTOC.md (Ch 4) determines what Cowork can produce; pantry (Ch 6) determines what it has to work with. Connection forward: every failure mode named here becomes a rewrite target in Ch 8. The bridge into Ch 8 is the worked example — Cowork draft, then a single human-rewritten paragraph. The reader sees the gate.

---

## 5. The AI Wayback Machine — Candidate Figures

**Candidate A — Joan Didion (1934–2021).** Wikipedia page title: **"Joan Didion."** American essayist. Substantive connection: Didion's "Why I Write" (1976) is the cleanest articulation of why voice cannot be specified, only recognized. The chapter's claim that voice drift is detectable but not metricizable is Didion's claim. Diversity contribution: woman, secular Western literary tradition. Lesser-known to working designers under 40; undergrad-accessible (Didion is widely taught). Example prompt: *"Ask Claude: Read Joan Didion's 'Why I Write.' She says grammar is a piano you play by ear. What does that mean about voice in writing — and how would Didion describe what an LLM is doing when it writes?"*

**Candidate B — Richard Feynman (1918–1988).** Wikipedia page title: **"Richard Feynman."** American physicist. Substantive connection: the chapter explicitly uses "Feynman voice" as half the AI+1 house style. The reader should know who Feynman was and what his lectures actually do. Widely known but the *operational* knowledge — what makes a Feynman explanation Feynman-shaped — is less common. Male, American. Example prompt: *"Ask Claude: Read the opening of Feynman's Lectures on Physics, volume 1, chapter 1. What rhetorical move does Feynman make in the first three paragraphs? Find one paragraph in your Cowork draft that fails to make the same move."*

**Candidate C — William Zinsser (1922–2015).** Wikipedia page title: **"William Zinsser."** American journalist and writing teacher. *On Writing Well* is the canonical handbook for nonfiction prose. Substantive connection: every Cowork failure mode is named in Zinsser; the human rewrite is Zinsser applied. Male, American. Use as backup if Didion is taken elsewhere or if a more practical figure is wanted. Example prompt: *"Ask Claude: Open On Writing Well to the chapter on clutter. Find three sentences in your Cowork draft Zinsser would cut."*

**Diversity flag:** Recommend Didion as lead (woman, literary). Feynman as the half-namesake of the voice. If both are used, this chapter pulls weight on the diversity quota for the four-chapter assignment. Consider also a non-Western writer for sidebar — possible: **James Baldwin** (Wikipedia: "James Baldwin"), whose 1962 essay "The Creative Process" is the strongest short text on voice as inseparable from identity. Baldwin would also bridge into Ch 8 (authorial identity, the human rewrite).

---

## 6. Pedagogical Delivery Research

- **The chapter must give the reader something to *read*, not something to *learn*.** The chapter is about reading a draft critically. The worked example — one Cowork chapter with five failures annotated — does the teaching.
- **Annotation as pedagogy.** Margin annotations on the worked example are the chapter's primary instructional move. Designers read annotated work fluently (it's how design crits work).
- **The [verify] flag must be normalized early.** Treat it as a sign of intellectual honesty, not a failure. The first time the reader sees one, the chapter should say: "this is what you want to see."
- **Don't list the five failure modes as a bulleted list and stop.** Each gets a section with a concrete example and a one-sentence diagnostic test. Otherwise the reader memorizes the list and misses the failures in their own draft.
- **The "rate each draft" exercise (SOLID FOUNDATION vs. NEEDS PANTRY WORK) is the chapter's evaluation hinge.** Make it explicit that this rating is feedback to the *pantry*, not to the writer. This keeps the reader from blaming themselves.

---

## 7. Representation and Display Research

- **Annotated chapter draft as the central figure.** Two-page spread if possible: full Cowork-drafted chapter on the left, margin annotations on the right with arrows. This is the figure the reader will photograph and use as their reference.
- **A "five failures" mini-table.** Failure mode | one-sentence diagnostic | example phrase. One-page reference. Goes in chapter and in the back-of-book appendix.
- **Before/after of a single paragraph.** Cowork voice → rewritten voice. One example. Three sentences each. Designers respect this kind of minimum-viable comparison.
- **The log.csv as opening figure.** Show the actual log.csv from a Cowork run — fourteen rows, all green. Then the reader opens chapter 03 and reads. The visual contrast (everything looks fine, then the prose isn't) is the chapter's opening punch.

---

## 8. Open Questions and Research Gaps

- **What is the actual Chapter Writer prompt?** The book cannot accurately describe the failure modes without it. Need the current prompt text.
- **Are the five failure modes exhaustive?** Sycophancy is missing. So is "false confidence on contested claims." Either expand to seven or argue why five.
- **Does the worked example come from a real ai-for-designers run?** Open Question 1 in TIKTOC.md. Cannot be drafted otherwise.
- **What does a [verify] flag look like in the actual output — inline? Footnote? Comment?** Determines what the chapter teaches.
- **How does Cowork handle BLOCKED chapters today?** The chapter needs current behavior, not specified behavior.
- **Should the chapter teach the reader to *re-run* a chapter or only to flag for rewrite?** The current pipeline answer matters.

---

## 9. Sourcing Notes

Feynman Lectures are freely available online (Caltech, CC-licensed). Cite chapter and section. Attenborough's documentary work is cited as a body — name two or three specific titles. Pinker, Strunk & White, Zinsser are standard publisher editions. Didion's "Why I Write" is in *Let Me Tell You What I Mean* (2021); cite that collection. Baldwin's "The Creative Process" is in *Creative America* (1962) and reprinted in *The Price of the Ticket* (1985); cite the reprint.

For the LLM failure-mode literature: Ji et al. 2023 (ACM Survey), Lin et al. 2022 (ACL), Bender et al. 2021 (FAccT), Liu et al. 2024 (TACL), Bansal et al. 2021 (CHI), Sharma et al. 2023 (Anthropic technical report). All peer-reviewed or industry-standard. Anthropic's blog posts on sycophancy and steering are useful supplements but cite the underlying papers for academic weight.

Lee et al. 2022 CoAuthor study (UIST) is the relevant empirical case for AI-assisted writing degradation; cite for the homogenization claim. Avoid citing journalism *about* LLM failure modes (Wired, The Verge) as primary evidence — they're useful for the cultural moment, not the technical claim.
