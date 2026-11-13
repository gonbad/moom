# Agent transport and conversation delivery

The transport authenticates the caller and yields a normalized internal envelope:

```text
ConversationEvent(platform, bot_id, caller_id, chat_id, event_key,
                  kind, text?, callback_token?, occurred_at)
```

The serving model receives sanitized text/context plus authoritative current business
state. It never chooses caller identity, API tokens, raw webhook routing or unrestricted
message destinations. Store pending proposals separately from generated prose.
For Telegram, adapt `message`/`callback_query` and verify webhook secret/URL or polling
configuration. Bale needs its own tested fixtures for messaging and payment objects;
Rubika needs explicit mapping of its update and button models. Consult current APIs:
[Telegram](https://core.telegram.org/bots/api), [Bale](https://docs.bale.ai/),
[Rubika](https://rubika.ir/botapi). Do not assume a common API from similar button names.

Use durable event deduplication, one active consumer and a per-caller run policy.
Acknowledge callbacks promptly; preserve incoming events while inference is delayed.
On a send timeout distinguish outcome-unknown from rejection. Record that an offer
was delivered before accepting a later soft confirmation. Multi-part replies must not
leave an undelivered confirmation pending. Buttons/contact/approval controls are
adapter capabilities; offer a working text alternative when the platform lacks them.

| Condition | Agent behavior |
| --- | --- |
| Duplicate update | Reuse durable run outcome; no second tool mutation |
| Parallel caller messages | Serialize/merge under a documented policy |
| Model outage | Preserve event/state and route to selected deterministic fallback |
| Tool success, reply failure | Reconstruct answer from result; never repeat action |
| Expired button or pending action | Explain current state; do not reuse authority |
| Platform auth/rate limit | Bounded retry/repair independent of model reasoning |

Test live inbound/outbound delivery, genuine model turns, cancellation, restarts and
fallback recovery on chosen platforms separately. Use synthetic callers and authorized
sandbox effects; record safe IDs and revisions instead of raw customer histories.
