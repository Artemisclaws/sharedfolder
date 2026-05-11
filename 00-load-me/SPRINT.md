# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude at handoff — automatic
**Last Updated:** 2026-05-10 | Session 35
**GitHub:** `00-load-me/SPRINT.md`

Both agents load this file. It answers: what matters most right now?

---

## ACTIVE ITEMS — S35 DIGEST

| ID | Item | Status |
|----|------|--------|
| I-23 | Artie cron audit — crons not triggering | ❌ Open — diagnose + fix backends |
| I-06 | Daily digest cron for #general | ❌ Open — decide time with Chris |
| I-07 | 9 cron job backends | ❌ Open — dedicated session |
| I-17 | Decommission old Cloudflare Tunnel | ❌ Open |
| I-10 | Artie bot token → .bashrc env variable | ❌ Open |
| I-02 | Drive + GitHub restructure (final cleanup) | 🔄 In Progress |
| A-01 | Aura Thai: run real data through processor (Lavu as primary) | ❌ Blocked — Lavu XLS needs Google Sheets conversion |
| A-02 | Aura Thai: UberEats price impact analysis | ⏳ Pending — UE Apr/May files uploaded to Drive dump, run next session |
| A-03 | Aura Thai: push finance dashboard to ops.radrooster.co/aura-thai | ❌ Pending real data |
| A-04 | Aura Thai: ARTIE SOP 13 (Monthly Finance Update) | ❌ Draft exists, needs formal write |
| B-01 | Pinyo Farms market validation | ❌ Open — queued |
| B-02 | Roam master content plan | ❌ Open — queued |
| O-01 | Playwright downloader (DD/UE) | ❌ Open — dedicated session |

---

## SPRINT GOAL — MAY 2026

**Theme:** Operations activation. Infrastructure locked. Now make Artie run things and get real data flowing.

S35 delivered real DoorDash price impact analysis — data is live, monitoring is scheduled. Next: UberEats price analysis, Lavu data access, daily digest, cron backends.

---

## BUSINESSES — CURRENT FOCUS

| Business | Status | Priority Action |
|----------|--------|-----------------|
| Aura Thai | 🟡 Active | UberEats price analysis (A-02) + Lavu data access (A-01) |
| Vine Arbitrage | 🟢 Running | Artie handles review backlog — no Claude action needed |
| Pinyo Farms | ⏳ Planning | Market validation research — not started, B-01 |
| AI Ventures | ⏳ Planning | Restaurant subscription stream — defined, not planned |
| Roam | ⏳ Planning | Master content plan — not started, B-02 |

---

## CHRIS — DECISIONS NEEDED

| Decision | Context | Urgency |
|----------|---------|---------|
| Daily digest time for #general | I-06 blocked until Chris picks a time (6am? 8am?) | High |
| Convert Lavu XLS → Google Sheets | Jan–Apr Transactions + Sale by Item — needed to make Lavu primary data source | High |
| Aura Thai price increase: hold or adjust? | DD revenue -5.1%, monitoring weekly. Review after June 9 if still below baseline | Medium |
| Lavu setup completion | O-03 and O-04 blocked until Chris finishes Lavu setup | Medium |

---

## PROTOCOL — ANALYZE BEFORE EXECUTE (added S35)
> For any strategy touching pricing, menu, marketing spend, or operations — model scenarios first, define decision criteria, get approval, then move. Added after April 9 price increase went live without pre-analysis.

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
| DoorDash price impact analysis — fixed script, ran real data, generated dd_price_impact.html | ✅ S35 |
| Aura Thai profile (businesses/aura-thai/aura-thai.md) — full update with finance status, price data, monitoring plan | ✅ S35 |
| Weekly price monitoring scheduled task (every Monday 9am) | ✅ S35 |
| "Analyze before execute" protocol established | ✅ S35 |

---

## 🔗 Graph Links
[[HOME]] | [[EMPIRE_STATUS]] | [[MASTER_OPEN_ITEMS]]
[[aura-thai]] | [[vine-arbitrage]] | [[pinyo-farms]] | [[ai-ventures]] | [[roam]]
