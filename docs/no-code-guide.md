# Run Threads Ads Library Scraper without code

You can run the hosted Actor in Apify Console without installing a client.

## Step by step

1. Open [Threads Ads Library Scraper](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata).
2. In **Input**, enter a keyword, numeric Facebook Page ID, or public Facebook page URL/alias. Provide at least one search target.
3. Select the country. Optionally set active status, media type, special ad category, language, dates, `maxAds`, and `maxPages`.
4. Leave **Enrich ad details** off for a basic search. Turn it on only if you need advertiser transparency and page details; successful returned detail payloads are billed separately.
5. Click **Start**. When the run completes, open **Dataset** and export JSON, CSV, or Excel.

## Small first search

Use [`../data/sample-input.json`](../data/sample-input.json) for a one-ad search. Results depend on what Meta currently returns; the example does not guarantee that a matching ad will be available each time.

## Read completeness and detail status

Each ad item has a `collection` object with counters and a `termination` value. `page_budget` means the configured page limit ended collection before the source was exhausted or the ad cap was reached. Check the run summary for final status. Optional detail outcomes are reported in `enrichment.status`; missing or failed details are not the same as an empty main search.

## Pricing

The Actor charges for delivered ad and creative events. A successful optional advertiser-detail response adds its event. See the current [Actor Pricing tab](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata) before a larger run.
