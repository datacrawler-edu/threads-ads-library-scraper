# Threads Ads Library API examples

Find public Meta Ads Library records whose reported placements include Threads. This repository shows how to run the hosted **Threads Ads Library Scraper** from Apify's web interface or call it with Python, JavaScript, or cURL.

[Open the Threads Ads Library Scraper on Apify](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata)

## What this repository helps you do

- Search Meta Ad Library by keyword or a Facebook advertiser page and collect matching ads that include Threads placement.
- Review ad copy, normalized creative, calls to action, landing links, placement labels, and collection metadata in a Dataset.
- Export a compact ad overview to CSV or connect Actor results to a Python or JavaScript workflow.
- Request optional advertiser transparency and page details when those details are available.

Threads is the fixed placement filter. A returned ad may also list Facebook or Instagram in `publisher_platform`, because the source record can cover several Meta placements.

## Example result

This is a selected-field projection from a real Dataset item. The raw source snapshot and time-limited media URLs are omitted; the live Dataset item includes the complete available record.

```json
{
  "ad_archive_id": "3675117995977459",
  "page_name": "IKEA",
  "is_active": true,
  "publisher_platform": [
    "FACEBOOK",
    "INSTAGRAM",
    "THREADS"
  ],
  "creative": {
    "title": "IKEA",
    "format": "CAROUSEL",
    "texts": [
      "Encuentra un nuevo dueño para tus muebles\nDescubre cómo",
      " "
    ],
    "ctaType": "SEE_DETAILS",
    "linkUrl": "https://secondhand.ikea.com/es/es/?utm_source=meta&utm_medium=paid-social&utm_campaign=es_secondhand"
  },
  "collection": {
    "query": "ikea",
    "country": "ES",
    "startDate": null,
    "endDate": null,
    "activeStatus": "ACTIVE",
    "mediaType": "ALL",
    "adType": "ALL",
    "publisherPlatforms": [
      "THREADS"
    ],
    "contentLanguages": [],
    "maxAds": 1,
    "maxPages": 1,
    "pageId": null,
    "pagesFetched": 1,
    "termination": "page_delivered",
    "uniqueAds": 1,
    "budgetLimited": false
  },
  "sourceUrl": "https://www.facebook.com/ads/library/?id=3675117995977459",
  "scrapedAt": "2026-10-02T16:40:45.564856+00:00"
}
```

The same sample is available as [`data/sample-output.json`](data/sample-output.json) and as a flattened row in [`data/sample-output.csv`](data/sample-output.csv).

## Run without code

1. Open the [hosted Actor](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata).
2. In **Input**, enter a keyword such as `ikea`, or provide a Facebook Page ID or Facebook page URL/alias.
3. Choose optional country, ad status, media type, date range, result limit, or advertiser-detail enrichment.
4. Click **Start**, then open **Dataset** after the run finishes.
5. Export the Dataset as JSON, CSV, or Excel.

See [`docs/no-code-guide.md`](docs/no-code-guide.md) for field-by-field steps and a small first input in [`data/sample-input.json`](data/sample-input.json).

## Try it with Apify's free plan

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors, and no credit card is required to start. A small Actor run can use that credit while it is available; it is not unlimited free usage. Unused credit expires at the end of the billing cycle. See [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current account terms.

## Quick start for developers

### Python

Install the official client:

```bash
python -m pip install apify-client
```

Set your Apify API token in the environment. In Bash:

```bash
export APIFY_API_TOKEN="your-token"
```

In Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

Run the example from the repository root:

```bash
python examples/python/search_threads_ads.py
```

The example reads [`data/sample-input.json`](data/sample-input.json), waits for the hosted Actor run to finish, and prints its Dataset items. Keep your API token private and out of committed files.

## Input example

The input below is a minimal one-result keyword search. Provide at least one search target: `query`, `pageId`, or `pageUrl`.

```json
{
  "query": "ikea",
  "country": "ES",
  "pageId": "",
  "pageUrl": "",
  "activeStatus": "ACTIVE",
  "mediaType": "ALL",
  "adType": "ALL",
  "contentLanguages": [],
  "startDate": "",
  "endDate": "",
  "maxAds": 1,
  "maxPages": 1,
  "includeDetails": false,
  "detailsLimit": 25
}
```

See [`docs/input-reference.md`](docs/input-reference.md) for all fields, defaults, allowed values, and limits.

## Request examples

### cURL

[`examples/curl-request.md`](examples/curl-request.md) shows the synchronous API request.

### Python

[`examples/python/search_threads_ads.py`](examples/python/search_threads_ads.py) runs the Actor and reads its Dataset. [`examples/python/export_threads_ads_csv.py`](examples/python/export_threads_ads_csv.py) writes a flattened CSV file.

### JavaScript

[`examples/javascript/request.mjs`](examples/javascript/request.mjs) uses Apify's official JavaScript API client.

All examples call the hosted Actor. They do not require the Actor's private source code.

## Output fields

| Field | Meaning |
| --- | --- |
| `ad_archive_id` | Meta Ad Library identifier used to identify and deduplicate an ad. |
| `publisher_platform` | Placements reported by Meta for the source ad; may include several platforms. |
| `creative` | Normalized creative fields such as text, title, format, CTA, destination, and media URLs. |
| `snapshot` | Original ad snapshot returned by Meta, when available. |
| `details` | Optional advertiser transparency, payer/beneficiary, audience, and page information. |
| `enrichment.status` | Per-ad detail result: `enriched`, `no_data`, `skipped`, or `failed`. |
| `collection` | Search filters, page count, result count, and collection termination information. |
| `sourceUrl` | Direct Meta Ad Library link for the ad. |
| `scrapedAt` | UTC timestamp when the Dataset item was assembled. |

See [`docs/output-reference.md`](docs/output-reference.md) for the output contract and nullable fields.

## Common use cases

[`docs/use-cases.md`](docs/use-cases.md) shows how to use the Actor for:

- Competitor creative research focused on ads that report Threads placement.
- Country-specific image or video creative review.
- Advertiser-page research with optional transparency details.

## How to find Meta ads with Threads placement and export them to CSV

Set `query` to a brand, advertiser, product, or phrase, then choose the country and `maxAds`. The Actor keeps the Threads placement filter fixed and returns one row per unique ad archive ID. Use the `publisher_platform` array to see every placement Meta reports, then download the Dataset as CSV or run [`examples/python/export_threads_ads_csv.py`](examples/python/export_threads_ads_csv.py).

## How to search one advertiser's Threads ads

Use `pageId` for the numeric Facebook Page ID, or `pageUrl` for the public Facebook page URL or exact page alias. These are alternatives to `query`; a Threads profile URL is not supported. The page's returned ads must still report Threads placement.

## FAQ

See [`docs/faq.md`](docs/faq.md) for search-target rules, placement interpretation, optional enrichment, and billing behavior.

## Limits and pricing

The Actor uses pay-per-event pricing. Each delivered ad creates an `ad` event and a `creative_details` event. A successful optional advertiser-detail result creates an `advertiser_details` event. The table lists the live configured per-event price and the equivalent for 1,000 billable events; there is no 1,000-result minimum.

| Apify tier | Ad event | Ad events / 1,000 | Creative event | Creative events / 1,000 | Advertiser-detail event | Detail events / 1,000 | 1,000 ads with creative | Plus 1,000 successful details |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FREE | $0.00040 | $0.40 | $0.00010 | $0.10 | $0.00040 | $0.40 | $0.50 | $0.90 |
| BRONZE | $0.00036 | $0.36 | $0.00009 | $0.09 | $0.00036 | $0.36 | $0.45 | $0.81 |
| SILVER | $0.00032 | $0.32 | $0.00008 | $0.08 | $0.00032 | $0.32 | $0.40 | $0.72 |
| GOLD | $0.00030 | $0.30 | $0.000075 | $0.075 | $0.00030 | $0.30 | $0.375 | $0.675 |
| PLATINUM | $0.00030 | $0.30 | $0.000075 | $0.075 | $0.00030 | $0.30 | $0.375 | $0.675 |
| DIAMOND | $0.00030 | $0.30 | $0.000075 | $0.075 | $0.00030 | $0.30 | $0.375 | $0.675 |

Empty searches, discarded records, failed requests, and unavailable details do not create their corresponding events. Check the Actor's [Pricing tab](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata) and your spending limit before a larger run; account-level Apify terms can change.

The Actor accepts `maxAds` from 1 to 5,000 and `maxPages` from 1 to 500. Reaching the page budget before the ad limit or source end can leave a partial collection; inspect `collection.termination` and the run summary.

## Hosted version

Use the hosted Actor to run searches from the web interface, save results in an Apify Dataset, or call it through the API:

[Open Threads Ads Library Scraper on Apify](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata)

## Responsible use

Use public ad data lawfully and respect the source terms, applicable privacy rules, and your organization's policies. Never commit API tokens or other credentials to this repository.

## Support

For a problem with these examples, [open a GitHub issue](https://github.com/datacrawler-edu/threads-ads-library-scraper/issues) with the command, sanitized input, and error message. For an Actor run issue, contact support through the [Apify Actor page](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata) and include its run ID without sharing your token.

## License

This repository is released under the MIT License.
