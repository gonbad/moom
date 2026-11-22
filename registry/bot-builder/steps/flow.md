---
name: flow
description: Design deterministic FSM states, menu hierarchies, transitions and message templates.
---

# /flow

Read the project constitution and current status. Use the following references from `docs/references/`: `fsm.md`, `workflow.md`.

Gate: `docs/living/prd.md` exists and has a closed review. Author `docs/living/flow.md` (always named `flow.md`):
1. **FSM State Transition Table:** Complete tabular mapping of every state (`idle`,
   domain draft states, confirmation, and conditional payment states only when payments
   are in scope), expected input (command, text, reply button, opaque callback token,
   contact or media), guard/validation rule, transactional mutation, outgoing reply and
   next state.
2. **Keyboards & Navigation:** Persistent reply keyboards, inline button layouts, and
   universal escape actions (`«انصراف»` / `/cancel`, `«بازگشت»`, `«منوی اصلی»`).
3. **Message Templates:** Verbatim text for greetings, prompts, validation errors,
   confirmations and help messages, written in natural Persian/chosen language suited to
   the persona.

Resolve open questions via `docs/versions/VERSION/NN-questions.md` in
Obsidian; once review closes, hand off to `/data-model`.
