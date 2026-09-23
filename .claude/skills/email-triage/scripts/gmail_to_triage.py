#!/usr/bin/env python3
"""Convert Gmail MCP / Gmail API message data into triage.py input.

Handles the full Gmail `users.messages.get` resource (base64url MIME parts,
header lists, threadId, labelIds) and the flattened shape some MCP servers
return instead. Emits a JSON list ready for triage.py.

Usage:
    python3 gmail_to_triage.py inbox.json | python3 triage.py - --format table --sort
    python3 gmail_to_triage.py inbox.json > triage-input.json
"""

import argparse
import base64
import json
import re
import sys
from datetime import datetime, timezone

# Gmail label names that carry triage meaning. Ids like "Label_7" are opaque,
# so we read the resolved names most MCP servers include alongside them.
VIP_LABELS = {"vip", "wholesale", "b2b", "trade"}
BULK_LABELS = {"category_promotions", "category_updates", "category_forums",
               "category_social", "promotions", "newsletters", "spam"}

QUOTED_LINE = re.compile(r"^\s*>.*$", re.MULTILINE)
QUOTE_HEADER = re.compile(
    r"\n\s*(on .{0,120}wrote:|op .{0,120}schreef:|le .{0,120}a écrit ?:|"
    r"-{2,}\s*(original message|forwarded message)\s*-{2,}|"
    r"_{10,}|from:\s.+\nsent:\s)", re.IGNORECASE)
SIGNATURE = re.compile(r"\n--\s*\n.*\Z", re.DOTALL)
TAGS_RE = re.compile(r"<[^>]+>")
ORDER_RE = re.compile(r"\bAF[-\s]?(\d{3,6})\b", re.IGNORECASE)


def _b64(data):
    if not data:
        return ""
    padded = data + "=" * (-len(data) % 4)
    try:
        return base64.urlsafe_b64decode(padded.encode("ascii")).decode("utf-8", "replace")
    except (ValueError, UnicodeDecodeError):
        return ""


def _headers(payload):
    return {h.get("name", "").lower(): h.get("value", "")
            for h in (payload or {}).get("headers", [])}


def _walk(part, wanted, found):
    """Depth-first collect of decoded bodies for a mime type."""
    if not part:
        return
    if part.get("mimeType") == wanted:
        text = _b64((part.get("body") or {}).get("data"))
        if text:
            found.append(text)
    for child in part.get("parts", []) or []:
        _walk(child, wanted, found)


def _body(message):
    """Best-effort plain-text body: text/plain wins, HTML is stripped as fallback."""
    payload = message.get("payload") or {}
    plain = []
    _walk(payload, "text/plain", plain)
    if not plain:
        html = []
        _walk(payload, "text/html", html)
        plain = [TAGS_RE.sub(" ", h) for h in html]
    if not plain:
        # Flattened MCP shapes put the text straight on the message.
        for key in ("body", "text", "plainText", "bodyText", "snippet"):
            if message.get(key):
                plain = [str(message[key])]
                break
    text = "\n".join(plain)
    return _strip_quotes(text)


def _strip_quotes(text):
    """Drop the quoted thread so an old P1 message can't re-trigger on a 'Any update?' reply."""
    text = QUOTE_HEADER.split(text)[0]
    text = QUOTED_LINE.sub("", text)
    text = SIGNATURE.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _received(message, headers):
    stamp = message.get("internalDate")
    if stamp:
        try:
            return datetime.fromtimestamp(int(stamp) / 1000, timezone.utc).isoformat()
        except (ValueError, OSError):
            pass
    raw = headers.get("date") or message.get("date") or ""
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%d %b %Y %H:%M:%S %z"):
        try:
            return datetime.strptime(raw.split(" (")[0].strip(), fmt).isoformat()
        except ValueError:
            continue
    return None


def convert(messages):
    """Gmail messages (oldest first within a thread) -> triage.py input objects."""
    seen_threads = {}
    out = []
    for message in messages:
        payload = message.get("payload") or {}
        headers = _headers(payload)
        subject = headers.get("subject") or message.get("subject") or ""
        sender = headers.get("from") or message.get("from") or ""
        body = _body(message)

        labels = {str(l).lower() for l in
                  (message.get("labels") or []) + (message.get("labelIds") or [])}

        email = {
            "id": message.get("id"),
            "from": sender,
            "subject": subject,
            "body": body,
        }
        received = _received(message, headers)
        if received:
            email["received_at"] = received

        order = ORDER_RE.search("{}\n{}".format(subject, body))
        if order:
            email["order_ref"] = "AF-{}".format(order.group(1))

        if labels & VIP_LABELS:
            email["vip"] = True
        if labels & BULK_LABELS:
            email["bulk"] = True

        # Second and later inbound messages on one thread are follow-up chasers.
        thread = message.get("threadId") or message.get("thread_id")
        if thread:
            if thread in seen_threads:
                email["duplicate_of"] = seen_threads[thread]
            else:
                seen_threads[thread] = message.get("id")

        out.append(email)
    return out


def _load(path):
    raw = sys.stdin.read() if path in (None, "-") else open(path, encoding="utf-8").read()
    if not raw.strip():
        sys.exit("gmail_to_triage.py: no input received")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        sys.exit("gmail_to_triage.py: input is not valid JSON ({})".format(exc))
    if isinstance(data, dict):
        for key in ("messages", "emails", "results", "data"):
            if isinstance(data.get(key), list):
                return data[key]
        return [data]
    if isinstance(data, list):
        return data
    sys.exit("gmail_to_triage.py: expected a Gmail message list")


def main():
    parser = argparse.ArgumentParser(description="Gmail message data -> triage.py input.")
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    args = parser.parse_args()
    json.dump(convert(_load(args.input)), sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
