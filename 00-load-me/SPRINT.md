# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S41 | 2026-05-30
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S42
```
Load soul files + checkpoint_S41_2026-05-30.md.
Dashboard live at ops.radrooster.co/aura-thai.
Priority: (1) Load May Lavu data into sheet. (2) A-09 COGS — start with invoice photos.
```

---

## LOAD NOTE — TOKEN EFFICIENCY
Do NOT load SESSION_HISTORY or MASTER_OPEN_ITEMS every session.
- If SPRINT.md session number is behind → pull those files from GitHub.
- Otherwise: SPRINT.md is the only context file needed at session start.

---

## CORRECTED DATA MODEL (S39 — do not revert)
- **Lavu = primary revenue source.** Captures ALL sales: dine-in + delivery + catering.
- GH, DD, UE are sub-channels. They contribute TO Lavu totals.
- Lavu XLS = UTF-16LE TSV — base64 decode → BOM strip → parse.

---

## PERMANENT RULES
> All dashboards live at ops.radrooster.co. No standalone URLs ever.
> Finance tab hardcodes data — MUST rebuild to read from Google Sheet (DASHBOARD ARCHITECTURE RULE violation).
> $5K/day focus filter: new ideas → parking lot unless they advance COGS → pipeline → unit economics → growth.

---

## ACTIVE ITEMS — S41 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-09 | COGS tracking system | 🔴 TOP PRIORITY | Weekly food cost entry. Target 28-32% revenue. Sustainability concern. |
| A-08b | Finance tab: rebuild to Google Sheet | 🔴 Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-08 | Aura Thai Finance tab | ✅ DONE S40 | Live at ops.radrooster.co. YoY chart, hero metrics, 5 recs. Data hardcoded (A-08b). |
| A-07 | Decision Dashboard → ops.radrooster.co | ✅ DONE S41 | Live at ops.radrooster.co/aura-thai. Apps Script JSON + static HTML. Apps Script needs redeploy for checklist fix. |
| A-06b | Revenue tab: live data connection | 🔄 Pending | Master Google Sheet → revenue.html reads on load. |
| I-23 | artie_report_sync.py cron fix | ❌ Open | Not firing since May 8. |
| A-04 | ARTIE SOP 13 | ❌ Open | Write to ARTIE-RUNBOOK.md. |
| I-06 | Daily digest cron #general | ❌ Open | |
| B-01 | Pinyo Farms market validation | ❌ Queued | Parking lot until COGS done. |

---

## KEY REVENUE NUMBERS (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | **YoY: -7.5%**
- Apr 2026 vs 2025: **-11.3%** (worst month so far)
- May MTD apples-to-apples 26 days: **-7.6%**
- BOH Labor: ~$15,000/month | ~$494/day

## FINANCE DATA STATUS
| Source | Coverage | Status |
|--------|----------|--------|
| Lavu 2025 Google Sheet | Jan-Jul 2025 | ✅ |
| Lavu Jan-Mar 2026 XLS | Q1 ($243,389.16 verified) | ✅ monthly splits by ratio |
| Lavu Apr 2026 XLS | $72,214.09 verified | ✅ |
| Lavu May 1-26 2026 XLS | $65,408 partial | ✅ |
| 2023/2024 XLS | Full years | ❌ Too large — need Sheets conversion |
| GH/DD/UE pipeline | May 8+ | ❌ Broken (I-23) |
| COGS | — | ❌ Not tracked yet (A-09) |
| Menu prices | Price Chart tab (8/1/2024) | ✅ Loaded S41 — dine-in + DD/UE +20% |

---


---

## AURA THAI — COGS TRACKING (A-09, TOP PRIORITY)
**Goal:** Build ingredient cost database → COGS % per dish → margin visibility on dashboard.
**Target:** 28–32% food cost as % of revenue.

### Architecture
- New tab `COGS Tracker` in `aura_thai_finance` Google Sheet
- New tab in `ops.radrooster.co` dashboard (index.html) after Aura Thai tab

### What we need from Chris
| Item | How to provide | Priority |
|------|----------------|----------|
| Purchase invoices | Photos in Cowork session → Claude extracts line items | 🔴 High |
| Portion sizes per dish | Kitchen estimate (rough OK) | 🔴 High |
| Estimated COGS % by category | Proteins ~35%, noodles ~25%, apps ~20% — confirm or adjust | 🟡 Medium |
| Supplier list | SJ Distributors seen in Tiller — any others? | 🟡 Medium |

### Invoice photo → data workflow (Claude)
1. Chris drops invoice photos in Cowork session
2. Claude reads image → extracts: vendor, date, item, unit, qty, unit price, total
3. Output: structured table → paste into COGS Tracker tab
4. Once SOP is written: Artie handles ongoing extraction (extends A-04)

### Note: Tiller does NOT do receipt photos
Tiller is bank-feed only (Plaid). It sees the payment total, not line items.
For itemized invoice data: use Claude (Cowork) or Dext (Receipt Bank) if a dedicated app is preferred.

## CLAUDE-CORE.md V5 (S40 — permanent)
- Build Protocol: test logic before building. Never hardcode data in dashboards.
- Within-session file rule: no re-fetching already-loaded files.
- Haiku agent default for mechanical tasks (file search, parsing, format conversion).

## I-24 ✅ COMPLETE (prior session)
- 33 grep-able anchors added to shared files.
