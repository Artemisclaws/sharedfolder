# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S43 | 2026-06-20
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S44
```
Load soul files.
S43: Invoice system stabilized. ARTIE-RUNBOOK.md live on GitHub (artie-config/). Artie cleared to enter invoices.
Priority: (1) Check if Artie has entered Invoice Log data + Sales by Period data for same period → run COGS analysis if yes. (2) Remind Chris to fill Dish Map column D. (3) A-08b Finance tab rebuild if COGS is blocked.
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

## ACTIVE ITEMS — S43 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog invoices + weekly Sales by Period. |
| A-09b | Chris fill Dish Map column D | OPEN — CHRIS | 31 ingredients loaded. Enter dish names per ingredient. Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| A-06b | Revenue tab: live data connection | Pending | Master Google Sheet → revenue.html reads on load. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| I-06 | Daily digest cron #general | OPEN | |
| B-01 | Pinyo Farms market validation | QUEUED | Parking lot until COGS done. |
| A-04 | ARTIE SOP 13 + 14 | DONE S43 | artie-config/ARTIE-RUNBOOK.md on GitHub. SOP 14 live-tested. |
| A-07 | Decision Dashboard ops.radrooster.co | DONE S41 | Live. |
| A-08 | Aura Thai Finance tab | DONE S40 | Live. |

---

## AURA THAI INVOICE SYSTEM (S40/S43 — FOUNDATION COMPLETE)
**Sheet:** aura_thai_finance | 5 new tabs added
**Artie SOP:** artie-config/ARTIE-RUNBOOK.md → SOP 14
**Sheet URL:** https://docs.google.com/spreadsheets/d/1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE

| Tab | Status | Owner |
|-----|--------|-------|
| Invoice Log | READY | Artie — enter every delivery |
| Price Tracker | READY | Auto — Aura Thai Ops > Refresh Price Tracker |
| Dish Map | READY (col D blank) | Chris — fill Used In Dishes column |
| Sales by Period | READY | Artie — weekly from Lavu Sale by Item |
| COGS by Dish | WAITING FOR DATA | Claude — analyze once Invoice Log + Sales by Period overlap |

**COGS trigger:** When Invoice Log + Sales by Period both have data for the same time period → Claude runs analysis.

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
| COGS | Starting S43 | Artie entering invoices |
