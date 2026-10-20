# Shared integration contracts

Resolve the selected business before accessing a provider. Business connection evidence belongs in businesses/<business_id>/integrations/ and its run control. No provider or sender is inherited across businesses.

For research/enrichment, verify the permitted data scope, Actor/tool input and output, source provenance, exact spend cap and current provider terms before running. Technical collection success is not contact qualification.

For a CRM, require business-scoped storage, campaign mappings, suppression, approval records, transactional action reservation and event history. Test with synthetic records in an authorised test area.

For email, confirm exact business account, identity, approved scope, delivery/authentication configuration, reply access, opt-out handling and provider event semantics. Test drafts first, then send only an explicitly authorised owner-recipient test and reconcile its provider ID.

For durable automation, assign one worker owner per lane, store jobs and events privately, use bounded retries, verify incoming event authenticity and provide pause/alert controls. Reconcile ambiguous writes before retry. Instructions do not create a running scheduler.

Keep credentials in provider OAuth or a secret manager. Recheck current API documentation, cost and plan eligibility at connection time. Save only public-safe evidence here.
