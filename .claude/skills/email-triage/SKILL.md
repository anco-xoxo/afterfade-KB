---
name: email-triage
description: Label and prioritise incoming customer emails using the Afterfade Eisenhower matrix (RESOLVE NOW / INVESTIGATE & FOLLOW UP / ROUTE OR AUTOMATE / CLOSE / SELF-SERVICE), with SLAs, owner (Andrea vs VA) and escalation flags. Use whenever emails, tickets or an inbox need triaging, labelling, prioritising or sorting into a work queue.
---

# Customer email triage

Classify incoming customer email into the four Eisenhower quadrants defined in
`Andrea/Customer_Email_Priority_Triage_Framework.md`, and assign owner per
`Andrea/VA/VA-DELEGATION-FRAMEWORK.md`.

**Always run the script.** It is the rule engine — do not classify by eye. Reading
the framework and judging in-context produces different answers run to run; the
script produces the same answer every time and shows which rule fired.

## Workflow

1. **Collect the emails into JSON.** One object per email, minimum `subject` +
   `body`. Add any structured facts you already know (order value, delivery
   status, days overdue) — they outrank keyword matching and raise confidence.

   **Coming from Gmail (MCP or API)?** Pipe the raw messages through the
   adapter instead of hand-copying them:

   ```bash
   python3 .claude/skills/email-triage/scripts/gmail_to_triage.py gmail.json \
     | python3 .claude/skills/email-triage/scripts/triage.py - --format table --sort
   ```

   The adapter decodes base64url MIME parts, prefers `text/plain` over HTML,
   strips quoted replies and signatures (so an old 🔴 message can't re-fire on a
   "any update?" reply), reads `Subject`/`From`/`Date`, pulls the `AF-####`
   order ref, maps Gmail labels (`VIP`/`Wholesale` → `vip`, `CATEGORY_PROMOTIONS`
   → `bulk`), and marks the 2nd+ message on a `threadId` as `duplicate_of` the
   first. Sample input: `scripts/example-gmail-inbox.json` (14 messages, EN/NL/FR,
   covering all four quadrants plus a thread duplicate, a pressure-only mail, a
   no-signal mail and a newsletter).

2. **Run it:**

   ```bash
   python3 .claude/skills/email-triage/scripts/triage.py inbox.json --format table --sort
   ```

   Formats: `json` (default, full reasoning), `table` (markdown, for the human),
   `csv` (for a spreadsheet or helpdesk import). `--sort` orders by priority.
   Reads stdin when the path is `-` or omitted.

3. **Report the result.** Lead with the 🔴 queue and anything flagged
   `escalate_to_andrea`. Give each email its tag, SLA and owner.

4. **Handle the flags — this is where your judgement is needed, not before:**
   - `needs_human_review: true` — no rule fired, defaulted to priority 4. Read
     it yourself and say what you think it is.
   - `confidence: "low"/"medium"` — keyword-only match. If you can pull a real
     fact (Shopify order value, Sendcloud status), add it to the JSON and re-run.
   - `escalate_to_andrea: true` — VA prepares the case, Andrea makes the call.

5. **Never silently override the script.** If you disagree with a verdict, say
   so explicitly ("script says P3, I'd argue P2 because …") and, if the rule is
   genuinely wrong, offer to fix the rule rather than the one-off answer.

## Input fields

| Field | Effect |
|---|---|
| `id`, `from`, `subject`, `body` | `subject`+`body` drive keyword rules |
| `received_at` (ISO8601) | adds `reply_due` / `resolve_due` timestamps |
| `order_value_eur` | ≥ €150 → important |
| `refund_amount_eur` | > €50 → important + escalate to Andrea |
| `days_overdue` | ≥ 5 → important; ≥ 7 → also urgent |
| `orders_affected` | ≥ 3 → important + escalate (systemic) |
| `delivery_status` | `out_for_delivery` / `delivery_today` / `pre_dispatch` → urgent |
| `hours_to_cutoff`, `hours_to_dispute_deadline` | ≤ 24 → urgent |
| `vip` (bool) | important + escalate |
| `outage_active` (bool) | urgent |
| `duplicate_of` (str) | forces priority 4, merge into the open thread |
| `bulk` (bool) | newsletter / promotional — priority 4, archive, no review flag |
| `order_ref` (str) | passed through to the output for reference |

Examples: `scripts/example-inbox.json` (plain), `scripts/example-gmail-inbox.json`
(raw Gmail shape, needs the adapter).

## Output

| Priority | Tag | Reply / resolve SLA | Default owner |
|---|---|---|---|
| 1 | 🔴 RESOLVE NOW | 30 min / 2 h | Andrea |
| 2 | 🟡 INVESTIGATE & FOLLOW UP | 4 h / 12 h | VA (Andrea for exceptions) |
| 3 | 🔵 ROUTE OR AUTOMATE | 1 h / 4 h | VA |
| 4 | ⚪ CLOSE / SELF-SERVICE | 12 h / 24 h | VA |

Each result also carries `important_rules` / `urgent_rules` (the exact rule ids
and patterns that fired), `escalations`, `confidence` and `notes` — quote these
when a human asks why something landed where it did.

## Two rules the engine enforces on purpose

- **Importance is impact, not tone.** "URGENT!!!" with no time-bound dependency
  stays priority 4; the ignored pressure wording is recorded in `notes`.
- **Urgency is deadlines, not customer pressure.** A calm note about a €500
  order is important; an angry note about return policy is not.

## Maintaining the rules

Everything tunable lives at the top of `scripts/triage.py`: `THRESHOLDS`,
`IMPORTANT_RULES`, `URGENT_RULES`, `SELF_SERVICE_RULES`, `ESCALATION_RULES`.
Patterns are English + Dutch + French. After any change run:

```bash
python3 .claude/skills/email-triage/scripts/test_triage.py
```

It replays the 11 worked examples from the framework plus six edge cases
(tone vs impact, past-tense narration vs deadline, invoice with and without a
same-day deadline, bulk mail). All 17 must pass — that's the contract with the
written framework. Then re-run the Gmail fixture end to end and eyeball it.

## Sources

- `Andrea/Customer_Email_Priority_Triage_Framework.md` — authoritative
- `Andrea/VA/VA-DELEGATION-FRAMEWORK.md` — owner + escalation exceptions
- `Andrea/onboarding/ONBOARDING.md` § Email Triage — summary for new VAs
