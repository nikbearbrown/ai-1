# Chapter 2 — What Tic TOC Does and Why You Spend Two Hours Here First

*The TIKTOC.md is not the author's outline. It is the book's instructional architecture — and the architecture is the product.*

**One-line capability:** Students learn what Tic TOC's three disciplines enforce, how to deploy it, and why the TIKTOC.md session is the highest-leverage step in the pipeline.

---

## Learning objectives

By the end of this chapter you will be able to:

- (Understand) Explain what Tic TOC's three disciplines — curriculum theorist, acquisitions pragmatist, instructional designer — each contribute to a TIKTOC.md that a Cowork run can actually execute.
- (Apply) Deploy Tic TOC: copy the system prompt, create a Claude Project, paste into Instructions, type /help, and begin /i1.
- (Analyze) Distinguish between a TIKTOC.md that is ready for Cowork and one that has unresolved phase-gate questions — and name what happens downstream when you skip a gate.
- (Evaluate) Explain to a colleague why spending two hours in a structured Tic TOC session before any writing produces a better book faster than starting with a Cowork prompt.

---

## Opening — read the product first

Most chapters explain the process and then show you the product.

This chapter does the opposite. Before any explanation, read what comes out of a Tic TOC session. The next several pages are an excerpt from the actual `TIKTOC.md` produced for `ai-for-designers-a-practitioners-guide` — the running example of this book. The excerpt is real. It was produced from a two-hour session in May 2026. The full document runs to roughly 7,000 words; what follows is selected sections totaling about 1,200 words.

Read it as a finished artifact. Notice what is in it. Notice what is *not* in it. Notice which lines you could not have written on your first try.

---

> **AI for Designers: A Practitioner's Guide**
> Full TOC Draft — compiled from all phase outputs
> Author: [redacted] · Series: AI+1 · Status: Pre-draft
>
> ---
>
> **PART 1 — BOOK CONCEPT AND THESIS**
>
> *Book concept summary:* This book teaches the **one-client freelance
> designer to operate as an AI+1 practitioner** — keeping the design
> identity, adding fluent and risk-aware AI use, and protecting the
> decisions that carry client trust, brand meaning, and creative
> accountability — by **walking them through the specific moves of an
> AI-enabled design practice: the delegation map, the contractual rider,
> the disclosure conversation, the brand stewardship discipline, and the
> portfolio defense.** It fills the gap left by tool tutorials (which
> teach Firefly but not the client conversation) and traditional design
> education (which teaches taste but not how to deploy AI without
> destroying it).
>
> *One-sentence logline:*
> The fluency trap costs you the account; the AI+1 designer keeps it.
>
> *Central thesis:*
> "This book argues that the working freelance designer's most valuable
> professional asset is the layer of tacit client knowledge that no AI
> tool can reach — and that AI fluency is most valuable when it
> accelerates production without ever being allowed to make decisions
> from that layer."
>
> ---
>
> **PART 2 — LEARNER PROFILE**
>
> *Primary reader:* A freelance graphic or brand designer with five to
> fifteen years of practice, one primary anchor client, and a
> ChatGPT-or-Claude tab open while reading this paragraph.
>
> *Prior knowledge assumed:* Working knowledge of Adobe Creative Cloud
> or Figma; basic familiarity with at least one generative AI tool;
> client-facing experience; comfort defending design decisions in a
> presentation.
>
> *Prior knowledge NOT assumed:* Legal training; copyright law;
> AI/ML literacy beyond consumer-grade tool use; experience writing
> for publication.
>
> *Prior misconceptions:*
> 1. "If the client likes it, it worked."
> 2. "The fluency trap means bad AI output."
> 3. "AI fluency means better prompting."
> 4. "If I reject AI, my role is safe."
>
> ---
>
> **PART 7 — LEARNING OUTCOMES BY CHAPTER (excerpt)**
>
> | Ch | Title | Bloom's Ceiling | Create-level outcome |
> |----|-------|----------------|----------------------|
> | 1 | The AI+1 Designer | Evaluate | — |
> | 2 | Production Tasks | Apply | — |
> | 3 | The Fluency Trap | Evaluate | — |
> | 4 | IP and Copyright | Apply | — |
> | 5 | Client Disclosure | Create | Disclosure framework |
> | 6 | The One-Client Relationship | Evaluate | — |
> | 7 | Taste and Accountability | Create | Defense rubric |
>
> ---
>
> **PART 8 — CHAPTER 1 ENTRY (excerpt — capability statement and bridge)**
>
> **Chapter 1 one-line:** *Readers learn to distinguish the AI+1
> designer from the designer who has been replaced — and to identify
> the specific decisions their own practice depends on protecting.*
>
> **Opening:** A freelance brand designer delivers an AI-generated
> identity system to a long-term client. The presentation looks clean.
> Six months later, the client asks: "Why did we choose this typeface?"
> The designer does not have an answer.
>
> **Bridge to Chapter 2:** The AI+1 designer is not the designer with
> the most tools. It is the designer with the clearest boundary between
> assistance and abdication. Chapter 2 turns the frame into a work
> tool: the delegation map.

---

That is the product.

Three things are doing work in those 1,200 words that would not be doing work in an ordinary outline.

First, the **capability statements**. Not topics. Not headings. Sentences that begin "Readers learn to…" and end with a verb that names what the reader can *do* by the end. *Distinguish*. *Identify*. Not *understand*. Not *be aware of*. The verbs are load-bearing.

Second, the **bridge question**. The Chapter 1 entry ends with a statement that names what Chapter 2 will answer. The bridge is a structural commitment — once it is written, Chapter 2 has to deliver on it. This is what stops a book from being eleven loosely connected essays.

Third, the **Bloom's ceiling table**. Every chapter has a maximum cognitive level it is required to reach. Some chapters are Apply ceilings — readers must *do* something. Some are Evaluate ceilings — readers must *judge*. Three of the eleven chapters in the ai-for-designers book are Create ceilings — the reader leaves with a deliverable in hand. Distributing those ceilings across the book is what makes it a textbook rather than a magazine.

The whole document is built like this. Sections have specified inputs and specified outputs. Cross-references are explicit. Open questions are logged. The result is something Cowork can read and execute against — without a clarifying conversation, without the model having to guess at the author's intent.

The rest of this chapter explains how this artifact got built. The honest version: by a two-hour structured conversation with a Claude Project running the Tic TOC prompt. That conversation is what the next sections describe.

---

## 1. What a TIKTOC.md is — and is not

A TIKTOC.md is the *instructional architecture* of your book. It is not the author's outline.

The distinction matters because the words sound similar and the artifacts look adjacent. Here is the precise difference:

| The author's outline | The TIKTOC.md |
|---|---|
| A list of chapter titles and topics the author plans to cover. | A structured document specifying capability statements, learning outcomes in Bloom's, sequencing logic, prerequisites, deliverables, contested claims, open questions. |
| Lives in the author's head or in a notes app. | Lives at the project root as `TIKTOC.md`; Cowork reads it at runtime. |
| Adequate for the author to start writing. | Adequate for Cowork to start writing. |
| Failure mode: vague enough that anything goes; the book drifts. | Failure mode: too specific to write fast; the gates force you to slow down. |

The TIKTOC.md is the *spec*. The Cowork run is the *implementation*. This distinction is borrowed directly from software engineering, where it is settled: specification quality predicts implementation quality, and the most expensive defects to fix are the ones introduced at the specification stage.[^curtis]

The empirical anchor for this claim is a famous 1988 paper by Curtis, Krasner, and Iscoe in *Communications of the ACM*. They studied seventeen large software projects and found that defects introduced during requirements analysis cost roughly 10–100x more to fix downstream than defects introduced during implementation. The deeper the defect was upstream, the more catastrophic the downstream rework.[^curtis] The number has been replicated in subsequent software engineering literature, with the exact ratio varying by domain.

The textbook analogy is inferred, not formally validated [verify — no peer-reviewed study confirms the 10–100x ratio for instructional-design specifications specifically]. But the practitioner experience matches the prediction. Authors who write a chapter with a vague capability statement spend more time rewriting the chapter than they would have spent fixing the statement. Two hours in Tic TOC up front saves dozens of hours of rewriting later. *This is the thesis, written as arithmetic.*

The TIKTOC.md is also not the same thing as a publisher's proposal, a book summary, a sales pitch, or an academic abstract. Those documents exist for different audiences. The TIKTOC.md exists for Cowork — a downstream automated system that needs a fully resolved specification because it cannot ask you to clarify what you meant.

[^curtis]: Curtis, B., Krasner, H., & Iscoe, N. (1988). "A Field Study of the Software Design Process for Large Systems." *Communications of the ACM*, 31(11), 1268–1287. Open access via the ACM Digital Library archive.

---

## 2. The three disciplines

Tic TOC behaves as if three different professionals were in the room with you for the entire session. The prompt does not literally instantiate three roles, but the questions it asks come from three distinct intellectual traditions, and naming them helps you understand *why* the prompt pushes back where it does.

**Discipline 1 — The curriculum theorist** asks: *Does this book have a coherent pedagogical arc?* Curriculum theory is the academic field that studies how learning experiences are designed. The canonical contemporary framework is Wiggins and McTighe's *Understanding by Design* (2005), which argues for *Backward Design* — start with the learning outcomes you want, design assessments that would demonstrate those outcomes, then design the instruction that prepares students to perform them.[^wiggins] The curriculum theorist in Tic TOC is the discipline that refuses to let you advance from /i4 (intake) to /l1 (outcomes) without a confirmed *Book Concept Summary*. The Summary is what Wiggins and McTighe call Stage 1: *Identify Desired Results*. They argue Stage 1 is the most-skipped step in curriculum design. Tic TOC enforces it as a software constraint.

An older but equally important name here is Hilda Taba, the Estonian-American curriculum theorist whose 1962 *Curriculum Development: Theory and Practice* argued for an inductive model — start from the specifics of student need and build the curriculum upward.[^taba] That is precisely what Tic TOC's /i3 (audience intake) phase enforces.

**Discipline 2 — The acquisitions pragmatist** asks: *Is there a market for this book and can the author actually deliver it?* This is the publishing-industry voice. It questions whether your reader actually exists, whether they have a budget or a reason to read, whether the timeline is realistic, and whether the book has positioning against comparable texts. The acquisitions pragmatist in Tic TOC is what refuses to let you advance through /m1 (market) without a defensible *positioning statement vs. comparable texts*.

There is no canonical academic source for this discipline because publishing acquisitions is a craft tradition, not a research field. The vocabulary the chapter uses here is borrowed from trade publishing — most notably from Greco's *The Book Publishing Industry* and from the operational realities of imprint editors who have to make acquisition decisions on incomplete information [verify — general trade publishing references; no single citation is load-bearing].

**Discipline 3 — The instructional designer** asks: *Can a reader actually learn this in this sequence?* This is the implementation voice. It questions whether your chapter ordering respects prerequisites, whether Apply-level outcomes appear before Evaluate-level outcomes, whether the cognitive load is bounded, whether the deliverables are graded. The instructional designer in Tic TOC is what refuses to let you advance through /c1 (chapter-by-chapter) without capability statements at Apply or above and explicit bridge questions between chapters.

Robert M. Gagné's *Conditions of Learning* (1965) is the canonical source here — the argument that different types of learning require different instructional sequences.[^gagne] The Anderson-Krathwohl 2001 revision of Bloom's taxonomy supplies the verb vocabulary: Remember, Understand, Apply, Analyze, Evaluate, Create.[^bloom] The Bloom's ceiling table you saw in the opening artifact is the instructional designer at work.

The three disciplines are not crisp categories. They overlap. Wiggins and McTighe are part curriculum theorist and part instructional designer. A working acquisitions editor borrows from both. The point of naming them is not academic taxonomy — it is to give you a vocabulary for noticing *which discipline is talking* when Tic TOC pushes back during your session. When the prompt says "the audience profile is too vague — who is the specific person you are writing for?" — that is the curriculum theorist asking Taba's question. When it says "what is the comparable book on the shelf next to this one?" — that is the acquisitions pragmatist. When it says "this capability statement has no verb a reader can demonstrate" — that is the instructional designer applying Mager.[^mager]

[^wiggins]: Wiggins, G., & McTighe, J. (2005). *Understanding by Design* (Expanded 2nd ed.). ASCD. First edition 1998.
[^taba]: Taba, H. (1962). *Curriculum Development: Theory and Practice*. Harcourt, Brace & World.
[^gagne]: Gagné, R. M. (1965). *The Conditions of Learning*. Holt, Rinehart and Winston. Multiple revised editions through the 1980s.
[^bloom]: Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives*. Longman.
[^mager]: Mager, R. F. (1962, revised 1997). *Preparing Instructional Objectives*. Center for Effective Performance.

---

## 3. The phase gates — why each exists, what breaks if skipped

Tic TOC is *phase-gated*. The session runs through three phases — Intake, Learning Architecture, Chapter Architecture — and you cannot advance past a gate until the prompt explicitly confirms the gate has been passed.

This is not novel software design. The phase-gate logic comes directly from Robert Cooper's 1990 paper *Stage-Gate Systems*, which formalized the practice in product development: work flows through clearly bounded phases with explicit decision gates between them, and compressing or skipping a gate produces compounding downstream cost.[^cooper] Cooper's original Stage-Gate had five gates. Tic TOC has three. The architecture is the same.

Here are the gates Tic TOC enforces and what each catches:

| Gate | Question the gate asks | What breaks if you skip it |
|---|---|---|
| /i4 → /l1 | Has the Book Concept Summary been confirmed? | Every downstream chapter drifts because there is no central thesis to align against. |
| /l4 → /c1 | Have learning outcomes been mapped to Bloom's levels with a defensible distribution? | Chapters end up reading like blog posts — interesting but not pedagogical. Cowork drafts pad. |
| /c4 → /g1 | Has every chapter received a capability statement and a bridge question? | The book becomes eleven loosely related essays. Readers cannot see why one chapter precedes another. |
| /g1 → /g2 | Has the full TOC been compiled into one document? | You cannot run the diagnostic against a TOC that is still in fragments. |
| /g2 → handoff to Cowork | Has the /g2 critique flagged and resolved high-risk failure modes? | Cowork drafts inherit the failure modes as voice drift, generic exercises, and padded middles. |

The gates are not bureaucracy. Each one catches a specific downstream defect. The diagnostic at /g2 — *the 7 Adoption Failure Mode critique* — runs the entire TOC against seven recurring failure modes for instructional texts (audience drift, missing prerequisites, over-claimed outcomes, contested claims unflagged, etc.). When /g2 returns clean, the TIKTOC.md is ready for Cowork. When /g2 flags items, those items are *blockers* — you resolve them, or you log them as BLOCKED in /p2 (the Open Questions Log) and proceed knowing where the risk lives.

What "confirmed" means at each gate is concrete. Tic TOC will explicitly ask: *I am proposing to mark gate /i4 as confirmed. Do you confirm, or do you want to revise?* You can revise. You can ask for elaboration. You can disagree. The gate does not advance on inertia. It advances on your explicit consent.

That is the second thing that makes Tic TOC unlike a chat session. The first is that it pushes back. The second is that *you have to actively agree*, and the prompt remembers what you agreed to.

[^cooper]: Cooper, R. G. (1990). "Stage-Gate Systems: A New Tool for Managing New Products." *Business Horizons*, 33(3), 44–54.

---

## 4. How to deploy Tic TOC — the five-minute setup

The deployment is short. The session is long. Here are the literal mechanical steps to get from "I want to use Tic TOC" to "I have typed /i1 and Tic TOC is waiting for my answer."

**Step 1 — Get the Tic TOC prompt.**

The current Tic TOC prompt lives in `pantry/TikTOC_prompt.md` in this book's project directory, and at Bear Brown & Company's prompt library online [verify URL at time of writing — point to the live prompt library, not a static link]. The file is roughly 600 lines of markdown. Copy the entire contents to your clipboard.

**Step 2 — Create a Claude Project.**

In claude.ai, click *Projects* in the left sidebar, then *Create Project*. Name it something specific — e.g., *Tic TOC — [your book working title]*. The name matters because you will keep this project open across multiple sessions.

**Step 3 — Paste the prompt into Instructions.**

Inside the project, find the *Instructions* field (sometimes labeled *Custom Instructions* or *Project Knowledge* depending on Claude's current UI [verify — interface labels shift; current as of May 2026]). Paste the entire Tic TOC prompt into Instructions. Save.

**Step 4 — Add your domain research brief to Project Knowledge.**

Inside the project, upload or paste your synthesized research brief from Chapter 3 (or, on first read of this book, the brief at `pantry/ai-for-designers-final-brief.md` for the running example). Tic TOC will reference it when it asks domain-specific questions during /i3 and /i4.

**Step 5 — Start a new conversation in the project. Type /help.**

If the prompt is loaded correctly, Tic TOC will respond with a menu of commands. The first entries should be `/i1` or `/intake`, `/i2` or `/booktype`, `/i3` or `/audience`, `/i4` or `/thesis`. The menu also lists the diagnostics (`/g2` or `/critique`) and the open-questions log (`/p2` or `/openlog`).

If you do not see this menu, the prompt is not loaded. Re-paste into Instructions and start a fresh conversation.

**Step 6 — Type /i1.**

Tic TOC will ask its first intake question. The first question is not "what is your book about." It is something like "*Who is the specific person you are writing for? Not the type of reader. The specific person — someone you know, with a face and a job and a problem.*" This is Taba's inductive move, asked at sentence one. You will answer. The session has begun.

Total setup time, including reading the menu: **five minutes**. Total session time: **roughly two hours**, spread across one sitting or two depending on your domain.

---

## 5. What the session feels like — conversation, not form

The most common reason authors abandon Tic TOC in the first twenty minutes is that they expect it to behave like a form-fill. It does not.

Tic TOC asks one question at a time. It waits for an answer that has *content*, not an answer that is *long*. When you give a vague answer, it does not move on. It pushes back. The pushback is not unkind, but it is direct: *"That answer would produce a chapter Cowork could write about any field. Can you make it specific to your reader's actual practice?"*

This is the move the chapter wants you to expect. The session's value is in the pushback. If you answer the first question of /i3 with "my reader is a graphic designer who wants to learn AI" — which is what most authors do — Tic TOC will not let you pass. It will ask you to name a specific person you know who matches that description, what they do for work this week, what they have already tried, and what specifically frustrates them about it. That sequence of follow-up questions is the conversation the session is built around.

You will sometimes disagree with Tic TOC. You should. The prompt is not always right. When it pushes back on a domain-specific claim where your expertise is greater than the prompt's knowledge, you can override. The phrase to use is: *"I am keeping this — here is why, in one sentence."* Tic TOC will accept the override, log the rationale, and proceed.

But — and this is the important asymmetry — *most of the time, when Tic TOC pushes back, the pushback caught something you did not see*. The author who finishes a Tic TOC session in thirty minutes is almost never the author who has the clearest book. It is the author who accepted the first answer at every gate. This is not a productive session. It is a session that produced a *Cowork dump's worth of preparation* in less time than the dump would have taken to produce.

The triage move during the session:

- **Defend** when Tic TOC misunderstands a domain specific. Use the one-sentence override.
- **Accept** when Tic TOC catches a real vagueness. Rewrite the answer.
- **Ask for elaboration** when you cannot tell which of the above is happening. Tic TOC will explain what it was looking for.

You will leave the session tired. Two hours of high-density specification is more cognitively demanding than two hours of writing. Sweller's *Cognitive Load Theory* predicts this — sustained working-memory load is finite, and the act of holding audience, outcomes, sequencing, and chapter content in mind simultaneously is what makes the phase structure necessary in the first place.[^sweller] Take a break between phases. Drink water. The session is dialogue, not deliverable — polished answers are not required and often paper over weak specification.

[^sweller]: Sweller, J. (1988). "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 12(2), 257–285.

---

## Worked example — one phase-gate conversation from the ai-for-designers session

The single most useful piece of texture you can have before running your own Tic TOC session is to see what one phase-gate conversation actually looks like. What follows is an annotated transcript excerpt from the May 2026 ai-for-designers session — the /i3 audience intake gate. The transcript has been lightly cleaned for readability; the substance is unchanged.

> **Tic TOC (/i3):** Who is the specific person you are writing for?
> Not the type of reader. A specific person you know — with a face,
> a job, and a current problem.
>
> **Author:** Freelance graphic designers who want to use AI without
> losing their professional identity.

That is a *type*. Not a *person*. Watch the pushback.

> **Tic TOC:** That is a category. Can you name one designer in that
> category that you actually know — first name only is fine — and
> describe what they were working on this week?

The author paused for thirty seconds before answering.

> **Author:** Okay. Maya. She has been freelance for nine years,
> mostly brand identity work. Her main client is a healthcare
> consultancy. She uses Photoshop and Figma daily, has a paid
> ChatGPT account, and used Midjourney once last month for a
> moodboard. She has been quietly worried for six months that her
> contracts are getting smaller. She has not raised her rates in
> two years because she does not know if AI is making her work
> easier or making her replaceable.

This is what /i3 was looking for. Notice what the answer contains that the first answer did not: a name, a tenure, a specific client type, a specific toolset, a specific incident, a specific worry, and a specific reason the worry has not been acted on. None of that survives in a category. All of it shapes downstream chapter design.

> **Tic TOC:** Good. One more probe. Maya has a paid ChatGPT account
> but only used Midjourney once. Why? Is this a learning curve
> problem, a confidence problem, a billing problem, or a "she hasn't
> needed it yet" problem? The answer matters because it tells me
> whether your book's Chapter 1 needs to be a tool tutorial, a
> permission conversation, a business case, or a defense against the
> fluency trap.

This is the curriculum theorist talking. The pushback is not about Maya's psychology; it is about *what the chapter structure must address* depending on which answer is true.

> **Author:** Confidence. She knows how to prompt. She does not know
> how to disclose AI use to her client without looking like she's
> cheating. So she uses it secretly for moodboards and refuses to
> use it for deliverables.

Now the curriculum theorist has what it needs. Chapter 1 of the ai-for-designers book is not a tool tutorial. It is a permission conversation. The Chapter 5 deliverable (*Disclosure framework* — see the Bloom's table at the top of this chapter) follows directly from this answer. The whole book's emotional center sits in this exchange.

> **Tic TOC:** Confirmed. /i3 gate ready to mark passed. Your reader
> is Maya — nine-year freelance brand designer, one anchor healthcare
> client, paid ChatGPT, hesitant about disclosure. Do you confirm
> this as your primary learner profile, or do you want to revise?
>
> **Author:** Confirm.
>
> **Tic TOC:** Gate /i3 passed. Advancing to /i4 (thesis).

That is one gate. The session has thirteen of them. The /i3 exchange above took the author about twenty minutes. The Maya profile then shows up in Part 2 of the final TIKTOC.md as the *Primary reader* paragraph you read at the top of this chapter. The conversation produced the document. The pushback produced the conversation.

**The reading move:** When you run your own /i3, notice when you give a category and when you give a person. The pushback is most productive when you have just given a category.

---

## Exercises

### Exercise 1 (Apply) — Deploy Tic TOC, confirm /help appears, begin /i1

Follow the five-minute setup in section 4. Confirm that the menu returned by `/help` includes `/i1`, `/i2`, `/i3`, `/i4`, `/l1` through `/l4`, `/c1` through `/c4`, `/g1`, `/g2`, and `/p2`. If any of these are missing, the prompt is not loaded.

Begin `/i1`. Answer the first question. Stop there. The full session is Chapter 4.

**Deliverable:** A screenshot of `/help` returning the command menu, plus a screenshot or paste of your `/i1` first answer.

### Exercise 2 (Analyze) — Identify two phase-gate decisions in the TIKTOC.md excerpt; name Cowork failure modes

Re-read the TIKTOC.md excerpt at the opening of this chapter. Identify *two* specific phase-gate decisions visible in the document. For each:

- Name the gate the decision was made at (likely /i3, /i4, /l1, /l2, or /c1).
- State what the decision was, in one sentence.
- Predict what Cowork would have produced *differently* if the decision had been left vague.

You are doing the reverse engineering Tic TOC performs in real time. The point of the exercise is to develop the *"what would Cowork do with this?"* reading discipline that Chapter 4 will turn into a working skill.

**Deliverable:** A 250–400 word memo, two decisions, with the failure-mode prediction for each.

### Exercise 3 (Evaluate) — Respond to "I don't need Tic TOC"

Write 200 words responding to a colleague who says: *"I don't need Tic TOC — I know what my book is about, and I'd rather just start drafting."*

Your response should make use of:

- The cost-ratio argument from Curtis, Krasner, and Iscoe (1988).
- The specific value of pushback that the colleague cannot give to themselves.
- One example, drawn from your own field or from the ai-for-designers running example, of what the pushback caught.

This is the rehearsal for explaining the AI+1 pipeline to peers, which Chapter 11 expects you to be fluent in.

**Deliverable:** 200-word memo.

---

## Still puzzling

- *Is two hours the right timebox?* It is not empirically derived. Ericsson's deliberate-practice literature supports 60–90 minute focused sessions;[^ericsson] Cirillo's Pomodoro literature supports 25-minute cycles.[^cirillo] Two hours is a defensible composite — long enough for sustained judgment, short enough that a working professional will actually commit. The number is heuristic.
- *Is three disciplines the right partition?* Curriculum theorist, acquisitions pragmatist, instructional designer. Defensible, but not a recognized triad in any field. A practicing acquisitions editor might split their own role into three. The framing is editorial.
- *Does Tic TOC's pushback hold up across Claude versions?* The transcripts in this chapter were captured against Claude as of May 2026. Claude's pushback texture will shift as the underlying model versions update. The structural moves (gates, capability statements, bridge questions) are stable; the *tone* is not.
- *Is the TIKTOC.md schema universal, or Bear Brown-specific?* It is currently Bear Brown / Cowork convention. The underlying instructional-architecture principles (Backward Design, Bloom's, phase-gating) are widely accepted. The specific file format is not standardized across publishers.

[^ericsson]: Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). "The Role of Deliberate Practice in the Acquisition of Expert Performance." *Psychological Review*, 100(3), 363–406.
[^cirillo]: Cirillo, F. (2006/2018). *The Pomodoro Technique*. Currency.

---

## What would change my mind

I would revise the claim that the TIKTOC.md session is the highest-leverage step in the pipeline if a controlled comparison — say, twenty author-instructors split between Tic TOC-first and Cowork-first drafting, holding domain research constant — showed that the Cowork-first cohort produced final drafts of equivalent quality after the human rewrite stage, with comparable total time investment. Such a study does not currently exist. The chapter's confidence rests on the analog with Curtis-Krasner-Iscoe (1988) and on consistent practitioner experience across the small set of authors who have completed both paths. If those analogs break — if downstream rework in textbook drafting turns out *not* to scale like software defect cost — then the two-hour upfront investment loses its arithmetic justification, and the pipeline reorganizes around a different gate.

---

## AI Wayback Machine — Hilda Taba

> **Prompt to run in Claude or ChatGPT:**
>
> "Read the Wikipedia article on Hilda Taba. In 300 words, explain how
> her inductive curriculum model maps onto what Tic TOC's /i1 (audience
> intake) phase tries to enforce — and identify one place where Tic TOC
> departs from Taba's approach."

Taba was an Estonian-American curriculum theorist whose 1962 *Curriculum Development: Theory and Practice* argued for an inductive model that starts from specific student needs and builds upward to general principles. Tic TOC's /i3 question — *who is the specific person?* — is Taba's move at the conversation level. The Wikipedia article is short; the prompt asks you to read it once and write the comparison.

---

## Bridge — Chapter 3

Tic TOC is now deployed. The menu appears when you type `/help`. You have begun `/i1` and answered one question. You have read the ai-for-designers TIKTOC.md and reverse-engineered two of its phase gates. You can defend the two-hour investment to a colleague.

What you do not yet have is the input.

Tic TOC is a forcing function. It only works when you bring it something to push back against. If your `/i1` first answer is "I'm not sure who my reader is," Tic TOC's pushback will hit empty air. The session will stall.

The thing Tic TOC needs is a *domain research brief* — the synthesized output of the three-LLM prompt you saw in Chapter 1, organized into a four-section format that maps cleanly onto Tic TOC's intake questions. That brief is what Chapter 3 walks you through producing.

Chapter 3 is the chapter before the chapter. It is short, mechanical, and indispensable.
