# Chapter 3 — Domain Research: The Chapter Before the Chapter

*One LLM gives you an answer. Three give you a map of what is settled, what is contested, and what nobody noticed.*

**One-line capability:** Students write, run, and synthesize a structured domain research prompt across three LLMs, producing a brief ready for the Tic TOC intake session.

---

## Learning objectives

By the end of this chapter you will be able to:

- (Apply) Write and run a domain research prompt structured around the eight required sections — for a specific professional domain.
- (Analyze) Combine outputs from three LLMs into a single synthesized research document, noting where the models agree, where they diverge, and where the divergence reveals a contested claim.
- (Evaluate) Assess the research output for fluency-trap examples — AI-generated content that looks authoritative but would not survive expert review.
- (Create) Produce a domain research brief in four-section format, ready to bring into a Tic TOC /i1 session as the primary input.

---

## Opening — three answers, same question

In May 2026 the prompt at the bottom of this section was sent — verbatim — to three frontier large language models: Claude (Anthropic), GPT-4 (OpenAI), and Gemini 1.5 (Google). The question was identical. The outputs were not.

Below is the first section of each response — *AI tool adoption in graphic design* — laid side by side. The full responses run to between 1,800 and 3,200 words each. What you see here is the opening 100–150 words of each, lightly trimmed for the page.

---

**Claude (with web research enabled):**

> *Adoption of generative AI in graphic design has shifted from experimental to embedded over 2023–2026. Major design tools now ship AI features as defaults rather than add-ons: Adobe Firefly is integrated into Photoshop and Illustrator; Figma launched Figma AI at Config 2024; Canva's Magic Studio (Oct 2023) brought generative AI into the small-business design market. According to recent industry reports — Figma's State of the Designer 2026 and Adobe's MAX 2025 keynotes — a substantial majority of working designers now use generative AI in some part of their workflow. I should flag that headline adoption percentages vary considerably across reports depending on what counts as "use," and many of the most-cited figures come from vendor-published research with potential incentive bias.*

Notice the texture: explicit dating, named sources, an immediate self-disclosed caveat about vendor bias. Claude with web research enabled tends to over-qualify. Read this as the *uncertainty-explicit* signature.

---

**GPT-4:**

> *AI tool adoption in graphic design has accelerated dramatically. Studies show that over 90% of graphic designers now use AI-powered tools weekly, with adoption highest among social media designers and lowest among high-end brand identity practitioners. Key tools include Adobe Firefly, Midjourney, DALL-E, Canva AI, and Figma AI. The general pattern is that AI is most embedded in production workflows (resizing, variation, layout drafts) and least embedded in strategic and brand decisions. AI adoption correlates positively with reported productivity gains, particularly for early-career designers facing "blank canvas syndrome."*

Notice the texture: confident enumeration, round-number specificity ("over 90%"), no named sources, no flagged uncertainty. GPT tends to *summarize confidently from compressed knowledge*. The 90% figure is plausible — it appears elsewhere in the literature — but GPT is reporting it without attribution.

---

**Gemini 1.5:**

> *Graphic design has experienced one of the highest AI adoption rates in creative professions. Specific data points from Figma's State of the Designer 2026 and the Adobe Creative Trends Report 2025: 93% of graphic designers use AI-powered tools at least once a week (Figma 2026); 82% use them to overcome "blank canvas syndrome"; 41% business adoption rate for Adobe Firefly. Only 12% of designers trust AI tools to handle high-stakes branding for Fortune 500 companies. The data shows a sharp divide between high-frequency use for low-stakes work and high-trust use for high-stakes brand work. The adoption story is not whether AI is used — it is — but for what.*

Notice the texture: specific percentages, named-source attribution, structural framing ("the adoption story is not whether but for what"). Gemini tends toward *retrieval-grounded enumeration with structural interpretation*.

---

Three responses. Same question. Three signatures.

Where do they **agree**? All three identify AI adoption as widespread and structurally embedded. All three name the same vendors. All three identify the same pattern — heavy adoption in production work, light adoption in strategic and brand work. This is *settled territory* for the field.

Where do they **diverge**? On specificity. Claude qualifies. GPT enumerates without sources. Gemini cites specific numbers. The numbers themselves *also* diverge — "over 90% weekly use" (GPT) vs. "93% at least once a week" (Gemini). These are close, but they are not the same claim. Which is right depends on the source.

Where does **one model add what the others missed**? Gemini names two specific reports (Figma 2026, Adobe Creative Trends 2025) and the 12% high-stakes-trust figure. Claude names the same Figma report but does not produce the 12% number. GPT names nothing specific. This is *divergent-as-gap* — Gemini retrieved a number the other two missed.

That single side-by-side comparison is the entire argument for the three-LLM domain research prompt. One model would have given you one answer. Three give you the *map of confidence* — what is settled, what is contested, what is conjecture, and what one model retrieved that the others missed.

This chapter walks you through producing that map for your own field.

The prompt that produced these three responses:

> *I am a [graphic designer] researching how AI is currently affecting
> my profession. Please produce a structured report with the following
> eight sections: (1) AI tool adoption by role and workflow stage,
> (2) Documented failure modes when AI is used in this work,
> (3) Copyright, IP, and legal-exposure landscape, (4) The fluency
> trap pattern in this domain, (5) Labor-market data, (6) The
> irreducibly human taxonomy, (7) Existing training and certification,
> (8) Context-specific risks for solo or one-primary-client practitioners.
> For each section: cite sources where you can; mark contested claims;
> distinguish current-state from settled territory.*

You ran this in Chapter 1's Exercise 1. If you did not, do it now. The rest of this chapter is unreadable without three responses in hand.

---

## 1. Why three LLMs — not one, not five

The case for three is empirical, methodological, and practical.

The **empirical case** is the side-by-side comparison above. Each frontier LLM has a distinctive output signature shaped by its training data, its reinforcement signal, and its safety conditioning. Claude is trained under Constitutional AI methodology with an emphasis on cautious, nuanced reasoning and explicit uncertainty markers.[^anthropic] GPT-4 is optimized for instruction-following and structured enumeration, with less native tendency to surface its own uncertainty.[^openai] Gemini 1.5 is multimodal-first and tightly integrated with Google Search, producing more retrieval-grounded outputs with specific source attribution.[^gemini]

These signatures are **temporally unstable** [contested — practitioner observation; model behavior shifts across versions and within versions over months]. Claude 3 in early 2024 had a different output profile than Claude in May 2026. The signature claims in section 4 below are accurate for the May 2026 vintage of all three models. They will not be accurate two years from now. The *practice* of comparing across three models survives even if any individual model's signature shifts.

The **methodological case** is investigator triangulation. Norman Denzin's 1978 *The Research Act* names four types of triangulation: data, investigator, theoretical, and methodological.[^denzin] The three-LLM rotation is *investigator triangulation* applied to AI tools — treating each LLM as an investigator with different training data and different known failure modes. Where investigators converge independently, the claim is more credible. Where they diverge, the contested territory is visible. This is the academic frame that elevates the practice from "ask three chatbots" to legitimate methodology.

James Surowiecki's *Wisdom of Crowds* (2004) provides the related but distinct argument: aggregation of independent estimates outperforms individual estimates under four conditions — diversity of opinion, independence, decentralization, and aggregation.[^surowiecki] Three frontier LLMs satisfy these conditions *weakly*. They share enormous overlap in training data (Common Crawl, books, code), so they are not fully independent. They share many of the same safety conditioning regimes. The wisdom-of-crowds claim must be qualified: this is *approximate triangulation*, not the statistical kind.

The **practical case** is the diminishing-returns curve. Adding a fourth model (Llama, DeepSeek, an open-source frontier model) doubles your runtime cost and rarely doubles the signal — most of what the fourth model adds is restating what one of the first three already said. Two models is *almost* enough but misses the third-perspective check that catches the divergent-as-gap pattern Gemini surfaced in the opening above. Three is the local optimum for the solo author-instructor working under time pressure.

This is **not a peer-reviewed methodology** [verify — no controlled study confirms three-LLM rotation produces better domain research than single-LLM use with verification]. Treat it as a defensible practitioner convention with strong analogical support from qualitative research methods.

[^anthropic]: Anthropic. (2024–2025). *Claude prompting guide* and *Anthropic Research blog posts on Constitutional AI*. Anthropic. Cite specific post URLs at retrieval date.
[^openai]: OpenAI. (2023–2025). *Model cards and system cards for GPT-4, GPT-4o, GPT-5*. OpenAI.
[^gemini]: Google DeepMind. (2024–2025). *Gemini technical reports and model cards*. Google DeepMind.
[^denzin]: Denzin, N. K. (1978). *The Research Act: A Theoretical Introduction to Sociological Methods* (2nd ed.). McGraw-Hill.
[^surowiecki]: Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday.

---

## 2. The domain research prompt — structure and adaptation

The prompt that runs across all three models has eight sections. The structure is not arbitrary. Each section asks for a specific kind of evidence; together they produce the input a Tic TOC /i1 session needs.

Here is the prompt with annotation for what each section is *for*:

> *I am a [your profession] researching how AI is currently affecting
> my profession. Please produce a structured report with the following
> eight sections:*

The opening line locks the perspective. You are not asking "what is AI doing." You are asking "what is AI doing *to a person in this profession*." The framing constrains the response toward applied detail.

> *1. AI tool adoption by role and workflow stage.*

Inventories what tools are actually being used, by whom, at what step. This becomes Section 1 of your synthesized brief and feeds Tic TOC's /i3 (audience intake) — *what does your reader already use?*

> *2. Documented failure modes when AI is used in this work.*

The fluency trap inventory. Becomes the spine of your Chapter 1 — whatever your book is called — and feeds Tic TOC's /i4 (thesis) by giving you the central professional risk your book argues against.

> *3. Copyright, IP, and legal-exposure landscape.*

The risk landscape. Different fields will have wildly different responses here — designers get *nemo dat* and Thaler v. Perlmutter; medical writers get FDA disclosure; lawyers get model rules of professional conduct. Becomes a dedicated chapter in most domain handbooks.

> *4. The fluency trap pattern in this domain — output that looks
> professional but fails expert review.*

The specific local instances. This is the section where the LLMs are asked to do the hardest work — naming *patterns* of expert-detectable failure rather than reciting generic failure modes. The three-way comparison here is most useful.

> *5. Labor-market data: postings, rates, displacement, wage premium.*

The arithmetic of why this matters now. Feeds Tic TOC's /i4 (positioning) and is the evidence base for any "AI is creating both threat and opportunity" claim your book makes.

> *6. The irreducibly human taxonomy — what AI cannot do here.*

Your book's *protect column*. Feeds Tic TOC's /l1 (outcomes) by naming what capabilities your book preserves rather than replaces.

> *7. Existing training and certification for AI literacy in this field.*

The market gap. Feeds Tic TOC's /m1 (market positioning) — what books, courses, certifications already exist, and which gap yours fills.

> *8. The context-specific risks for solo or one-primary-client
> practitioners.*

The deployment specificity. Your book is for one kind of reader; this section produces the reader-specific risk inventory.

> *For each section: cite sources where you can; mark contested
> claims; distinguish current-state from settled territory. Length:
> roughly 1,500–2,500 words.*

The instruction matters. Without it, the models will produce summary text without source attribution. With it, you get something closer to a research memo than to a blog post.

**Adaptation guidance.** The eight sections are field-agnostic by design. The *one* substitution you make is the profession in brackets. Do not rewrite the eight sections; the structure has to be identical across the three models for the side-by-side comparison to be tractable. If you customize the sections per-model, you lose triangulation — you cannot tell whether a divergence reflects the model or the prompt.

The eight-section schema is editorial (this is Bear Brown / Cowork convention; there is no canonical academic source for the exact partition). What survives the editorial choice is the *coverage*: any domain research brief that produces these eight outputs is ready for /i1.

---

## 3. How to combine outputs — agreement, divergence, gaps

You now have three documents. Each is between 1,500 and 3,200 words. The synthesis move is the load-bearing skill of this chapter.

Read all three outputs in one sitting. Do not paraphrase, do not summarize, do not start writing yet. Read for the *pattern of overlap*. You are looking for three categories of claim, and you will mark each one as you go:

| Marker | Meaning | What to do |
|---|---|---|
| **ALL THREE AGREE** | Claim appears in all three responses with consistent framing. | Treat as settled territory for your field. Quote one model's clearest formulation. |
| **TWO AGREE** | Two of three responses produce the claim; one omits or contradicts. | Flag as probably-settled. Note the dissenter explicitly. |
| **DIVERGENT** | Models disagree on substance, magnitude, or interpretation. | Flag as contested. State both positions. |
| **ONE ONLY** | One model raises a claim the others did not. | Flag as candidate. Investigate whether the omission is a gap or a correction. |

This labeling is the discipline that carries forward into Chapter 6 (pantry evaluation), Chapter 8 (rewrite gate-checking), and Chapter 10 (enrichment exercises). Once you can do this on a research brief, you have internalized the analytic move the whole book runs on.

Here is the pattern, drawn from the running example, showing what each marker looks like in practice:

**ALL THREE AGREE — the fluency trap definition.** All three models, asked to describe the fluency trap pattern in graphic design, produce variants of "AI generates output that looks professional but lacks the craft judgment, brand knowledge, or strategic rationale to survive expert review." The wording differs; the substance is identical. Quote the clearest formulation (Gemini's, with the Oppenheimer cognitive-fluency framing) and move on.

**TWO AGREE — the AI wage premium magnitude.** Claude and Gemini both cite the PwC 2025 AI Jobs Barometer 56% premium figure with the U.S./advanced-skills qualifier. GPT-4 cites "approximately 25% wage premium" without source or qualifier. Two-of-three agreement, but the dissenter is reporting a *different cut of the same data set* — likely the global average rather than the US-advanced cut. The 56% number is probably right; the 25% number is probably the global figure. Flag both, attribute both, and let the reader see the variance.

**DIVERGENT — whether AI is displacing junior designers.** Claude says "junior production tasks are being automated, with mixed evidence on entry-level hiring." GPT says "AI is creating new junior roles in AI-assisted production." Gemini says "the junior pipeline gap is an underreported design crisis — agencies are hiring fewer juniors because AI handles their tasks." Three positions ranging from cautious through optimistic through alarmed. Flag as contested. State all three. Do not synthesize prematurely — the divergence is the finding.

**ONE ONLY — *nemo dat quod non habet*.** Gemini surfaces the IP doctrine name *nemo dat quod non habet* — "you cannot give what you do not have" — as the foundational legal principle for designers assigning AI-generated work to clients. Claude and GPT both discuss copyright issues for AI-generated work but neither names the doctrine. This is divergent-as-gap. Verify the claim (it checks out under the U.S. Copyright Office's January 2025 guidance and Thaler v. Perlmutter [verify — D.C. Circuit ruling 2025]) and include in the synthesis with attribution to Gemini.

The synthesis is **not averaging**. Averaging would lose the expert-judgment move that is the entire point. You are reading three differently-biased reports and applying domain expertise to triage. Where you, the expert, know the field, you choose. Where you do not, you flag.

**The output is a single document, 600–800 words minimum, organized by the eight original sections.** Every claim is marked with one of the four markers. Contested claims are stated as contested. One-only claims are attributed. This is the synthesis exercise (Exercise 2 below) and it is the most cognitively demanding hour in this chapter.

---

## 4. The fluency trap check on LLM research

The fluency trap returns here, at the research stage, at lower stakes than at the deliverable stage. This is rehearsal for Chapter 4.

The risk: an LLM produces a paragraph that *sounds* authoritative — confident verbs, named studies, specific percentages — but is wrong. Not hallucinated wholesale; wrong in the way of slightly-off citations, conflated findings, or invented specificity. The flag for this is *plausibility without verifiability*.

Three patterns to watch for:

**Pattern 1 — the invented citation.** A model says "according to a 2024 Stanford study…" with no further citation, and the study does not exist. This is rarer in 2026 than it was in 2023 but still occurs, especially in lower-traffic subfields. *Catch:* when a claim is anchored to a specific named study without enough metadata to verify, search for the study before quoting it. If it does not exist, the underlying claim may still be true — but you cannot quote the study, and you should not let the model's confidence carry into your brief.

**Pattern 2 — the conflated finding.** A model reports "PwC found a 56% wage premium for AI skills" without naming the geography or skill-level cut. The 56% figure is real; it is the U.S./advanced-AI-skills cut. Quoting it without the qualifier turns a defensible regional finding into an indefensible global claim. *Catch:* when a number is given without sufficient qualification, find the original source and add the qualifier — or drop the number.

**Pattern 3 — the precision illusion.** A model reports "93% of graphic designers use AI weekly" — a precise-feeling number that comes from a specific report (Figma's State of the Designer 2026 in this case). Other reports from the same year give different numbers ("over 90%" in GPT's response; "a substantial majority" in Claude's). *Catch:* precise numbers are usually defensible but should not be treated as canonical without verifying the methodology of the source survey.

The **fluency trap check** is a five-minute pass on your synthesis document before you call it done. For each numeric claim and each named study, ask: *can I verify this in five minutes?* If yes, do. If no, downgrade the claim — replace "X%" with "a majority" or with "[verify]".

This is *exactly* the move you will make in Chapter 6 when evaluating pantry research output, in Chapter 8 when rewriting Cowork drafts, and in Chapter 11 with the Fact-Checking Assistant. The fluency trap check is the recurring move. This is the first time you do it. Get the habit here.

---

## 5. What makes a brief ready for /i1 — four things Tic TOC will ask

The deliverable of this chapter is a brief in **four-section format**. The eight-section LLM output is the raw material; the four-section brief is the input format Tic TOC expects.

The four sections collapse the eight LLM sections into the structure that maps onto Tic TOC's intake questions. Here is the format:

### Section A — The state of the field

Roughly 200–400 words. What is settled, what is contested, what is current-state. Draws from LLM sections 1, 5, and 7 of your research output. Tic TOC's /i2 (booktype) and /i4 (positioning) questions read against this section.

### Section B — The fluency trap and irreducibly human taxonomy

Roughly 200–400 words. The five failure modes specific to your field and the corresponding human-retained competencies. Draws from LLM sections 2, 4, and 6. Tic TOC's /i4 (thesis) and /l1 (outcomes) read against this section.

### Section C — The reader's specific risk context

Roughly 150–300 words. The risks and opportunities for the specific kind of practitioner your book is for (solo, one-client, mid-career, freelance, etc.). Draws from LLM section 8. Tic TOC's /i3 (audience intake) reads against this section.

### Section D — The market gap and book positioning

Roughly 150–300 words. What training exists, what does not, and what the book's specific contribution is. Draws from LLM section 7. Tic TOC's /m1 (market positioning) and /m3 (out of scope) read against this section.

**Total brief length: roughly 700–1,400 words.** No longer. The brief is a working document, not a publication. Tic TOC will read it once at the start of the session and reference it during /i3 and /i4. If it is longer than 1,400 words the session loses focus on the actionable items.

**Four things Tic TOC will ask that the brief must already answer:**

1. *Who is your specific reader?* — Section C must name them.
2. *What is the central professional risk your book argues against?* — Section B must articulate it.
3. *What is the current state of AI in this field that makes your book necessary now?* — Section A must establish it.
4. *What existing books or courses does your book sit beside, and what gap does it fill?* — Section D must position it.

If the brief cannot answer all four when held up against the page, /i1 will stall and Tic TOC will spend the first thirty minutes of your session asking you to draft answers in real time. That is a poor use of the timebox. Spend forty minutes on the brief; save an hour of stalling in the session.

---

## Worked example — the synthesized domain research brief for ai-for-designers

The full synthesized brief for the running example lives at `pantry/ai-for-designers-final-brief.md` and runs to roughly 9,000 words (longer than the 700–1,400 recommended above; the full brief is more thorough than a /i1 minimum because it doubles as the source document for *every chapter* of the ai-for-designers book, not just /i1).

What follows is the four-section /i1-ready summary distilled from the full brief, with provenance annotations showing which LLM contributed each claim.

> ### Section A — The state of the field
>
> Generative AI is structurally embedded in graphic design as of 2026.
> 93% of graphic designers report using AI tools at least once a
> week — Figma State of the Designer 2026 [ALL THREE AGREE, specific
> number from Gemini]. 72% report generative AI in their workflows;
> 91% report quality improvements, not just speed gains [ALL THREE
> AGREE]. Adoption is uneven across roles: heaviest in social-media
> production work and lightest in high-end brand identity work, where
> only 12% trust AI tools for Fortune 500 branding [ONE ONLY — Gemini,
> Figma 2026 source]. Tools include Adobe Firefly (41% business
> adoption), Midjourney, DALL-E, Canva Magic Studio, Figma AI [ALL
> THREE AGREE on tool list]. AI sits inside Photoshop, Illustrator,
> Figma, and Canva as a default feature, not an external service
> [ALL THREE AGREE]. PwC 2025 reports a 56% wage premium for workers
> with advanced AI skills (U.S. cut) [TWO AGREE — Claude and Gemini].
> The labor-market signal is mixed: WEF 2025 ranks graphic design as
> the 11th fastest-declining job category, citing AI as primary cause
> [DIVERGENT — Claude flags the source; GPT does not raise it];
> simultaneously 59% of freelance designers report raising rates via
> AI-enhanced prototyping [ONE ONLY — Gemini]. Both signals are real
> and present.

> ### Section B — The fluency trap and irreducibly human taxonomy
>
> Five fluency-trap patterns recur across all three LLM outputs:
> brand-correct surface with brand-wrong meaning [ALL THREE AGREE,
> primary pattern]; accountability collapse — designer can produce
> the asset but not defend the decision [ALL THREE AGREE, GPT
> framing]; client-relationship misread — AI blind to unspoken brief
> context [ALL THREE AGREE]; revision-cycle breakdown from
> non-localized generative control [ONE ONLY — Gemini, most
> technically specific]; variation overload without selection
> principle [TWO AGREE — Claude and GPT]. The irreducibly human
> taxonomy: client intuition; subtractive judgment (taste); creative
> accountability; brief interpretation; constraint navigation;
> presentation under questioning; cultural reading; brand stewardship;
> ethical judgment [ALL THREE AGREE on category list, varying
> formulations]. Empirical anchor: arXiv 2024 expert evaluation
> found GenAI-supported designs rated more creative and unconventional
> but not significantly better in visual appeal, brand alignment, or
> usefulness [TWO AGREE — Claude and GPT cite the same study; Gemini
> does not raise it].

> ### Section C — The reader's specific risk context
>
> The target reader is a freelance graphic or brand designer with
> five to fifteen years of practice, one primary anchor client, and
> at least one consumer-grade AI tool in active use. Specific risks
> include: confidentiality and NDA exposure from feeding proprietary
> client data into consumer-grade AI tools [ONE ONLY — Gemini, most
> complete]; legal exposure void — no in-house legal department to
> backstop a copyright or trademark claim arising from AI-assisted
> work [TWO AGREE — Claude and Gemini]; rate compression from clients
> who assume AI makes everything faster and cheaper [ALL THREE AGREE];
> scope creep from clients asking for "a few more variations" [ONE
> ONLY — GPT framing]. Specific opportunities: retainer expansion
> via embedded creative partner positioning [ONE ONLY — GPT framing];
> rate-raise via AI-enhanced rapid prototyping (59% of freelancers
> reporting this) [ONE ONLY — Gemini]. The reader holds tacit
> knowledge — client history, internal politics, brand memory — that
> is the long-term relationship's primary value and cannot be
> replicated by AI [ALL THREE AGREE].

> ### Section D — The market gap and book positioning
>
> No current training program teaches the full AI+1 framework for
> graphic designers specifically. Adobe, Figma, and Canva publish
> product-focused tutorials driving user adoption [ALL THREE AGREE].
> AIGA's "Business for Designers" and "Law for Designers" certificates
> cover legal and business fundamentals but are slow to adapt to
> generative AI law changes [ONE ONLY — Gemini, specific institutional
> claim]. RISD and SVA have responded institutionally with strategic
> design pedagogy and formal AI use guidelines, but these programs
> are designed for full-time degree students, not mid-career
> freelancers [ONE ONLY — Gemini, specific institutional detail].
> Independent design educators (The Futur, Flux Academy) teach
> business scaling and visual fundamentals but lack comprehensive
> AI+legal+strategy curriculum [TWO AGREE — Claude and Gemini]. The
> book's market position: a practitioner handbook for the freelance
> designer with deep domain expertise and one anchor client, teaching
> AI fluency as a layer on top of preserved professional identity —
> with the IP, disclosure, brand stewardship, and accountability
> moves that the existing training market does not cover [SYNTHESIS,
> derived from gap analysis ALL THREE AGREE].

This is the brief Tic TOC's /i1 session worked from. Notice three things about the format:

1. **Every claim has provenance.** Either marked ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY, or attributed to a specific model. A reader picking up the brief can immediately see how confident to be in each line.
2. **Contested claims are stated as contested.** The labor-market section names *both* the WEF decline signal *and* the freelancer rate-rise signal without resolving them. The synthesis is honest about what is settled and what is not.
3. **The length is bounded.** Four sections, roughly 900 words total. This is the document the Tic TOC session reads. It is not the full 9,000-word source brief; it is the input.

The full source brief at `pantry/ai-for-designers-final-brief.md` exists because the running example will be drawn from it across all eleven chapters of *this* book. Your own brief does not need to be 9,000 words. It needs to be **enough** for /i1.

---

## Exercises

### Exercise 1 (Apply) — Adapt the template to your field; run on three LLMs

Take the eight-section prompt template from section 2. Substitute your specific profession for `[graphic designer]`. Do not modify any other word in the prompt. Run the prompt verbatim in:

- **Claude** (with web research enabled if available)
- **GPT-4 or later** (claude.ai counterpart; use a fresh chat, not a project)
- **Gemini** (use the equivalent web-research-enabled mode if available)

Save each response as a separate markdown file: `claude-output.md`, `gpt-output.md`, `gemini-output.md`. Do not synthesize yet.

**Time required:** 30–60 minutes including waiting for outputs.

**Deliverable:** Three markdown files, each between 1,500 and 3,500 words, on disk.

### Exercise 2 (Analyze) — Produce a 600–800 word synthesis with provenance flags

Read all three outputs from Exercise 1 in one sitting. Produce a synthesis document organized by the eight original sections. For *every* claim in your synthesis, mark with one of: ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY. For ONE ONLY claims, attribute the source LLM. For DIVERGENT claims, state all positions without resolving prematurely.

Length: 600–800 words. Tight. The discipline of compression is part of the exercise.

Run a five-minute **fluency trap check** at the end: every numeric claim, every named study, every specific institutional reference — can you verify it in five minutes? Downgrade what you cannot verify.

**Deliverable:** One markdown file, 600–800 words, every claim flagged.

### Exercise 3 (Create) — Produce a four-section brief ready for /i1

Distill the synthesis from Exercise 2 into a four-section brief following the format in section 5: state of the field; fluency trap and irreducibly human taxonomy; reader's specific risk context; market gap and book positioning. Total length: 700–1,400 words.

This is the document you will paste into the Project Knowledge of your Claude Project before running Tic TOC. It is the spec-for-the-spec — the document that lets the /i1 session start productive instead of stalling on basic context.

**Deliverable:** One markdown file, 700–1,400 words, four sections. This is your **Create-level deliverable** for this chapter.

---

## Still puzzling

- *Three LLMs versus more.* No empirical evidence establishes that three is the right number. Two may be sufficient for some questions; four may add value in specific domains (legal research, for example, where open-source models like Llama trained on different legal corpora bring different signal). The chapter's recommendation is heuristic.
- *Are LLM signatures stable enough to teach as a recurring pattern?* Probably not, beyond an 18-month horizon. By 2028 the signatures of Claude, GPT, and Gemini may have converged enough that the divergence patterns this chapter describes become weaker. The triangulation *logic* survives convergence; the pedagogical anchor in distinct signatures may not.
- *How much of the "wisdom of crowds" claim survives the training-data overlap?* Surowiecki's independence condition is held weakly by frontier LLMs that share enormous training corpora. The chapter argues triangulation still produces value because *output styles* differ even when *training inputs* overlap. This is plausible but unproven.
- *Can the eight-section schema be improved?* The schema is editorial. Other partitions are defensible. A medical practitioner might split section 3 (IP) into separate disclosure-and-malpractice sections. Adapt as needed without abandoning the eight-output structure.

---

## What would change my mind

I would revise this chapter's central claim — that three-LLM rotation produces better domain research than single-LLM use with verification — if a controlled comparison emerged showing that authors who used a single frontier LLM with rigorous five-minute fluency-trap verification produced briefs of equivalent quality to authors using three-LLM rotation, with significantly lower total time investment. The closest current evidence is anecdotal. The chapter's confidence rests on the side-by-side comparison move being more legible across three sources than across one, and on the divergent-as-gap pattern being the highest-value finding (Gemini's *nemo dat* surfacing in the running example is the canonical instance). If single-LLM rigorous verification produced comparable divergent-as-gap findings — by, say, prompting one model to argue against its own first response — then the three-LLM heuristic loses its time-cost justification, and the recommended practice updates.

---

## AI Wayback Machine — Paula Scher

> **Prompt to run in Claude or ChatGPT:**
>
> "Read the Wikipedia article on Paula Scher. Identify one project
> where her research into a domain — a city, a publisher, a museum —
> shaped the visual identity in a way no quick brief could have
> produced. Explain how this maps onto the chapter's argument that
> domain research must precede design."

Scher is a Pentagram partner whose fifty-year career is an extended argument for graphic design as cultural research before it is visual production. Her work on the NYC Public Theater identity, the Citi logo, and Microsoft's corporate identity all begin with extended immersion in the client's domain. The Wikipedia article is robust; the prompt asks you to read it once and write the comparison memo. [^scher]

[^scher]: Pentagram. (n.d.). "Paula Scher — Partner Biography." Pentagram. Cross-reference with Scher, P. (2002). *Make It Bigger*. Princeton Architectural Press, for first-person account of the research-first practice.

---

## Bridge — Chapter 4

The brief exists. Four sections, 700–1,400 words, every claim flagged. It sits in a markdown file on your disk. You can read it without flinching.

You are now ready for the hardest chapter in the book.

Chapter 4 walks you through the full Tic TOC session — /i1 through /g2 — with the brief you just produced as the primary input. The session takes two hours. The chapter is long because the moves are not transferable from reading; they have to be done.

Chapter 4 is also the chapter where the central thesis of this book becomes visible as a single image: two TIKTOC.md chapter specs, side by side, one from a rushed session and one from a session where the pushback was honored. The Cowork outputs below them differ in ways that matter.

The difference is the argument.
