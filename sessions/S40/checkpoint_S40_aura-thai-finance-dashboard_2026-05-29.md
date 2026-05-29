# Checkpoint: Aura Thai Finance Dashboard — S40
**Date:** 2026-05-29  
**Session:** S40  
**Status:** ✅ COMPLETE — Finance tab live at ops.radrooster.co

---

## What Was Completed

**Finance tab added to ops.radrooster.co dashboard.**  
New "💰 Finance" tab alongside existing Ops and Revenue tabs.

### Features Built
1. **Alert banner** — auto-shows when YTD revenue is below prior year
2. **3 hero metrics** — May Revenue (projected), YTD vs 2025, BOH Labor %
3. **YoY bar chart** — 2025 vs 2026 side-by-side bars, Jan–Jul, color-coded by direction
4. **Monthly detail table** — Rev 2025 / Rev 2026 / YoY% / BOH Labor / Rev−BOH
5. **5 action recommendations** — prioritized, specific, actionable
6. **Data freshness indicators** — what's current vs what's missing

---

## Key Findings Surfaced in This Build

| Month | 2025 | 2026 | YoY |
|-------|------|------|-----|
| Jan | $90,361 | $84,651† | -6.3% |
| Feb | $77,122 | $72,248† | -6.3% |
| Mar | $92,324 | $86,490† | -6.3% |
| Apr | $81,437 | $72,214 ✅ | **-11.3%** |
| May | $83,422 | $77,986 (proj) | -6.5% |
| **YTD** | $412,036 | $381,011 | **-7.5%** |

† Q1 monthly split estimated by 2025 ratio (Q1 2026 verified total = $243,389.16)  
BOH Labor: 17–21% of monthly revenue (healthy range for BOH only)

**Critical gap:** True net profit unknown — COGS not tracked. Next session priority.

---

## Key Decisions

- **Ratio-estimated Q1 splits** — Q1 total verified from XLS totals row; individual months allocated by 2025 ratios. Close enough for trend visibility. Exact values will populate when 2023/2024 XLS → Google Sheets conversion happens.
- **May uses 26-day actual + projection** — $65,408 actual through May 26, projected $77,986 for full month ($2,516/day × 31 days)
- **Rev−BOH as proxy** — True net profit requires COGS + FOH labor + overhead. Dashboard makes this limitation explicit.
- **Finance tab, not new page** — Kept within ops.radrooster.co tab structure per design rule

---

## Output Files

- **GitHub push:** `dashboard/index.html` → commit `7464de80`  
- **Live at:** https://ops.radrooster.co (Cloudflare Pages auto-deploy, ~2 min)
- **Local backup:** `/outputs/process_revenue.py` (data processing notes)

---

## Data Sources Used

| Source | Coverage | Notes |
|--------|----------|-------|
| Lavu Daily Sale 2025 (Google Sheet) | Jan 2 – Aug 19, 2025 | Full months Jan–Jul, Aug partial |
| Lavu Daily Sales Jan-Mar 2026 (XLS) | Jan 2 – Mar 31, 2026 | Q1 total verified $243,389.16 |
| Lavu Daily Sale Apr 2026 (XLS) | Apr 1–30, 2026 | Verified $72,214.09 |
| Daily Sales May 1-26 2026 (XLS) | May 1–26, 2026 | Partial $65,408 |
| BOH Labor | Fixed | $6,917.50/period × 2 = ~$15,000/mo |

**Still missing:** 2023 XLS, 2024 XLS (too large for Drive download → need Google Sheets conversion), Aug–Dec 2025, GH/DD/UE platform data (pipeline broken)

---

## What Remains (Next Session)

### Immediate Priority: COGS Tracking System
- Plan and build COGS input system
- Weekly food cost entry (invoices from suppliers)
- COGS % target: 28–32% of revenue
- This is the sustainability concern Chris raised

### Ongoing Blockers
- Convert 2023/2024 Lavu XLS to Google Sheets (for full multi-year view)
- Fix GH/DD/UE pipeline (broken since May 8) — I-23
- Fix ARTIE cron job — I-23
- Write ARTIE SOP 13 — A-04

### Dashboard Enhancements (After COGS)
- Add COGS % bar/trend when data exists
- Add FOH labor entry (from Lavu time cards)
- Fix 2023/2024 XLS → exact Q1 monthly splits
- Add delivery platform split (after pipeline fix)

---

## Handoff Notes

**Start next session with:** "Load soul files, then read `checkpoint_S40_aura-thai-finance-dashboard_2026-05-29.md`"

**Session ID:** S40  
**GitHub commit:** `7464de80b6ae756b6b954819052730f5e860eb54`  
**Next task:** COGS tracking system design + build
