# Telegram, Bale and Rubika adapters

## Normalize at the boundary

Choose the platforms explicitly and verify their current official APIs. A shared
business dispatcher receives an internal event, not a platform SDK object:

```text
Event(platform, bot_id, update_key, caller_id, chat_id, kind,
      text?, callback_token?, contact?, payment?, occurred_at)
Messenger.send_text(chat, text, buttons?, idempotency_key?) -> Delivery
Messenger.answer_callback(callback_id, text?) -> Delivery
Messenger.send_document(chat, file, caption?) -> Delivery
```

`Delivery` distinguishes accepted, retryable, permanently rejected and outcome-unknown.
This is an internal contract, not a claimed SDK shared by all three platforms. Retain
only needed raw fields in protected diagnostics. Do not log API tokens in request URLs.

Telegram update example (illustrative, not live identity):

```json
{"update_id":71,"message":{"message_id":9,"from":{"id":42},"chat":{"id":42,"type":"private"},"text":"/start"}}
```

Map `message`, `callback_query` and payment/contact variants separately; require the
trusted transport caller rather than text claiming an identity. Acknowledge callbacks
promptly, then process long work asynchronously. For Telegram choose polling or webhook,
verify the webhook URL/secret header, and inspect `getWebhookInfo`; stop the prior
consumer before cutover. Keep secrets in ignored environment files. Configure through
the application client so tokens never appear in shell history or evidence.

For Bale, verify the actual endpoint and current field/method behavior; maintain
separate fixtures for its callbacks, contact collection and native payment events.
For Rubika, start with its official `receiveUpdate`/`receiveInlineMessage` and polling
models. Map button IDs and chat/sender fields explicitly rather than treating Rubika
as Telegram with another base URL. Unsupported controls need a working text/menu
alternative, not a fabricated payload.

| Failure | Action |
| --- | --- |
| Invalid authentication | Stop retries; surface token/account repair without logging values |
| Rate limit | Apply bounded provider backoff; preserve pending outbox |
| Timeout after send | Mark outcome unknown; avoid duplicate effect on blind retry |
| Duplicate webhook | Return success after durable deduplication |
| Unsupported media/control | Explain limitation and send selected text fallback |
| Malformed/untrusted event | Reject or quarantine without business mutation |

Local webhooks can travel through a loopback reverse SSH tunnel behind the shared
HTTPS route. Test one actual inbound message, one button callback, one reply and
restart persistence on each chosen platform. Record identity and safe expected/actual
results separately from fixture tests. Sources: [Telegram](https://core.telegram.org/bots/api),
[Bale](https://docs.bale.ai/), [Rubika](https://rubika.ir/botapi).
