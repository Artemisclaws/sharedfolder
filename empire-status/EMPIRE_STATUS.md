# EMPIRE_STATUS.md
**Last Updated:** 2026-06-24 | Session S52
**Updated By:** Claude (S52)

---

## STATUS OVERVIEW

| Area | Status | Notes |
|------|--------|-------|
| GitHub setup | LIVE | `github.com/Artemisclaws/sharedfolder` |
| Discord setup | LIVE | All 8 channels wired |
| ops.radrooster.co | LIVE - CLOUDFLARE PAGES | Auto-deploy from GitHub. |
| Obsidian Second Brain | LIVE | S34 - vault synced, graph live |
| artie_report_sync.py cron | NOT FIRING | Broken since ~May 8 (I-23) |
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
| Price Tracker tab | PENDING | Run `populatePriceTrackerDirect` - script ready |
| populatePriceTrackerDirect | READY | `aura_thai_price_tracker_script_v1.gs` in Investment Strategies folder |
| setupInvoiceSystem | BANNED | Wipes all data. Never run again. |
| updatePriceTracker | ON HOLD | Needs Invoice Log data first |
| ezCater menu plan | BUILT | `aura_thai_ezcater_menu_plan_v1.md` - 47 to 28 items, 3 packages. Not yet uploaded. |
| DD price impact | DONE | +20% Apr 9: ticket +13.1%, orders -16.2%, revenue -5.1% |
| UE price impact | PARTIAL | Only 5 days POST, Easter confound |
| Artie invoice pipeline | ABANDONED | Not a dependency. Design without Artie. |

### Real Ingredient Prices (Taiwah + SJ, Feb-Apr 2026)
| Ingredient | Actual | Model | Flag |
|---|---|---|---|
| Chicken Breast | $2.08/lb | $2.49/lb | OK |
| Long Grain Rice | $0.64/lb | $1.06/lb | OK |
| Basil | $5.95/lb | $3.95/lb | Model LOW |
| Green Bean | $2.95/lb | $1.29/lb | Model 2.3x LOW |
| Shrimp 21/25 | $5.25/lb | $5.85/lb | OK |
| Eggs Jumbo | $0.13/ea | $0.19/ea | OK |

Suppliers: Taiwah Trading Corp (dry goods/produce) | SJ Distributors LLC (protein)

---

## AURA SWEET — KEY FACTS (do not ask Chris again)

### Concept
Thai dessert spin-off of Aura Thai. Products modeled after Kanomwann Thai gelato style — ice cream, gelato, and broader Thai dessert formats. Delivery-native brand with nightly events (Fri-Sat). Runs from Aura Thai kitchen. Zero additional kitchen overhead.

### Location
4085 Atlantic Ave, Bixby Knolls, Long Beach (same kitchen as Aura Thai)

### Positioning
"Thai sweets. Real flavors. No compromise." | Premium craft Thai dessert meets street food authenticity.

### Current Products and Proven Sales (pre-launch)
| Product | Size | Price | Units Sold | Channel |
|---------|------|-------|-----------|---------|
| Thai Tea Ice Cream | 3.5 oz | $5 | ~100 | Walk-in (poster) |
| Fish Sauce Caramel Ice Cream | 3.5 oz | $5 | ~35 | Walk-in (poster) |
| Coconut Ice Cream | 3.5 oz | TBD | Ongoing | Walk-in |
| Mango Sticky Rice Ice Cream | 5 oz | $8 | Not yet marketed | - |

**All sales to date were impulse purchases driven by a poster. No active marketing yet.**

### Standardized Sizing (S52 Decision)
| Format | Size | Delivery Price | In-Person Price |
|--------|------|---------------|-----------------|
| Cup (single) | 8 oz | $8-9 | $7-8 |
| Pint (take-home) | 16 oz | $16-18 | $14-16 |

### Market Intelligence
Full demographic research: `bixby-knolls/BIXBY_KNOLLS_MARKET.md`
Business plan: `AuraSweet_BusinessPlan_v1.md` (Drive uploads)

### Key Opportunities
| Opportunity | Details |
|------------|---------|
| First Fridays pop-up | August 2026 (July skipped) - highest foot traffic night on Atlantic Ave |
| Thunderbolt Pizza spillover | Lines 10 ft away - A-frame sign captures impulse buyers |
| Ramen Hub dessert traffic | Families leaving Ramen Hub are pre-qualified dessert customers |
| Mango sticky rice bridge | 427 Aura Thai DD dessert customers = existing Aura Sweet audience |
| BKBA leverage | Business association IG + newsletter for community reach |

### Platform Strategy
| Platform | Priority | Timeline |
|----------|----------|---------|
| DoorDash | First | Launch week |
| Uber Eats | Second | +30-60 days |
| GrubHub | Third | +90 days |

### Content Creator
Chris (Instagram Reels primary - not TikTok yet)

### Open Questions (not yet decided)
1. Brand name final? ("Aura Sweet" vs. Wan Aura / Khanom Aura)
2. Packaging budget confirmed?
3. Ice cream / gelato made in-house or sourced?
4. Licensing/permits for second brand under same kitchen?

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
|---------|----|
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
| S52 | 2026-06-24 | Aura Sweet customer avatar + demographic research. BIXBY_KNOLLS_MARKET.md created. Aura Sweet section added to EMPIRE_STATUS. Sizing standardized (8oz cup / 16oz pint). |

## Graph Links
HOME | SPRINT | MASTER_OPEN_ITEMS | SESSION_HISTORY
