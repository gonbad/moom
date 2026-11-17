# bot-builder

Build deterministic Telegram, Bale or Rubika menu/button/dialog bots, with optional narrow AI helpers and owner-selected payment policies.

Job revision: 0.5

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea and platforms | هسته ایده و پلتفرم‌ها | [idea](commands/idea.md) | Adapt to actual needs |
| Bot requirements | نیازمندی و پرسونای کاربر | [prd](commands/prd.md) | Adapt to actual needs |
| FSM and conversation flow | حالات، منوها و جریان FSM | [flow](commands/flow.md) | Adapt to actual needs |
| Data model and persistence | مدل داده‌ها و نشست‌ها | [data-model](commands/data-model.md) | Adapt to actual needs |
| Integrations and payments | پیام‌رسان‌ها و درگاه‌ها | [integrations](commands/integrations.md) | Adapt to actual needs |
| Edge cases and resilience | موارد استثنا و تاب‌آوری | [edge-cases](commands/edge-cases.md) | Adapt to actual needs |
| Acceptance scenarios | سناریوهای آزمون تعاملی | [scenarios](commands/scenarios.md) | Adapt to actual needs |
| Architecture and plan | معماری، نقشه و هندآف | [architecture](commands/architecture.md) | Adapt to actual needs |
| Engine implementation | پیاده‌سازی ربات و موتور FSM | [build](commands/build.md) | Adapt to actual needs |
| Live messenger rehearsal | آزمون زنده در پیام‌رسان | [test](commands/test.md) | Adapt to actual needs |
| Deployment and webhook | استقرار سرور و وب‌هوک | [deploy](commands/deploy.md) | Local delivery may skip hosting |

For version 0.1 follow the chosen full pipeline. Later versions use only affected
steps and prerequisites, recording skipped steps and reasons. Every command resolves
workspace-root paths, applies file review/certainty, checks the four mutable domains
and ends with dynamic localized progress plus one exact next action.

## References to install and read when relevant

- [workflow](references/workflow.md): Read for state, review and every step handoff.
- [fsm](references/fsm.md): Read for dialog state design and implementation.
- [messenger](references/messenger.md): Read for each selected platform/integration.
- [payments](references/payments.md): Read only when payments are included.
- [infrastructure](references/infrastructure.md): Read when connecting services or deploying.
- [quality](references/quality.md): Read when defining acceptance, testing and delivering.

## Retained workshop work

The pipeline preserves the architecture of deterministic messenger applications:
idea core and platform targeting in idea; rich user personas in PRD; formal state
transition tables, button hierarchies and message templates in flow; persistent user
identities and session storage in data-model; Telegram/Bale/Rubika adapter normalization
and payment lifecycles in integrations; stale callbacks and transport resilience in
edge-cases; interactive turn sequences in scenarios; blueprinting on the strongest model
in plan; FSM engine and mock test harness in build; real messenger rehearsals with test
tokens in test; and production HTTPS webhooks or managed pollers in deploy.

## Infrastructure intake

`/architecture` owns initial server intake, before selecting the database/runtime
route. Offer reuse of an identified existing target, a new Project-specific server or
local deferral using the infrastructure Constitution. Earlier steps need no server
question. Resume the saved Project selection on later commands; `/deploy` verifies
that selected target and its authorization, never inferring it from another Project.
