# Product journeys and matched visual evidence

Derive tests from the PRD's user actions, not component implementation details.
At minimum cover one end-to-end success, empty data, validation failure, unavailable
backend, unauthenticated access and cross-user resource denial. Verify pagination/
filtering and refresh/deep links where applicable. Test at the intended phone width,
keyboard-only input, visible focus, labels and RTL mixed-script content.

Compare approved HTML and the integrated product using matching viewport/data/state.
A build passing does not excuse a changed layout. Record evidence alongside the
source revision and reviewed design. Remove preview CDNs and inspect production
requests for missing assets, secrets and dev endpoints. Contract tests exercise the
real HTTP/schema boundary; migrations and rollback tests use isolated data.

Before delivery run the production build, affected tests and actual user journeys.
Verify deployment from the real runtime identity: HTTPS, routing, database access,
service restart, backup restoration and a rollback. State which checks were skipped
or unavailable. Keep owner acceptance and live release evidence separate from local
browser success; do not force a test suite that simply mirrors trivial code.
