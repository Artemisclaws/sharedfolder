# MASTER_OPEN_ITEMS.md
**Living task tracker for the Pinyo Empire.**
**Last Updated:** 2026-06-10 | Session 42 (ezcater onboarding)
**GitHub:** `master-open-items/MASTER_OPEN_ITEMS.md`

---

## AURA THAI ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| A-09 | COGS tracking system | OPEN | TOP | Weekly food cost entry. Target 28-32% revenue. |
| A-08b | Finance tab: rebuild to Google Sheet | OPEN | High | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-06b | Revenue tab: live data connection | Pending | Medium | Master Google Sheet → revenue.html reads on load. |
| A-10 | ezCater onboarding — complete paperwork | IN PROGRESS | High | Fee strategy + quick-ref doc delivered S42. Chris to complete platform setup. |
| A-07 | Decision Dashboard ops.radrooster.co | DONE S41 | — | Live at ops.radrooster.co/aura-thai. |
| A-08 | Aura Thai Finance tab | DONE S40 | — | Live at ops.radrooster.co. |
| A-06 | Aura Thai Decision Dashboard | DONE S40 | — | Revenue tab live. |

## INFRASTRUCTURE ITEMS

| ID | Item | Status | Priority | Notes |
|----|------|--------|----------|-------|
| I-23 | artie_report_sync.py cron fix | OPEN | High | Not firing since May 8. GH/DD/UE pipeline broken. |
| A-04 | ARTIE SOP 13 | OPEN | Medium | Write to ARTIE-RUNBOOK.md. |
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
