import subprocess
import os
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

query = f"SELECT * FROM `{TABLE}` ORDER BY avg_reputation DESC"
rows = client.query(query).result()

print(f"{'Language':<14} {'Dev Count':<12} {'Avg Rep':<10} {'Med Rep':<10} {'Max Rep':<10}")
print("-" * 56)
for row in rows:
    print(
        f"{row.language:<14} {row.developer_count:<12} {row.avg_reputation:<10} {row.median_reputation:<10} {row.max_reputation:<10}"
    )
