# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S40 | 2026-05-28
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
- GH-only data in `aura_thai_finance` sheet is NOT a revenue baseline — it is one channel.
- **True daily revenue baseline comes from Lavu Daily Sale reports.**
- Lavu Daily Sale 2025 is already a Google Sheet in Drive (readable). 2023/2024 are XLS.

---

## ACTIVE ITEMS — S40 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| I-24 | Document anchor/index system for large soul files | 🔴 Priority | S41 first task. Add grep-able section anchors to SHARED-CORE, CLAUDE-CORE, THINKING_OS, EMPIRE_STATUS. Update BOOT.md fetch triggers with anchor names. |
| A-06b | Connect revenue dashboard to master Lavu sheet | 🔴 Priority | Dashboard is static HTML. Needs live data connection. Architecture: master Google Sheet (Artie updates from raw XLS) → revenue.html reads live. Same pattern as ops dashboard reading GitHub. |
| A-06c | Add 3rd party fees to revenue dashboard | 🔴 Priority | GH/DD/UE fee data already in Drive. Factor into net revenue + projections. S41. |
| A-02 | UberEats price impact — complete analysis | ⏳ Partial | Jan UE file needed. Full Apr 14-30 data. Files in Drive. |
| I-23 | artie_report_sync.py cron — fix trigger | ❌ Open | Not firing since ~May 8. Fix SOP needed (A-04). |
| A-04 | ARTIE SOP 13 — cron fix + monthly finance | ❌ Open | Write to ARTIE-RUNBOOK.md. |
| A-05 | Wire email pipeline → aura_thai_finance sheet | ❌ Open | GH in sheet ✅. DD/UE not yet loaded. Fix I-23 first. |
| I-06 | Daily digest cron for #general | ❌ Open | Decide time with Chris. |
| I-17 | Decommission old Cloudflare Tunnel | ❌ Open | |
| B-01 | Pinyo Farms market validation | ❌ Queued | |

---

## A-06 DECISION DASHBOARD — STATUS (built S40)
**Live at:** ops.radrooster.co → Revenue tab
**Files:** `dashboard/revenue.html` (static), `dashboard/index.html` (tabbed)
**Current state:** Static HTML with hardcoded Apr + May 2026 numbers.

### What is baked in (static, S40)
| Data | Value |
|------|-------|
| April 2026 total | $72,214 (29 days, $2,490/day) |
| May 1-26 2026 total | $65,408 (from Lavu summary row) |
| April 2025 baseline | $81,437 → -11.3% YoY |
| May 1-26 2025 baseline | $70,792 → -7.6% YoY |
| Current week May 20-26 | $18,344 (+12.6% WoW) |
| BOH labor | $494/day, ~$15,000/month |
| Monthly 2025 baselines | Jan-Jul loaded |

### What is needed to make it live (A-06b, S41)
1. Create master Lavu Google Sheet — one row per day, all months
2. Artie: when new XLS arrives in Drive → parse → append to master sheet
3. revenue.html: read from master sheet via Sheets API on page load (like ops reads GitHub)
4. Dashboard auto-updates whenever Artie adds data. No Claude needed to rebuild.

### Drive folders for S41 — Jan-Mar 2026 XLS
Chris confirmed Jan-Mar files are in Drive. Use haiku model to find and parse:
- Folder 1: https://drive.google.com/drive/folders/1_5WYvoliZ46w4mRuIayLm8uoMBeHb-mZ
- Folder 2: https://drive.google.com/drive/folders/1jNC_5d4fK1JxAfvC6oWUMVK5Cbe-56rx
- Folder 3: https://drive.google.com/drive/folders/1bAl7InIONZGy_XshNWzrtzcLMOXzuS7k

---

## AURA THAI — CHEF / BOH LABOR (captured S39)
**Daily BOH labor cost:** ~$494/day | **Monthly:** ~$15,000/month

| Name | Role | Rate | Days/Period | Total/Period |
|------|------|------|-------------|--------------|
| Miguel | Head Chef | $175/day | 12 | $2,100 |
| P Sang | 2nd Head Chef | $155/day | 12 | $1,860 |
| Eliseo | Chef | $130/day | 10.5 | $1,365 |
| Rambo | Dishwasher | $125/day | 10.5 | $1,312.50 |
| Erick | Chef | $140/day | 2 | $280 |
| **TOTAL** | | | | **$6,917.50/period** |

FOH labor tracked in Lavu time cards (servers @ $16/hr).

---

## AURA THAI PIPELINE — KEY FACTS (do not ask Chris)
- `artie_report_sync.py v2` built S20 — 13-parser email pipeline (DD/UE/GH auto-email Artie)
- Pipeline NOT firing since ~May 8 (I-23)
- GH data in `aura_thai_finance` sheet through May 8 only
- DD + UE NOT in sheet yet — do not move those source files
- Sheet ID: `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE`
- Rad Rooster: NOT launched (confirmed S39)
- Lavu XLS files are UTF-16LE TSV (not real Excel) — decode: base64 → BOM strip → UTF-16LE parse

---

## AURA THAI — PRICE ANALYSIS RESULTS
- DD +20% live Apr 9: ticket +13.1%, orders -16.2%, revenue -5.1% ✅ complete
- UE +20% live Apr 9: ticket +34.7% vs March, orders -1.5% — PARTIAL (Easter confound, 5-day window)

---

## INFRASTRUCTURE — KEY FACTS (do not ask Chris)
- **GitHub PAT:** Drive Soul folder (fileId: `1528C9LxOxjxQvS5iUM8vFjE50clNM1NT`)
- **Cloudflare Pages:** auto-deploys on push → ops.radrooster.co
- **ops.radrooster.co:** Ops tab (live from GitHub) + Revenue tab (revenue.html — static S40)
- **Drive Data Dump:** `1C96_Z8__1WVzbApAnHQaKxkiPFVNViDt` → Financial Data subfolder

---

## SPRINT GOAL — MAY/JUN 2026
**Theme:** Make the Aura Thai Decision Dashboard live — connected to real data, auto-updating.

---

## BUSINESSES — CURRENT FOCUS

| Business | Status | Priority Action |
|----------|--------|-----------------|
| Aura Thai | 🔴 Active | A-06b: live data connection. A-06c: 3PD fees. Parse Jan-Mar 2026. |
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
