"""
artie_wheel_report.py — Wheel Cycle Morning/Close Reporter
Session S64 | Author: Claude (Pinyo Empire Strategist)

Follows the same proven pattern as artie_report_sync.py (3PD report) and
invoice_processor.py: pull source data, compute, post to Discord — one
script, one command, per the Bedrock Rule (ARTIE-RUNBOOK.md).

Reads:
  - investing/OPTIONS_POSITIONS_LOG.md (GitHub) — source of truth for open positions
Fetches:
  - Live price per ticker (Yahoo Finance chart API, no key required; falls
    back to Stooq CSV if Yahoo fails — same fallback-chain pattern as the
    LLM model chain in models.json)
Posts:
  - Formatted report to Discord #finance (channel ID 1501467891474759770)
Writes back:
  - Appends one line to the REPORT LOG section of OPTIONS_POSITIONS_LOG.md
    and pushes to GitHub, so there's a running history of every check.

Run modes: python3 artie_wheel_report.py morning
           python3 artie_wheel_report.py close
"""

import os
import re
import sys
import base64
import requests
from datetime import datetime, date

# ─── CONFIG ──────────────────────────────────────────────────────────────────

GITHUB_PAT = os.environ.get("GITHUB_PAT")  # Artie already has this — see REGISTRY
REPO = "Artemisclaws/sharedfolder"
LOG_PATH = "investing/OPTIONS_POSITIONS_LOG.md"
GITHUB_API = f"https://api.github.com/repos/{REPO}/contents/{LOG_PATH}"

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")  # already in Artie's env
FINANCE_CHANNEL_ID = "1501467891474759770"

WATCH_WINDOW_DAYS = 10  # flag earnings/ex-div within this many days

# ─── GITHUB: READ + WRITE THE LOG ────────────────────────────────────────────

def fetch_log():
    r = requests.get(GITHUB_API, headers={"Authorization": f"token {GITHUB_PAT}"})
    r.raise_for_status()
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content, data["sha"]

def push_log(new_content, sha, message):
    b64 = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")
    r = requests.put(
        GITHUB_API,
        headers={"Authorization": f"token {GITHUB_PAT}"},
        json={"message": message, "content": b64, "sha": sha},
    )
    r.raise_for_status()

def parse_positions(md_text):
    """Pull rows out of the OPEN POSITIONS markdown table."""
    positions = []
    in_table = False
    for line in md_text.splitlines():
        if line.startswith("| Ticker | Type | Side"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            if "---" in line:
                continue
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) < 8 or cols[6] == "PENDING ENTRY":
                continue  # skip unfilled placeholder rows
            positions.append({
                "ticker": cols[0], "type": cols[1], "side": cols[2],
                "contracts": cols[3], "strike": float(cols[4].replace("$", "")),
                "expiration": cols[5], "opened": cols[6], "premium": cols[7],
            })
    return positions

def parse_watch_dates(md_text):
    """Pull rows out of the WATCH DATES table."""
    watches = []
    in_table = False
    for line in md_text.splitlines():
        if line.startswith("| Event | Ticker | Date"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            if "---" in line:
                continue
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) < 4:
                continue
            watches.append({"event": cols[0], "ticker": cols[1], "date": cols[2], "note": cols[3]})
    return watches

# ─── PRICE FETCH (Yahoo primary, Stooq fallback) ─────────────────────────────

def get_price(ticker):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        result = r.json()["chart"]["result"][0]
        return float(result["meta"]["regularMarketPrice"])
    except Exception:
        pass
    try:
        url = f"https://stooq.com/q/l/?s={ticker.lower()}.us&f=sd2t2ohlcv&h&e=csv"
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        line = r.text.strip().splitlines()[1]
        close = line.split(",")[6]
        return float(close)
    except Exception:
        return None

# ─── REPORT BUILD ─────────────────────────────────────────────────────────────

def days_to(expiration_str):
    exp = datetime.strptime(expiration_str, "%Y-%m-%d").date()
    return (exp - date.today()).days

def build_report(mode, positions, watches):
    header = "☀️ **Wheel Cycle — Morning Check**" if mode == "morning" else "🌙 **Wheel Cycle — Close Check**"
    lines = [header, ""]

    prices = {}
    for p in positions:
        if p["ticker"] not in prices:
            prices[p["ticker"]] = get_price(p["ticker"])

    for p in positions:
        px = prices.get(p["ticker"])
        if px is None:
            lines.append(f"⚠️ {p['ticker']} — price fetch failed, check manually")
            continue
        dte = days_to(p["expiration"])
        pct = (px - p["strike"]) / p["strike"] * 100
        moneyness = "ITM" if (p["side"] == "SELL" and (
            (p["type"] == "CALL" and px > p["strike"]) or
            (p["type"] == "PUT" and px < p["strike"])
        )) else "OTM"
        flag = "⚠️ Watch — near/in the money" if moneyness == "ITM" or abs(pct) < 1 else "✅"
        lines.append(
            f"{p['ticker']} {p['type']} ${p['strike']:.2f} x{p['contracts']} — "
            f"px ${px:.2f} ({pct:+.1f}% vs strike), {dte} DTE, {moneyness}. {flag}"
        )

    upcoming = [w for w in watches if 0 <= days_to(w["date"].split(" to ")[0].split(" (")[0]) <= WATCH_WINDOW_DAYS] \
        if watches else []
    if upcoming:
        lines.append("")
        for w in upcoming:
            lines.append(f"⚠️ {w['event']} — {w['ticker']} in {days_to(w['date'].split(' to ')[0].split(' (')[0])}d")

    lines.append("")
    lines.append(f"_Checked {datetime.now().strftime('%Y-%m-%d %H:%M')} — full log: investing/OPTIONS_POSITIONS_LOG.md_")
    return "\n".join(lines)

# ─── DISCORD POST ─────────────────────────────────────────────────────────────

def post_to_discord(message):
    url = f"https://discord.com/api/v10/channels/{FINANCE_CHANNEL_ID}/messages"
    r = requests.post(url, headers={"Authorization": f"Bot {DISCORD_BOT_TOKEN}"}, json={"content": message})
    r.raise_for_status()

# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "morning"
    content, sha = fetch_log()
    positions = parse_positions(content)
    watches = parse_watch_dates(content)
    report = build_report(mode, positions, watches)
    post_to_discord(report)

    log_line = f"\n- {datetime.now().strftime('%Y-%m-%d %H:%M')} ({mode}): posted to #finance"
    new_content = content.replace(
        "*(empty — first entry lands once Phase 3 automation goes live, or once Chris/Claude runs the first manual report)*",
        log_line.strip()
    ) if "*(empty" in content else content + log_line
    push_log(new_content, sha, f"Artie: {mode} wheel report — {date.today().isoformat()}")

    print(f"{mode} report sent. {len(positions)} positions checked.")

if __name__ == "__main__":
    main()
