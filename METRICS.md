# Diff Lab offers — engagement metrics

Low-noise funnel for https://ds-code-t.github.io/endoglyph-diff-offers/

**Stack:** GoatCounter (free, privacy-light, no cookies / no ad pixels).  
**Dashboard:** https://endoglyph-diff.goatcounter.com/  
**Site code:** `endoglyph-diff`  
**Login email:** dan.shell.80@gmail.com  
(Password: see `/workspace/diff-lab/ops/goatcounter-credentials.txt` on the box.)

Silent analytics only — no customer-facing “tracking” copy.

## What we measure

| Signal | How it shows in GoatCounter |
| --- | --- |
| Pageviews (hub / doors / about) | Paths: `/`, `/index.html`, `/nogales-crossing-truth.html`, `/pistachio-dual-gate.html`, `/about.html` (under the GitHub Pages project path) |
| Which door (hub) | Events: `door-nogales`, `door-pistachio` |
| Subscribe CTA clicks | Events: `cta-subscribe-nogales`, `cta-subscribe-pistachio` |
| Checkout starts / payments | **Not** in GoatCounter — use Stripe |

Stripe Payment Links (unchanged):

- Nogales: https://buy.stripe.com/14A4gBa6E7aa6pMcbU5Rm00
- Pistachio: https://buy.stripe.com/eVq28tgv2cuu3dA6RA5Rm01

## Weekly read (10 minutes)

1. Open https://endoglyph-diff.goatcounter.com/ → set range to **Last week**.
2. **Views / paths** — hub vs Door A vs Door B vs about. Doors should be readable from path titles.
3. **Referrers** — where traffic came from (direct, X, email, etc.).
4. **Events** — filter `is:event` (or look for paths without a leading `/`):
   - `door-nogales` / `door-pistachio` = which door from hub
   - `cta-subscribe-nogales` / `cta-subscribe-pistachio` = Subscribe CTA clicks before Stripe
5. **Stripe Dashboard → Payment Links** — checkout starts and successful payments for each link. That is the money funnel; GoatCounter only covers the static-site side.

Rough funnel: hub views → door events / door pageviews → CTA events → Stripe Payment Link starts → paid.

## What NOT to obsess over

- **First 48 hours bot / crawler noise** after publish or sharing a link. Ignore weird spikes from GitHub, scrapers, and one-off probes.
- Unique-visitor precision (GoatCounter is intentionally privacy-light).
- Bounce rate theater, session recordings, heatmaps.
- Comparing to GA-style vanity metrics — we only need: traffic → door → CTA → Stripe.

## Ops notes

- Embed: `data-goatcounter="https://endoglyph-diff.goatcounter.com/count"` + `//gc.zgo.at/count.js` on all public HTML pages.
- CTA / door clicks use `data-goatcounter-click` (fires on click before navigation).
- If GoatCounter ever fails hard, fallback candidates (still $0): another free privacy-light counter that works on static GitHub Pages (e.g. Umami cloud free). Do **not** add paid tools, ad pixels, or cookie-heavy GA unless GoatCounter is dead.
- Credentials stay ops-only; do not commit passwords into the public Pages repo.
