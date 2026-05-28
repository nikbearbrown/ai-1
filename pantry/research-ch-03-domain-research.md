# Research: Chapter 03 — Domain Research: The Chapter Before the Chapter
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students write, run, and synthesize a structured domain research prompt across three LLMs, producing a brief ready for the Tic TOC intake session.
**Research date:** 2026-05-28

---

## 1. Primary Sources

### Foundational papers and texts

- **Denzin, N. K. (1978). *The Research Act: A Theoretical Introduction to Sociological Methods* (2nd ed.).** McGraw-Hill.
  The foundational text on methodological triangulation. Denzin identifies four types of triangulation: data, investigator, theoretical, and methodological. The three-LLM domain research prompt is a form of investigator triangulation applied to AI tools — treating each LLM as a different "investigator" with different training data, reinforcement signals, and known failure modes, then looking for convergence and divergence. This is the academic frame that elevates "ask three chatbots the same question" from prompt-engineering trick to legitimate methodology.

- **Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). "Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing."** *ACM Computing Surveys*, 55(9), Article 195.
  The most-cited prompt-engineering survey at the time of writing. Establishes the taxonomy of prompting strategies (cloze, prefix, structured, few-shot) and documents the brittleness of prompts across model families. This is the citation that justifies the chapter's framing of prompts as documented, reusable artifacts rather than disposable inputs — and that justifies cross-model evaluation because the same prompt produces measurably different outputs across model families.

- **Surowiecki, J. (2004). *The Wisdom of Crowds*.** Doubleday.
  The popular-but-rigorous treatment of why aggregation of independent estimates outperforms expert individuals under specified conditions: diversity of opinion, independence, decentralization, and aggregation. The three-LLM pattern works to the extent that LLMs from different vendors satisfy diversity and (rough) independence. The chapter should be honest that this is *approximate* — three frontier LLMs trained on overlapping internet data are not as independent as three randomly sampled human estimators.

- **Anthropic. (2024–2025). "Claude prompting guide" and Anthropic Research blog posts on constitutional AI and Claude's training.** Anthropic.
  Documents Claude's training philosophy (Constitutional AI, RLHF with safety-trained preference models) and how it shapes output style. Use for the chapter's "what each LLM does differently" content block. Anthropic's emphasis on cautious, nuanced reasoning produces a recognizable Claude signature — long-form analysis with explicit uncertainty markers — distinct from GPT's tendency toward confident enumeration.

- **OpenAI. (2023–2025). Model cards and system card documents for GPT-4, GPT-4o, GPT-5.** OpenAI.
  Documents GPT's training methodology and known capability profile. Use comparatively with Anthropic and Google sources for the "three LLMs do different things" content block.

- **Google DeepMind. (2024–2025). Gemini technical reports and model cards.** Google DeepMind.
  Same purpose — Gemini's training, capability profile, and known signature. Gemini's multimodal-first training and tighter integration with Google Search produce a distinctive output profile (more retrieval-grounded, sometimes less stylistically fluent).

### Key empirical cases

- **Adobe Firefly launch (March 2023) and Generative Fill integration in Photoshop (May 2023).** Adobe MAX 2023 keynote; investor relations materials. The single most documented case of generative AI shipping inside a design professional's primary tool. The chapter's worked example (domain research brief for ai-for-designers) will report this case as one of the field's three or four pivot events.

- **Midjourney v4 → v5 → v6 release sequence (Nov 2022 – Dec 2023).** Documented on Midjourney's own announcements and across design press. Midjourney's rapid quality jumps redefined what "AI-generated image" meant for working designers in the 18 months following ChatGPT.

- **Figma Config 2024 launch of Figma AI (June 2024).** Figma product blog and Config 2024 keynote. Brought generative AI into the dominant UI/UX design tool for collaborative workflows. The combination of Firefly + Figma AI is the empirical "the field has changed" case.

- **Canva Magic Studio (October 2023).** Canva product announcements and trade press. Pushed generative AI into the small-business-design market — relevant to the running example because Canva is the primary competition for the freelance designer's lower-end clients.

- **The Anthropic / OpenAI / Google Gemini "model rotation" practitioner pattern (2023–2026).** Documented across practitioner blogs (Simon Willison, Ethan Mollick, Anthropic Cookbook, OpenAI Cookbook). The convention of running the same prompt across multiple frontier models for synthesis emerged in this community. There is no canonical academic source; cite as practitioner convention.

---

## 2. The Core Concept — State of the Field

### What is settled

- LLMs from different vendors produce measurably different outputs on identical prompts. This is documented in the prompting survey literature (Liu et al. 2023; subsequent benchmarking work).
- Triangulation across sources improves reliability of synthesis under specified conditions (Denzin 1978; subsequent qualitative research methodology).
- Frontier LLMs have distinctive "signatures" recognizable to experienced practitioners — Claude's nuance, GPT's enumeration, Gemini's retrieval-grounding. Settled at the level of practitioner experience; less rigorously documented in peer-reviewed work.
- Domain research must come before instructional architecture. This is settled in instructional design literature (Wiggins & McTighe; Dick, Carey & Carey *The Systematic Design of Instruction*).

### What is disputed

- **How independent the three frontier LLMs actually are.** They share massive overlap in training data (Common Crawl, books, code). True statistical independence does not hold. The wisdom-of-crowds claim must be qualified.
- **Whether "three LLMs" is the right number.** Two may be sufficient; four may be diminishing returns. The chapter's choice of three is heuristic — defensible but not derived from research.
- **Whether LLMs can do domain research at all.** Critics argue LLMs report what they were trained on, not the current state of a field — so for fast-moving fields (which generative AI in design certainly is), the LLM is a stale lagging indicator. The chapter must acknowledge this and address it via the synthesis step (where the author's domain expertise catches stale claims).

### What has changed recently (last 5 years)

- 2020–2022: Cross-model evaluation was a benchmarking activity for ML researchers. Practitioners typically used one model.
- 2022–2023: ChatGPT's dominance made single-model use the default. Claude 1 was niche; Gemini did not yet exist as a frontier consumer product.
- 2023–2024: Claude 2 and Claude 3 (March 2024) became practitioner-competitive with GPT-4. Gemini 1.5 (Feb 2024) brought Google into the frontier. The three-LLM rotation became a practical option.
- 2024–2025: Open-source frontier models (Llama 3, DeepSeek, Qwen) added a fourth lane that some practitioners now include. The chapter could mention but should not require — the workflow is fragile enough at three.
- 2025–2026: Tools like OpenRouter and Claude Code's multi-model orchestration made cross-model prompting tractable from a single interface. The friction cost has fallen.

---

## 3. Application Domain Examples

For graphic design / freelance design profession (the running domain):

- **The Adobe Firefly + Photoshop Generative Fill case.** A designer running the three-LLM prompt asking "what has changed in the graphic design profession in the last three years?" will get convergent reports about Firefly and Generative Fill across all three models — this is settled territory. Documented.
- **The Midjourney moodboarding workflow.** Documented across design Twitter/X, Reddit r/graphic_design, and trade press (CreativeBloq, It's Nice That) starting late 2022. The three LLMs will converge on the existence of this workflow but diverge on its evaluation — some will report it as a productivity win, others as a craft-erosion threat. The divergence is the value.
- **Figma AI and the UX/UI design subfield.** A designer running the prompt for the UX subspecialty will see this come up consistently. The chapter's worked example can show divergence on whether Figma AI is "augmentation" or "replacement of junior designers."
- **The Canva Magic Studio + small-business client erosion case.** A designer running the prompt for the freelance practitioner subspecialty will find LLMs reporting this differently — Claude is more likely to acknowledge the threat to lower-end design work; GPT may frame it as opportunity; Gemini may surface specific Canva product announcements. Illustrative of why the multi-LLM run matters.
- **The "AI-generated logos on Fiverr" race-to-the-bottom case.** Documented in design industry press (Print Magazine, Eye on Design). A lower-end design service tier has been transformed by AI generation. The three LLMs will report this differently — and the synthesis is the designer's own evaluation. Illustrative.

---

## 4. The Book's Thesis Connection

The book's thesis: **the TIKTOC.md session is the highest-leverage step.** Chapter 3's contribution is specific and load-bearing: **the TIKTOC.md session can only be high-leverage if its inputs are high-quality.** A vague domain research brief produces a vague Tic TOC session produces a vague TIKTOC.md produces a Cowork dump. Garbage in, fluency trap out.

Chapter 3 is therefore the chapter that protects the thesis from a specific failure mode: an author-instructor who completes a Tic TOC session with thin domain knowledge will get a TIKTOC.md that *passes* Tic TOC's gates (because Tic TOC tests internal consistency, not domain accuracy) but produces a textbook detached from the actual current state of the field.

Chapter 3's specific contributions to the thesis:

1. **It defines "ready for /i1."** The chapter ends with a four-section format that is exactly the input Tic TOC expects. This is the spec-for-the-spec — the document the TIKTOC.md session works from. Without it, the session is conversation without anchor.

2. **It teaches LLM literacy in a low-stakes context.** Before the high-stakes TIKTOC.md session, the reader practices reading LLM output critically — catching the fluency trap at the research stage, where errors are recoverable. This is rehearsal for Chapter 4.

3. **It establishes triangulation as a discipline.** The reader learns to mark each claim as "ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY." This labeling discipline carries forward into Chapter 6 (pantry evaluation) and Chapter 8 (rewrite gate-checking). Chapter 3 plants the methodological habit.

4. **It introduces the "fluency trap check" as a recurring move.** The fluency trap was named in Chapter 1 as a phenomenon. Here it becomes a verb — the author *runs* a fluency trap check on the research output. By Chapter 10, the author runs a fluency trap check on the pedagogy. The chapter is the first operationalization.

5. **It produces the Create-level deliverable that feeds Chapter 4.** Per the TIKTOC.md's Bloom's table, Chapter 3 is one of three Create-level chapters (along with Ch 4 and Ch 8). The deliverable is real — the author leaves Chapter 3 with a document, not a feeling.

---

## 5. The AI Wayback Machine — Candidate Figures

- **Paula Scher.** Wikipedia page title: "Paula Scher." Pentagram partner; designer of the Citi logo, the NYC Public Theater identity system, Microsoft's corporate identity. Scher's career is a fifty-year argument for graphic design as cultural research before it is visual production — she famously talks about research, immersion, and "knowing the territory" before designing. She is the embodied case for what Chapter 3 teaches: research is the chapter before the chapter. Strong candidate; female, working at the heart of contemporary American design. *Example prompt:* "Read the Wikipedia article on Paula Scher. Identify one project where her research into a domain (a city, a publisher, a museum) shaped the visual identity in a way no quick brief could have produced. Explain how this maps onto the chapter's argument that domain research must precede design."

- **Massimo Vignelli.** Wikipedia page title: "Massimo Vignelli." Italian designer; created the NYC Subway signage system, American Airlines identity, Bloomingdale's. Vignelli was outspoken about the discipline of research and constraint as the foundation of design — "the life of a designer is a life of fight." Non-American (Italian-born, worked globally), male. Provides non-Anglo representation. *Example prompt:* "Read the Wikipedia article on Massimo Vignelli. Summarize his philosophy of design as a research-first discipline. Identify one constraint he embraced that produced a design decision an AI tool would not have arrived at."

- **Donald A. Norman.** Wikipedia page title: "Don Norman." Cognitive scientist, author of *The Design of Everyday Things* (1988, revised 2013), co-founder of the Nielsen Norman Group, former Apple VP. Norman is the canonical figure for "research the user before you design for them" — affordances, conceptual models, user-centered design. Strong candidate for the methodology side of Chapter 3 (rather than the design-craft side). American, male, anglophone — does not contribute to diversity. *Example prompt:* "Read the Wikipedia article on Don Norman. Explain how his concept of 'conceptual model' applies to what Chapter 3 calls a 'domain research brief.'"

- **Bruno Munari.** Wikipedia page title: "Bruno Munari." Italian designer, artist, and design theorist; author of *Design as Art* (1966). Munari treated research and play as foundational to design — the title of his book is the argument. Non-Anglo (Italian), male. Optional fourth candidate if non-Western representation is a higher priority elsewhere in the book.

**Diversity assessment:** Scher provides gender diversity; Vignelli and Munari provide non-Anglo (European) representation. None of the candidates is non-Western. **For the book overall, Chapter 3 is a natural place to insert a non-Western figure** — possibilities include Kenya Hara (Japanese designer, art director for Muji, author of *White* and *Designing Design*) or Ikko Tanaka. Recommendation: Paula Scher as primary candidate; flag for the author to consider Kenya Hara as an alternative if non-Western representation across the book is thin.

---

## 6. Pedagogical Delivery Research

**Prior knowledge required:** Familiarity with using one LLM (per the TIKTOC.md learner profile, basic Claude or ChatGPT use). The reader does not need to have used multiple LLMs before. The chapter must walk through the friction of opening three browser tabs or installing OpenRouter without making it sound technical.

**Common misconceptions in the target reader (solo author-instructor / graphic designer):**

1. "One LLM is enough." This is the dominant practitioner default. The chapter must overcome it without making three-LLM rotation sound dogmatic. The argument: three LLMs catch the fluency trap *between* them in ways one LLM cannot self-catch.
2. "The LLMs will give me the same answer." Many readers have not run the same prompt across multiple frontier models. The chapter's opening — three LLM responses to the same prompt side by side — is the move that breaks this misconception.
3. "I should trust the longest, most detailed answer." Length is not accuracy. The chapter must teach the reader to read for *evidence and specificity*, not for prose volume.
4. "Domain research is what I already know — I'm the expert." The expert has tacit knowledge; the brief externalizes it for Tic TOC's consumption. The chapter must distinguish what's in the designer's head from what's in a document Tic TOC can read.

**Instructional sequences that work:**

- **Same prompt, three answers.** The chapter's specified opening — three LLM responses to the same domain research prompt side by side — is the right move. It produces the "oh" moment instantly.
- **Convergence-then-divergence reading.** Teach the reader to read agreement first (settled territory), then divergence (contested territory), then gaps (what no LLM mentioned that the expert knows). This is the analytic move that produces a useful synthesis.
- **The template first, the customization second.** Provide the eight-section prompt template, then teach adaptation. Reverse order (teach principles, ask reader to construct) produces non-comparable outputs and undermines the triangulation argument.

**Teaching failure modes:**

- Treating one LLM as authoritative. If the chapter implies Claude is "right" and GPT is "wrong," readers will reduce to one-LLM workflow with their preferred model. The chapter must hold the three models as complementary.
- Making the synthesis sound like averaging. It is not — it is reading three differently-biased reports and using domain expertise to triage. Averaging would lose the expert judgment that is the whole point.
- Making the fluency trap check sound like fact-checking. It is broader — it is checking for plausible-sounding claims that fail expert review, not just verifiable errors.

**What makes understanding vs. memorization:** A reader who has memorized can run three prompts and produce a synthesis document. A reader who understands can look at a synthesis document and predict which claims will turn out to be wrong — and explain why. The "fluency trap check" exercise is the operationalized comprehension.

---

## 7. Representation and Display Research

**Required display:** A three-column comparison table showing the same domain research prompt run across Claude, GPT, and Gemini, with corresponding sections side by side. This is the chapter's load-bearing figure — without it, the "three LLMs do different things" argument is abstract.

**Format suggestion:** Three columns (Claude / GPT / Gemini), with rows for each of the eight prompt sections (e.g., "AI tools disrupting the field," "Wage premium evidence," "Skills shifting"). Highlight cells where the three converge (green or "AGREE"), diverge (yellow or "DIVERGENT"), or where only one LLM raises a point (orange or "ONE ONLY"). This is exactly the labeling system the chapter teaches.

**Source material:** The actual three-LLM output for ai-for-designers — must be produced from a real run, not invented (per TIKTOC.md Open Question #1, the running example is the highest-priority production constraint). The pantry already contains `ai-for-designers-research-prompt.md` and `ai-for-designers-final-brief.md` — these should be the source for the figure.

**Required display 2:** A four-section brief template (the deliverable). Show it twice: once as a blank template, once filled in for ai-for-designers. The reader needs to see both — the form and the worked example.

**Optional display:** A simple flow diagram showing prompt → three LLMs → three outputs → synthesis → four-section brief → /i1. This connects the chapter to Chapter 4 visually.

---

## 8. Open Questions and Research Gaps

- **The three-LLM pattern lacks academic validation.** There is no peer-reviewed study showing three-LLM rotation produces better domain research than single-LLM use with verification. The chapter must present it as defensible practitioner convention, not as proven methodology.
- **The eight-section prompt structure is editorial.** Likely a Bear Brown / Cowork convention. The chapter should be transparent about provenance.
- **LLM signatures are temporally unstable.** Claude in 2024 had a different output profile than Claude in 2026. The chapter's claims about what each LLM "does" must be flagged as current-state. Aging risk: high.
- **The disruption case studies (Firefly, Midjourney, Figma AI, Canva) are 2023–2024 vintage.** By 2027 the specific tools and versions will have changed. Cite year of data; flag as current-state. Pipe to "online prompt library" or equivalent for current versions.
- **Open-source frontier models (Llama 3, DeepSeek) are not in the three-LLM rotation as specified.** The chapter should acknowledge this and explain why three frontier commercial models is the recommended default for non-technical authors, while flagging that practitioners with infrastructure can add a fourth.
- **The "wisdom of crowds" application to LLMs is approximate.** Surowiecki's conditions (diversity, independence, decentralization, aggregation) hold weakly. The chapter should be honest about this without abandoning the framing.

---

## 9. Sourcing Notes

- **Denzin 1978:** Out of print in original; widely reproduced in subsequent qualitative methods texts. Cite Denzin's original work; reference subsequent treatments (e.g., Patton's *Qualitative Research & Evaluation Methods*) for accessibility.
- **Liu et al. 2023 prompting survey:** Open access via arXiv (preprint) and ACM Digital Library. No paywall.
- **Surowiecki 2004:** Popular trade book; widely available. The relevant material is in the first three chapters; quotation is straightforward.
- **Anthropic / OpenAI / Google Gemini documentation:** Public via each company's developer documentation, model cards, and research blogs. Cite specific posts with retrieval dates because these documents are revised.
- **Adobe Firefly launch dates:** Adobe press releases (March 2023, May 2023). Cross-reference Adobe's own product timelines because trade press dates sometimes differ.
- **Midjourney version timeline:** Midjourney's announcement Discord and product blog. Trade press summaries are useful but inconsistent on exact dates.
- **Figma AI launch:** Figma Config 2024 keynote (June 2024). Figma product blog is the primary source.
- **Canva Magic Studio:** Canva product announcement October 2023.
- **Fact-checking priority for this chapter:** All product-launch dates (Firefly, Midjourney v5/v6, Figma AI, Canva Magic Studio). These will be quoted in the worked example and must be exact.
- **AI Wayback figures:** Paula Scher's Wikipedia article is robust. Vignelli's is comprehensive. Don Norman's is extensive. Kenya Hara's English-language Wikipedia article is shorter — verify depth before recommending.
- **Existing pantry artifacts:** `ai-for-designers-research-prompt.md` and `ai-for-designers-final-brief.md` exist in pantry already — these are primary sources for the chapter's worked example and should be reviewed during drafting to ensure the chapter explains what the artifacts demonstrate.
