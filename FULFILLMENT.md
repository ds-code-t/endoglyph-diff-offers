# Diff Lab offers — fulfillment (v1)

Minimal paid → deliver path. Manual or scripted is fine for v1.

## Trigger

Buyer completes Stripe Payment Link for Door A or Door B ($999/mo seat mid-band).

Stripe collects **email** at checkout. That email is the delivery address.

## What to deliver

**Weekly digest** for their door — not a live dashboard login in v1.

| Door | Source material |
|------|-----------------|
| A — Nogales Crossing Truth | `/workspace/diff-lab/door-a/sample_output/ALERT_SAMPLE.md` and/or latest run output; cross-check `/workspace/diff-lab/last_run_summary.md` |
| B — Pistachio Dual Gate | `/workspace/diff-lab/door-b/sample_output/ALERT_SAMPLE.md` and/or latest run output; cross-check `/workspace/diff-lab/last_run_summary.md` |

Refresh sources by running:

```bash
python3 /workspace/diff-lab/run_all.py
```

Then email the buyer a short digest: what fired (or why quiet), caveats from the sample, timestamp. Prefer the door’s `ALERT_SAMPLE.md` body over inventing narrative.

Optional later: filter Door B digests to the buyer’s supplier list (collected once after payment).

## v1 ops path (manual)

1. Stripe payment → note email + which door (`data-door` / product name).
2. Add row to a simple roster (spreadsheet or `offers/buyers.csv`):
   - `email`, `door` (`a`|`b`), `started`, `status=active`
3. Weekly (or after each `run_all.py`):
   - For each active buyer, attach/paste that door’s latest `ALERT_SAMPLE.md` (or a trimmed digest).
   - Subject example: `EndoGlyph Diff Lab — Door A weekly digests` / `Door B weekly digests`.
4. On cancel / failed payment: mark roster inactive; stop sending.

## v1 ops path (script sketch)

OK to automate later:

1. Stripe webhook `checkout.session.completed` / `invoice.paid` → append buyer email + door to roster.
2. Cron after `run_all.py` → for each active seat, send digest from that door’s `ALERT_SAMPLE.md` + `last_run_summary.md` line.
3. No need for customer accounts in v1.

## Human leftovers (once)

- Approve Stripe / ToS before listing live Payment Links.
- Door A: optional commodity / port list once.
- Door B: paste supplier names once.

## Do not

- Promise human analysts or 24/7 desk coverage.
- Invent alert metrics or testimonials.
- Ship SoftPro or unrelated product copy.
- Deliver Door C (or other doors) under these Payment Links without a separate offer.
