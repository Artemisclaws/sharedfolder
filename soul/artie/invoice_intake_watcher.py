#!/usr/bin/env python3
"""
ARTIE — INVOICE INTAKE WATCHER (v1 draft, S70)
STATUS: WRITTEN, NOT PROVEN. Do not add to cron until a manual test run
succeeds on Artie's machine. See "OPEN QUESTIONS" below -- Claude cannot
verify the Gmail/Drive OAuth pieces from this session; only Artie's own
environment can.

PURPOSE: existence/count check only (no invoice reading/extraction yet --
that's a separate future script, built only after this one is proven,
per the Bedrock rule of proving one script before layering the next).

Checks since the last run:
  1. New Gmail messages to artemisclaws+invoices@gmail.com
  2. New files in the "Invoices Dump Folder" Drive folder
     (id: 1HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza, created S70 2026-08-02)

COMMAND:        python3 invoice_intake_watcher.py
EXPECTED OUTPUT: one summary line, exit code 0 (0 new items is a valid
                 result, not a failure)
REPORT:         appends the summary line to artie/ARTIE_REPORTS.md on
                 GitHub (same mechanism as freshness_heartbeat.py --
                 that part IS proven). Also prints for Discord relay.

OPEN QUESTIONS (resolve before first test run):
  - Does this machine have google-api-python-client + google-auth
    installed? (pip show google-api-python-client)
  - Do the token files at
      /home/artemis/.openclaw/workspace/credentials/gmail_token.json
      /home/artemis/.config/google-drive-mcp/tokens.json
    match the google.oauth2.credentials.Credentials schema this script
    assumes (token, refresh_token, client_id, client_secret, scopes)?
    If they're a different shape (e.g. the "gog" CLI's own format),
    this script's load_credentials() needs rewriting to match -- do
    not guess, check the actual file structure first.
  - Does gmail_token.json have the readonly Gmail scope, and does the
    Drive token have at least drive.readonly on the target folder?
  - Alternative if the above is a dead end: check whether "gog" itself
    exposes a search/list subcommand (run `gog --help` and
    `gog gmail --help` / `gog drive --help` on Artie's machine) and
    rewrite this to shell out to gog instead of using the Python
    libraries directly. Report back to Claude either way.

FIRST TEST RUN: run manually, read the output carefully, confirm counts
look right against what's actually in the inbox/folder, THEN add to cron
(same two-step pattern as SOP 03 / SOP 05).
"""

import urllib.request
import urllib.parse
import json
import datetime
import sys
import os
import base64

GITHUB_REPO = "Artemisclaws/sharedfolder"
GITHUB_LOG_PATH = "artie/ARTIE_REPORTS.md"
STATE_FILE = os.path.expanduser("~/.openclaw/workspace/invoice_intake_state.json")

INVOICES_FOLDER_ID = "1HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza"  # Invoices Dump Folder
GMAIL_QUERY = "to:artemisclaws+invoices@gmail.com"

GMAIL_TOKEN_PATH = os.path.expanduser("/home/artemis/.openclaw/workspace/credentials/gmail_token.json")
DRIVE_TOKEN_PATH = os.path.expanduser("/home/artemis/.config/google-drive-mcp/tokens.json")


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


def count_new_gmail_messages(since_iso):
    """
    UNVERIFIED. Assumes google-api-python-client + a standard OAuth
    Credentials JSON at GMAIL_TOKEN_PATH. If gmail_token.json is a
    different shape, this will raise -- that's expected and fine, it'll
    surface as a script failure the first manual test run, which is the
    point of testing manually before cron.
    """
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    creds = Credentials.from_authorized_user_file(GMAIL_TOKEN_PATH)
    service = build("gmail", "v1", credentials=creds)

    query = GMAIL_QUERY
    if since_iso:
        since_date = datetime.date.fromisoformat(since_iso[:10])
        query += f" after:{since_date.strftime('%Y/%m/%d')}"

    resp = service.users().messages().list(userId="me", q=query, maxResults=50).execute()
    messages = resp.get("messages", [])
    return len(messages)


def count_new_drive_files(since_iso):
    """
    UNVERIFIED. Assumes google-api-python-client + a standard OAuth
    Credentials JSON at DRIVE_TOKEN_PATH.
    """
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    creds = Credentials.from_authorized_user_file(DRIVE_TOKEN_PATH)
    service = build("drive", "v3", credentials=creds)

    q = f"'{INVOICES_FOLDER_ID}' in parents and trashed = false"
    if since_iso:
        q += f" and modifiedTime > '{since_iso}'"

    resp = service.files().list(q=q, fields="files(id, name, modifiedTime)").execute()
    files = resp.get("files", [])
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
        n_emails = count_new_gmail_messages(since)
    except Exception as e:
        errors.append(f"Gmail check failed: {type(e).__name__}: {e}")

    try:
        n_files, file_names = count_new_drive_files(since)
    except Exception as e:
        errors.append(f"Drive check failed: {type(e).__name__}: {e}")

    if errors:
        line = f"{today} | artie-invoice-intake-watcher | ERROR | " + " || ".join(errors)
        print(line)
        append_github_log(line)
        sys.exit(1)

    since_label = since or "first run"
    detail = f"{n_emails} new invoice email(s), {n_files} new Drive file(s) since {since_label}"
    if file_names:
        detail += f" ({', '.join(file_names)})"

    status = "GREEN" if (n_emails or 0) + (n_files or 0) >= 0 else "GREEN"  # existence check never RED by itself
    line = f"{today} | artie-invoice-intake-watcher | {status} | {detail}"
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
