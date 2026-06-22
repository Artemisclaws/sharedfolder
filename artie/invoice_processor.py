"""
invoice_processor.py — Aura Thai Invoice Photo Pipeline
Session S45/S46 | Author: Claude (Pinyo Empire Strategist)

Pulls invoice photos from Google Drive, converts HEIC → JPEG,
sends to Haiku for OCR, validates data, appends to Invoice Log,
confirms write, then archives file to Archive folder.
Uses service account auth — no browser/OAuth required.
"""

import os
import json
import base64
import subprocess
import tempfile
import sys
from datetime import datetime
from pathlib import Path

import anthropic
import gspread
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
SA_PATH = SCRIPT_DIR / "service_account.json"
PROCESSED_LOG = SCRIPT_DIR / "processed_invoice_files.json"

DRIVE_FOLDER_ID = "1jOJaTcZ9g-_k4BKypme7B-IsU8ojwcr3"
ARCHIVE_FOLDER_ID = "1GPxZT-mG6rlYFRCIKmRiEgxIQj9Xuh31"
SHEET_ID = "1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE"
SHEET_TAB = "Invoice Log"

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

# ─── AUTH ─────────────────────────────────────────────────────────────────────

def get_google_creds():
    if not SA_PATH.exists():
        raise FileNotFoundError(
            f"service_account.json not found at {SA_PATH}\n"
            "Place the service account key file in the same folder as this script."
        )
    return service_account.Credentials.from_service_account_file(
        str(SA_PATH), scopes=SCOPES
    )

# ─── PROCESSED FILE TRACKING ─────────────────────────────────────────────────

def load_processed_ids():
    if PROCESSED_LOG.exists():
        with open(PROCESSED_LOG, "r") as f:
            return set(json.load(f))
    return set()


def save_processed_ids(ids):
    with open(PROCESSED_LOG, "w") as f:
        json.dump(list(ids), f, indent=2)

# ─── DRIVE ───────────────────────────────────────────────────────────────────

def list_invoice_files(drive_service):
    query = f"'{DRIVE_FOLDER_ID}' in parents and trashed=false"
    results = drive_service.files().list(
        q=query,
        fields="files(id, name, mimeType)",
        pageSize=200,
    ).execute()
    return results.get("files", [])


def download_file(drive_service, file_id, dest_path):
    request = drive_service.files().get_media(fileId=file_id)
    with open(dest_path, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()


def archive_file(drive_service, file_id, filename):
    """Move file from invoice folder to archive folder."""
    drive_service.files().update(
        fileId=file_id,
        addParents=ARCHIVE_FOLDER_ID,
        removeParents=DRIVE_FOLDER_ID,
        fields="id, parents",
    ).execute()
    print(f"  → Archived: {filename}")

# ─── HEIC CONVERSION ─────────────────────────────────────────────────────────

def convert_to_jpeg(src_path, dest_path):
    result = subprocess.run(
        ["convert", str(src_path), str(dest_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"ImageMagick convert failed: {result.stderr.strip()}")

# ─── OCR VIA HAIKU ───────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an OCR assistant for a Thai restaurant.
Extract all line items from this invoice photo.
Return ONLY a JSON array. Each element must have these exact keys:
  date, vendor, item_name, quantity, unit, unit_price, total_price, notes

Rules:
- date format: YYYY-MM-DD (infer year if not shown, assume current year)
- quantity and prices: numbers only, no currency symbols
- unit: ea, lb, oz, kg, bag, box, case, can, bottle, bunch, etc.
- notes: any relevant text (invoice number, lot, etc.) or empty string
- If a field is unreadable, use empty string or 0 for numbers
- Do NOT include markdown, explanation, or anything outside the JSON array"""


def ocr_invoice(image_path):
    with open(image_path, "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Extract all line items from this invoice as JSON.",
                    },
                ],
            }
        ],
    )
    return message.content[0].text.strip()

# ─── VALIDATION ──────────────────────────────────────────────────────────────

def validate_line_items(line_items, filename):
    """
    Check 1: Validate extracted data before writing.
    Returns (passed: bool, issues: list of str)
    """
    issues = []
    if not line_items:
        issues.append("No line items extracted")
        return False, issues

    for i, item in enumerate(line_items):
        row_label = f"Row {i+1}"

        # Required text fields
        if not item.get("item_name", "").strip():
            issues.append(f"{row_label}: missing item_name")
        if not item.get("vendor", "").strip():
            issues.append(f"{row_label}: missing vendor")

        # Date parseable
        date_val = item.get("date", "")
        if date_val:
            try:
                datetime.strptime(date_val, "%Y-%m-%d")
            except ValueError:
                issues.append(f"{row_label}: bad date format '{date_val}' (expected YYYY-MM-DD)")
        else:
            issues.append(f"{row_label}: missing date")

        # Numeric fields
        for field in ("quantity", "unit_price", "total_price"):
            val = item.get(field, 0)
            try:
                numeric = float(val)
                if numeric < 0:
                    issues.append(f"{row_label}: {field} is negative ({val})")
            except (TypeError, ValueError):
                issues.append(f"{row_label}: {field} is not a number ({val})")

    passed = len(issues) == 0
    return passed, issues

# ─── SHEET WRITING ───────────────────────────────────────────────────────────

def get_header_map(sheet):
    row1 = sheet.row_values(1)
    return {h.strip().lower(): i for i, h in enumerate(row1)}


def append_and_confirm(gc, line_items, filename):
    """
    Write rows to sheet, then re-read to confirm count.
    Returns (success: bool, rows_written: int)
    """
    sh = gc.open_by_key(SHEET_ID)
    ws = sh.worksheet(SHEET_TAB)
    header_map = get_header_map(ws)

    rows_to_append = []
    for item in line_items:
        row = [""] * len(header_map)
        for key, col_idx in header_map.items():
            row[col_idx] = item.get(key, "")
        rows_to_append.append(row)

    if not rows_to_append:
        return False, 0

    # Get row count before write
    all_before = ws.get_all_values()
    rows_before = len([r for r in all_before if any(c.strip() for c in r)])

    ws.append_rows(rows_to_append, value_input_option="USER_ENTERED")

    # Check 2: Confirm rows actually landed
    all_after = ws.get_all_values()
    rows_after = len([r for r in all_after if any(c.strip() for c in r)])
    rows_added = rows_after - rows_before

    if rows_added >= len(rows_to_append):
        print(f"  → Wrote {rows_added} rows | Confirmed in sheet ✓")
        return True, rows_added
    else:
        print(f"  → WRITE MISMATCH: expected {len(rows_to_append)}, confirmed {rows_added}")
        return False, rows_added

# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    print("── Aura Thai Invoice Processor ──")
    creds = get_google_creds()
    drive_service = build("drive", "v3", credentials=creds)
    gc = gspread.authorize(creds)

    processed_ids = load_processed_ids()
    all_files = list_invoice_files(drive_service)

    new_files = [f for f in all_files if f["id"] not in processed_ids]
    if not new_files:
        print("No new invoice files found. All up to date.")
        return

    print(f"Found {len(new_files)} new file(s) to process.")

    newly_processed = set()
    archived = []
    failed = []

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        for f in new_files:
            file_id = f["id"]
            name = f["name"]
            print(f"\nProcessing: {name}")

            raw_path = tmp / name
            jpeg_path = tmp / (Path(name).stem + ".jpg")

            try:
                # 1. Download
                download_file(drive_service, file_id, str(raw_path))

                # 2. Convert to JPEG
                convert_to_jpeg(raw_path, jpeg_path)

                # 3. OCR
                raw_json = ocr_invoice(str(jpeg_path))
                line_items = json.loads(raw_json)

                # 4. Validate (Check 1)
                valid, issues = validate_line_items(line_items, name)
                if not valid:
                    print(f"  VALIDATION FAILED — file left in inbox:")
                    for issue in issues:
                        print(f"    • {issue}")
                    failed.append(f"{name} (validation)")
                    continue

                # 5. Write + confirm (Check 2)
                write_ok, rows_written = append_and_confirm(gc, line_items, name)
                if not write_ok:
                    print(f"  WRITE CONFIRMATION FAILED — file left in inbox")
                    failed.append(f"{name} (write confirm)")
                    continue

                # 6. Both checks passed — archive
                archive_file(drive_service, file_id, name)
                newly_processed.add(file_id)
                archived.append(name)
                print(f"  ✓ Complete")

            except json.JSONDecodeError as e:
                print(f"  FAILED (JSON parse): {e}")
                failed.append(f"{name} (JSON parse)")
            except Exception as e:
                print(f"  FAILED: {e}")
                failed.append(f"{name} ({type(e).__name__})")

    save_processed_ids(processed_ids | newly_processed)

    print(f"\n── Summary ──")
    print(f"Processed & archived: {len(archived)}")
    if archived:
        for a in archived:
            print(f"  ✓ {a}")
    if failed:
        print(f"Failed (left in inbox): {len(failed)}")
        for f in failed:
            print(f"  ✗ {f}")
    else:
        print("Failed: none")


if __name__ == "__main__":
    main()
