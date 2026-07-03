/**
 * AURA THAI — COST BASELINE TAB BUILDER — v1 (S58, 2026-07-02)
 * Creates a "Cost Baseline" tab in aura_thai_finance with all fixed costs,
 * payroll, tax absorption, and a live break-even calculator.
 *
 * SAFETY:
 *  - Only creates a NEW tab. Never touches any existing tab.
 *  - If "Cost Baseline" already exists, it stops (protects your edits).
 *    To rebuild from scratch: delete the tab manually, run again.
 *  - Non-blocking toasts only. No popups. (V2 pattern)
 *
 * DEPLOY: Extensions > Apps Script > + File > paste this > Run buildCostBaseline
 * Optional: add to your 🍜 menu in onOpen():
 *   .addItem('Build Cost Baseline tab', 'buildCostBaseline')
 */

function buildCostBaseline() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (ss.getSheetByName('Cost Baseline')) {
    ss.toast('Cost Baseline tab already exists — delete it manually first if you want a rebuild.', '🍜 Skipped', 8);
    return;
  }
  var sh = ss.insertSheet('Cost Baseline');
  ss.toast('Building Cost Baseline tab…', '🍜 Working', 5);

  var YELLOW = '#fff2cc'; // = fill me / editable
  var GREY   = '#efefef';

  function header(row, text) {
    sh.getRange(row, 1).setValue(text).setFontWeight('bold').setFontSize(11);
    sh.getRange(row, 1, 1, 10).setBackground(GREY);
  }

  // ── Title ──────────────────────────────────────────────
  sh.getRange('A1').setValue('AURA THAI — COST BASELINE (ground truth S58, 2026-07-02 payday)')
    .setFontWeight('bold').setFontSize(13);

  // ── FIXED COSTS ────────────────────────────────────────
  header(3, 'FIXED COSTS — MONTHLY');
  sh.getRange(4, 1, 1, 3).setValues([['Item', 'Amount', 'Notes']]).setFontWeight('bold');
  var fixed = [
    ['Restaurant rent', 7735, ''],
    ['Extra CAM', 1360, ''],
    ['SBA EIDL payment', 436, '$350K @3%/30yr'],
    ['Sang rent incentive (net)', 590, 'Total $1,640; Sang reimburses $1,050'],
    ['Chefs\' apartment (net)', 2, '$1,850 − $616 × 3 deducted from Miguel/Rambo/Eliseo — CONFIRM $616 each, monthly'],
    ['Natural gas', 592.63, 'Range $535.26–$650 — midpoint'],
    ['Electricity', 1600, 'Range $1,500–$1,700 — midpoint'],
    ['Water', 0, 'FILL IN'],
    ['Trash', 0, 'FILL IN'],
    ['Insurance', 0, 'FILL IN'],
    ['Internet / phone', 0, 'FILL IN'],
    ['Lavu / POS fees', 0, 'FILL IN'],
    ['Card processing', 0, 'FILL IN — ~2.5–3% of card sales, material'],
    ['Repairs / maintenance', 0, 'FILL IN'],
    ['Supplies / smallwares', 0, 'FILL IN']
  ];
  sh.getRange(5, 1, fixed.length, 3).setValues(fixed);
  sh.getRange(12, 2, 8, 1).setBackground(YELLOW); // rows 12–19 = FILL IN
  sh.getRange(20, 1).setValue('FIXED SUBTOTAL').setFontWeight('bold');
  sh.getRange(20, 2).setFormula('=SUM(B5:B19)').setFontWeight('bold');

  // ── BOH PAYROLL ────────────────────────────────────────
  header(22, 'BOH PAYROLL — BI-WEEKLY (flat day rate = guaranteed take-home; balance paid cash)');
  sh.getRange(23, 1, 1, 10).setValues([[
    'Name', 'Role', 'Day rate', 'Days/period', 'Take-home', 'Reported gross',
    'Net check', 'Cash paid', 'Tax absorbed/period', 'Notes'
  ]]).setFontWeight('bold');
  // E = C*D | H = E-G | I = (F-G) + F*7.65%
  var boh = [
    ['Miguel', 'Head Chef', 175, 12, '=C24*D24', 669.00, 609.12, '=E24-G24', '=(F24-G24)+F24*0.0765', 'Chris stated cash $1,511.28 vs computed — CONFIRM $20.40 gap'],
    ['Sang', '2nd Head Chef', 155, 12, '=C25*D25', 613.98, 526.48, '=E25-G25', '=(F25-G25)+F25*0.0765', 'Rent incentive handled in fixed costs'],
    ['Eliseo', 'Chef', 130, 10, '=C26*D26', 693.88, 631.78, '=E26-G26', '=(F26-G26)+F26*0.0765', 'Actual cash paid $688 → total $1,319.78 vs $1,300 — CONFIRM'],
    ['Rambo', 'Dishwasher', 125, 10, '=C27*D27', 0, 0, '=E27-G27', 0, 'All cash, no reporting'],
    ['Mee Ann', 'Eggroll maker', 110, 2, '=C28*D28', 0, 0, '=E28-G28', 0, '$110/WEEK (rate=weekly, period=2) — cash, CONFIRM']
  ];
  sh.getRange(24, 1, boh.length, 10).setValues(boh);
  sh.getRange(29, 1).setValue('BOH SUBTOTAL').setFontWeight('bold');
  sh.getRange(29, 5).setFormula('=SUM(E24:E28)').setFontWeight('bold');
  sh.getRange(29, 9).setFormula('=SUM(I24:I28)').setFontWeight('bold');

  // ── FOH PAYROLL ────────────────────────────────────────
  header(31, 'FOH PAYROLL — BI-WEEKLY (W-2, per 2026-07-02 payday)');
  sh.getRange(32, 1, 1, 6).setValues([['Name', 'Role', 'Hours', 'Gross', 'Net', 'Employer FICA (7.65%)']]).setFontWeight('bold');
  var foh = [
    ['Vanly (Ly)', 'Manager', 60.10, 1202.00, 1003.72, '=D33*0.0765'],
    ['Nopphawan (Dream)', 'Waitress', 58.54, 989.33, 851.52, '=D34*0.0765'],
    ['Pichai', 'Delivery', 64.00, 1081.60, 884.88, '=D35*0.0765'],
    ['Pornthip (PT)', 'Waitress', 32.50, 549.25, 500.10, '=D36*0.0765'],
    ['Sutatip (Jiew)', 'Waitress', 16.43, 277.67, 252.81, '=D37*0.0765'],
    ['Suriya', 'Delivery', 16.00, 270.40, 246.20, '=D38*0.0765'],
    ['Vutthikorn (Chris)', 'Manager — salary', '', 3000.00, 2453.58, '=D39*0.0765']
  ];
  sh.getRange(33, 1, foh.length, 6).setValues(foh);
  sh.getRange(39, 10).setValue('Sometimes undeposited when cash short — still a real cost (accrued)');
  sh.getRange(40, 1).setValue('FOH SUBTOTAL').setFontWeight('bold');
  sh.getRange(40, 4).setFormula('=SUM(D33:D39)').setFontWeight('bold');
  sh.getRange(40, 6).setFormula('=SUM(F33:F39)').setFontWeight('bold');

  // Employer FICA on BOH reported gross
  sh.getRange(41, 1).setValue('Employer FICA on BOH reported gross');
  sh.getRange(41, 6).setFormula('=SUM(F24:F28)*0.0765');

  // ── MONTHLY ROLLUP ─────────────────────────────────────
  header(43, 'MONTHLY ROLLUP');
  sh.getRange(44, 1).setValue('Total labor / bi-weekly period');
  sh.getRange(44, 2).setFormula('=E29+I29+D40+F40'); // BOH take-home + absorbed tax(incl employer) + FOH gross + FOH employer FICA
  sh.getRange(45, 1).setValue('Total labor / month (×26/12)');
  sh.getRange(45, 2).setFormula('=B44*26/12');
  sh.getRange(46, 1).setValue('Fixed costs / month');
  sh.getRange(46, 2).setFormula('=B20');
  sh.getRange(47, 1).setValue('TOTAL KNOWN COSTS / MONTH (before COGS)').setFontWeight('bold');
  sh.getRange(47, 2).setFormula('=B45+B46').setFontWeight('bold');

  // ── BREAK-EVEN ─────────────────────────────────────────
  header(49, 'BREAK-EVEN CALCULATOR');
  sh.getRange(50, 1).setValue('COGS % (EDIT ME — decimal, e.g. 0.30)');
  sh.getRange(50, 2).setValue(0.30).setBackground(YELLOW);
  sh.getRange(51, 1).setValue('Break-even revenue / month');
  sh.getRange(51, 2).setFormula('=B47/(1-B50)');
  sh.getRange(52, 1).setValue('Break-even / day (÷30.4)');
  sh.getRange(52, 2).setFormula('=B51/30.4');
  sh.getRange(53, 1).setValue('May 2026 actual / day (reference)');
  sh.getRange(53, 2).setValue(2200);
  sh.getRange(54, 1).setValue('GAP / day (actual − break-even)').setFontWeight('bold');
  sh.getRange(54, 2).setFormula('=B53-B52').setFontWeight('bold');

  // ── OPEN CONFIRMATIONS ─────────────────────────────────
  header(56, 'OPEN CONFIRMATIONS (Chris)');
  var open = [
    ['1. Chefs\' apartment: $616 from EACH of Miguel/Rambo/Eliseo, monthly? (assumed)'],
    ['2. Miguel cash $1,511.28 vs computed $1,490.88 ($20.40 gap)'],
    ['3. Eliseo total $1,319.78 vs $1,300 implied ($19.78 gap)'],
    ['4. Mee Ann paid cash? Any reporting?'],
    ['5. Actual hours/day per chef → true hourly rate'],
    ['6. COGS estimate ($/mo purchases or % of sales)'],
    ['7. Fill yellow cells: water, trash, insurance, internet, POS fees, card processing'],
    ['8. Where does 2026 Lavu daily data live?']
  ];
  sh.getRange(57, 1, open.length, 1).setValues(open);

  // ── Formatting ─────────────────────────────────────────
  sh.getRange('B5:B20').setNumberFormat('$#,##0.00');
  sh.getRange('C24:I29').setNumberFormat('$#,##0.00');
  sh.getRange('D24:D28').setNumberFormat('0');
  sh.getRange('C24:C28').setNumberFormat('$#,##0.00');
  sh.getRange('D33:F41').setNumberFormat('$#,##0.00');
  sh.getRange('C33:C39').setNumberFormat('0.00');
  sh.getRange('B44:B47').setNumberFormat('$#,##0.00');
  sh.getRange('B50').setNumberFormat('0%');
  sh.getRange('B51:B54').setNumberFormat('$#,##0.00');
  sh.setColumnWidth(1, 300);
  sh.setColumnWidths(2, 8, 110);
  sh.setColumnWidth(10, 380);
  sh.setFrozenRows(1);

  ss.toast('Cost Baseline tab built. Fill the yellow cells (COGS %, water, insurance, etc.) — break-even updates live.', '🍜 Done', 10);
}
