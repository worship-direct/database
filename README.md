# Religious Buildings Database

This repository contains a structured database of religious buildings and organizations.

## Automated Entry Addition Workflow

- Place new organization entries as `.json` files in `new_entry/`.
- On push, the workflow merges new entries into `db.json`.
- Each new entry receives a unique organization ID using base-36 (0-9, A-Z).
- The workflow commits changes to `db.json`.

See `.github/workflows/add_new_entries.yml` and `scripts/process_new_entries.py` for details.

## Schema

Each organization entry includes:
- organization_id (base-36 alphanumeric)
- name
- religion
- street_address
- city
- state
- postal_code
- country
- web_address
- phone
- year_established
- notes

See `organization.schema.json` for formal schema.
