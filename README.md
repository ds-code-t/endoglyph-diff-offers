# EndoGlyph Diff Lab — customer offer pages

Static customer-facing seats for **Door A** (Nogales Crossing Truth) and **Door B** (Pistachio Dual Gate).

Brand: **EndoGlyph Diff Lab** / proprietary watches. Company: **EndoGlyph LLC**.

## Files

| Path | Role |
|------|------|
| `index.html` | Hub linking both doors |
| `nogales-crossing-truth.html` | Door A offer |
| `pistachio-dual-gate.html` | Door B offer |
| `assets/style.css` | Shared styles |
| `FULFILLMENT.md` | Paid → deliver (weekly digest) |

## Publish

Any static host works (S3+CloudFront, Netlify, GitHub Pages, nginx root).

```bash
# Example: serve locally to preview
cd /workspace/diff-lab/offers
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Point the public origin at this directory (or sync these files into your web root under `/offers/`).

## Paste Stripe Payment Link URLs

CTAs are mid-band **$999/mo** seat placeholders:

1. Create two Stripe **Payment Links** (or Prices + Payment Links) for recurring $999/mo.
   - Collect **customer email** at checkout (Stripe default).
   - Product names: `Nogales Crossing Truth — seat` and `Pistachio Dual Gate — seat`.
2. Open each offer HTML and replace the subscribe button `href`:

```html
<!-- Door A — nogales-crossing-truth.html -->
<a class="btn-subscribe" id="payment" href="PASTE_STRIPE_PAYMENT_LINK_A"
   data-door="a" data-price="999" data-product="nogales-crossing-truth">
  Subscribe — $999/mo seat
</a>

<!-- Door B — pistachio-dual-gate.html -->
<a class="btn-subscribe" id="payment" href="PASTE_STRIPE_PAYMENT_LINK_B"
   data-door="b" data-price="999" data-product="pistachio-dual-gate">
  Subscribe — $999/mo seat
</a>
```

Keep `data-door="a"|"b"` so fulfillment scripts can map payment → door.

Until live links are pasted, `href="#payment"` is intentional (no accidental charge).

Custom setup ($3k–5k) is invoice / separate Payment Link — not on these seat buttons.

## Copy rules (black-box)

- No “bot,” no automation theater, no fake human-analyst claims.
- No SoftPro. No invented testimonials or fake metrics.
- Source briefs: idea-foundry `DIFF_LAB_OFFER_A.md` / `DIFF_LAB_OFFER_B.md`.

## After a paid seat

See **`FULFILLMENT.md`**.

## Live Payment Links (test mode — 2026-09-06)

- Door A Nogales: https://buy.stripe.com/14A4gBa6E7aa6pMcbU5Rm00
- Door B Pistachio: https://buy.stripe.com/eVq28tgv2cuu3dA6RA5Rm01

These are Stripe **live** links (EndoGlyph LLC sandbox). Replace with live-mode Payment Links after account activation / bank link for real charges.
