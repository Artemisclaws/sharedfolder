# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S57 | 2026-07-01
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S57
```
Load soul files.
S56: Family Investment Playbook v2 LOCKED — BTC ladder 40/30/30, 529 dip-adds, Golfii 70/30 all approved; $5K ladder cash committed ($2K@$50K/$1.5K@$45K/$1.5K@$40K). Playbook updated on GitHub (sessions/S55/). Investment execution is now 100% Chris physical actions (INV-13/08/15/14) — queued, not active.
Priority: (1) Verify Apps Script V2 installed + syncIngredientsToDishMap ran clean (Execution Log). (2) Execute audit fixes H1–H5 with Chris approval (I-25): repoint/archive artie-config runbook, reconcile tracker IDs, EMPIRE_RULES archive banner, CLAUDE-CORE header version. (3) A-11 Aura Thai PATH-TO-BLACK — Priority #1 per Chris; load P&L/Lavu data first. (4) RoamWithChris — trip count + sheet location → build Story Index. (5) Aura Sweet spinoff strategy + Somisomi analysis.
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

## ACTIVE ITEMS — S56 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-12 | Install Apps Script V2 (timeout fix) | IN PROGRESS — CHRIS | Paste outputs/aura-thai_invoice-system_apps-script_v2.gs → run syncIngredientsToDishMap. Alerts→toasts, setupInvoiceSystem disarmed. |
| I-25 | Soul-file audit fixes | OPEN | 5H/7M/6L. H1–H5 first. Report: soul-files_audit_S55 (outputs). Chris approves order. |
| AS-01 | Aura Sweet spinoff strategy | OPEN — S56 | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Somisomi competitive analysis | OPEN — S56 | Carried from S52 — Chris to walk the block first |
| AS-03 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-04 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. |
| RWC-05 | Story Index master sheet — build | BLOCKED — CHRIS | Schema locked (20 fields). Need trip count + sheet location before build. |
| RWC-06 | Footage consolidation onto external HD | OPEN — CHRIS | Single source of truth. microSDs + cameras + Google Photos → one drive. |
| RWC-07 | DaVinci Resolve tagging pass | OPEN — CHRIS | After RWC-06. Free — Keywords + Smart Bins. |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog. |
| A-09b | Chris fill Dish Map column B (dish names) | OPEN — CHRIS | CORRECTED S55: column B, not D (ground truth from live script — 2-col Dish Map). Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| INV-13 | Park $5K USDT on KuCoin + set ladder limit orders $50/45/40K | OPEN — CHRIS | Approved S56: $2,000/$1,500/$1,500. BTC ~$58K — first rung ~14% away. |
| INV-08 | Move 1.7 BTC → cold wallet | OPEN — CHRIS | S55 decision. Only ladder cash stays on KuCoin. |
| INV-15 | Tax preparer meeting — 5 questions (playbook §7) | OPEN — CHRIS | Blocks Golfii backdoor + 529 vehicle choice (SB 529 check). |
| INV-14 | Open Auggie 529 this month — $300/mo, 100% equity | OPEN — CHRIS | Starts 15-yr 529→Roth clock. Vehicle pends INV-15. |
| INV-16 | Golfii backdoor Roth — Trad+Roth IRA, Form 8606 | BLOCKED | On INV-15 (MAGI + pro-rata). 70/30 approved S56. |

---

## ROAMWITHCHRIS — S54 STATUS
**Story Protocol:** LOCKED, TESTED S54 — script written in one clean pass, zero rewrites.
**Series signature opener:** "You won't remember this. So let me tell you."
**Series tagline (bio/channel):** "This is one of the stories I kept for you."
**Hook format:** Auggie hero visual → AI baby text "Daddy tell me a story" → signature opener → story
**Lesson format:** One line woven in voiceover + pinned comment breakdown + future compilation reel
**Auggie backpacking reel:** Script DONE — ready for CapCut.
**Story Bible Protocol:** V2 locked — Compass (4.5), false-belief line, Why Auggie Needs This Story (7.5) added.
**Content system:** Footage → Story Index → Story Bible → Script → Edit → Post — fully designed. Story Index (20-field Google Sheet) is next build, blocked on trip count + sheet location from Chris.
**Storage plan:** External HD = source of truth (not Google Photos — cost trap). DaVinci Resolve (free) for tagging. Descript if it earns its keep. Wideframe/NAS deferred — not worth it at current volume.
**Note:** Full Story Bible content must come from Chris directly each time — "memory item #7" references are not accessible cross-session in this environment. Always ask, never fabricate.

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

## AURA THAI INVOICE SYSTEM (S40/S43 — FOUNDATION COMPLETE, SCRIPT V2 S55)
| Tab | Status | Owner |
|-----|--------|-------|
| Invoice Log | READY | Artie — enter every delivery |
| Price Tracker | READY | Auto — run updatePriceTracker from 🍜 menu (V2) |
| Dish Map | READY (col B blank) | Chris — fill Dish Name(s) column B |
| Sales by Period | READY | Artie — weekly from Lavu Sale by Item |
| COGS by Dish | WAITING FOR DATA | Claude — analyze once Invoice Log + Sales by Period overlap |

---

## KEY REVENUE NUMBERS (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | **YoY: -7.5%**
- Apr 2026 vs 2025: **-11.3%** (worst month so far)
- BOH Labor: ~$15,000/month | ~$494/day
