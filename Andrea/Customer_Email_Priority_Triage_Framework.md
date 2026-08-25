# 📬 Customer Email Priority & Triage Framework

> A practical **Eisenhower Matrix–based classification system** for prioritising customer emails by **impact** and **time sensitivity**.

---

## 📑 Table of Contents

1. [🎯 Eisenhower Matrix](#-eisenhower-matrix)
2. [🏷️ Recommended Email Tags](#️-recommended-email-tags)
3. [💡 What “Important” Means](#-what-important-means)
4. [⏱️ What “Urgent” Means](#️-what-urgent-means)
5. [🧪 Classification Examples](#-classification-examples)
6. [🔎 Practical Filtering Design](#-practical-filtering-design)
7. [⚙️ Simple Tagging Rules](#️-simple-tagging-rules)
   - [Tag Assignment Logic](#tag-assignment-logic)

---

## 🎯 Eisenhower Matrix

Use the **Eisenhower Matrix** as a two-axis email classification system:

|  | **Urgent** | **Not urgent** |
|---|---|---|
| **Important** | <span style="color:#DC2626; font-weight:bold;">1. 🔴 Resolve now</span><br>Target SLA: **< 1 hour**<br>Handle immediately | <span style="color:#D97706; font-weight:bold;">2. 🟡 Investigate & follow up</span><br>Target SLA: **< 12 hours**<br>Assign owner and schedule resolution |
| **Not important** | <span style="color:#2563EB; font-weight:bold;">3. 🔵 Route or automate</span><br>Target SLA: **< 2 hours**<br>Use saved reply, flow, or routing | <span style="color:#6B7280; font-weight:bold;">4. ⚪ Close / self-service</span><br>Target SLA: **< 24 hours** (or Instant Bot)<br>Automate, merge, or close |

### Core Definitions

- **Importance** = the business, financial, operational, or customer impact if the issue is not resolved.
- **Urgency** = how quickly action is required to prevent a missed delivery window, chargeback, customer escalation, or lost parcel.

> **Key principle:** This framework separates **high-impact customer issues** from routine time-sensitive tasks.

---

## 🏷️ Recommended Email Tags

| Priority tier | Matrix category & tag | Target first-reply SLA | Target resolution SLA | Meaning | Default action |
|:---:|---|:---:|:---:|---|---|
| **1** | <span style="color:#DC2626; font-weight:bold;">🔴 RESOLVE NOW</span><br>*(Important & Urgent)* | **< 30 min** | **< 2 hours** | A critical customer, financial, legal, delivery, security, or reputation issue requiring immediate action | Handle immediately and escalate when necessary |
| **2** | <span style="color:#D97706; font-weight:bold;">🟡 INVESTIGATE & FOLLOW UP</span><br>*(Important & Not Urgent)* | **< 4 hours** | **< 12 hours** | A high-impact issue requiring research, cross-team coordination, or scheduled resolution within SLA | Assign an owner, investigate, and follow up within SLA |
| **3** | <span style="color:#2563EB; font-weight:bold;">🔵 ROUTE OR AUTOMATE</span><br>*(Not Important & Urgent)* | **< 1 hour** | **< 4 hours** | A time-sensitive but standard operational or administrative request with limited risk | Send a saved reply, trigger an automated shipping workflow, or route to the relevant queue |
| **4** | <span style="color:#6B7280; font-weight:bold;">⚪ CLOSE / SELF-SERVICE</span><br>*(Not Important & Not Urgent)* | **< 12 hours** | **< 24 hours** | An informational, duplicate, non-actionable, or low-value message | Send self-service content, merge into an existing ticket, archive, or mark as spam |

> **Note:** **Close / self-service** does not mean ignoring legitimate customers. It means resolving simple queries automatically, deflecting with knowledge-base links, merging duplicate inquiries into an open thread, or archiving noise.

---

## 💡 What “Important” Means

An email is **important** when it carries meaningful business, customer, or financial consequences—even if it does not require an instant reply.

### Mark an email important when it involves:

- **Order risk:** Lost parcels, misdeliveries, or orders that cannot be fulfilled.
- **Financial impact:** Payment errors, duplicate charges, or refunds over **€50**.
- **Returns & claims:** Damaged goods, return escalations, or warranty claims.
- **Retention & volume:** VIP customers, repeat buyers, or orders valued at **> €150**.
- **Legal & platform risk:** Chargeback threats, formal claims, or consumer dispute notices.
- **Systemic issues:** Recurring failures affecting **≥ 3 orders** on the same PostNL route.
- **Compliance & security:** Data privacy, account access, or suspected fraud.
- **Cross-functional investigation:** Cases requiring coordination across support, shipping, warehouse, or finance teams.

> **Rule:** *Importance is about impact, not tone.* An angry email about a minor question is not automatically important; a calm inquiry regarding a missing **€500** order is.

---

## ⏱️ What “Urgent” Means

An email is **urgent** when waiting causes immediate, time-bound consequences—such as carrier cutoffs, dispatch deadlines, or same-day delivery exceptions.

### Mark an email urgent when:

- **Dispatch deadlines:** Parcel cutoff is in **< 2 hours** and can still be stopped or modified.
- **Pickup point expiration:** The parcel will be returned to sender within **24 hours** if uncollected.
- **Same-day delivery:** Delivery is scheduled for **today** and address or buzzer details need updating.
- **Order cancellation:** Customer requests cancellation before warehouse packing starts (**within 1 hour of purchase**).
- **Dispute timelines:** Bank chargeback response deadline is in **< 24 hours**.
- **Widespread outages:** An active system or checkout incident impacting multiple customers simultaneously.
- **Security containment:** Compromised account or fraudulent transaction reported in real time.

> **Rule:** *Urgency is about deadlines, not customer pressure.* A message saying **“URGENT!!”** with no time-sensitive dependency should not be marked urgent.

---

## 🧪 Classification Examples

| # | Customer message | Important? | Urgent? | Applied tag | SLA target | Rationale |
|:---:|---|:---:|:---:|---|:---:|---|
| **01** | *“Order AF-2614 is 11 days overdue—please update me.”* | Yes | Yes | <span style="color:#DC2626; font-weight:bold;">🔴 RESOLVE NOW</span> | **< 30 min** | Severe fulfillment delay (**11 days**) with high cancellation and churn risk. |
| **02** | *“PostNL is delivering today, but the street number is wrong.”* | Yes | Yes | <span style="color:#DC2626; font-weight:bold;">🔴 RESOLVE NOW</span> | **< 30 min** | Delivery failure imminent unless corrected before the driver route starts today. |
| **03** | *“My parcel was delivered to the wrong city.”* | Yes | Yes | <span style="color:#DC2626; font-weight:bold;">🔴 RESOLVE NOW</span> | **< 30 min** | Potential misdelivery or lost parcel requiring prompt carrier contact. |
| **04** | *“My parcel was returned to the pickup point; can you resend it?”* | Yes | No | <span style="color:#D97706; font-weight:bold;">🟡 INVESTIGATE & FOLLOW UP</span> | **< 4 hours** | High customer impact, but reshipment can be handled within the standard **12-hour** SLA. |
| **05** | *“I want to return my order—please send a return label.”* | Yes | No | <span style="color:#D97706; font-weight:bold;">🟡 INVESTIGATE & FOLLOW UP</span> | **< 4 hours** | Standard return workflow requiring label generation and tracking. |
| **06** | *“Can I change delivery from pickup point to my home address?”* | No | Yes | <span style="color:#2563EB; font-weight:bold;">🔵 ROUTE OR AUTOMATE</span> | **< 1 hour** | Standard operational request; route directly to Shipping or apply macro before dispatch. |
| **07** | *“Where is my package?”* (within promised delivery window) | No | No | <span style="color:#6B7280; font-weight:bold;">⚪ CLOSE / SELF-SERVICE</span> | **Instant / < 12h** | Routine status check; resolve with automated tracking link. |
| **08** | *“What are your return conditions?”* | No | No | <span style="color:#6B7280; font-weight:bold;">⚪ CLOSE / SELF-SERVICE</span> | **Instant / < 12h** | Informational query; send help-centre link or template. |
| **09** | *“Any update??”* (duplicate message on open ticket) | No | No | <span style="color:#6B7280; font-weight:bold;">⚪ CLOSE / SELF-SERVICE</span> | **Merged** | Merge into the existing thread to avoid duplicate workload. |
| **10** | *“I was charged twice and will dispute it tomorrow.”* | Yes | Yes | <span style="color:#DC2626; font-weight:bold;">🔴 RESOLVE NOW</span> | **< 30 min** | Direct financial and chargeback risk requiring immediate review within **24 hours**. |
| **11** | *“Can you send me an invoice for my order?”* | No | Sometimes | <span style="color:#2563EB; font-weight:bold;">🔵 ROUTE OR AUTOMATE</span> *(or ⚪)* | **< 1 hour** | Simple administrative request; urgency depends on an explicit same-day deadline. |

---

## 🔎 Practical Filtering Design

Replace the generic inbox view with **four dedicated workflow filters** and counter badges:

1. **All (23)** — every active customer conversation.
2. <span style="color:#DC2626; font-weight:bold;">🔴 Resolve now (4)</span> — high-impact, time-sensitive cases requiring immediate agent ownership (**SLA < 2h**).
3. <span style="color:#D97706; font-weight:bold;">🟡 Investigate & follow up (3)</span> — high-impact cases to resolve within the standard queue (**SLA < 12h**).
4. <span style="color:#2563EB; font-weight:bold;">🔵 Route or automate (11)</span> — time-sensitive but routine tasks handled via templates, automated flows, or team routing (**SLA < 4h**).
5. <span style="color:#6B7280; font-weight:bold;">⚪ Close / self-service (5)</span> — informational, duplicate, or self-service queries ready for automated answers or closing.

### ⚠️ SLA Breach Risk

An optional <span style="color:#DC2626; font-weight:bold;">⚠️ SLA breach risk</span> badge should trigger automatically when a ticket reaches **≥ 75% of its allowed SLA time** without agent assignment or resolution.

---

## ⚙️ Simple Tagging Rules

A practical rule engine for the system:

### Importance Rules

```text
IMPORTANT = TRUE if:
- Category IN [Payment, Refund, Chargeback, Fraud, Lost Parcel, Misdelivery, VIP, Damaged Goods]
- Order Value >= €150
- Delay >= 5 business days
- Batch issue affecting >= 3 orders
```

### Urgency Rules

```text
URGENT = TRUE if:
- Carrier / pickup cutoff <= 24 hours (or warehouse dispatch <= 2 hours)
- Delivery status == "Out for delivery" OR "Delivery today"
- Parcel intercept or reroute possible == TRUE
- Payment or dispute deadline <= 24 hours
- System / store outage active == TRUE
```

### Tag Assignment Logic

```text
1. IF Important == TRUE AND Urgent == TRUE
   → 🔴 RESOLVE NOW
     Priority 1 | SLA: 30m reply / 2h resolve

2. IF Important == TRUE AND Urgent == FALSE
   → 🟡 INVESTIGATE & FOLLOW UP
     Priority 2 | SLA: 4h reply / 12h resolve

3. IF Important == FALSE AND Urgent == TRUE
   → 🔵 ROUTE OR AUTOMATE
     Priority 3 | SLA: 1h reply / 4h resolve

4. IF Important == FALSE AND Urgent == FALSE
   → ⚪ CLOSE / SELF-SERVICE
     Priority 4 | SLA: Bot instant / 24h resolve
```

---

## 🧭 Final Principle

> **Critical issues receive immediate ownership, while routine urgent tasks should not displace high-impact customer and financial priorities.**

---

### 🔗 Quick Navigation

| Section | Jump to |
|---|---|
| 🎯 Matrix | [Eisenhower Matrix](#-eisenhower-matrix) |
| 🏷️ Tags | [Recommended Email Tags](#️-recommended-email-tags) |
| 💡 Importance | [What “Important” Means](#-what-important-means) |
| ⏱️ Urgency | [What “Urgent” Means](#️-what-urgent-means) |
| 🧪 Examples | [Classification Examples](#-classification-examples) |
| 🔎 Filters | [Practical Filtering Design](#-practical-filtering-design) |
| ⚙️ Rules | [Simple Tagging Rules](#️-simple-tagging-rules) |

