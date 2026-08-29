# SOUL_CHANGELOG.md — Soul File Change History
**Updated by:** Claude every time a soul file changes
**Last Updated:** 2026-05-07 | Session 30
**GitHub:** `indexes/SOUL_CHANGELOG.md`

Every rule change, soul file update, or architectural shift gets one line here. This is the paper trail for the YouTube channel and for understanding why the system is the way it is.

Format: `YYYY-MM-DD | Version | File | What changed | Why | Session`

---

## 2026 — April (Reconstructed from handoffs)

- 2026-04-06 | V1 | SOUL.md (pre-ARTIE-CORE) | Master System Prompt V1 delivered — dual-role persona locked | First complete soul prompt | S04, S05
- 2026-04-13 | — | ARTIE-CORE | gog CLI reference appended (100 lines, auth wrapper embedded) | Artie kept guessing flags wrong | S07, S08
- 2026-04-17 | — | ARTIE-CORE | gog sheets append syntax added (positional + --values-json) | Sheets writes were failing | S11, S12
- 2026-04-19 | V3 | ARTIE-CORE | Thinking OS summary block + domain routing table added | Centralized mental models in one place | S14
- 2026-04-19 | V3 | ARTIE-STANDARDS | Full Thinking OS with triggers added, full reorganization | Mental models needed triggers to be actionable | S14
- 2026-04-19 | V2 | Claude Session Doc | Priority hierarchy + trigger-based mental model system + 24 domain models | Claude needed same OS as Artie | S14
- 2026-04-28 | — | ARTIE-STANDARDS | EMPIRE_STATUS update protocol added | Artie wasn't updating status consistently | S18

---

## 2026 — May

- 2026-05-05 | V1 | CLAUDE-CORE.md | Created — Claude's identity, authority, session start protocol, file map | Claude needed a soul file of his own | S23
- 2026-05-05 | V1 | ARTIE-RUNBOOK.md | Drafted with 10 SOPs — uploaded to Drive/Soul | Artie forgot recurring tasks without step-by-step SOPs | S23
- 2026-05-05 | V2 | ARTIE-PROJECTS.md | All placeholders filled with actual project context | Task bible was empty — Artie couldn't prioritize | S24
- 2026-05-05 | V1 | ARTIE-DEPT.md | Created with all 8 Discord channel IDs | Artie needed channel routing without asking every time | S24
- 2026-05-05 | V4 | ARTIE-CORE.md | GitHub shared file database added; EMPIRE_STATUS protocol updated to GitHub | GitHub became source of truth this session | S26
- 2026-05-05 | V4 | ARTIE-STANDARDS.md | EMPIRE_STATUS protocol updated — Drive deprecated, GitHub only | Single source of truth, no drift between copies | S26
- 2026-05-05 | V1 | ARTIE-DEPT.md | Discord channel IDs section added (8 channels) | Discord replaced Telegram as primary channel | S26
- 2026-05-07 | V1 | THINKING_OS.md | Extracted from ARTIE-STANDARDS as standalone shared file | Both agents need mental models — shouldn't live only in Artie's soul | S29
- 2026-05-07 | V1 | EMPIRE_RULES.md | Created — shared quality + security rules for both agents | Rules were scattered across multiple files, no single source | S29
- 2026-05-07 | V2 | CLAUDE-CORE.md | File paths updated to GitHub structure; build queue updated; Discord bot added | Drive → GitHub migration; V1 was pointing to deprecated locations | S29
- 2026-05-07 | V1 | CLAUDE-PROJECTS.md | Created — Claude's dedicated build queue and project tracker | CLAUDE-CORE was too long; build queue deserves its own file | S29
- 2026-05-07 | — | ALL ARTIE soul files | Migration from Drive/Soul to GitHub soul/artie/ — planned, execution pending | GitHub is source of truth for living docs | S29

---

- 2026-05-07 | V4 | ARTIE-CORE.md | Migrated to GitHub soul/artie/. Updated to V4: CORE FILE MAP now has GitHub paths, SOUL SYNC updated with sync_soul.sh GitHub raw URL script, Drive soul folder marked ARCHIVED | GitHub is source of truth — S30 migration complete | S30
- 2026-05-07 | V4 | ARTIE-STANDARDS.md | Migrated to GitHub soul/artie/. EMPIRE_STATUS protocol updated: Python snippet uses GitHub API. SOUL SYNC RULE updated: GitHub is source of truth, Drive archived | S30 migration | S30
- 2026-05-07 | V2 | ARTIE-PROJECTS.md | Migrated to GitHub soul/artie/. Updated sync rule to reference GitHub path | S30 migration | S30
- 2026-05-07 | V1 | ARTIE-RUNBOOK.md | Migrated to GitHub soul/artie/. SOP 09 updated: sync_soul.sh now fetches from GitHub raw URLs. SOP 07 updated: EMPIRE_STATUS update uses GitHub API | S30 migration | S30
- 2026-05-07 | V1 | ARTIE-DEPT.md | Migrated to GitHub soul/artie/. Discord listed as primary, Telegram as backup | S30 migration | S30

---

## OUTSTANDING

- ✅ DONE S30: All 5 Artie soul files migrated to GitHub soul/artie/. sync_soul.sh updated in ARTIE-CORE V4.
- THINKING_OS.md section in ARTIE-STANDARDS.md — now redundant once both agents load standalone THINKING_OS.md. Remove from ARTIE-STANDARDS in next Artie soul update session.
- Drive/Soul folder — ready to archive to Drive/_ARCHIVE/. Chris must do this manually in Drive (file IDs preserved).

---

*This file is append-only. Never delete entries — they are the history.*
| CLAUDE-CORE.md | V3→V4 | S49 | 2026-06-23 | Step 6 fully rewritten — removed all bash blocks, Drive MCP only. Fixed S32 hardcode in Step 1. Added CHANGE CONTROL section. Root cause of S40–S48 silent push failures eliminated. |
| CLAUDE-CORE.md | V7: Added PROVEN-MODEL STANDARD section (sector-leader models applied to Chris's specific situation, named in deliverables) | Chris standing instruction | S55 |
| CLAUDE-CORE.md | V7→V8: Added WORKING DOCUMENTS — COWORK + DRIVE SYNC section under FILE SYSTEM REFERENCE (all working docs edited via ~/Documents/G Drive with Claude; Drive connector cannot edit files) | Chris explicit approval — permanent workflow | S59 |
| CLAUDE-CORE.md | V8→V9: Bedrock migration step 3 — SESSION BOOT PROTOCOL (freshness gate + boot line + huddle), handoff trimmed to 3 writes w/ debrief row, PARK/RIDE idea capture, five-homes + cache rule, master-file-map section removed (REGISTRY replaces), RPG_LEDGER retired, header fork V3/V8 fixed (closes I-25 H4) | Chris-approved Bedrock v2 migration (BEDROCK_SYSTEM_DESIGN_v2.md §5/§9/§10) | S62 |
| ARTIE-CORE.md | Removed MASTER_FILE_MAP reference row | Map retired S62 (REGISTRY in EMPIRE_STATUS replaces it) | S62 |
| CLAUDE-CORE.md | V9→V10: FILE SYSTEM REFERENCE's Google Drive section fully rewritten — three-account role split (chrispinyo/aurathailb/artemisclaws) with folder-scoped Editor access only, 5-bucket ATLAS/Active/Final/Resource/_ARCHIVE structure (supersedes the two-lane v2 §6 model and the prior per-business nesting), file-naming convention (versioned living files vs. dated point-in-time files), Mac sync folder redefined as the Active/ working mirror, no-hand-maintained-map rule reaffirmed against Forte's PARA, Wickman's EOS, and Gmail's "search, don't sort" | Chris explicit approval — full redesign session, past reorganizations hadn't solved findability | S72 |

| SHARED-CORE.md | Added LOG KEYWORD PROTOCOL section — 'log:' keyword writes dated one-liners to events/BUSINESS_LOG.md or personal/PERSONAL_LOG.md, both agents respond | Chris explicit request (Lavu negotiation session) — needed a low-friction way to record business/personal events without full CHRONICLE/handoff overhead | S67-adjacent |
| EMPIRE_STATUS.md | REGISTRY: added events/BUSINESS_LOG.md and personal/PERSONAL_LOG.md as canonical, both-agent-editable file pointers | Chris explicit approval — new events/ and personal/ folders created in repo, prevents duplicate log files | S67-adjacent |
