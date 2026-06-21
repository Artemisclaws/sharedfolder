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

*Maintained by Claude. Flag updates to Claude at next session.*
