# Chapter 1 — What AI+1 Is and Why It Works

*The fluency trap is not bad AI. It is good-looking AI that quietly replaces the decisions you are paid to make.*

**One-line capability:** Students learn to identify what AI is doing to their profession, name the irreducibly human layer, and explain why AI+1 preserves professional identity rather than replacing it.

---

## Learning objectives

By the end of this chapter you will be able to:

- (Understand) Explain the difference between an AI+1 practitioner — someone who keeps their domain identity and adds AI fluency — and a generic AI user who loses it.
- (Analyze) Run the three-LLM domain research prompt for your own field and identify the Tier 1 tasks AI handles well versus the irreducibly human tasks AI cannot perform.
- (Evaluate) Identify the fluency trap in your own domain — output that looks like professional-grade work but lacks the judgment that makes it defensible.
- (Evaluate) Assess how AI is affecting the labor market and professional identity in your field, using the research output as evidence rather than dread.

---

## Opening case — the brief that looked right

A boutique brand designer with eight years of work for one anchor client — a healthcare consultancy — receives a request from the consultancy's new VP of marketing. They want a brief for a new advisory product. The VP is in a hurry. The designer is in a hurry. The designer types a prompt into Claude:

> "Draft a creative brief for a new healthcare advisory product. Modern, calm, credible, not hospital. Aimed at C-suite buyers. About 500 words."

Forty seconds later, the brief is on screen. Two pages. Polished headings. *Project Overview. Target Audience. Brand Personality. Deliverables. Timeline. Success Metrics.* The tone is professional. The language is industry-appropriate. The deliverables list reads like every agency brief the designer has ever seen.

The designer skims it, nods, copies it into an email, and sends it to the VP.

Read the brief. Before reading on, find what the model missed.

---

> **PROJECT BRIEF — Advisory Product Identity**
>
> **Project Overview**
> Our client, a healthcare consultancy, is launching a new advisory
> product targeted at senior healthcare executives. The product offers
> strategic guidance during periods of organizational transition. The
> brief is to develop a distinctive brand identity that positions this
> product as a premium, trusted resource in a crowded advisory market.
>
> **Target Audience**
> C-suite healthcare executives (CEOs, COOs, CSOs) at hospital systems,
> payer organizations, and healthcare technology firms. Decision-makers
> who value credibility, calm authority, and discretion.
>
> **Brand Personality**
> Modern, calm, credible. Not hospital. Premium without being cold.
> Confident without being aggressive. A trusted advisor, not a vendor.
>
> **Deliverables**
> - Primary logo and supporting wordmark
> - Color palette and typographic system
> - Brand guidelines (12–16 pages)
> - Business card and letterhead templates
> - Pitch deck template (10 slides)
>
> **Timeline**
> 6 weeks from kickoff to final delivery.
>
> **Success Metrics**
> Brand recognition with target audience. Differentiation from
> competitors. Internal alignment among consultancy leadership on
> brand voice.

---

Did you catch it?

Re-read the brief with the eye of someone who has run a healthcare client account for eight years. The brand personality bullet — *modern, calm, credible, not hospital* — is the only line in the document that did not come out of a template. Everything else is generic agency boilerplate.

There is no mention that the founder of the consultancy dislikes any visual language that recalls wellness branding — a grudge that started when a competitor copied his "calm gradient" identity in 2023 and now manifests as *any* gradient in any deliverable being rejected on sight. There is no acknowledgment that the consultancy's existing brand uses a specific PMS green that the new product must either honor or explicitly break from. There is no note about the VP being new to the account, which means the entire history of what the founder will and will not accept is sitting in the freelancer's head, not in the brief. There is no budget number — the model invented "premium" without knowing whether premium here means $20K or $200K. There is no mention that the consultancy's competitors include three former employees who now run rival shops and whose visual languages must be *recognizably* not copied. There is no flag that "C-suite" in this client's world means a very specific six-person buying committee whose names the designer knows by heart.

The brief is fluent. It is not informed.

This is the fluency trap.

If you sent that brief to the founder, you would lose the account inside one quarter. Not because the brief is *wrong* — it is correct at every line — but because it is correct in the way a brochure is correct. It is generic. It tells the founder that the designer outsourced the thinking the founder pays the designer to do.

The dangerous AI output, in this profession and most others, is not the obviously bad output. Ugly logos and broken typography are easy to reject. The dangerous output is the output that looks finished. It is good enough to stop your judgment before your judgment has begun.

That is the trap this book exists to teach you to see. Once. Then again. Then again at the pedagogy scale in Chapter 10. Once you can name it in your own domain, the rest of this book becomes a set of structural responses to it.

---

## 1. The fluency trap

The phrase comes from a specific lineage. In 2021, four researchers — Emily Bender, Timnit Gebru, Angelina McMillan-Major, and a fourth author writing as "Shmargaret Shmitchell" (Margaret Mitchell, then at Google) — published a paper at the FAccT conference called *On the Dangers of Stochastic Parrots*. Their core claim was technical and precise: large language models produce text that is statistically coherent without being grounded in communicative intent. They produce *form*, not *meaning*. The text reads like a person wrote it because the model has learned what such text usually looks like, not because the model has anything to say.[^bender]

That is the academic version. The freelance version is what just happened to you reading that brief.

Cognitive scientists have a second piece of vocabulary that completes the picture. *Processing fluency* is the ease with which the mind handles a stimulus. Easy-to-process stimuli feel more truthful, more trustworthy, more competent. Reber, Schwarz, and Winkielman documented this in 2004; Alter and Oppenheimer extended it in 2009.[^reber][^alter] Fluent things feel more right. Polished things feel finished. Your client, who is not a designer, will read a sleek AI-generated identity system the same way you read that brief: *this looks done*. By the time the client discovers it isn't, the designer has either rebuilt the work three times for free or lost the relationship.

For the working designer, the fluency trap has a precise signature. Adoption data from the running-domain research [contested — see pantry flag] suggests that the failure mode appears in five recurring patterns:

1. **Brand-correct surface, brand-wrong meaning.** The colors are right. The mood is right. The positioning is wrong — because the model cannot know what your client *avoids*. It only knows what your client looks like from the outside.
2. **Accountability collapse.** The designer can show the asset. The designer cannot defend the decision. The model produced the look; nobody produced the rationale. Under client questioning the work folds.
3. **Client-relationship misread.** The model is blind to the unspoken brief — the history, the politics, the rejected directions, the founder's grudge. It translates the literal words and misses the actual problem.
4. **Revision-cycle breakdown.** A client likes the AI-generated image but wants one element changed. Regenerating shifts everything. Inpainting blurs. What was supposed to be fast becomes slow, expensive, and increasingly off-brand.
5. **Variation overload without selection principle.** The designer produces fifty directions. The client cannot choose. The designer cannot defend any one of them. Volume becomes noise.

You will recognize at least three of these from your own work, or from the work of someone you know. That recognition is the point of this section.

**Practical rule:** If the AI output looks finished and you cannot explain *why each decision is right for this specific client*, the work is not finished. It is decorated.

[^bender]: Bender, E. M., Gebru, T., McMillan-Major, A., & Mitchell, M. (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (FAccT '21), 610–623.
[^reber]: Reber, R., Schwarz, N., & Winkielman, P. (2004). "Processing Fluency and Aesthetic Pleasure." *Personality and Social Psychology Review*, 8(4), 364–382.
[^alter]: Alter, A. L., & Oppenheimer, D. M. (2009). "Uniting the Tribes of Fluency to Form a Metacognitive Nation." *Personality and Social Psychology Review*, 13(3), 219–235.

---

## 2. The AI+1 frame

The structural response to the fluency trap is not to refuse AI. Refusal does not protect you. The 33% drop in graphic design job postings reported in 2025 [verify — pull current cite from PwC AI Jobs Barometer 2025 or Lightcast] is happening whether you use the tools or not. The question is no longer *whether* AI enters your workflow but *where you keep the decisions*.

The AI+1 frame is the answer. Read the name literally.

> **AI+1 = domain expertise (the 1) + AI fluency (the AI).**

You are the 1. The "+1" is not the tool. It is *you*, kept as the load-bearing professional. The "AI" is layered on top — for speed, for variation, for production friction reduction, for the things that AI is actually good at.

This is not original framing. The intellectual ancestor is Daugherty and Wilson's *Human + Machine* (2018), which named "the missing middle" — work that neither pure humans nor pure machines do well, but hybrid teams do.[^daugherty] Frey and Osborne's 2017 paper on the automation of jobs identified three durable bottlenecks for machine work: perception/manipulation, creative intelligence, and social intelligence.[^frey] The AI+1 frame is what happens when you take Frey and Osborne's bottlenecks seriously and structure your practice around them rather than against them.

The empirical case that AI+1 is *economically real* — not just a comfortable story — sits in the labor market data.

PwC's 2025 *AI Jobs Barometer* reports that revenue per employee in AI-exposed industries grew nearly four times faster than in less-exposed sectors, and that workers with advanced AI skills command a wage premium of roughly 56% in PwC's US data.[^pwc] Lightcast's 2025 job-posting analysis found that postings mentioning AI skills offered approximately 28% higher salaries — roughly $18,000 more per year — than comparable postings without.[^lightcast] In the running-domain research, 59% of freelance designers reported successfully raising rates by offering "AI-enhanced" rapid prototyping [verify — Figma State of the Designer 2026 or comparable source].

These numbers come with caveats. The PwC figure is contested — critics argue the premium reflects survivor selection bias rather than causal benefit (workers who keep their jobs in AI-exposed industries are systematically the most skilled to begin with).[^pwc-critique] The 28% Lightcast figure varies by sector and is geographically uneven [contested — see pantry flag]. The 56% number is the US/advanced-skills cut and is not a global average.

What survives the caveats is the directional finding. *The AI-fluent practitioner in a domain that retains an irreducibly human core is currently a more valuable practitioner than either the pure-domain expert who refuses AI or the pure-AI user who does not have a domain.* That is the AI+1 frame as labor-market arithmetic.

The wage premium is the evidence, not the promise. Read it as a data point, not as a sales pitch. The frame can be true without making you rich.

[^daugherty]: Daugherty, P. R., & Wilson, H. J. (2018). *Human + Machine: Reimagining Work in the Age of AI*. Harvard Business Review Press.
[^frey]: Frey, C. B., & Osborne, M. A. (2017). "The Future of Employment: How Susceptible Are Jobs to Computerisation?" *Technological Forecasting and Social Change*, 114, 254–280.
[^pwc]: PwC. (2025). *AI Jobs Barometer 2025*. PwC Global Report. Use the US/advanced-AI-skills cut for the 56% figure; geography and skill-level cuts differ across the report.
[^lightcast]: Lightcast. (2025). AI Skills in the Labor Market. Cited in PwC AI Jobs Barometer 2025 and labor-market trade press.
[^pwc-critique]: Selection-bias critique drawn from labor-economics commentary on the Barometer methodology, 2024–2025. Treat the wage premium as suggestive evidence rather than causal proof.

---

## 3. The irreducibly human taxonomy

If the AI+1 frame is the structural claim, the *irreducibly human taxonomy* is the operational one. It names which decisions stay with you.

Michael Polanyi wrote in 1966 that "we can know more than we can tell."[^polanyi] He was describing tacit knowledge — the things professionals do well that cannot be reduced to a written rule. Donald Schon picked up the same thread in 1983 with *The Reflective Practitioner* and named it *reflection-in-action*: the way a professional thinks *while* doing, adjusting as the situation talks back.[^schon] Both are describing what your AI tools cannot do for you, because the AI tools were trained on the things that *can* be written down.

For a freelance designer with one primary client, the irreducibly human layer breaks down into eight competencies. The exact list varies by domain; the structure does not.

| Human competency | Why AI cannot replace it |
|---|---|
| Client intuition | Built from relationship history, emotional cues, internal politics, trust, unstated preferences |
| Taste — subtractive judgment | Not pattern recognition; judgment under constraints; knowing what to *remove*, not just add |
| Creative accountability | Clients pay for risk mitigation and ownership of decisions; AI cannot absorb reputational fallout |
| Brief interpretation | The written brief is rarely the real problem; experienced designers interpret, not execute |
| Constraint navigation | Designers turn constraints into stronger work, not merely smaller work |
| Presentation and persuasion | Design must be defended live under client questioning, in front of a buying committee |
| Cultural and contextual reading | AI learns from historical data; misses emerging context, taboo shifts, local nuance |
| Brand stewardship | A brand is a memory system, not a style prompt |

This is not a 2024 list pretending to be eternal. The "irreducibly human" boundary moves. Erik Brynjolfsson has argued, persuasively, that several categories on lists like this will erode faster than current consensus expects.[^brynjolfsson] Five years ago, "image generation" was on a list like this one. The list updates.

Two implications for how to use this table:

First, *treat the list as the current frontier, not as a fortress*. Anything that depends on tacit client knowledge belongs in the protect column **until you can articulate exactly why it does not**. The act of articulating the protection is the act of doing the work.

Second, *do this exercise for your own domain*. The eight categories above are designer-specific. A tax accountant's list looks different. A litigator's looks different. A nurse practitioner's looks very different. Exercise 1 walks you through producing your own version using the three-LLM research prompt. That is where the chapter becomes practical.

The fluency trap, restated as a one-line professional decision: *never let the AI make a call from your right-hand column*.

[^polanyi]: Polanyi, M. (1966). *The Tacit Dimension*. University of Chicago Press.
[^schon]: Schön, D. A. (1983). *The Reflective Practitioner: How Professionals Think in Action*. Basic Books.
[^brynjolfsson]: Brynjolfsson, E. (2023). "The Turing Trap: The Promise and Peril of Human-Like Artificial Intelligence." *Daedalus*, 151(2), 272–287. Also Brynjolfsson's subsequent work on AI complementarity, 2024–2025.

---

## 4. The three-LLM research prompt — structure

You cannot trust me on what is "irreducibly human" in your field. You cannot trust any single LLM either. Each frontier model has a distinctive signature — Claude leans into nuance and explicit uncertainty markers; GPT tends toward confident enumeration; Gemini tends toward retrieval-grounded reporting with specific named tools and dates [contested — practitioner observation, model behavior shifts across versions]. Each is wrong about different things.

The three-LLM domain research prompt is the move that catches what one model misses. You run the same structured prompt across Claude, GPT, and Gemini. Where all three agree, you have settled territory. Where they diverge, you have contested ground worth flagging. Where one raises a point the others missed, you have a candidate for your synthesis.

This is *investigator triangulation* in Norman Denzin's 1978 vocabulary — using multiple independent investigators to catch what any single one misses.[^denzin] It is also a rough application of Surowiecki's *Wisdom of Crowds* — aggregation outperforms individual estimates under conditions of diversity, independence, and aggregation.[^surowiecki] The three frontier LLMs satisfy these conditions weakly (they overlap enormously in training data), but they satisfy them better than any single model does on its own.

The prompt has eight sections. Each section asks for a specific kind of evidence. The structure forces parallel outputs across the three models, which is what makes the synthesis tractable later.

> **Prompt template — adapt the bracketed field to your own domain:**
>
> *I am a [graphic designer] researching how AI is currently affecting
> my profession. Please produce a structured report with the following
> eight sections:*
>
> 1. *AI tool adoption by role and workflow stage*
> 2. *Documented failure modes when AI is used in this work*
> 3. *Copyright, IP, and legal-exposure landscape*
> 4. *The fluency trap pattern in this domain — output that looks
>    professional but fails expert review*
> 5. *Labor-market data: postings, rates, displacement, wage premium*
> 6. *The irreducibly human taxonomy — what AI cannot do here*
> 7. *Existing training and certification for AI literacy in this field*
> 8. *The context-specific risks for solo or one-primary-client
>    practitioners*
>
> *For each section: cite sources where you can; mark contested claims;
> distinguish current-state from settled territory. Length: roughly
> 1,500–2,500 words.*

Run this verbatim in Claude. Run it verbatim in ChatGPT. Run it verbatim in Gemini. Save all three outputs in plain markdown.

You will get three documents that are recognizably about the same field and confidently disagree on several specifics. That disagreement is the value. A single LLM cannot disagree with itself; three of them can. Your job is to read across the three and produce a synthesis — which is what Chapter 3 walks you through in detail.

[^denzin]: Denzin, N. K. (1978). *The Research Act: A Theoretical Introduction to Sociological Methods* (2nd ed.). McGraw-Hill.
[^surowiecki]: Surowiecki, J. (2004). *The Wisdom of Crowds*. Doubleday.

---

## 5. What to do with the research output

The research output is *not* the textbook. It is the input to the Tic TOC session that produces the textbook.

This is the load-bearing distinction. Authors who go straight from "I have a research brief" to "let me prompt Cowork to draft my book" produce what this book calls a *Cowork dump* — a polished-looking manuscript that fails the fluency trap test at every chapter. The research brief is the raw material. The Tic TOC session in Chapter 4 is the foundry. The TIKTOC.md that comes out the other end is what Cowork can actually execute against.

What the research brief gives you, concretely:

1. **A defensible position on what is settled and what is contested in your field.** This is the basis for every claim your book will make.
2. **A list of the AI failure modes specific to your domain.** This is the spine of your Chapter 1, whatever your book is called.
3. **An irreducibly human taxonomy for your readers.** This is what your book promises to protect.
4. **A current-state snapshot of labor-market signal.** This is the evidence you cite when readers ask "why does this matter now."
5. **A working bibliography.** Not exhaustive — but enough to anchor your Tic TOC session and your Chapter 3 deliverable.

The brief is also a rehearsal. Before you spend two hours in a structured conversation with Tic TOC where every vague answer triggers pushback, you should have already practiced reading LLM output critically. The fluency trap check on your own research output is the warm-up for the fluency trap check on your own TIKTOC.md — and, eventually, on your own enrichment exercises in Chapter 10.

The chapter you are reading now is the *inoculation*. Chapter 10 is the *booster*. In between is the pipeline.

---

## Worked example — the three-LLM research prompt run for graphic design

The chapter's worked example is the actual research brief produced for `ai-for-designers-a-practitioners-guide`, the running example of this book. The full synthesized brief lives in `pantry/ai-for-designers-final-brief.md`; what follows is the annotated walk-through of what the three-LLM run produced and how to read it.

The prompt was run verbatim across Claude (with web research enabled), GPT-4, and Gemini 1.5 in May 2026. Three outputs returned, each between 1,800 and 3,200 words. Combining them produced a synthesized brief organized around the eight sections of the prompt.

**What the three-LLM run produced — selected highlights with annotation:**

> *Core thesis (all three passes agree):* AI does not replace the
> designer. It compresses low-level production work and raises the
> premium on judgment, taste, client intuition, and creative
> accountability.

Note the convergence. All three models, with different training data and different output styles, arrived independently at the same structural claim. This is the kind of agreement that survives synthesis. The claim is settled territory for the field as of May 2026.

> *Adoption data (Gemini synthesis — most specific):* 93% of graphic
> designers use AI-powered tools at least once a week. 82% use them
> to overcome "blank canvas syndrome." Only 12% trust these tools to
> handle high-stakes branding for Fortune 500 companies.

Gemini surfaced the specific percentages. Claude and GPT both gestured at "widespread adoption" without specifics. **Reading move:** the most specific number is not necessarily the most accurate — verify the source (Figma State of the Designer 2026) before quoting in your book. Treat Gemini's numbers as candidates for verification, not as facts.

> *Fluency trap pattern #1 (all three passes agree — primary fluency
> trap pattern):* Brand-correct surface, brand-wrong meaning. AI can
> imitate visible brand artifacts: colors, shapes, photographic style,
> layout density, tone words. It cannot replicate the invisible brand
> logic: what the client avoids, what past campaigns taught them, what
> competitors own, what internal politics require.

All three. Independently. This is the most reliable single claim in the brief.

> *IP doctrine (Gemini synthesis only — the sharpest formulation):*
> *Nemo dat quod non habet* — you cannot give what you do not have.
> A designer who generates a logo entirely with AI possesses no
> copyright in that work. Any standard IP assignment in the designer's
> contract transfers NOTHING to the client.

Gemini surfaced the legal doctrine. Neither Claude nor GPT named it. This is *divergent-as-gap* — a real piece of information one model retrieved that the other two missed. **Reading move:** verify the legal claim against the actual Copyright Office reports and Thaler v. Perlmutter [verify — D.C. Circuit ruling, 2025], then include in the brief with attribution.

> *Junior pipeline gap (Gemini synthesis — clearest formulation):*
> Historically, agencies hired junior designers for production tasks.
> AI is automating these Tier 1 tasks. Studios are hiring fewer
> juniors. Early-career designers have fewer opportunities to gain
> real-world experience. This threatens the long-term pipeline of
> senior design talent.

Another divergent-as-gap. Gemini saw a structural problem the other models did not raise. This is the value of the three-LLM run — it surfaces structural arguments a single model would have missed.

**The synthesis move:** Read the three outputs side by side. Mark each claim as ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY. Write a 600–800 word synthesis. Flag contested claims explicitly. Where one model adds what the others missed, decide whether to keep it (and attribute it) or drop it.

The full synthesized brief that came out the other end of this process — the four-section format that the Tic TOC /i1 session uses as input — runs to roughly 9,000 words. It is reproduced in full at `pantry/ai-for-designers-final-brief.md` and is the primary input that produced the TIKTOC.md you will see in Chapter 2 and the working session you will see in Chapter 4.

Read it once. Notice how every claim is either flagged as settled, flagged as contested, or attributed to a specific model. That is what a research brief ready for Tic TOC looks like.

---

## Exercises

### Exercise 1 (Apply) — Run the three-LLM domain research prompt for your own field

Use the prompt template in section 4 of this chapter. Adapt the bracketed field. Run it verbatim in Claude (with web research enabled), GPT-4 or later, and Gemini. Save all three outputs to a folder on your machine.

**Time required:** 45–60 minutes including running the prompts, copying outputs, and saving files.

**Deliverable:** Three plain-text or markdown files named `claude-output.md`, `gpt-output.md`, `gemini-output.md`. No synthesis yet — that is Chapter 3.

### Exercise 2 (Analyze) — Identify three fluency-trap examples in your domain from the research output

Read the three outputs from Exercise 1. Find three examples of AI output failure modes specific to your field. For each example, write:

- **The failure pattern** (one sentence).
- **Why a non-expert would not notice the failure** (one sentence — this is what makes it a fluency trap, not a regular bug).
- **What the expert sees that the non-expert misses** (one sentence — this is the irreducibly human layer).

**Deliverable:** A 200-word memo, three examples, total roughly 60 words per example.

### Exercise 3 (Evaluate) — Assess whether AI is creating a wage premium or displacement risk in your field

Re-read section 5 of each of the three LLM outputs (the labor-market section). Identify:

- The strongest piece of evidence that AI is creating a wage premium for AI-fluent practitioners in your field.
- The strongest piece of evidence that AI is displacing workers in your field.
- Your considered judgment, in 100–200 words, about which signal is currently stronger in your specific subfield, and why.

This is an evaluate-level exercise: there is no correct answer. There is a *defensible* answer, supported by your reading of the research output and your domain expertise. The exercise is the defense, not the conclusion.

**Deliverable:** A 200-word position memo with one piece of evidence cited on each side and one sentence of disclosure about your own uncertainty.

---

## Still puzzling

Honest open questions where the chapter's confidence does not match the field's confidence:

- *How durable is the irreducibly human taxonomy?* The list in section 3 is the current frontier. Five years from now, three of those competencies may have shifted into the AI column. There is no settled science here — only the practitioner's running judgment, which the chapter recommends you keep updating.
- *Is the wage premium causal or selection bias?* The PwC data shows correlation. Critics argue survivor selection. Both can be right; the policy implications differ. The book does not resolve this — it cites the directional evidence and asks you to make your own call.
- *Does the three-LLM rotation actually work, or is it ritual?* No peer-reviewed study confirms that three frontier LLMs produce better domain research than one frontier LLM with verification. The chapter recommends three because the convergence-divergence-gaps pattern is more legible across three than across one. This is a practitioner heuristic, not a finding.
- *What happens when LLMs are no longer distinguishable?* Claude, GPT, and Gemini will converge as the field matures. The "three different signatures" claim will weaken. The triangulation logic survives convergence (independent investigators are still independent) but the texture of disagreement may flatten.

---

## What would change my mind

I would revise this chapter's central claim — that the AI+1 frame preserves professional identity by locating the irreducibly human layer — if strong evidence emerged that markets reward AI-generated work *equally even when practitioners cannot defend, revise, or explain it*. The closest current evidence runs the other way: client questioning collapses undefended work, and that collapse is the reputational cost that pays the wage premium. If that mechanism breaks — if clients stop asking why, or if AI systems begin reliably incorporating tacit relationship knowledge — then the protected layer in section 3 stops being protected, and the AI+1 frame becomes a transitional posture rather than a durable one. The arrival of agentic systems with persistent client-specific memory is the most likely accelerant. I would update at that point, not before.

---

## AI Wayback Machine — Lucy Suchman

> **Prompt to run in Claude or ChatGPT:**
>
> "Read the Wikipedia article on Lucy Suchman. In 300 words, explain
> how her concept of 'situated action' applies to the way a freelance
> graphic designer makes judgment calls during a client call —
> judgments that an AI assistant cannot make for them."

Suchman is an anthropologist of work who argued, against the Stanford AI mainstream of the 1980s, that intelligent machines do not replace human judgment but *reconfigure* the work it does. Her 1987 book *Plans and Situated Actions* is the intellectual ancestor of the AI+1 frame. The prompt is short. The Wikipedia article is accessible. The deliverable is a one-page memo you can keep alongside your delegation map. [^suchman]

[^suchman]: Suchman, L. A. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press. Second edition published 2007 as *Human-Machine Reconfigurations*.

---

## Bridge — Chapter 2

The fluency trap is now felt and named. You can see it in your own field, in your own outputs, in your own drafts. You can name the irreducibly human layer that protects against it. You have the three-LLM research prompt and you have a sense of what the synthesized brief looks like when it is done.

That is the diagnosis. What you do not yet have is the *structural response*.

Tic TOC is the structural response. The two-hour conversation that produces a TIKTOC.md is the architecture that catches the fluency trap before it becomes a chapter, then a chapter, then a book. Chapter 2 shows you the product — the ai-for-designers TIKTOC.md, in full — before it explains how the product was made.

You will see what comes out of the session before you see the session.

Then you will understand why two hours there is the right first move.
