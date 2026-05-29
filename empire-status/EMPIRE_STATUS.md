# EMPIRE_STATUS.md
**Last Updated:** 2026-05-29 | Session 40
**Updated By:** Claude (Session 40)

---

## STATUS OVERVIEW

| Area | Status | Notes |
|------|--------|-------|
| OpenClaw | 2026.5.7 | Services: openclaw-gateway + openclaw-node (systemd --user). |
| GitHub setup | ✅ LIVE | github.com/Artemisclaws/sharedfolder |
| Discord setup | ✅ LIVE | All 8 channels wired, Artie responding |
| Morning briefing → Discord | ✅ CONFIRMED | Verified by Chris, S27 |
| ops.radrooster.co | ✅ LIVE — CLOUDFLARE PAGES | GitHub auto-deploy. No Artie dependency. |
| MASTER_OPEN_ITEMS.md | ✅ LIVE | GitHub: master-open-items/MASTER_OPEN_ITEMS.md |
| SESSION_HISTORY.md | ✅ LIVE | GitHub: session-history/SESSION_HISTORY.md |
| Handoff system | ✅ REFORMED | Checkpoint in sessions/S40/ + SPRINT.md digest |
| Obsidian Second Brain | ✅ LIVE | S34 — vault synced, auto-pull every 5min |
| Aura Thai Finance Dashboard | ✅ LIVE — Finance tab | S40 — YoY chart, hero metrics, 5 recs. ⚠️ HARDCODE DEBT: FINANCE_DATA embedded in HTML — rebuild A-08b |
| Aura Thai Price Monitoring | ✅ ACTIVE | S35 — DD +20% live Apr 9. Monitoring weekly. |
| COGS Tracking System | ❌ NOT BUILT | A-09 — TOP PRIORITY next session |
| GH/DD/UE pipeline | ❌ BROKEN | I-23 — not firing since May 8 |
| Rad Rooster | ❌ NOT LAUNCHED | Confirmed S39 |
| Daily digest cron | ❌ NOT BUILT | I-06 |
| Drive folder reorg | ❌ DEFERRED | I-02 |

---

## AURA THAI — KEY FACTS (do not ask Chris again)

### Revenue Model — CORRECTED S39
- **Lavu = primary revenue source.** Captures ALL sales (dine-in + delivery + catering).
- GH/DD/UE are delivery sub-channels — contribute TO Lavu totals, not separate.
- Lavu Daily Sale = ground truth.

### Revenue Performance (S40 verified)
| Month | 2025 | 2026 | YoY |
|-------|------|------|-----|
| Jan | $90,361 | $84,651† | -6.3% |
| Feb | $77,122 | $72,248† | -6.3% |
| Mar | $92,324 | $86,490† | -6.3% |
| Apr | $81,437 | $72,214 ✅ | -11.3% |
| May | $83,422 | $77,986 proj | -6.5% |
| **YTD** | **$412,036** | **$381,011** | **-7.5%** |
† Q1 monthly splits estimated by 2025 ratio. Verified Q1 total = $243,389.16.

### BOH Labor — Captured S39
Pay cycle: every 2 weeks | ~$15,000/month | ~$494/day

| Name | Role | $/day | Days/period | Total/period |
|------|------|-------|-------------|--------------|
| Miguel | Head Chef | $175 | 12 | $2,100 |
| P Sang | 2nd Head Chef | $155 | 12 | $1,860 |
| Lek | Prep Cook | $100 | 12 | $1,200 |
| Nim | Dishwasher | $80 | 12 | $960 |
| Extra | Occasional | $100 | 8 | $800 |
| **Total** | | | | **$6,917.50/period** |

### COGS — NOT YET TRACKED
- Target: 28–32% of revenue
- System to be built: A-09 (weekly invoice entry)
- This is the #1 sustainability concern as of S40

### Dashboard Architecture Rule (S39 — permanent)
All dashboards must pull from master Google Sheet. Never hardcode data in HTML/JS.
Finance tab currently violates this (A-08b to fix).

---

## PINYO EMPIRE — BUSINESSES

| Business | Status | Notes |
|----------|--------|-------|
| Aura Thai | ✅ OPERATING | Revenue down -7.5% YTD vs 2025. Sustainability concern. |
| Rad Rooster | ❌ NOT LAUNCHED | Ghost kitchen — pending launch. |
| Vine Arbitrage | 🔄 ACTIVE | FB/marketplace arbitrage. |
| Pinyo Farms | ❌ QUEUED | Market validation pending — parked until COGS done. |
