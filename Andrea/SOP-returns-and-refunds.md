# SOP — Returns, Refunds & Shipping Claims

## When to use
Use when a customer wants to return an item, asks for a refund, or reports a parcel that is lost, damaged or delivered but not received.

## Key references
- Full return policy: `kb/policies/returns_warranty.md`
- Return deadlines and eligibility: `data/returns.json`
- Contact channels: `data/contacts.json`
- Task tracking: `SOP-task-management.md`

---

## Part 1: Returns & Refunds

### Return policy (summary)
- Customers have **14 calendar days** from receiving the order to notify Afterfade they want to return it, and a further **14 days** to send the items back.
- To start a return, the customer contacts Afterfade by email (hello@afterfade.be) or WhatsApp (+32 460 25 60 47) with their name, order number, product details and reason. Returns not notified in advance may be delayed.
- Afterfade refunds within **14 calendar days** of being notified of the return, though it may wait until the goods arrive back or proof of return shipment is provided.
- Refunds cover the purchase price and standard shipping, not any premium delivery surcharge.
- Sealed coatings and cleaners (Afterfade Pro-Tech+ and Afterfade Prep+) lose their return right once the seal is broken; custom or personalised items cannot be returned.
- Full policy: `afterfade.be/policies/refund-policy`

### Return address
The return address is communicated once the return request is approved and registered. Afterfade BV may direct returns to a specific address or logistics partner.

Spain return address:
Afterfade BV
Carrer Sant Joan 3
17491 Peralada
Spain

### Refund steps
1. **Log the task.** Create a card for the refund on the task board (see `SOP-task-management.md`).
2. **Check the order.** Verify the order and its status in Sendcloud; confirm it matches the customer's name and order number. If the parcel was lost or damaged in transit, see Part 2 below.
3. **Confirm eligibility.** Check against the return policy above (notification within 14 days, seal not broken, not a custom item). Refunds are escalated to a human in case of doubt.
4. **Give the return address.** Share the return address and ask the customer to send the items back with the order details.
5. **Process the refund.** Once the goods arrive back (or proof of return shipment is provided), process the refund and issue it within 14 days of notification. Refund the purchase price and standard shipping only.
6. **Close out.** Note the refund amount and outcome on the task card before moving on.

---

## Part 2: Shipping Claims (Sendcloud)

### When to use
Use when a customer's parcel is lost, damaged, delivered but not received, or delayed, and Afterfade needs to start an investigation or file a claim with the carrier through Sendcloud.

### Key rules
- **Own carrier contract:** if a shipment uses Afterfade's own carrier contract, the claim must be opened directly with the carrier, not with Sendcloud.
- **When to file:** a claim can only be filed once a parcel has been announced for at least 48 hours. Recommended start within 7 days of delivery or the last scan. For damaged shipments, file as soon as possible — late claims may be rejected.
- **Reimbursements do not include VAT.**
- **Uninsured parcels:** claims are based on per-kilo compensation only, unless the shipping option includes carrier default insurance (shown in the label details). A claim based on sales or purchase value is only possible with Sendcloud Shipping Protection insurance.
- **Insured parcels (Sendcloud Shipping Protection):** covers lost and damaged shipments only — file under "Shipment damaged" or "Shipment lost". Proof of ID is required for any shipment insured above GBP 1,000 (XCover policy). Compensation can be based on sales or purchase value.

### Damage claims

**Deadline:** Report damage no later than **14 days after delivery**.

**Preserve evidence:** Keep the damaged items and all packaging in their original condition until the claim is completed. Do not dispose of, repair, or clean anything — the carrier may request inspection.

**Documents required:**
- A detailed description of what happened
- Photos or video showing the damage, including the packaging
- The original shipping receipt and tracking number
- Information about the shipment and its value
- Any relevant order invoice or summary
- Customer correspondence confirming the issue, if available

### How to file a claim

**Option 1 — from the label details**
1. Go to Shipping > Orders in the Sendcloud panel.
2. Go to Shipped, click the shipment, and click the eye icon to open the label details.
3. You are redirected to the Support menu with the tracking number and claim reason pre-filled.
4. Click Find my shipment, fill in as many fields as possible, and click Submit.

**Option 2 — from the Support menu**
1. Open the Support menu (question mark icon) and click + New ticket.
2. Click Select a category > Submit a request for a parcel.
3. Select the claim reason, enter the tracking code, and click Find my shipment.
4. Fill in the required information and click Submit.

**Option 3 — bulk from the Shipped tab**
1. Go to Shipping > Orders > Shipped.
2. Select one or more shipments and click Create investigation.

### After submitting
- Sendcloud forwards the investigation to the carrier. It can take from a few days to several weeks; carriers set their own timelines.
- The carrier may request extra evidence (photos, invoices, a signed statement from the recipient). The ticket status changes to Action required — respond as quickly as possible, since delays can slow or hurt the claim.
- Track ticket status in the Support section (Lite subscription or higher: Support Automation → Issue Management).
- Keep all packaging materials and damaged products for at least 3 months after submitting a claim — the carrier may request them as evidence.

---

## Related
- **data/returns.json** — return deadlines, eligibility, addresses
- **data/contacts.json** — contact channels
- **SOP-task-management.md** — task card tracking
- **kb/policies/returns_warranty.md** — full official return policy
- **SOP-canary-islands-shipping.md** — customs handling for Canary Islands orders
