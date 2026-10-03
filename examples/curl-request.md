# cURL request

Set `APIFY_API_TOKEN` in your shell, then run this command from the repository root. The bearer token stays in the HTTP authorization header instead of the URL.

Bash:

```bash
curl --request POST \
  "https://api.apify.com/v2/actors/datascraperes~threads-ads-library-scraper/run-sync-get-dataset-items" \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

Windows PowerShell:

```powershell
curl.exe --request POST `
  "https://api.apify.com/v2/actors/datascraperes~threads-ads-library-scraper/run-sync-get-dataset-items" `
  --header "Authorization: Bearer $env:APIFY_API_TOKEN" `
  --header "Content-Type: application/json" `
  --data-binary "@data/sample-input.json"
```

This synchronous endpoint waits for the Actor and returns the default Dataset items. Use the Apify client examples for longer jobs or when your integration needs the run ID and status.
