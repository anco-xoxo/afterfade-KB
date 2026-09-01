# afterfade-KB

The knowledge base for the **Afterfade** customer-support assistant.

Afterfade BV (Paal, Belgium) sells DIY restoration coatings that bring faded
aluminium and PVC back to their original colour and gloss — applied by the
customer themselves in an afternoon. This repository holds the curated source
of truth the assistant uses to answer customer questions across web chat,
WhatsApp and voice.

## What this repo contains

### `kb/` — Knowledge Base (reference information)

Markdown files grouped by topic:

| Directory | Contents |
| --- | --- |
| `kb/company/` | Company overview, legal details, contact and support hours, supported languages |
| `kb/policies/` | Orders & shipping, returns & warranty, safety & compliance, e-invoicing & VAT |
| `kb/product_families/` | Products by family (coatings, surface prep, kits) plus the authoritative per-language product names |
| `kb/systems/` | The Restore-Protect-Maintain method: application steps, use cases, known questions |
| `kb/troubleshooting/` | Common issues and their resolution |
| `kb/definitions.json` | Definitions of materials and terms the assistant may be asked about (e.g. Trespa) |

### `data/` — Structured Data (single source of truth for facts)

JSON files that hold structured reference data. SOPs and KB files link to these instead of hardcoding the information:

| File | Contents |
| --- | --- |
| `data/contacts.json` | All contact channels: WhatsApp numbers, email, addresses, links |
| `data/payment_methods.json` | Payment methods, SEPA bank details (IBAN, BIC), troubleshooting |
| `data/returns.json` | Return deadlines, eligibility rules, return addresses |
| `data/questions.json` | Log of collected customer questions, used for the weekly common-issues survey |

### `Andrea/` — SOPs (action workflows)

Standard operating procedures for the support agent. Each SOP tells the agent **what to do** and links to `kb/` or `data/` for details:

| File | Purpose |
| --- | --- |
| `SOP-application.md` | Full product application workflow: water test, surface prep, application steps, coverage |
| `SOP-payments.md` | Payment methods overview + SEPA bank transfer process |
| `SOP-klarna.md` | Klarna checkout troubleshooting |
| `SOP-returns-and-refunds.md` | Returns, refunds, return-label creation + shipping claims |
| `SOP-ugc.md` | User-generated content incentive + Shopify discount codes |
| `SOP-estimate-information.md` | Quantity estimates for DIY product orders |
| `SOP-painting-quotes.md` | Professional on-site painting service quotes |
| `SOP-checking-orders.md` | Checking order status + customer address changes |
| `SOP-shipment-investigation.md` | Investigation of returned/not-received parcels + DPD escalation |
| `SOP-canary-islands-shipping.md` | Customs handling for Canary Islands orders |
| `SOP-task-management.md` | Task tracking rules (Trello/Vocero) |

## How it works

- The assistant answers in the language the customer writes in (Dutch, French,
  German, Spanish, Italian, Portuguese or English), translating the facts at
  answer time — the KB itself is written in English.
- Product names are never translated on the fly: they are pulled from
  [`kb/product_families/product_names_by_language.md`](kb/product_families/product_names_by_language.md).
- Prices are always in EUR and SKUs are never altered.
- Human-handled topics (orders, complaints, wholesale enquiries) escalate to
  the Afterfade team rather than being answered by the assistant.

## Editing

Keep facts accurate and consistent — this is the single source of truth for
customer-facing answers. When updating a fact (a price, a name, a policy),
check for other files that reference the same information so they stay aligned.

**Structured data** (contact details, bank addresses, return rules) lives in
`data/*.json`. Update it there — the SOPs and KB files reference the JSON
files instead of duplicating the values.
