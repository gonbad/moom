# Use model-directed actions only where they add value

Compare a deterministic bot or ordinary web app first. An agent is useful for variable
intent, choosing among scoped tools or composing information; it adds model cost,
latency, semantic mistakes and a larger review surface. Explain these tradeoffs before
settling on it. The serving model must never inherit the coding assistant's shell,
filesystem, credentials or deployment permissions.

Retain the workshop specification work inside short steps: idea/suitability; PRD and
scenarios; contracts (capabilities, SOPs, data, privacy, tools, prompts and edge cases);
build; real provider/service wiring; boundary and dialogue testing; deployment.
Project living files include `prd.md`, `tools.md`, `policies.md`, `data-model.md`,
`prompts.md`, `services.md`, `budgets.md`, `connections.md` and `status.md` as needed.
Do not require a chat UI for a scheduled task; its trusted run principal and bounded
job context replace fictional conversations.

Specify tool-visible authority separately from service implementation. Build each
owned backend/bridge as a usable service and connect through reviewed APIs. Keep
question rounds small, then review the whole action surface and its failure behavior.
For a later version identify changed policies, tools, data and prompts and invalidate
only affected evidence. A model dialogue, structural security test and live service
round trip establish different things; never count a scripted fixture as an AI rehearsal.
