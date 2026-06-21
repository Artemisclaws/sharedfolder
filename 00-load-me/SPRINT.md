# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S45 | 2026-06-21
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S46
```
Load soul files.
S45: SOP 14 pipeline built (invoice_processor.py). Dish Map synced — 53 ingredients, col B blank.
Priority: (1) A-09b: Chris fill Dish Map col B (Dish Name(s)) — unlocks COGS. (2) A-06: Decision Dashboard. (3) I-23: artie_report_sync.py cron fix. (4) Send invoice_processor.py + SOP_14 to Artie.
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

## ACTIVE ITEMS — S45 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-09b | Chris fill Dish Map col B (Dish Name(s)) | OPEN — CHRIS | 53 ingredients loaded. Supplies → "Supply". Universal costs → "All Dishes". ~35 dish-specific to map. Unlocks COGS. |
| A-06 | Decision Dashboard | OPEN — CLAUDE | Build next session. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| SOP-14-deploy | Send invoice_processor.py + SOP_14 to Artie | OPEN — CHRIS | Files in outputs/. Uses service_account.json (no OAuth). Artie needs: SA file, ANTHROPIC_API_KEY from Chris, DRIVE_FOLDER_ID. |
| A-08b | Finance tab: rebuild to Google Sheet | OPEN | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| AS-01 | Aura Sweet spinoff strategy | OPEN | Parked — address after COGS. |
| B-01 | Pinyo Farms market validation | QUEUED | Parking lot until COGS done. |

---

## AURA THAI INVOICE SYSTEM (S45 — FULLY OPERATIONAL)
**Sheet:** aura_thai_finance | Script: aura_thai_invoice_system.gs (deployed)
**Pipeline:** invoice_processor.py → send to Artie with SOP_14_invoice_processing.md

| Tab | Status | Owner |
|-----|--------|-------|
| Invoice Log | ✅ 277 rows loaded (Feb–May 2026) | Artie — add new deliveries |
| Price Tracker | READY | Auto — run updatePriceTracker() after invoices |
| Dish Map | 53 ingredients loaded, col B BLANK | Chris — fill Dish Name(s) |
| Sales by Period | READY | Artie — weekly from Lavu Sale by Item |
| COGS by Dish | WAITING | Claude — analyze once Dish Map col B + Sales data overlap |

**Dish Map guidance for Chris:**
- Supplies (chopsticks, bags, cleaning): mark "Supply"
- Universal costs (fry oils, sugar, vinegar, soy sauces): mark "All Dishes"
- ~35 dish-specific ingredients: map to actual dish names or shorthand (All Stir Fry, All Curry, etc.)

---

## KEY REVENUE NUMBERS (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | **YoY: -7.5%**
- Apr 2026 vs 2025: **-11.3%** (worst month so far)
- BOH Labor: ~$13,835/period | ~$494/day

