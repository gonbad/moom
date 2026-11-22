# web-app-builder workflow

Server mode: dedicated

At /architecture, use /server to configure a dedicated target or record local deferral before selecting the database route. The project allocates its own ports, volumes and routes and verifies live delivery at /deploy.

| Command | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- |
| `/idea` | Idea and competitors | هسته ایده و رقبا | MVP slice, differentiator and service fallbacks resolved |
| `/prd` | Product requirements | نیازمندی و پرسونای کاربر | Personas, capabilities and non-goals resolved |
| `/data-model` | Conceptual data model | مدل داده‌های مفهومی | Plain business entities, invariants and relationships resolved |
| `/ux` | User experience and flows | تجربه کاربری و صفحات | Screen inventory, empty/error states and key screen resolved |
| `/visuals` | Visual design and system | طراحی بصری و استایل | Return bundle imported; owner selected visual direction |
| `/prototype` | Interactive prototype | پیش‌نمایش فرانت‌اند | HTML-to-React visual comparison accepted; local Tailwind verified |
| `/scenarios` | Acceptance scenarios and edge cases | سناریوهای آزمون و لبه‌ها | Synthetic scenarios and edge cases walked on prototype |
| `/architecture` | Technical plan and architecture | معماری، نقشه و هندآف | DB route, API seam mapping and build checklist complete |
| `/build` | Build and implementation | ساخت و اتصال بک‌اند | Migrations, APIs, wired UI and automated tests pass |
| `/test` | Human acceptance testing | آزمون پذیرش و بازبینی | Prototype-to-app comparison and owner scenario acceptance recorded |
| `/deploy` | Production deployment | استقرار روی سرور | Live HTTPS/DB restart verified, or local delivery recorded |

For the initial version follow these stages in order. Read each installed procedure for its inputs, outputs and exit evidence. Review only affected stages and prerequisites during later iterations.

References in `docs/references/`: `design.md`, `infrastructure.md`, `intake.md`, `quality.md`, `workflow.md`.
