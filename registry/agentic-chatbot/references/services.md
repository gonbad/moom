# Business services and complete integrations

Inventory existing APIs, owned business backends and required API bridges. Record
contract, owner, authentication, scoped identity mapping, supported UI and evidence
for each in LIVING/tools.md. Reuse existing business engines. Where no usable service
exists, building its backend or bridge is part of this product rather than a placeholder
external prerequisite. Review new HTTP contracts under SOURCE/contracts/ before build;
reference current authoritative contracts for existing APIs.

The business service owns domain records, final eligibility, settlement and transactions.
The agent owns conversations/runs, sanitized history, handles and pending proposals.
A bridge owns connection/session state. Components may share the repository and VPS
while retaining separate code/state and service authorization. Agent clients call the
business API; broad credentials plus a model-chosen user ID are not caller binding.

Return structured sanitized outcomes and render them in the approved persona. Verify
unknown remote mutation outcomes before retrying. Payment OCR is evidence extraction,
not proof of settlement; the reviewed optimistic policy can grant provisional access.

For personal-account integrations, use only verified UI controls and supported login
methods. The person completes protected interactive login locally when needed. Keep
session artifacts ignored, transfer only required artifacts to the authorized server,
protect them and prove restart under the real service identity. Never promise bot-only
inline controls on a transport that lacks them. Explain any extra trusted approval
interaction before the owner selects a hard policy there.
