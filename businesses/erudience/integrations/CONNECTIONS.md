# Connections and activation contracts

Status checked 20 October 2026 for this task. No live sales-provider execution tests were performed.

| Function | Current evidence | Activation requirement |
| --- | --- | --- |
| GitHub | sales-os accessible, public, initially empty | Save public-safe instructions only |
| Prospect source | Saved Telecom Partner Lead Dashboard read | Private staging import and reconciliation |
| Apify | Connection discussed; no Apify tools exposed here | Connect account, inspect available tools, test bounded read/run and results |
| Email verification | No verification results established | Select existing licensed provider, record verdict and timestamp |
| Sender | Exact outbound sender not confirmed | Confirm mailbox, account, identity, draft/read/send capabilities |
| Private CRM | No CRM selected or queried in this task | Choose existing system, validate permissions and stage mapping |
| Scheduler/worker | None deployed or enabled | Select owner-controlled scheduler, scoped credentials and monitored job |
| Booking/demo | Destinations not tested | Owner-approved links, fictional demo data, verify access |

## Apify

Reference: https://docs.apify.com/integrations/chatgpt and https://docs.apify.com/integrations/mcp. Historic setup discussed endpoint https://mcp.apify.com with OAuth. Verify current account eligibility and provider documentation at connection time; do not rely on old plan/UI instructions.

Treat Apify as a data collection tool. Inspect Actor input/output and current cost before running. Begin with a five-domain pilot, explicit spend cap and no purchased batch until authorised. Record Actor ID/version, input hash, run ID, dataset ID, records count and cost when available. Do not treat Actor output as verified merely because collection succeeded. Validate against official sources and import privately with provenance.

Some Actors offer enrichment or technical verification, but availability/prices/results depend on the selected Actor. Confirm actual output and verdict semantics. Stop on rate-limit or provider rejection. Do not scrape behind authentication or use third-party credentials without approved access.

## Sender and CRM

Prefer existing owned tools; n8n is not required. A connected email app can support supervised work if its operations are verified. An external worker is needed for durable unattended execution; choose it only after a supervised pilot works.

Confirm exact sender and return path, authorised identity, authentication/deliverability configuration, inbox access, event tracking and opt-out process. Validate with owner-controlled test recipients before a real campaign. Campaign requirements vary by jurisdiction; owner review must precede activation. Never publish credentials or contact exports.

CRM read test: resolve five records and IDs. Write test: create/update a synthetic record in an approved test area, verify it and remove/archive as agreed. Sender test: create and inspect a draft, then send only an explicitly authorised test and verify provider ID and destination.

## Unattended execution, later

Choose one owner platform per sending lane. Use a private worker with transactional action reservation, scoped secrets, bounded retries, suppression processing, webhook authentication, alerting and pause controls. Store jobs and events durably. Schedule by recipient timezone. Complete failure/replay tests before enabling an owner-approved cap. This document does not implement or deploy that service.
