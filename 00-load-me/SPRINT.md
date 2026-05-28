# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S39 | 2026-05-27
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## ⚠️ LOAD NOTE — TOKEN EFFICIENCY
Do NOT load SESSION_HISTORY or MASTER_OPEN_ITEMS every session.
- If SPRINT.md session number is behind the latest known session → pull from GitHub:
  - `session-history/SESSION_HISTORY.md` — full session log
  - `master-open-items/MASTER_OPEN_ITEMS.md` — complete open item history
- Otherwise: SPRINT.md is the only context file needed at session start.

---

## CORRECTED DATA MODEL (S39 — do not revert)
- **Lavu = primary revenue source.** Lavu captures ALL sales: dine-in + delivery + catering.
- GH, DD, UE are 3rd-party delivery sub-channels. They contribute TO Lavu totals.
- GH-only data in `aura_thai_finance` sheet is NOT a revenue baseline — it's one channel.
- **True daily revenue baseline comes from Lavu Daily Sale reports.**
- Lavu Daily Sale 2025 is already a Google Sheet in Drive (readable). 2023/2024 are XLS.

---

## ACTIVE ITEMS — S39 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-06 | Aura Thai: Decision Dashboard | 🔴 Priority | Checklist built S38. Data inventory mostly in Drive. Need May Lavu + chef pay (captured S39). |
| A-02 | UberEats price impact — complete analysis | ⏳ Partial | Missing Jan UE + full Apr 14-30. Files in Drive UE folder. |
| I-23 | artie_report_sync.py cron — fix trigger | ❌ Open | Confirmed not firing since ~May 8. Fix SOP needed (A-04). |
| A-04 | ARTIE SOP 13 — cron fix + monthly finance | ❌ Open | Write to ARTIE-RUNBOOK.md. |
| A-05 | Wire email pipeline → aura_thai_finance sheet | ❌ Open | GH in sheet ✅. DD/UE not yet loaded. Fix I-23 first. |
| A-03 | Push aura_thai_finance.html → ops.radrooster.co | ❌ Pending | Needs real Lavu data first. |
| I-06 | Daily digest cron for #general | ❌ Open | Decide time with Chris. |
| I-17 | Decommission old Cloudflare Tunnel | ❌ Open | |
| B-01 | Pinyo Farms market validation | ❌ Queued | |

---

## AURA THAI — DECISION DASHBOARD (A-06, PRIORITY)
**Goal:** Dashboard showing current status, next week prediction, action recommendations.
**Checklist file:** Drive → Financial Data → `Aura Thai — Decision Dashboard Data Checklist` (created S38)

### Data inventory — what's in Drive now
| Data | Location | Status |
|------|----------|--------|
| Lavu Daily Sale 2025 | Drive/Lavu/ — Google Sheet | ✅ Readable |
| Lavu Daily Sale 2024 | Drive/Lavu/ — XLS | ⚠️ Needs conversion |
| Lavu Daily Sale 2023 | Drive/Lavu/ — XLS | ⚠️ Needs conversion |
| Lavu Daily Sale Apr 2026 | Drive/Lavu/ — XLS | ⚠️ Needs conversion |
| Lavu Daily Sale Jan–Mar 2026 | Drive/Lavu/ — XLS | ⚠️ Had parsing issues — prefer monthly exports |
| Lavu Transactions Jan–May 2026 | Drive/Lavu/ — XLS by month/day | ✅ Available |
| Lavu Time Cards Jan–Apr 2026 | Drive/Lavu/ — CSV | ✅ Readable |
| Sale by Item Jan–Apr 2026 | Drive/Lavu/Sale by Item — XLS | ⚠️ XLS |
| Chef fixed pay (BOH) | Captured S39 — see below | ✅ Recorded |
| GH data Jan–May 8 2026 | aura_thai_finance Google Sheet | ✅ Live |
| DD/UE delivery data | Drive/Financial Data/ folders | ✅ Available |

### Still needed from Chris
| Item | Priority |
|------|----------|
| May 2026 Lavu Daily Sale export (summary) | 🔴 High |
| Current menu prices (dine-in, DD, UE, GH) | 🔴 High |
| Lavu labor reports 2024–2026 | 🟡 Medium |
| 2023 delivery platform exports (GH/DD/UE) | 🟢 Low |

---

## AURA THAI — CHEF / BOH LABOR (captured S39)
**Pay cycle:** Every 2 weeks
**Structure:** 32–40 hrs @ $20/hr on paycheck (after tax), remainder in cash
**Example:** $1,000 total → $400 paycheck, ~$100 tax withheld → $400 check + $600 cash

| Name | Role | Rate | Days/Period | Total/Period |
|------|------|------|-------------|--------------|
| Miguel | Head Chef | $175/day | 12 | $2,100 |
| P Sang | 2nd Head Chef | $155/day | 12 | $1,860 |
| Eliseo | Chef | $130/day | 10.5 | $1,365 |
| Rambo | Dishwasher | $125/day | 10.5 | $1,312.50 |
| Erick | Chef | $140/day | 2 | $280 |
| **TOTAL** | | | | **$6,917.50/period** |

**Daily BOH labor cost:** ~$494/day (6,917.50 ÷ 14 days)
**Monthly BOH labor:** ~$15,000/month
FOH labor tracked in Lavu time cards (servers @ $16/hr).

---

## AURA THAI PIPELINE — KEY FACTS (do not ask Chris)
- `artie_report_sync.py v2` built S20 — 13-parser email pipeline (DD/UE/GH auto-email Artie)
- Pipeline NOT firing since ~May 8 (I-23)
- GH data in `aura_thai_finance` sheet through May 8 only
- DD + UE NOT in sheet yet — do not move those source files
- Sheet ID: `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE`
- Rad Rooster: NOT launched (confirmed S39)

---

## AURA THAI — PRICE ANALYSIS RESULTS
- DD +20% went live Apr 9: ticket +13.1%, orders -16.2%, revenue -5.1% — slightly hurting ✅ complete
- UE +20% went live Apr 9: ticket +34.7% vs March, orders -1.5% — PARTIAL (only 5 days POST, Easter confound)
- Analysis files: `dd_price_impact.html`, `ue_price_impact.html` v2 in /outputs

---

## INFRASTRUCTURE — KEY FACTS (do not ask Chris)
- **GitHub repo:** `~/Documents/Claude/sharedfolder` on Chris's Mac
- **GitHub PAT:** Drive Soul folder (fileId: `1528C9LxOxjxQvS5iUM8vFjE50clNM1NT`) — also `~/.pinyo_github_pat`
- **Push script:** `outputs/handoff/push_handoff.sh` — run from Terminal.app
- **Cloudflare Pages:** auto-deploys on push → ops.radrooster.co
- **Drive Data Dump:** `1C96_Z8__1WVzbApAnHQaKxkiPFVNViDt` → Financial Data subfolder → Lavu/GH/DD/UE folders

---

## SPRINT GOAL — MAY/JUN 2026
**Theme:** Build the Aura Thai Decision Dashboard. Lavu as primary data source. Real numbers. Real predictions. Actionable weekly recommendations.

---

## BUSINESSES — CURRENT FOCUS

| Business | Status | Priority Action |
|----------|--------|-----------------|
| Aura Thai | 🔴 Active | Decision Dashboard (A-06). Fix cron (I-23). Complete UE analysis (A-02). |
| Vine Arbitrage | 🟢 Running | Artie handles — no Claude action needed |
| Pinyo Farms | ⏳ Planning | Market validation — B-01, queued |
| AI Ventures | ⏳ Planning | Not started |
| Roam | ⏳ Planning | Not started |

---

## PROTOCOL — ANALYZE BEFORE EXECUTE (S35)
> For any strategy touching pricing, menu, marketing spend, or operations — model scenarios first, define decision criteria, get approval, then move.

---

## BLOCKED — DO NOT TOUCH

| Item | Blocker |
|------|---------|
| A-01 Lavu as live data source | Lavu API setup incomplete (Chris) |
| O-04 Shift Close integration | Chris needs to complete setup |

---

## 🔗 Graph Links
[[HOME]] | [[EMPIRE_STATUS]] | [[MASTER_OPEN_ITEMS]]
[[aura-thai]] | [[vine-arbitrage]] | [[pinyo-farms]] | [[ai-ventures]] | [[roam]]
