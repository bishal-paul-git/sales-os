# Connections and activation contracts

Status checked 23 October 2026. Account discovery and bounded read-only checks were completed. No campaign email, verification lookup or provider write was executed during setup.

Public files use stable aliases only. Provider link IDs, Drive file IDs, credentials, live records, email verdicts and message history remain private.

| Function | Current evidence | Activation requirement |
| --- | --- | --- |
| GitHub | `sales-os` is accessible and public | Save public-safe instructions and status only |
| Private audience | `private://erudience/partner-leads` resolves to an owned Google Sheet; the expected 28-column header schema exists but there are zero populated records | Owner supplies or shares the latest 42/47-record workbook; import to staging, reconcile versions and preserve provenance and suppressions |
| Email verification | `rocketreach:erudience-primary` returned a registered Erudience account with 10 verification credits available at check time | Owner authorised at most five credits for the pilot; run only after the five records are selected, store verdict and timestamp privately, and never treat catch-all or unknown as valid |
| Sender | `hostinger-mail:erudience-founder` resolves to the selected `bishal@erudience.com` mailbox; account discovery succeeded | Confirm display name, return path, inbox access and deliverability; send only an explicitly approved owner-controlled test before any prospect email |
| Private CRM | Google Sheets is selected as the supervised staging store; header read succeeded and writes remain disabled | Import the supplied source, validate row mapping, write a synthetic record only with approval, and reconcile it before enabling writes |
| Scheduler/worker | None deployed or enabled | Select an owner-controlled platform only after the supervised five-record pilot works |
| Booking/demo | Destinations not tested | Use owner-approved links and fictional demo data; verify every destination before sending |

Other connected personal or client Gmail accounts are excluded from this Erudience campaign lane. A connected account is not automatically an approved sender.

## Private audience contract

The private Google Sheet is the campaign staging destination, not yet the source of truth. Its visible tab is `Partner Leads` and its current schema covers company, fit, named contact, work email, verification, sources, outreach state, replies, suppression and notes.

When the latest workbook is supplied:

1. Record source filename, modified date, version and import run ID privately.
2. Compare the 42-record and 47-record claims rather than choosing one by recency alone.
3. Preserve raw source values and exclusions, then recompute fit and readiness under the current shared qualification workflow.
4. Deduplicate by stable source ID where available, then by normalised company domain and person identity.
5. Select five high-fit records with complete evidence. Do not add new discovery records until the existing candidates are resolved.
6. Keep the public campaign reference null until a populated, reconciled private audience exists.

## RocketReach verification contract

Use one verification credit per selected pilot address, up to five credits total under the recorded owner authorisation. Record the provider, checked time, address hash or private record ID, status, individual checks and freshness expiry in the private sheet or event store.

- `valid`: eligible to continue through the remaining gates.
- `invalid`: suppress that route and do not send.
- `catchall`: hold for manual evidence; do not assume deliverability.
- `unknown`: hold; at most one later retry if it is still useful.

The account balance observed during discovery is not a standing budget or permission for later batches.

## Sender contract

The selected lane is founder-led partner outreach from `bishal@erudience.com` through the Hostinger connection. Keep campaign sending disabled until all of the following pass:

1. Confirm the display name, signature, reply-to and monitored inbox.
2. Review SPF, DKIM and DMARC evidence outside the public repository.
3. Send one explicitly approved test to an owner-controlled recipient and reconcile the provider response.
4. Confirm the message arrives, replies return to the monitored inbox and suppression can be applied before another send.
5. Approve the exact five recipients, content revisions, cadence, regional requirements and daily cap.

Hostinger exposes direct send rather than an unsent-draft workflow here. Therefore the first provider write must be an owner-approved test, not a prospect draft.

## Unattended execution, later

Choose one owner platform per sending lane. Use a private worker with transactional action reservation, scoped secrets, bounded retries, suppression processing, webhook authentication, alerting and pause controls. Store jobs and events durably. Schedule by recipient timezone. Complete failure and replay tests before enabling an owner-approved cap. This document does not implement or deploy that service.
