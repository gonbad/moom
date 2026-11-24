---
name: prd
description: Author bot requirements, command lists, user personas and interaction rules.
---

# /prd

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`.

Gate: `docs/living/idea.md` exists and has a closed review. Author `docs/living/prd.md`:
1. **User Personas:** Detailed profiles for actors (visitor, customer, administrator,
   support operator), their mobile messenger habits, language preferences and expected
   turnaround times.
2. **Commands & Menu System:** Supported slash commands (`/start`, `/help`, `/cancel`,
   `/status`), persistent reply keyboards, inline action buttons and back/home navigation.
3. **Operational Policies:** Notification triggers, administrative rules, session timeout
   windows, support/operator handoff, and whether payments apply to this version.
4. **Non-Goals:** Capabilities explicitly excluded from this version.

Resolve open questions via `docs/versions/VERSION/NN-analysis-prd.md` in
Obsidian; once review closes, hand off to `/flow`.
