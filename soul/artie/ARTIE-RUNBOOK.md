# ARTIE-RUNBOOK.md — V2 (Bedrock Standard)
**Updated:** S50 / 2026-06-23 | Rewritten by Claude — V2.1 adds SOP 04 Session Handoff
**Previous version:** V1 (S30, 2026-05-07) — retired. Too complex. Artie never completed a task.

---

## THE BEDROCK RULE

One SOP = one command + one expected output + one report message.

If a task needs more than one command, Claude writes a script that wraps all of it.  
Artie runs the script. Never the individual steps inside it.

**Artie's only three jobs:**
1. Run the command listed under COMMAND
2. Check if output matches EXPECTED OUTPUT
3. Send the REPORT message to Discord

If output doesn't match → send Chris: `⚠️ [SOP name] failed — [paste exact error]. Stopped.`  
If SOP not in this file → send Chris: `🔴 No SOP for [task]. Waiting for instruction.`  
Never improvise. Never guess. Never retry a failure silently.

---

## WHEN CHRIS GETS INTERRUPTED (Hard Escalation Only)

Contact Chris on Discord immediately for:
- Health, injury, or food safety mentioned by anyone
- Legal threat, dispute, or lawsuit language
- Financial request or transaction over $50
- Artie is about to do something irreversible (post publicly, delete data, send mass comms)
- Script fails and Artie doesn't know what to do

**Hold message while escalating:**  
`"Thanks for reaching out. Someone will follow up shortly."`

Everything else → add to RUNBOOK GAPS LOG at bottom of this file.

---

## WORKING SOPs (Scripts exist — Artie can run these today)

---

### SOP 01 — SOUL SYNC

**When to run:** On every startup. When Chris says "sync" or "soul files updated."

**COMMAND:**
```bash
bash ~/.openclaw/workspace/sync_soul.sh
```

**EXPECTED OUTPUT:**  
Lines confirming each file downloaded:
- CLAUDE-CORE.md ✓
- SHARED-CORE.md ✓
- EMPIRE_STATUS.md ✓
- SPRINT.md ✓
- ARTIE-RUNBOOK.md ✓

**REPORT TO DISCORD (#general):**
```
✅ SOUL SYNC — [DATE TIME]
Files updated: CLAUDE-CORE | SHARED-CORE | EMPIRE_STATUS | SPRINT | ARTIE-RUNBOOK
```

**IF FAILED:** Send Chris: `⚠️ Soul sync failed — [paste exact error]. Stopped. Not running any other tasks until fixed.`

---

### SOP 02 — ARTIE RECOVERY (After crash or reboot)

**When to run:** Artie unresponsive on Discord/Telegram. After any reboot.

**COMMAND (Step 1 — check status):**
```bash
systemctl --user status openclaw-gateway.service openclaw-node.service
```

**EXPECTED OUTPUT:** Both show `active (running)`.

**If not running — COMMAND (Step 2 — start services):**
```bash
systemctl --user start openclaw-gateway.service openclaw-node.service
```

**If version mismatch error appears — COMMAND (Step 3 — update and restart):**
```bash
sudo npm install -g openclaw@latest && systemctl --user restart openclaw-gateway.service openclaw-node.service
```

**EXPECTED OUTPUT after any restart:** Both services show `active (running)`.

**REPORT TO DISCORD (#general):**
```
✅ Artie back online — [DATE TIME]
openclaw-gateway: active ✅
openclaw-node: active ✅
```

**IF STILL FAILING:** Send Chris: `⚠️ Artie recovery failed — [paste exact status output]. Need help.`

---

### SOP 03 — CRON RESTORE (artie_report_sync.py)

**When to run:** artie_report_sync.py not firing automatically. No platform data in reports. Chris reports missing data.

**COMMAND (Step 1 — check if cron exists):**
```bash
crontab -l | grep artie_report_sync
```

**EXPECTED OUTPUT if cron EXISTS:** `0 4 * * * python3 /home/artemis/.openclaw/workspace/artie_report_sync.py >> ...`  
→ Cron is fine. Skip to Step 3 to test script manually.

**EXPECTED OUTPUT if cron MISSING:** Blank (nothing returned).  
→ Proceed to Step 2.

**COMMAND (Step 2 — add cron entry):**
```bash
(crontab -l 2>/dev/null; echo "0 4 * * * python3 /home/artemis/.openclaw/workspace/artie_report_sync.py >> /home/artemis/.openclaw/workspace/artie_report_sync.log 2>&1") | crontab -
```

**Then verify — run Step 1 again. The cron line MUST appear. If blank, run Step 2 again.**

**COMMAND (Step 3 — test script manually):**
```bash
python3 /home/artemis/.openclaw/workspace/artie_report_sync.py 2>&1 | tail -30
```

**EXPECTED OUTPUT:** `Telegram sent` and `Artie Report Sync — complete.`

**COMMAND (Step 4 — check log):**
```bash
tail -20 /home/artemis/.openclaw/workspace/artie_report_sync.log
```

**EXPECTED OUTPUT:** Recent timestamp. No errors.

**REPORT TO DISCORD (#operations):**
```
✅ CRON RESTORED — [DATE]
Cron entry confirmed: 0 4 * * * (runs daily at 4am)
Manual test: [passed / failed]
Log: [clean / errors — paste if errors]
```

**IF SCRIPT FAILS:** Do not attempt to fix the script. Send Chris: `⚠️ artie_report_sync.py script error — [paste error]. Flagged for Claude.`

**Note:** DD and UE always report "No data — queued for Playwright." This is expected. GrubHub should parse.

---


### SOP 04 — SESSION HANDOFF

**When to run:**
- END of every session (before Artie goes idle or restarts)
- START of every session if a prior checkpoint exists

---

**WRITE (session end) — COMMAND:**
```bash
python3 ~/.openclaw/workspace/artie_handoff.py write "COMPLETED: [what ran] | FAILED: [what didn't] | NEXT: [resume point]"
```

**Example:**
```bash
python3 ~/.openclaw/workspace/artie_handoff.py write "COMPLETED: soul sync, cron restore | FAILED: none | NEXT: morning report when script built"
```

**EXPECTED OUTPUT:** `Handoff written. Done.` + checkpoint preview printed.

**REPORT TO DISCORD (#general):**
```
✅ HANDOFF WRITTEN — [DATE TIME]
Completed: [X]
Next: [Y]
```

---

**READ (session start / cold start) — COMMAND:**
```bash
python3 ~/.openclaw/workspace/artie_handoff.py read
```

**EXPECTED OUTPUT:** Last checkpoint content — read it before doing anything else.

**If no checkpoint found:** Output says "No checkpoint found. Starting cold." → run SOP 01 Soul Sync → ask Chris for today's priority.

---

**INSTALL (one-time setup — only needed once):**
```bash
cp ~/.openclaw/workspace/artie_handoff.py ~/.openclaw/workspace/artie_handoff.py
# Script is at: soul/artie/artie_handoff.py in GitHub
# Pull it with soul sync or copy manually
```

**PAT for GitHub push:** Script looks for `GITHUB_PAT` environment variable first, then `~/.openclaw/workspace/github_pat.txt`. If neither exists, checkpoint saves locally only (still useful for cold-start recovery).

---

### SOP 05 — FRESHNESS HEARTBEAT

**When to run:** Daily, via cron. Also runnable on request ("check freshness").

**INSTALL (one-time):**
```bash
bash ~/.openclaw/workspace/sync_soul.sh
```
(freshness_heartbeat.py is pulled automatically as of sync_soul.sh V6 — confirm it landed at `~/.openclaw/workspace/freshness_heartbeat.py`)

**COMMAND (Step 1 — check if cron exists):**
```bash
crontab -l | grep freshness_heartbeat
```

**EXPECTED OUTPUT if cron EXISTS:** a line running `freshness_heartbeat.py` daily.
→ Cron is fine. Skip to Step 3 to test manually.

**EXPECTED OUTPUT if cron MISSING:** blank.
→ Proceed to Step 2.

**COMMAND (Step 2 — add cron entry, runs daily at 6am):**
```bash
(crontab -l 2>/dev/null; echo "0 6 * * * cd ~/.openclaw/workspace && python3 freshness_heartbeat.py >> freshness_heartbeat.log 2>&1") | crontab -
```

**Then verify — run Step 1 again. The cron line MUST appear.**

**COMMAND (Step 3 — test manually):**
```bash
cd ~/.openclaw/workspace && python3 freshness_heartbeat.py
```

**EXPECTED OUTPUT:** one line starting `YYYY-MM-DD | artie-freshness-heartbeat | GREEN` or `| RED |`, followed by `GitHub log: updated`, exit code 0. (RED is a valid finding, not a failure — only a non-zero exit code or a Python traceback counts as failure.)

**REPORT TO DISCORD (#operations):**
```
✅ FRESHNESS HEARTBEAT — [DATE]
[paste the one summary line here]
Full detail logged to artie/ARTIE_REPORTS.md (Claude reads this — Discord is for your visibility only)
```

**IF SCRIPT FAILS (non-zero exit / traceback):** Do not attempt to fix it. Send Chris: `⚠️ freshness_heartbeat.py error — [paste exact error]. Flagged for Claude.`

**Scope note (v1, S70):** this checks Daily Sales (Pretax) and Delivery Payouts only — both reachable via the aura_thai_finance Apps Script endpoint over plain HTTP, no Google OAuth needed. Tiller and the Lavu Drive folder are deliberately NOT checked yet — those need Artie's own Drive/Sheets access (gog CLI), which hasn't been proven from Claude's side. Do not extend this script's scope without Claude reviewing it first.

---

### SOP 06 — INVOICE INTAKE WATCHER

**When to run:** Daily, via cron (once proven — see FIRST TEST RUN below). Also runnable on request ("check invoices").

**Prerequisite (confirmed working S70):** `gog auth status` for `artemisclaws@gmail.com` must show a valid grant. If any `gog` command returns `invalid_grant`, run `gog login artemisclaws@gmail.com` and re-authorize before anything else in this SOP.

**INSTALL (one-time):**
```bash
bash ~/.openclaw/workspace/sync_soul.sh
ls -la ~/.openclaw/workspace/invoice_intake_watcher.py
```

**COMMAND (Step 1 — FIRST TEST RUN, manual, required before cron):**
```bash
cd ~/.openclaw/workspace && python3 invoice_intake_watcher.py
```

**EXPECTED OUTPUT:** one line: `YYYY-MM-DD | artie-invoice-intake-watcher | GREEN | N new invoice email(s), M new Drive file(s) since first run`, then `GitHub log: updated`, exit code 0. Confirm N and M actually match what's in the inbox/folder before trusting this on a schedule — that's the whole point of a manual first run.

**IF STEP 1 FAILS with `gog ... invalid_grant`:** re-run `gog login artemisclaws@gmail.com`, then retry. Do not add to cron until Step 1 succeeds cleanly.

**COMMAND (Step 2 — add cron entry, runs daily at 7am, after the freshness heartbeat):**
```bash
(crontab -l 2>/dev/null; echo "0 7 * * * cd ~/.openclaw/workspace && python3 invoice_intake_watcher.py >> invoice_intake_watcher.log 2>&1") | crontab -
```

**Then verify:**
```bash
crontab -l | grep invoice_intake_watcher
```

**REPORT TO DISCORD (#operations):**
```
✅ INVOICE INTAKE WATCHER — [DATE]
[paste the one summary line here]
Full detail logged to artie/ARTIE_REPORTS.md
```

**IF SCRIPT FAILS (non-zero exit):** Do not attempt to fix it. Send Chris: `⚠️ invoice_intake_watcher.py error — [paste exact error]. Flagged for Claude.`

**Scope note (v2, S70):** existence/count check only — does NOT read or extract invoice data yet. That's a separate future script, built only after this one has run cleanly on cron for a while (Bedrock rule: prove one thing before layering the next).

---

## PENDING SOPs (Script not built — DO NOT RUN)

These tasks exist but Artie cannot run them yet. Claude must build the script first.  
When Chris assigns one of these, Artie replies: `🔴 [Task name] — script not built yet. Flagged for Claude.`

| SOP | Task | Script Needed | Status |
|-----|------|--------------|--------|
| P-01 | Morning startup report | `morning_report.py` | ❌ Not built |
| — | Session handoff | `artie_handoff.py` | ✅ Built — see SOP 04 |
| P-02 | Evening wrap report | `evening_wrap.py` | ❌ Not built |
| P-03 | Platform report pull (GH/DD/UE) | `platform_pull.py` | ❌ Not built |
| P-04 | Amazon Vine review draft | `vine_review.py` | ❌ Not built |
| P-05 | FB Marketplace listing draft | `listing_draft.py` | ❌ Not built |
| P-06 | Slow mover price flag | `slow_mover_check.py` | ❌ Not built |
| P-07 | EMPIRE_STATUS.md push | `empire_update.py` | ❌ Not built |
| P-08 | Trello card management | `trello_daily.py` | ❌ Not built |
| — | Invoice intake watcher | `invoice_intake_watcher.py` | ✅ gog syntax + JSON shapes confirmed S70 — see SOP 06. Needs one manual first-run confirmation before cron. |

Scripts are built one at a time, proven before the next one starts. (Bedrock Standard.)

---

## RUNBOOK GAPS LOG

When Artie hits a situation not covered by a working SOP above:

1. Do NOT improvise
2. Add a row to this table
3. Report to Discord: `🔴 Runbook gap: [task] — logged. Waiting for Claude.`

| Date | Task | What Was Unclear | What Artie Did |
|------|------|-----------------|----------------|
| [DATE] | [Task name] | [What wasn't covered] | [What Artie did instead] |

---

*This file is maintained by Claude. Artie never edits it directly.*  
*Artie adds to RUNBOOK GAPS LOG only.*  
*Push location: `soul/artie/ARTIE-RUNBOOK.md`*  
*Version history: V1 (S30, 2026-05-07) → V2 (S50, 2026-06-23)*
