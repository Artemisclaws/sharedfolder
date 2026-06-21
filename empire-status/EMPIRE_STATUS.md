# EMPIRE_STATUS.md
**Last Updated:** 2026-06-21 | Session 45
**Updated By:** Claude (Session 45)

---

## STATUS OVERVIEW

| Area | Status | Notes |
|------|--------|-------|
| OpenClaw | 2026.5.7 | Updated S33. Services: openclaw-gateway + openclaw-node (systemd --user). Paths confirmed. |
| GitHub setup | ✅ LIVE | `github.com/Artemisclaws/sharedfolder` |
| Discord setup | ✅ LIVE | All 8 channels wired, Artie responding |
| Morning briefing → Discord | ✅ CONFIRMED | Verified by Chris, Session 27 |
| 9 cron jobs disabled | ✅ CONFIRMED | Verified by Chris, Session 27 |
| ops.radrooster.co | ✅ LIVE — CLOUDFLARE PAGES | Migrated from Artie's PC tunnel → GitHub auto-deploy. No Artie dependency. |
| Dashboard — open items at top | ✅ DONE | Pushed S27. Infrastructure + Operations items appear first. |
| MASTER_OPEN_ITEMS.md | ✅ LIVE | GitHub: `master-open-items/MASTER_OPEN_ITEMS.md` |
| SESSION_HISTORY.md | ✅ LIVE | GitHub: `session-history/SESSION_HISTORY.md` |
| Handoff system | ✅ REFORMED | 5-line handoffs + GitHub as living task tracker |
| Cowork → Discord bot (2nd bot) | ✅ LIVE | S28 — Bot ID 1501667305518530711, posting in #general |
| Daily digest cron (#general) | ❌ NOT BUILT | S28+ |
| Telegram → Discord migration | 🔄 IN PROGRESS | Cron redirect done; backends pending |
| Naming convention | ✅ LOCKED | FB Arbitrage → Vine Arbitrage S31 |
| Old Cloudflare Tunnel (Artie) | 🔄 DECOMMISSION PENDING | ops.radrooster.co now on Pages — tunnel no longer needed |
| Playwright downloader | ❌ DEFERRED | Dedicated session — DD/UE auth wall |
| 9 cron job backends | ❌ NOT BUILT | Dedicated session needed |
| Drive folder reorganization | ❌ DEFERRED | S28 — I-02 |
| Live market data | ❌ NOT SET UP | Future session |
| Obsidian Second Brain | ✅ LIVE | S34 — vault synced, graph live, HOME as hub, auto-pull every 5min |
| Aura Thai Finance Dashboard | 🟡 IN PROGRESS | S34–S40 — HIGH priority data gaps resolved. Ready to build next session. |
| Aura Thai Price Increase Monitoring | ✅ ACTIVE | S35 — DD +20% went live Apr 9. Revenue -5.1%, monitoring weekly (Mon 9am scheduled task). |
| Aura Thai Invoice System | ✅ LIVE | S40/S43/S45 — 5-tab system deployed. 277 rows in Invoice Log. Dish Map synced (53 ingredients). |
| SOP 14 — Invoice Photo Pipeline | ✅ BUILT S45 | invoice_processor.py: Drive → HEIC → Haiku OCR → Invoice Log → Dish Map. Ready for Artie. |
| Dish Map | 🟡 AWAITING CHRIS | 53 ingredients synced from Invoice Log. Column B (Dish Name(s)) blank — Chris fills. |
| artie_report_sync.py cron | ❌ BROKEN | Not firing since May 8 — I-23. |

---

## AURA THAI — KEY FACTS (do not ask Chris again)

### Revenue Model — CORRECTED S39
- **Lavu = primary revenue source.** Captures ALL sales (dine-in + delivery + catering).
- GH/DD/UE are delivery sub-channels — they contribute TO Lavu totals, not separate from them.
- Lavu XLS = UTF-16LE TSV — base64 decode → BOM strip → parse.

### Invoice System — S45 STATUS
- **Invoice Log:** 277 rows (Feb–May 2026), Taiwah + SJ Distributors
- **Dish Map:** 53 unique ingredients, alphabetically sorted. Column B (Dish Name(s)) = BLANK — Chris fills next.
- **SOP 14 script:** `invoice_processor.py` in outputs — send to Artie with SOP_14_invoice_processing.md
- **DRIVE_FOLDER_ID:** Still needs to be filled in by Artie before first run
- **Apps Script:** Updated `aura_thai_invoice_system.gs` deployed. `syncIngredientsToDishMapV2()` is the working sync function.

### Dish Map Notes
- Non-food supplies (chopsticks, cleaning supplies, bags): mark "Supply"
- Universal cost items (oils, sugar, vinegar, soy sauces): mark "All Dishes"
- ~35 dish-specific ingredients for Chris to map

### Labor (S39 confirmed)
- BOH Fixed: ~$13,835/period (~$6,917/biweekly) | Daily: ~$494
- FOH: Lavu Time Cards, $16/hr

### Key Revenue (S40 verified)
- YTD 2026: $381,011 | YTD 2025: $412,036 | YoY: -7.5%
- Apr 2026 vs 2025: -11.3% (worst month)

---

## BLOCKERS — ACTIVE

| Blocker | Blocks | Resolution |
|---------|--------|-----------|
| Chris fill Dish Map col B | COGS analysis | A-09b — ~20 min task |
| Artie set DRIVE_FOLDER_ID in invoice_processor.py | SOP 14 automation | One-time setup per SOP 14 |
| I-23 artie_report_sync.py broken | GH/DD/UE pipeline | Needs dedicated debug session |

