# Output reference

The default Dataset contains one item per deduplicated Meta ad. The full source snapshot and normalized creative can contain additional values when Meta returns them.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `ad_archive_id` | string | Yes | Meta Ad Library ID used for deduplication. |
| `is_active` | boolean or null | No | Whether Meta reports the ad as active. |
| `page_name` | string or null | No | Advertiser's Facebook Page name. |
| `publisher_platform` | string array | No | Platforms reported for the ad; may include multiple platforms. |
| `snapshot` | object or null | No | Original Meta snapshot, when returned. |
| `creative` | object | Yes | Normalized title, text, format, CTA, destination, media URLs, cards, and advertiser-page fields when available. |
| `details` | object | No | Optional transparency, payer/beneficiary, audience, regional, and page details. |
| `enrichment.status` | string | No | Optional enrichment result: `enriched`, `no_data`, `skipped`, or `failed`. |
| `collection` | object | Yes | Search filters, pagination limits, deduplication counters, and termination state. |
| `sourceUrl` | URI | Yes | Direct Meta Ad Library link for the ad. |
| `scrapedAt` | date-time | Yes | UTC time when the Dataset item was assembled. |

A nullable field can be `null` when Meta did not provide a value. `creative.videoUrls` contains video file URLs; video preview images are separate media references. The Key-value Store run summary reports final completion and termination details.
