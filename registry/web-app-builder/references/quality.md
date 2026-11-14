# Product journeys, synthetic test data and matched visual evidence

Derive acceptance scenarios and automated tests from user goals in `prd.md` and `ux.md`,
using **synthetic test identities and isolated test credentials**—never real personal
phone numbers, real customer records or live passwords. Cover end-to-end happy paths,
admin/operator flows, multi-actor state reflection, empty states, validation errors,
upstream service timeouts/503s, double-submit idempotency, unauthenticated access,
cross-user resource denial and session expiry recovery.

## Concrete scenario mini-example

- **Scenario S-03 (Double-tap booking with synthetic user):** Precondition: synthetic
  account `09000000011` signed in; slot `SL-104` has capacity `1`. Action: rapid
  double-click on «ثبت نوبت» at mobile width `390px`. Expected: button enters loading
  state immediately, exactly one reservation row is committed in backend transaction,
  second request returns idempotent confirmation without duplicate charge or 500 error,
  and screen transitions to confirmation state matching `design-system.md`.

Keep the **two visual comparisons** separate in `docs/projects/ID/versions/VERSION/`:
1. **HTML vs React Prototype (`job-prototype`):** Verified at matching viewports, fonts
   and empty/error/filled states before freezing `project/ID/prototype/VERSION`.
2. **Frozen Prototype vs Integrated App (`job-test`):** Verified side-by-side by running
   the frozen prototype copy on a free port alongside the full-stack app, confirming
   layout parity and zero runtime CDN requests (`cdn.tailwindcss.com` absent).

Contract and migration tests run against isolated test data. Before production sign-off,
verify HTTPS, routing, PostgreSQL persistence across `docker compose restart`, backup
restoration and rollback from the real runtime identity—stating any deferred checks
explicitly and never printing secret values in chat, logs or `.md` review files.
