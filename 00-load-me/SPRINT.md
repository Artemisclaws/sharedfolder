# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S49 | 2026-06-23
**Current session:** S50 (increment by 1 each new session — do not confuse data model labels like 'S39' with session numbers)
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## ⚠️ LOAD NOTE — TOKEN EFFICIENCY
Do NOT load SESSION_HISTORY or MASTER_OPEN_ITEMS every session.
Pull them only if SPRINT.md session number is behind the latest known session.

---

## BUILD PHILOSOPHY — LOCKED S46 (applies to everything)
1. Simple first. Automate second. Scale third.
2. One function, one job. No dependencies on things that can break.
3. Manual before automated. Automation is always the end goal.
4. Phase 1 (manual) → 2 (script) → 3 (AI assist) → 4 (full auto). Never skip.
5. Design so AI can take it over later — manual is a placeholder, not a destination.

---

## ACTIVE ITEMS — S46 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| **S50** | **ARTIE-RUNBOOK.md — rewrite to Bedrock Standard** | ✅ **COMPLETE S50** | V2 pushed. 3 working SOPs (Soul Sync, Recovery, Cron Restore). 8 pending SOPs marked DO NOT RUN until scripts built. Commit 3846b498. |
| A-07 | Price Tracker: run populatePriceTrackerDirect | 🔴 NEXT | Script ready in workspace. Paste into Apps Script, run once. Seeds 8 ingredients. |
| A-08 | Invoice Log: establish manual entry process | 🔴 Phase 1 | Who enters data when delivery arrives? Define process before automating. |
| A-06 | Aura Thai Decision Dashboard | 🔴 Priority | Data in Drive. Needs Lavu XLS conversion first. |
| A-09 | ezCater menu upload | ⏳ Pending | Plan built (aura_thai_ezcater_menu_plan_v1.md). Needs upload to platform. |
| A-10 | Food cost model: fix Basil + Green Bean | ⏳ Pending | Basil actual $5.95 vs model $3.95. Green Bean $2.95 vs $1.29. Both understated. |
| A-02 | UberEats price impact — complete | ⏳ Partial | Only 5 days POST data. Easter confound. |
| I-23 | artie_report_sync.py cron fix | ⏸ DEPRIORITIZED | Not S50 priority. Fix Artie runbook first. |
| A-04 | ARTIE SOP 13 — cron fix + monthly finance | ❌ Open | Write to ARTIE-RUNBOOK.md. |
| I-06 | Daily digest cron for #general | ❌ Open | |
| I-17 | Decommission old Cloudflare Tunnel | ❌ Open | |
| B-01 | Pinyo Farms market validation | ❌ Queued | |
| S49 | Mac file organization system | 🔴 S49 | Checkpoints scattered. No system for what goes where. Design this session. |
| S49 | Core file bug audit | ✅ DONE S49 | All 4 files audited. CLAUDE-CORE V4 pushed. EMPIRE_STATUS + SPRINT updated. |

---

## AURA THAI — CURRENT SYSTEM STATE

| System | Status |
|--------|--------|
| Invoice Log | ❌ EMPTY — wiped by setupInvoiceSystem S46 |
| Price Tracker | 🔲 PENDING — run populatePriceTrackerDirect |
| setupInvoiceSystem | 🚫 BANNED — wipes data every run |
| updatePriceTracker | ⏸ On hold — needs Invoice Log data |
| ezCater plan | ✅ Built — not yet uploaded |

**We are in Phase 1.** Manual entry only until Invoice Log is stable.

---

## CORRECTED DATA MODEL (S39 — do not revert)
- **Lavu = primary revenue source.** Lavu captures ALL sales.
- GH/DD/UE contribute TO Lavu totals — not separate baselines.
- May 2026 Lavu avg: ~$2,200/day net.

---

## AURA THAI PIPELINE — KEY FACTS
- Sheet ID: `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE`
- Apps Script ID: `1lNMZ_Hvwj-4ncLGy0nWN9rEr6xJYADZxM9OpOTTloNfGsAIA0DV-uDzr`
- artie_report_sync.py: NOT firing since May 8 (I-23)
- Rad Rooster: NOT launched

---

## BUSINESSES — CURRENT FOCUS

| Business | Status | Priority Action |
|----------|--------|-----------------|
| Aura Thai | 🔴 Active — urgent | Price Tracker (A-07) → Invoice Log process (A-08) → Dashboard (A-06) |
| Vine Arbitrage | 🟢 Running | Artie handles |
| Pinyo Farms | ⏳ Planning | Market validation — B-01 |
| AI Ventures | ⏳ Planning | Not started |
| Roam | ⏳ Planning | Not started |

---

## INFRASTRUCTURE — KEY FACTS
- GitHub PAT: Drive fileId `1528C9LxOxjxQvS5iUM8vFjE50clNM1NT` — Drive MCP only, no local file paths
- CLAUDE-CORE.md: V4 (S49) — Step 6 rewritten, CHANGE CONTROL added, soul files locked
- Cloudflare Pages: auto-deploys on push → ops.radrooster.co

---

## BLOCKED — DO NOT TOUCH
| Item | Blocker |
|------|---------|
| Lavu as live data source | Lavu API setup incomplete (Chris) |
| O-04 Shift Close integration | Chris needs to complete setup |
| setupInvoiceSystem | 🚫 PERMANENTLY BANNED — wipes all data every run, always times out |

## 🔗 Graph Links
[[HOME]] | [[EMPIRE_STATUS]] | [[MASTER_OPEN_ITEMS]]
