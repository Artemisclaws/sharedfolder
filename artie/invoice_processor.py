"""
invoice_processor.py — Aura Thai Invoice Photo Pipeline
Session S45 | Author: Claude (Pinyo Empire Strategist)

Pulls invoice photos from Google Drive, converts HEIC → JPEG,
sends to Haiku for OCR, appends extracted line items to Invoice Log.
Uses service account auth — no browser/OAuth required.
"""

import os
import io
import json
import base64
import subprocess
import tempfile
import sys
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
SHEET_ID = "1KSTvAjsTLHhy5Lbk3jXva0AQzPg68ff13IMoLLK2aaE"
SHEET_TAB = "Invoice Log"

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
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

# ─── HEIC CONVERSION ─────────────────────────────────────────────────────────

def convert_to_jpeg(src_path, dest_path):
    """Convert any image (including HEIC) to JPEG using ImageMagick."""
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

# ─── SHEET WRITING ───────────────────────────────────────────────────────────

EXPECTED_HEADERS = [
    "date", "vendor", "item_name", "quantity", "unit",
    "unit_price", "total_price", "notes",
]


def get_header_map(sheet):
    """Return dict mapping header name → 0-based column index."""
    row1 = sheet.row_values(1)
    return {h.strip().lower(): i for i, h in enumerate(row1)}


def append_rows_to_sheet(gc, line_items, filename):
    sh = gc.open_by_key(SHEET_ID)
    ws = sh.worksheet(SHEET_TAB)
    header_map = get_header_map(ws)

    rows_to_append = []
    for item in line_items:
        row = [""] * len(header_map)
        for key, col_idx in header_map.items():
            row[col_idx] = item.get(key, "")
        rows_to_append.append(row)

    if rows_to_append:
        ws.append_rows(rows_to_append, value_input_option="USER_ENTERED")
        print(f"  → Appended {len(rows_to_append)} rows from {filename}")
    else:
        print(f"  → No rows to append from {filename}")

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

                # 4. Write to sheet
                append_rows_to_sheet(gc, line_items, name)

                newly_processed.add(file_id)
                print(f"  ✓ Done")

            except json.JSONDecodeError as e:
                print(f"  FAILED (JSON parse): {e}")
                failed.append(name)
            except Exception as e:
                print(f"  FAILED: {e}")
                failed.append(name)

    # Save processed IDs
    save_processed_ids(processed_ids | newly_processed)

    print(f"\n── Summary ──")
    print(f"Processed: {len(newly_processed)} file(s)")
    if failed:
        print(f"Failed:    {len(failed)} file(s): {', '.join(failed)}")
    else:
        print("Failed:    none")


if __name__ == "__main__":
    main()
