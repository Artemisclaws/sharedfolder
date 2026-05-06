# MASTER_OPEN_ITEMS.md
**Source of truth for all open tasks across the Pinyo Empire.**
**Last Updated:** 2026-05-06 | Session 27 (end of session)
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
| I-01 | Cowork/Claude second Discord bot | ❌ Open | Session 28 | Create new bot in Discord Dev Portal — so Claude messages are distinct from Artie's |
| I-02 | Drive folder reorganization | ❌ Open | Session 28 | Soul/Artie/, Soul/SHARED/, Soul/Claude/ — never executed despite being planned S23-S26 |
| I-04 | Artie HTML dashboard generator script | ❌ Open | Future | generate_dashboard.py on Artie — reads EMPIRE_STATUS, writes index.html |
| I-05 | Drive flag watcher cron (15-min) | ❌ Open | Future | Checks REGEN_DASHBOARD.flag, regenerates if found |
| I-06 | Daily digest cron for #general | ❌ Open | Session 28 | Decide time with Chris, then build |
| I-07 | 9 cron job backends | ❌ Open | Dedicated session | All 9 non-functioning crons need backends built |
| I-08 | Telegram → Discord full migration | 🔄 In Progress | Future | Cron redirect done; backends and full switchover pending |
| I-09 | Live market data for morning briefing | ❌ Open | Future | Section 1 of briefing currently skipped |
| I-10 | Artie bot token → env variable | ❌ Open | Session 28 | Move from file to `export DISCORD_BOT_TOKEN=` in .bashrc on Artie machine |
| I-12 | Telegram thread routing test | ⚠️ Unconfirmed | Artie | SOP 11 written, test message never confirmed landed in Finance thread |
| I-13 | ARTIE_DASHBOARD_PROTOCOL.md → ARTIE-STANDARDS | ⚠️ Unconfirmed | Chris/Artie | Written S22, never confirmed loaded |
| I-14 | Delete old EMPIRE_STATUS Google Doc | ❌ Open | Chris | Drive ID: 1AMnMkAzD8xoYsGHwDRRl7-VRL2OADb6irVsnZdFVpoQ |
| I-15 | Delete 4 old files on Mac/Aura Thai | ❌ Open | Chris (manual) | Shell is read-only — must delete in Finder |
| I-16 | MASTER_INDEX.md — keep current | 🔄 Ongoing | Each session | Verify it reflects current file locations |
| I-17 | Decommission old Cloudflare Tunnel on Artie | ❌ Open | Session 28 | ops.radrooster.co now on Pages — tunnel (e1588a4f.cfargotunnel.com) no longer needed |

---

## 🟡 OPERATIONS & AUTOMATION

| # | Item | Status | Owner | Notes |
|---|------|--------|-------|-------|
| O-01 | Playwright downloader (DD/UE) | ❌ Open | Dedicated session | artie_playwright_downloader.py — reads pending_downloads.json, bypasses auth wall |
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

## 📋 SESSION 28 PRIORITY ORDER

1. **I-01** — Build Cowork/Claude second Discord bot
2. **I-02** — Drive folder reorganization
3. **I-06** — Daily digest cron for #general (decide time with Chris first)
4. **I-17** — Decommission old Cloudflare Tunnel on Artie
5. **O-01** — Playwright downloader (dedicated session — plan it)

**Start S28 with:** "Pull MASTER_OPEN_ITEMS.md and EMPIRE_STATUS.md from GitHub. Start with I-01: build the Cowork Discord bot."

---

*GitHub source of truth. Updated end of every session. Never recreated — only appended/edited.*
