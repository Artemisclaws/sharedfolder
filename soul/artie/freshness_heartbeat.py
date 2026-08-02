#!/usr/bin/env python3
"""
ARTIE — FRESHNESS HEARTBEAT (v1, S70)
Checks aura_thai_finance freshness via the existing Apps Script Web App
endpoint. Pure HTTP -- no Google OAuth needed for this script, so it
runs on any machine with python3 + internet (proven from Claude's sandbox
2026-08-01 before being handed to Artie).

v1 SCOPE: Daily Sales (Pretax) + Delivery Payouts only.
Tiller and the old Lavu Drive folder are DEFERRED -- both would need
Artie's own Drive/Sheets OAuth (gog CLI), which is unproven from Claude's
side. Do not add those checks until gog's exact command syntax is
confirmed working on Artie's machine.

COMMAND:        python3 freshness_heartbeat.py
EXPECTED OUTPUT: one summary line printed to stdout, exit code 0
                 (exit code 0 = script ran successfully, REGARDLESS of
                 whether the finding is GREEN or RED -- RED is a valid
                 result, not a script failure)
REPORT:         appends the summary line to artie/ARTIE_REPORTS.md on
                 GitHub via the API (this is what Claude actually reads).
                 Also print the line so Artie can relay it to Discord for
                 Chris.

IF SCRIPT RAISES AN EXCEPTION (network down, endpoint down, GitHub push
fails): that IS a real failure -- exit code 1, print the error, do not
retry silently. Send Chris: "Freshness heartbeat failed -- [error]."
"""

import urllib.request
import urllib.parse
import json
import datetime
import sys
import os
import base64

ENDPOINT = "https://script.google.com/macros/s/AKfycbzpDwWXpxAfryJ6Re23HzePLOaWXTgGAkVMXLxTVArH-pzZtrzAWuKpk5KcWzSavdNLHQ/exec"
SECRET = "1-10"
GITHUB_REPO = "Artemisclaws/sharedfolder"
GITHUB_LOG_PATH = "artie/ARTIE_REPORTS.md"
DAILY_SALES_BUDGET_DAYS = 7


def call_endpoint(payload):
    enc = urllib.parse.quote(json.dumps(payload))
    url = f"{ENDPOINT}?payload={enc}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode())


def get_github_pat():
    env = os.environ.get("GITHUB_PAT")
    if env:
        return env
    path = os.path.expanduser("~/.pinyo_github_pat")
    if os.path.exists(path):
        return open(path).read().strip()
    return None


def check_daily_sales():
    resp = call_endpoint({
        "action": "readRange", "secret": SECRET,
        "sheet": "Daily Sales (Pretax)", "range": "A1:A200"
    })
    values = [row[0] for row in resp["result"]["values"] if row and row[0]]
    dates = []
    for v in values:
        try:
            d = datetime.datetime.fromisoformat(str(v).replace("Z", "+00:00")).date()
            dates.append(d)
        except (ValueError, TypeError):
            continue
    if not dates:
        return {"ok": False, "error": "no parseable dates found"}
    newest = max(dates)
    age = (datetime.date.today() - newest).days
    return {
        "ok": age <= DAILY_SALES_BUDGET_DAYS,
        "newest": str(newest),
        "age_days": age,
        "budget_days": DAILY_SALES_BUDGET_DAYS,
    }


def check_delivery_payouts():
    resp = call_endpoint({
        "action": "readRange", "secret": SECRET,
        "sheet": "Delivery Payouts", "range": "A1:J20"
    })
    rows = resp["result"]["values"]
    pending = []
    for row in rows[1:]:
        if any(str(c).strip().upper() == "PENDING" for c in row):
            label = row[0] if row and row[0] else "unlabeled row"
            pending.append(str(label))
    return {"ok": len(pending) == 0, "pending_rows": pending}


def append_github_log(line):
    pat = get_github_pat()
    if not pat:
        print("WARNING: no GitHub PAT found (checked $GITHUB_PAT and ~/.pinyo_github_pat) -- skipping log push")
        return False

    api = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_LOG_PATH}"

    meta_req = urllib.request.Request(api, headers={"Authorization": f"token {pat}"})
    with urllib.request.urlopen(meta_req, timeout=30) as r:
        meta = json.loads(r.read().decode())
    sha = meta["sha"]

    content_req = urllib.request.Request(api, headers={
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3.raw",
    })
    with urllib.request.urlopen(content_req, timeout=30) as r:
        current = r.read().decode()

    marker = "---\n"
    idx = current.find(marker)
    insert_at = idx + len(marker) if idx != -1 else len(current)
    new_content = current[:insert_at] + "\n" + line + current[insert_at:]

    body = json.dumps({
        "message": "Artie: freshness heartbeat",
        "content": base64.b64encode(new_content.encode("utf-8")).decode("ascii"),
        "sha": sha,
    }).encode("utf-8")

    put_req = urllib.request.Request(api, data=body, method="PUT", headers={
        "Authorization": f"token {pat}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(put_req, timeout=30) as r:
        result = json.loads(r.read().decode())

    return bool(result.get("commit", {}).get("sha"))


def main():
    today = datetime.date.today().isoformat()

    ds = check_daily_sales()
    dp = check_delivery_payouts()

    status = "GREEN" if ds.get("ok") and dp.get("ok") else "RED"

    if ds.get("ok"):
        ds_part = f"Daily Sales current to {ds['newest']} ({ds['age_days']}d, budget {ds['budget_days']}d)"
    elif "error" in ds:
        ds_part = f"Daily Sales CHECK FAILED -- {ds['error']}"
    else:
        ds_part = f"Daily Sales STALE -- newest {ds['newest']} ({ds['age_days']}d, budget {ds['budget_days']}d)"

    if dp.get("ok"):
        dp_part = "Delivery Payouts: no PENDING rows"
    else:
        dp_part = f"Delivery Payouts: PENDING -- {', '.join(dp['pending_rows'])}"

    line = f"{today} | artie-freshness-heartbeat | {status} | {ds_part} | {dp_part}"
    print(line)

    pushed = append_github_log(line)
    print("GitHub log: " + ("updated" if pushed else "SKIPPED/FAILED -- check GITHUB_PAT"))


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")
        sys.exit(1)
