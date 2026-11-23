# agentic-chatbot workflow

Server mode: dedicated

At /architecture, use /server to configure a dedicated target or record local deferral before selecting the database route. The project allocates its own ports, volumes and routes and verifies live delivery at /deploy.

| Command | Mode | Stage | فارسی | Exit or condition |
| --- | --- | --- | --- | --- |
| `/idea` | ai | Suitability and idea | تناسب‌سنجی و هسته ایده | Suitability gate passed; narrow `0.1` domain scoped |
| `/prd` | ai | Agent requirements | نیازمندی و مرزهای ایجنت | Personas, agent role, channels and refusal boundaries resolved |
| `/tools` | ai | Tool inventory and contracts | ابزارها و قراردادهای سرویس | Service classes, attenuated tool contracts and secret keys resolved |
| `/sops` | ai | Standard operating procedures | رویه‌های استاندارد عملیاتی | Multi-step procedures, parameter checks and recovery rules resolved |
| `/data-model` | ai | Data model and memory | مدل داده‌ها و حافظه ایجنت | Domain entities, session memory and redacted audit metadata resolved |
| `/privacy` | ai | Privacy and envelope masking | حریم خصوصی و انولوپ‌ها | `[h_*]` handle masking, audit retention and sink rules resolved |
| `/capabilities` | ai | Capabilities and authority | ماتریس اختیارات و تایید | Per-action owner confirmation policy (`read+none`, `direct+none`, `direct+soft`, `confirm+hard`) resolved |
| `/edge-cases` | ai | Edge cases and safeguards | دفاع امنیتی و موارد استثنا | Injection defense, token/spend quotas and outage fallback resolved |
| `/prompts` | ai | Runtime prompts | پرامپت‌ها و دیالوگ‌های نمونه | Reviewed prompts aligned with capability vocabulary and handles |
| `/architecture` | ai | Architecture and plan | معماری، نقشه و هندآف | Reference monitor, DB route and checklist complete |
| `/build` | tool | Harness implementation | پیاده‌سازی موتور و هارنس | Harness, services and deterministic security/gate tests pass |
| `/wire` | ai | Live model and tool wiring | اتصال به مدل و سرویس واقعی | Real configured model and service round trips verified |
| `/test` | ai | Adversarial and owner test | آزمون خصمانه و پذیرش | Adversarial boundary probes and owner acceptance recorded |
| `/deploy` | ai | Deployment and budget monitoring | استقرار سرور و پایش بودجه | VPS daemon, HTTPS/poller and budget caps verified, or local delivery recorded |

For the initial version follow these stages in order. Read each installed procedure for its inputs, outputs and exit evidence. Review only affected stages and prerequisites during later iterations.

References in `docs/references/`: `authority.md`, `budgets.md`, `infrastructure.md`, `intake.md`, `messenger.md`, `payments.md`, `quality.md`, `services.md`, `workflow.md`.
