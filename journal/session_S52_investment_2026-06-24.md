# Session S52 — Investment — 2026-06-24
**Project:** Pinyo Empire · Investment Portfolio Dashboard
**Date:** 2026-06-24
**Claude Session:** S52 (Investment sub-track)
**Prior Investment Session:** S48-Investment (2026-06-23) — Crypto integration, $246K total
**Dashboard:** ops.radrooster.co (Portfolio tab) · GitHub: Artemisclaws/sharedfolder/dashboard/portfolio.html

---

## The Problem

The portfolio dashboard existed but was lying. The position data came from an old S47 checkpoint — wrong share counts, wrong symbols, wrong accounts, and multiple positions that Chris doesn't actually hold. PLTR was listed as 62 shares; the spreadsheet shows 44.4 total across two accounts. AMZN, AAPL, NVO, DIS appeared as active positions; none are held. NFLX showed 50 shares; the actual holding is 1 share at $93 in the Roth IRA.

Stock prices displayed as $0 or —. The entire "live" dashboard was static noise. The crypto section was missing. STRC was placed in crypto when it belongs in a Fidelity watchlist.

Tab navigation on other pages also broke when the Portfolio tab was added — the nav in index.html didn't include the Portfolio button, so clicking Portfolio from another page destroyed the nav.

---

## Questions We Were Trying to Solve

1. How do we replace the checkpoint fiction with real position data?
2. Why are prices not loading — is it CORS, rate limits, or a structural API change?
3. Where does BTC go? Where does STRC go? (Two different answers.)
4. How many BTC does Chris hold and in what wallet?
5. What does a correct "Next Actions" section look like against real holdings?

---

## What We Tried That Didn't Work

**Yahoo Finance bulk quote endpoint** — the 4-endpoint fallback chain (v8/finance/quote → v7/finance/quote → corsproxy.io → allorigins.win) failed across all four. Root cause: Yahoo Finance now requires a crumb cookie for the bulk quote API. Browser-based `fetch()` cannot obtain the crumb because the crumb endpoint itself has CORS restrictions. Retrying the same endpoint through different proxies doesn't fix a structural auth requirement. More retries = same zero.

**Old S47 checkpoint as data source** — the checkpoint data had been used to build the dashboard originally. It was stale by multiple sessions and significantly wrong on share counts, account assignments, and symbols held. It was not a minor delta — it was a different portfolio.

---

## What We Built

**Complete rebuild of portfolio.html** from the Pinyo_Portfolio_Tracker_v1 Google Sheets ground truth (last synced 2026-06-22). Four account sections, accurate to the spreadsheet:

| Account | ID | Value |
|---------|-----|-------|
| Individual Brokerage | Z31836993 | ~$9,951 |
| Morgan Stanley Managed | Z39168352 | ~$12,981 |
| Roth IRA | 236231244 | ~$52,357 |
| Cash Management TOD | Z28833138 | $12,187 |

**Corrected positions (sample of what changed):**
- PLTR: was 62sh in "MS Trading" → now 32sh brokerage + 12.4sh Roth = 44.4 total
- NFLX: was 50sh → now 1sh in Roth at $93 cost
- GOOGL: was 15sh in "MS Trading" → now 0.5sh in Roth at $307.58 cost
- Added: NVDA 17sh (+78%), META 4sh, UNH 11.5 total, TSLA 4sh across accounts
- Removed: AMZN, AAPL, NVO, DIS (not held)
- Morgan Stanley account: 11 advisor-managed ETFs (SPYM, GSLC, EMGF, IEFA, FNDA, SPMD, GLD, AGG, TSLA, JPME, QEFA) — labeled "Managed, no triggers"

**Crypto section** — added above Fidelity Watchlist:
- BTC · 0.5 coins · Cold wallet · Chris only
- Live price via CoinGecko API
- Golfii's crypto position excluded per security protocol

**STRC** — moved out of crypto, placed in Fidelity Watchlist with BTC-USD safety check alongside it. STRC is not a current holding; it's a conditional buy (war chest + BTC stability threshold).

**Price loading fix** — switched architecture entirely:
- Per-symbol Yahoo Finance chart endpoint: `GET /v8/finance/chart/{SYM}?interval=1d&range=1d`
- 26 parallel fetches via `Promise.allSettled` — no crumb needed, no bulk quota
- BTC via CoinGecko: `simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true`
- Result: all prices load live; P&L columns populate with real data

**Next Actions section** — rebuilt against real holdings:
- PLTR 44.4 total: exit ALL @ $140, stop $105, Sep 30 review
- NVDA 17sh: Free Ride — sell 3 shares at $250+ (up 78%)
- COST 11.4 total: sell 2.8 swing (brokerage) at $960-980, add to Roth at $860 dip
- UNH 11.5 total: trim 4 brokerage shares at $450+ (brokerage basis +44%)
- USO 15sh: hold, review XLE swap at +15%
- SCHD + KO covered calls: ~$180/mo tax-free from Roth IRA (3x SCHD OTM 3.5%, 1x KO OTM 4%)

**Trigger alerts** — live price comparisons against targets:
- PLTR ≥ $140: sell all now · PLTR ≤ $105: exit now · PLTR ≥ $135: prep order
- NVDA ≥ $250: Free Ride rule triggers
- UNH ≥ $450: trim brokerage shares
- COST ≥ $960: sell swing / COST ≤ $870: add to Roth

---

## Key Decisions

**No assumptions on BTC cost basis.** Cold wallet means no Fidelity record. Chris didn't provide it. Dashboard shows live value without P&L rather than inventing a number. Chris can add it anytime.

**STRC is a watchlist item, not a position.** Chris explicitly said so. It lives in the Fidelity Watchlist section alongside a BTC safety check (BTC > $60K = STRC dividend safe; < $50K = at risk).

**Golfii's crypto excluded.** Chris mentioned "the short one is Golfii's" when confirming his BTC. Security protocol: never mix holders. Golfii's position not shown on Chris's dashboard.

**Chart endpoint over bulk quote.** Not a workaround — it's the correct tool. The bulk quote endpoint changed auth requirements. The chart endpoint is what Yahoo's own frontend uses for per-symbol price display. It's more stable, not less.

**Morgan Stanley account labeled "Managed, no triggers."** These are advisor-managed ETFs. Chris doesn't pull the levers here. Showing them for visibility and P&L tracking, but no Next Action tags.

---

## What's Alive Now

- `ops.radrooster.co/portfolio.html` — auto-deployed via Cloudflare Pages on GitHub push
- Portfolio tab embedded in `ops.radrooster.co/index.html` via iframe (same nav pattern as Revenue/Aura Thai)
- 4 Fidelity accounts + Crypto + Fidelity Watchlist sections
- Live prices: 26 equity/ETF symbols via Yahoo Finance chart API + BTC via CoinGecko
- 5-minute auto-refresh with countdown timer
- Trigger alerts firing against real price targets
- Covered calls section with live strike price calculation
- War chest progress bar ($63K / $150K = 42%) and hard assets tracker (gold 5oz, silver 60oz)

**GitHub SHA after final push:** `6632f3a20ccff5c2e4311f0635db630d491b236b`

---

## What's Next

- **BTC cost basis** — Chris to provide; unlocks P&L column for crypto section
- **S50 options income** — cash-secured puts strategy (enter positions at target price, collect premium); covered call income optimization; monthly income setup
- **Perplexity Search API integration** — S49 carry-forward
- **Trust/ILIT framework** — S49 carry-forward, currently in-progress
- **EMPIRE_STATUS.md** — portfolio section doesn't exist yet; add it with ops.radrooster.co/portfolio.html as live system
- **BTC cycle thesis** (memory: ATL ~Oct 6, 2026, ~105 days out) — accumulation window note in watchlist section

---

## Tone Note

Chris came in mid-session after the context window had already been exhausted rebuilding the dashboard from scratch. He had two specific, verifiable complaints: crypto missing, prices not live. Both were real problems with concrete root causes. The price failure wasn't a network fluke — it was a structural Yahoo Finance API change that the 4-endpoint chain couldn't paper over. The fix required a different endpoint, not more retries.

The BTC ask was the right call. A cold wallet position has no exchange record; the quantity matters, the basis matters, and guessing either would have put wrong data in a financial dashboard. Chris answered in one line. The rest was build.

No sessions since the prior investment entry (S48-Investment, 2026-06-23) produced any portfolio work. This session closed the gap between the dashboard and reality. The dashboard now reflects what Chris actually holds.

