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
| Pageviews (hub / doors / about) | Paths: `/`, `/index.html`, `/nogales-crossing-truth.html`, `/pistachio-dual-gate.html`, bait slugs (`/spearmint-mint-oil-mo.html`, `/wi-ginseng-shipment.html`, `/fluorspar-acidspar-hf.html`, `/seed-onion-state-cert.html`, `/lcfs-pathway-suspend.html`, `/dea-apq-api-production.html`), `/about.html` (under the GitHub Pages project path) |
| Which door (hub) | Events: `door-nogales`, `door-pistachio`, `door-spearmint`, `door-ginseng`, `door-fluorspar`, `door-allium`, `door-lcfs`, `door-dea-apq` |
| Subscribe CTA clicks | Events: `cta-subscribe-nogales`, `cta-subscribe-pistachio`, `cta-subscribe-spearmint-mint-oil-mo`, `cta-subscribe-wi-ginseng-shipment`, `cta-subscribe-fluorspar-acidspar-hf`, `cta-subscribe-seed-onion-state-cert`, `cta-subscribe-lcfs-pathway-suspend`, `cta-subscribe-dea-apq-api-production` |
| Checkout starts / payments | **Not** in GoatCounter — use Stripe |

Stripe Payment Links (live):

- Nogales: https://buy.stripe.com/14A4gBa6E7aa6pMcbU5Rm00
- Pistachio: https://buy.stripe.com/eVq28tgv2cuu3dA6RA5Rm01
- M459 Spearmint: https://buy.stripe.com/eVq28tceMdy29w7VE5Rm05
- M485 WI ginseng: https://buy.stripe.com/7sY3cx4Mk8eebK65Nw5Rm04
- M524 Fluorspar: https://buy.stripe.com/dRm7sN0w46665lIdfY5Rm03
- M543 Seed-onion: https://buy.stripe.com/dRm28tdiQeCC5lIdfY5Rm02
- M633 LCFS: https://buy.stripe.com/8x2eVfgv2dyybk63Fo5Rm06
- M664 DEA APQ: https://buy.stripe.com/bJe3cx7Yw6666pMfo65Rm07

## Weekly read (10 minutes)

1. Open https://endoglyph-diff.goatcounter.com/ → set range to **Last week**.
2. **Views / paths** — hub vs Door A vs Door B vs about. Doors should be readable from path titles.
3. **Referrers** — where traffic came from (direct, X, email, etc.).
4. **Events** — filter `is:event` (or look for paths without a leading `/`):
   - `door-nogales` / `door-pistachio` / bait `door-*` = which door from hub
   - `cta-subscribe-nogales` / `cta-subscribe-pistachio` / bait `cta-subscribe-*` = Subscribe CTA clicks before Stripe
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


## New door checklist (HARD — every public offer)

Before a door is “live” on Pages, it MUST have:

1. GoatCounter script on the page:
   `data-goatcounter="https://endoglyph-diff.goatcounter.com/count"` + `//gc.zgo.at/count.js`
2. `data-goatcounter-click` on Subscribe / door CTAs (unique event name per door, e.g. `cta-subscribe-spearmint`)
3. Hub `index.html` card link to the new page
4. `sitemap.xml` + `robots.txt` still allowing crawl
5. Stripe Payment Link (when money path is on) — track checkouts in Stripe Dashboard
6. Copy template from `offers/_door_template.html` when adding HTML

Invent / MARKET_PASS / proto folders without a customer offer page are **out of scope** for GoatCounter until an offer page ships.


## Google Search Console
- Account: `endoglyphllc@gmail.com`
- Property: https://ds-code-t.github.io/endoglyph-diff-offers/
- Sitemap: https://ds-code-t.github.io/endoglyph-diff-offers/sitemap.xml (submitted 2026-09-06)
- Use for search impressions/clicks once data appears (can lag days).


## Related
Ops modes + prune: `BAIT_POLICY.md`.
