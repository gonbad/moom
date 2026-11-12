---
name: bot-builder
description: Build a deterministic Telegram, Bale or Rubika bot driven by menus, buttons and explicit dialog state, with optional narrow AI helpers. Use for transactional messenger workflows without an autonomous agent loop.
license: MIT
metadata:
  version: "0.1.0"
  author: gonbad
  origin: https://github.com/gonbad/moom
---

# Messenger bot builder

Read the [Project contract](references/project.md) and [workflow](references/workflow.md).
Core code chooses actions and state transitions. Optional AI may classify input or
answer a bounded question; it receives no autonomous tool loop or broad execution.
Choose agentic-chatbot in a separate Kandoo only if this simpler model cannot fit.

1. [start](commands/start.md): actual bot idea, platform credentials and early VPS access.
2. [infra](commands/infra.md): Project-owned Compose, TLS and native webhook tunneling.
3. [idea-core](commands/idea-core.md): V0.1 premise and optional existing product.
4. [prd](commands/prd.md): user outcomes, permissions and acceptance journeys.
5. [flow](commands/flow.md): menus, dialog paths and failure behavior.
6. [data-model](commands/data-model.md): PostgreSQL state, inbox/outbox and payment records.
7. [fsm](commands/fsm.md): a bespoke transactional state machine for the reviewed flow.
8. [messenger](commands/messenger.md): normalized Telegram/Bale/Rubika adapters.
9. [payments](commands/payments.md): native Bale payments and strict/optimistic receipt review.
10. [build](commands/build.md): handlers, dispatch, integrations and optional narrow AI.
11. [test](commands/test.md): dialog, concurrency, retry and owner verification.
12. [deploy](commands/deploy.md): production handoff, webhooks, TLS and restart checks.

Read [infrastructure](references/infrastructure.md) for infra/deploy,
[messenger contracts](references/messenger.md) for transport,
[FSM](references/fsm.md) for state, and [payments](references/payments.md) when needed.
Apply [quality criteria](references/quality.md). Use scripts/smoke.py for Moom setup;
it checks local Project mechanics and does not certify live platform integrations.
