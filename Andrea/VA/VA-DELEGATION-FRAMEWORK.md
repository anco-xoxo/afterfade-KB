# Afterfade VA Delegation Framework — Eisenhower-Based

## Delegation Principle

> **The VA owns everything that is not both Important *and* Urgent.**
> That means the VA takes full ownership of the **🟡 Important / Not Urgent** quadrant (investigate-and-follow-up work) as well as both **Not Important** quadrants (🔵 routine-urgent, ⚪ routine-not-urgent). Andrea's direct hands-on time is reserved for **🔴 Important / Urgent** cases and the small set of decision-authority exceptions inside the Important/Not-Urgent quadrant that legally, financially or reputationally cannot be delegated (see Section 4).

This flips the current default (Andrea touching almost everything) into a model where the VA is the first line of execution across three of the four quadrants, and Andrea's queue is deliberately short.

---

## 1. Quadrant → Owner Map

| Quadrant | Tag | SLA | Default owner | Why |
|---|---|---|---|---|
| Important & Urgent | 🔴 Resolve Now | 30 min reply / 2h resolve | **Andrea** | Needs judgement + speed together — the one combination too risky to hand to the execution layer |
| **Important & Not Urgent** | 🟡 **Investigate & Follow Up** | 4h reply / 12h resolve | **VA (primary)** — Andrea only for the exceptions in Section 4 | Has time to be worked through a process; this is exactly the kind of task a trained VA can execute reliably once the SOP is clear |
| Not Important & Urgent | 🔵 Route or Automate | 1h reply / 4h resolve | **VA** | Routine, low-risk, time-sensitive — templates and macros handle it |
| Not Important & Not Urgent | ⚪ Close / Self-Service | 12h reply / 24h resolve | **VA** | Informational, duplicate, or deflectable with existing content |

**Net effect:** the VA owns 🟡 + 🔵 + ⚪ in full. Andrea's personal queue shrinks to 🔴 plus the named exceptions below.

---

## 2. VA-Owned Task Inventory, by Quadrant

### 🟡 Important & Not Urgent — VA's primary workload
Standard, high-impact-but-not-time-critical cases the VA works through to resolution using the SOPs, escalating only if they hit an exception trigger (Section 4):

- Parcel returned to pickup point, needs reshipment (`SOP-shipment-investigation.md`)
- Standard return/refund requests under the €50 threshold — registering the return, sending the label, confirming eligibility (`SOP-returns-and-refunds.md`)
- Damaged/defective/wrong item reports — collecting order number, description, photos, opening the case
- Non-VIP customer complaints about delay (under 5 business days) — investigating tracking, providing an update, setting expectations
- Warranty questions that don't require a policy judgement call
- Standard carrier claim preparation (collecting evidence, filing through Sendcloud) once past the 48-hour threshold
- Coverage/quantity estimate requests using the approved guide figures — collecting photos, dimensions, surface condition
- Product/kit selection guidance (Complete Kit vs Double Kit vs Refill vs Prep+)
- Collecting professional-service quote information (photos, material, scope, location) before handing to the team
- UGC intake: confirming consent, collecting content, logging the task, applying the standard 10% code
- Following up on unanswered sales enquiries and incomplete customer information

### 🔵 Not Important & Urgent — VA owns via templates/routing
- Address or pickup-point-to-home changes before dispatch
- Simple invoice requests with no same-day deadline complication
- Klarna-at-checkout troubleshooting (standard template)
- Routine "please confirm my order" or "did my payment go through" checks

### ⚪ Not Important & Not Urgent — VA owns via self-service/close
- "Where is my package?" within the promised delivery window (send tracking link)
- General policy questions (return conditions, shipping cost, delivery times)
- Duplicate messages on an already-open ticket (merge and close)
- General product-info questions already covered in the FAQ/KB
- Basic social media product questions and comment monitoring

### Cross-cutting VA execution (regardless of quadrant, once a case is opened)
- Sendcloud order/shipment/tracking lookups
- Shopify invoice retrieval
- Creating and updating Trello/Vocero task cards, attaching order numbers, photos, and status
- Website/FAQ inconsistency flagging (VA flags, Andrea approves the fix, VA executes the approved edit)
- Social media monitoring, lead forwarding, UGC organising and follow-up

---

## 3. Andrea-Owned Task Inventory (what stays off the VA's plate)

### 🔴 Important & Urgent — always Andrea (or Andrea-directed escalation)
- 11+ day overdue orders / severe fulfilment delay with churn risk
- Same-day delivery address errors that can still be corrected before the driver route starts
- Misdelivery to the wrong city
- Duplicate-charge disputes with a chargeback threatened within 24 hours
- Active system/checkout outages affecting multiple customers
- Suspected fraud or compromised account, in real time

### Strategic / non-triage work — never enters the inbox queue at all
- SOP creation and maintenance; process design and bottleneck removal
- Systems ownership: Shopify, Sendcloud, Trello/Vocero configuration and automation
- Fulfilment centre coordination, inventory visibility and replenishment
- Carrier negotiation (tariffs, coverage, service levels)
- Supplier invoices, large bills, accounting coordination
- KPI definition and reporting to Sebastiaan
- VA training, oversight and performance management

---

## 4. Exceptions — Important/Not-Urgent Cases the VA Must Still Escalate

Not urgent does not always mean safely delegable. A small set of 🟡-quadrant cases carry decision authority, legal, financial or reputational weight that stays with Andrea even though there's no deadline pressure. The VA works the intake (collects information, opens the task) but hands the *decision* to Andrea:

- Refunds or compensation **over €50**
- **VIP or high-value (>€150) customer** complaints of any kind
- **Chargeback, legal or formal dispute** notices, even with no imminent deadline
- **Data privacy, account-access or fraud** concerns
- **Systemic issues** affecting 3+ orders on the same route/carrier
- **Custom colour, wholesale/B2B, or professional-quote pricing** decisions
- **Discount requests** beyond the standard, pre-approved 10% UGC code
- **Manufacturer/sourcing** questions
- Any case where the knowledge base doesn't cover the answer, or two sources conflict

Rule of thumb for the VA: *if it would require the VA to make a judgement call the SOP doesn't already make for them, it escalates — regardless of urgency.*

---

## 5. Resulting Division of Labour

```
                         SEBASTIAAN
                              │
                 ┌────────────┴────────────┐
                 │                          │
             ANDREA                        VA
      🔴 Important+Urgent           🟡 Important+Not Urgent
      Exceptions inside 🟡          🔵 Not Important+Urgent
      Strategy / Systems /          ⚪ Not Important+Not Urgent
      Fulfilment / Finance          (full ownership, SOP-driven)
```

| Quadrant | Volume (indicative, from triage examples) | Owner |
|---|---|---|
| 🔴 Resolve Now | ~17% of active queue | Andrea |
| 🟡 Investigate & Follow Up | ~13% of active queue | VA (minus named exceptions) |
| 🔵 Route or Automate | ~48% of active queue | VA |
| ⚪ Close / Self-Service | ~22% of active queue | VA |

On this split, roughly **83% of the inbound queue** moves to the VA by default, with Andrea's attention concentrated on the ~17% that is genuinely time-critical plus the smaller set of high-stakes 🟡 exceptions that surface as they occur.

---

## 6. What This Requires to Work

1. **SOP coverage** for every 🟡/🔵/⚪ task type listed above must be current — the VA should never be improvising outside a documented procedure.
2. **A clear escalation trigger list** (Section 4) built into the VA's working reference, not left to judgement.
3. **Task visibility for Andrea** — Trello/Vocero must surface escalated and exception cases automatically rather than requiring Andrea to scan the full inbox.
4. **A short daily/weekly check-in** where Andrea reviews closed 🟡 cases in bulk (spot-check, not re-do) to catch drift before it becomes a pattern.