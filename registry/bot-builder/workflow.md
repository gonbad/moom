# bot-builder workflow

Server mode: dedicated

At /architecture, use /server to configure a dedicated target or record local deferral before selecting the database route. The project allocates its own ports, volumes and routes and verifies live delivery at /deploy.

| Command | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- |
| `/idea` | Idea and platforms | هسته ایده و پلتفرم‌ها | Core journey, target platforms and payment applicability resolved |
| `/prd` | Bot requirements | نیازمندی و پرسونای کاربر | Personas, slash/menu commands and non-goals resolved |
| `/flow` | FSM and conversation flow | حالات، منوها و جریان FSM | FSM transition table, keyboards and message templates resolved |
| `/data-model` | Data model and persistence | مدل داده‌ها و نشست‌ها | User, session, domain and optional payment entities resolved |
| `/integrations` | Integrations and payments | پیام‌رسان‌ها و درگاه‌ها | Selected platform adapters, token variable names and conditional payment policy resolved |
| `/edge-cases` | Edge cases and resilience | موارد استثنا و تاب‌آوری | Deduplication, stale callbacks, unexpected inputs and expiry resolved |
| `/scenarios` | Acceptance scenarios | سناریوهای آزمون تعاملی | Turn-by-turn synthetic scenarios and failure cases specified |
| `/architecture` | Architecture and plan | معماری، نقشه و هندآف | DB route, adapter interfaces and build checklist complete |
| `/build` | Engine implementation | پیاده‌سازی ربات و موتور FSM | Engine, adapters and local simulated harness tests pass |
| `/test` | Live messenger rehearsal | آزمون زنده در پیام‌رسان | Live messenger rehearsal and owner acceptance recorded |
| `/deploy` | Deployment and webhook | استقرار سرور و وب‌هوک | Production webhook/poller and restart verified, or local delivery recorded |

For the initial version follow these stages in order. Read each installed procedure for its inputs, outputs and exit evidence. Review only affected stages and prerequisites during later iterations.

References in `docs/references/`: `fsm.md`, `infrastructure.md`, `intake.md`, `messenger.md`, `payments.md`, `quality.md`, `workflow.md`.
