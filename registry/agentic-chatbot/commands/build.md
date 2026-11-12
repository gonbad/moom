# Build all owned components

Implement the reviewed design under SOURCE/app and SOURCE/services as appropriate,
using compatible pinned Pydantic AI/FastAPI dependencies or the reviewed equivalent.
Keep trusted transport/caller context separate from model output. Generate only the
allowed tools; apply handle checks, normal business validation and selected approvals
at trusted execution boundaries. Implement all owned backends/bridges and current
contracts. Enforce atomic budgets, concurrency/run bounds, deduplication/outbox and
model-free fallback in code, not just prompts.

Use a separate test database. Attempt structural authority bypass and quota/concurrency
failures while building; verify scoped history, errors and restart recovery. Preserve
real integration blockers for wire. Record actual checklist/test evidence without
claiming model conversations were exercised before inference is configured.
