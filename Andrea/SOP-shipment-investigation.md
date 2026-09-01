# SOP — Shipment Investigation (Returned Parcel / Not Received)

## When to use
Use when a customer's parcel was delivered to a pick-up point but is no longer there, shows as "delivered" but was not received, or was returned to sender because it was not collected in time. This SOP covers investigating what happened and escalating the resolution (resend or refund).

## When NOT to use
Do not use this SOP for a routine status check of a parcel still in transit — that is handled in `SOP-checking-orders.md`. For a lost/damaged parcel where a carrier claim is being filed through Sendcloud, see the shipping-claims part of `SOP-returns-and-refunds.md`.

---

## Key references
- Order lookup: `SOP-checking-orders.md`
- Shipping claims and refunds: `SOP-returns-and-refunds.md`
- Task tracking: `SOP-task-management.md`
- Contact channels: `data/contacts.json`

---

## Part 1: Investigate the Parcel

### Steps
1. **Log the task.** Create a card on the task board (see `SOP-task-management.md`) and log the order and tracking reference.
2. **Look up the order.** Open the order in Sendcloud to confirm its status and tracking number (see `SOP-checking-orders.md`).
3. **Check the DPD tracking.** Open the tracking link from Sendcloud and review the latest status:
   - Confirm whether the parcel shows as **delivered at the pick-up point**, **returned to sender**, or is still in transit.
   - A parcel that was not collected in time is returned to the sender once it goes back through the carrier.
4. **If the pick-up point no longer has it**, the parcel is most likely already on its way back to the Afterfade warehouse (or has arrived). Confirm the current location in tracking and with the team.
5. **Hand to the team for a decision.** Deciding whether to **resend** the order or **refund** the customer is a human decision — escalate it and record it on the task card.

### Escalation details to collect from the customer
Gather and log all of these so the team can act immediately:
- Order number (e.g. AF-1374)
- Customer name
- Correct delivery address (street, number, postcode, city, country)
- Customer phone number
- Preferred contact method (phone or email)
- Tracking number
- Any notes (e.g. went on holiday, pick-up point no longer has it, contacted carrier)

---

## Part 2: DPD Investigation Channels

### When to open a DPD investigation
Open a DPD investigation when the parcel shows as delivered but was not received (e.g. at a pick-up point), or has had no tracking update for more than 3 days.

### Key rule
Only the **sender** (Afterfade) can request a parcel investigation with DPD. For a parcel delivered outside the Netherlands, DPD cannot give the recipient any information — they must be referred back to Afterfade, who will contact DPD in the destination country. Do not tell the customer to contact DPD directly for a foreign destination.

### How to request (per DPD's own guidance)
- A customer parcel with no tracking update for more than **3 days** → the sender requests an investigation with DPD.
- For parcels to countries other than the Netherlands → route through DPD's local office for that destination country (all local DPD offices are listed via Geopost).
- If you are offering Afterfade's own DPD contact, file the investigation through the Sendcloud Support menu (see `SOP-returns-and-refunds.md`, Part 4) so it is tracked.

### DPD (Netherlands) recipient support — for reference
> Applies only to the recipient of a parcel *within the Netherlands*. Since Afterfade sends from Belgium to multiple countries, most inquiries fall under the sender/destination-country rule above, not this one.
>
> - **Recipient phone:** 085-0022222 (local rate), Mon–Fri 08:00–17:30, Sat 09:00–17:00. Have the parcel number ready.
> - **Recipient of a parcel abroad:** DPD cannot give details — the customer must go through Afterfade (the sender).

---

## Part 3: Communication & Resolution

### Guideline for the assistant (when a human cannot act immediately)
- Acknowledge the customer's frustration and that the wait is not acceptable.
- Do **not** promise a specific outcome; resend vs. refund is a team decision.
- Collect the escalation details (see Part 1) and escalate to the team.
- Track the case as a task and follow up so the customer is not left waiting — repeated no-response is the failure this SOP exists to prevent.

### Example handoff (customer writes Spanish, response in English shown for reference)
Hand the case to a human with the full context, e.g.:
> Customer Patricia Moreno (patricia2674@hotmail.com, +34 625637467) — order AF-1374 (Afterfade PRO+ The Complete Kit, 85,94 EUR, paid). DPD 05308822225645 showed delivered 18/08 at the pick-up point, but the parcel was returned to sender because the customer was on holiday. Customer visited the pick-up point; it no longer has the parcel. Correct address: Avda Montseny 11 B, 08812 Sant Pere de Ribes, Barcelona. Requesting reshipment to home address. Escalate: resend or refund.

---

## Related
- **SOP-checking-orders.md** — order lookup and address changes
- **SOP-returns-and-refunds.md** — refunds, returns and Sendcloud shipping claims
- **SOP-task-management.md** — task card tracking
- **data/contacts.json** — contact channels
