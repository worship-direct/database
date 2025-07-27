import os
import json

DB_PATH = "db.json"
NEW_ENTRY_DIR = "new_entry"

def base36encode(number):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return "0"
    result = ""
    while number:
        number, i = divmod(number, 36)
        result = chars[i] + result
    return result

# Load existing database
if os.path.exists(DB_PATH):
    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = []

existing_ids = {entry.get("organization_id", "") for entry in db if "organization_id" in entry}

def next_id(existing_ids):
    # Find the max base-36 id, increment, and return as base-36 string
    if not existing_ids:
        return "0"
    max_id = max([int(i, 36) for i in existing_ids if i])
    new_id = max_id + 1
    return base36encode(new_id).upper()

# Process new entries
new_files = [fname for fname in sorted(os.listdir(NEW_ENTRY_DIR)) if fname.endswith(".json")]
if not new_files:
    print("No new entries found.")
else:
    for fname in new_files:
        path = os.path.join(NEW_ENTRY_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            entry = json.load(f)
        # Assign new base-36 ID
        entry["organization_id"] = next_id(existing_ids)
        existing_ids.add(entry["organization_id"])
        db.append(entry)
        print(f"Added {fname} as {entry['organization_id']}")
        # Optionally remove file after processing
        os.remove(path)

    # Write updated database
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"{len(new_files)} new entries added to {DB_PATH}.")
