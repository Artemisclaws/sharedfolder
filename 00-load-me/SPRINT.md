# SPRINT.md — Active Work Digest
**Updated:** S52 | 2026-06-24

---

## START HERE — THIS OVERRIDES EVERYTHING BELOW

> **YOU ARE CLAUDE. YOU ARE STARTING SESSION S53.**
> Last real session = S52 (2026-06-24).

| Field | Value |
|-------|-------|
| **You are in** | Session S53 |
| **Last session** | S52 — 2026-06-24 |
| **What S52 completed** | Aura Sweet customer avatar built. Demographic research (Bixby Knolls + DoorDash). BIXBY_KNOLLS_MARKET.md created. Sizing standardized (8oz cup / 16oz pint). Competitors confirmed: Somisomi + Ding Tea next to Ramen Hub. EMPIRE_STATUS updated with full Aura Sweet section. |
| **First task S53** | Aura Sweet: Competitive analysis (Somisomi vs Aura Sweet) → finalize sizes, prices, strategy, launch action steps |
| **Also pending** | Artie cron tasks below — TeamViewer paste still ready, not yet executed |

**Each session: update this table before handoff. Increment session number. Replace last session summary. Set next task.**

---

## TEAMVIEWER PASTE — READY TO RUN (pending from S52)

Paste in Artie's terminal in order:

```bash
# 1 — Remove dead Vine cron
crontab -l | grep -v vine_review_writer | crontab -

# 2 — Add 6-hour sync cron with nohup
(crontab -l 2>/dev/null; echo "0 */6 * * * nohup bash /home/artemis/.openclaw/workspace/sync_soul.sh > /home/artemis/.openclaw/workspace/sync_last.log 2>&1 &") | crontab -

# 3 — Verify
crontab -l
```

Then run sync to pull artie_handoff.py:
```bash
bash /home/artemis/.openclaw/workspace/sync_soul.sh
```

Then confirm handoff script loaded:
```bash
python3 /home/artemis/.openclaw/workspace/artie_handoff.py read
```

---

## ACTIVE ITEMS

| ID | Task | Status | Notes |
|----|------|--------|-------|
| AS-01 | Aura Sweet: finalize sizes, prices, strategy, action steps | OPEN | S53 primary task |
| AS-02 | Competitive analysis: Somisomi vs Aura Sweet | OPEN | Do before finalizing strategy |
| AS-03 | Walk the block: verify Somisomi + Ding Tea menus/pricing | OPEN - CHRIS | Physical walkthrough before launch |
| AS-04 | Confirm 4 open questions (brand name, packaging budget, in-house vs sourced, permits) | OPEN - CHRIS | Blocks launch planning |
| AS-05 | First Fridays pop-up planning — August 2026 | OPEN | July skipped — August is first opportunity |
| S52-1 | Artie cron: remove Vine, add 6hr sync | OPEN | TeamViewer paste ready above |
| S52-2 | Run sync_soul.sh + verify artie_handoff.py | OPEN | After cron confirmed |
| A-07 | Price Tracker: run populatePriceTrackerDirect | OPEN - CHRIS | Apps Script → Investment Strategies folder |
| VINE | Amazon Vine reinstatement | BLOCKED | Kicked off for late reviews. Plan needed. |

---

## BLOCKED / DEPRIORITIZED

| ID | Item | Why |
|----|------|-----|
| A-06 | Aura Thai Decision Dashboard | Deprioritized |
| I-23 | artie_report_sync.py cron | Cron exists on Artie's machine — verify before fixing |
| A-02 | UE price analysis | Partial — pick up when A-06 resumes |

---

## PERMANENTLY BANNED

| Item | Reason |
|------|--------|
| setupInvoiceSystem | Wipes all data + always times out. Never run again. |

---

## INFRASTRUCTURE STATE (as of S52)

| Item | Status |
|------|--------|
| CLAUDE-CORE.md | V6 S51 — CHRONICLE protocol added |
| BIXBY_KNOLLS_MARKET.md | LIVE S52 — bixby-knolls/BIXBY_KNOLLS_MARKET.md |
| EMPIRE_STATUS.md | Updated S52 — Aura Sweet section + Bixby Knolls ref |
| CHRONICLE | LIVE — journal/ + CONTENT_LOG.md |
| ARTIE-CORE.md | V6 — Session start/end protocol |
| ARTIE-RUNBOOK.md | V2 Bedrock — 3 working SOPs |
| artie_handoff.py | On GitHub — needs sync to pull to Artie |
| Soul sync cron (6hr) | PENDING — TeamViewer paste ready |
| Vine cron (dead) | PENDING removal — TeamViewer paste ready |

---

*Load bixby-knolls/BIXBY_KNOLLS_MARKET.md for any Aura Sweet or Atlantic Ave session.*
