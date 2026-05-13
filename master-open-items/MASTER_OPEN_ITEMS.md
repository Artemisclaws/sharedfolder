# MASTER_OPEN_ITEMS.md
**Source of truth for all open tasks across the Pinyo Empire.**
**Last Updated:** 2026-05-08 | Session 33
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
| I-23 | Artie automated task audit — crons not triggering | ❌ Open | S33 | Aura Thai finance pull/analyze/daily update + Vine reviews/product descriptions. Diagnose why crons aren't firing and fix backends. |
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
