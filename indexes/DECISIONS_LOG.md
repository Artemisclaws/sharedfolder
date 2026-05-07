# DECISIONS_LOG.md — Key Architectural Decisions
**Updated by:** Claude when a major decision is made
**Last Updated:** 2026-05-07 | Session 29
**GitHub:** `indexes/DECISIONS_LOG.md`

Every major architectural, strategic, or system decision that shapes how the empire operates. The "why" behind every "what." YouTube gold and recovery anchor.

Format: `YYYY-MM-DD | Decision | Why | Alternatives Rejected | Session`

---

## SYSTEM ARCHITECTURE

| Date | Decision | Why | Alternatives Rejected | Session |
|------|----------|-----|-----------------------|---------|
| 2026-04-06 | Dual agent architecture: Claude (strategist) + Artie (executor) | Separation of thinking from doing. Claude can't run 24/7; Artie can't strategize. | Single agent doing everything; Claude-only | S04 |
| 2026-04-06 | 11 mental models codified as Thinking OS with triggers | Models without triggers stay theoretical. Triggers make them automatic. | Reference list only; no structured activation | S04 |
| 2026-04-19 | Thinking OS embedded in soul files (not just conversation) | Must survive session resets. If it's not in the soul file, it doesn't persist. | Re-prompting every session | S14 |
| 2026-05-05 | GitHub as single source of truth for all living documents | Both agents need to read and write the same files. Drive doesn't support bidirectional agent access cleanly. | Drive only; Notion; local files only | S26 |
| 2026-05-05 | Discord as primary channel (Telegram as backup only) | Discord has threads, channels, and bot separation. Telegram is one flat conversation. | Telegram primary; WhatsApp; Slack | S26 |
| 2026-05-05 | Cloudflare Pages for dashboard (not Artie's PC tunnel) | Artie's PC going offline = dashboard offline. Pages has 99.9% uptime and zero infrastructure cost. | Keep Cloudflare Tunnel; self-hosted VPS | S27 |
| 2026-05-06 | MASTER_OPEN_ITEMS.md replaces handoff files | Handoffs became stale instantly. A living task tracker doesn't. "The handoff IS the file." | Session handoff .md files; Trello; Notion | S27 |
| 2026-05-07 | GitHub = living brain. Drive = file cabinet. | Living docs (updated repeatedly) → GitHub. Static docs (written once) → Drive. Clean separation of concerns. | Everything on GitHub; everything on Drive; Notion hybrid | S29 |
| 2026-05-07 | Soul files migrate from Drive/Soul to GitHub soul/ | Both agents need latest soul. Drive sync had lag and manual steps. GitHub is always current. | Keep Drive as soul home; use Drive + GitHub sync | S29 |
| 2026-05-07 | GitHub filenames: no version numbers. Drive files: Munger convention with version. | Git IS version control for GitHub files. Version numbers in filenames create confusion. Drive has no native versioning, so Munger convention necessary. | Version numbers everywhere; no versioning anywhere | S29 |
| 2026-05-07 | Journal = one Google Doc per session in Drive/JOURNAL/ (YouTube format) | Session journals are written once, sealed, never edited. Not a "living doc." Rich Google Doc format suits YouTube content prep. | GitHub journal file; single running journal; notion | S29 |
| 2026-05-07 | Drive folder structure: Hybrid Musk/Bezos/Munger | Musk: 00_LOAD_ME fast brief. Bezos: self-contained business folders. Munger: filename tells you everything. No single system alone solved all three needs. | Numbered folders (current); flat structure; Notion | S29 |

---

## BUSINESS DECISIONS

| Date | Decision | Why | Alternatives Rejected | Session |
|------|----------|-----|-----------------------|---------|
| 2026-05-05 | Pinyo Farms: Phase 1 market validation before building anything | Don't build infrastructure for a business that hasn't been validated. | Build first, validate later | S23 |
| 2026-05-05 | Roam: Master content plan before any Artie automation | Content strategy first. Automating the wrong content is worse than no content. | Automate existing content; hire content creator | S23 |

---

## RULES & PROTOCOLS

| Date | Decision | Why | Alternatives Rejected | Session |
|------|----------|-----|-----------------------|---------|
| 2026-04-20 | No Assumptions core rule — ask before producing any plan | A wrong plan built on assumptions wastes more time than a good question saves. | Infer from context; produce draft then correct | S18 |
| 2026-05-07 | Index everything — JOURNAL_INDEX, SOUL_CHANGELOG, DECISIONS_LOG, MASTER_INDEX | Without maps, finding information requires scanning. Maps make the system scale. | Search when needed; no index | S29 |
| 2026-05-07 | Paper trail for soul changes via SOUL_CHANGELOG + JOURNAL entries | Rule changes have history and YouTube value. Without a log, "why does this rule exist?" is unanswerable. | Git blame only; no changelog | S29 |

---

*This file is append-only. Decisions are never deleted — they explain the history of the system.*
*Add a row any time a major architectural or strategic decision is made.*
