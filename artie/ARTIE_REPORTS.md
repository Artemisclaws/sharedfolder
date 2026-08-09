# ARTIE_REPORTS.md
**Home:** `artie/ARTIE_REPORTS.md` — canonical, not a cache.
**Written by:** Artie's automated scripts only. Claude reads this at session start / on request.
**Purpose:** Machine-generated status reports (freshness checks, intake watchers, etc.) that need to reach Claude, not just Chris. Discord posts are for Chris's own visibility only — Claude has no Discord connector and cannot read them. This file is the actual handoff channel from Artie to Claude.
**Format:** one line per report, reverse-chronological, newest on top.
`YYYY-MM-DD | script-name | STATUS | detail`

---

2026-08-09 | artie-invoice-intake-watcher | ERROR | Gmail check failed: gog gmail search to:artemisclaws+invoices@gmail.com after:2026/08/08 --max 50 failed (exit 1): Get "https://gmail.googleapis.com/gmail/v1/users/me/threads?alt=json&maxResults=50&prettyPrint=false&q=to%3Aartemisclaws%2Binvoices%40gmail.com+after%3A2026%2F08%2F08": round trip: base token source: oauth2: "invalid_grant" "Token has been expired or revoked." || Drive check failed: gog drive ls --parent 1HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza --query modifiedTime > '2026-08-08T14:00:00.360260+00:00' failed (exit 1): Get "https://www.googleapis.com/drive/v3/files?alt=json&corpora=allDrives&fields=nextPageToken%2C+files%28id%2C+name%2C+mimeType%2C+size%2C+modifiedTime%2C+parents%2C+webViewLink%29&includeItemsFromAllDrives=true&orderBy=modifiedTime+desc&pageSize=20&pageToken=&prettyPrint=false&q=modifiedTime+%3E+%272026-08-08T14%3A00%3A00.360260%2B00%3A00%27+and+%271HkVrBfkooEdjzRlj_Jg_jFdcoGwObyza%27+in+parents+and+trashed+%3D+false&supportsAllDrives=true": round trip: base token source: oauth2: "invalid_grant" "Token has been expired or revoked."
2026-08-09 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (13d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-08 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-07T14:00:00.391510+00:00
2026-08-08 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (12d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-07 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-06T14:00:01.388775+00:00
2026-08-07 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (11d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-06 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-05T14:00:01.066092+00:00
2026-08-06 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (10d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-05 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-04T14:00:01.845104+00:00
2026-08-05 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (9d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-04 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-03T14:00:03.282505+00:00
2026-08-04 | artie-freshness-heartbeat | RED | Daily Sales STALE -- newest 2026-07-27 (8d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-03 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-02T22:01:49.712294+00:00
2026-08-03 | artie-freshness-heartbeat | RED | Daily Sales current to 2026-07-27 (7d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-02 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-02T21:57:33.727620+00:00
2026-08-02 | artie-freshness-heartbeat | RED | Daily Sales current to 2026-07-27 (6d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-02 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since 2026-08-02T02:41:43.719888Z
2026-08-02 | artie-freshness-heartbeat | RED | Daily Sales current to 2026-07-27 (6d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-01 | artie-invoice-intake-watcher | GREEN | 0 new invoice email(s), 0 new Drive file(s) since first run
2026-08-01 | artie-freshness-heartbeat | RED | Daily Sales current to 2026-07-27 (5d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20
2026-08-01 | artie-freshness-heartbeat | RED | Daily Sales current to 2026-07-27 (5d, budget 7d) | Delivery Payouts: PENDING -- 2026-07-13 to 2026-07-20