# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S66 (closed) | 2026-07-22
**GitHub:** `00-load-me/SPRINT.md`

**Counter note (S60):** Session numbering forked — this SPRINT lineage was at S58 (closed 2026-07-03). A same-day session on 2026-07-04 (Google Drive Desktop sync repair; added CLAUDE-CORE's WORKING DOCUMENTS rule, V8) ran as "S59" but never updated this counter. This session (S60) declares the SPRINT lineage canonical going forward. **SPRINT.md line item below is now the sole home of the session counter — no other file may originate a session number.**
**COUNTER: S66 | closed 2026-07-22**

**GOAL (S66 close):** Chris redirected this session away from A-11 to a different named priority: the Lavu POS/payment-processing contract renegotiation (separate thread from the A-11 Lavu daily-sales export stall — do not conflate the two). Kassey (Lavu rep) sent the full order form: Lavu POS $150/mo + 2 Additional Terminals $100 + Digital Gift Cards $59 + MenuDrive $0 = $309/mo software, all hardware/professional-services fees zeroed (100% off), 36-month term with a real early termination penalty, dual pricing at 4% "if applicable." Corrected two facts from the prior checkpoint: actual terminal count is 2 (order form overquotes by 1, corroborated live by Chris), current Lavu software bill is $861/mo (up from $836.64), true all-in baseline (with the ~$269/mo processing leak) now ~$1,130/mo. Iterated round 3 through 16 drafts using negotiation tactics (Voss calibrated/assumptive framing, Fisher-Ury objective criteria, a merged ChatGPT second opinion) plus two research passes: confirmed iOS/iPadOS has no external-touch support (killed the "big screen + iPad" kiosk idea, outdoor-enclosure kiosk is the only real path) and confirmed Lavu does NOT bundle DoorDash/UberEats/Grubhub for free — it routes through paid third-party integrators, so the final email asks about Lavu-side API access/fees only, not a false "it's included" claim. **Final round 3 email saved and ready to send:** Drive doc `lavu_negotiation_email-draft_v16_round3_FINAL.md`. Full checkpoint: `checkpoint_lavu-negotiation_2026-07-22.md` (Drive, same folder — fileId in that doc's own history chain, searchable by title). A-11 still did not move this session — 7th redirect, but this one was Chris's explicit, named choice, not drift (resolves the S65-close commitment asking Claude to name the choice out loud rather than silently continue).

**COMMITMENTS (huddle, S66 close):**
- Chris: send `lavu_negotiation_email-draft_v16_round3_FINAL.md` to Kassey.
- Chris: A-11 PATH-TO-BLACK — Lavu export stall diagnostic still owed (needs Mac), now the 7th session redirected past it. Streak continues; flag again at next A-11-adjacent session.
- Claude, next session touching this thread: load `checkpoint_lavu-negotiation_2026-07-22.md` + Kassey's round-3 reply, then run round 4. Reserve playbook (deliberately NOT sent in round 3 — anchor discipline): if Kassey rejects the 12-month/no-ETF ask, deploy the declining-ETF language (tied to documented, unamortized hardware subsidy, straight-line to zero — not a flat remaining-months formula), the no-penalty business-sale/closure exit, and the no-penalty exit if Lavu stops materially supporting/updating the hardware. The moment she offers any ETF movement, immediately ask for the exact formula and amortization schedule in writing. Statement details, processor identity (CardConnect), and the $269/mo leak figure stay private — never send.
- Claude/Chris: still-forked question from S65 (does A-11 need explicit protected time, e.g. a session where Chris pre-commits to no redirects) — unresolved two sessions running now, worth naming directly rather than re-asking the same huddle question indefinitely.

Both agents load this file. It answers: what matters most right now?

---

## SESSION START — S67
Boot per CLAUDE-CORE V9. **FIRST QUESTION TO CHRIS: does this session open on A-11 PATH-TO-BLACK, the Lavu contract renegotiation (round 4 — check for Kassey's reply, load `checkpoint_lavu-negotiation_2026-07-22.md`), the options wheel thread, or an explicit different priority for today?** Do not silently continue any one thread without naming the choice out loud — this is the 2nd straight session this exact gap got flagged. If Lavu contract renegotiation: Kassey should have replied to round 3 (`lavu_negotiation_email-draft_v16_round3_FINAL.md`) — run round 4 against the reserve playbook in this file's S66 commitments. If investing: options wheel state lives in `investing/OPTIONS_POSITIONS_LOG.md` + playbook §5/v1.1–v1.6 (GitHub, source of truth) — Cycle 1's 3 filled legs now all have resting GTC Buy-to-Close orders in Fidelity (KO $0.23 / SCHD $0.09 / VZ $0.25 limits), no active monitoring needed until they fill or expire 8/21. Trading log (separate, supplementary): Google Sheet fileId `1SkOTFF5ExGplHl08nEjREnps3yhS5PKLTdUpUkxzj90` in `G Drive with Claude` folder — check for GTC fills before assuming still open.

---

## LOAD NOTE — TOKEN EFFICIENCY
Do NOT load SESSION_HISTORY or MASTER_OPEN_ITEMS every session.
- If SPRINT.md session number is behind → pull those files from GitHub.
- Otherwise: SPRINT.md is the only context file needed at session start.

---

## CORRECTED DATA MODEL (S39 — do not revert)
- **Lavu = primary revenue source.** Captures ALL sales: dine-in + delivery + catering.
- GH, DD, UE are sub-channels. They contribute TO Lavu totals.
- Lavu XLS = UTF-16LE TSV — base64 decode → BOM strip → parse.

---

## PERMANENT RULES
> All dashboards live at ops.radrooster.co. No standalone URLs ever.
> Finance tab hardcodes data — MUST rebuild to read from Google Sheet (DASHBOARD ARCHITECTURE RULE violation).
> $5K/day focus filter: new ideas → parking lot unless they advance COGS → pipeline → unit economics → growth.

---

## ACTIVE ITEMS — S57 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-11 | Aura Thai PATH-TO-BLACK plan | 🟡 COST SIDE DONE — S63 | Ground truth in `aura-thai/COST_BASELINE.md` (canonical). Known costs ~$44.9K/mo pre-COGS; break-even ~$2,110/day @30% COGS scenario. Remaining: COGS %, missing fixed items, current revenue (Lavu stall). Then 3-lever plan. |
| OPT-01 | Artie morning/close wheel-cycle reporting | 🟢 READY TO DEPLOY — S64 | **Correction from earlier S64 note:** the "blocked on I-23" call was wrong — Chris showed proof both the 3PD cron (4am Telegram) and the daily briefing cron (6am Discord) are firing reliably today. Cron infra is proven, not broken. Built: `investing/OPTIONS_POSITIONS_LOG.md` (source of truth), `artie/artie_wheel_report.py` (fetches log + live price via Yahoo/Stooq, posts to Discord #finance, logs the check back to GitHub), SOP 15 in `artie-config/ARTIE-RUNBOOK.md` with cron setup commands. **Chris's action:** get this script onto Artie's machine (TeamViewer session or have Artie pull it from GitHub) and run the two crontab commands in SOP 15. Verify server timezone before trusting the 8am/4:05pm ET cron times. |
| A-13 | Build + fill "Cost Baseline" tab in aura_thai_finance | OPEN — CHRIS | Run buildCostBaseline (aura-thai/cost_baseline_tab_builder.gs, safe: creates new tab only). Fill yellow cells: COGS %, water, trash, insurance, internet, POS fees, card rate. Live break-even updates automatically. |
| A-14 | COST_BASELINE open confirmations | OPEN — CHRIS | $616/each monthly?, Miguel $20.40 gap, Eliseo $19.78 gap, Mee Ann cash?, chef actual hrs/day (→ true hourly; some scenarios below CA min wage — add to INV-15 preparer questions). |
| A-12 | Install Apps Script V2 (timeout fix) | ✅ COMPLETE — S58 | Alerts→toasts, setupInvoiceSystem disarmed. |
| I-25 | Soul-file audit fixes | OPEN | 5H/7M/6L. H4 (header fork) CLOSED S62 via V9. Report: soul-files_audit_S55 (outputs). Chris approves order. |
| AS-01 | Aura Sweet spinoff strategy | OPEN — S56 | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Somisomi competitive analysis | OPEN — S56 | Carried from S52 — Chris to walk the block first |
| AS-03 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-04 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. |
| RWC-05 | Story Index master sheet — build | 🟡 PHASE 1 DONE — S58 | Manifest built (3,505 rows, mechanical fields) on Crucial 2TB: `RoamWithChris_Footage-Manifest_v1.xlsx`. Story/Theme/Tags columns still need Chris. |
| RWC-06 | Footage consolidation onto external HD | 🟡 PARTIAL — S58 | Crucial 2TB connected + cleaned (2,055 junk files removed). Has Thailand/USA/Vietnam/Manila Layover/Japan. Still missing: Korea, London, Hawaii. |
| RWC-07 | DaVinci Resolve tagging pass | OPEN — CHRIS | After RWC-06 fully complete (Korea/London/Hawaii still need consolidating). |
| RWC-08 | Resolve ambiguous file — Aug 10 2024 Miami vs Key West | OPEN — CHRIS | 2 files in `_NEEDS REVIEW - Ambiguous Match` on drive. |
| RWC-09 | Confirm Thailand trip Nov 2024 == Bangkok Nov 2024? | OPEN — CHRIS | Same month, not confirmed same event. |
| RWC-10 | Decide fate of 77 orphaned proxy files (no master anywhere) | OPEN — CHRIS | In `_NEEDS REVIEW - Orphaned Proxies` on drive. |
| RWC-11 | 32 raw pairs confirmed missing other lens | OPEN — CHRIS | Review in Insta360 Studio — may be unusable. |
| RWC-12 | ~26 renamed Vegas/Mammoth files lost ID pairing | OPEN — CHRIS | Cannot auto-pair. Root cause of "won't open" files. Manual review needed. |
| I-26 | Map cleanup items (5, from S23 scan) | OPEN — CHRIS | Dupes to delete/archive: financial_ops_daily.py x3, MASTER_LIVE_HANDOFF.md x3, old artie_playwright_downloader.py, Aura_Thai_Finance_Dashboard.xlsx x4 (Drive), Drive/00_Temp_Dump_Folder script copies. Full detail: _archive/MASTER_FILE_MAP_S40.md |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog. |
| A-09b | Chris fill Dish Map column B (dish names) | OPEN — CHRIS | CORRECTED S55: column B, not D (ground truth from live script — 2-col Dish Map). Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | PRIORITY — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| INV-13 | Park $5K USDT on KuCoin + set ladder limit orders $50/45/40K | OPEN — CHRIS | Approved S56. S57 FLAG: re-confirm $5K is surplus — cash tight (Buffett rule, playbook §9). |
| INV-08 | Move 1.7 BTC → cold wallet | PRIORITY — CHRIS | S55 decision. Only ladder cash stays on KuCoin. |
| INV-15 | Tax preparer meeting — 8 questions (playbook §7) | OPEN — CHRIS | Blocks Golfii backdoor + 529 vehicle choice (SB 529 check). |
| INV-14 | Open Auggie 529 this month — $300/mo, 100% equity | PRIORITY — CHRIS | Starts 15-yr 529→Roth clock. Vehicle pends INV-15. |
| INV-16 | Golfii backdoor Roth — Trad+Roth IRA, Form 8606 | BLOCKED | On INV-15 (MAGI + pro-rata). 70/30 approved S56. |
| EST-01 | Pull term life policy (benefit, term left, beneficiary) | PRIORITY — CHRIS | Feeds sizing check + EST-05. |
| EST-02 | WillMaker (~$110): Chris will + Auggie guardianship | OPEN — CHRIS | DIY tier. No dependencies. |
| EST-03 | Mom's revocable trust — 2–3 flat-fee attorney quotes | OPEN — CHRIS | Scope: trust + SBA consent + QSST/ESBT only (~$1.5–2.5K). Playbook v2.2 §9. |
| EST-04 | Crypto access letter template | OPEN — CLAUDE | Then Chris seals + stores. Without it, 1.7 BTC dies with him. |
| EST-05 | Beneficiary alignment (Roth/529/UTMA/term) | OPEN — CHRIS | After EST-01. |

---

## ROAMWITHCHRIS
See EMPIRE_STATUS.md → ROAMWITHCHRIS KEY FACTS (canonical — deduped S61).

---

## AURA SWEET
See EMPIRE_STATUS.md → AURA SWEET KEY FACTS (canonical — deduped S61; proof stat ported over).

---

## AURA THAI
Invoice System table + Key Revenue Numbers moved to EMPIRE_STATUS.md → AURA THAI sections (S62, migration step 2).**GOAL (S62 close):** Bedrock migration steps 2-5 EXECUTED — SYS-01 closed. CLAUDE-CORE V9 live (boot/freshness gate, 3-write handoff w/ debrief, huddle, PARK/RIDE). MASTER_FILE_MAP + RPG_LEDGER archived (GitHub `_archive/`); Drive Soul/ copies + map copy archived by Chris same-session; ARTIE-CORE map row removed; Tiller IMPORTRANGE note + I-26 cleanup digest ported. All pushes verified 200.

**COMMITMENTS (S62 close):**
- Chris: NEXT MAC SESSION OPENS ON LAVU DIAGNOSTIC → A-11 PATH-TO-BLACK. Fourth session (S58/S60/S61/S62) without moving the #1 constraint — the streak ends next session. No exceptions.
- Chris: relocate `github_pat.txt` out of Drive _ARCHIVE root to a deliberate home (fileId survives moves — nothing breaks meanwhile).
- Chris: reconcile the S62/S63 notes discrepancy — today ran as the real S62, so whatever those notes staged is still unaccounted for.
- Claude: first boot under the new protocol next session — run the full freshness gate and report whether it holds in practice.

Both agents load this file. It answers: what matters most right now?

---

## SESSION START COMMAND — S60
```
Load soul files.
S60 = BEDROCK SYSTEM REDESIGN session. Two Fable-5-authored design docs produced and verified this session (outputs/BEDROCK_SYSTEM_DESIGN_v1.md, v2.md) — v2 supersedes v1. Also produced: outputs/BOOT_LOADER_v2.md (ready for Chris to paste into Claude project custom instructions).

CORE DECISIONS MADE (Chris-approved, not yet executed):
1. Session counter: SPRINT.md is sole home, resolved S41/S58 fork (see counter note above).
2. RPG_LEDGER.md: retired. Zero effect on Chris ("doesn't have any effect on me"). See indexes/RPG_LEDGER.md banner.
3. Master file map: discontinued entirely (not replaced by another map) — GitHub copy, Drive copy, and Mac FILE_INDEX table all get archived. Replaced by a small REGISTRY (durable IDs only) living inside EMPIRE_STATUS.md + live tool lookups (Drive search, Glob, GitHub API) for everything else.
4. New team/motivation layer: the "Fireteam Sprint" loop — GOAL -> HUDDLE (3 questions, plan before executing) -> RUN -> DEBRIEF (Braintrust-style, blameless, no boardroom/elimination). Team = Chris + Claude today; Golfii (Chris's wife) + Kate (Golfii's sister) join for Aura Sweet sprints; scales later to Aura Thai staff as more instances of the same small loop, never a bigger loop. See EMPIRE_STATUS TEAM section.
5. Idea capture: revives the dormant _inbox/ + Obsidian vault (already built S34, abandoned since) instead of building anything new. PARK (2 min, default) or RIDE (~15 min, if Chris asks) then escort back to task.

MIGRATION STEP 5 (one-way doors) — Chris confirmed all five, NOT YET EXECUTED:
- Archive GitHub master-file-map/MASTER_FILE_MAP.md (port S41 findings into EMPIRE_STATUS first)
- Delete/archive Drive copy of the map (fileId 1wA_k8r5pZ7NcN7UHP2iejp1cOWDSCZGO)
- Retire Mac Aura Thai/FILE_INDEX.md hand-written table
- Mark Mac FILE_ORG_PLAN_S49.md executed -> archive/
- RPG_LEDGER.md — banner added this session (see above); full archive-move still pending

NEXT SESSION (S61) STARTS HERE:
1. Chris pastes outputs/BOOT_LOADER_v2.md into Claude project custom instructions (his action, not done yet as of S60 close).
2. Execute migration steps 2-4 (rewrite CLAUDE-CORE session-start/handoff sections per BEDROCK_SYSTEM_DESIGN_v2.md section 5 and 9; add full REGISTRY block with LIVE/FROZEN classes to EMPIRE_STATUS; add CACHE headers to Drive Soul/ copies).
3. Execute migration step 5 (the five one-way archive actions above).
4. Also unresolved from this session: Lavu daily-sales export pipeline stalled since 2026-05-26 (no June/July data) -- cause undiagnosed, blocks A-11 PATH-TO-BLACK; aura_thai_finance was edited 2026-07-03 with no new data added, cause unknown; Obsidian vault (~/Documents/pinyo-empire per the S34 note in _inbox/) sync status on the Mac unverified.
5. A-11 AURA THAI PATH-TO-BLACK still the #1 standing priority thread underneath all of the above -- has not moved in two sessions (S58, S60 both redirected elsewhere). Do not let a third session pass without naming that explicitly to Chris.
```

---

## LOAD NOTE — TOKEN EFFICIENCY
Do NOT load SESSION_HISTORY or MASTER_OPEN_ITEMS every session.
- If SPRINT.md session number is behind → pull those files from GitHub.
- Otherwise: SPRINT.md is the only context file needed at session start.

---

## CORRECTED DATA MODEL (S39 — do not revert)
- **Lavu = primary revenue source.** Captures ALL sales: dine-in + delivery + catering.
- GH, DD, UE are sub-channels. They contribute TO Lavu totals.
- Lavu XLS = UTF-16LE TSV — base64 decode → BOM strip → parse.

---

## PERMANENT RULES
> All dashboards live at ops.radrooster.co. No standalone URLs ever.
> Finance tab hardcodes data — MUST rebuild to read from Google Sheet (DASHBOARD ARCHITECTURE RULE violation).
> $5K/day focus filter: new ideas → parking lot unless they advance COGS → pipeline → unit economics → growth.

---

## ACTIVE ITEMS — S57 DIGEST

| ID | Item | Status | Notes |
|----|------|--------|-------|
| A-11 | Aura Thai PATH-TO-BLACK plan | NEXT — PRIORITY #1 | S63 OPENS HERE (4 sessions redirected). Chris brings fixed costs: rent, SBA payment, utilities, FOH labor, COGS. Deliverable: break-even + 3-lever plan. |
| A-12 | Install Apps Script V2 (timeout fix) | ✅ COMPLETE — S58 | Alerts→toasts, setupInvoiceSystem disarmed. |
| I-25 | Soul-file audit fixes | OPEN | 5H/7M/6L. H4 (header fork) CLOSED S62 via V9. Report: soul-files_audit_S55 (outputs). Chris approves order. |
| AS-01 | Aura Sweet spinoff strategy | OPEN — S56 | "How should we approach Aura Sweet as a spinoff?" |
| AS-02 | Somisomi competitive analysis | OPEN — S56 | Carried from S52 — Chris to walk the block first |
| AS-03 | Execute 3-move campaign | READY — CHRIS | Move 1: proof post. Move 2: BKBA collab. Move 3: Chef's Secret video. |
| AS-04 | Finalize poster in Canva | IN PROGRESS — CHRIS | Mockup complete. Copy locked. |
| RWC-05 | Story Index master sheet — build | 🟡 PHASE 1 DONE — S58 | Manifest built (3,505 rows, mechanical fields) on Crucial 2TB: `RoamWithChris_Footage-Manifest_v1.xlsx`. Story/Theme/Tags columns still need Chris. |
| RWC-06 | Footage consolidation onto external HD | 🟡 PARTIAL — S58 | Crucial 2TB connected + cleaned (2,055 junk files removed). Has Thailand/USA/Vietnam/Manila Layover/Japan. Still missing: Korea, London, Hawaii. |
| RWC-07 | DaVinci Resolve tagging pass | OPEN — CHRIS | After RWC-06 fully complete (Korea/London/Hawaii still need consolidating). |
| RWC-08 | Resolve ambiguous file — Aug 10 2024 Miami vs Key West | OPEN — CHRIS | 2 files in `_NEEDS REVIEW - Ambiguous Match` on drive. |
| RWC-09 | Confirm Thailand trip Nov 2024 == Bangkok Nov 2024? | OPEN — CHRIS | Same month, not confirmed same event. |
| RWC-10 | Decide fate of 77 orphaned proxy files (no master anywhere) | OPEN — CHRIS | In `_NEEDS REVIEW - Orphaned Proxies` on drive. |
| RWC-11 | 32 raw pairs confirmed missing other lens | OPEN — CHRIS | Review in Insta360 Studio — may be unusable. |
| RWC-12 | ~26 renamed Vegas/Mammoth files lost ID pairing | OPEN — CHRIS | Cannot auto-pair. Root cause of "won't open" files. Manual review needed. |
| I-26 | Map cleanup items (5, from S23 scan) | OPEN — CHRIS | Dupes to delete/archive: financial_ops_daily.py x3, MASTER_LIVE_HANDOFF.md x3, old artie_playwright_downloader.py, Aura_Thai_Finance_Dashboard.xlsx x4 (Drive), Drive/00_Temp_Dump_Folder script copies. Full detail: _archive/MASTER_FILE_MAP_S40.md |
| A-09 | COGS — Artie data entry | IN PROGRESS | Invoice system live. Artie entering backlog. |
| A-09b | Chris fill Dish Map column B (dish names) | OPEN — CHRIS | CORRECTED S55: column B, not D (ground truth from live script — 2-col Dish Map). Unlocks COGS by Dish. |
| A-08b | Finance tab: rebuild to Google Sheet | Next build | Hardcoded FINANCE_DATA violates DASHBOARD ARCHITECTURE RULE. |
| A-10 | ezCater onboarding | PRIORITY — CHRIS | Fee strategy + quick-ref doc delivered S42. Chris completing paperwork. |
| I-23 | artie_report_sync.py cron fix | OPEN | Not firing since May 8. |
| INV-13 | Park $5K USDT on KuCoin + set ladder limit orders $50/45/40K | OPEN — CHRIS | Approved S56. S57 FLAG: re-confirm $5K is surplus — cash tight (Buffett rule, playbook §9). |
| INV-08 | Move 1.7 BTC → cold wallet | PRIORITY — CHRIS | S55 decision. Only ladder cash stays on KuCoin. |
| INV-15 | Tax preparer meeting — 8 questions (playbook §7) | OPEN — CHRIS | Blocks Golfii backdoor + 529 vehicle choice (SB 529 check). |
| INV-14 | Open Auggie 529 this month — $300/mo, 100% equity | PRIORITY — CHRIS | Starts 15-yr 529→Roth clock. Vehicle pends INV-15. |
| INV-16 | Golfii backdoor Roth — Trad+Roth IRA, Form 8606 | BLOCKED | On INV-15 (MAGI + pro-rata). 70/30 approved S56. |
| EST-01 | Pull term life policy (benefit, term left, beneficiary) | PRIORITY — CHRIS | Feeds sizing check + EST-05. |
| EST-02 | WillMaker (~$110): Chris will + Auggie guardianship | OPEN — CHRIS | DIY tier. No dependencies. |
| EST-03 | Mom's revocable trust — 2–3 flat-fee attorney quotes | OPEN — CHRIS | Scope: trust + SBA consent + QSST/ESBT only (~$1.5–2.5K). Playbook v2.2 §9. |
| EST-04 | Crypto access letter template | OPEN — CLAUDE | Then Chris seals + stores. Without it, 1.7 BTC dies with him. |
| EST-05 | Beneficiary alignment (Roth/529/UTMA/term) | OPEN — CHRIS | After EST-01. |

---

## ROAMWITHCHRIS
See EMPIRE_STATUS.md → ROAMWITHCHRIS KEY FACTS (canonical — deduped S61).

---

## AURA SWEET
See EMPIRE_STATUS.md → AURA SWEET KEY FACTS (canonical — deduped S61; proof stat ported over).

---

## AURA THAI
Invoice System table + Key Revenue Numbers moved to EMPIRE_STATUS.md → AURA THAI sections (S62, migration step 2).
