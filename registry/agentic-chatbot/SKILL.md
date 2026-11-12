---
name: agentic-chatbot
description: Build an advanced conversational agent with model-selected tools, caller-scoped capabilities, configurable confirmations and enforced usage budgets. Use only when a deterministic bot is inadequate; this workflow requires more review and carries greater operational risk.
license: MIT
metadata:
  version: "0.1.0"
  author: gonbad
  origin: https://github.com/gonbad/moom
---

# Agentic chatbot builder

First check whether a deterministic bot or web app can meet the actual need. This job
adds autonomous tool selection and substantially more specification, verification and
operating work. Explain the increased injection, authority and usage-cost risks before
choosing it. The owner selects action policies after receiving those explanations.

Read [Project ownership](references/project.md), then [the workflow](references/workflow.md).
1. [start](commands/start.md): suitability, actual input and early VPS identity.
2. [infra](commands/infra.md): server Compose and native development tunnels.
3. [idea-core](commands/idea-core.md): V0.1 concept and existing-product inventory.
4. [prd](commands/prd.md): scoped outcomes and acceptance journeys.
5. [tools](commands/tools.md): services, owned backends/bridges and contracts.
6. [sops](commands/sops.md): concrete dialogues, operations and fallback menus.
7. [data-model](commands/data-model.md): agent/domain state boundaries and PostgreSQL.
8. [privacy](commands/privacy.md): sensitive data, handles, recipients and retention.
9. [capabilities](commands/capabilities.md): caller binding and owner-selected action policies.
10. [edge-cases](commands/edge-cases.md): abuse, outage, concurrency and recovery behavior.
11. [prompts](commands/prompts.md): actual versioned runtime prompts and examples.
12. [plan](commands/plan.md): architecture, budgets, components and verification handoff.
13. [build](commands/build.md): complete agent and owned services with automated checks.
14. [wire](commands/wire.md): real provider, transport and account-session verification.
15. [test](commands/test.md): complete conversations and structural authority/budget checks.
16. [deploy](commands/deploy.md): HTTPS service, webhook handoff and restart evidence.

Use [infrastructure](references/infrastructure.md) for infra/deploy,
[authority](references/authority.md) for capabilities/build/test,
[budget controls](references/budgets.md) for plan/build/test, and
[service boundaries](references/services.md) for tools/plan/wire.
Read [messengers](references/messenger.md) and [payments](references/payments.md)
when applicable. Apply [quality criteria](references/quality.md) throughout.
Use scripts/smoke.py for isolated Moom setup verification, not live-agent certification.
