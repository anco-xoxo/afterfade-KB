# afterfade-KB

The knowledge base for the **Afterfade** customer-support assistant.

Afterfade BV (Paal, Belgium) sells DIY restoration coatings that bring faded
aluminium and PVC back to their original colour and gloss — applied by the
customer themselves in an afternoon. This repository holds the curated source
of truth the assistant uses to answer customer questions across web chat,
WhatsApp and voice.

## What this repo contains

Markdown files under [`kb/`](kb/), grouped by topic:

| Directory | Contents |
| --- | --- |
| `kb/company/` | Company overview, legal details, contact and support hours, supported languages |
| `kb/policies/` | Orders & shipping, returns & warranty, safety & compliance |
| `kb/product_families/` | Products by family (coatings, surface prep, kits) plus the authoritative per-language product names |
| `kb/systems/` | The Restore-Protect-Maintain method: application steps, use cases, known questions |
| `kb/troubleshooting/` | Common issues and their resolution |
| `kb/definitions.json` | Definitions of materials and terms the assistant may be asked about (e.g. Trespa) |

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
