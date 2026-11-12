# Deploy and hand off bot delivery

Read the infrastructure contract. Confirm target authorization and current verification.
Deploy all owned components with retained volumes, migrations and backup. Use the
container service URLs or host-process URLs appropriate to the actual runtime; prove
DB/cache access there. Drain/stop local consumption and repoint the public HTTPS proxy
from the reverse tunnel to the production app port without changing handler logic.

Register/inspect the selected platform endpoints and validate webhook authentication,
real receive/send/callback/payment paths, duplicate-update safety, trusted TLS/renewal,
restart, logs and recovery. For supported polling, use one consumer and the same
normalized dispatcher in both environments. Record deployed revision, redacted evidence,
URL, operating/backup instructions and remaining limitations in VERSION/deployment.md
and LIVING/status.md. Do not mark unavailable integrations as working.
