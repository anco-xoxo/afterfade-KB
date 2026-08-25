Use the **Eisenhower Matrix** as a two-axis email classification system:

|  | **Urgent** | **Not urgent** |
|---|---|---|
| **Important** | **Resolve now**<br>Handle immediately | **Investigate & follow up**<br>Assign owner and schedule resolution |
| **Not important** | **Route or automate**<br>Use saved reply, flow, or routing | **Close / self-service**<br>Automate, merge, or close |

- **Importance** = the business, financial, operational, or customer impact if the issue is not resolved.

- **Urgency** = how quickly action is required to prevent a missed delivery window, chargeback, customer escalation, or lost parcel.

This creates four clear email tags and inbox filters, separating high-impact customer issues from routine time-sensitive tasks .

***

## Recommended email tags

| Matrix category | Meaning | Default action |
|---|---|---|
| **Resolve now**<br>*(Important & Urgent)* | A critical customer, financial, legal, delivery, security, or reputation issue requiring immediate action | Handle immediately and escalate when necessary |
| **Investigate & follow up**<br>*(Important & Not Urgent)* | A high-impact issue requiring research, cross-team coordination, or scheduled resolution within the standard service-level agreement | Assign an owner, investigate, and follow up within SLA |
| **Route or automate**<br>*(Not Important & Urgent)* | A time-sensitive but standard operational or administrative request with limited business or customer risk | Send a saved reply, trigger an automated shipping workflow, or route to the relevant queue |
| **Close / self-service**<br>*(Not Important & Not Urgent)* | An informational, duplicate, non-actionable, or low-value message | Send self-service content, merge into an existing ticket, archive, or mark as spam |

*Note: **Close / self-service** does not mean ignoring legitimate customers. It means resolving simple queries automatically, deflecting with knowledge-base links, merging duplicate inquiries into an open thread, or archiving noise.*

***

## What “important” means

An email is **important** when it carries meaningful business, customer, or financial consequences—even if it does not require an instant reply.

Mark an email important when it involves:
- Lost parcels, misdeliveries, or orders that cannot be fulfilled.
- Payment errors, duplicate charges, or blocked refunds.
- Return, cancellation, or warranty cases with direct financial impact.
- VIP, repeat, or high-value customer inquiries where retention is at risk.
- Formal complaint threats, chargeback risks, or consumer disputes.
- Recurring operational issues affecting multiple orders or carrier routes.
- Data privacy, account security, or fraud concerns.
- Investigations requiring coordination across support, shipping, warehouse, or finance teams.

> **Rule:** *Importance is about impact, not tone.* An angry email about a minor question is not automatically important; a calm inquiry regarding a missing high-value order is.

***

## What “urgent” means

An email is **urgent** when waiting causes immediate, time-bound consequences—such as carrier cutoffs, dispatch deadlines, or same-day delivery exceptions.

Mark an email urgent when:
- A parcel can still be rerouted, stopped, or corrected before carrier dispatch.
- A package is at risk of being returned from a pickup point today.
- Delivery is scheduled for today and address or access details need immediate updating.
- An order must be cancelled or modified before warehouse packing.
- A payment dispute, chargeback, or refund deadline is expiring shortly.
- An active issue affects multiple customers simultaneously right now.
- Security, fraud, or safety concerns require immediate containment.

> **Rule:** *Urgency is about deadlines, not customer pressure.* A message saying "URGENT!!" with no time-sensitive dependency should not be marked urgent .

***

## Classification examples

| Customer message | Important? | Urgent? | Applied tag | Rationale |
|---|:---:|:---:|---|---|
| *"Order AF-2614 is 11 days overdue—please update me."* | Yes | Yes | `RESOLVE NOW` | Severe fulfillment delay with high cancellation and churn risk. |
| *"PostNL is delivering today, but the street number is wrong."* | Yes | Yes | `RESOLVE NOW` | Delivery failure imminent unless corrected before carrier cutoff. |
| *"My parcel was delivered to the wrong city."* | Yes | Yes | `RESOLVE NOW` | Potential misdelivery or lost parcel requiring prompt carrier contact. |
| *"My parcel was returned to the pickup point; can you resend it?"* | Yes | No | `INVESTIGATE & FOLLOW UP` | High customer impact, but reshipment can be handled within standard SLA. |
| *"I want to return my order—please send a return label."* | Yes | No | `INVESTIGATE & FOLLOW UP` | Standard return workflow requiring label generation and tracking. |
| *"Can I change delivery from pickup point to my home address?"* | No | Yes | `ROUTE OR AUTOMATE` | Standard operational request; route directly to Shipping or apply macro. |
| *"Where is my package?" (within promised delivery window)* | No | No | `CLOSE / SELF-SERVICE` | Routine status check; resolve with automated tracking link. |
| *"What are your return conditions?"* | No | No | `CLOSE / SELF-SERVICE` | Informational query; send help-centre link or template. |
| *"Any update??" (duplicate message on open ticket)* | No | No | `CLOSE / SELF-SERVICE` | Merge into the existing thread to avoid duplicate workload. |
| *"I was charged twice and will dispute it tomorrow."* | Yes | Yes | `RESOLVE NOW` | Direct financial and chargeback risk requiring immediate review. |
| *"Can you send me an invoice for my order?"* | No | Sometimes | `ROUTE OR AUTOMATE` if needed today; otherwise `CLOSE / SELF-SERVICE` | Simple administrative request; urgency depends on an explicit same-day deadline. |

***

## Practical filtering design

Replace the generic inbox view with four dedicated workflow filters:

- **All** — every active customer conversation.
- **Resolve now** — high-impact, time-sensitive cases requiring immediate agent ownership.
- **Investigate & follow up** — high-impact cases to resolve within the standard SLA queue.
- **Route or automate** — time-sensitive but routine tasks handled via templates, automated flows, or team routing.
- **Close / self-service** — informational, duplicate, or self-service queries ready for automated answers or closing.

An optional **SLA breach risk** badge can be displayed alongside these filters whenever an unassigned or pending ticket approaches its deadline.

***

## Simple tagging rules

A practical rule engine for the system:

```text
IMPORTANT = TRUE if:
- Category IN [Payment, Refund, Chargeback, Fraud, Lost Parcel, Misdelivery, VIP, Damaged Goods, Overdue > 5 days]

URGENT = TRUE if:
- Carrier / pickup cutoff <= 24 hours
- Delivery status == "Out for delivery" OR "Delivery today"
- Parcel intercept or reroute possible == TRUE
- Payment or dispute deadline <= 24 hours
- System or batch issue affecting multiple orders == TRUE
```

### Tag assignment logic

```text
IF Important AND Urgent         → RESOLVE NOW
IF Important AND NOT Urgent      → INVESTIGATE & FOLLOW UP
IF NOT Important AND Urgent      → ROUTE OR AUTOMATE
IF NOT Important AND NOT Urgent  → CLOSE / SELF-SERVICE
```

This structure ensures critical issues receive immediate ownership, while routine urgent tasks do not displace high-impact customer and financial priorities .