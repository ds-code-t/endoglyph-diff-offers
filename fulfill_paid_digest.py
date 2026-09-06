#!/usr/bin/env python3
"""v1 fulfillment helper: build a weekly digest email body from door ALERT_SAMPLE.md.

Usage (manual after Stripe email arrives):
  python3 fulfill_paid_digest.py a buyer@example.com
  python3 fulfill_paid_digest.py b buyer@example.com

Does not send mail by itself — prints a ready-to-send body (or writes under out/).
Wire SMTP / Stripe webhook later; never invent alert content.
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
PT = ZoneInfo("America/Phoenix")
DOORS = {
    "a": ROOT / "door-a" / "sample_output" / "ALERT_SAMPLE.md",
    "b": ROOT / "door-b" / "sample_output" / "ALERT_SAMPLE.md",
}
OUT = Path(__file__).resolve().parent / "out"


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: fulfill_paid_digest.py a|b buyer@email", file=sys.stderr)
        return 2
    door, email = sys.argv[1].lower(), sys.argv[2]
    path = DOORS.get(door)
    if not path:
        print("door must be a or b", file=sys.stderr)
        return 2
    if not path.exists():
        print(f"missing {path}", file=sys.stderr)
        return 1
    body = path.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).astimezone(PT).strftime("%Y-%m-%d %H:%M %Z")
    title = "Nogales Crossing Truth" if door == "a" else "Pistachio Dual Gate"
    msg = (
        f"To: {email}\n"
        f"Subject: EndoGlyph Diff Lab — {title} weekly digest\n\n"
        f"EndoGlyph Diff Lab proprietary watch digest ({title})\n"
        f"Generated: {now}\n\n"
        f"{body}\n"
        f"— EndoGlyph LLC\n"
    )
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"digest_{door}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.txt"
    out.write_text(msg, encoding="utf-8")
    print(msg)
    print(f"\n# wrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
