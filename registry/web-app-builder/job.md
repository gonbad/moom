# web-app-builder

Build independent web products from reviewed requirements and approved external designs, then test and deploy them with HTTPS.

Job revision: 0.4

This is an adaptable initial base. Change any step, format or style to fit the
participant’s exact work, including while doing a real Project. No fixed schema,
orientation, toolkit or bundled runtime limits the result. Start with the real idea.

## Suggested ordered full pipeline

| Step | Persian label | Command | Condition |
| --- | --- | --- | --- |
| Idea and competitors | هسته ایده و رقبا | [job-idea](commands/job-idea.md) | Adapt to actual needs |
| Product requirements | نیازمندی و پرسونای کاربر | [job-prd](commands/job-prd.md) | Adapt to actual needs |
| Conceptual data model | مدل داده‌های مفهومی | [job-data-model](commands/job-data-model.md) | Adapt to actual needs |
| User experience and flows | تجربه کاربری و صفحات | [job-ux](commands/job-ux.md) | Adapt to actual needs |
| Visual design and system | طراحی بصری و استایل | [job-design](commands/job-design.md) | Adapt to actual needs |
| Interactive prototype | پیش‌نمایش فرانت‌اند | [job-prototype](commands/job-prototype.md) | Adapt to actual needs |
| Acceptance scenarios and edge cases | سناریوهای آزمون و لبه‌ها | [job-scenarios](commands/job-scenarios.md) | Adapt to actual needs |
| Technical plan and architecture | معماری، نقشه و هندآف | [job-plan](commands/job-plan.md) | Adapt to actual needs |
| Build and implementation | ساخت و اتصال بک‌اند | [job-build](commands/job-build.md) | Adapt to actual needs |
| Human acceptance testing | آزمون پذیرش و بازبینی | [job-test](commands/job-test.md) | Adapt to actual needs |
| Production deployment | استقرار روی سرور | [job-deploy](commands/job-deploy.md) | Local delivery may skip hosting |

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
external styling in design; 1:1 direct HTML-to-React component transcription with
bundled Tailwind in prototype; comprehensive acceptance scenarios and edge cases in
scenarios; strongest-model blueprinting in plan; backend implementation in build;
side-by-side visual and functional verification in test; and production HTTPS delivery
in deploy.
