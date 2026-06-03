# Research: Chapter 13 — Canvas Course Export: .imscc
## AI+1: AI Native Personalized Textbooks

**Chapter one-line:** Students compile their book's markdown source into a Canvas-importable .imscc package — using the same source that produced the Kindle book, no Canvas API access required.
**Research date:** 2026-06-02

---

## 1. Chapter Summary from TIKTOC.md

**Opening:** The professor uploads one file. Settings → Import Course Content → Choose File. A complete course appears in Canvas: modules, pages, assignments, the syllabus. The chapter works backward from that moment to explain what the file contains and how the build script produced it.

**Core content blocks:**
1. What .imscc is and why one file upload builds the course — the ZIP structure; imsmanifest.xml as the course index; how Canvas reads it; the two files that signal Canvas-flavored vs. standard CC (`course_settings/syllabus.html` and `course_settings/course_settings.xml`)
2. What the Blueprint already produced that maps to Canvas — learning objectives → module learning outcomes; TIKTOC.md chapters → module sequence; assessment philosophy → assignment specs; compliance layer → syllabus.html content
3. `build-imscc-standard.py` — the pure Python path; what it reads (chapters/*.md, metadata.yaml, TIKTOC.md); what it produces (modules, pages, assignment shells, discussion shells, the manifest); one command, no dependencies beyond the standard library
4. `build-imscc-canvas.rb` — the Canvas-optimized path; what the canvas_cc gem adds (rubric criteria, quiz shells, outcome alignments, module completion requirements); Ruby install sidebar (optional path only); when it is worth the extra step
5. After the import — the diff review; what Canvas builds from the spec vs. what needs human correction; the correction conversation with Blueprint; what publish_allowed: false means and when the professor says "publish it"

**Worked example:** ai-for-designers .imscc imported into Canvas — module list shown, one module opened, assignment spec visible, syllabus.html rendered. Diff between Blueprint spec and Canvas build annotated.

---

## 2. Primary Sources and References

**Instructure Canvas Instructor Guide: Import content from Common Cartridge.** This is the authoritative current UI source for the reader-facing workflow. Canvas imports Common Cartridge ZIP or IMSCC files from Course Settings → Import Course Content → Common Cartridge 1.x Package → Choose File, with options for all content/specific content, question banks, New Quizzes conversion, date adjustment, and import queue status. Source: https://community.instructure.com/en/kb/articles/660732-how-do-i-import-content-from-common-cartridge-into-canvas

**Instructure Canvas Instructor Guide: Export a Canvas course.** Canvas exports courses as IMSCC ZIP files and notes that student interactions and grades are not included. The file can be imported back into Canvas and can be treated as a ZIP by changing the extension. Source: https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-export-a-Canvas-course/ta-p/785

**1EdTech Common Cartridge specification.** Common Cartridge 1.3 is a stable specification; the manifest version must refer to 1.3.0, resource and assessment metadata can use LOM, LTI links and additional resource types are supported, and multiple question banks are allowed. Source: 1EdTech Common Cartridge page (https://www.imsglobal.org/cc/index.html). Common Cartridge 1.4 implementation guide also clarifies resource categories and web content resources. Source: https://www.imsglobal.org/node/167531

**Canvas REST API content export and migration docs.** Chapter 13 claims the standard path requires no API, but an advanced sidebar can note that Canvas API supports Common Cartridge export/import through content exports/migrations. Useful for distinguishing "professor upload path" from "admin automation path." Source: Canvas Content Exports API summary (https://bcourses.berkeley.edu/doc/api/content_exports.html); Canvas Content Migrations API summary (https://www.canvas.instructure.com/doc/api/content_migrations.html).

**canvas_cc Ruby gem.** Instructure-authored Ruby gem for building Canvas Common Cartridge-compatible files. The RubyDoc README says the gem lets authors build Canvas objects without hand-writing XML and then create an `.imscc` file. Source: RubyDoc README (https://www.rubydoc.info/gems/canvas_cc/0.0.23). RubyGems page shows latest version 0.0.43, released August 22, 2019, with dependencies including nokogiri, rubyzip, builder, thor, happymapper, and rdiscount. Source: https://rubygems.org/gems/canvas_cc

**Local library cross-reference: `_lib_Humanitarians_AI_Course_Template.md`.** Relevant for module/assignment/course-template language; not a Common Cartridge technical source.

**Local library cross-reference: `_lib_tic-toc-v2.md`.** Relevant for the mapping from learning outcomes and assessment logic into course modules.

---

## 3. Conceptual Foundations

### Concept 1: `.imscc` is a course package, not a Canvas API call

An `.imscc` file is a ZIP-like Common Cartridge package. Canvas can import it through the normal instructor interface. This is the chapter's most important practical reassurance: the professor does not need Canvas admin rights, API tokens, or IgniteAI access to test the standard path.

**Common misconception:** "Canvas deployment requires an API integration." Correct version: API access is useful for automation, but Common Cartridge import is a file-upload workflow available in ordinary Canvas course settings.

**Worked example:** The reader runs `build-imscc-standard.py`, receives `ai-for-designers.imscc`, enters Canvas, opens Settings, chooses Import Course Content, selects Common Cartridge 1.x Package, uploads the file, and waits for the import queue.

**Source(s):** Instructure import guide (https://community.instructure.com/en/kb/articles/660732-how-do-i-import-content-from-common-cartridge-into-canvas).

### Concept 2: `imsmanifest.xml` is the course index

The manifest is the file that tells the LMS what resources exist and how they are organized. It points to pages, assignments, discussions, files, assessment resources, and metadata. In the AI+1 standard path, the manifest should be generated from the same source materials that produced the book: `chapters/*.md`, `metadata.yaml`, and `TIKTOC.md`.

**Common misconception:** The package is just a folder of HTML pages. Correct version: the pages matter, but the manifest is what makes the package a course rather than a loose website.

**Worked example:** Rename `.imscc` to `.zip`, inspect it, confirm `imsmanifest.xml` exists at package root, then verify that the manifest references module/page resources generated from chapter files.

**Source(s):** 1EdTech Common Cartridge spec (https://www.imsglobal.org/cc/index.html); 1EdTech CC 1.4 implementation guide (https://www.imsglobal.org/node/167531).

### Concept 3: Standard Common Cartridge and Canvas-flavored Common Cartridge differ

The pure Python path should produce a conservative, standard Common Cartridge: pages, modules, assignment shells, discussions, and a manifest. A Canvas-flavored path can include Canvas-specific course settings, syllabus files, rubrics, quiz shells, module completion requirements, and outcome alignments, often through Canvas-specific XML structures or tooling such as `canvas_cc`.

**Common misconception:** More Canvas-specific features always make a better cartridge. Correct version: the standard path is more portable and less fragile; the Canvas-optimized path is richer but more dependent on Canvas behavior and Ruby/gem maintenance.

**Worked example:** Build both packages. Standard package imports with modules and pages. Canvas-optimized package imports with richer assignment/rubric structures. The chapter asks whether the extra features justify the maintenance burden.

**Source(s):** canvas_cc RubyDoc (https://www.rubydoc.info/gems/canvas_cc/0.0.23); RubyGems metadata (https://rubygems.org/gems/canvas_cc).

### Concept 4: The TIKTOC already contains the course map

The TIKTOC chapter list becomes Canvas modules. Learning outcomes become module outcomes or page learning objectives. Exercises become assignment shells. Dig Deeper and LLM exercises become pages, discussions, or assignments. The build script is a compiler from instructional architecture to LMS structure.

**Common misconception:** Canvas conversion is a separate instructional design task. Correct version: if TIKTOC was done properly, Canvas conversion is largely a mapping task plus post-import review.

**Worked example:** Chapter 11's exercises become an assignment shell named "Figure SCOPE Pass"; Chapter 13's exercises become "Build and Import IMSCC" and "Canvas Diff Review."

**Source(s):** TIKTOC.md; `_lib_tic-toc-v2.md`; `_lib_Humanitarians_AI_Course_Template.md`.

### Concept 5: Import is not publication

Canvas import creates draft course structure. It does not guarantee pedagogical correctness, visual polish, date alignment, accessibility, or publication status. The post-import diff review is the human gate: compare Blueprint/TIKTOC spec against the actual imported course and correct mismatches before publishing.

**Common misconception:** "The import worked" means "the course is ready." Correct version: import success means the structure exists; the professor still needs to review modules, links, assignments, syllabus, due dates, accessibility, and publish state.

**Worked example:** After import, the professor lists three exact matches and two human corrections. Corrections feed back into Blueprint or the build script so the next package improves.

**Source(s):** Canvas import guide import status and content-selection behavior (https://community.instructure.com/en/kb/articles/660732-how-do-i-import-content-from-common-cartridge-into-canvas).

---

## 4. Domain Examples and Cases

### Case 1: ai-for-designers package upload

The worked example should be a real `ai-for-designers.imscc` imported into a Canvas sandbox. Required screenshots/artifacts: import settings screen, import queue completion, module list, one opened module, one assignment shell, syllabus page, and a diff note showing what matched the Blueprint spec and what did not.

### Case 2: Pressbooks-to-Canvas Common Cartridge

Pressbooks and university help desks routinely teach Common Cartridge export/import as a way to move book/course content into Canvas. This supports the chapter's practical claim that the standard is an ordinary courseware workflow, not exotic infrastructure. Example source: UW-Madison Pressbooks/Canvas import guidance (https://kb.wisc.edu/helpdesk/84559).

### Case 3: Canvas export as backup

Canvas itself exports courses as IMSCC ZIP files, which reinforces the reader's mental model: the file is a portable course snapshot, not a live LMS integration. Source: Instructure export guide (https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-export-a-Canvas-course/ta-p/785).

### Failure case: Treating Common Cartridge as SCORM

Common Cartridge packages course structure and content for LMS import. SCORM is aimed at trackable e-learning objects and runtime communication. A reader who expects SCORM-style interaction tracking from a Common Cartridge page will be disappointed. Chapter 13 should say: this package builds the course shell and content; it does not create a SCORM runtime.

---

## 5. Connections and Dependencies

**Prerequisites:**
- Chapter 4: TIKTOC produces the instructional map.
- Chapter 5: scaffold creates chapter files and repository structure.
- Chapter 10: enrichment creates AI+1 exercises that can become Canvas activities.
- Chapter 11: figures must have accessible static artifacts.
- Chapter 12: build logic and rebuild loop are already familiar.

**Unlocks:**
- A single-source publishing model: chapters become EPUB/PDF and Canvas course.
- Versioned course updates: corrections to markdown rebuild both book and `.imscc`.
- Workshop deployment: Humanitarians AI and similar programs can import a ready course shell quickly.

**Adjacent chapter connections:**
- Chapter 12 ships the book through Kindle/PDF. Chapter 13 ships the same source as a course.
- Appendix 90 should document the standard Python path and Common Cartridge structure.
- Appendix 91 should document the Canvas-optimized path, Ruby setup, and `canvas_cc` features/limits.

---

## 6. Current State of the Field

**Settled:**
- Canvas supports importing Common Cartridge ZIP/IMSCC files via course settings. Source: Instructure import guide (https://community.instructure.com/en/kb/articles/660732-how-do-i-import-content-from-common-cartridge-into-canvas).
- Common Cartridge is a mature 1EdTech standard; CC 1.3 was finalized in 2013, and 1EdTech continues to maintain later guidance. Source: 1EdTech (https://www.imsglobal.org/cc/index.html).
- Canvas exports are IMSCC ZIP files and do not include student interactions/grades. Source: Instructure export guide (https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-export-a-Canvas-course/ta-p/785).

**Contested or implementation-dependent:**
- How well non-Canvas LMS platforms preserve Canvas-specific features is variable.
- Whether to target standard Common Cartridge or Canvas-specific enrichment depends on the course's portability needs.
- New Quizzes conversion, question banks, rubrics, outcomes, and LTI links can drift across Canvas versions and institutional settings.

**Recent changes to acknowledge:**
- Canvas UI paths are mostly stable but screenshots and option wording drift.
- Canvas's quiz ecosystem continues to distinguish Classic Quizzes and New Quizzes; imports may offer conversion options.
- AI-generated course materials make validation more important: instructors need to diff imported course content against the source spec rather than trusting generated shells.

---

## 7. Teaching Considerations

Students get stuck on the invisible structure of the file. They can see pages and modules after import, but they cannot see why `imsmanifest.xml` mattered. The chapter should have them unzip the package before importing it.

Effective analogy: "An `.imscc` is a moving box with a packing list. The files are the objects; `imsmanifest.xml` is the packing list Canvas uses to rebuild the room."

Best exercises:
1. Inspect the package: rename `.imscc` to `.zip`, open it, find `imsmanifest.xml`, and identify three resources.
2. Import into Canvas: use Common Cartridge 1.x Package, all content, and observe import status.
3. Diff review: compare module names, page titles, assignment shells, syllabus text, links, and publish state against the Blueprint.
4. Correction loop: record the exact prompt or spec change that would prevent one mismatch in the next build.

---

## 8. Open Questions and Production Risks

- The standard Python script must be written and tested before drafting. TIKTOC explicitly says Chapter 13 cannot be drafted authentically until the script runs and imports.
- The Canvas-optimized Ruby path depends on `canvas_cc`, whose latest RubyGems release is old (0.0.43, August 22, 2019). The chapter should present it as optional and test it against the current Canvas instance before recommending it.
- The two claimed Canvas-flavored trigger files, `course_settings/syllabus.html` and `course_settings/course_settings.xml`, must be verified against a real import before publication.
- The worked example requires a real Canvas sandbox import. A mock screenshot would violate the book's artifact-authenticity rule.
- Canvas import behavior varies by institution: New Quizzes settings, external tools, LTI availability, file-size limits, and course-navigation defaults can differ.

---

## 9. Search Queries Used

- Canvas LMS import Common Cartridge IMSCC package documentation Settings Import Course Content Canvas
- IMS Common Cartridge specification imsmanifest resources organizations assessment items LTI 1.3
- Instructure Canvas Common Cartridge export import course_settings syllabus.html course_settings.xml imsmanifest
- canvas_cc Ruby gem Common Cartridge Canvas course export documentation
- Canvas LMS export course IMSCC Common Cartridge instructor guide
- Common Cartridge imsmanifest organizations resources webcontent assessment item specification

