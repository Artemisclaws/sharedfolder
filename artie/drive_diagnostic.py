"""drive_diagnostic.py — Check what service account can see in Drive folder."""
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pathlib import Path
import json

SA = Path("service_account.json")
FOLDER = "1jOJaTcZ9g-_k4BKypme7B-IsU8ojwcr3"

creds = service_account.Credentials.from_service_account_file(
    str(SA), scopes=["https://www.googleapis.com/auth/drive"]
)
drive = build("drive", "v3", credentials=creds)

folders = [FOLDER]
all_files = []

while folders:
    fid = folders.pop(0)
    r = drive.files().list(
        q=f"'{fid}' in parents and trashed=false",
        fields="files(id,name,mimeType)",
    ).execute()
    items = r.get("files", [])
    print(f"Folder {fid} — {len(items)} item(s):")
    for f in items:
        if f["mimeType"] == "application/vnd.google-apps.folder":
            print(f"  SUBFOLDER: {f['name']} ({f['id']})")
            folders.append(f["id"])
        else:
            print(f"  FILE: {f['name']}")
            all_files.append(f)

print(f"\nTotal files visible to service account: {len(all_files)}")

p = Path("processed_invoice_files.json")
if p.exists():
    ids = json.load(open(p))
    print(f"processed_invoice_files.json: {len(ids)} IDs already logged")
else:
    print("processed_invoice_files.json: does not exist (no files processed yet)")
