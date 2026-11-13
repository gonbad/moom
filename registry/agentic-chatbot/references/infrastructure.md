# Runtime identities, budgets and service deployment

Inherit shared SSH/DNS/TLS/proxy facts; allocate Project-specific ports, Compose identity,
volumes and service users without disturbing previous deployments. PostgreSQL/Redis
run on the VPS; native OpenSSH forwarding supports laptop development. Container DB
hosts are service names, host DB addresses are loopback, and laptop addresses are
forwarded loopback ports. Test each from the actual runtime rather than copying URLs.

Deploy agent, owned business backends and bridges together only after each component's
API and state owner are recorded. Their process permissions and credentials differ.
The inference worker has scoped business API access and no coding/deployment shell.
Keep bridge browser profiles/session cookies in restricted ignored storage and verify
restoration after restart. Do not ship development-machine sessions indiscriminately.

For webhook development use a selected loopback reverse SSH tunnel behind the shared
HTTPS route; at cutover drain local runs/events and prove a single production consumer.
Apply forward-proxy access per service when needed; do not expose credential-bearing
URLs in telemetry. Verify actual provider/service connectivity from the service user,
with bounded requests charged to the operational budget.

Before activation back up domain and agent state; test migrations, restart, restored
quota/cooldown/pending-proposal state, and rollback. Check that fallback and deployment
retries cannot bypass selected hard approvals or duplicate a completed effect. Public
HTTPS and health endpoints prove serving, not semantic dialogue quality or settlement.
Keep skipped model/platform checks visible for later owner rehearsal.
