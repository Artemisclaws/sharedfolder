/**
 * AURA THAI — SYSTEM BUILDER
 * Builds/refreshes: Daily Sales (Pretax), Sales by Item (Monthly),
 * Item Buying Behavior, 3PD Fees & Reconciliation, Prime Cost Dashboard.
 *
 * SAFE TO RE-RUN: only ever touches the 5 tabs this script owns (named below).
 * Never touches Cost Baseline, or any other tab in this file.
 *
 * HOW TO RUN: Extensions > Apps Script > paste this file > Run > buildAuraThaiSystem
 * (Same install motion as cost_baseline_tab_builder.gs — safe, additive.)
 *
 * SOURCE REPORTS — pull these from Lavu, upload to the reports Drive folder,
 * then run this script. File names just need to start with these prefixes:
 *   "Sales "                    -> Daily Totals report (REQUIRED)
 *   "Sales by Item "            -> Sales by Item report (REQUIRED, excludes "with Mods")
 *   "Sales by Item with Mods "  -> Sales by Item with Mods report (OPTIONAL)
 * The script always uses the MOST RECENTLY UPLOADED file per type — you don't
 * need to delete old ones, just upload the new date range and run.
 */

// ─── CONFIG ──────────────────────────────────────────────────────────────
const REPORTS_FOLDER_ID = '1h3fkDDFPyo_V036LGstk3eVCvviE_tCg'; // Lavu reports drop folder
const TAB_DAILY = 'Daily Sales (Pretax)';
const TAB_ITEMS = 'Sales by Item (Monthly)';
const TAB_MODS = 'Item Buying Behavior';
const TAB_3PD = '3PD Fees & Reconciliation';
const TAB_PRIME = 'Prime Cost Dashboard';

const CHANNEL_TAGS = ['Door Dash', 'DoorDash', 'GrubHub', 'Grubhub', 'Uber Eats', 'UberEats'];

// ─── ENTRY POINT ─────────────────────────────────────────────────────────
function buildAuraThaiSystem() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const folder = DriveApp.getFolderById(REPORTS_FOLDER_ID);

  const dailyFile = getLatestFileByPrefix(folder, 'Sales ', ['Sales by Item']);
  const itemFile = getLatestFileByPrefix(folder, 'Sales by Item ', ['with Mods']);
  const modsFile = getLatestFileByPrefix(folder, 'Sales by Item with Mods ');

  if (!dailyFile) {
    SpreadsheetApp.getUi().alert('No "Sales <month/range>.csv" (Daily Totals) file found in the reports folder. Upload it first.');
    return;
  }

  const dailyRows = parseDailyCsv(dailyFile);
  writeDailyTab(ss, dailyRows, dailyFile.getName());

  let itemRows = [], channelCounts = {};
  if (itemFile) {
    const parsed = parseItemCsv(itemFile);
    itemRows = parsed.items;
    channelCounts = parsed.channelCounts;
    writeItemsTab(ss, itemRows, itemFile.getName());
  }

  if (modsFile) {
    const modsParsed = parseItemCsv(modsFile, true);
    writeModsTab(ss, modsParsed.items, modsFile.getName());
  }

  write3pdTab(ss, channelCounts, dailyFile.getName());
  writePrimeCostTab(ss, dailyRows);
  updateStreak(ss, [dailyFile, itemFile, modsFile].filter(Boolean));

  SpreadsheetApp.getUi().alert('Aura Thai system rebuilt. Tabs updated: ' +
    [TAB_DAILY, itemFile ? TAB_ITEMS : null, modsFile ? TAB_MODS : null, TAB_3PD, TAB_PRIME].filter(Boolean).join(', '));
}

// ─── FILE LOOKUP ─────────────────────────────────────────────────────────
function getLatestFileByPrefix(folder, prefix, excludeSubstrings) {
  excludeSubstrings = excludeSubstrings || [];
  const it = folder.getFiles();
  let best = null;
  while (it.hasNext()) {
    const f = it.next();
    const name = f.getName();
    if (!name.startsWith(prefix)) continue;
    if (excludeSubstrings.some(s => name.indexOf(s) !== -1)) continue;
    if (!best || f.getLastUpdated() > best.getLastUpdated()) best = f;
  }
  return best;
}

// ─── PARSERS ─────────────────────────────────────────────────────────────
function csvRowsFromFile(file) {
  let text = file.getBlob().getDataAsString('UTF-8');
  text = text.replace(/^\uFEFF/, ''); // strip BOM
  return Utilities.parseCsv(text);
}

function parseMoney(s) {
  if (s === undefined || s === null || s === '') return 0;
  const n = parseFloat(String(s).replace(/[$,]/g, ''));
  return isNaN(n) ? 0 : n;
}

function parseDailyCsv(file) {
  const rows = csvRowsFromFile(file);
  const out = [];
  for (let i = 1; i < rows.length; i++) {
    const r = rows[i];
    const dateStr = (r[0] || '').trim();
    if (!dateStr) continue; // skip Lavu's own totals row
    const guests = parseInt(r[1], 10) || 0;
    const itemDisc = parseMoney(r[2]);
    const subtotal = parseMoney(r[3]);
    const checkDisc = parseMoney(r[4]);
    const tax = parseMoney(r[5]);
    const autoGrat = parseMoney(r[6]);
    const total = parseMoney(r[7]);
    const cash = parseMoney(r[8]);
    const card = parseMoney(r[9]);
    const other = parseMoney(r[10]);
    const pretaxNet = subtotal - checkDisc;
    out.push({ dateStr, guests, itemDisc, subtotal, checkDisc, pretaxNet, tax, autoGrat, total, cash, card, other });
  }
  return out;
}

function parseItemCsv(file, hasMods) {
  const rows = csvRowsFromFile(file);
  const items = [];
  const channelCounts = {};
  // headers: Quantity,Item,ID,Category,Item Total,...,Item Disc.,Subtotal,Check Disc.,After Disc.,Tax,Total
  // with-mods adds a "Mods" column after Item: Quantity,Item,Mods,ID,Category,...
  const modsOffset = hasMods ? 1 : 0;
  for (let i = 1; i < rows.length; i++) {
    const r = rows[i];
    const qty = parseInt(r[0], 10);
    if (!qty) continue; // skip blank/totals row
    const item = r[1] || '';
    const mods = hasMods ? (r[2] || '') : '';
    const category = r[3 + modsOffset] || '';
    const subtotal = parseMoney(r[9 + modsOffset]);
    const afterDisc = parseMoney(r[11 + modsOffset]);
    const tax = parseMoney(r[12 + modsOffset]);
    const total = parseMoney(r[13 + modsOffset]);

    if (category === 'CUSTOMER INFO' && CHANNEL_TAGS.some(tag => item.indexOf(tag) !== -1)) {
      const key = item.trim();
      channelCounts[key] = (channelCounts[key] || 0) + qty;
      continue; // these are channel tags, not real menu items
    }
    if (category === 'CUSTOMER INFO') continue; // e.g. "NOTES" tag — not a sale

    items.push({ qty, item, mods, category, subtotal, afterDisc, tax, total });
  }
  return { items, channelCounts };
}

// ─── TAB WRITERS ─────────────────────────────────────────────────────────
function getOrCreateTab(ss, name) {
  let sheet = ss.getSheetByName(name);
  if (!sheet) sheet = ss.insertSheet(name);
  sheet.clear();
  return sheet;
}

function writeDailyTab(ss, rows, sourceFileName) {
  const sheet = getOrCreateTab(ss, TAB_DAILY);
  sheet.getRange(1, 1).setValue(
    'SOURCE: Lavu "Daily Totals" report. Last loaded from: ' + sourceFileName +
    ' | Pretax Net = Subtotal − Check Disc. (tax & auto-grat excluded). Re-run builder after each new upload.'
  ).setFontStyle('italic').setFontColor('#666666');
  sheet.getRange(1, 1).setNote(
    'GUESTS COLUMN IS NOT RELIABLE (Chris, S64): dine-in entries get an accurate headcount, but ' +
    'takeout (~90% of orders) is always logged as 1 guest regardless of order size, since Lavu requires ' +
    'a guest count field to submit any order. Do not use this column for avg-ticket-per-guest, covers, or ' +
    'any per-person metric — it will be badly skewed. Fine to ignore/hide.'
  );
  sheet.getRange(2, 1, 1, 12).setValues([[
    'Date', 'Guests', 'Subtotal (Pretax Gross)', 'Item Disc.', 'Check Disc.',
    'Pretax Net Sales', 'Tax', 'Auto Grat.', 'Total (Post-tax)', 'Cash', 'Card', 'Other'
  ]]).setFontWeight('bold');

  const data = rows.map(r => [
    r.dateStr, r.guests, r.subtotal, r.itemDisc, r.checkDisc,
    r.pretaxNet, r.tax, r.autoGrat, r.total, r.cash, r.card, r.other
  ]);
  if (data.length) sheet.getRange(3, 1, data.length, 12).setValues(data);

  const lastRow = 3 + data.length;
  sheet.getRange(lastRow, 1).setValue('TOTAL').setFontWeight('bold');
  sheet.getRange(lastRow, 6).setFormula(`=SUM(F3:F${lastRow - 1})`).setFontWeight('bold');
  sheet.getRange(lastRow, 3).setFormula(`=SUM(C3:C${lastRow - 1})`);
  sheet.getRange(lastRow, 9).setFormula(`=SUM(I3:I${lastRow - 1})`);
  sheet.getRange(lastRow + 1, 1).setValue('AVG PRETAX NET / DAY');
  sheet.getRange(lastRow + 1, 6).setFormula(`=F${lastRow}/COUNTA(A3:A${lastRow - 1})`);
  sheet.autoResizeColumns(1, 12);
}

function writeItemsTab(ss, items, sourceFileName) {
  const sheet = getOrCreateTab(ss, TAB_ITEMS);
  sheet.getRange(1, 1).setValue(
    'SOURCE: Lavu "Sales by Item" report. Last loaded from: ' + sourceFileName +
    ' | Channel tags (Door Dash/GrubHub/Uber Eats) excluded here — see 3PD Fees & Reconciliation tab.'
  ).setFontStyle('italic').setFontColor('#666666');
  sheet.getRange(2, 1, 1, 6).setValues([[
    'Item', 'Category', 'Qty Sold', 'Pretax Subtotal', '% of Monthly Sales', 'Avg Price/Unit'
  ]]).setFontWeight('bold');

  items.sort((a, b) => b.subtotal - a.subtotal);
  const totalSubtotal = items.reduce((s, i) => s + i.subtotal, 0) || 1;
  const data = items.map(i => [
    i.item, i.category, i.qty, i.subtotal, i.subtotal / totalSubtotal, i.qty ? i.subtotal / i.qty : 0
  ]);
  if (data.length) sheet.getRange(3, 1, data.length, 6).setValues(data);
  sheet.getRange(3, 5, data.length, 1).setNumberFormat('0.0%');
  sheet.getRange(3, 4, data.length, 1).setNumberFormat('$#,##0.00');
  sheet.getRange(3, 6, data.length, 1).setNumberFormat('$#,##0.00');
  sheet.autoResizeColumns(1, 6);
}

function writeModsTab(ss, items, sourceFileName) {
  const sheet = getOrCreateTab(ss, TAB_MODS);
  sheet.getRange(1, 1).setValue(
    'SOURCE: Lavu "Sales by Item with Mods" report. Last loaded from: ' + sourceFileName +
    ' | Menu-engineering input (protein/size/spice mix) — not yet wired into Prime Cost. Reference only for now.'
  ).setFontStyle('italic').setFontColor('#666666');
  sheet.getRange(2, 1, 1, 5).setValues([[
    'Item', 'Modifier (protein/size/etc)', 'Category', 'Qty Sold', 'Pretax Subtotal'
  ]]).setFontWeight('bold');

  items.sort((a, b) => b.qty - a.qty);
  const data = items.map(i => [i.item, i.mods, i.category, i.qty, i.subtotal]);
  if (data.length) sheet.getRange(3, 1, data.length, 5).setValues(data);
  sheet.getRange(3, 5, data.length, 1).setNumberFormat('$#,##0.00');
  sheet.autoResizeColumns(1, 5);
}

function write3pdTab(ss, channelCounts, dailyFileName) {
  const sheet = getOrCreateTab(ss, TAB_3PD);
  sheet.getRange(1, 1).setValue(
    'Order counts (below) auto-pull from the Sales by Item report\'s channel tags — a FLOOR, not an exact count ' +
    '(Chris, S64: staff tags DD/GH/UE orders manually when entering them, and sometimes forgets — so these ' +
    'numbers undercount, never overcount). Use as a rough cross-check against the platform portal\'s own order ' +
    'count, not as ground truth on their own. ' +
    'FEE/COMMISSION $ COLUMNS ARE MANUAL — pull "Payout Summary" (or equivalent) from each platform\'s merchant portal and enter below.'
  ).setFontStyle('italic').setFontColor('#666666');

  sheet.getRange(3, 1, 1, 6).setValues([[
    'Platform', 'Order Count (Lavu tag, auto)', 'Gross Sales $ (enter from portal)',
    'Fees/Commission $ (enter from portal)', 'Net Payout $ (enter from portal)', 'Commission %'
  ]]).setFontWeight('bold');

  const platforms = [
    { label: 'DoorDash', tags: ['Door Dash', 'DoorDash'] },
    { label: 'Uber Eats', tags: ['Uber Eats', 'UberEats'] },
    { label: 'GrubHub', tags: ['GrubHub', 'Grubhub'] }
  ];
  platforms.forEach((p, idx) => {
    const count = p.tags.reduce((s, t) => s + (channelCounts[t] || 0), 0);
    const row = 4 + idx;
    sheet.getRange(row, 1).setValue(p.label);
    sheet.getRange(row, 2).setValue(count);
    // C, D, E left blank for manual entry
    sheet.getRange(row, 6).setFormula(`=IF(C${row}=0,"",D${row}/C${row})`);
    sheet.getRange(row, 6).setNumberFormat('0.0%');
  });

  sheet.getRange(8, 1).setValue('Order counts reflect period in: ' + dailyFileName).setFontStyle('italic').setFontColor('#999999');

  // ── Upload streak block ──
  sheet.getRange(10, 1).setValue('UPLOAD STREAK').setFontWeight('bold');
  sheet.getRange(11, 1, 4, 1).setValues([['Last upload:'], ['Current streak (weeks):'], ['Longest streak (weeks):'], ['Status:']]);
  sheet.getRange(11, 2).setValue('__LAST_DATE__');
  sheet.getRange(12, 2).setValue('__STREAK__');
  sheet.getRange(13, 2).setValue('__LONGEST__');
  sheet.getRange(14, 2).setValue('__STATUS__');
  sheet.autoResizeColumns(1, 6);
}

function writePrimeCostTab(ss, dailyRows) {
  const sheet = getOrCreateTab(ss, TAB_PRIME);
  sheet.getRange(1, 1).setValue(
    'PRIME COST MODEL (industry standard: COGS % + Labor % of Pretax Net Sales; target ≤60% full-service). ' +
    'COGS % and Labor $ below are MANUAL until the Cost Baseline tab (A-13) is live — then link cells directly.'
  ).setFontStyle('italic').setFontColor('#666666');

  const pretaxNet = dailyRows.reduce((s, r) => s + r.pretaxNet, 0);
  const days = dailyRows.length;

  sheet.getRange(3, 1).setValue('Pretax Net Sales (period)');
  sheet.getRange(3, 2).setValue(pretaxNet).setNumberFormat('$#,##0.00');
  sheet.getRange(4, 1).setValue('Days in period');
  sheet.getRange(4, 2).setValue(days);
  sheet.getRange(5, 1).setValue('Avg Pretax Net Sales / Day');
  sheet.getRange(5, 2).setFormula('=B3/B4').setNumberFormat('$#,##0.00');

  sheet.getRange(7, 1).setValue('COGS % (enter — from Cost Baseline tab once live)');
  sheet.getRange(7, 2).setValue(0.30).setNumberFormat('0.0%'); // S63 scenario default — overwrite once real
  sheet.getRange(8, 1).setValue('Monthly Labor $ (from COST_BASELINE.md, S63)');
  sheet.getRange(8, 2).setValue(32597).setNumberFormat('$#,##0.00');
  sheet.getRange(9, 1).setValue('Monthly Fixed Costs $ (from COST_BASELINE.md, S63)');
  sheet.getRange(9, 2).setValue(12316).setNumberFormat('$#,##0.00');

  sheet.getRange(11, 1).setValue('COGS $ (period)');
  sheet.getRange(11, 2).setFormula('=B3*B7').setNumberFormat('$#,##0.00');
  sheet.getRange(12, 1).setValue('Labor $ (prorated to period)');
  sheet.getRange(12, 2).setFormula('=B8/30.4*B4').setNumberFormat('$#,##0.00');
  sheet.getRange(13, 1).setValue('PRIME COST $ (COGS + Labor)');
  sheet.getRange(13, 2).setFormula('=B11+B12').setFontWeight('bold').setNumberFormat('$#,##0.00');
  sheet.getRange(14, 1).setValue('PRIME COST % of Pretax Net Sales');
  sheet.getRange(14, 2).setFormula('=B13/B3').setFontWeight('bold').setNumberFormat('0.0%');
  sheet.getRange(15, 1).setValue('Target: ≤60% (full-service industry standard)');

  sheet.getRange(17, 1).setValue('Fixed Costs $ (prorated to period)');
  sheet.getRange(17, 2).setFormula('=B9/30.4*B4').setNumberFormat('$#,##0.00');
  sheet.getRange(18, 1).setValue('BREAK-EVEN Pretax Net Sales (period)');
  sheet.getRange(18, 2).setFormula('=B13+B17').setFontWeight('bold').setNumberFormat('$#,##0.00');
  sheet.getRange(19, 1).setValue('ACTUAL vs BREAK-EVEN (period)');
  sheet.getRange(19, 2).setFormula('=B3-B18').setFontWeight('bold').setNumberFormat('$#,##0.00');
  sheet.getRange(20, 1).setValue('(positive = above break-even, negative = below)');

  sheet.autoResizeColumns(1, 2);
}

// ─── STREAK TRACKER ────────────────────────────────────────────────────
function updateStreak(ss, files) {
  const props = PropertiesService.getDocumentProperties();
  const lastDateStr = props.getProperty('LAST_UPLOAD_DATE');
  const streakStr = props.getProperty('CURRENT_STREAK') || '0';
  const longestStr = props.getProperty('LONGEST_STREAK') || '0';

  const mostRecentUpload = files.reduce((max, f) => {
    const t = f.getLastUpdated();
    return (!max || t > max) ? t : max;
  }, null);

  let streak = parseInt(streakStr, 10);
  let longest = parseInt(longestStr, 10);
  let status = '';

  if (!lastDateStr) {
    streak = 1;
    status = 'First upload logged.';
  } else {
    const lastDate = new Date(lastDateStr);
    const gapDays = (mostRecentUpload - lastDate) / (1000 * 60 * 60 * 24);
    if (gapDays < 0.5) {
      status = 'Same-session re-run — streak unchanged.';
    } else if (gapDays <= 10) {
      streak += 1;
      status = 'Streak continued.';
    } else {
      streak = 1;
      status = `Streak reset — ${Math.round(gapDays)} days since last upload.`;
    }
  }
  if (streak > longest) longest = streak;

  props.setProperty('LAST_UPLOAD_DATE', mostRecentUpload.toISOString());
  props.setProperty('CURRENT_STREAK', String(streak));
  props.setProperty('LONGEST_STREAK', String(longest));

  const sheet = ss.getSheetByName(TAB_3PD);
  if (sheet) {
    sheet.getRange(11, 2).setValue(Utilities.formatDate(mostRecentUpload, Session.getScriptTimeZone(), 'yyyy-MM-dd'));
    sheet.getRange(12, 2).setValue(streak + (streak === 1 ? ' week' : ' weeks'));
    sheet.getRange(13, 2).setValue(longest + (longest === 1 ? ' week' : ' weeks'));
    sheet.getRange(14, 2).setValue(status);
  }
}
