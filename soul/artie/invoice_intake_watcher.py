#!/usr/bin/env python3
"""
ARTIE — INVOICE INTAKE WATCHER (v2, S70)
STATUS: gog syntax + JSON shapes CONFIRMED on Artie's machine (2026-08-01).
Auth was re-authorized same session (old refresh token had gone invalid_grant).
Still needs ONE manual test run before cron -- see FIRST TEST RUN below.

PURPOSE: existence/count check only (no invoice reading/extraction --
that's a separate future script, built only after this one is proven).

Uses the `gog` CLI (not raw Python OAuth libraries -- v1 draft assumed
that and was wrong; gog is the actual mechanism on this machine).

Checks since the last run:
  1. New Gmail threads to artemisclaws+invoices@gmail.com
     -> gog gmail search "..." -a artemisclaws@gmail.com -j --max 50
     -> JSON shape confirmed: {"nextPageToken": "", "threads": [...]}
  2. New files in the "Invoices Dump Folder" Drive folder
     (id: 1HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza)
     -> gog drive ls --parent <id> -a artemisclaws@gmail.com -j
     -> JSON shape confirmed: {"files": [{"id","mimeType","modifiedTime",
        "name","parents","webViewLink"}], "nextPageToken": ""}
     -> Archive subfolder itself will always appear in this list -- it's
        excluded by name below so it doesn't get counted as "a new invoice."

COMMAND:        python3 invoice_intake_watcher.py
EXPECTED OUTPUT: one summary line, exit code 0 (0 new items is a valid
                 result, not a failure)
REPORT:         appends the summary line to artie/ARTIE_REPORTS.md on
                 GitHub. Also prints for Discord relay.

FIRST TEST RUN: run manually, confirm the counts match what's actually in
the inbox/folder, THEN add to cron (same two-step pattern as SOP 03/05).
Suggested cron once proven: daily, e.g. "0 7 * * *" (after the 6am
freshness heartbeat).
"""

import subprocess
import json
import urllib.request
import datetime
import sys
import os
import base64

GITHUB_REPO = "Artemisclaws/sharedfolder"
GITHUB_LOG_PATH = "artie/ARTIE_REPORTS.md"
STATE_FILE = os.path.expanduser("~/.openclaw/workspace/invoice_intake_state.json")

ACCOUNT = "artemisclaws@gmail.com"
INVOICES_FOLDER_ID = "1HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza"  # Invoices Dump Folder
ARCHIVE_SUBFOLDER_NAME = "Archive"
GMAIL_QUERY_BASE = "to:artemisclaws+invoices@gmail.com"


def run_gog(args):
    """Run a gog command, return parsed JSON. Raises on non-zero exit."""
    cmd = ["gog"] + args + ["-a", ACCOUNT, "-j"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(f"gog {' '.join(args)} failed (exit {result.returncode}): {result.stderr.strip()}")
    return json.loads(result.stdout)


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"last_run": None}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)


def get_github_pat():
    env = os.environ.get("GITHUB_PAT")
    if env:
        return env
    path = os.path.expanduser("~/.pinyo_github_pat")
    if os.path.exists(path):
        return open(path).read().strip()
    return None


def append_github_log(line):
    pat = get_github_pat()
    if not pat:
        print("WARNING: no GitHub PAT found -- skipping log push")
        return False
    api = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_LOG_PATH}"
    meta_req = urllib.request.Request(api, headers={"Authorization": f"token {pat}"})
    with urllib.request.urlopen(meta_req, timeout=30) as r:
        meta = json.loads(r.read().decode())
    sha = meta["sha"]
    content_req = urllib.request.Request(api, headers={
        "Authorization": f"token {pat}", "Accept": "application/vnd.github.v3.raw"})
    with urllib.request.urlopen(content_req, timeout=30) as r:
        current = r.read().decode()
    marker = "---\n"
    idx = current.find(marker)
    insert_at = idx + len(marker) if idx != -1 else len(current)
    new_content = current[:insert_at] + "\n" + line + current[insert_at:]
    body = json.dumps({
        "message": "Artie: invoice intake watcher",
        "content": base64.b64encode(new_content.encode("utf-8")).decode("ascii"),
        "sha": sha,
    }).encode("utf-8")
    put_req = urllib.request.Request(api, data=body, method="PUT", headers={
        "Authorization": f"token {pat}", "Content-Type": "application/json"})
    with urllib.request.urlopen(put_req, timeout=30) as r:
        result = json.loads(r.read().decode())
    return bool(result.get("commit", {}).get("sha"))


def count_new_gmail_threads(since_iso):
    query = GMAIL_QUERY_BASE
    if since_iso:
        since_date = datetime.date.fromisoformat(since_iso[:10])
        query += f" after:{since_date.strftime('%Y/%m/%d')}"
    data = run_gog(["gmail", "search", query, "--max", "50"])
    threads = data.get("threads", [])
    return len(threads)


def count_new_drive_files(since_iso):
    args = ["drive", "ls", "--parent", INVOICES_FOLDER_ID]
    if since_iso:
        args += ["--query", f"modifiedTime > '{since_iso}'"]
    data = run_gog(args)
    files = data.get("files", [])
    files = [f for f in files if f.get("name") != ARCHIVE_SUBFOLDER_NAME]
    return len(files), [f["name"] for f in files]


def main():
    state = load_state()
    since = state.get("last_run")
    today = datetime.date.today().isoformat()
    now_iso = datetime.datetime.utcnow().isoformat() + "Z"

    errors = []
    n_emails = None
    n_files = None
    file_names = []

    try:
        n_emails = count_new_gmail_threads(since)
    except Exception as e:
        errors.append(f"Gmail check failed: {e}")

    try:
        n_files, file_names = count_new_drive_files(since)
    except Exception as e:
        errors.append(f"Drive check failed: {e}")

    if errors:
        line = f"{today} | artie-invoice-intake-watcher | ERROR | " + " || ".join(errors)
        print(line)
        append_github_log(line)
        sys.exit(1)

    since_label = since or "first run"
    detail = f"{n_emails} new invoice email(s), {n_files} new Drive file(s) since {since_label}"
    if file_names:
        detail += f" ({', '.join(file_names)})"

    line = f"{today} | artie-invoice-intake-watcher | GREEN | {detail}"
    print(line)

    pushed = append_github_log(line)
    print("GitHub log: " + ("updated" if pushed else "SKIPPED/FAILED"))

    state["last_run"] = now_iso
    save_state(state)


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")
        sys.exit(1)
