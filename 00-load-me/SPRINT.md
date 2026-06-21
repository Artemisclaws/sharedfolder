# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S44 | 2026-06-21
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S45
```
Load soul files.
S44: Aura Sweet naming, poster, and campaign completed. 3-move campaign ready to execute.
Priority: (1) Aura Sweet spinoff strategy — "How should we approach Aura Sweet as a spinoff?" (2) Check if Artie has entered Invoice Log + Sales by Period data → run COGS if yes. (3) Remind Chris: Dish Map column D still blank.
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

## ACTIVE ITEMS — S44 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| AS-01 | Aura Sweet spinoff strategy | OPEN — S45 | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post today. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-03 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. Add to Canva. |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog invoices + weekly Sales by Period. |
| A-09b | Chris fill Dish Map column D | OPEN — CHRIS | 31 ingredients loaded. Enter dish names per ingredient. Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| B-01 | Pinyo Farms market validation | QUEUED | Parking lot until COGS done. |

---

## AURA SWEET — S44 STATUS
**Flavor names locked:**
- The Brew (Thai Tea)
- Chef's Secret (Fish Sauce Caramel)
- Island Cream (Coconut)
- Sweet Grain (Mango Sticky Rice)

**Poster:** Menu poster mockup complete. One poster only. Copy locked.
**Campaign:** 3-move local launch playbook ready to execute.
**Proof:** 100 Thai Tea + 40 Chef's Secret scoops sold by poster alone.
**Next:** Spinoff strategy discussion S45.

---

## AURA THAI INVOICE SYSTEM (S40/S43 — FOUNDATION COMPLETE)
**Sheet:** aura_thai_finance | 5 new tabs added
**Artie SOP:** artie-config/ARTIE-RUNBOOK.md → SOP 14

| Tab | Status | Owner |
|-----|--------|-------|
| Invoice Log | READY | Artie — enter every delivery |
| Price Tracker | READY | Auto |
| Dish Map | READY (col D blank) | Chris — fill Used In Dishes column |
| Sales by Period | READY | Artie — weekly from Lavu Sale by Item |
| COGS by Dish | WAITING FOR DATA | Claude — analyze once Invoice Log + Sales by Period overlap |

---

## KEY REVENUE NUMBERS (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | **YoY: -7.5%**
- Apr 2026 vs 2025: **-11.3%** (worst month so far)
- BOH Labor: ~$15,000/month | ~$494/day
