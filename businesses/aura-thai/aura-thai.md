# 🍜 Aura Thai
**Status:** 🟡 Active
**Last Updated:** 2026-05-10 | Session 35
**Tags:** #business #aura-thai

---

## At a Glance
| Item | Detail |
|------|--------|
| Type | Restaurant — Full service + delivery |
| Location | 4085 Atlantic Ave Ste C, Long Beach, CA |
| POS | Lavu (SOURCE OF TRUTH for all revenue) |
| Delivery Platforms | DoorDash, UberEats, GrubHub |
| Daily Revenue Goal | **$5,000/day** |
| Status | Active — Finance dashboard built, price increase monitoring underway |

---

## Active Projects

### 1. Finance Dashboard (S34–S35)
| Item | Status |
|------|--------|
| `aura_thai_revenue_processor.py` | ✅ Built — auto-detects all platform files |
| `aura_thai_finance.html` | ✅ Built — dark theme, GH data embedded (sample) |
| Real data run (Lavu as primary) | ⏳ Blocked — Lavu XLS needs conversion to Google Sheets |
| Push to ops.radrooster.co/aura-thai | ❌ Pending real data |
| ARTIE SOP 13 (Monthly Finance Update) | ❌ Draft exists in checkpoint, not yet formal |

**Artie SOP 13 (draft):**
1. Download new month's reports from each platform
2. Drop all files into `~/aura_thai_drop/`
3. `python3 aura_thai_revenue_processor.py --input ~/aura_thai_drop --output ~/aura_thai_finance.html`
4. Copy output to `sharedfolder/dashboard/aura_thai_finance.html`
5. `git add dashboard/aura_thai_finance.html && git commit -m "Aura Thai finance update [MONTH]" && git push`
6. Confirm deploy at ops.radrooster.co/aura-thai
7. Report to Chris in #finance

### 2. 20% Delivery Price Increase — Monitoring (S35)
**Went live: April 9, 2026 — DoorDash + UberEats**

**Apr 2–18 findings (DoorDash Marketplace, excl. catering):**
| Metric | Before (Apr 2–8) | After (Apr 10–18) | Change |
|--------|-----------------|-------------------|--------|
| Avg ticket | $39.99 | $45.22 | +13.1% |
| Orders/day | 14.8 | 12.4 | -16.2% |
| Revenue/day | $593 | $563 | **-5.1%** |

**GrubHub control group (no price change):** orders +11.1%, revenue +0.2%

**Verdict:** ⚠️ Neutral/slightly hurting. Prices raised 20% but ticket only up 13% (discount usage absorbing the rest). Volume dropped 16%, more than the ticket gain. Net revenue down 5% vs a market that was actually growing.

**What to watch (30-day rolling):**
- DD avg ticket — should stabilize around $45+
- DD orders/day — watch for continued erosion below 12/day
- GH orders — rising GH while DD/UE falls = customers platform-hopping on price
- UberEats — need Apr/May data (download error, retry pending)
- Discount code usage — increasing = customers resisting the increase

**Monitor cadence:** Weekly check the first Monday of each month. Pull fresh DD/GH data and compare to pre-increase baseline.

**Report file:** `outputs/dd_price_impact.html`

---

## Protocol Note (Added S35)
> **Analyze before execute.** For any strategy touching pricing, menu, marketing spend, or operations — model the scenarios first, define decision criteria, get approval, *then* move. The April 9 price increase went live without pre-analysis. We now have the data to course-correct, but this is the new standard going forward.

---

## Data Sources
| Source | Files | Status |
|--------|-------|--------|
| Lavu POS (transactions) | Jan–Apr XLS | ⚠️ XLS not readable — needs conversion to Google Sheets |
| Lavu POS (sale by item) | Jan–Apr XLS | ⚠️ Same — convert to Google Sheets |
| GrubHub | GH_Financial_Summary_Daily_Jan_-_May_8_2026.csv | ✅ Processed — 124 data points |
| DoorDash | FINANCIAL_SIMPLIFIED_TRANSACTIONS + PAYOUT_SUMMARY | ✅ In Drive |
| UberEats | Jan–Mar only | ⚠️ Apr–May download error — retry needed |
| 1099s 2025 | GrubHub 1099-K: $133,486 gross | ✅ YoY baseline |

**Drive folder:** [Aura Thai Data](https://drive.google.com/drive/folders/1b3-Q3mJsPSyb2w6MBF12XyFWbKHHVBNB)

---

## Open Items
- [ ] Convert Lavu XLS → Google Sheets (Jan–Apr, both Transactions and Sale by Item)
- [ ] Run real data through processor with Lavu as primary source
- [ ] Retry UberEats Apr–May download
- [ ] Push aura_thai_finance.html to GitHub dashboard/ → ops.radrooster.co/aura-thai
- [ ] Add aura_thai_finance.html link to ops.radrooster.co index.html
- [ ] Write ARTIE SOP 13 formally in ARTIE-RUNBOOK.md
- [ ] Monitor DD price increase weekly (first Monday each month)
- [ ] Run UberEats price impact analysis once Apr/May data is available
- [ ] O-03 — Lavu integration (blocked on Chris completing Lavu setup)
- [ ] O-04 — Shift Close integration (blocked on Chris)

---

## Systems
- [[ARTIE-RUNBOOK]] — Artie's SOPs for this business
- [[EMPIRE_STATUS]] — Live system status
- `aura_thai_revenue_processor.py` — Monthly run script
- `aura_thai_finance.html` — Finance dashboard → ops.radrooster.co/aura-thai
- `dd_price_impact.html` — DoorDash price increase analysis report

---

## Key Files (outputs/)
| File | Purpose |
|------|---------|
| `aura_thai_revenue_processor.py` | Auto-processing script — drop files, run, push |
| `aura_thai_finance.html` | Main finance dashboard |
| `dd_price_impact.html` | Price increase impact report (Apr 2–18) |
| `price_impact_analysis.py` | Script that generated dd_price_impact.html |
| `checkpoint_aura-thai-finance_2026-05-10.md` | Session 34 checkpoint |

---

[[HOME]] | [[SPRINT]] | [[EMPIRE_STATUS]]
