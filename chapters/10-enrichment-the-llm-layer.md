# Chapter 10 — Enrichment: The LLM Layer
*The fluency trap, one more time — this time inside the textbook that warned you about it.*

**Capability:** Students run the enrichment pipeline to add domain-specific, hands-on LLM integration to every chapter and evaluate whether the result meets the AI+1 standard.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Evaluate)** State the AI+1 standard for LLM Exercises in one sentence and apply it as a test to any exercise in any chapter draft — distinguishing exercises that survive the transplant test from those that fail it.
2. **(Analyze)** Distinguish a Dig Deeper prompt from an LLM Exercise by placement, purpose, and deliverable — and explain why mixing the two breaks the chapter.
3. **(Apply)** Run the "With LLMs" Curriculum Enrichment Generator through all three phases, select a running project from the proposed candidates, and confirm Chapter 00: Claude Basics is generated.
4. **(Apply)** Revise a failing generic LLM Exercise into a domain-specific one — naming the specific domain knowledge added and explaining why no generic prompt could have supplied it.
5. **(Evaluate)** Audit three LLM Exercises across your book against the AI+1 standard, flag any that fail, and produce a one-paragraph diagnosis per failure.

---

## Two exercises, same chapter — the fluency trap returns

Open the *ai-for-designers* draft. Chapter 7 — *The Cowork Draft Run*. Two LLM Exercises were proposed for the end of this chapter on different runs. Read both.

> **Exercise A.** *Ask Claude to explain the eight-section structure of a textbook chapter. Then ask Claude to draft a chapter using that structure for a topic of your choice. Read the output and identify three improvements you would make.*

> **Exercise B.** *Open your most recent client brief — the one with the most contested feedback. Paste it into Claude with this prompt: "Read this brief as a senior creative director would. Where is the client telling me what they want, and where are they telling me what they don't want? Quote the lines and explain." Then read Claude's answer next to your own read. List three places where Claude saw something you missed, three places where Claude misread the client's voice because the model has not worked with this client before, and one decision you will make differently on the next round of revisions.*

Exercise A is generic. It would work — unchanged — in a textbook on cooking, accounting, screenwriting, or veterinary medicine. The prompt is about how Claude responds, not about how a freelance designer uses Claude inside a real client relationship.

Exercise B is AI+1. Built around a real client brief the designer has. It assumes the *irreducibly human* layer — the designer has read this client before, heard their feedback, has a sense of what they want that the brief does not state. It uses Claude as a *second reader* whose disagreements with the designer's read are the data. It cannot transplant. The accountant has no client brief in this sense. The exercise is *only useful for this domain, this reader, this career stage*.

This is the fluency trap at the pedagogy scale. A textbook can be written entirely in Exercise-A form. The exercises will look correct and read pedagogical. They will teach nothing the reader could not get from the Claude documentation, and they will hand the reader the habit of using LLMs the way the textbook used them — as if the domain did not matter. This is what Chapter 10 is built to prevent.

You caught the verbal fluency trap in Chapter 1. The visual fluency trap arrived in Chapter 9. The pedagogical fluency trap arrives here. Same shape, different layer.

---

## Block one — The AI+1 standard for LLM Exercises

The AI+1 standard is a single test, stated as a question:

> *Could this exercise appear in a different field's textbook unchanged? If yes, it fails.*

The "different field" is at the *field* level, not the sub-specialty level. A graphic-design exercise that transplants to product design might still pass — they are adjacent sub-specialties within design. A graphic-design exercise that transplants to accounting fails. The standard is set at the field boundary, not the sub-specialty boundary, because that is where the *irreducibly human* layer lives: in the domain expertise that the LLM cannot infer from training data because the data is private, embodied, relational, or local.

This is not arbitrary. The deep-source argument is Paulo Freire's, from *Pedagogy of the Oppressed* (1968; English trans. 1970, Continuum). Freire's critique of what he called the "banking model" of education — the teacher deposits content, the student stores and withdraws — is that it treats the learner as a *container* for transferable knowledge rather than as a domain-situated practitioner. A generic LLM exercise *is* a banking-model exercise. bell hooks extended Freire in *Teaching to Transgress* (1994, Routledge), arguing pedagogy must be *engaged* — must take the learner's specific context seriously. The AI+1 standard is engaged pedagogy translated into an exercise-design rule.

There is empirical backing. Eric Mazur's concept-inventory research at Harvard (*Peer Instruction*, 1997) and the Force Concept Inventory work that preceded it (Hestenes, Wells, Swackhamer, *The Physics Teacher*, 1992) demonstrated that students who pass traditional exams routinely fail at the *application* layer when the application is novel. The AI+1 analog is exact: students who complete generic LLM exercises retain *generic prompting habits* and fail to apply LLMs to their own domain. The exercise has to test domain integration, not prompt syntax.

There is a bound on the standard. Apply it too aggressively and you produce hyper-specific exercises that no individual reader matches — for a designer who works in branding for D2C fashion startups in Brooklyn during economic downturns. The standard is *field-distinguishing*, not *individual-distinguishing*. Graphic design as a whole. If the generator drifts toward hyper-specificity, edit back.

### The three-question audit

For any LLM Exercise in your book, ask:

1. **Could this appear in a different field's textbook unchanged?** If yes — fails.
2. **Does it require the reader to bring something only they have?** A real brief, portfolio, client, or remembered failure. If no — fails.
3. **Is the deliverable a judgment, not a generation?** The reader should produce a *decision* the LLM could not have produced. If the deliverable is just LLM output — fails.

An exercise that passes all three is doing AI+1 work. An exercise that fails any one is, on at least one axis, generic.

---

## Block two — Dig Deeper vs. LLM Exercise

The enrichment pipeline adds two kinds of LLM-integrated content to each chapter, and they are *different*. Mixing them is one of the most common failures the enrichment pass produces.

### Dig Deeper — inline, optional, low-stakes

A Dig Deeper prompt is a short copy-paste-ready prompt embedded *in the chapter prose*, at the moment it would be useful. It is offered as an optional rabbit hole — the reader can take it or skip it without losing the thread of the chapter. Two to four per chapter is typical.

**Placement:** Inline, at the moment in the chapter where the prompt would be useful. Usually right after a concept is introduced and right before the next concept builds on it.
**Purpose:** Let the reader extend the chapter's argument into their own domain, in a low-stakes way that does not commit them to a deliverable.
**Deliverable:** None enforced. The reader gets value from running the prompt. The textbook does not require an artifact.

Example, mid-chapter in *ai-for-designers* Chapter 7:

> **Dig deeper.** *Take one of your last three project briefs. Paste it into Claude with: "What is this client asking for in a way that does not name what they actually want?" Read the answer. You do not have to do anything with it. Notice whether Claude saw something you missed.*

### LLM Exercise — end of chapter, mandatory, deliverable required

An LLM Exercise sits at the *end* of the chapter, in the exercises section, with the same Apply/Analyze/Evaluate Bloom's label as the other exercises in that block. It is mandatory in the sense that it produces a deliverable the reader will reference later. Usually one per chapter.

**Placement:** End of the chapter, inside the assessable-exercises block. Numbered alongside the other exercises.
**Purpose:** Advance a *running project* across the chapters so that by the end of the book the reader has built something cumulative, not a list of disconnected outputs.
**Deliverable:** A concrete artifact — a paragraph, a comparison, a revised brief — that the reader saves and returns to in a later chapter.

Example, end of *ai-for-designers* Chapter 7:

> **Exercise 7.4 (Apply).** Take the brief you used in the Dig Deeper above. Paste it into Claude with the prompt: "Read this brief as a senior creative director would. Where is the client telling me what they want, and where are they telling me what they don't want? Quote the lines and explain." Save Claude's response. Read your own first-pass interpretation alongside it. Write 250 words naming three places Claude saw something you missed, three places Claude misread the client because the model has no relationship history, and one revision decision you will make differently on the next round.

Same chapter. Same client brief. Different scaffolding.

The Dig Deeper is permission-to-explore. The LLM Exercise is the assignment. The deliverable from the LLM Exercise — the 250-word comparison — becomes part of the *running project* the next chapter will reference.

### Failure mode — using a Dig Deeper as an LLM Exercise

The most common enrichment-pass failure is putting what should be an LLM Exercise inline as a Dig Deeper. Symptom: the prompt is consequential, the reader should produce an artifact, but it lives in the middle of the chapter with no deliverable enforcement. Or the inverse: an LLM Exercise that has the casual structure of a Dig Deeper — no scaffolded prompt, no required output, no place to save the result.

Audit pattern: an LLM Exercise without an explicit *Save this. You will use it in Chapter X.* belongs as a Dig Deeper. A Dig Deeper that says *Write 250 words and submit them in your portfolio* belongs as an LLM Exercise.

---

## Block three — The "With LLMs" Curriculum Enrichment Generator

The enrichment pipeline has a name, and it has three phases. The name on the prompt-library is *"With LLMs" Series — Curriculum Enrichment Generator*. The three phases — detect state, generate Chapter 00, enrich every chapter — run in order and they pause for your judgment between them.

### Phase one — detect book state

The generator reads your book and decides whether the chapters are draft-ready or whether the draft pass needs to run first. There are three states:

- **State A — written flat chapters.** Chapters exist in `chapters/` as a flat list of `.md` files. Most readers of this book will be in State A by Chapter 10 — Chapter 7 produced the drafts, Chapter 8 rewrote them, Chapter 9 added subtitles and figures. The generator skips drafting and proceeds.
- **State B — source subfolders.** Chapter material exists as subfolders like `chapters/03-domain-research/01-source.md`, `02-source.md`. This is the OpenStax-import or student-submission pattern. The generator triggers a conversion pass first.
- **State C — external source.** Chapters live elsewhere — a Google Doc folder, a separate repo. The generator pauses and asks you to bring them in.

You are in State A. The generator proceeds.

### Phase two — generate Chapter 00: Claude Basics for [your field]

The generator writes a full onboarding chapter, called `00-claude-basics.md`, customized to your book's field. The chapter is the reader's *introduction to the LLM layer* — what Claude can and cannot do for this craft, when to use Claude vs. a Claude Project vs. Claude Code vs. Cowork, and what Claude's field-specific failure modes look like.

Chapter 00 is doing work the rest of the book cannot do efficiently. The rest of the book has LLM Exercises and Dig Deeper prompts scattered through it. Chapter 00 explains the *vocabulary* once so the rest of the book does not have to. Without it, the LLM Exercises read as a series of disconnected prompts. With it, they read as a curriculum.

This is the worked example for this chapter. We will look at the *ai-for-designers* version in the next section.

### Phase three — propose running projects, then enrich all chapters

The generator reads the full TIKTOC.md, reads the chapter drafts, and proposes three to five candidate *running projects* — a cumulative artifact the reader will build across chapters via the LLM Exercises. For *ai-for-designers*, the proposed projects were:

1. **A redesigned client brief deck.** Iteratively improved across chapters as the reader learns to use Claude for brief intake, variant generation, design-system audit, and portfolio positioning.
2. **A personal positioning document.** Self-portrait of the reader's practice, built from Claude's outside-reader audits of the reader's portfolio across chapters.
3. **A workshop curriculum.** The reader's own next-quarter workshop on AI for working designers, built chapter by chapter from the textbook's frame.

The generator pauses and asks the author to pick one — only one. The running project will appear in every chapter's LLM Exercise from this point forward. Mixing projects produces a fragmented sequence; one project produces a cumulative artifact.

Once the project is chosen, the generator runs across every chapter and inserts two to four Dig Deeper prompts inline and one LLM Exercise at chapter end. It updates the TOC. It logs every insertion. The book becomes an AI+1 textbook — domain-specific, hands-on, cumulative — at the pedagogy layer.

### What can go wrong in phase three

Two failure modes show up regularly:

1. **The generator produces a Dig Deeper that is too generic** because the chapter prose did not give it enough domain hooks to work with. Diagnosis: open the chapter. If the prose itself does not name specific tools, specific deliverables, specific moments in the reader's workflow, the generator has nothing to attach to. The fix is to enrich the *chapter prose* before re-running the generator on that chapter.
2. **The LLM Exercise does not advance the running project.** Diagnosis: the chapter is about a topic that does not cleanly connect to the chosen project. Either the running project was poorly chosen (pick a different one and regenerate), or the chapter needs a *different* end-of-chapter exercise that does not advance the project. Both are acceptable. A book does not need every chapter to feed the running project — three-quarters is fine.

---

## Block four — The AI Wayback Machine

The enrichment pipeline has a fourth artifact — the AI Wayback Machine. After the LLM Exercises are in place, this generator runs across every chapter and inserts a short section connecting the chapter's argument to a lesser-known historical figure whose work substantively connects. Three operating principles:

**Substantive connection only.** A figure included for representation but whose work does not connect to the chapter's argument *fails the AI+1 standard at the figure-selection layer*. A token figure is a tokenized chapter. If the connection from figure to argument is forced, drop the figure and find one whose work genuinely bears on the chapter.

**Diverse on multiple axes.** Gender. Geography. Era. Discipline. The generator maintains a diversity tracker and reports at the end. Across Chapters 1 through 11 of a typical AI+1 book the targets are *at least one woman per book*, *at least one non-Western figure*, *no era or discipline in more than half the chapters*. Sara Ahmed's *Living a Feminist Life* (2017, Duke) frames this as "diversity work" — representation done well is *labor*, not gesture.

**Wikipedia instruction, not Wikipedia summary.** Every prompt directs the reader to a *substantial* Wikipedia entry. The Wiki Education program (wikiedu.org, 2010–present) uses the phrase: students read Wikipedia critically and produce something. The textbook is not summarizing Wikipedia; it is teaching the reader to *use* it. Every Wayback prompt should have a follow-up move — *verify a claim against a second source*. Wikipedia is an excellent starting point and an inadequate ending point.

---

## Block five — The fluency trap at the pedagogy scale

Once the enrichment pipeline has run, the AI+1 standard becomes an *audit* problem. You have somewhere between twenty and sixty new LLM-integrated artifacts in the book (Dig Deepers, LLM Exercises, Wayback prompts). Some of them passed the standard. Some did not. You will not catch the failures by reading them in order — they read fluently and pedagogically because they were generated by a fluent model.

The audit pattern that catches them:

### Pull every LLM Exercise into one document

Copy the LLM Exercise from every chapter into a single document. Strip the chapter context. Read them in sequence as if you had never seen the book.

Three failure patterns appear:

- **The interchangeable pattern.** Two exercises that could swap chapter positions without losing anything. Diagnosis: at least one of them is generic, possibly both.
- **The Claude-documentation pattern.** An exercise that teaches Claude itself ("Try this prompt format and observe how Claude responds"). Diagnosis: this is documentation, not pedagogy. Belongs in Chapter 00 if anywhere; rewrite or delete.
- **The no-deliverable pattern.** An exercise without a saved artifact. Diagnosis: this is a Dig Deeper, not an Exercise. Demote it.

### Apply the three-question audit

For each exercise, run the three-question audit from Block one. Mark each exercise as *passes all three*, *passes two of three*, or *passes one or zero*. The third bucket is the rewrite list.

### Rewrite, do not re-generate

When an exercise fails the audit, rewrite it by hand, not by re-running the enrichment generator. The generator produced the failure once; it is more likely than not to produce a similar failure on the second run. The rewrite is where you *name* the specific domain knowledge the exercise now requires the reader to bring — the real brief, the real portfolio, the real client, the real failure they remember.

The acid test for a rewrite: can you state, in one sentence, why no generic prompt could have supplied the same outcome? If the answer is "the reader has to bring [the specific thing only they have]," the rewrite passes. If the answer is "the reader has to bring expertise," that is not specific enough — every exercise in every textbook requires expertise. The standard demands specificity.

---

## Worked example — Chapter 00: Claude Basics for ai-for-designers

The generator produced a Chapter 00 for *ai-for-designers* that runs about 4,800 words. Here is the structure, annotated for what makes it AI+1 vs. what would have made it generic.

### Section 1 — What Claude can and cannot do *for a freelance graphic designer*

Generic version (what we did *not* write): *"Claude is a large language model that can answer questions, generate text, and assist with creative tasks."*

AI+1 version (what we did write): *"Claude can read a client brief and tell you what the brief is not saying. Claude can produce a logo concept brief that reads professional and is content-empty. Claude cannot tell you whether this particular client tends to backslide on color choices three weeks into a project. Claude can audit your portfolio site as an outside reader and surface positioning gaps. Claude cannot replace the taste-calibration conversation you had with your senior designer in your first year. This chapter is about the first set of moves, and about why the second set still belongs to you."*

The first version is true. The second version is *true and useful only for this reader*. The AI+1 standard at the chapter scale.

### Section 2 — When to use Claude vs. Claude Project vs. Claude Code vs. Cowork

Four Anthropic-stack tools, each paired with a part of the freelance workflow:

- **Claude (chat).** Brief reading, variant evaluation, portfolio reads. One-shot. ~80% of LLM use.
- **Claude Project.** Ongoing client work where the conversation needs to remember the brand guide and past decisions. ~15%.
- **Claude Code.** Automation — batch-renaming assets, scripting Figma exports, design-system token reports. ~5%, high-leverage.
- **Cowork.** Book-building. The tool the reader is using *right now* to build this very book.

A generic Chapter 00 would say "Claude is good at X, Y, Z." The AI+1 Chapter 00 says "you, the freelance designer building this book, will use Claude in chat for most of your daily work, and Cowork for the activity you are doing right now."

### Section 3 — Worked example — Brief Intake on a real client brief

The chapter walks through an anonymized real brief, pasted into Claude with the Brief Intake prompt. The annotation calls out three places Claude saw something the designer would have seen, three places Claude missed something the designer would have caught, and one place Claude *introduced* a constraint the brief did not state — which the designer caught and rejected.

A generic version would show a hypothetical "client X asks for a logo for company Y" example. The AI+1 version shows the actual texture — the unstated constraints, the political dynamics, the moment Claude invents a constraint. The reader sees the workflow at production speed, not tutorial speed.

### Section 4 — Claude's field-specific failure modes for freelance graphic designers

Five named failure modes, each with a one-paragraph diagnosis and a fix:

1. **The brief-summary trap.** Claude summarizes the brief and the summary obscures the contested terms. Fix: ask Claude to *quote* the disputed lines.
2. **Generative-fill overreach.** Adobe Firefly is excellent at production (background extension, object removal). Not at concepts. The designer should reject Claude's Firefly-for-concepts recommendations.
3. **Brand-system drift.** Figma AI Make can generate a form that looks like the brand. It will drift on type weights, grid units, tone. The drift compounds.
4. **Taste-calibration replacement.** Midjourney variants are faster than sketching. They will not surface the bad variants the designer needs to see to know what they are *not* doing.
5. **Portfolio-positioning blindspot.** Claude can read a portfolio and miss the meta-claim. Ask Claude what it would *expect* the next project to be, and notice where its expectation diverges from yours.

Every failure mode names a specific tool paired with a specific freelance-design workflow. A generic Chapter 00 would describe failures at the model level ("Claude can hallucinate"). The AI+1 Chapter 00 describes them at the *workflow-integration* level — where the reader will encounter them.

### What would have made this chapter generic

The chapter would have failed the AI+1 standard if it:

- Spent more than two paragraphs on what an LLM is in general terms.
- Listed Claude's capabilities without pairing each capability with a designer-specific workflow.
- Showed worked examples with hypothetical clients, hypothetical briefs, hypothetical portfolios.
- Used failure modes drawn from "common LLM mistakes" rather than from the freelance graphic design workflow.

The line between AI+1 and generic is the *binding of the LLM behavior to the domain workflow*. When that binding is tight, the chapter passes. When the binding is loose — when the chapter could be re-titled "Claude Basics for Accountants" with a search-and-replace on field names — the chapter fails.

---

## Exercises

### Exercise 10.1 — (Apply) Run the enrichment generator and select a running project

Run the "With LLMs" Curriculum Enrichment Generator. Let it run through phase one (state detection) and phase two (Chapter 00 generation). Pause when it presents the candidate running projects. Read all three to five candidates carefully.

- Pick one. Document your choice and the reasoning in three sentences.
- Confirm Chapter 00: Claude Basics has been generated for your field.
- Spot-check Chapter 00 against the four failure modes named in the worked example above. Note any sections where the chapter is too generic to your specific field.

Deliverable: the generated Chapter 00 plus a one-paragraph audit of its AI+1 strength, with your running-project choice and rationale.

### Exercise 10.2 — (Evaluate) Apply the AI+1 test to three LLM Exercises

After the generator has run through phase three, pull three LLM Exercises from three different chapters into a single document. Strip the chapter context. Apply the three-question audit:

- Could this exercise appear in a different field's textbook unchanged?
- Does it require the reader to bring something only they have?
- Is the deliverable a judgment, not a generation?

Mark each exercise as *passes all three* / *passes two of three* / *passes one or zero*.

Deliverable: a table with the three exercises, the audit answers per row, and a one-sentence diagnosis for any exercise that does not pass all three.

### Exercise 10.3 — (Apply) Revise one failing LLM Exercise

Pick the worst-scoring exercise from Exercise 10.2. Rewrite it by hand — not by re-running the generator. In the rewrite, do three things:

1. Name the *specific domain knowledge* the exercise now requires the reader to bring. A real artifact (a brief, a portfolio, a project file), or a real memory (a project that went wrong, a client who pushed back).
2. Change the deliverable to a judgment the reader produces — not just LLM output.
3. State, in one sentence at the end of the rewrite, why no generic prompt could have supplied the same outcome.

Deliverable: the original exercise, the revised exercise, and the one-sentence statement of irreducible domain specificity.

---

## AI Wayback Machine — bell hooks

You have already met bell hooks in this chapter — she is one of the deep sources for the AI+1 standard. Her *Teaching to Transgress* (1994) is the operational case for engaged pedagogy.

Worth knowing beyond the citation: she chose the lowercase styling of her pen name (Gloria Jean Watkins) deliberately, taking it from her great-grandmother Bell Blair Hooks and dropping the capitals to draw attention away from the author and toward the work. She taught at Yale, Oberlin, CCNY, and at Berea College in Kentucky — the last chosen because Berea served Appalachian students who would not otherwise have access to elite education. The pedagogical commitment was operational, not abstract. Her argument: pedagogy that does not take the learner's specific context seriously *cannot* produce competent practitioners. It produces *credentialed* students.

**Try this prompt:** *Visit the Wikipedia page for bell hooks. Read the sections on "Teaching to Transgress" and "engaged pedagogy." In 250 words, explain why hooks would predict that generic LLM exercises will fail to produce competent practitioners. Then revise one LLM Exercise in your draft to be more "engaged" in hooks's sense — name the specific learner context you are now addressing.*

Sharper: name the chapter and exercise you are revising. Ask Claude to articulate what *engagement* means in operational, exercise-design terms. Then ask: *what evidence from outside hooks's work would you want to see to test her claim empirically?* Wikipedia is the starting point; *Teaching to Transgress* (Routledge, 1994) is the ending point.

---

## Bridge — content-complete, one check away

The book is now content-complete. The prose is the author's. The figures encode arguments. The LLM Exercises pass the AI+1 standard. The Wayback Machine has done diversity work that bears on the chapters' arguments.

One layer remains — the layer that catches everything previous layers missed. The fact-checking pass. The build pipeline. The EPUB on a device. The submission to KDP. Chapter 11 is short. It is not skippable.

---

## Still puzzling

Open questions this chapter does not close:

1. **Where exactly is the field boundary that the AI+1 standard tests against?** Graphic design vs. product design is debatable. Graphic design vs. industrial design is more clearly distinct. The book takes the position that "field" means "what a working practitioner would name their profession to a stranger at a dinner party." That is not rigorous. A more rigorous answer might require an actual professional taxonomy (BLS occupation codes, or a discipline-specific equivalent).
2. **What happens when Claude becomes native at graphic-design judgment?** Suppose a 2030-era model can read a client relationship's history, calibrate taste, and surface unstated constraints — all the things this chapter named as irreducibly human in 2026. The AI+1 framing would need to *shift* to whatever the new irreducibly human layer becomes. The argument is not "Claude cannot do X forever." It is "there is always a current irreducibly human layer, and good pedagogy works at it."
3. **Should Wayback prompts be required or optional?** The pipeline treats them as required (one per chapter). A reader could reasonably argue some chapters do not have a strong historical-figure connection and the prompt is forced. Author judgment overrides. The pipeline produces a default; the author decides whether to keep it.
4. **What is the right ratio of Dig Deeper prompts to LLM Exercises across the book?** The generator's default is two-to-four Dig Deepers per chapter and one LLM Exercise. That works for most chapters. For chapters that are heavily conceptual — like Chapter 2 of this book, on *what Tic TOC does* — fewer Dig Deepers and one *stronger* LLM Exercise may be the right call. The default is a default.

## What would change my mind

The strongest counter-argument to the AI+1 standard is that *as LLMs improve at domain inference*, the line between "generic" and "domain-specific" will erode — because the generic prompt will produce domain-specific output when Claude already knows the field. If a body of empirical evidence emerged showing that generic LLM exercises, run through a 2028-era model, produced *the same learning outcomes* as AI+1-standard exercises run through a 2026-era model, the standard would have to weaken. The bet the book is making is that the irreducibly human layer (the private brief, the embodied taste calibration, the relational continuity) is *not* the kind of thing a more capable model gets better at, because the data is not in the training set and the data is privately held. If that bet turns out to be wrong — if Claude can somehow learn the contents of every freelance designer's locked Figma file — the AI+1 framing collapses. I do not expect this. I would update if I saw it.
