# SESSION_HISTORY.md
**GitHub:** `session-history/SESSION_HISTORY.md`

---

## Session 43 — 2026-06-20

**Theme:** Aura Thai — Invoice system stabilization, ARTIE-RUNBOOK created, Artie cleared to run

**Completed:**
- Fixed resetDishMap() timeout (3 iterations): removed sheet.clear(), switched to batch color calls, cleared data validation explicitly, tightened dropdown ranges from :200 to :35
- Dish Map now fully populated — all 31 ingredients loaded (21 Taiwah + 10 SJ)
- Created artie-config/ARTIE-RUNBOOK.md on GitHub — SOP 13 (Monthly Finance) + SOP 14 (Invoice Entry)
- Live-tested Invoice Log SOP via Chrome: entered full test row (6/17/2026 | INV#296590 | Taiwah | 0009-1 | Basil | Produce | 10.2 lb | $1.59 | $16.22), verified all fields saved correctly, deleted test row
- Artie cleared to begin data entry: Invoice Log (backlog invoices) + Sales by Period (weekly Lavu)

**Files created/updated:**
- artie-config/ARTIE-RUNBOOK.md — NEW on GitHub (SOP 13 + SOP 14)
- /Users/macbook/Downloads/aura_thai_invoice_system.gs — updated (resetDishMap fix)
- /Users/macbook/Downloads/ARTIE_SOP_invoice_entry.md — source SOP (local)

**Key decisions:**
- sheet.clear() is slow on formatted sheets — never use it again; target specific ranges instead
- Dropdowns scoped to tight ranges (B2:B35 vs B2:B200) for performance
- ARTIE-RUNBOOK.md lives in artie-config/ on GitHub (Artie finds it himself)
- SOP tested end-to-end before Artie cleared — this is the standard going forward

**Blockers remaining:**
- Chris still needs to fill Dish Map column D (Used In Dishes) — unlocks COGS by Dish
- No invoice data yet — COGS analysis cannot run until Artie enters first batch

**Next session starts with:** Load soul files. Check if Artie has entered any invoices (Invoice Log). If data exists for same period in Invoice Log + Sales by Period → run first COGS analysis. If not → fill Dish Map column D or debug with Artie.

---

## Session 42 — 2026-06-10

**Theme:** Aura Thai — ezCater platform onboarding

**Completed:**
- Researched ezCater platform mechanics (15% commission + 2.99% processing, Fixed-rate recommended fee type)
- Live-scraped 7+ Long Beach Asian/Thai competitors on ezcater: WaBa Grill, moonbowls, Rascals Teriyaki, Super Mex, Thai Barbeque, Pick Up Stix
- Key finding: All Reliability Rockstar Asian performers use $30 & up / $100 minimum. Thai-specific competitors with low fees ($10, $11.25) have 2-46 reviews, no Rockstar badge.
- Locked fee strategy: Fixed-rate, 4 zones. Do NOT carry over small-order DD/UE/GH tiers — ezcater is B2B corporate catering only.
- Chris set final Zone 4: $60 fee / $350 minimum (personal delivery option for far orders)
- Built and delivered ezcater_quickref.docx — 4-section Word doc: Delivery Fee Tiers, Competitor Benchmark, Platform Settings, Winning Strategy

**Files created:**
- outputs/ezcater_quickref.docx — quick-reference onboarding doc (4085 Atlantic Ave, Long Beach CA)
- outputs/context_business.md — business context file for continuity

**Key decisions:**
- ezcater = strictly catering platform, not DD/UE/GH equivalent. Minimum $100, no small orders.
- Reliability Rockstar badge is the #1 visibility driver — accept all orders, 100% on-time.
- Do not compete with Thai Barbeque ($10 fee, 2 reviews in 6 years). Follow the Rockstar winners.

**Final fee table:**
| Zone 1 | 0-5mi | $30 | $100 |
| Zone 2 | 6-10mi | $40 | $150 |
| Zone 3 | 11-15mi | $50 | $250 |
| Zone 4 | 16-20mi | $60 | $350 |

**Next session starts with:** Load soul files. A-09 COGS tracking — this is still TOP priority. ezCater onboarding is in Chris's hands (completing paperwork using quick-ref doc).
