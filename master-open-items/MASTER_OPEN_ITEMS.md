# MASTER_OPEN_ITEMS.md
**Living task tracker for the Pinyo Empire.**
**Last Updated:** 2026-06-20 | Session 43
**GitHub:** `master-open-items/MASTER_OPEN_ITEMS.md`

---

## AURA THAI ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| SOP-14-deploy | Deploy invoice_processor.py to Artie | OPEN — CHRIS | High | Files in outputs/. Artie does one-time setup (credentials, DRIVE_FOLDER_ID). Replaces manual invoice entry. |
| A-09 | COGS — Artie enter invoice backlog + weekly Sales by Period | IN PROGRESS | TOP | Foundation complete S43. Artie cleared to run. Waiting on data for first COGS analysis. |
| A-09b | Chris fill Dish Map col B (Dish Name(s)) | OPEN — CHRIS | High | 53 ingredients synced S45. Column B blank. Supplies → "Supply". Universal → "All Dishes". ~35 dish-specific. Unlocks COGS. |
| A-08b | Finance tab: rebuild to Google Sheet | OPEN | High | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-06b | Revenue tab: live data connection | Pending | Medium | Master Google Sheet → revenue.html reads on load. |
| A-10 | ezCater onboarding — complete paperwork | IN PROGRESS | High | Fee strategy + quick-ref doc delivered S42. Chris to complete platform setup. |
| A-07 | Decision Dashboard ops.radrooster.co | DONE S41 | — | Live at ops.radrooster.co/aura-thai. |
| A-08 | Aura Thai Finance tab | DONE S40 | — | Live at ops.radrooster.co. |
| A-04 | ARTIE SOP 13 + SOP 14 | DONE S43/S45 | — | SOP 13 done S43. SOP 14 (invoice_processor.py pipeline) built S45. Send to Artie: invoice_processor.py + SOP_14_invoice_processing.md. |

## INFRASTRUCTURE ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| I-23 | artie_report_sync.py cron fix | OPEN | High | Not firing since May 8. GH/DD/UE pipeline broken. |
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
| INV-08 | Move KuCoin holdings to cold storage (partial) | ❌ Open | Chris | $144K+ on KuCoin = custody risk. KuCoin hacked 2020. Hardware wallet recommended. |


## 📋 SESSION 46 PRIORITY ORDER (Investment Strategy)

1. **INV-07** — Define strategic buckets (aggressive $, property target, timeline) — BLOCKER
2. **INV-05** — Auggie UTMA → ETF transition plan
3. **INV-04** — Solo 401k / SEP-IRA evaluation
4. **INV-06** — BTC building strategy for all three holders
5. **B-01** — Pinyo Farms (still queued pending COGS)

**Start S47 with:** Load soul files. Open `Pinyo_Portfolio_Tracker_v1.xlsx` (Investment Strategies folder). Step 2: Ask Chris the three bucket questions. Then build per-holder strategy.

