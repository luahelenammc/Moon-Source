# Conversation-native Visual Explanation — Moon Source applied design guide

**Purpose:** help an AI choose and compose a visually didactic answer when the user needs to **understand** an idea, situation, relationship, comparison or process, not necessarily to operate a tool. The response is the illustration. Interaction is an optional extension, not its organizing center.

**Status:** public applied design guide within Moon Source's existing architecture. It is not a seventeenth registered capability, a standalone portable, an HTML framework, a renderer, an image-generation engine or evidence of universal platform support. The [AI Kernel](../MOON_SOURCE_AI_KERNEL.md) routes to this guide when useful. [Operational Devices](OPERATIONAL_DEVICES.md) owns real executable device contracts; [Moon Source Language](../portables/msl/MOON_SOURCE_LANGUAGE.md) governs proportional document/packet form; [Adaptive Orchestration](../portables/adaptive-orchestration/ADAPTIVE_ORCHESTRATION_PROTOCOL.md) governs execution surfaces. None of these responsibilities becomes a new runtime merely because the reply is illustrated.

## The primary decision: what should become easier to see?

Do not start with "Which widget can I build?" or "How can I put this into HTML?" Start with the user's **cognitive task**: what needs to be understood, distinguished, situated, remembered or acted upon? Select the lightest form that makes the essential relationship perceptible.

A user asking for "HTML in GPT-6", "visual", "illustrate it" or "make it more beautiful" may want a visually composed response **inside the conversation**, not HTML source, a hosted web page, a dashboard, an interactive checklist or an exported image. Resolve the intended medium from the request and context; ask only when an essential ambiguity remains. No magic phrase is required.

### Visual-form selection

| What needs to become clear? | First visual candidate | What to avoid |
|---|---|---|
| Two or more options | Parallel labeled comparisons, small aligned cards or a compact table | A full product dashboard for a short contrast |
| Sequence or procedure | Illustrated step flow, timeline, arrows or connected stages | A fake application with unused navigation |
| Causes and dependencies | Directed diagram, dependency chain or layered flow | Decorative arrows that imply invented causality |
| A conceptual structure | Nested/adjacent groups, taxonomy or layered architecture | Boxes that reproduce headings without adding relationships |
| A qualitative situation | Short icon-guided sections, semantic grouping and a restrained key | Invented numerical scoring or severity badges |
| Numbers and distribution | Clearly labeled chart, proportion, comparison or annotated statistic | Unlabeled axes, misleading scales or fabricated precision |
| Priorities and trade-offs | Visual matrix, side-by-side consequences or clearly distinguished conditions | Ranking that silently turns opinions into objective scores |
| Warning, exception or uncertainty | Targeted visual cue and concise contextual note | Coloring all conclusions as alerts or hiding caveats in small print |

These are choices, not mandatory layouts. A strong paragraph can still be the most effective explanation. Do not turn an ordinary answer into a display cabinet of cards merely because a visual surface is available.

## Didactic illustration grammar

**Semantic fidelity comes first.** Resolve the content's actual categories, dependencies, distinctions and uncertainty before choosing colors or shapes. A layout is wrong when it imposes a relationship the source did not support.

**Editorial hierarchy:** give the main point perceptual priority, then the supporting relationship, then necessary details, then caveats. The eye should know where to go. Avoid overlong headings, tiny type, scattered emphasis and repeated titles.

**Color with meaning:** use a controlled palette to distinguish categories, phases, emphasis or a genuinely meaningful status. Do not rely on color alone. Green does not automatically mean approved; red does not turn an assumption into a verified risk. Match contrast to both light and dark themes when applicable.

**Icons with a job:** choose recognizable, consistent icons to label concepts or help navigation, not to wallpaper paragraphs. Ensure the icon's meaning agrees with the text; avoid implying a medical, legal, security or political status through iconography without basis.

**Composition and whitespace:** group related facts, align comparable quantities, let diagrams breathe, keep card count proportional and preserve responsive/mobile reading order. Beautiful is not synonymous with maximal density, decorative framing, artificial gradients or heavy borders.

**Text + visuals:** the important facts remain present as accessible text or clear labels. A diagram should clarify a relationship, not conceal the only explanation. Diagrams, labels and callouts must be consistent with the accompanying prose.

**Visual truth:** show provenance, units, dates and uncertainties when material; avoid fabricated statistics, precise percentages without evidence, decorative charts and pseudo-scientific visual authority. When evidence is provisional or locally unapproved, make that distinction visible.

## Composition patterns that teach rather than decorate

- **Explain a process:** use 3–6 differentiated stages, each with a short action label and a note explaining its condition or purpose. A connected visual relation is better than five unrelated identical cards.
- **Teach a difficult concept:** pair a short definition with a precise analogy or schematic; show what each visual element corresponds to and where the analogy stops.
- **Explain a decision:** lay out alternatives with comparable criteria, then show the reason for the current recommendation and the condition that would change it. Do not manufacture probabilities.
- **Reconstruct an institutional flow:** show who receives, assesses, authorizes, acts and records, preserving authority and exception routes. Do not portray a proposal as an approved workflow.
- **Summarize a report:** one dominant insight, a few thematically distinct visual clusters and grounded evidence. Tables belong where exact details matter; diagrams belong where relationships matter.

### Anti-patterns and correction

**Negative: HTML literalism.** The model hears "HTML in GPT-6" and emits an entire site-like layout with hero, tabs, package listings, pseudo-product sections and navigation. **Correction:** if the task is to explain existing material, compose a didactic answer inside Chat. Full HTML/CSS/JS is warranted only when the user actually requests an app, independently executable artifact, exact HTML output, or a composition whose richer treatment materially helps.

**Negative: ornamental interaction.** Checkboxes, progress bars, selectors and quizzes make a static explanation look operable without improving comprehension. **Correction:** remove controls; show relationships using typography, color, icons, clear grouping and visual sequencing.

**Negative: pseudo-dashboard inflation.** Everything becomes a card and every card looks equally important. **Correction:** start from the explanatory hierarchy, use fewer visual objects with distinct roles, and keep the narrative visible.

**Negative: pretty but misleading.** Smooth graphs, precise-looking ranks or a confident illustration conceal uncertainty, unverified facts or missing inputs. **Correction:** validate source and mapping first; label hypotheses and conditions in the same visual field.

**Negative: purely cosmetic styling.** The answer receives colors and icons but no clearer model of the subject. **Correction:** each visual choice must help contrast, orient, group, sequence, signal uncertainty or recall something essential. Otherwise remove it.

## Interaction is a conditional second layer

When the person truly needs to **operate** on an explanation, retain the validated interactive operations: change inputs, select items, compare consequences, sequence work, evaluate understanding, replan the unfinished portion. A visual explanation may include a small interaction if it deepens understanding, for example changing one assumption to reveal its effect on a diagram. It need not become an application.

Interaction has its own acceptance checks: genuine behavior, clear inputs, valid calculations, feedback, reversible local state where useful, accessible controls and authorization boundaries. For a repeated operational device, follow the [Operational Devices contract](OPERATIONAL_DEVICES.md#public-device-contract). Local state does not prove durable storage or authorize third-party mutations.

## Choosing the right materialization

1. **Plain prose:** no visual structure when concise text explains better.
2. **Visually composed answer in Chat:** the default for a didactic visualization request in a capable conversational client. Native composition can combine text, icons, labeled groups, charts and diagrams with restrained color.
3. **Visual explanation with microinteraction:** only when altering a variable, toggling a perspective or advancing a step teaches or decides something.
4. **Interactive tool:** when the main task is input, calculation, selection, completion or recurring operation.
5. **Standalone HTML/app/site:** when independent execution, source code, portability, editing or persistent distribution is actually requested or required.
6. **Generated image:** when the desired result is a rendered image, illustration, photograph, poster or diagram image artifact; use a suitable native image-generation facility for image creation rather than pretending HTML or simple plotted shapes are equivalent.
7. **Specialized domain format:** map, spreadsheet, document, slide deck or 3D renderer when geography, formulas, publication layout or spatial interaction are essential. Do not force every medium into an HTML-shaped reply.

A visual response that the client renders inline and a downloadable HTML document are distinct outcomes. In some compatible surfaces, embedded HTML/JavaScript can also run in a message; this does not mean every large composition, arbitrary script or complete HTML file will render inside every chat. Prove the relevant surface before promising parity.

## Preflight and acceptance

**Preflight (proportional, often silent):** identify the user's actual intent, the source facts, the relationship worth illustrating, the best visual morphology and the minimal degree of interaction. When "HTML" is used loosely, resolve whether the person means visual response, an embedded interactive application or a file. The preference shown by a user-selected positive/negative example should override generic dashboard styling when within the task's constraints.

**Visual-first acceptance:**
1. **Faithfulness:** the graphic preserves the source's relationships, categories, units and epistemic limits.
2. **Explanatory gain:** the reader understands something faster, more accurately or more intuitively than through unstructured text alone.
3. **Visual craft:** purposeful iconography, legible hierarchy, pleasing but functional contrast, grouping, spacing and restrained color semantics.
4. **Didactic flow:** the sequence of attention matches how the subject should be learned or decided.
5. **Portability and accessibility:** meaningful text fallback, adequate labels and mobile ordering; no core meaning encoded only in color.
6. **Honest scope:** visually rich answers do not claim to be products, completed actions, real-time dashboards, image outputs or persistent records.
7. **Interaction correctness, if applicable:** controls work, dependent outcomes update, and state/action boundaries remain explicit.

**Progressive rendering check:** validate one illustrated block, then a small composition, then larger layouts if needed. For interactive elements, separately verify native control, state selection, embedded app when supported and composed behavior. A valid script or standalone HTML browser test is not proof of Chat rendering. If a large composition fails, reduce it to a minimal reproducer rather than assuming the platform lacks visuals or HTML entirely.

**Success condition:** the output is first a better explanation. Interactivity is successful only when it adds the *next* useful operation.

## Example request without a magic template

> Explain [subject] visually inside this chat. Prioritize a didactic illustration with purposeful icons, color, hierarchy and clear relationships, not a mini-site, a dashboard or gratuitous controls. Preserve facts and uncertainties. Add interaction only when changing something makes the explanation genuinely better.

When intent is already clear, the model should make this choice without requiring the user to recite a formula.

## Evidence and provenance

- [OpenAI · Intelligent UI in ChatGPT](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt): describes matching layout, visuals and interactivity to the user's question; examples include graphics, comparisons, diagrams and interactive experiences. Product-specific availability is time-sensitive.
- [OpenAI · GPT-6 and Intelligent UI](https://openai.com/index/gpt-6-for-everyone/): source announcement and product context.
- [Operational Devices](OPERATIONAL_DEVICES.md) retains the subordinate interactive instrument/device distinction. The current guide reclassifies the **primary** user need as didactic illustration rather than mini-tool construction.
- Community lineage: u/Professional-Rest138, r/PromptEngineering, supplied excerpt dated 2026-10-18, suggested ten interactive task examples; u/Educational-View8524 suggested replan-after-progress. This is credited as an inspiration for the subordinate interaction branch, not as the origin or proof of Intelligent UI's visual-explanation capability.
- The 2026-10-21 visual-first correction follows a user's comparison of attractive, didactic visual explanations against a superfluous checklist and an overbuilt page-like response. These examples calibrate design intent; they do not constitute a formal platform benchmark or permission to disclose private project data.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
