# Input reference

Provide at least one search target: `query`, `pageId`, or `pageUrl`. The Actor searches Meta Ad Library with the Threads placement filter. A page target is a Facebook advertiser page; Threads profile URLs are unsupported.

| Field | Type | Required | Default / allowed values | Description |
| --- | --- | :---: | --- | --- |
| `query` | string | Search target | empty | Brand, advertiser, product, or phrase. |
| `pageId` | string | Search target | empty | Numeric Facebook Page ID. Do not paste a URL here. |
| `pageUrl` | string | Search target | empty | Public Facebook page URL or exact page alias. |
| `country` | string | No | `ES` | Two-letter market code such as `ES`, `US`, `GB`, or `FR`, or `ALL`. |
| `activeStatus` | string | No | `ACTIVE`, `INACTIVE`, `ALL` | Delivery-status filter. |
| `mediaType` | string | No | `ALL`, `IMAGE`, `VIDEO`, `NONE` | Creative media filter. |
| `adType` | string | No | `ALL`, `EMPLOYMENT_ADS`, `FINANCIAL_PRODUCTS_AND_SERVICES_ADS`, `HOUSING_ADS`, `POLITICAL_AND_ISSUE_ADS` | Meta special-category filter; availability depends on market. |
| `contentLanguages` | string array | No | empty | Meta Ad Library language codes. Empty includes every language. |
| `startDate` | string | No | empty | Earliest ad start date, `YYYY-MM-DD`. |
| `endDate` | string | No | empty | Latest ad start date, `YYYY-MM-DD`. |
| `maxAds` | integer | No | `100`, range 1-5,000 | Maximum unique ads to deliver. |
| `maxPages` | integer | No | `100`, range 1-500 | Pagination safety limit. A reached page budget can produce a partial collection. |
| `includeDetails` | boolean | No | `false` | Request optional advertiser transparency and page details. Successful returned details create a billable event. |
| `detailsLimit` | integer | No | `25`, range 1-5,000 | Maximum ads for which details are requested. Used only when enrichment is enabled; unavailable or failed detail requests count toward this cap. |

The full small input is [`../data/sample-input.json`](../data/sample-input.json). Its property names match the Actor input schema.
