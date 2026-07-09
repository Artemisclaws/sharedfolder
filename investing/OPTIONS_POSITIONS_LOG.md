# OPTIONS_POSITIONS_LOG.md — Wheel Cycle Source of Truth
**Account:** Chris's Fidelity Roth
**GitHub:** `investing/OPTIONS_POSITIONS_LOG.md`
**Maintained by:** Claude/Chris, updated on every fill (never let this go stale — Artie's reports are only as good as this file)
**Governing rules:** `sessions/S55/pinyo-family_investment-playbook_v2.md` §5, v1.1–v1.3

---

## OPEN POSITIONS (update on every fill, close, assignment, or roll)

| Ticker | Type | Side | Contracts | Strike | Expiration | Opened | Premium collected | Status |
|--------|------|------|-----------|--------|------------|--------|--------------------|--------|
| KO | CALL | SELL | 1 | $87.50 | 2026-08-21 | 2026-07-09 | **$0.88/contract, $88.00 gross / $87.35 net** | **FILLED** — price improvement over $0.82 limit |
| SCHD | CALL | SELL | 3 | $33.00 | 2026-08-21 | 2026-07-09 | **$0.32/contract, $96.00 gross / $94.05 net** | **FILLED** — price improvement over $0.30 limit |
| SCHD | PUT | SELL | 1 | $32.00 | 2026-08-07 | PENDING ENTRY | ~$0.25 (live bid, 7/9) | Not yet placed — expiration corrected to Aug 7 (actual Friday exp, not Aug 6) |
| VZ | PUT | SELL | 1 | $40.00 | 2026-08-21 | PENDING ENTRY | ~$0.96 (live bid, 7/9) | Not yet placed — real premium ~2x the theoretical estimate, confirms IV spike thesis |
| VZ | PUT | SELL | 1 | $40.00 | 2026-08-21 | PENDING ENTRY | — | Not yet placed |

*Update the "Opened" and "Premium collected" columns the moment each order actually fills on Fidelity — do not log an order as open until confirmed filled.*

---

## UNDERLYING SHARE POSITIONS (ground truth — do not re-ask Chris)

| Ticker | Shares | Cost basis (weighted avg) | Covered-call-eligible | Odd lot |
|--------|--------|----------------------------|------------------------|---------|
| KO | 113 | ~$48.83 | 100 (1 contract) | 13 |
| SCHD | 316 | ~$27.13 | 300 (3 contracts) | 16 |

**Cash buffer status:** $9,723 total Roth cash → $3,200 (SCHD put) + $4,000 (VZ put) = $7,200 committed → **$2,523 (26%) uncommitted, within the Collateral Buffer Rule (min 5–10%).**

---

## WATCH DATES — refresh every cycle, do not assume these stay fixed

| Event | Ticker | Date | Relevance |
|-------|--------|------|-----------|
| Earnings | KO | 2026-07-28, before open | Falls inside the Aug 21 call/expiration window — KO call strike widened to $86 to compensate |
| Earnings | VZ | 2026-07-24 | **Active** — inside the Aug 21 put expiration; $40 strike chosen with earnings cushion in mind |
| Earnings | PG | 2026-07-29 | Relevant once PG tier is funded (v1.2) |
| Earnings | JNJ | 2026-07-15 | Relevant once JNJ tier is funded (v1.2) — do not enter a fresh CSP in the days right before this date |
| Ex-dividend | KO | ~2026-09-11 to 09-15 (est.) | Outside current cycle's expirations — re-verify closer to date |
| Ex-dividend | SCHD | ~2026-09-23 (est.) | Outside current cycle's expirations — re-verify closer to date |

---

## REPORT LOG (Artie/Claude appends here after every morning/close update — do not overwrite history)

*(empty — first entry lands once Phase 3 automation goes live, or once Chris/Claude runs the first manual report)*

---

## Graph Links
Governing playbook: `sessions/S55/pinyo-family_investment-playbook_v2.md`
EMPIRE_STATUS / SPRINT: `00-load-me/SPRINT.md`, `empire-status/EMPIRE_STATUS.md`
