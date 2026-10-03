"""Run the Actor and write a flattened CSV overview of its Dataset items."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Any

from apify_client import ApifyClient


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
OUTPUT_PATH = ROOT / "data" / "exported-threads-ads.csv"
ACTOR_ID = "datascraperes/threads-ads-library-scraper"
FIELDS = [
    "ad_archive_id", "page_name", "is_active", "publisher_platform",
    "creative.title", "creative.format", "creative.ctaType", "creative.linkUrl",
    "collection.country", "collection.termination", "sourceUrl", "scrapedAt",
]


def nested(item: dict[str, Any], path: str) -> Any:
    value: Any = item
    for part in path.split("."):
        value = value.get(part) if isinstance(value, dict) else None
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN in your environment before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        raise SystemExit("The Actor run did not return a run record.")
    items = client.dataset(run.default_dataset_id).iterate_items()

    with OUTPUT_PATH.open("w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()
        for item in items:
            writer.writerow({field: nested(item, field) for field in FIELDS})

    print(f"Wrote CSV to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
