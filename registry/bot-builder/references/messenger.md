# Messenger contract and platform verification

Create a MessengerClient interface over normalized incoming events and outgoing
operations: send/edit message, acknowledge callback, send/download file, register and
inspect webhook, and poll updates if supported. Identify platform, bot identity,
peer/sender, update ID, message ID, text, callback, attachment and payment event.
Treat all IDs as opaque and preserve platform scope. Core handlers import this
interface rather than issuing platform HTTP calls themselves.

Implement only the selected TelegramAdapter, BaleAdapter and/or RubikaAdapter, using
current official documents and actual account capabilities. The HTTP libraries can
be conventional async clients; normalize retries, timeouts, formatting/keyboards,
file identifiers and sanitized errors. Configure proxy/base URLs per platform when
required by network access. Never put bot tokens or token-bearing URLs in diagnostics.

- [Telegram Bot API](https://core.telegram.org/bots/api): verify update/callback
  shapes, webhook secret header, registration and delivery status.
- [Bale bot documentation](https://docs.bale.ai/): verify its own methods, native
  payments and amount units; compatibility does not imply identical behavior.
- [Rubika bot documentation](https://rubika.ir/botapi): implement its documented
  API and event schemas, including its webhook/endpoint registration and polling
  cursor contract, rather than replacing the Telegram base URL.

For every selected transport retain sanitized request/response fixtures and test
normalization. Prove live receive/send and a button round trip before declaring that
platform working. Polling and webhook inputs must reach the same normalized dispatcher.
