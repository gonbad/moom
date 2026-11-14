---
name: kandoo-add-idea
description: Bank a spontaneous idea into the active Project, shared Kandoo or both roadmaps without disrupting work.
---

# /kandoo-add-idea

Read `AGENTS.md`, all of `docs/constitution/`, `docs/kandoo/living/profile.md`,
`docs/kandoo/living/server.md`, `docs/kandoo/living/status.md` and
`docs/kandoo/living/job.md`. Resolve paths from the workspace root; require configured
state. This floating utility banks ideas into `roadmap.md` during any active stage
without changing the active Project, current step or pending review.

Receive the idea directly from chat (or the command argument). Determine the target
scope from the idea and current Project context:
1. **Active Project:** A feature, scenario or improvement specific to the current
   output. Bank it in `docs/projects/ID/living/roadmap.md`.
2. **Kandoo / Reusable Method:** A reusable step, template rule, starter adaptation or
   shared infrastructure improvement. Bank it in `docs/kandoo/living/roadmap.md`.
3. **Both:** An idea that affects both the active Project's output and the reusable
   Job or shared Kandoo. Create two linked items with distinct scope—the Project-specific
   part in `docs/projects/ID/living/roadmap.md` and the reusable part in
   `docs/kandoo/living/roadmap.md`—cross-referencing each other so ownership never
   conflicts.

When the scope is already clear from the participant's phrasing, classify and record it
directly without unnecessary questioning. Ask one concise question in chat **only when
scope is genuinely ambiguous**, using the conversation language from `profile.md` (for
example: "Does this idea apply to the active Project, the reusable Kandoo method, or
both?" / «آیا این ایده مربوط به همین پروژهٔ جاری است، متد و ساختار کندو، یا هر دو؟»).

Assess value, differentiation and external dependencies in one brief note. Create or
update the target Markdown roadmap file(s) inside `docs/` using the document language
from `profile.md`, marking the entry ready for future selection (`Ready to select` /
`آماده انتخاب`). Banking an idea is **not** authorization to implement, version or
publish it now. Do not alter code, specifications or stage states. End with what was
banked, the preserved active Project progress block in the conversation language, and
the exact unchanged next action from `docs/kandoo/living/status.md`.
