# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S42 | 2026-06-10
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S43
```
Load soul files.
S42 was ezCater onboarding — quick-ref doc delivered, Chris completing paperwork.
Priority: (1) A-09 COGS tracking system — TOP PRIORITY, still not built. (2) A-08b Finance tab rebuild to Google Sheet.
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

## ACTIVE ITEMS — S42 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-09 | COGS tracking system | TOP PRIORITY | Weekly food cost entry. Target 28-32% revenue. Sustainability concern. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| A-06b | Revenue tab: live data connection | Pending | Master Google Sheet → revenue.html reads on load. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| A-04 | ARTIE SOP 13 | OPEN | Write to ARTIE-RUNBOOK.md. |
| I-06 | Daily digest cron #general | OPEN | |
| B-01 | Pinyo Farms market validation | QUEUED | Parking lot until COGS done. |
| A-07 | Decision Dashboard ops.radrooster.co | DONE S41 | Live at ops.radrooster.co/aura-thai. |
| A-08 | Aura Thai Finance tab | DONE S40 | Live at ops.radrooster.co. |

---

## KEY REVENUE NUMBERS (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | **YoY: -7.5%**
- Apr 2026 vs 2025: **-11.3%** (worst month so far)
- BOH Labor: ~$15,000/month | ~$494/day

## EZCATER — LOCKED S42
- Fee type: Fixed-rate | 4 zones: 0-5mi $30/$100 → 6-10mi $40/$150 → 11-15mi $50/$250 → 16-20mi $60/$350
- Strategy: Reliability Rockstar path. Match WaBa Grill / moonbowls / Rascals ($30 & up / $100 min / 4.9 rating).
- Quick-ref doc: ezcater_quickref.docx in outputs folder.
- Chris completing onboarding paperwork independently.

## FINANCE DATA STATUS
| Source | Coverage | Status |
|--------|----------|--------|
| Lavu 2025 Google Sheet | Jan-Jul 2025 | Ready |
| Lavu Jan-Mar 2026 XLS | Q1 ($243,389.16 verified) | Ready |
| Lavu Apr 2026 XLS | $72,214.09 verified | Ready |
| Lavu May 1-26 2026 XLS | $65,408 partial | Ready |
| 2023/2024 XLS | Full years | Too large — need Sheets conversion |
| GH/DD/UE pipeline | May 8+ | BROKEN (I-23) |
| COGS | — | NOT tracked yet (A-09) |

## AURA THAI — COGS TRACKING (A-09, TOP PRIORITY)
**Goal:** Build ingredient cost database → COGS % per dish → margin visibility on dashboard.
**Target:** 28-32% food cost as % of revenue.
**Architecture:** New tab COGS Tracker in aura_thai_finance. New tab on ops.radrooster.co after Aura Thai.
**Invoice workflow:** Chris drops invoice photos → Claude extracts line items → paste into COGS Tracker.
**Note:** Tiller is bank-feed only. For itemized invoice data: use Claude (Cowork) or Dext.

## CLAUDE-CORE.md V5 (S40 — permanent)
- Build Protocol: test logic before building. Never hardcode data in dashboards.
- Within-session file rule: no re-fetching already-loaded files.
- Haiku agent default for mechanical tasks (file search, parsing, format conversion).
