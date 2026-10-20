# Business isolation and configuration resolution

Every campaign, audience record, draft, approval, provider action and event must carry business_id. Campaign IDs are globally unique within this repository. Storage queries require both business_id and campaign_id where campaign-specific. An operator selects exactly one business for a run.

Business identity, sender, offers, proof and subscriptions are never inherited from another business. The owner managing both businesses is not recipient consent to hear from both. Suppression can have sender, business or all-owner scope; enforce the applicable union. Never remove an opt-out by moving a recipient between campaigns.

Order: core prohibitions → business restrictions → campaign restrictions → exact approved payload. The most restrictive applicable rule wins. A campaign cannot enable a sender disabled by business run control, increase an approved cap, invent consent or reuse another business's proof. Missing settings disable execution. A future implementation must enforce this server-side; these documents do not themselves provide row-level security.

Keep reusable procedure in core. Store business overlays and campaign facts separately. Record source of every resolved setting so reviewers know what changed. Version business facts/offers and invalidate approvals when relevant payload content changes.
