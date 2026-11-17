# web-app-builder

Build independent web products from reviewed requirements and approved external designs, then test and deploy them with HTTPS.

Job revision: 0.5

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea and competitors | هسته ایده و رقبا | [idea](commands/idea.md) | Adapt to actual needs |
| Product requirements | نیازمندی و پرسونای کاربر | [prd](commands/prd.md) | Adapt to actual needs |
| Conceptual data model | مدل داده‌های مفهومی | [data-model](commands/data-model.md) | Adapt to actual needs |
| User experience and flows | تجربه کاربری و صفحات | [ux](commands/ux.md) | Adapt to actual needs |
| Visual design and system | طراحی بصری و استایل | [visuals](commands/visuals.md) | Adapt to actual needs |
| Interactive prototype | پیش‌نمایش فرانت‌اند | [prototype](commands/prototype.md) | Adapt to actual needs |
| Acceptance scenarios and edge cases | سناریوهای آزمون و لبه‌ها | [scenarios](commands/scenarios.md) | Adapt to actual needs |
| Technical plan and architecture | معماری، نقشه و هندآف | [architecture](commands/architecture.md) | Adapt to actual needs |
| Build and implementation | ساخت و اتصال بک‌اند | [build](commands/build.md) | Adapt to actual needs |
| Human acceptance testing | آزمون پذیرش و بازبینی | [test](commands/test.md) | Adapt to actual needs |
| Production deployment | استقرار روی سرور | [deploy](commands/deploy.md) | Local delivery may skip hosting |

For version 0.1 follow the chosen full pipeline. Later versions use only affected
steps and prerequisites, recording skipped steps and reasons. Every command resolves
workspace-root paths, applies file review/certainty, checks the four mutable domains
and ends with dynamic localized progress plus one exact next action.

## References to install and read when relevant

- [workflow](references/workflow.md): Read for state, review and every step handoff.
- [design](references/design.md): Read for external design and prototype fidelity.
- [infrastructure](references/infrastructure.md): Read when connecting services or deploying.
- [quality](references/quality.md): Read when defining acceptance, testing and delivering.

## Retained workshop work

The pipeline preserves the complete separation of concerns: idea core and competitor
advantage in idea; rich user personas in PRD; conceptual things and relationships in
data-model (no SQL); screen inventory, key screen and theme in UX; Tailwind-prompted
external styling in visuals; 1:1 direct HTML-to-React component transcription with
bundled Tailwind in prototype; comprehensive acceptance scenarios and edge cases in
scenarios; strongest-model blueprinting in architecture; backend implementation in build;
side-by-side visual and functional verification in test; and production HTTPS delivery
in deploy.

## Infrastructure intake

`/architecture` owns initial server intake, before selecting the database/runtime
route. Offer reuse of an identified existing target, a new Project-specific server or
local deferral using the infrastructure Constitution. Earlier steps need no server
question. Resume the saved Project selection on later commands; `/deploy` verifies
that selected target and its authorization, never inferring it from another Project.
