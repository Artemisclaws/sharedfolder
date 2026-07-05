# EMPIRE_STATUS.md
**Last Updated:** 2026-07-05 | Session S60
**Updated By:** Claude (S60)

---

## STATUS OVERVIEW

| Area | Status | Notes |
|------|--------|-------|
| GitHub setup | LIVE | `github.com/Artemisclaws/sharedfolder` |
| Discord setup | LIVE | All 8 channels wired |
| ops.radrooster.co | LIVE - CLOUDFLARE PAGES | Auto-deploy from GitHub. |
| Obsidian Second Brain | LIVE | S34 - vault synced, graph live |
| artie_report_sync.py cron | NOT FIRING | Broken since ~May 8 (I-23) |
| Bedrock System Redesign | DESIGNED S60, migration pending | v1+v2 docs in outputs (Fable-5-authored, verified). Kills the hand-maintained master file map (all copies), adds REGISTRY + freshness gate, adds Fireteam Sprint team loop. See SPRINT S60 block for exact next steps. |
| Lavu daily-sales export pipeline | STALLED | No exports since 2026-05-26 (37+ days as of S60). Cause undiagnosed — script broken vs. paused collection vs. unprocessed backlog. Blocks A-11 PATH-TO-BLACK (needs current revenue). |
| Master file map (GitHub + Drive copies) | DISCONTINUING | Replaced by REGISTRY (below) once S61 migration executes. Do not update the old map further. |
| RPG_LEDGER.md | RETIRED S60 | Confirmed zero effect on Chris. Banner added to file. Replaced by named commitments to teammates in the Fireteam Sprint loop (see TEAM section). |
| Old Cloudflare Tunnel | DECOMMISSION PENDING | |
| Daily digest cron (#general) | NOT BUILT | |
| Build Philosophy | LOCKED S46 | Navy SEAL rules. Manual to automated phases. |
| GitHub Handoff PAT | FIXED S49 | Drive MCP only (fileId: 1528C9LxOxjxQvS5iUM8vFjE50clNM1NT). No local paths. |
| CLAUDE-CORE.md | V6 S51 | CHRONICLE keyword protocol added. |
| Cowork project instructions | FIXED S51 | Now uses GitHub API via bash - no more stale web_fetch cache. |
| CHRONICLE protocol | LIVE S51 | journal/session_SXX_date.md + indexes/CONTENT_LOG.md. S48 entry tested. |
| ARTIE-CORE.md | V6 S50 | Session start/end protocol added |
| ARTIE-RUNBOOK.md | V2 Bedrock S50 | 3 working SOPs. 8 pending scripts queued. |
| artie_handoff.py | On GitHub | Pulls to Artie via sync_soul.sh |
| Soul sync cron (6hr) | PENDING | TeamViewer paste ready - waiting for Chris to execute |
| Vine | SUSPENDED | Kicked for late reviews. vine_review_writer.py cron must be removed. |
| BIXBY_KNOLLS_MARKET.md | LIVE S52 | bixby-knolls/BIXBY_KNOLLS_MARKET.md - shared intel for all Atlantic Ave businesses |
| RoamWithChris Story Protocol | LIVE S53, TESTED S54 | Story Bible required before any script. Signature opener locked. Series format established. S54: protocol test passed — script written in one clean pass, zero rewrites. |
| RoamWithChris Story Bible Protocol | V2 S54 | Added Compass (4.5), false-belief line, Why Auggie Needs This Story (7.5). Locked, provisional bedrock pending a second differently-shaped story. |
| RoamWithChris Content System | DESIGNED S54 | Full pipeline locked: Footage → Story Index → Story Bible → Script → Edit → Post. Story Index not yet built — blocked on trip count + sheet location. |
| Soul files audit | DONE S55 | 5 HIGH / 7 MEDIUM / 6 LOW findings. Fixes pending Chris approval (I-25). Report in outputs: soul-files_audit_S55. |
| Aura Thai Apps Script | V2 DELIVERED S55 | Timeout root cause fixed: blocking ui.alert → non-blocking toast. setupInvoiceSystem disarmed + removed from menu. Chris installing. |
| RoamWithChris footage drive organized | DONE S58 | External HD (Crucial 2TB) cleaned (2,055 junk files removed), 429 orphaned proxies re-matched to masters, 6 renamed/collision files restored to playable pairs. Footage Manifest v1 built (3,505 rows) — Phase 1 of Story Index. Policy locked: never rename raw .insv. |
| Family Investment Playbook v2 | LOCKED S56 | sessions/S55/pinyo-family_investment-playbook_v2.md — all PROPOSED approved. $5K BTC ladder: $2K@$50K/$1.5K@$45K/$1.5K@$40K. Chris executing INV-13/08/15/14. |
| Playbook v2.2 — D8/D9 estate + insurance | RESOLVED S57 | §9 added. Mom's trust holds S-corp shares (QSST trap flagged), will+guardianship DIY, parent policies/IUL rejected. EST-01..05 queued. Aura Thai = S-CORP, shares under mom (shelter), SBA $350K @3% mom-guaranteed. |

---

## TEAM (added S60 — do not ask Chris again)

| Who | Relationship | Role | Notes |
|-----|--------------|------|-------|
| Chris | Chairman | Direction, decisions, approvals | Thinks process-first; flows best working with a teammate. |
| Golfii | Chris's wife | Manager/partner — Aura Sweet | Ready to help with anything asked; currently fully directive-dependent. Goal: teach her to think/plan before executing (see Fireteam Sprint, BEDROCK_SYSTEM_DESIGN_v2.md §9). Highly effective — does first, thinks second (opposite of Chris). |
| Kate | Golfii's sister | Manager/partner — Aura Sweet | Same profile and goal as Golfii. |
| Claude | AI — Strategist/Architect | Planning-partner teammate, all ventures | Right now Chris's main team member day-to-day. No persistent memory between sessions — this file + SPRINT are how continuity works. |
| Artie | AI — Executor (OpenClaw, own machine DESKTOP-R7E8H6E) | Automation/execution teammate | NOT an agent session — cron jobs + scripts, changes require code/TeamViewer, never "just told." Goes dark during `sync_soul.sh` — expected, not a failure. |

**The loop they all run (Fireteam Sprint):** GOAL (one sentence) -> HUDDLE (3 questions, plan before executing) -> RUN -> DEBRIEF (blameless, peer-level, no boardroom). Full detail: outputs/BEDROCK_SYSTEM_DESIGN_v2.md §9.

---

## BIXBY KNOLLS LOCATION — KEY FACTS
**Address:** 4085 Atlantic Ave, Bixby Knolls, Long Beach, CA
**Full market intelligence:** `bixby-knolls/BIXBY_KNOLLS_MARKET.md` (load for any new business launch in this area)

### Quick Reference
- Median household income: $103,777 (19% above Long Beach median)
- Median age: 40 | Predominantly White + Hispanic/Latino families
- Thunderbolt Pizza = 10 ft away, lines out the door (captive foot traffic)
- Ramen Hub = down the street, always full, dessert-seeking families
- First Fridays = monthly community event on Atlantic Ave (no July) - NEXT: August 2026
- BKBA (Bixby Knolls Business Improvement Association) = free community reach
- DoorDash proven: 427 mango sticky rice orders in April-May 2026

---

## ROAMWITHCHRIS — KEY FACTS

### Story Protocol (S53 — LOCKED)
- **Bible before script.** No exceptions. Claude confirms protocol out loud at session start.
- **Series signature opener:** "You won't remember this. So let me tell you."
- **Series tagline (bio/channel):** "This is one of the stories I kept for you."
- **Hook format:** Auggie hero visual → AI baby text "Daddy tell me a story" → signature opener → story
- **Lesson format:** One line in voiceover + pinned comment breakdown + future compilation reel
- **Voice:** Chris speaking TO Auggie — always "you," never third person

### Active Content
| Item | Status | Notes |
|------|--------|-------|
| Auggie backpacking reel | SCRIPT DONE S54 | `outputs/roamwithchris_auggie-backpacking-reel_script_v1.md` — ready for CapCut. One clean pass, protocol test passed. |

### Content Archive System (S54)
Pipeline: **Footage → Story Index → Story Bible → Script → Edit → Post**

| Stage | Owner | Tool | Status |
|-------|-------|------|--------|
| Footage archive | Chris | External HD, single source of truth | Not started — Chris consolidating microSDs/GoPro/Insta360/iPhone/Google Photos |
| Story Index | Claude (build) / Chris (fill) | Google Sheet — 20 fields, 6 groups (Identity/Story/Theme/Production/Triage/Tags). Theme is first-class (1 primary + 2 secondary). | Designed, not built. Blocked on trip count + sheet location. |
| Story Bible | Chris (fill) / Claude (facilitate) | RoamWithChris_StoryBible_Protocol_v2.docx | Template locked v2 |
| Script | Claude | One clean pass off a complete Bible | Proven S54 on Auggie reel |
| Edit | Chris | DaVinci Resolve (free, Keywords + Smart Bins) now; Descript (~$16-24/mo) if it earns its keep; Wideframe/full semantic search deferred until volume justifies ~$99/mo | Manual, staged toward AI-assist |
| Post | Chris | IG first, YouTube Shorts 48hrs later | Manual |

**Note on Artie:** organizing (mechanical) is Artie's eventual lane; tagging (judgment) is not. Artie SOP for footage organizing is design-ready but not deployed — Artie is not a reliable enough dependency yet (see I-23).

### Content Inventory
- 1.85TB footage: Japan, Korea, London, Vietnam, Thailand, Hawaii, US outdoors
- @RoamWithChris Instagram + YouTube
- Series: "The Layover," "Out There," "Rooted"
- Brand truth: "Everything Will Be Okay"

---

## AURA THAI — KEY FACTS (do not ask Chris again)

### Revenue Model
- **Lavu = primary revenue source.** Captures ALL sales.
- GH/DD/UE are sub-channels - contribute TO Lavu totals.
- Sheet ID: `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE`
- Rad Rooster: NOT launched.
- May 2026 avg: ~$2,200/day net (31 days in sheet)
- Average ticket: ~$30 | Primarily takeout

### Proven DoorDash Dessert Sales
| Item | April 2026 | May 2026 | Channel |
|------|-----------|---------|---------| 
| Mango Sticky Rice | 203 orders | 224 orders | Mostly DoorDash |

### BOH Labor
| Name | Role | $/day | Days/period | Total/period |
|------|------|-------|-------------|--------------|
| Miguel | Head Chef | $175 | 12 | $2,100 |
| P Sang | 2nd Head Chef | $155 | 12 | $1,860 |
| Eliseo | Chef | $130 | 10.5 | $1,365 |
| Rambo | Dishwasher | $125 | 10.5 | $1,312.50 |
| Erick | Chef | $140 | 2 | $280 |
| **Total** | | | | **$6,917.50/period (~$494/day)** |

---

## AURA THAI — SYSTEM STATE (S46)

| System | Status | Notes |
|--------|--------|-------|
| Invoice Log tab | EMPTY | Wiped by setupInvoiceSystem. NEVER run setupInvoiceSystem again. |
| Price Tracker tab | PENDING | Run updatePriceTracker from 🍜 menu once Apps Script V2 installed |
| populatePriceTrackerDirect | NEVER INSTALLED | S55 finding: sheet still ran S45 script. Superseded by Apps Script V2. |
| setupInvoiceSystem | BANNED + DISARMED S55 | V2 version refuses to run. Removed from menu. |
| updatePriceTracker | ON HOLD | Needs Invoice Log data first |
| ezCater menu plan | BUILT | `aura_thai_ezcater_menu_plan_v1.md` - 47 to 28 items, 3 packages. Not yet uploaded. |
| DD price impact | DONE | +20% Apr 9: ticket +13.1%, orders -16.2%, revenue -5.1% |
| UE price impact | PARTIAL | Only 5 days POST, Easter confound |
| Artie invoice pipeline | ABANDONED | Not a dependency. Design without Artie. |

---

## AURA SWEET — KEY FACTS (do not ask Chris again)

### Concept
Thai dessert spin-off of Aura Thai. Products modeled after Kanomwann Thai gelato style — ice cream, gelato, and broader Thai dessert formats. Delivery-native brand with nightly events (Fri-Sat). Runs from Aura Thai kitchen. Zero additional kitchen overhead.

### Flavor Names (LOCKED S53)
- **The Brew** (Thai Tea)
- **Chef's Secret** (Fish Sauce Caramel) — viral hook, NEVER reveal ingredient early
- **Island Cream** (Coconut)
- **Sweet Grain** (Mango Sticky Rice)

### Sizing (S52 locked)
| Format | Size | Delivery Price | In-Person Price |
|--------|------|---------------|-----------------|
| Cup (single) | 8 oz | $8-9 | $7-8 |
| Pint (take-home) | 16 oz | $16-18 | $14-16 |

### Campaign — 3 Moves Ready
| Move | Action | Owner |
|------|--------|-------|
| 1 | Proof post — show the scoops, real customers, real reactions | Chris |
| 2 | BKBA collab — community reach, newsletter + IG | Chris |
| 3 | Chef's Secret video — tease the mystery ingredient | Chris |

### Key Opportunities
| Opportunity | Details |
|------------|---------|
| First Fridays pop-up | August 2026 (July skipped) |
| Thunderbolt Pizza spillover | Lines 10 ft away |
| Ramen Hub dessert traffic | Families = pre-qualified dessert customers |
| Mango sticky rice bridge | 427 DD customers = existing audience |

---

## BUILD PHILOSOPHY — LOCKED S46
1. Simple first. Automate second. Scale third. Never out of order.
2. One function, one job. No dependencies on things that can break.
3. Manual before automated. Automation is always the end goal.
4. Phase 1 to 2 to 3 to 4. Never skip. Never build on unproven foundation.

---

## ARTIE STATUS
- Machine: DESKTOP-R7E8H6E
- Not completing tasks reliably. NOT a dependency in any Phase 1 build.
- PAT location: `~/.pinyo_github_pat`
- Handoff script: `~/.openclaw/workspace/artie_handoff.py`

---

## DISCORD CHANNELS
| Channel | ID |
|---------|-----|
| #general | 1493421633359315089 |
| #finance | 1501467891474759770 |
| #operations | 1501468053672689834 |
| #escalations | 1501468242739204097 |

---

## KEY FILE IDs
| File | Location/ID |
|------|-------------|
| GitHub PAT | Drive: `1528C9LxOxjxQvS5iUM8vFjE50clNM1NT` |
| aura_thai_finance sheet | `1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE` |
| Apps Script | `1lNMZ_Hvwj-4ncLGy0nWN9rEr6xJYADZxM9OpOTTloNfGsAIA0DV-uDzr` |
| Bixby Knolls Market Intel | `bixby-knolls/BIXBY_KNOLLS_MARKET.md` (GitHub) |

---

## SESSION LOG
| Session | Date | Key Work |
|---------|------|----------|
| S39 | 2026-05-27 | Decision Dashboard checklist, BOH labor, Lavu as primary source |
| S40 | 2026-06-19 | Apps Script invoice system built |
| S45 | 2026-06-21 | Dish Map redesigned, ezCater menu plan |
| S46 | 2026-06-23 | Build philosophy locked. setupInvoiceSystem BANNED. populatePriceTrackerDirect ready. |
| S47 | 2026-06-23 | Price Tracker script delivered. |
| S48 | 2026-06-23 | Handoff PAT root cause found. SESSION_HISTORY caught up S41-S48. |
| S49 | 2026-06-23 | Full bug audit. CLAUDE-CORE V4 rewritten. CHANGE CONTROL added. |
| S50 | 2026-06-23 | Artie runbook V2 Bedrock. 3 working SOPs. artie_handoff.py built. |
| S51 | 2026-06-23 | CHRONICLE added to CLAUDE-CORE V6. Project instructions fixed. |
| S52 | 2026-06-24 | Aura Sweet customer avatar + demographic research. BIXBY_KNOLLS_MARKET.md created. Sizing standardized. |
| S53 | 2026-07-01 | RoamWithChris Story Protocol established. Auggie backpacking reel Story Bible locked. Series signature opener locked. "You won't remember this. So let me tell you." Series tagline locked. Lesson format established. |
| S54 | 2026-07-01 | Auggie backpacking reel script written in one clean pass — protocol test passed. Story Bible Protocol v2 built (Compass, false-belief line, Why Auggie Needs This Story). Full content archive system designed end to end (Footage → Story Index → Story Bible → Script → Edit → Post). Budget-conscious storage/AI editing plan staged in 3 phases. Story Index schema locked (20 fields) — build blocked on trip count + sheet location. |
| S55 | 2026-07-01 | Soul-file audit: 5H/7M/6L, report in outputs, fixes pending approval (I-25). Apps Script timeout root-caused (blocking ui.alert + popup block); V2 delivered — toasts, setupInvoiceSystem disarmed, V1 sync removed. Found populatePriceTrackerDirect never installed. Ground truth: Dish Map dish names = column B. |

| S55 | 2026-07-01 | Investment strategy unblocked: all S47/S48 deferred questions answered. Options income playbook v1 (covered calls + CSPs, KO/SCHD, Fidelity Roth) built + math verified. Six decisions: crypto hold to $120K then exit/restructure; 1.7 BTC to cold wallet; property window 2027-2032 LA/OC STR house-hack profile (DEFERRED); +20% trim rule; Roth=active/taxable=long-term verified; PRIORITY #1 = AURA THAI TO BLACK. Roth cash conflict named: CSP vs BTC window. MCD at 52-wk low = buy-on-sale branch live. |
| S57 | 2026-07-01 | D8/D9 resolved → Playbook v2.2. Ground truth: Aura Thai S-corp 100% under mom (post-lawsuit shelter); SBA EIDL $350K @3%/30yr, corp borrower + mom guarantor; no will/trust/guardianship existed; no real property; term policy exists (details TBD). Estate stack approved: mom's revocable trust w/ QSST/ESBT language, WillMaker will+guardianship, beneficiary alignment, crypto access plan, own trust deferred to property. Insurance: term stays, parent policies + IUL rejected. Legal spend 3-tier (~$110 DIY + $1.5–2.5K attorney). Cash-flow warning logged — path-to-black outranks all triggers; INV-13 surplus re-confirm flagged. Next: A-11 PATH-TO-BLACK. |
| S56 | 2026-07-01 | Family Playbook v2 LOCKED: BTC ladder 40/30/30, 529 dip-adds, Golfii 70/30 all approved; $5K ladder cash committed. Playbook updated on GitHub, math verified. INV to-dos added to SPRINT → live on ops dashboard. |
| S58 | 2026-07-03 | RoamWithChris: Crucial 2TB HD connected, cleaned (2,055 junk files), inventoried without lumping repeat trips. "Havasupai/Japan/Thailand 2025" dump folder found to be orphaned proxies only — 429 re-matched to real masters. Insta360 pairing audit: 32 pairs confirmed truly broken, 6 collision-renamed files restored, ~26 Vegas/Mammoth files unpairable (manually renamed, lost ID). Policy locked: never rename raw .insv. Footage Manifest v1 (3,505 rows) built as Phase 1 of Story Index — RWC-05 unblocked. |
| S59 | 2026-07-04 | (Backfilled S60 — not documented at the time.) Google Drive Desktop sync repaired (was crashing, nothing syncing). `~/Documents/G Drive with Claude` folder created and connected to Cowork — Claude can now edit Drive files directly. CLAUDE-CORE updated to V8 (WORKING DOCUMENTS rule) but SPRINT counter was never advanced to match — root cause of the S41/S58 counter fork resolved in S60. |
| S60 | 2026-07-05 | BEDROCK SYSTEM REDESIGN. Discovered: session counter forked (a Drive-based file-map copy called itself "S41," which had already happened weeks earlier in the real S58 lineage); master file map 37+ days stale and missed the Lavu export stall entirely; FILE_ORG_PLAN_S49 executed but status never flipped; RPG_LEDGER already decaying (S58 skipped it). Two Fable-5-authored design docs produced and independently verified (v1, then v2 after Chris's feedback that the system also needed to fit how he works — team, ideas, motivation). v2: Lean/Toyota as the spine, GTD for idea capture, kills the file map for a small REGISTRY + live lookups, fixes two logic gaps (frozen files falsely flagged stale; touched-but-empty files falsely flagged fresh), adds the Fireteam Sprint team loop (GOAL->HUDDLE->RUN->DEBRIEF) covering Chris, Golfii, Kate, Claude, Artie, retires RPG_LEDGER for named teammate commitments, revives the dormant S34 Obsidian second-brain + `_inbox/` for idea capture instead of building anything new. Boot-loader v2 delivered for Chris to paste into custom instructions. Migration steps 2-5 approved but not yet executed — queued for S61. |

## Graph Links
HOME | SPRINT | MASTER_OPEN_ITEMS | SESSION_HISTORY
