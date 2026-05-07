# CLAUDE-PROJECTS.md — Active Build Queue
**Updated by:** Claude at end of every session
**Last Updated:** 2026-05-07 | Session 29
**GitHub:** `soul/claude/CLAUDE-PROJECTS.md`

This is Claude's task bible. Every active build, its status, and what's blocking it. Cross-reference with MASTER_OPEN_ITEMS.md for the full empire task list.

---

## 🔴 ACTIVE — IN PROGRESS THIS SPRINT

| # | Build | Business | Status | Blocking What |
|---|-------|----------|--------|---------------|
| I-02 | Drive + GitHub restructure (hybrid Bezos/Musk/Munger) | All | 🟡 In Progress — S29 | File organization for entire empire |
| I-06 | Daily digest cron for Discord #general | All | ❌ Not started | Decide time with Chris first |
| I-17 | Decommission old Cloudflare Tunnel on Artie | Infrastructure | ❌ Not started | Cleanup |
| I-10 | Artie bot token → env variable in .bashrc | Infrastructure | ❌ Not started | Security hygiene |

---

## 🟡 QUEUED — NEXT SESSIONS

| # | Build | Business | Status | Notes |
|---|-------|----------|--------|-------|
| I-07 | 9 cron job backends | All | ❌ Not started | Dedicated session — each needs script + data source |
| I-04 | Artie HTML dashboard generator script | Infrastructure | ❌ Not started | generate_dashboard.py reads EMPIRE_STATUS → writes index.html |
| I-05 | Drive flag watcher cron (15-min) | Infrastructure | ❌ Not started | Checks REGEN_DASHBOARD.flag |
| I-09 | Live market data for morning briefing | Infrastructure | ❌ Not started | Section 1 of briefing currently skipped |
| O-01 | Playwright downloader (DD/UE) | Aura Thai | 🟡 Built, needs deploy | artie_playwright_downloader_UPDATED.py — bypasses auth wall |
| O-03 | Aura Thai: Lavu integration | Aura Thai | 🔴 Blocked | Blocked on Chris completing Lavu setup |
| O-04 | Aura Thai: Shift Close integration | Aura Thai | 🔴 Blocked | Blocked on Chris |

---

## 🟢 STRATEGY & RESEARCH (Claude + Chris sessions)

| # | Project | Business | Status | Notes |
|---|---------|----------|--------|-------|
| B-01 | Pinyo Farms market validation | Pinyo Farms | ❌ Not started | Phase 1 greenlit — research not started |
| B-02 | Roam master content plan | Roam | ❌ Not started | No Artie tasks until plan complete |
| B-03 | AI Ventures: restaurant subscription stream | AI Ventures | ❌ Not started | Stream 2 defined, not planned |

---

## ✅ COMPLETED (permanent record)

| Build | Completed | Session | Notes |
|-------|-----------|---------|-------|
| GitHub restructure — soul/, indexes/, 00-load-me/ | 2026-05-07 | S29 | New files pushed: THINKING_OS, EMPIRE_RULES, CLAUDE-CORE V2, CLAUDE-PROJECTS, indexes |
| Cowork/Claude second Discord bot | 2026-05-06 | S28 | Bot ID: 1501667305518530711, live in #general |
| ops.radrooster.co → Cloudflare Pages | 2026-05-05 | S27 | Auto-deploys from GitHub dashboard/ |
| MASTER_OPEN_ITEMS.md live on GitHub | 2026-05-05 | S27 | Source of truth for all tasks |
| Morning briefing → Discord #general | 2026-05-05 | S27 | Confirmed by Chris |
| GitHub repo live | 2026-05-05 | S26 | github.com/Artemisclaws/sharedfolder |
| Discord all 8 channels wired | 2026-05-05 | S26 | All channels confirmed |
| EMPIRE_STATUS.md → GitHub | 2026-05-05 | S26 | Drive version deprecated |
| MASTER_INDEX.md V1 | 2026-05-05 | S24 | Built and on Drive/Soul (to migrate GitHub) |
| 14 duplicate files resolved | 2026-05-05 | S24 | Per duplicate hit list |
| ARTIE-RUNBOOK.md drafted (10 SOPs) | 2026-05-05 | S23 | Uploaded to Drive/Soul |
| CLAUDE-CORE.md V1 | 2026-05-05 | S23 | Created, now superseded by V2 |
| 3PD email pipeline V2 | 2026-04-30 | S20 | 13 parsers, GH/DD/UE |
| Empire ops dashboard live | 2026-04-30 | S21 | ops.radrooster.co (now on Pages) |

---

## HANDOFF TO ARTIE QUEUE

Builds ready for Artie to deploy — Claude built, waiting on Chris to give Artie the green light:

| Build | File | Deploy SOP | Chris Action Needed |
|-------|------|------------|---------------------|
| Playwright downloader | artie_playwright_downloader_UPDATED.py | ARTIE-RUNBOOK SOP 12 (TBD) | Review script, confirm Artie can run it |

---

*This file is the source of truth for Claude's work queue.*
*Update at end of every session. Cross-reference: MASTER_OPEN_ITEMS.md on GitHub.*
