# Afterfade Knowledge Base — Project Summary

**Period:** August 1 – September 5, 2026
**Author:** Justin (with Andrea)

---

## What This Project Is

In just over one month, we built a complete, structured knowledge base and operational system for Afterfade's customer service function — from zero documentation to a fully operational CS infrastructure that supports a 7-language, 7-market European operation.

---

## Phase 1: Foundation (August 1–3)

### Knowledge base structure created

- Uploaded the initial knowledge base into a Git repository with a clear directory structure: `kb/` for facts, `Andrea/` for SOPs, `data/` for structured data, `dashboard/` for operations.
- Wrote the README describing the project architecture.
- Established the separation of concerns: knowledge base files contain *what to know*, SOPs contain *what to do*, data files contain *reusable facts*.

### First knowledge base entries

- Defined Trespa and door wreath in `kb/definitions.json` — terms customers ask about that need consistent definitions.
- Moved definitions to a structured JSON format for reuse.
- Created `data/questions.json` for logging customer questions weekly.

### First SOPs

- **SOP-task-management.md** — Established the rule: every CS task gets a Trello card, one task per card, 24-hour email SLA. Referenced the Trello board (https://trello.com/b/tJxpuJim/afterfade-cs-ops).
- **SOP-estimate-information.md** — How to handle "how much do I need?" questions, including a French template reply.
- **E-invoicing & VAT** — Documented Belgium's B2B e-invoicing mandate and VAT terminology.

### Key questions answered (Aug 2–3)

- **Can we produce invoices for a company?** Yes — Afterfade BV is a registered Belgian company (BE 1038.625.619) and can issue B2B invoices.
- **Types of order numbers** — Differentiated Shopify order numbers from Sendcloud tracking numbers. Established that Shopify is the source of truth for orders, Sendcloud for shipping.
- **Belgium has e-invoices** — Documented the Peppol BIS 3.0 format requirement for B2B e-invoicing in Belgium.

---

## Phase 2: Operational SOPs (August 4–10)

### Returns & refunds system

- Built a comprehensive returns SOP (`SOP-returns-and-refunds.md`) covering:
  - Return policy summary (14+14 day windows, eligibility rules)
  - Step-by-step refund workflow
  - Sendcloud return label creation (Part 2)
  - Dutch return client template (Part 3)
  - Shipping damage claims through Sendcloud (Part 4) with 3 filing options
  - Evidence requirements, deadlines, post-submission tracking

### Canary Islands shipping

- Created `SOP-canary-islands-shipping.md` after discovering the Canary Islands are outside EU VAT/customs territory despite being part of Spain.
- Documented the proforma invoice process, HS codes, IGIC tax (~7%), and customs declaration thresholds (H7 under EUR 150, H1/SAD over EUR 150, full SAD over EUR 1,000).
- Discovered and documented how to create proforma invoices in Billit.

### Quote system

- Created `SOP-painting-quotes.md` for the professional on-site spray-painting service.
- Established the quote intake process: pictures, material type, work description, quantity, condition, location.
- Set the rule: never invent a price.

### Item dashboard

- Created `Andrea/items-dashboard.md` with SKU weights, values, and HS codes for Sendcloud labels.
- Updated HS codes for the Complete Kit.
- Noted that some weight fields need to be filled in [FILL IN].

### Key questions answered (Aug 4–10)

- **How do we ask for proof of delivery from DPD?** Established that only the sender can request investigation, and the process goes through Sendcloud or directly to DPD.
- **How do we make proforma invoices for the Canary Islands?** Documented in the Canary Islands SOP.
- **Can I reply to emails through Vocero?** Yes — Vocero is one of the two approved task-tracking tools (alongside Trello).
- **How do I find an invoice with the order number?** Use Shopify admin → Orders → search.
- **What is the Belgian VAT for Sebastiaan?** BE 1038.625.619.
- **Discount link** — https://afterfade.be/en/pages/share-your-result

---

## Phase 3: Process Refinement (August 10–18)

### Trello rules established

- Created a "created date" rule for Trello cards.
- Established that marking a card as "resolved" should clear all pending labels.

### Carrier accounts

- Decided to create admin accounts for each carrier (DPD, bpost, GLS) to have direct control over investigations and claims.

### Vocero feedback

- Identified notification issues: need better notification management, ability to exclude AI handling, dark theme preference.
- Reported broken search bar.
- Reported UI issue: canned replies banner blocks the send button.

### Website scraped

- Scraped all major pages from afterfade.be (homepage, shop, FAQ, about, shipping, refunds, terms, privacy, cookies, results) into `Andrea/Questions and summaries /WebsiteMapping/`.
- Created a comprehensive website analysis (`website_Analysis.md`) with wireframe plans and knowledge base mapping.

### Trello board status

- Summarised both Trello boards (orders + emails) with 74 cards total, many duplicates, and identified stalled items.
- Created `Andrea/Questions and summaries /Summaries/summary16aug2026` as a snapshot.

### Laeti's return analysis

- Integrated Laeti's analysis of the returns process, identifying the logistics gap: Afterfade had zero intel on courier tariffs, coverage, and logistics capabilities per country.
- Established that Afterfade needs to negotiate with carriers per country, understand which courier covers which territory, and use that to inform return timelines.
- The return process should be: where was it shipped → which courier handles it (based on negotiated coverage) → how long it takes → inform the customer.

### Key questions answered (Aug 10–18)

- **When someone comments, they should authenticate** — flagged as a concern (Jolanda case).
- **Upload the whole project into Google Drive** — documented in backlog-log.md with folder ID and service account details.
- **How do we track when 2 kits are sent separately?** Established that Sendcloud tracks individual shipments, and Shopify orders can have multiple fulfillments.
- **Do we take bank transfers?** Yes — SEPA bank transfer with IBAN BE90 7380 5400 0932, BIC KREDBEBBXXX, Bank KBC Belgium. Documented in `SOP-payments.md` with templates in 5 languages.

---

## Phase 4: SOPs Working & Live Operations (August 18–25)

### SOPs validated in live use

- Confirmed that the SOP system worked in practice — the carrier investigation SOP was used for the Herman/GLS case (tracking 00736554482176, parcel redirected to Parcel Shop, customer couldn't find it).
- Established the 48-hour threshold for carrier investigations.

### Accounts & infrastructure

- Created `Andrea/Questions and summaries /Summaries/Accounts.md` to track all CS tool accounts (email, Shopify, Correos, PostNL).
- Set up Correos account for Coverso (hola@coverso.io).
- Created DPD account with Correos.
- Created PostNL account.
- Set up iPhone 14 Pro Max with Shopify passkey, Sendcloud in Chrome, Billit, Vocero.

### Thursday invoice policy

- Established that Thursdays are the designated day for editing/processing invoices. All invoice requests processed on Thursdays.
- Need to communicate this to customers and add to website.

### Email routing

- Discovered that contact form confirmations for house numbers need to be sent from hello@afterfade.be, but were going from info@afterfade.be. Fixed routing.
- Checked all contact forms to ensure they route to the correct inbox.
- Verified no duplicate information across systems.

### Discount campaign history

- Identified the need to maintain a history of all discount campaigns that have been run.

### Safety knowledge

- Documented TDS (Technical Data Sheet) and MSDS (Safety Data Sheet) terminology.
- Updated safety compliance: confirmed Pro-Tech+ is an eye irritant (H319), NOT flammable, gloves optional.
- Added safety section to product description in `kb/product_families/coatings/products.md`.

---

## Phase 5: Advanced Operations (August 25–September 2)

### Email priority triage system

- Built a comprehensive Eisenhower Matrix-based email classification framework (`Customer_Email_Priority_Triage_Framework.md`) with:
  - 4 priority tiers with defined SLAs
  - 11 classification examples
  - Importance rules (impact-based) and urgency rules (deadline-based)
  - Practical filtering design with counter badges
  - Tag assignment logic
  - SLA breach risk badge concept

### Shipment investigation workflow

- Updated `SOP-shipment-investigation.md` with a structured investigation process:
  - Log task → look up order → check DPD tracking → hand to team for resend/refund decision
  - DPD investigation channels (only sender can request, 3-day no-update threshold)
  - Route through local DPD office for foreign destinations
  - Example handoff template

### Return labels on Sendcloud

- Confirmed that return labels can be printed directly from Sendcloud (Natasja case).
- Rules documented in the returns SOP.

### Lost parcel retrieval

- Handled a case where a lost parcel was retrieved — established the decision framework: is it better to return the parcel or let the customer keep it?

### Canary Islands / Azores shipping

- Confirmed that shipping to Azores goes through UPS (not bpost/DPD).
- Updated Canary Islands SOP with correct carrier information.

### Italian customer interaction

- Handled a cleaning question from an Italian customer — added to troubleshooting knowledge.

### Glove order

- Ordered gloves from euro-industry.com for the Afterfade team.

### Billing and shipping addresses

- Documented Afterfade BV addresses:
  - Billing: Schaffensesteenweg 132, 3583 Paal, BE1038625619
  - Shipping: Hasseltstraat 40, Pelt 3900, Belgium

---

## Phase 6: Scaling & Onboarding (September 2–5)

### VA role discussion

- Discussed adding a Virtual Assistant to the team.
- Andrea's role shift: 60% operations & escalations, 40% email handling & VA management.
- VA responsibilities documented in Notion.
- Created the onboarding system for new CS hires.

### Knowledge base delivered

- Built the onboarding package in `Andrea/onboarding/`:
  - `ONBOARDING.md` — comprehensive guide covering company, products, safety, policies, application, tools, SOPs, communication, escalation, daily workflow, and a quick-reference file index.
  - `ONBOARDING-CHECKLIST.md` — day-by-day checklist for Week 1 (5 days) and Week 2 (supervised live), with sign-off table.

### Tool decisions

- **Trello** → only for orders and tasks that have a lifecycle (not general notes).
- **Notion** → memory and historical context (work in progress).
- **GitHub** → knowledge base source of truth, version-controlled.

---

## What Was Built — Complete Inventory

### Knowledge Base (`kb/`) — 16 files

| File | Purpose |
|------|---------|
| `company/overview.md` | Company identity, legal details, markets |
| `company/languages.md` | Supported languages, CLP phrasing rules |
| `policies/orders_shipping.md` | Shipping rates, carriers, free-shipping thresholds |
| `policies/returns_warranty.md` | Return policy, eligibility, warranty |
| `policies/safety_compliance.md` | H319 hazard, safe use, SDS sharing, CLP by language |
| `policies/e_invoicing_vat.md` | Belgian e-invoicing, VAT terminology |
| `product_families/coatings/overview.md` | What Pro-Tech+ is and isn't |
| `product_families/coatings/products.md` | Full product description, safety, technical data |
| `product_families/coatings/surfaces.md` | Surface compatibility guide |
| `product_families/coatings/selection_logic.md` | Decision logic for product recommendations |
| `product_families/surface_prep/overview.md` | Prep+ overview |
| `product_families/surface_prep/products.md` | Prep+ product description |
| `product_families/kits/overview.md` | Kit range overview |
| `product_families/kits/products.md` | All kit SKUs, prices, accessories |
| `product_families/kits/selection_logic.md` | Kit recommendation logic |
| `product_families/product_names_by_language.md` | Product names in 7 languages |
| `systems/restore_protect_maintain/overview.md` | The 3-step method |
| `systems/restore_protect_maintain/use_cases.md` | Surface-specific use cases |
| `systems/restore_protect_maintain/known_questions.md` | Common customer Q&A |
| `troubleshooting/common_issues.md` | Issue resolution guide |
| `definitions.json` | Term definitions (Trespa, door wreath) |

### SOPs (`Andrea/`) — 11 SOPs

| SOP | Lines | Coverage |
|-----|-------|----------|
| `SOP-application.md` | 142 | Full application workflow with templates |
| `SOP-payments.md` | 100 | Payment methods + SEPA with 5-language templates |
| `SOP-klarna.md` | 59 | Klarna checkout troubleshooting |
| `SOP-returns-and-refunds.md` | 172 | Returns, refunds, labels, shipping claims |
| `SOP-checking-orders.md` | 33 | Order status, address changes |
| `SOP-shipment-investigation.md` | 81 | Lost/returned parcel investigation |
| `SOP-estimate-information.md` | 44 | Quantity estimates with French template |
| `SOP-painting-quotes.md` | 27 | Professional painting service quotes |
| `SOP-ugc.md` | 36 | UGC incentive + Shopify discount codes |
| `SOP-canary-islands-shipping.md` | 27 | Canary Islands customs handling |
| `SOP-task-management.md` | 28 | Trello/Vocero task tracking rules |

### Operational Documents — 6 files

| File | Purpose |
|------|---------|
| `Customer_Email_Priority_Triage_Framework.md` | Eisenhower Matrix email classification |
| `items-dashboard.md` | SKU weights, HS codes for labels |
| `backlog-log.md` | Deferred items (Drive sync, dashboard sync) |
| `website_Analysis.md` | Website structure analysis and wireframe plan |
| `questions+bitacora.md` | Daily operations log |
| `Accounts.md` | Tool account credentials |

### Website Mapping — 10 pages scraped

Homepage, shop, FAQ, about, shipping, refunds, terms, privacy, cookies, results.

### Data Files — 4 files

`contacts.json`, `payment_methods.json`, `questions.json`, `returns.json`.

### Dashboard

Browser-based daily checklist with opening/closing workflows, dark theme, GitHub Pages deployment.

### Onboarding — 2 files

`ONBOARDING.md` (comprehensive guide) + `ONBOARDING-CHECKLIST.md` (day-by-day checklist).

---

## Key Decisions Made

1. **Task tracking:** Trello for lifecycle tasks, Notion for memory/history. One tool per task, not both.
2. **Invoice processing:** Thursdays only. All invoice requests queued and processed on Thursdays.
3. **SDS sharing:** Only to customers who have actually placed an order.
4. **Safety:** Pro-Tech+ is an eye irritant (H319), NOT flammable. Gloves optional for normal use.
5. **Coverage figure:** Quote ~10m² per bottle. The higher published figure is under review.
6. **Return address:** Carrer Sant Joan 3, 17491 Peralada, Spain (communicated after approval).
7. **Carrier strategy:** Negotiate per country, understand coverage, use that to inform return timelines.
8. **Email SLA:** 24 hours maximum for all email responses.
9. **Canary Islands:** Outside EU VAT territory, requires customs declarations, IGIC tax.
10. **Azores:** Ships via UPS, not bpost/DPD.

---

## Open Items & Gaps

1. **Coverage figure inconsistency** — Higher published number still marked [UNDER REVIEW].
2. **UFI discrepancy** — Two different UFI codes found for Pro-Tech+ SDS. Must be resolved.
3. **Prep+ safety classification** — SDS pending. Do not call it non-hazardous.
4. **Items dashboard** — Some weight/HS code fields still marked [FILL IN].
5. **questions.json** — Only 1 entry. Needs regular population from CS interactions.
6. **Accounts.md** — Plaintext passwords. Should be moved to a secrets manager.
7. **Dashboard cross-device sync** — Pending GitHub API integration.
8. **Google Drive auto-sync** — Pending service account setup.
9. **Discount campaign history** — Not yet maintained.
10. **Vocero notifications** — Need better management, dark theme, search bar fix.

---

## By the Numbers

| Metric | Count |
|--------|-------|
| Git commits | 30 |
| Knowledge base files | 16 |
| SOPs created | 11 |
| Data files | 4 |
| Operational documents | 6 |
| Website pages scraped | 10 |
| Languages supported | 7 |
| Markets served | 7 |
| Products documented | 8 SKUs |
| Email priority tiers | 4 |
| Days from zero to operational | 35 |
