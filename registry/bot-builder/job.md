# bot-builder

Build deterministic Telegram, Bale or Rubika menu/button/dialog bots, with optional narrow AI helpers and owner-selected payment policies.

Job revision: 0.2

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea | ایده | [job-idea](commands/job-idea.md) | Adapt to actual needs |
| Requirements | نیازمندی | [job-prd](commands/job-prd.md) | Adapt to actual needs |
| Dialogs, state and data | گفتگو، وضعیت و داده | [job-flow](commands/job-flow.md) | Adapt to actual needs |
| Build | ساخت | [job-build](commands/job-build.md) | Adapt to actual needs |
| Test and live round trips | آزمون و رفت‌وبرگشت واقعی | [job-test](commands/job-test.md) | Adapt to actual needs |
| Deploy | استقرار | [job-deploy](commands/job-deploy.md) | Local delivery may skip hosting |

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

Keep the full scenario, state/data, platform, payment, build, live-test and recovery
work under the short commands. The flow table and adapter fixtures are deliverables,
not optional prose summaries of an unimplemented messenger integration.
