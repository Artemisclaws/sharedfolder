# AURA THAI — COST BASELINE
**Source:** Chris, ground truth, Session S58 (2026-07-02 payday)
**Status:** LIVE reference — payroll is "very similar every paycheck." Do not ask Chris to re-dictate this.
**GitHub:** `aura-thai/COST_BASELINE.md`

---

## FIXED COSTS — MONTHLY

| Item | Amount | Notes |
|------|--------|-------|
| Restaurant rent | $7,735.00 | |
| Extra CAM | $1,360.00 | |
| SBA EIDL payment | $436.00 | $350K @ 3%/30yr, mom guaranteed |
| Sang rent incentive (net) | $590.00 | Total $1,640; Sang reimburses $1,050 |
| Chefs' apartment (net) | ~$2.00 | $1,850 rent − $616 deducted from Miguel, Rambo, Eliseo (⚠️ assumed $616 EACH, monthly: 3 × $616 = $1,848 ≈ full offset. CONFIRM.) |
| Natural gas | $535.26 – $650 | midpoint $592.63 |
| Electricity | $1,500 – $1,700 | midpoint $1,600 |
| **SUBTOTAL (midpoints)** | **~$12,316/mo** | |

**NOT YET CAPTURED:** water, trash, insurance, internet/phone, Lavu/POS fees, card processing (~2.5–3% of card sales — material), repairs/maintenance, smallwares/supplies, licenses/permits. Break-even is understated until these are in.

---

## PAYROLL — BI-WEEKLY (26 periods/yr; monthly = period × 2.1667)

### BOH — flat day-rate, take-home guaranteed (partial hours through payroll, balance paid in cash)

| Name | Role | Rate | Days/period | Take-home | Reported gross | Net check | Cash |
|------|------|------|-------------|-----------|----------------|-----------|------|
| Miguel | Head Chef | $175/day, 6d/wk | 12 | $2,100.00 | $669.00 (33.45h) | $609.12 | $1,490.88 ⚠️ |
| Sang | 2nd Head Chef | $155/day, 6d/wk | 12 | $1,860.00 | $613.98 (36.33h) | $526.48 | $1,333.52 ✓ |
| Eliseo | Chef | $130/day, 5d/wk | 10 | $1,300.00 | $693.88 (36.52h) | $631.78 | $688.00 ⚠️ |
| Rambo | Dishwasher | $125/day, 5d/wk | 10 | $1,250.00 | — (all cash) | — | $1,250.00 |
| Mee Ann | Eggroll maker | $110/week | — | $220.00 | — (cash, confirm) | — | $220.00 |

⚠️ Miguel: Chris stated cash $1,511.28; net check + guaranteed take-home implies $1,490.88 ($20.40 gap). CONFIRM.
⚠️ Eliseo: net $631.78 + cash $688 = $1,319.78 vs $1,300 implied by 10 × $130 ($19.78 gap). CONFIRM.

**BOH take-home subtotal: $6,749.78/period** (using stated Eliseo components)

### FOH / W-2 — hourly, per this payday

| Name | Role | Hours | Gross | Net |
|------|------|-------|-------|-----|
| Vanly (Ly) | Manager | 60.10 | $1,202.00 | $1,003.72 |
| Nopphawan (Dream) | Waitress | 58.54 | $989.33 | $851.52 |
| Pichai | Delivery | 64.00 | $1,081.60 | $884.88 |
| Pornthip (PT) | Waitress | 32.50 | $549.25 | $500.10 |
| Sutatip (Jiew) | Waitress | 16.43 | $277.67 | $252.81 |
| Suriya | Delivery | 16.00 | $270.40 | $246.20 |
| Vutthikorn (Chris) | Manager | salary | $3,000.00 | $2,453.58 |

**FOH gross subtotal: $7,370.25/period.** Chris sometimes doesn't deposit his own check when cash is short — it is still modeled as a real cost (accrued liability, not savings).

---

## TAX ABSORPTION — FLAT-RATE CHEFS (Chris's question, answered)

Because the day rate is guaranteed take-home, the restaurant absorbs the employee-side withholding on reported wages, plus normal employer payroll taxes.

| Chef | Withholding absorbed /period | Employer FICA (7.65%) /period | Total /period | ~Monthly | ~Annual |
|------|------------------------------|-------------------------------|---------------|----------|---------|
| Miguel | $59.88 | $51.18 | $111.06 | $240.63 | $2,887.56 |
| Sang | $87.50 | $46.97 | $134.47 | $291.35 | $3,496.22 |
| Eliseo | $62.10 | $53.08 | $115.18 | $249.56 | $2,994.68 |
| **Total** | **$209.48** | **$151.23** | **$360.71** | **$781.54** | **~$9,378** |

Excludes CA SUI, ETT, FUTA (need rates from payroll provider — small, annual wage caps apply). Employer FICA on FOH gross adds $563.82/period.

### Effective hourly rate — pending actual shift hours
True $/hr = day rate ÷ actual hours worked per day (NOT reported hours). Scenarios:

| Chef | 8 hr/day | 10 hr/day | 12 hr/day |
|------|----------|-----------|-----------|
| Miguel ($175) | $21.88 | $17.50 | $14.58 |
| Sang ($155) | $19.38 | $15.50 | $12.92 |
| Eliseo ($130) | $16.25 | $13.00 | $10.83 |
| Rambo ($125) | $15.63 | $12.50 | $10.42 |

**OPEN:** Chris to supply actual hours/day per chef for the real number. Note for INV-15 preparer meeting: several scenarios fall below CA minimum wage on an hourly basis — worth a quiet question to the tax preparer alongside the existing 8.

---

## MONTHLY LABOR ROLLUP

| Block | /period | /month |
|-------|---------|--------|
| BOH take-home | $6,749.78 | $14,624.52 |
| Withholding absorbed (chefs) | $209.48 | $453.87 |
| Employer FICA (all reported) | $715.05 | $1,549.28 |
| FOH gross | $7,370.25 | $15,968.88 |
| **TOTAL LABOR** | **$15,044.56** | **~$32,597** |

Excluding Chris's pay ($3,229.50/period incl. FICA): ~$25,600/mo.
Prior EMPIRE_STATUS BOH table (S39) is superseded by this doc: Erick off roster, Rambo now 5d/wk, Mee Ann + FOH added.

---

## KNOWN-COST BREAK-EVEN — PREVIEW (SCENARIO ONLY, NOT FINAL)

Known monthly base = fixed ~$12,316 + labor ~$32,597 = **~$44,912/mo** before COGS and before missing fixed items.

Break-even revenue = $44,912 ÷ (1 − COGS%):

| COGS | Monthly break-even | Daily (÷30.4) |
|------|--------------------|----------------|
| 25% | $59,883 | $1,970 |
| 30% | $64,160 | $2,110 |
| 35% | $69,096 | $2,273 |

May 2026 actual: ~$2,200/day. At 30% COGS the restaurant is roughly at break-even; at 35% it is underwater — **before** water/insurance/card fees are added. This is why path-to-black is Priority #1. Final number pends: real COGS, missing fixed costs, 2026 Lavu daily data.

---

## OPEN CONFIRMATIONS (Chris)
1. Chefs' apartment: $616 deducted from EACH of Miguel/Rambo/Eliseo, monthly? (assumed)
2. Miguel cash $1,511.28 vs computed $1,490.88
3. Eliseo total $1,319.78 vs $1,300 implied
4. Mee Ann paid cash? Any reporting?
5. Actual hours/day per chef (for true hourly rate)
6. COGS estimate ($/mo purchases or %)
7. Where does 2026 Lavu daily data live? (Sheet read returned 2025 only, Jan–Aug)
8. Missing fixed items: water, trash, insurance, internet, POS fees, card processing rate
