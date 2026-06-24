# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S53 | 2026-06-24
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S54
```
Load soul files + BIXBY_KNOLLS_MARKET.md.
S53: Aura Sweet naming locked, poster done, 3-move campaign ready to execute.
Priority: (1) Aura Sweet spinoff strategy — "How should we approach Aura Sweet as a spinoff?" (2) Competitive analysis: Somisomi vs Aura Sweet (carried from S52). (3) Check if Artie has Invoice Log + Sales by Period data → run COGS if yes. (4) Remind Chris: Dish Map column D still blank.
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

## ACTIVE ITEMS — S53 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| AS-01 | Aura Sweet spinoff strategy | OPEN — S54 | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Somisomi competitive analysis | OPEN — S54 | Carried from S52 — Chris to walk the block first |
| AS-03 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post today. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-04 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog. |
| A-09b | Chris fill Dish Map column D | OPEN — CHRIS | 31 ingredients loaded. Enter dish names per ingredient. Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |

---

## AURA SWEET — S53 STATUS
**Flavor names locked:**
- The Brew (Thai Tea)
- Chef's Secret (Fish Sauce Caramel) — viral hook, never reveal early
- Island Cream (Coconut)
- Sweet Grain (Mango Sticky Rice)

**Sizing (S52 locked):** 8oz cup + 16oz pint. Two formats only.
**Poster:** Menu poster mockup complete. One poster only. Copy locked. Ready for Canva.
**Campaign:** 3-move local launch playbook ready. BKBA is the reach move.
**Proof:** 100 Thai Tea + 40 Chef's Secret scoops sold by poster alone.
**Market intel:** BIXBY_KNOLLS_MARKET.md — load this at session start for any Aura Sweet work.
**Next:** Spinoff strategy + Somisomi competitive analysis.

---

## AURA THAI INVOICE SYSTEM (S40/S43 — FOUNDATION COMPLETE)
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
