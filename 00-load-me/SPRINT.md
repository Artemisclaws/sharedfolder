# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S56 | 2026-07-01
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S56
```
Load soul files.
S55: Investment strategy UNBLOCKED — all S47/S48 deferred questions answered by Chris. Options income playbook v1 built (covered calls + CSPs, KO/SCHD, Fidelity Roth — outputs/pinyo-empire_options-income-playbook_v1.md + checkpoint). Six decisions locked: crypto hold to BTC $120K+ then exit/restructure; property window 2027–2032, LA/OC/LB STR house-hack profile (DEFERRED — not priority); +20% trim rule; PRIORITY #1 = AURA THAI TO BLACK; trust/ILIT education queued; 1.7 BTC → cold wallet.
Priority: (1) AURA THAI PATH-TO-BLACK PLAN — dedicated session, load P&L/Lavu data first (YTD -7.5%, Apr -11.3%). (2) Chris decisions pending: Roth cash → KO CSP vs BTC window Sept 15–Oct 31 ($9,694 can't fund both — one-way door); MCD trigger (at $270, −20% off ATH, near 52-wk low NOW). (3) RoamWithChris Story Index build (needs trip count + sheet location from Chris). (4) Aura Sweet spinoff strategy (AS-01) + Somisomi analysis (AS-02). (5) Queued Claude builds: crypto exit plan at $120K+, correction battle plan, trust/ILIT/insurance education.
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
> PRIORITY #1 (Chris, S55): Aura Thai to black. Property and heavy investing moves are deferred behind it.

---

## ACTIVE ITEMS — S55 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| AT-11 | Aura Thai path-to-black plan | NEXT BUILD — CLAUDE | Priority #1 per Chris S55. Dedicated session with P&L data. |
| INV-A | Fidelity Tier 1 options approval + verify ≥100 KO / ≥300 SCHD in Roth | OPEN — CHRIS | Unlocks covered calls + CSPs → $105–195/mo tax-free (playbook v1 in outputs). |
| INV-B | Roth cash allocation: KO CSP vs BTC window (Sept 15–Oct 31) | DECISION — CHRIS | $9,694 cannot fund both. One-way door. |
| INV-C | MCD entry decision | DECISION — CHRIS | $270, −20% off ATH, near 52-wk low. Name trigger + tranche 1 size (direct shares, not CSP — CSP needs $26K). |
| INV-D | 1.7 BTC → cold wallet | OPEN — CHRIS | Committed S55. KuCoin custody risk closes when done. |
| AS-01 | Aura Sweet spinoff strategy | OPEN | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Somisomi competitive analysis | OPEN | Carried from S52 — Chris to walk the block first |
| AS-03 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-04 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. |
| RWC-05 | Story Index master sheet — build | BLOCKED — CHRIS | Schema locked (20 fields). Need trip count + sheet location. |
| RWC-06 | Footage consolidation onto external HD | OPEN — CHRIS | Single source of truth. |
| RWC-07 | DaVinci Resolve tagging pass | OPEN — CHRIS | After RWC-06. |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog. |
| A-09b | Chris fill Dish Map column D | OPEN — CHRIS | Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | DASHBOARD ARCHITECTURE RULE violation. |
| A-10 | ezCater onboarding | IN PROGRESS — CHRIS | Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |

---

## INVESTMENT — S55 STATUS
**Playbook:** `outputs/pinyo-empire_options-income-playbook_v1.md` — covered calls + cash-secured puts from zero, exact KO/SCHD deployment, Fidelity click-by-click, guardrails. Math verified.
**Market snapshot (7/1):** KO $81.32 (near ATH) | SCHD $31.80 | MCD $270 (−20% off ATH, near 52-wk low).
**Account structure (verified S55):** Roth = active trading + options income (tax-free). Taxable = long-term holds (LTCG rates, step-up basis). Caveats: Roth losses irreplaceable ($7K/yr limit) — defined playbook only, no speculation; wash-sale trap across taxable↔IRA on same names.
**"Sell short positions" reframed:** Chris confirmed he meant cash-secured puts. Shorting is off the table.
**Crypto:** Hold to BTC $120K+, cash out, restructure. 1.7 BTC → cold wallet (Chris). BTC accumulation window Sept 15–Oct 31 draws from Roth cash IF Chris allocates it there (see INV-B).
**Property (deferred):** Window 2027–2032. Profile: LA/OC/Long Beach, STR-friendly, multi-unit on one lot, house-hack + future ADU (Pasadena model, ref 606 Palisade St 91103). CA insurance = known risk. Backup: similar-climate state. Metals held: 5oz gold, 60oz silver.

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
