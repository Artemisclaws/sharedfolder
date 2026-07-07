# SPRINT.md — Current Sprint Priorities
**Updated by:** Claude | Session S62 (closed) | 2026-07-07
**GitHub:** `00-load-me/SPRINT.md`

**Counter note (S60):** Session numbering forked — this SPRINT lineage was at S58 (closed 2026-07-03). A same-day session on 2026-07-04 (Google Drive Desktop sync repair; added CLAUDE-CORE's WORKING DOCUMENTS rule, V8) ran as "S59" but never updated this counter. This session (S60) declares the SPRINT lineage canonical going forward. **SPRINT.md line item below is now the sole home of the session counter — no other file may originate a session number.**
**COUNTER: S62 | closed 2026-07-07**

**GOAL (S62 close):** Voice-session RoamWithChris story braindump (Chris driving). Two new stories captured: **Augustus Chang** (Bible locked, AI-visuals-only episode) and **Vietnam Cousin Trip** (raw braindump, not yet Bible-locked, likely splits into a 3-part series: Halong Bay / Ninh Binh / Ha Giang Loop). **Correction from S61 close:** the prior handoff claimed these were written to Drive/GitHub but the write never actually executed (Drive MCP was down and the GitHub push was narrated, not run) — caught and fixed at the start of S62 when Chris asked "did we record this session in the right places?" Both story docs are now genuinely saved to Drive. Migration steps 2-5 (Bedrock CLAUDE-CORE rewrite, REGISTRY, CACHE headers) still NOT executed — still carrying forward.

**COMMITMENTS (huddle, S62 close):**
- Claude: verify-before-claiming-done going forward — do not narrate a save/push as complete without an actual tool call confirming it. This session's opening exchange is the concrete example to reference if it recurs.
- Claude: hold migration steps 2-5 until Chris is at the Mac with review bandwidth. aura_thai_finance still RED — data still ends 2026-05-31 despite touched mtimes. Lavu export pipeline still stalled (unchanged since S61).
- Claude: naming convention locked — Chris's college friend is **Augustus Chang**; Chris's son is **Auggie / Augustus Pinyo**. Always disambiguate by full name in any RWC reference doc.
- Chris: Vietnam Cousin Trip story needs Ninh Binh and Ha Giang Loop details still — only Halong Bay was captured in depth this session.
- Chris: next Mac session should open on A-11 PATH-TO-BLACK or the Lavu diagnostic — this is now the **fourth** session (S58, S60, S61, S62) this has been redirected. Flagging explicitly per standing SPRINT rule.

Both agents load this file. It answers: what matters most right now?

---

## SESSION START — S63
Boot per CLAUDE-CORE V9 (custom-instructions boot-loader is live). Open on: Lavu export stall diagnostic (blocks A-11), then A-11 PATH-TO-BLACK. Bedrock system is fully migrated — no infra work pending except Phase 2 (Artie freshness cron, gated on I-23) after 2-3 weeks of manual boots.

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
