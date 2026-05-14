# MASTER_OPEN_ITEMS.md
**Source of truth for all open tasks across the Pinyo Empire.**
**Last Updated:** 2026-05-13 | Session 36
**Rule:** Items are ONLY marked ✅ when personally confirmed completed in session. Never assumed.

---

## HOW TO USE THIS FILE
- Start every session: pull this file from GitHub
- End every session: update statuses, add new items, push back
- **This file IS the handoff.** No separate handoff files. Reference this + SESSION_HISTORY.md.
- Session handoffs = this file + 1 sentence of where to start next session.

---

## 🔴 INFRASTRUCTURE & SYSTEM

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| I-02 | Drive + GitHub restructure (hybrid Musk/Bezos/Munger) | 🔄 In Progress | S29 | GitHub brain done ✅. Drive folder skeleton + Artie soul migration still needed. |
| I-04 | Artie HTML dashboard generator script | ❌ Open | Future | generate_dashboard.py on Artie — reads EMPIRE_STATUS, writes index.html |
| I-05 | Drive flag watcher cron (15-min) | ❌ Open | Future | Checks REGEN_DASHBOARD.flag, regenerates if found |
| I-06 | Daily digest cron for #general | ❌ Open | Session 29+ | Decide time with Chris, then build |
| I-07 | 9 cron job backends | ❌ Open | Dedicated session | All 9 non-functioning crons need backends built |
| I-08 | Telegram → Discord full migration | 🔄 In Progress | Future | Cron redirect done; backends and full switchover pending |
| I-09 | Live market data for morning briefing | ❌ Open | Future | Section 1 of briefing currently skipped |
| I-10 | Artie bot token → env variable | ❌ Open | Session 29+ | Move from file to `export DISCORD_BOT_TOKEN=` in .bashrc on Artie machine |
| I-12 | Telegram thread routing test | ⚠️ Unconfirmed | Artie | SOP 11 written, test message never confirmed landed in Finance thread |
| I-13 | ARTIE_DASHBOARD_PROTOCOL.md → ARTIE-STANDARDS | ⚠️ Unconfirmed | Chris/Artie | Written S22, never confirmed loaded |
| I-14 | Delete old EMPIRE_STATUS Google Doc | ❌ Open | Chris | Drive ID: 1AMnMkAzD8xoYsGHwDRRl7-VRL2OADb6irVsnZdFVpoQ |
| I-15 | Delete 4 old files on Mac/Aura Thai | ❌ Open | Chris (manual) | Shell is read-only — must delete in Finder |
| I-16 | MASTER_INDEX.md — keep current | 🔄 Ongoing | Each session | Verify it reflects current file locations |
| I-17 | Decommission old Cloudflare Tunnel on Artie | ❌ Open | Session 29+ | ops.radrooster.co now on Pages — tunnel (e1588a4f.cfargotunnel.com) no longer needed |
| I-18 | Artie soul files → GitHub soul/artie/ | ✅ Done | S30 | All 5 files pushed. ARTIE-CORE V4 has sync_soul.sh with GitHub raw URLs. EMPIRE_STATUS updated. |
| I-19 | Drive folder skeleton (PROJECTS, DATA, JOURNAL, REFERENCE, _ARCHIVE) | ✅ Done | S31 | Folders created on Drive. PROJECTS + 5 business subfolders. Chris drags files. |
| I-20 | THINKING_OS section — remove from ARTIE-STANDARDS | ✅ Done | S31 | Removed L132–222. One-line pointer to soul/shared/THINKING_OS.md added. |
| I-21 | Soul file architecture — build SHARED-CORE.md + handoff keyword | ✅ Done | S32 | SHARED-CORE.md + handoff keyword + boot-loader delivered. |
| I-22 | SHARED-CORE.md content rebuild — coaching + RPG game | ✅ Done | S32 | Coaching rebuilt S31 context. RPG ledger live. Background layer active. |

---

## 🟡 OPERATIONS & AUTOMATION

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| I-23 | Artie automated task audit — crons not triggering | 🔍 Diagnosed | S37 | **ROOT CAUSE (S36):** cron not firing since ~May 8. GH daily PDFs arriving at 3:34 AM May 10/11/12 — all unprocessed. GH CSV in aura_thai_finance stops at May 8 = 4 days missed. **Fix needed S37:** check cron logs, restart cron, verify email detection logic. Artie SOP needed (see A-04). |
| A-01 | Aura Thai: Lavu XLS → Google Sheets | ❌ Blocked | Chris | Lavu setup not complete. Blocked on Chris. Once unblocked: convert Lavu export → aura_thai_finance sheet. |
| A-02 | UberEats price impact analysis | 🔄 Partial | S37 | **S36 progress:** ue_price_impact.html v2 in /outputs. Key finding: ticket +34.7% vs March. Easter confound identified. **Still needed:** Jan UE file (Drive folder: 19_v1W_TvzZ8OilqRDzsN5PPJFytJYphw — search title "2026-01") + full Apr 14-30 data. |
| A-03 | Push aura_thai_finance.html to ops.radrooster.co | ❌ Open | S37+ | Push to GitHub dashboard/ folder → auto-deploys to ops.radrooster.co/aura-thai |
| A-04 | ARTIE SOP 13 — Monthly Finance Update | ❌ Open | S37 | Write Artie runbook: check cron logs, restart cron, verify email detection for GH/DD/UE. Update ARTIE-RUNBOOK.md. |
| A-05 | Wire email pipeline output to aura_thai_finance sheet | ❌ Open | S37 | Sheet ID: 1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE. GH data already in sheet. DD + UE NOT yet loaded (do NOT move source files until confirmed). After successful write: move processed files to _DELETE_ME/. Report to #finance after each run. |
| O-01 | Playwright downloader (DD/UE) | ❌ Open | Dedicated session | artie_playwright_downloader_UPDATED.py — reads pending_downloads.json, bypasses auth wall |
| O-02 | Daily financial tracking SOP (AI Ventures) | ❌ Open | Future | SOP for Artie — daily financials → Vine → secondary |
| O-03 | Aura Thai: Lavu integration | ❌ Blocked | Chris | Blocked on Chris completing Lavu setup |
| O-04 | Aura Thai: Shift Close integration | ❌ Blocked | Chris | Blocked on Chris |
| O-05 | Aura Thai: Grubhub confirmed | ⚠️ Unconfirmed | Chris | Markup live but not confirmed working |

---

## 🟢 BUSINESS STRATEGY (Claude + Chris research sessions)

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| B-01 | Pinyo Farms market validation research | ❌ Open | Claude + Chris | Phase 1 greenlit, research not started |
| B-02 | Roam master content plan | ❌ Open | Claude + Chris | No Artie tasks until plan complete |
| B-03 | AI Ventures: restaurant subscription stream | ❌ Open | Claude + Chris | Stream 2 defined, not planned |

---

## ✅ CONFIRMED DONE (permanent record)

| Item | Completed | Session |
|------|-----------|---------|
| Obsidian second brain live — vault, graph, HOME, 5 business notes, wikilinks, auto-sync | ✅ | S34 |
| OpenClaw recovery + path docs (S33): Updated 2026.5.7, ARTIE-CORE infra section, SOP 12, PAT stored | ✅ | S33 |
| Soul file architecture (I-21): SHARED-CORE.md + handoff keyword + boot-loader | ✅ | S32 |
| SHARED-CORE.md content rebuild (I-22): coaching philosophy + RPG game + rules v3 | ✅ | S32 |
| THINKING_OS duplicate removed from ARTIE-STANDARDS V4 — pointer to soul/shared/THINKING_OS.md added | ✅ | S31 |
| Drive folder skeleton created: PROJECTS, DATA, JOURNAL, REFERENCE, _ARCHIVE + 5 business subfolders | ✅ | S31 |
| Artie soul files migrated: ARTIE-CORE V4 + 4 soul files → GitHub soul/artie/ | ✅ | S30 |
| EMPIRE_STATUS.md updated — soul files section reflects GitHub | ✅ | S30 |
| GitHub restructure — soul/, indexes/, 00-load-me/ pushed to main | ✅ | S29 |
| THINKING_OS.md created (extracted from ARTIE-STANDARDS) | ✅ | S29 |
| EMPIRE_RULES.md created (shared quality + security rules) | ✅ | S29 |
| CLAUDE-CORE.md V2 (updated paths to GitHub structure) | ✅ | S29 |
| CLAUDE-PROJECTS.md created (Claude's build queue) | ✅ | S29 |
| SPRINT.md created on GitHub 00-load-me/ | ✅ | S29 |
| JOURNAL_INDEX.md created (S01–S29, tags, Drive links) | ✅ | S29 |
| SOUL_CHANGELOG.md created (full history S04–S29) | ✅ | S29 |
| DECISIONS_LOG.md created (all key architectural decisions) | ✅ | S29 |
| Hybrid Drive/GitHub architecture designed and locked | ✅ | S29 |
| Cowork/Claude second Discord bot created + live in #general | ✅ | S28 |
| ops.radrooster.co migrated to Cloudflare Pages (auto-deploys from GitHub) | ✅ | S27 |
| Dashboard open items moved to top of layout | ✅ | S27 |
| MASTER_OPEN_ITEMS.md created on GitHub (this file) | ✅ | S27 |
| SESSION_HISTORY.md created on GitHub | ✅ | S27 |
| Morning briefing → Discord #general (CONFIRMED by Chris) | ✅ | S27 |
| 9 cron jobs disabled (CONFIRMED by Chris) | ✅ | S27 |
| Discord API accessible from Cowork via bot token | ✅ | S27 |
| GitHub repo live (github.com/Artemisclaws/sharedfolder) | ✅ | S26 |
| Discord fully wired — all 8 channels | ✅ | S26 |
| Soul files updated (ARTIE-CORE, ARTIE-STANDARDS, ARTIE-DEPT) | ✅ | S26 |
| EMPIRE_STATUS moved to GitHub (source of truth) | ✅ | S26 |
| Master File Map pushed to GitHub | ✅ | S26 |
| 14 duplicate files resolved | ✅ | S24 |
| MASTER_INDEX.md v1 built | ✅ | S24 |
| ARTIE-PROJECTS.md v2 (all placeholders filled) | ✅ | S24 |
| ARTIE-DEPT.md v2 (all 8 Telegram thread IDs) | ✅ | S24 |
| SOP 11 added to ARTIE-RUNBOOK.md | ✅ | S24 |
| Session End Protocol designed | ✅ | S24/S25 |
| Claude & Artie Shared Folder created on Drive | ✅ | S25 |
| CLAUDE-CORE.md drafted | ✅ | S23 |
| ARTIE-RUNBOOK.md drafted (10 SOPs) | ✅ | S23 |
| System architecture locked | ✅ | S23 |
| artie_report_sync.py v2 — 13-parser 3PD email pipeline | ✅ | S20 |
| GH daily pipeline live (PDF→parse→Drive→Telegram) | ✅ | S20 |
| dashboard.html built + ops.radrooster.co originally live | ✅ | S22 |
| EMPIRE_STATUS.md structure built | ✅ | S22 |

---

## 📋 SESSION 32 PRIORITY ORDER

1. ✅ ~~**I-21** — Soul file architecture + handoff keyword~~ DONE S32
2. ✅ ~~**I-22** — SHARED-CORE.md content rebuild + RPG game~~ DONE S32
3. **I-06** — Daily digest cron for #general (decide time with Chris first)
4. **I-17** — Decommission old Cloudflare Tunnel
5. **B-01** — Pinyo Farms market validation (leverage is flat — time to move)

**Start S33 with:** "Pull MASTER_OPEN_ITEMS.md and EMPIRE_STATUS.md from GitHub. Load SPRINT.md. Priority order: I-23 (Artie cron audit — Aura Thai finance + Vine reviews not triggering), I-06 (daily digest time), B-01 (Pinyo Farms validation)."

---

*GitHub source of truth. Updated end of every session. Never recreated — only appended/edited.*

---

## 🔗 Graph Links
[[HOME]] | [[SPRINT]] | [[EMPIRE_STATUS]] | [[SESSION_HISTORY]]
[[aura-thai]] | [[vine-arbitrage]] | [[pinyo-farms]] | [[ai-ventures]] | [[roam]]

## 📋 SESSION 34 PRIORITY ORDER

1. **I-06** — Daily digest cron for #general (decide time with Chris)
2. **I-23** — Artie cron audit (fix backends)
3. **B-01** — Pinyo Farms market validation

**Start S35 with:** Load soul files. Check Obsidian vault is auto-pulling correctly. Priority: I-06 (daily digest — pick a time), then I-23 (cron backends).

---

## 📋 SESSION 36 COMPLETED + S37 START INSTRUCTIONS

**S36 Summary (2026-05-13):**
- PAT permanently fixed — now stored in Google Drive Soul folder (fileId: 1528C9LxOxjxQvS5iUM8vFjE50clNM1NT). No more session uploads. CLAUDE-CORE.md updated and pushed to GitHub.
- I-23 diagnosed: cron not firing since ~May 8. Evidence = GH daily PDFs arriving but not processed.
- A-02 partially complete: ue_price_impact.html v2 built with Feb/Mar/Apr partial data. Easter confound identified. Key finding: ticket +34.7-39.8% vs March baseline (most defensible). Orders near-flat (-1.5%) vs DD's -16.2% collapse.

**S37 SESSION START SEQUENCE:**
```
# 1. Read PAT from Drive connector
#    Tool: mcp__f942c9da...__read_file_content
#    fileId: 1528C9LxOxjxQvS5iUM8vFjE50clNM1NT
# 2. Load soul files via bash+curl with PAT
PAT="[from Drive]"
BASE="https://raw.githubusercontent.com/Artemisclaws/sharedfolder/main"
curl -s -H "Authorization: token $PAT" "$BASE/soul/claude/CLAUDE-CORE.md" > CLAUDE-CORE.md
curl -s -H "Authorization: token $PAT" "$BASE/soul/shared/SHARED-CORE.md" > SHARED-CORE.md
curl -s -H "Authorization: token $PAT" "$BASE/empire-status/EMPIRE_STATUS.md" > EMPIRE_STATUS.md
curl -s -H "Authorization: token $PAT" "$BASE/00-load-me/SPRINT.md" > SPRINT.md
# 3. Pull this file + SESSION_HISTORY.md + RPG_LEDGER.md from GitHub
```

**S37 PRIORITY ORDER:**
1. **A-02 COMPLETE** — Find Jan UE file: search Drive folder `19_v1W_TvzZ8OilqRDzsN5PPJFytJYphw` for title containing "2026-01". Get full Apr 14-30 data from April file (Drive ID: `1oUBI8HM7rIpAB0DU9V3EBGJbznqpIb5Y6VjyfijcEeU`) — all 5 tools have truncation at row 50; try `download_file_content` + bash parse. Rerun analysis → final `ue_price_impact.html`.
2. **A-04** — Write Artie SOP for cron restart + I-23 fix. Update ARTIE-RUNBOOK.md.
3. **A-05** — Wire artie_report_sync.py output → aura_thai_finance sheet (ID: 1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE). GH data already in sheet ✅. DD/UE NOT loaded yet — don't move those source files.

**KEY DATA NOTES FOR S37:**
- UE price markup went live: **April 9, 2026** (same day as DD)
- PRE window = Apr 1-8 (Easter week — confound: orders suppressed vs March baseline)
- March comparison (no Easter): avg ticket $33.45 (outlier removed) — USE THIS as PRE baseline
- Apr POST (Apr 9-13 only, 5 days): avg ticket $45.05
- DD comparison (complete data): ticket +13.1%, orders -16.2%, revenue -5.1% — "slightly hurting"
- UE (partial): ticket +34.7%, orders -1.5%, revenue +37.7% — MUCH better than DD, but only 5 days
- Easter Sunday = April 5 = 0 UE orders. Apr 6 (Mon) = 1 order. Recovery started Apr 7.
- March file is Transactions format ("Sales excl. tax" = ticket size). Apr/Feb files are order_history format ("Ticket Size").
