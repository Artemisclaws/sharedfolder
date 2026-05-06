# Empire AI — Shared Folder

Shared file database for Claude, Artie, and Chris.

## Structure

- `empire-status/` — EMPIRE_STATUS.md lives here. Source of truth for all empire metrics.
- `sessions/` — Session handoff files and journals.
- `artie-config/` — Artie read-only config files.

## Rules

- EMPIRE_STATUS.md is the single source of truth. Always overwrite, never duplicate.
- Claude writes via HTTPS + PAT after each session.
- Artie reads on sync; writes only to artie-config/.
- No Drive for shared files. GitHub is the database.
