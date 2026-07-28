# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S69 (closed) | 2026-07-28
**GitHub:** `00-load-me/SPRINT.md`

**Counter note (S60):** Session numbering forked — this SPRINT lineage was at S58 (closed 2026-07-03). A same-day session on 2026-07-04 (Google Drive Desktop sync repair; added CLAUDE-CORE's WORKING DOCUMENTS rule, V8) ran as "S59" but never updated this counter. This session (S60) declares the SPRINT lineage canonical going forward. **SPRINT.md line item below is now the sole home of the session counter — no other file may originate a session number.**
**COUNTER: S69 | closed 2026-07-28**

**GOAL (S69 close):** Filed and reconciled this week's (and prior) DoorDash/UberEats delivery reports, and — the real deliverable — finally solved the standing problem that Claude had no reliable way to write into `aura_thai_finance` directly. Built `aura_thai_finance_write_endpoint.gs` (Apps Script Web App: listSheets/readRange/setCell/setRange/appendRow, secret-gated). Deployment was NOT trivial: first URL was an accidental Library-type deployment (not HTTP-callable); rebuilt project still threw a generic "unable to open file" error on POST even from the account owner directly in-browser — isolated via a bare-minimum script.new control test (worked instantly), proving the ORIGINAL finance-bound Apps Script project itself was corrupted (likely Library-deployment residue), not the account. Chris rebuilt the project from scratch with the same code and it worked — but only via GET with a URL-encoded `?payload=` param; POST still fails identically on this specific deployment for unknown reasons (worked around, not root-caused). Endpoint now live: `https://script.google.com/macros/s/AKfycbzpDwWXpxAfryJ6Re23HzePLOaWXTgGAkVMXLxTVArH-pzZtrzAWuKpk5KcWzSavdNLHQ/exec`, WRITE_SECRET stored in the sheet's Script Properties (value: `1-10`). Wrote 2 real rows into `Delivery Payouts`: UberEats 7/13-7/19 (31 orders, $1,724.46 gross, -$216.22 marketplace fee, -$162.92 facilitator tax, $1,338.43 net — cross-verified against 3 independent sources: order CSV, item CSV, official payout PDF, all matched exactly) and DoorDash 7/13-7/19 (91 orders, $4,121.48 gross Subtotal — fees/net payout still PENDING, need the DoorDash Financial Detail/Payout Summary report). Caught and corrected a commission-% math error before writing (19.5% miscalc → recomputed to the correct 12.54%) per Chris's explicit "double check then execute" instruction. Filed 5 DoorDash report zips + 9 of 12 UberEats files into their correct Drive folders (`Financial Data`, `UberEats`) — 3 UberEats files (2 financial CSVs + 1 Gmail payout PDF) still only in session scratch, not yet uploaded. Established the ongoing intake workflow: new connected Mac folder `Finance Dump Folder` (+ `Archive` subfolder) as the standard drop/processed location going forward, replacing ad hoc chat uploads — confirmed `mv` works for archiving (no delete permission needed). Delivered `REPORTS_NEEDED_checklist.md` (checkbox format, saved in Finance Dump Folder) auditing every tab in `aura_thai_finance` against the live sheet, not assumption: Lavu Daily Sales (Pretax) stalled at 7/7 is now flagged the single biggest gap (bigger than the delivery-platform gaps this session focused on), GrubHub Weekly Summary stalled since early May, plus the two remaining DoorDash/UberEats gap-fill windows (7/8-7/12). **INV-17 (Thailand Kai-Fak) and A-11 PATH-TO-BLACK were NOT touched — A-11 is now 10 sessions cold.**

**INV-17 — THAILAND KAI-FAK DEAL: GROUND TRUTH (do not re-derive)**
*Land (read off the deed photos — verify against the land office before acting):*
- Title type: **Chanote / โฉนดที่ดิน (Nor Sor 4 Jor)** — strongest freehold title in Thailand. Good collateral class.
- Deed no. **45188** | parcel (เลขที่ดิน) **317** | survey page (หน้าสำรวจ) **7844**
- Location: **Nong Saeng subdistrict, Wapi Pathum district, Maha Sarakham province** (rural Isaan)
- Size: **1 rai 0 ngan 57 wah = 457 sq wah ≈ 1,828 sqm (~0.45 acre)**
- Govt appraisal, certificate dated **16 July 2026**: 2,650 THB/wah × 457 = **1,211,050 THB**. Certificate states no seizure/freeze and no replacement deed issued.
- **Ownership chain flag:** deed face names **Sitthisak Kaewsingh**; the registration record on the reverse shows a sale on **24 Dec 2018 to Ms. Patchareerat Ocha**, who is the current owner and in whose name the 2026 appraisal was issued. The redeemer must BE her (or her lawful attorney-in-fact) — confirm ID against the deed.
- **Odd but not necessarily wrong:** appraisal certificate was issued by the **Bangkok / Phra Khanong** land office for a Maha Sarakham parcel. Plausible via the Land Department central system, but it is a reason to run a fresh title check at the **Wapi Pathum** land office rather than trusting the paper.

*The two blockers (this is the important part):*
1. **The 15% cap kills the spread.** Because this is agricultural/residential land held by an individual, it falls under the **2019 Protection Act (PAHA)**. The redemption price may not exceed principal + a benefit of **max 15%/yr (~1.25%/mo)**; market rates run 9–15%/yr. The proposed **2%/mo (24%/yr) is illegal and unenforceable.** Chris cannot charge the borrower 24% and pay lenders 15% — the borrower's legal max IS the number he wanted to pay out. No margin exists in the structure as designed. Realistic options: lenders take something under 15% and Chris takes an arrangement/servicing fee, OR Chris is a lender himself and 15% is the return, not a spread.
2. **Foreigners cannot hold Thai land title, and Kai-Fak transfers title on registration.** If the borrower defaults, the lender KEEPS the land — so the buyer-of-record must be a genuine Thai national or Thai-majority entity investing their own money. Putting a Thai person on title to hold for Chris is an **illegal nominee arrangement (criminal offense under the Land Code)**. If his mom is Thai and using her own funds she can legitimately be the buyer — but then it is her investment with Chris advising, not his position wearing her name.

*Other PAHA terms confirmed:* minimum 1-year redemption period (his 1-yr term is fine), 10-year maximum, borrower retains possession/use during the term, and the lender must notify the borrower 3–6 months before expiry or the redemption window auto-extends 6 months.

*Deal quality:* 500K against 1,211,050 appraised = **~41% LTV** — conservative, inside the safe Kai-Fak band. The real risk is **liquidity, not the ratio**: rural Isaan land can take a year-plus to sell and may not fetch appraised value in a distress sale. The 2,650/wah appraisal suggests village/roadside rather than deep farmland (more sellable) — a hypothesis to verify on the ground, not assume.

*Delivered in chat:* due-diligence list (physical inspection, fresh title/encumbrance search at Wapi Pathum, independent market valuation + local broker liquidity read, identity match, register at the land office and never by private contract), structuring guidance, 4 exit strategies (redemption / negotiated extension within the 10-yr cap / default→keep and resell budgeting 6–18 months / assign the Kai-Fak position to another Thai investor), and the lender term-sheet checklist (rate ≤15%, who bears servicing fee, payment cadence, **who holds title and what happens to it on default**, capital-loss waterfall if sold below principal, who funds/decides a resale, extension rule, and — if multiple lenders — split, decision rights and default-liquidation mechanics in writing up front).

*Claude's honest read, stated to Chris:* at a 15% ceiling with real illiquidity risk and a structure he cannot personally sit inside, the risk-adjusted return is thinner than the "make interest, worst case we get land" pitch suggests. Can still be worth doing as his mom's investment with Chris advising.

**COMMITMENTS (huddle, S69 close):**
- Claude (next session, if Chris wants them): build the **due-diligence checklist** + **draft term sheet** for INV-17 — still offered, still not answered, now carried 2 sessions.
- Chris: decide the **fundamental question on INV-17** before any more work — is this his mom's deal (she is the Thai buyer-of-record with her own funds, Chris advises), or is he out? There is no compliant version where Chris holds the title.
- Chris: if INV-17 proceeds, engage a **Thai property lawyer in Maha Sarakham** to paper and register it. Non-negotiable — Claude is not a lawyer and this is cross-border property lending.
- Chris: **CARRIED FROM S66 (unchanged, still open)** — send `lavu_negotiation_email-draft_v16_round3_FINAL.md` to Kassey.
- Claude, next session touching the Lavu thread: **CARRIED FROM S66 (full reserve playbook — do not lose this)** — load `checkpoint_lavu-negotiation_2026-07-22.md` + Kassey's round-3 reply, then run round 4. Reserve playbook (deliberately NOT sent in round 3 — anchor discipline): if Kassey rejects the 12-month/no-ETF ask, deploy the declining-ETF language (tied to documented, unamortized hardware subsidy, straight-line to zero — not a flat remaining-months formula), the no-penalty business-sale/closure exit, and the no-penalty exit if Lavu stops materially supporting/updating the hardware. The moment she offers any ETF movement, immediately ask for the exact formula and amortization schedule in writing. Statement details, processor identity (CardConnect), and the $269/mo leak figure stay private — never send.
- Chris: A-11 PATH-TO-BLACK — Lavu export stall diagnostic still owed (needs Mac). **10th session redirected past it.**
- Claude/Chris: the S65 forked question is now **five sessions unresolved** — does A-11 need explicit protected time (a session where Chris pre-commits to no redirects)? Stop re-asking it in the huddle and either schedule it or consciously drop it.
- Claude (process): **SESSION_HISTORY is behind — S65 and S66 rows were never written.** Still flagged, NOT backfilled. Chris to decide whether to reconstruct them from EMPIRE_STATUS or accept the gap.
- Chris: drop new Aura Thai reports straight into the new **`Finance Dump Folder`** (Mac, synced to Drive) — see `Finance Dump Folder/REPORTS_NEEDED_checklist.md` for exactly what's still needed to get `aura_thai_finance` current: Lavu Daily Totals export (7/8→today, now the single biggest gap), GrubHub sales export (5/4→today), plus DoorDash/UberEats gap-fills for 7/8-7/12 and the DoorDash Financial Detail report to close the 7/13-7/19 PENDING row.
- Chris: two harmless leftover test files (`_write_test.txt` in Finance Dump Folder, `_mvtest.txt` in Archive) — Claude cannot delete without explicit permission; say the word or ignore them.
- Chris: decide whether the fix to the 1-row DoorDash CSV data-entry typo (SALES_BY_ORDER, order 22991601, cosmetic only) is worth a session — carried, low priority.

Both agents load this file. It answers: what matters most right now?

Both agents load this file. It answers: what matters most right now?

---

## SESSION START — S70
Boot per CLAUDE-CORE V9. **FIRST QUESTION TO CHRIS: does this session open on A-11 PATH-TO-BLACK (now 10 sessions cold), INV-17 (Thailand Kai-Fak — build the DD checklist + term sheet, or close the thread), the Lavu contract renegotiation (round 4), the options wheel thread, continuing Aura Thai finance intake (Finance Dump Folder checklist), or an explicit different priority?** Do not silently continue any one thread without naming the choice out loud. If Aura Thai finance: the write endpoint is LIVE — `https://script.google.com/macros/s/AKfycbzpDwWXpxAfryJ6Re23HzePLOaWXTgGAkVMXLxTVArH-pzZtrzAWuKpk5KcWzSavdNLHQ/exec`, WRITE_SECRET `1-10`, GET-only (POST fails on this deployment for unknown reasons — use `?payload=<url-encoded JSON>`), and `Finance Dump Folder/REPORTS_NEEDED_checklist.md` on Drive is the live checklist — check it against whatever Chris has dropped in `Finance Dump Folder` before assuming what's missing. If INV-17: the ground truth is in this file's S67 block — do NOT re-read the deed photos or re-derive the appraisal, and lead with the two blockers (15% PAHA cap, foreign-ownership/nominee) before any modelling. If Lavu contract renegotiation: Kassey should have replied to round 3 (`lavu_negotiation_email-draft_v16_round3_FINAL.md`) — run round 4 against the reserve playbook in the S67 commitments above. If investing: options wheel state lives in `investing/OPTIONS_POSITIONS_LOG.md` + playbook §5/v1.1–v1.6 (GitHub, source of truth) — Cycle 1's 3 filled legs have resting GTC Buy-to-Close orders in Fidelity (KO $0.23 / SCHD $0.09 / VZ $0.25 limits), no active monitoring needed until they fill or expire 8/21. Trading log (supplementary): Google Sheet fileId `1SkOTFF5ExGplHl08nEjREnps3yhS5PKLTdUpUkxzj90`.

**BOOT NOTE (S69):** boot sequence did run this session (fetched SPRINT/EMPIRE_STATUS/SPRINT-freshness at start), but this was a session-length continuation of prior Aura Thai finance work rather than a fresh huddle-from-zero — no 3-question huddle was run at open. Chris asked for "handoff and journal" at close, which surfaced that CHRONICLE is a genuinely separate, keyword-gated protocol from handoff — worth remembering going forward rather than assuming "handoff" covers both.

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
| INV-17 | Thailand Kai-Fak deal (500K THB, Maha Sarakham chanote) | 🔴 BLOCKED ON DECISION — S67 | Ground truth in S67 GOAL block above. Two blockers: PAHA caps benefit at 15%/yr (kills the 24% spread plan); foreigner cannot hold title + nominee is criminal. Chris must decide if this is his mom's deal or dead. DD checklist + term sheet offered, not built. |

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
