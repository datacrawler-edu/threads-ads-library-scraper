# Use cases

## Research competitors advertising on Threads

Set `query` to a competitor name, choose a market, and select an appropriate `activeStatus`. Review `creative.texts`, `creative.title`, `creative.ctaType`, and `creative.linkUrl`. The fixed Threads placement filter is recorded in `collection.publisherPlatforms`.

## Compare image and video formats

Run one search with `mediaType: "IMAGE"` and another with `mediaType: "VIDEO"`. Compare `creative.format`, `creative.imageUrls`, and `creative.videoUrls`. The source can return several records for the same advertiser; `ad_archive_id` identifies each deduplicated ad.

## Review ads from one Facebook advertiser page

Supply `pageId` or `pageUrl` instead of `query`. Use the advertiser page associated with the ads; Threads profile URLs are outside this Actor's input contract. Inspect `page_name` and the placement list on every returned ad.

## Add available advertiser transparency details

Set `includeDetails` to `true` and choose `detailsLimit`. Review `details` and `enrichment.status`. Only a successful returned details payload creates the optional advertiser-details event; unavailable or failed detail responses do not.
