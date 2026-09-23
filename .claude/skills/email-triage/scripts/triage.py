#!/usr/bin/env python3
"""Afterfade customer email triage — Eisenhower rule engine.

Deterministic implementation of Andrea/Customer_Email_Priority_Triage_Framework.md.
Reads one email object or a list of them as JSON (stdin or file), decides
IMPORTANT / URGENT, and emits the tag, priority, SLAs, owner and the exact
rules that fired.

Usage:
    echo '{"subject":"...","body":"..."}' | python3 triage.py
    python3 triage.py inbox.json --format table
    python3 triage.py inbox.json --format csv > triaged.csv

Input fields (only subject/body required; structured fields beat keywords):
    id, from, subject, body, received_at (ISO8601),
    order_value_eur, refund_amount_eur, days_overdue, orders_affected,
    delivery_status (out_for_delivery|delivery_today|at_pickup_point|
                     pre_dispatch|delivered|in_transit),
    hours_to_cutoff, hours_to_dispute_deadline,
    vip (bool), duplicate_of (str), outage_active (bool)
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timedelta, timezone

# --------------------------------------------------------------------------
# Thresholds — from the framework. Change here, never inside the rules.
# --------------------------------------------------------------------------
THRESHOLDS = {
    "important_order_value_eur": 150,   # > €150 order = important
    "important_refund_eur": 50,         # refunds over €50 = important + escalate
    "important_delay_days": 5,          # >= 5 business days overdue
    "important_batch_orders": 3,        # >= 3 orders on the same route
    "urgent_cutoff_hours": 24,          # carrier / pickup cutoff window
    "urgent_dispatch_hours": 2,         # warehouse dispatch window
    "urgent_dispute_hours": 24,         # chargeback response deadline
}

# --------------------------------------------------------------------------
# Keyword rules. Multilingual (EN / NL / FR) — afterfade.be sells into BE/NL.
# Each pattern is matched case-insensitively against "subject \n body".
# --------------------------------------------------------------------------
IMPORTANT_RULES = [
    ("IMP-PAYMENT", "Payment error or duplicate charge", [
        r"\bcharged twice\b", r"\bdouble charge", r"\bduplicate charge",
        r"\bpayment (error|failed|issue|problem)", r"\bwrong amount\b",
        r"\btwee keer (betaald|afgeschreven)", r"\bdubbel (betaald|afgeschreven)",
        r"\bbetaling (mislukt|geweigerd|probleem)",
        r"\bdébité deux fois", r"\bpaiement (refusé|échoué|problème)",
    ]),
    ("IMP-REFUND", "Refund or compensation request", [
        r"\brefund\b", r"\bmoney back\b", r"\bterugbetaling\b", r"\bgeld terug\b",
        r"\bremboursement\b", r"\bcompensat", r"\bvergoeding\b",
    ]),
    ("IMP-CHARGEBACK", "Chargeback, legal or formal dispute", [
        r"\bchargeback\b", r"\bdispute\b", r"\bdisputing\b", r"\bmy bank\b",
        r"\blawyer\b", r"\blegal action\b", r"\bconsumer (protection|authority)\b",
        r"\bombudsman\b", r"\bsmall claims\b", r"\btest ?aankoop\b",
        r"\bincasso\b", r"\badvocaat\b", r"\bjuridische stappen\b",
        r"\bavocat\b", r"\bmise en demeure\b", r"\blitige\b",
    ]),
    ("IMP-FRAUD", "Fraud, account access or data privacy", [
        r"\bfraud", r"\bunauthori[sz]ed\b", r"\bhacked\b", r"\bstolen card\b",
        r"\bgdpr\b", r"\bavg\b", r"\bdata (privacy|breach|request)\b",
        r"\bdelete my (data|account)\b", r"\baccount (locked|access)\b",
        r"\bfraude\b", r"\bgegevens verwijderen\b", r"\bpersoonsgegevens\b",
        r"\bdonnées personnelles\b", r"\bpiratage\b",
    ]),
    ("IMP-LOST", "Lost parcel or non-delivery", [
        r"\blost (parcel|package|order)\b", r"\bnever (arrived|received|delivered)\b",
        r"\bstill (haven'?t|not) received\b", r"\bmissing (parcel|package|order|item)\b",
        r"\bpakket (kwijt|verdwenen|nooit|niet ontvangen)\b", r"\bniks ontvangen\b",
        r"\bcolis (perdu|jamais re[çc]u|non re[çc]u)\b",
    ]),
    ("IMP-MISDELIVERY", "Misdelivery or wrong / incomplete address", [
        r"\bwrong (address|city|street|house|door|postcode|zip)\b",
        r"\b(address|city|street|house number|street number|postcode|zip)\b[^.\n]{0,25}\b(is |are )?(wrong|incorrect|missing|not right)\b",
        r"\bdelivered to (the )?(wrong|neighbou?r)", r"\bsomeone else('s)? (address|door)\b",
        r"\bverkeerd(e)? (adres|stad|straat|huisnummer)\b", r"\bbij de buren\b",
        r"\b(adres|huisnummer|postcode)\b[^.\n]{0,25}\b(klopt niet|is verkeerd|ontbreekt)\b",
        r"\bmauvaise adresse\b", r"\blivré (au mauvais|chez le voisin)",
        r"\b(adresse|num[ée]ro)\b[^.\n]{0,25}\b(incorrect|erron[ée]|manque)\b",
    ]),
    ("IMP-DELIVERY-FAILED", "Delivery failed / parcel returned — needs reshipment", [
        r"\breturned to (sender|the )?(pickup point|depot|warehouse|you)\b",
        r"\bsent back to (you|sender)\b", r"\b(can you |please )?(resend|reship|send it again)\b",
        r"\bteruggestuurd\b", r"\bterug naar (de )?(afzender|afhaalpunt)\b",
        r"\bopnieuw (versturen|opsturen)\b",
        r"\bretourn[ée] (à l'exp[ée]diteur|au point relais)\b", r"\brenvoyer (le colis|la commande)\b",
    ]),
    ("IMP-DAMAGED", "Damaged, defective or wrong item", [
        r"\bdamaged\b", r"\bbroken\b", r"\bleaking\b", r"\bdefect", r"\bfaulty\b",
        r"\bwrong (item|product|colou?r|size)\b", r"\bempty (bottle|can|tin)\b",
        r"\bbeschadigd\b", r"\bkapot\b", r"\bgebroken\b", r"\blekt?\b",
        r"\bverkeerd(e)? (product|artikel|kleur)\b",
        r"\bendommag", r"\bcass[ée]", r"\bd[ée]fectueux\b", r"\bmauvais produit\b",
    ]),
    ("IMP-RETURN-ESCALATION", "Return escalation or warranty claim", [
        r"\bwarranty\b", r"\bguarantee\b", r"\bgarantie\b", r"\bwaarborg\b",
        r"\breturn (escalat|refused|rejected|ignored)", r"\bthird time\b",
        r"\bstill waiting for (my )?(return|refund|label)\b",
    ]),
    ("IMP-RETURN", "Return or cancellation request", [
        r"\breturn (label|my order|the order)\b", r"\bwant to return\b",
        r"\bsend (it |them )?back\b", r"\bretourneren\b", r"\bretourlabel\b",
        r"\bterugsturen\b", r"\bherroeping", r"\bretourner\b", r"\bétiquette de retour\b",
        r"\bdroit de r[ée]tractation\b",
    ]),
    ("IMP-SYSTEMIC", "Systemic / multi-order or outage report", [
        r"\bmultiple orders\b", r"\ball (my |our )?orders\b", r"\bsame problem (again|as)\b",
        r"\bwebsite (is )?(down|broken)\b", r"\bcheckout (is )?(broken|failing|down)\b",
        r"\bmeerdere bestellingen\b", r"\bsite (ligt plat|werkt niet)\b",
        r"\bplusieurs commandes\b", r"\bsite (hors service|ne fonctionne pas)\b",
    ]),
    ("IMP-VIP", "VIP / wholesale / B2B / professional enquiry", [
        r"\bwholesale\b", r"\bb2b\b", r"\bbulk order\b", r"\breseller\b",
        r"\bdistributor\b", r"\bprofessional (quote|project)\b", r"\bcustom colou?r\b",
        r"\bgroothandel\b", r"\bwederverkoper\b", r"\bofferte\b",
        r"\bgrossiste\b", r"\brevendeur\b", r"\bdevis\b",
    ]),
]

URGENT_RULES = [
    ("URG-TODAY", "Delivery / dispatch happening today", [
        # A delivery verb must sit next to the time word — "arrived this morning"
        # is narration about the past, not a deadline.
        r"\b(deliver\w*|arriv(e|es|ing)|coming|schedul\w*|due)\b[^.\n]{0,25}"
        r"\b(today|this (morning|afternoon))\b",
        r"\b(today|this (morning|afternoon))\b[^.\n]{0,25}"
        r"\b(deliver\w*|arriv(e|es|ing)|coming|schedul\w*|due)\b",
        r"\bout for delivery\b", r"\btoday between\b",
        r"\bvandaag\b[^.\n]{0,25}\b(levert|lever|geleverd|bezorgt|bezorgd|onderweg|komt)\b",
        r"\b(levert|lever|bezorgt|geleverd|bezorgd|komt)\b[^.\n]{0,25}\bvandaag\b",
        r"\blivraison aujourd'hui\b", r"\bliv\w* aujourd'hui\b",
        r"\baujourd'hui\b[^.\n]{0,25}\bliv\w*\b",
    ]),
    ("URG-INTERCEPT", "Parcel can still be stopped, rerouted or corrected", [
        r"\bstop the (parcel|package|delivery|shipment)\b", r"\bbefore (it|the parcel) ships?\b",
        r"\bchange (the )?(address|delivery address|pickup point)\b",
        r"\breroute\b", r"\bredirect\b", r"\bbuzzer\b", r"\bdoorbell\b",
        r"\badres (wijzigen|aanpassen|veranderen)\b", r"\bnog niet verzonden\b",
        r"\bchanger (l'|d')adresse\b", r"\bpas encore exp[ée]di",
    ]),
    ("URG-PICKUP-EXPIRY", "Pickup point return deadline", [
        r"\bpickup point\b.{0,40}\b(expir|return|last day|deadline)\b",
        r"\b(expir|return|last day|deadline)\b.{0,40}\bpickup point\b",
        r"\bafhaalpunt\b.{0,40}\b(terug|verloopt|laatste dag)\b",
        r"\bpoint relais\b.{0,40}\b(retour|expire|dernier jour)\b",
    ]),
    ("URG-CANCEL", "Cancellation before packing", [
        r"\bcancel (my |the )?order\b", r"\bjust ordered\b.{0,60}\b(cancel|mistake|wrong)\b",
        r"\bordered by (mistake|accident)\b",
        r"\bbestelling annuleren\b", r"\bnet besteld\b", r"\bper ongeluk besteld\b",
        r"\bannuler (ma |la )?commande\b", r"\bje viens de commander\b",
    ]),
    ("URG-DISPUTE-DEADLINE", "Dispute / chargeback deadline running", [
        r"\b(dispute|chargeback|claim)\b.{0,40}\b(tomorrow|today|deadline|24 ?h)\b",
        r"\b(tomorrow|today|deadline)\b.{0,40}\b(dispute|chargeback)\b",
        r"\bwill (contact|call) my bank\b", r"\bfiling (a )?(claim|dispute)\b",
        r"\bmorgen\b.{0,40}\b(bank|betwist|terugvorder)",
        r"\bdemain\b.{0,40}\b(banque|litige)\b",
    ]),
    ("URG-SECURITY", "Live security / fraud containment", [
        r"\bhappening (right )?now\b.{0,40}\b(fraud|unauthori[sz]ed|charge)\b",
        r"\bsomeone (is )?using my (card|account)\b",
        r"\bunauthori[sz]ed (charge|payment|transaction)\b",
    ]),
    ("URG-DEADLINE-DATE", "Customer names a hard same-day/next-day deadline", [
        r"\bneed it (by|before) (today|tomorrow)\b", r"\bbefore \d{1,2}\s?(am|pm|h|u)\b",
        r"\bdeadline is\b", r"\bnodig (voor|tegen) (vandaag|morgen)\b",
        r"\bvandaag nog\b", r"\b(liefst|graag|uiterlijk) (vandaag|morgen)\b",
        r"\bvoor (het )?einde van de dag\b",
        r"\bavant (ce soir|demain|la fin de journ[ée]e)\b",
        r"\b(si possible )?aujourd'hui si possible\b",
    ]),
]

# Explicitly ignored: pressure is not urgency (framework rule).
PRESSURE_NOISE = [
    r"\burgent!*\b", r"\basap\b", r"\bimmediately\b", r"\bdringend\b", r"\bspoed\b",
    r"\burgentissime\b", r"\bd[èe]s que possible\b", r"!!+",
]

# Signals that actively argue for the low-value quadrant.
SELF_SERVICE_RULES = [
    ("SS-WISMO", "Routine status check inside the promised window", [
        r"\bwhere is my (package|parcel|order)\b", r"\btracking (number|link)\b",
        r"\bany update\b", r"\bstatus of my order\b",
        r"\bwaar is mijn (pakket|bestelling)\b", r"\bstatus van mijn bestelling\b",
        r"\bo[uù] est ma commande\b", r"\bsuivi de (ma )?commande\b",
    ]),
    ("SS-INFO", "Informational / policy / how-to question", [
        r"\bwhat are your (return|shipping|delivery) (conditions|policy|terms)\b",
        r"\bhow (do i|to) (apply|use)\b", r"\bhow long does (shipping|delivery) take\b",
        r"\bdo you ship to\b", r"\bopening hours\b",
        r"\bhoe (breng ik|gebruik ik|pas ik)\b", r"\bretourvoorwaarden\b",
        r"\bcomment (appliquer|utiliser)\b", r"\bconditions de retour\b",
    ]),
    ("SS-INVOICE", "Simple invoice / document request", [
        r"\binvoice\b", r"\breceipt\b", r"\bfactuur\b", r"\bfacture\b", r"\bbon de commande\b",
    ]),
]

TAGS = {
    1: {
        "tag": "RESOLVE NOW", "emoji": "🔴", "quadrant": "Important & Urgent",
        "reply_sla_minutes": 30, "resolve_sla_minutes": 120,
        "owner": "Andrea", "action": "Handle immediately; escalate where needed",
    },
    2: {
        "tag": "INVESTIGATE & FOLLOW UP", "emoji": "🟡", "quadrant": "Important & Not Urgent",
        "reply_sla_minutes": 240, "resolve_sla_minutes": 720,
        "owner": "VA", "action": "Assign owner, investigate, follow up within SLA",
    },
    3: {
        "tag": "ROUTE OR AUTOMATE", "emoji": "🔵", "quadrant": "Not Important & Urgent",
        "reply_sla_minutes": 60, "resolve_sla_minutes": 240,
        "owner": "VA", "action": "Saved reply, automated flow, or route to the right queue",
    },
    4: {
        "tag": "CLOSE / SELF-SERVICE", "emoji": "⚪", "quadrant": "Not Important & Not Urgent",
        "reply_sla_minutes": 720, "resolve_sla_minutes": 1440,
        "owner": "VA", "action": "Self-service content, merge into open ticket, archive",
    },
}

# VA-delegation exceptions: important-but-not-urgent work Andrea must still decide.
ESCALATION_RULES = [
    ("ESC-REFUND-50", "Refund/compensation over €50 — Andrea decides",
     lambda e, m: _num(e, "refund_amount_eur") is not None
     and _num(e, "refund_amount_eur") > THRESHOLDS["important_refund_eur"]),
    ("ESC-VIP", "VIP or >€150 order — Andrea decides",
     lambda e, m: bool(e.get("vip")) or (_num(e, "order_value_eur") or 0) >
     THRESHOLDS["important_order_value_eur"]),
    ("ESC-LEGAL", "Chargeback, legal or formal dispute — Andrea decides",
     lambda e, m: "IMP-CHARGEBACK" in m),
    ("ESC-FRAUD", "Data privacy, account access or fraud — Andrea decides",
     lambda e, m: "IMP-FRAUD" in m),
    ("ESC-SYSTEMIC", "Systemic issue on 3+ orders — Andrea decides",
     lambda e, m: (_num(e, "orders_affected") or 0) >= THRESHOLDS["important_batch_orders"]
     or "IMP-SYSTEMIC" in m),
    ("ESC-PRICING", "Wholesale / B2B / custom colour / quote pricing — Andrea decides",
     lambda e, m: "IMP-VIP" in m),
]


def _num(email, key):
    """Return a numeric field as float, or None when absent/unparseable."""
    value = email.get(key)
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _text(email):
    return "{}\n{}".format(email.get("subject") or "", email.get("body") or "")


def _overdue(email):
    """Days overdue: the structured field wins, otherwise read it out of the text."""
    value = _num(email, "days_overdue")
    if value is not None:
        return value
    match = DAYS_OVERDUE_RE.search(_text(email))
    return float(match.group(1)) if match else None


def _match_rules(text, rules):
    hits = []
    for rule_id, description, patterns in rules:
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                hits.append({"rule": rule_id, "why": description, "matched": pattern})
                break
    return hits


def _structured_important(email):
    hits = []
    order_value = _num(email, "order_value_eur")
    if order_value is not None and order_value >= THRESHOLDS["important_order_value_eur"]:
        hits.append({"rule": "IMP-VALUE", "why": "Order value >= €{}".format(
            THRESHOLDS["important_order_value_eur"]), "matched": "order_value_eur={}".format(order_value)})
    refund = _num(email, "refund_amount_eur")
    if refund is not None and refund > THRESHOLDS["important_refund_eur"]:
        hits.append({"rule": "IMP-REFUND-VALUE", "why": "Refund over €{}".format(
            THRESHOLDS["important_refund_eur"]), "matched": "refund_amount_eur={}".format(refund)})
    overdue = _overdue(email)
    if overdue is not None and overdue >= THRESHOLDS["important_delay_days"]:
        hits.append({"rule": "IMP-DELAY", "why": "Delay >= {} business days".format(
            THRESHOLDS["important_delay_days"]), "matched": "days_overdue={}".format(overdue)})
    affected = _num(email, "orders_affected")
    if affected is not None and affected >= THRESHOLDS["important_batch_orders"]:
        hits.append({"rule": "IMP-BATCH", "why": "Batch issue affecting >= {} orders".format(
            THRESHOLDS["important_batch_orders"]), "matched": "orders_affected={}".format(affected)})
    if email.get("vip"):
        hits.append({"rule": "IMP-VIP-FLAG", "why": "VIP / repeat customer", "matched": "vip=true"})
    return hits


def _structured_urgent(email):
    hits = []
    status = (email.get("delivery_status") or "").strip().lower().replace(" ", "_")
    if status in ("out_for_delivery", "delivery_today"):
        hits.append({"rule": "URG-STATUS", "why": 'Delivery status is "{}"'.format(status),
                     "matched": "delivery_status={}".format(status)})
    if status == "pre_dispatch":
        hits.append({"rule": "URG-INTERCEPTABLE", "why": "Parcel not dispatched — intercept still possible",
                     "matched": "delivery_status=pre_dispatch"})
    cutoff = _num(email, "hours_to_cutoff")
    if cutoff is not None and cutoff <= THRESHOLDS["urgent_cutoff_hours"]:
        hits.append({"rule": "URG-CUTOFF", "why": "Carrier / pickup cutoff within {}h".format(
            THRESHOLDS["urgent_cutoff_hours"]), "matched": "hours_to_cutoff={}".format(cutoff)})
    dispute = _num(email, "hours_to_dispute_deadline")
    if dispute is not None and dispute <= THRESHOLDS["urgent_dispute_hours"]:
        hits.append({"rule": "URG-DISPUTE", "why": "Payment / dispute deadline within {}h".format(
            THRESHOLDS["urgent_dispute_hours"]), "matched": "hours_to_dispute_deadline={}".format(dispute)})
    if email.get("outage_active"):
        hits.append({"rule": "URG-OUTAGE", "why": "Active system or store outage",
                     "matched": "outage_active=true"})
    return hits


DAYS_OVERDUE_RE = re.compile(
    r"\b(\d{1,3})\s*(?:business\s*)?(?:days?|dagen|jours?)\b[^.\n]{0,20}"
    r"\b(overdue|late|delay|te laat|vertraging|retard)\b", re.IGNORECASE)
URGENT_DELAY_DAYS = 7  # beyond this the churn/cancellation clock is the deadline


def _derived_urgent(email, important_hits):
    """Urgency the framework's worked examples imply but the literal rules don't state."""
    hits = []
    important_ids = {h["rule"] for h in important_hits}

    overdue = _overdue(email)
    if overdue is not None and overdue >= URGENT_DELAY_DAYS:
        hits.append({"rule": "URG-SEVERE-DELAY",
                     "why": "Delay of {:.0f} days — cancellation / churn risk now".format(overdue),
                     "matched": "days_overdue>={}".format(URGENT_DELAY_DAYS)})

    if "IMP-MISDELIVERY" in important_ids:
        hits.append({"rule": "URG-MISDELIVERY",
                     "why": "Misdelivery — carrier recovery window is short",
                     "matched": "derived from IMP-MISDELIVERY"})
    return hits


def _sla_deadlines(email, priority):
    received = email.get("received_at")
    if not received:
        return {}
    try:
        stamp = datetime.fromisoformat(str(received).replace("Z", "+00:00"))
    except ValueError:
        return {}
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    spec = TAGS[priority]
    return {
        "reply_due": (stamp + timedelta(minutes=spec["reply_sla_minutes"])).isoformat(),
        "resolve_due": (stamp + timedelta(minutes=spec["resolve_sla_minutes"])).isoformat(),
    }


def triage(email):
    """Classify one email. Pure function — same input, same output."""
    text = _text(email)

    important_hits = _match_rules(text, IMPORTANT_RULES) + _structured_important(email)
    urgent_hits = (_match_rules(text, URGENT_RULES) + _structured_urgent(email)
                   + _derived_urgent(email, important_hits))
    self_service_hits = _match_rules(text, SELF_SERVICE_RULES)
    pressure_hits = [p for p in PRESSURE_NOISE if re.search(p, text, re.IGNORECASE)]

    notes = []

    # Duplicate on an open ticket → merge, never important or urgent.
    if email.get("duplicate_of"):
        notes.append("Duplicate of {} — merge into the open thread.".format(email["duplicate_of"]))
        important_hits, urgent_hits = [], []

    # Bulk / promotional mail is not customer work at all.
    if email.get("bulk"):
        notes.append("Bulk or promotional mail — archive; not customer work.")
        important_hits, urgent_hits = [], []

    # Pressure words are recorded, never scored (framework rule).
    if pressure_hits and not urgent_hits:
        notes.append("Pressure wording ignored ({}) — no time-bound dependency found.".format(
            ", ".join(sorted({p.strip('\\b') for p in pressure_hits}))))

    # A pure WISMO/info question with no importance signal stays self-service.
    if self_service_hits and not important_hits:
        notes.append("Self-service signal: {}.".format(
            "; ".join(sorted({h["why"] for h in self_service_hits}))))

    important = bool(important_hits)
    urgent = bool(urgent_hits)

    if important and urgent:
        priority = 1
    elif important:
        priority = 2
    elif urgent:
        priority = 3
    else:
        priority = 4

    matched_ids = {h["rule"] for h in important_hits + urgent_hits}
    escalations = [{"rule": rid, "why": why}
                   for rid, why, test in ESCALATION_RULES if test(email, matched_ids)]

    # Confidence: structured fields are hard evidence, keywords are inference.
    structured = any(h["rule"].endswith(("VALUE", "FLAG", "STATUS", "CUTOFF", "DISPUTE",
                                         "OUTAGE", "BATCH", "DELAY", "INTERCEPTABLE"))
                     for h in important_hits + urgent_hits)
    if structured:
        confidence = "high"
    elif important_hits or urgent_hits or self_service_hits:
        confidence = "medium"
    else:
        confidence = "low"

    needs_review = (confidence == "low" and not email.get("duplicate_of")
                    and not email.get("bulk"))
    if needs_review:
        notes.append("No rule fired — defaulted to priority 4. Read this one manually.")

    spec = TAGS[priority]
    result = {
        "id": email.get("id"),
        "from": email.get("from"),
        "subject": email.get("subject"),
        "order_ref": email.get("order_ref"),
        "priority": priority,
        "tag": spec["tag"],
        "emoji": spec["emoji"],
        "quadrant": spec["quadrant"],
        "important": important,
        "urgent": urgent,
        "owner": "Andrea" if (priority == 1 or escalations) else spec["owner"],
        "action": spec["action"],
        "reply_sla_minutes": spec["reply_sla_minutes"],
        "resolve_sla_minutes": spec["resolve_sla_minutes"],
        "escalate_to_andrea": bool(escalations),
        "escalations": escalations,
        "important_rules": important_hits,
        "urgent_rules": urgent_hits,
        "confidence": confidence,
        "needs_human_review": needs_review,
        "notes": notes,
    }
    result.update(_sla_deadlines(email, priority))
    return result


def _load(path):
    raw = sys.stdin.read() if path in (None, "-") else open(path, encoding="utf-8").read()
    if not raw.strip():
        sys.exit("triage.py: no input received")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        sys.exit("triage.py: input is not valid JSON ({})".format(exc))
    if isinstance(data, dict):
        data = data.get("emails", [data]) if "emails" in data else [data]
    if not isinstance(data, list):
        sys.exit("triage.py: expected an email object or a list of them")
    return data


def _render_table(results):
    lines = [
        "| # | Priority | Tag | Owner | Reply SLA | Subject | Why |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(results, 1):
        why = "; ".join(h["why"] for h in r["important_rules"] + r["urgent_rules"]) or \
            (r["notes"][0] if r["notes"] else "no signal")
        flag = " ⚠️" if r["escalate_to_andrea"] else ("" if not r["needs_human_review"] else " ❓")
        lines.append("| {} | {} | {} {}{} | {} | {} min | {} | {} |".format(
            i, r["priority"], r["emoji"], r["tag"], flag, r["owner"],
            r["reply_sla_minutes"], (r["subject"] or "")[:60].replace("|", "/"),
            why[:110].replace("|", "/")))
    return "\n".join(lines)


def _render_csv(results, out):
    fields = ["id", "from", "subject", "order_ref", "priority", "tag", "quadrant", "important", "urgent",
              "owner", "reply_sla_minutes", "resolve_sla_minutes", "reply_due", "resolve_due",
              "escalate_to_andrea", "confidence", "needs_human_review"]
    writer = csv.DictWriter(out, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    for r in results:
        writer.writerow(r)


def main():
    parser = argparse.ArgumentParser(description="Triage customer emails (Eisenhower matrix).")
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    parser.add_argument("--format", choices=["json", "table", "csv"], default="json")
    parser.add_argument("--sort", action="store_true", help="sort output by priority")
    args = parser.parse_args()

    results = [triage(e) for e in _load(args.input)]
    if args.sort:
        results.sort(key=lambda r: (r["priority"], not r["escalate_to_andrea"]))

    if args.format == "json":
        json.dump(results, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    elif args.format == "table":
        print(_render_table(results))
    else:
        _render_csv(results, sys.stdout)


if __name__ == "__main__":
    main()
