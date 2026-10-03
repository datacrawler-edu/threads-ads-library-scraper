"""Run a short list of keyword searches sequentially with the hosted Actor."""

from __future__ import annotations

import json
import os
from pathlib import Path

from apify_client import ApifyClient


ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
ACTOR_ID = "datascraperes/threads-ads-library-scraper"
QUERIES = ["ikea", "nike"]


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN in your environment before running this example.")

    client = ApifyClient(token)
    base_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))

    for query in QUERIES:
        run_input = {**base_input, "query": query}
        print(f"\nResults for {query}:")
        run = client.actor(ACTOR_ID).call(run_input=run_input)
        if run is None:
            raise SystemExit(f"The Actor run for {query!r} did not return a run record.")

        for item in client.dataset(run.default_dataset_id).iterate_items():
            print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
