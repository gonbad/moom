# Platform boundaries and live verification

Normalize platform, bot identity, peer/sender, update/message ID, text, callback,
attachment and payment events behind a transport interface. Treat IDs as opaque and
platform-scoped. Implement only selected adapters from current official contracts;
do not assume Bale or Rubika is Telegram with a different base URL.

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Bale documentation](https://docs.bale.ai/)
- [Rubika Bot API](https://rubika.ir/botapi)

Verify send/edit/file operations, keyboard capabilities, callback acknowledgement,
delivery registration, authenticated webhooks and polling/cursors where supported.
Redact tokens from URLs/logs, normalize retries/timeouts and retain sanitized fixtures.
Prove receive/send and a real button round trip for each selected platform. Simulated
fixtures alone never establish that a live platform integration works.

For personal-account integrations, verify supported login and UI capabilities separately
from bot APIs. The person completes protected interactive login locally when needed.
Protect ignored session artifacts and prove restart under the actual deployment identity.
Never promise inline bot controls on a transport that lacks them.
