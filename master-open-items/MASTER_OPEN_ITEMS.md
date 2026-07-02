# MASTER_OPEN_ITEMS.md
**Living task tracker for the Pinyo Empire.**
**Last Updated:** 2026-07-01 | Session 56
**GitHub:** `master-open-items/MASTER_OPEN_ITEMS.md`

---

## ROAMWITHCHRIS ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| RWC-01 | Story Bible Protocol template | DONE S54 | — | v2 — added Compass (4.5), false-belief line, Why Auggie Needs This Story (7.5). Locked, pending second-story stress test before true bedrock. |
| RWC-02 | Auggie backpacking reel — final script | DONE S54 | — | One clean pass, 37 cuts. roamwithchris_auggie-backpacking-reel_script_v1.md in outputs. Ready for CapCut. Protocol test passed — no rewrites needed. |
| RWC-03 | Footage consolidation onto external HD | OPEN — CHRIS | High | Single source of truth. microSDs + GoPro/Insta360/iPhone originals + Google Photos → `/Trip_Name_YYYY-MM/Camera_Source/`. |
| RWC-04 | Story Index master sheet | BLOCKED — CHRIS | High | Schema designed (20 fields, 6 groups: Identity/Story/Theme/Production/Triage/Tags). Need: rough trip count + standalone sheet vs. existing tab before build. |
| RWC-05 | DaVinci Resolve tagging pass (Keywords + Smart Bins) | OPEN — CHRIS | Medium | After RWC-03. Free. Ties footage location pointers in Story Index to actual clips. |
| RWC-06 | Artie footage-organizing SOP | QUEUED | Low | Design-ready but not deployed — Artie not reliable enough to be a Phase 1 dependency (see I-23). Draft once Artie reliability proven. |

## AURA THAI ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| SOP-14-deploy | Deploy invoice_processor.py to Artie | OPEN — CHRIS | High | Files in outputs/. Artie does one-time setup (credentials, DRIVE_FOLDER_ID). Replaces manual invoice entry. |
| A-12 | Install Apps Script V2 (timeout fix) | IN PROGRESS — CHRIS | High | S55: paste outputs/aura-thai_invoice-system_apps-script_v2.gs into Apps Script editor, run syncIngredientsToDishMap. Root cause of every timeout: blocking ui.alert dialogs (+ Chris's popup block) — replaced with toasts. setupInvoiceSystem disarmed. |
| A-09 | COGS — Artie enter invoice backlog + weekly Sales by Period | IN PROGRESS | TOP | Foundation complete S43. Artie cleared to run. Waiting on data for first COGS analysis. |
| A-09b | Chris fill Dish Map col B (Dish Name(s)) | OPEN — CHRIS | High | 53 ingredients synced S45. Column B blank. Supplies → "Supply". Universal → "All Dishes". ~35 dish-specific. Unlocks COGS. |
| A-08b | Finance tab: rebuild to Google Sheet | OPEN | High | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-06b | Revenue tab: live data connection | Pending | Medium | Master Google Sheet → revenue.html reads on load. |
| A-11 | Aura Thai PATH-TO-BLACK plan | ❌ NEXT BUILD | TOP | Chris S55: Priority #1 over property/investing. Dedicated session, load P&L/Lavu data first. YTD −7.5%, Apr −11.3%. |
| A-10 | ezCater onboarding — complete paperwork | IN PROGRESS | High | Fee strategy + quick-ref doc delivered S42. Chris to complete platform setup. |
| A-07 | Decision Dashboard ops.radrooster.co | DONE S41 | — | Live at ops.radrooster.co/aura-thai. |
| A-08 | Aura Thai Finance tab | DONE S40 | — | Live at ops.radrooster.co. |
| A-04 | ARTIE SOP 13 + SOP 14 | DONE S43/S45 | — | SOP 13 done S43. SOP 14 (invoice_processor.py pipeline) built S45. Send to Artie: invoice_processor.py + SOP_14_invoice_processing.md. |

## INFRASTRUCTURE ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| I-23 | artie_report_sync.py cron fix | OPEN | High | Not firing since May 8. GH/DD/UE pipeline broken. |
| I-25 | Execute soul-file audit fixes (S55) | OPEN | High | 5 HIGH: dup ARTIE-RUNBOOK pointer (artie-config/ is retired), tracker ID collisions (RWC/AS/INV), EMPIRE_RULES needs ARCHIVED banner, CLAUDE-CORE header says V3 is V6. Dish Map col conflict RESOLVED S55: column B. 7 MEDIUM: stale FILE_MAP/SOUL_CHANGELOG/DECISIONS_LOG/CLAUDE-PROJECTS, dual CONTENT_LOGs, S53 collision, BOOT vs CORE load protocol. Report: soul-files_audit_S55 (outputs). Chris approves fix order. |
| I-06 | Daily digest cron #general | OPEN | Low | Deferred many sessions. |
| I-02 | Drive folder reorg | DEFERRED | Low | Parked. |
| B-01 | Pinyo Farms market validation | QUEUED | — | Parking lot until COGS done. |
| I-24 | Section anchors in shared files | DONE S41 | — | 33 anchors added. |

---

## EZCATER — A-10 DETAILS (S42)

### What was completed S42
- Competitor research: 7+ Long Beach Asian/Thai caterers scraped live on ezcater
- Fee structure locked: Fixed-rate delivery, 4 zones
- Quick-reference Word doc delivered: ezcater_quickref.docx (outputs folder)
- Platform strategy locked: Reliability Rockstar path, do not compete on price with weak performers

### Final fee table (locked by Chris)
| Zone | Distance | Delivery Fee | Order Minimum |
|------|----------|-------------|---------------|
| Zone 1 | 0-5 miles | $30.00 | $100 |
| Zone 2 | 6-10 miles | $40.00 | $150 |
| Zone 3 | 11-15 miles | $50.00 | $250 |
| Zone 4 | 16-20 miles | $60.00 | $350 |

### What Chris still needs to do
- Log into ezcater and complete onboarding form using quick-ref doc
- Set delivery fee type to Fixed-rate (platform recommended)
- Enter Zone 1-4 fee table above
- Set up menu with photos, individual packaging option on all items
- Enable Reliability Rockstar tracking from day one (100% on-time delivery)

---

## AURA THAI INVOICE SYSTEM — S43 STATUS
**Built S40, stabilized S43**

| Tab | Status | Owner |
|-----|--------|-------|
| Invoice Log | READY | Artie — enter invoices |
| Price Tracker | READY | Auto — run after every 2-3 invoices |
| Dish Map | READY (column D blank) | Chris — fill "Used In Dishes" column |
| Sales by Period | READY | Artie — weekly from Lavu |
| COGS by Dish | WAITING FOR DATA | Claude — analyze once data exists |

**What Artie needs:** ARTIE-RUNBOOK.md → SOP 14 (artie-config/ARTIE-RUNBOOK.md on GitHub)
**What Claude needs to run COGS:** Invoice Log + Sales by Period data for the same period

---

## 💼 INVESTMENT STRATEGY (Live — S46)

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| INV-01 | Open 529 for Auggie | ❌ Open | Chris | Intent confirmed S46. Education savings — better tax treatment than UTMA. |
| INV-02 | Open HSA for Chris + Wife | ❌ Open | Chris | Intent confirmed S46. Both self-employed — eligible. Triple tax advantage. |
| INV-03 | Open Roth IRA for Wife (2026) | ❌ Open | Chris | Intent confirmed S46. Wife has no retirement account currently. |
| INV-04 | Evaluate Solo 401k / SEP-IRA for both | ❌ Open | Claude + Chris | Self-employed = far higher limits than Roth alone. High priority S47. |
| INV-05 | Transition Auggie UTMA → broad index ETFs | ❌ Open | Claude + Chris | Current: TSLA, MSFT, META, HOOD, GOOGL, GLD. Too concentrated for 60-year horizon. |
| INV-06 | Build BTC positions for Wife + Auggie | ❌ Open | Claude + Chris | Chris wants BTC exposure for all three. Vehicle + size TBD after bucket definition. |
| INV-07 | Define strategic buckets (aggressive $, property target, timeline) | ❌ Open | Chris (S47) | BLOCKER. Nothing else maps until this is answered. First agenda item. |
| INV-08 | Move KuCoin holdings to cold storage | ❌ Open | Chris | Chris committed S55: 1.7 BTC → cold wallet. Execute before Sept BTC window. |


## 📋 SESSION 46 PRIORITY ORDER (Investment Strategy)

1. **INV-07** — Define strategic buckets (aggressive $, property target, timeline) — BLOCKER
2. **INV-05** — Auggie UTMA → ETF transition plan


---

## 💼 INVESTMENT STRATEGY

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| INV-01 | Enable options trading on Fidelity Roth IRA (Tier 1) + verify ≥100 KO / ≥300 SCHD | ❌ Open | Chris | Playbook v1 built S55 (outputs/pinyo-empire_options-income-playbook_v1.md). Realistic income $105–195/mo tax-free at current IV. Apply → verify holdings → deploy Trades 1-2. |
| INV-02 | Property target markets | ✅ ANSWERED S55 — track DEFERRED | Chris | LA/OC/Long Beach, STR-friendly, multi-unit house-hack + ADU (Pasadena model, ref 606 Palisade St 91103). Window 2027–2032. CA insurance = known risk; backup = similar-climate state. WHOLE PROPERTY TRACK DEFERRED — Priority #1 = Aura Thai to black (Chris, S55). |
| INV-03 | Kate ITIN application (Form W-7) | ❌ Queued | Kate/Chris | File W-7 with IRS. 6-11 week turnaround. Unlocks LLC membership for property equity. |
| INV-04 | Family Trust + ILIT + insurance-based generational wealth education | ❌ Queued | Claude + Chris | Chris confirmed S55: wants full education/plan incl. how the wealthy use insurance. Attorney framework needed for execution. |
| INV-05 | Auggie UTMA reallocation | ❌ Open | Chris | Concentrated single stocks (META, MSFT, TSLA — all underwater). Reallocate to VTI/VXUS for 60-year compounding window. |
| INV-06 | First DSCR deal evaluation | ❌ Queued | Claude + Chris | After INV-02 (markets identified). Run numbers on first candidate property. DSCR ≥ 1.25 target. |
| INV-07 | Golfii cash deployment plan | ❌ Open | Chris + Golfii | $6,810 idle in joint account. 30+ year runway — needs to work harder. |
| INV-09 | Roth cash allocation: KO CSP vs BTC window (Sept 15–Oct 31) | ✅ RESOLVED S55-cont | — | Fidelity-crypto wall (Rule 1) frees all Roth cash for CSPs; BTC window = KuCoin only. |
| INV-10 | MCD entry decision | ❌ DECISION | Chris | $270 = −20% off ATH, near 52-wk low (7/1). CSP impossible ($26K lock) → direct share tranches. Name trigger + tranche 1 size. |
| INV-11 | Crypto exit plan at BTC $120K+ | ❌ Queued | Claude | Chris S55: hold to $120K+, cash out, restructure properly. Build: sell order, tax exposure, proceeds allocation. |
| INV-12 | Correction battle plan | ❌ Queued | Claude | Formalize +20% trim rule, quality watchlist with buy ladders, refresh 4-tranche crash deployment. |
| INV-13 | Park $5K USDT on KuCoin + set ladder limit orders $50/45/40K | ❌ Open | Chris | APPROVED S56: $2,000 @ $50K / $1,500 @ $45K / $1,500 @ $40K (~0.1108 BTC, ~$45.1K avg if all fill). |
| INV-14 | Open Auggie 529 this month — $300/mo auto-draft, 100% equity | ❌ Open | Chris | Starts 15-yr 529→Roth clock (eligible 2041). Dip-adds APPROVED S56. Vehicle pends INV-15 SB 529 answer. |
| INV-15 | Tax preparer meeting — 5 questions (playbook §7) | ❌ Open | Chris | MFS vs MFJ, CA community property MAGI, SB 529, pro-rata, Form 8606. Blocks INV-14 vehicle + INV-16. |
| INV-16 | Golfii backdoor Roth — Trad+Roth IRA, 70/30 growth/dividend | ❌ BLOCKED | Chris + Golfii | On INV-15. Allocation APPROVED S56. Cap: min($7,500, her W-2). |

---

## 📋 SESSION 47 PRIORITY ORDER (Investment Strategy)

**S47 Summary (2026-06-22):**
- Full portfolio loaded: $114,836.59 across Chris ($87,475.43), Golfii ($23,727.26), Auggie ($3,633.90)
- Three bucket framework: 🔴 Aggressive $1-2K | 🟡 Medium-term (profit rotation) | 🟢 Property war chest
- Covered calls playbook: KO (1 contract) + SCHD (3 contracts) in Fidelity Roth → ~$180/month tax-free
- Cash-secured puts: use Roth cash ($9,694) to generate premium while waiting for crash
- Crash deployment ladder: −10% → 20%, −20% → 30%, −30% → 30%, −40%+ → 20%
- DSCR loans = primary property vehicle (no income docs — based on rental cash flow)
- Mom co-borrower: 800 FICO + $1,200/month SS + born 1959 → extends to 20-property capacity
- Kate ITIN path confirmed: Form W-7 → LLC membership → property equity
- Family Trust + ILIT → deferred to S48

**S48 STARTS WITH:** Load `checkpoint_S47-investment-strategy_2026-06-22.md` from Investment Strategies project. First question: which property markets (city/state)? Unlocks first DSCR deal evaluation.

---

## 📋 SESSION 55 PRIORITY ORDER

1. **A-11** — Aura Thai path-to-black plan (Priority #1 per Chris)
2. **INV-01** — Fidelity Tier 1 approval + verify holdings (Chris) → deploy covered calls
3. **INV-09 / INV-10** — Roth cash + MCD trigger decisions (Chris)
4. **INV-08** — 1.7 BTC → cold wallet (Chris, before Sept 15)
5. **RWC-04** — Story Index build (blocked on Chris: trip count + sheet location)

---

## 📋 SESSION 56 PRIORITY ORDER (executed)

S56 (2026-07-01): Family Investment Playbook v2 LOCKED — all three PROPOSED items approved + $5K ladder cash committed. Playbook updated on GitHub (sessions/S55/). Chris's physical queue: INV-13 (USDT + limit orders), INV-08/cold wallet, INV-15 (tax meeting), INV-14 (529). INV-16 blocked on INV-15.

---

## 🔗 Graph Links
[[HOME]] | [[SPRINT]] | [[EMPIRE_STATUS]] | [[SESSION_HISTORY]]
[[aura-thai]] | [[vine-arbitrage]] | [[pinyo-farms]] | [[ai-ventures]] | [[roam]]

## AURA SWEET ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| AS-01 | Finalize sizes, prices, strategy, launch action steps | OPEN | TOP | S53 primary task |
| AS-02 | Competitive analysis: Somisomi vs Aura Sweet | OPEN | High | Before finalizing strategy — Somisomi is direct competitor on ice cream/gelato |
| AS-03 | Walk the block: verify Somisomi + Ding Tea menus/pricing | OPEN - CHRIS | High | Physical walkthrough before launch. Both next to Ramen Hub. |
| AS-04 | Confirm brand name final ("Aura Sweet" vs alternatives) | OPEN - CHRIS | High | Blocks packaging and social setup |
| AS-05 | Confirm packaging budget | OPEN - CHRIS | High | Blocks packaging sourcing |
| AS-06 | Decide: ice cream/gelato in-house vs sourced | OPEN - CHRIS | High | Changes cost structure and sizing options |
| AS-07 | Check permits for second brand under same kitchen | OPEN - CHRIS | High | Local health department — required before launch |
| AS-08 | First Fridays pop-up plan — August 2026 | OPEN | Medium | July skipped. August = first opportunity. Plan event format, signage, products. |
| AS-09 | Register Aura Sweet on DoorDash | OPEN | High | Launch step 1 per business plan |
| AS-10 | Create Aura Sweet Instagram account | OPEN - CHRIS | High | Chris is content creator. Reels primary channel. |
