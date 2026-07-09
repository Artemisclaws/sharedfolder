# ARTIE RUNBOOK — Aura Thai
**Maintained by:** Claude
**Last Updated:** 2026-06-20 | Session 41

This file contains all SOPs Artie follows for Aura Thai operations.

---

## SOP 13 — Monthly Finance Update
**Trigger:** First Monday of each month, or when prompted by Chris/Claude
**Built by:** Claude | Session 35 | 2026-05-10

1. Download new month's reports from each delivery platform (GrubHub, DoorDash, UberEats)
2. Drop all files into `~/aura_thai_drop/`
3. Run: `python3 aura_thai_revenue_processor.py --input ~/aura_thai_drop --output ~/aura_thai_finance.html`
4. Copy output to `sharedfolder/dashboard/aura_thai_finance.html`
5. `git add dashboard/aura_thai_finance.html && git commit -m "Aura Thai finance update [MONTH]" && git push`
6. Confirm deploy at ops.radrooster.co/aura-thai
7. Post in Discord **#finance**: `✅ Aura Thai finance dashboard updated — [MONTH]`

---

## SOP 14 — Invoice Data Entry
**Sheet:** [aura_thai_finance](https://docs.google.com/spreadsheets/d/1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE) — Invoice Log tab
**Trigger:** Every vendor delivery (Taiwah Trading Corp or SJ Distributors LLC)
**Built by:** Claude | Session 40 | 2026-06-19

### STEP 0 — Convert Invoice Photos

Invoices arrive as iPhone HEIC photos. Convert before reading.

**Via Google Drive:** Right-click the .HEIC file → Open with > Google Docs — readable image appears.

**Via WhatsApp/Telegram:** Download usually auto-converts to JPG. If not, use https://heictojpg.com

Tips: Zoom to 100%. Columns needed: Item code | Description | Qty | U/M | Price Each | Amount. If a number is unclear, flag in Notes — do not guess.

---

### Step 1 — Open the Sheet
https://docs.google.com/spreadsheets/d/1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE → Invoice Log tab

### Step 2 — Find Next Empty Row

### Step 3 — Enter One Row Per Line Item

| Column | What to enter | Example |
|--------|--------------|---------|
| Date | Date on the invoice (not today) | 6/17/2026 |
| Invoice # | Invoice number on document | 296590 |
| Vendor | Pick from dropdown | Taiwah Trading Corp |
| Item Code | Code on left of invoice | 0009-1 |
| Item Name | Use standard names below | Basil |
| Category | Pick from dropdown | Produce |
| Qty | Qty column | 10.2 |
| Unit | Unit of measure | lb |
| Unit Price | Price Each column | 1.59 |
| Total Amount | Amount column (rightmost) | 16.22 |
| Notes | Leave blank unless unusual | |

### Step 4 — Category Guide

| Category | Items |
|----------|-------|
| Protein | Chicken, crab, mussels, tofu, any meat/seafood |
| Produce | Basil, mint, garlic, cucumber, peppers, cabbage, lime, carrot |
| Noodle / Rice | Rice noodle, pad thai noodle, wide cut noodle, long grain rice |
| Sauce / Condiment | Chili paste, soy sauce, oyster sauce, sweet chili sauce |
| Oil | Fry oil, shortening, cooking oil |
| Dairy / Egg | Eggs |
| Cleaning Supply | Dishwash, cleaning products |
| Other | Anything else |

### Step 5 — Standard Item Names (use exact spellings)

**Taiwah Trading Corp:** Basil, Mint (Hung Lui), Carrot #25, Cucumber, Eggs / Jumbo 200ct, Garlic Peeled #5, Serrano, Thai Chili Fresh, Green Cabbage #45, Lime Juice Fresh 1gal, Pineapple Chunks Sunlee, Rice Noodle (Pho) Rama #10, Pad Thai Noodle Lucky #10, Long Grain Rice AA #50, Green 1/2 Shell Mussel 2lb, Chicken & Vegetable Gyoza, Sweet Chili Sauce Maeploy, Chili Paste & Oil Pantai, Thin Soy Sauce DSB, White Pepper Whole #5, Sugar #50

**SJ Distributors LLC:** FR-Breast Chicken (Halal), Chicken Tenderloin Clipped, FR-Claw Crab Meat Signature, Firm Tofu, Mushroom Med #10, Green Bell Pepper, Bean Sprout Vita King, Cilantro, Rice Noodle WideGut, Creamy Liquid Shortening (Fry Oil)

### Step 6 — Save and Notify
Sheet saves automatically. Post in Discord **#operations**:
`✅ Invoice entered: [Vendor] INV#[number] — [X] items, $[total]`

### Step 7 — Refresh Price Tracker (after every 2-3 invoices)
In the sheet: **Aura Thai Ops > Refresh Price Tracker**

---

### Sales by Period Entry (weekly — every Friday)

1. Lavu → Reports → Sale by Item → set Monday-Sunday date range → Export
2. Sales by Period tab: add one row per dish (Period Start, Period End, Dish Name, Qty Sold, Revenue, Source: Lavu Sale by Item)
3. Post in Discord **#operations**: `✅ Sales by Period entered: week of [date] — [X] dishes`

---

### Escalation Rules
- Item does not match any category → use Other, add a note
- Vendor not in dropdown → flag to Chris immediately, do not enter
- Price more than 20% higher than last time → note in Notes, flag to Chris
- Invoice total over $1,000 → notify Chris in Discord #operations

---

## SOP 15 — Wheel Cycle Morning/Close Report
**Sheet/Source:** `investing/OPTIONS_POSITIONS_LOG.md` (GitHub, canonical — Chris/Claude update on every fill)
**Trigger:** Cron, twice daily — see schedule below. Also runnable on demand: Chris says "morning check" or "close check."
**Built by:** Claude | Session 64 | 2026-07-09

### Cron setup (one-time)
```bash
(crontab -l 2>/dev/null; echo "0 8 * * 1-5 python3 /home/artemis/.openclaw/workspace/artie_wheel_report.py morning >> /home/artemis/.openclaw/workspace/artie_wheel_report.log 2>&1") | crontab -
(crontab -l 2>/dev/null; echo "5 16 * * 1-5 python3 /home/artemis/.openclaw/workspace/artie_wheel_report.py close >> /home/artemis/.openclaw/workspace/artie_wheel_report.log 2>&1") | crontab -
```
**Verify the times land at 8:00 AM ET and 4:05 PM ET** — the numbers above assume the server runs in ET. If Artie's machine is on a different timezone, convert first (`timedatectl` to check, or just run `date` and compare to actual ET).

### What the script does (one script, one command — per the Bedrock Rule)
1. Reads `investing/OPTIONS_POSITIONS_LOG.md` from GitHub — this file is the only source of truth for open positions. If it's stale, the report is wrong; Chris/Claude own keeping it current.
2. Pulls live price per ticker (Yahoo Finance chart endpoint, Stooq CSV fallback if Yahoo fails — no new credentials needed).
3. Computes DTE, moneyness (ITM/OTM %), and cross-checks the WATCH DATES table for anything (earnings/ex-div) inside a 10-day window.
4. Posts the formatted report to Discord **#finance**.
5. Appends one line to the log's REPORT LOG section and pushes back to GitHub — running history, nothing overwritten.

### COMMAND (manual test)
```bash
python3 /home/artemis/.openclaw/workspace/artie_wheel_report.py morning
```

### EXPECTED OUTPUT
`[mode] report sent. [N] positions checked.` — and a new message appears in Discord #finance within seconds.

### IF FAILED
- Price fetch fails for a ticker → script posts anyway with `⚠️ [ticker] — price fetch failed, check manually` inline, does not block the rest of the report.
- GitHub read/write fails → send Chris: `⚠️ Wheel report failed — GitHub [read/write] error: [paste exact error]. Stopped.`
- Discord post fails → send Chris: `⚠️ Wheel report computed but Discord post failed — [paste exact error].`
- Never guess at a price or a position if the script errors. Report the failure, don't improvise a number.

### Escalation Rules
- Any position shown ITM in a close report → no action needed from Artie, this is expected wheel behavior — just visibility for Chris
- Script reports a ticker not in the Positions Log's underlying share table → flag to Claude next session, likely means the log needs an update

---



*Maintained by Claude. Flag updates to Claude at next session.*
