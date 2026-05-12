# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude at handoff — automatic
**Last Updated:** 2026-05-11 | Session 35 (extended)
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## ACTIVE ITEMS — S35 DIGEST

| ID | Item | Status |
|----|------|--------|
| A-05 | Aura Thai: wire email pipeline → aura_thai_finance output | ❌ Next session — see full spec below |
| A-02 | Aura Thai: UberEats price impact analysis | ⏳ UE Apr/May files in Drive dump, ready to process |
| I-23 | Artie cron audit — diagnose email pipeline trigger | ❌ Open — is artie_report_sync.py actually firing? |
| I-06 | Daily digest cron for #general | ❌ Open — decide time with Chris |
| I-07 | 9 cron job backends | ❌ Open — dedicated session |
| I-17 | Decommission old Cloudflare Tunnel | ❌ Open |
| A-01 | Aura Thai: Lavu as primary data source | ❌ Blocked — Lavu XLS needs Google Sheets conversion |
| A-03 | Aura Thai: push finance dashboard to ops.radrooster.co/aura-thai | ❌ Pending real data |
| A-04 | Aura Thai: ARTIE SOP 13 (Monthly Finance Update) | ❌ Draft exists, needs formal write |
| B-01 | Pinyo Farms market validation | ❌ Open — queued |

---

## AURA THAI PIPELINE — FULL ARCHITECTURE (do not ask Chris to re-explain)

### What already exists (built S20)
- `artie_report_sync.py v2` — 13-parser email pipeline
- DD, UE, and GH automatically email reports to Artie
- Artie scans incoming email, detects platform reports, runs the parser script
- **This trigger already works — do not rebuild it**

### What the output currently does
- Was originally writing to Drive + reporting to Telegram (pre-Discord migration)
- Is NOT yet connected to `aura_thai_finance` Google Sheet
- This is the gap to fix next session

### What needs to be built (A-05)
1. Update `artie_report_sync.py` output to write data into `aura_thai_finance` Google Sheet (ID: `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE`)
2. After successful write: move processed source file to `_DELETE_ME/` folder in Drive (Chris empties this folder manually — Artie and Claude cannot delete files)
3. Report to Discord #finance after each run: "✅ Aura Thai finance updated — [platform] [date range]"

### Reconcile file = aura_thai_finance
- `aura_thai_finance` Google Sheet IS the master reconcile file
- All platforms feed into it: GH + DD + UE + Lavu (when available)
- **GrubHub data is already in it** (Jan 2–May 8, 124 rows) — GH source files are safe to move to `_DELETE_ME/`
- **DD and UE data is NOT yet in it** — do not move/delete those source files until confirmed in sheet
- **Lavu data is NOT yet in it** — blocked on XLS → Google Sheets conversion

### I-23 diagnosis — check this first
Before building A-05, confirm whether `artie_report_sync.py` is actually firing:
- Check Artie's cron logs for recent runs
- Check if platform emails are arriving in Artie's inbox
- If not firing: fix the cron trigger first, then wire the output

---

## INFRASTRUCTURE — KEY FACTS (do not ask Chris)
- **GitHub repo:** `~/Documents/Claude/sharedfolder` on Chris's Mac
- **GitHub PAT:** embedded in push script + saved at `~/.pinyo_github_pat` (Mac)
- **Push script:** `outputs/handoff/push_handoff.sh` — run from Terminal.app, no cd needed
- **Git identity:** configured as Chris / neosubz@gmail.com (set S35)
- **Cloudflare Pages:** auto-deploys on every push to main → ops.radrooster.co

---

## SPRINT GOAL — MAY 2026

**Theme:** Get real data flowing into aura_thai_finance automatically. Email pipeline → sheet → _DELETE_ME folder. Then Lavu. Then dashboard live.

---

## BUSINESSES — CURRENT FOCUS

| Business | Status | Priority Action |
|----------|--------|-----------------|
| Aura Thai | 🟡 Active | Wire email pipeline to aura_thai_finance (A-05). UE price analysis (A-02). |
| Vine Arbitrage | 🟢 Running | Artie handles — no Claude action needed |
| Pinyo Farms | ⏳ Planning | Market validation — not started, B-01 |
| AI Ventures | ⏳ Planning | Restaurant subscription stream — not started |
| Roam | ⏳ Planning | Master content plan — not started |

---

## PROTOCOL — ANALYZE BEFORE EXECUTE (added S35)
> For any strategy touching pricing, menu, marketing spend, or operations — model scenarios first, define decision criteria, get approval, then move.

---

## BLOCKED — DO NOT TOUCH

| Item | Blocker |
|------|---------|
| O-03 Aura Thai Lavu integration | Chris needs to complete Lavu setup |
| O-04 Aura Thai Shift Close integration | Chris needs to complete setup |
| A-01 Real data processor run | Lavu XLS → Google Sheets conversion needed |

---

## S35 COMPLETED

| Item | Done |
|------|------|
| DoorDash price impact analysis — real data, dd_price_impact.html generated | ✅ S35 |
| Aura Thai profile updated — businesses/aura-thai/aura-thai.md | ✅ S35 |
| Weekly price monitoring scheduled (every Monday 9am → #finance) | ✅ S35 |
| "Analyze before execute" protocol established | ✅ S35 |
| GitHub repo cloned to ~/Documents/Claude/sharedfolder on Chris's Mac | ✅ S35 |
| Git identity set (Chris / neosubz@gmail.com) | ✅ S35 |
| Handoff push script working end-to-end | ✅ S35 |

---

## 🔗 Graph Links
[[HOME]] | [[EMPIRE_STATUS]] | [[MASTER_OPEN_ITEMS]]
[[aura-thai]] | [[vine-arbitrage]] | [[pinyo-farms]] | [[ai-ventures]] | [[roam]]
