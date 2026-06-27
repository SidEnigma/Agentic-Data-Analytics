import subprocess
import os
import sys
from google.cloud import bigquery
from google.oauth2 import credentials

PROJECT = "project-504296d8-0479-471d-a5a"
TABLE = f"{PROJECT}.stackoverflow_analysis.language_reputation"

gcloud_bin = os.path.join(
    os.environ["LOCALAPPDATA"],
    "Google", "Cloud SDK", "google-cloud-sdk", "bin", "gcloud.cmd"
)
token = subprocess.check_output([gcloud_bin, "auth", "print-access-token"], text=True).strip()
creds = credentials.Credentials(token=token)
client = bigquery.Client(project=PROJECT, credentials=creds)

rows = list(client.query(f"SELECT * FROM `{TABLE}` ORDER BY language").result())
warnings = []

expected_languages = {
    'python', 'javascript', 'java', 'c#', 'c++', 'php', 'ruby', 'go',
    'rust', 'swift', 'kotlin', 'typescript', 'scala', 'r', 'perl',
    'haskell', 'lua', 'dart', 'elixir', 'clojure', 'sas', 'matlab'
}

print("=== Quality Checks ===\n")

# --- Row count ---
print(f"[CHECK] Row count: {len(rows)} (expected {len(expected_languages)})")
if len(rows) != len(expected_languages):
    warnings.append(f"Expected {len(expected_languages)} rows, got {len(rows)}")

# --- Languages present ---
found_languages = {row.language for row in rows}
missing = expected_languages - found_languages
extra = found_languages - expected_languages
if missing:
    warnings.append(f"Missing languages: {missing}")
if extra:
    warnings.append(f"Unexpected languages: {extra}")

# --- Per-row checks ---
for row in rows:
    lang = row.language
    dev_count = row.developer_count
    avg_rep = row.avg_reputation
    med_rep = row.median_reputation
    max_rep = row.max_reputation

    if lang is None:
        warnings.append("Row with NULL language found")
    if dev_count is None:
        warnings.append(f"{lang}: NULL developer_count")
    else:
        if dev_count < 1:
            warnings.append(f"{lang}: developer_count={dev_count} should be >= 1")
        if dev_count >= 1_000_000:
            warnings.append(f"{lang}: developer_count={dev_count} seems high")

    if avg_rep is None:
        warnings.append(f"{lang}: NULL avg_reputation")
    elif avg_rep < 100:
        warnings.append(f"{lang}: avg_reputation={avg_rep} < 100 (should not happen with filter)")

    if med_rep is None:
        warnings.append(f"{lang}: NULL median_reputation")
    elif med_rep < 100:
        warnings.append(f"{lang}: median_reputation={med_rep} < 100")

    if max_rep is None:
        warnings.append(f"{lang}: NULL max_reputation")

    if avg_rep is not None and max_rep is not None:
        if avg_rep > max_rep:
            warnings.append(f"{lang}: avg_reputation={avg_rep} > max_reputation={max_rep}")
    if med_rep is not None and max_rep is not None:
        if med_rep > max_rep:
            warnings.append(f"{lang}: median_reputation={med_rep} > max_reputation={max_rep}")

print(f"[CHECK] Null/range checks passed for all {len(rows)} rows")

# --- Summary ---
print(f"\n=== Summary ===")
if warnings:
    print(f"{len(warnings)} warning(s):")
    for w in warnings:
        print(f"  WARN: {w}")
    sys.exit(1)
else:
    print("All quality checks passed.")
    sys.exit(0)
