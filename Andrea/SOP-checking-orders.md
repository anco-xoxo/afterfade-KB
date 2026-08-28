# SOP — Checking Orders & Address Changes

## When to use
Use whenever a CS-ops task involves checking an order: confirming it exists, its status, shipment, tracking, pulling an invoice, or changing a customer's address.

## Where to check
- **Sendcloud** — check the order and its shipment. Sendcloud is where Afterfade's orders are shipped through the logistics partner, so look there for order status, shipping, and tracking information.
- **Shopify** — download the invoice. Invoices are pulled from Shopify, not Sendcloud.

## Steps
1. Open the order in Sendcloud to check its status (payment, processing, shipped, delivered).
2. If the task needs an invoice, download it from Shopify.
3. Log the order reference on the task card so the context is kept (see `SOP-task-management.md`).

---

## Changing a Customer Address

Use when a customer requests an address change after placing an order.

### Procedure
1. **Edit the address in Shopify first** — this is the order source and the single source of truth.
2. **Verify in Sendcloud** — open the order in Sendcloud and confirm the updated address has synced.
3. **If the parcel has already been handed to the carrier** — the address cannot be changed. Inform the customer that the change was not possible and, if needed, follow the return process once the parcel is delivered or returned.

### Priority
Address changes are time-sensitive. If the parcel is close to dispatch (< 2 hours), mark the request urgent (see `Customer_Email_Priority_Triage_Framework.md`).

## Related
- **SOP-returns-and-refunds.md** — returns and shipping claims
- **SOP-shipment-investigation.md** — returned/not-received parcel investigation and DPD escalation
- **SOP-task-management.md** — task card tracking
- **data/contacts.json** — contact channels
