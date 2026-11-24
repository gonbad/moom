---
name: ux
description: Define screens, empty/error states, user flows, theme keywords and primary key screen.
---

# /ux

Read the project constitution and current status. Use the following references from `docs/references/`: `design.md`, `workflow.md`.

Gate: `docs/living/data-model.md` exists and has a closed review. Author `docs/living/ux.md`:
1. **Screens Inventory:** Name every screen explicitly (reused across design, prototype
   and scenarios), stating its content plus its **loading**, **empty** and **error** states.
2. **Primary Key Screen:** Identify the single screen that best expresses the product's
   value; `/visuals` will explore three distinct directions on this screen first.
3. **User Flows:** Step-by-step paths for each persona goal, including back navigation
   and cancellation.
4. **Theme & Viewport:** 3–4 tone keywords, mobile-first vs desktop viewport, RTL/LTR
   typography expectations and light/dark preference.

If walking screens reveals missing fields or PRD gaps, update `data-model.md` and
`prd.md` in place and note the change. Resolve open questions via
`docs/versions/VERSION/NN-analysis-ux.md` in Obsidian; once review closes, hand
off to `/visuals`.
