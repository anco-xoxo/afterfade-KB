#!/usr/bin/env python3
"""Regression test: the 11 worked examples from the framework must classify as documented.

Run: python3 test_triage.py
"""
import sys

from triage import triage

# (subject/body, structured fields, expected priority) — taken verbatim from
# Andrea/Customer_Email_Priority_Triage_Framework.md § Classification Examples.
CASES = [
    ("01", "Order AF-2614 is 11 days overdue, please update me.", {"days_overdue": 11}, 1),
    ("02", "PostNL is delivering today, but the street number is wrong.", {}, 1),
    ("03", "My parcel was delivered to the wrong city.", {}, 1),
    ("04", "My parcel was returned to the pickup point; can you resend it?", {}, 2),
    ("05", "I want to return my order, please send a return label.", {}, 2),
    ("06", "Can I change delivery from pickup point to my home address?",
     {"delivery_status": "pre_dispatch"}, 3),
    ("07", "Where is my package?", {}, 4),
    ("08", "What are your return conditions?", {}, 4),
    ("09", "Any update??", {"duplicate_of": "AF-1189"}, 4),
    ("10", "I was charged twice and will dispute it tomorrow.", {}, 1),
    ("11", "Can you send me an invoice for my order?", {}, 4),
    # Framework rule: pressure is not urgency.
    ("P1", "URGENT!!! What are your return conditions?", {}, 4),
    # Framework rule: calm high-value inquiry is important.
    ("P2", "Hi, just checking in on my order.", {"order_value_eur": 220}, 2),
    # Past-tense narration is not a delivery deadline (damaged goods = P2, not P1).
    ("P3", "The box arrived this morning and one bottle is broken and leaking.", {}, 2),
    # Framework example 11: invoice WITH an explicit same-day deadline is P3 (NL wording).
    ("P4", "Kan ik een factuur krijgen voor AF-2690? Liefst vandaag nog.", {}, 3),
    # ...and without one it stays P4.
    ("P5", "Kan ik een factuur krijgen voor bestelling AF-2690?", {}, 4),
    # Bulk/promotional mail is archived, not flagged for review.
    ("P6", "Webinar invitation: new carrier rates", {"bulk": True}, 4),
]

failures = []
for case_id, text, fields, expected in CASES:
    email = dict(fields, subject=text, body="")
    got = triage(email)["priority"]
    status = "ok " if got == expected else "FAIL"
    if got != expected:
        failures.append((case_id, expected, got, text))
    print("{} {}  expected P{} got P{}  {}".format(status, case_id, expected, got, text[:60]))

if failures:
    print("\n{} failing case(s)".format(len(failures)))
    sys.exit(1)
print("\nAll {} cases pass.".format(len(CASES)))
