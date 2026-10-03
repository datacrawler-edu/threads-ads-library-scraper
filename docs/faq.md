# FAQ

## Can I run the Actor without Python or code?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata), enter a keyword or Facebook advertiser page, click **Start**, then inspect or export the **Dataset**. See [`no-code-guide.md`](no-code-guide.md).

## Can I enter a Threads profile URL?

No. Use a keyword, numeric Facebook Page ID, public Facebook page URL, or exact Facebook page alias. Threads profiles, posts, and replies are not this Actor's input target.

## Are returned ads exclusive to Threads?

The Actor applies the Threads placement filter. Meta may report the same ad on several placements, so `publisher_platform` can also contain Facebook or Instagram. `collection.publisherPlatforms` records the fixed filter.

## Why did the search return no ads?

A complete successful empty search means the source returned no matches for that input at that time. A failed or partial run does not prove that there were no matches. Check the run status, `collection.termination`, and the run summary.

## Are advertiser details always available?

No. Details are optional and depend on what Meta returns. Check `enrichment.status`; unavailable or failed detail requests are not billed as successful advertiser-detail events.

## How is the Actor charged?

Each delivered ad creates an ad event and a creative-details event. Successful optional advertiser-detail results create a separate event. Current tier prices are on the [Actor Pricing tab](https://apify.com/datascraperes/threads-ads-library-scraper?fpr=edudata).

## Which exports are available?

The Dataset can be exported as JSON, CSV, or Excel. Use the Python CSV example when you want a flattened file with selected fields.
