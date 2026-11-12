# Agent acceptance criteria

- The owner understands why deterministic bots are insufficient and the extra effort/risk.
- Specs, source, credentials, state and deployment belong to the selected Project.
- Reviewed capabilities match the actual model-visible surface; trusted caller binding,
  handle scope and selected authorization remain effective on every execution path.
- Configurable direct/soft/hard policies reflect the owner's informed choices; observed
  soft behavior is not described as independently enforced hard authorization.
- Per-user and global budgets, run bounds and concurrency gates work across workers
  and restarts. Exhaustion/outage reaches a functional deterministic fallback.
- Runtime prompts and example dialogues are actual deliverables. Owned backends and
  bridges are implemented and their current contracts and live connections are verified.
- Duplicate updates/effects, cancellation, unknown outcomes and restart are recoverable.
- Real provider/messenger behavior, HTTPS/renewal, production DB access and service
  restart have evidence. Missing credentials or live checks remain explicit blockers.
- The owner reviews changed decisions, policy choices, key dialogues and a complete
  final journey. Tests, readiness, deployment and human acceptance are distinct records.
