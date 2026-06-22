"""drive_diagnostic.py — Check what the service account can see in Drive (no folder filter)."""
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pathlib import Path

SA = Path("service_account.json")
FOLDERS = [
    "14cxHSf8ubo3x9R07bz_fvUQsT2O2YO5o",
    "1SBQ3e3SjfQwiLyldozTOZoQWz5MtP50A",
]

creds = service_account.Credentials.from_service_account_file(
    str(SA), scopes=["https://www.googleapis.com/auth/drive"]
)
drive = build("drive", "v3", credentials=creds)

print("=== ALL files visible to service account (first 20) ===")
r = drive.files().list(
    fields="files(id,name,mimeType,parents)",
    pageSize=20,
).execute()
items = r.get("files", [])
if not items:
    print("NONE — service account cannot see any Drive files at all")
else:
    for f in items:
        print(f"  {f['mimeType']} | {f['name']} | parents: {f.get('parents','?')}")

print(f"\nTotal visible: {len(items)}")

print("\n=== Folder metadata check ===")
for fid in FOLDERS:
    try:
        meta = drive.files().get(fileId=fid, fields="id,name,mimeType,shared").execute()
        print(f"  ACCESSIBLE: {meta['name']} (shared={meta.get('shared')})")
    except Exception as e:
        print(f"  ERROR on {fid}: {e}")
