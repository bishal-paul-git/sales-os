# Private CRM data contract

Implement in an existing private CRM or approved database. These are field contracts, not deployed tables. Use stable UUIDs, UTC timestamps and source timezone for appointments. A CSV pilot may follow the same fields. Do not put populated records in public GitHub.

| Record | Required fields |
| --- | --- |
| Campaign | id, name, market, ICP_version, offer_version, owner, state, limits, evidence_freshness_days |
| Company | id, canonical_domain, name, country, partner_type, legal_entity, fit_breakdown, conflict_status, owner, source_version |
| Contact | id, company_id, name, role, decision_scope, email, route_type, source, checked_at, verification_provider/result/checked_at, routing_exception_id |
| Evidence | id, company_id/contact_id, criterion, source_url, observed_at, expires_at, fact, confidence, evidence_type |
| Opportunity | id, company_id, campaign_id, stage, stage_entered_at, owner, next_action, next_action_due, amount/currency nullable, commercial_approval_id |
| Draft | id, opportunity_id, channel, recipient, sender, subject, body, revision, content_hash, claim_ids, review_state |
| Approval | id, draft_id, revision, content_hash, recipient, sender, action, approver, approved_at, expires_at, revoked_at |
| Suppression | id, normalised_email/domain/contact_id, scope, reason, source, effective_at |
| Action | id, campaign_id, draft_id, idempotency_key, state, attempted_at, provider_id, error, reconciled_at |
| Event | id, entity_type, entity_id, actor, occurred_at, event_type, prior_state, new_state, evidence_id, run_id |
| Run | id, trigger, owner_platform, scope, started_at, completed_at, result, blockers, cost/currency nullable |

## Normalisation and integrity

Canonical domain: lowercase hostname, remove www and trailing dot; retain original URL and resolve redirects before merging. Email: trim and normalise for lookup; keep original provider address. Never merge companies solely because names match. Alias domains need evidence.

Foreign keys must resolve. Require one current opportunity owner and due action for each active opportunity. Approval is invalid after any change to recipient, sender, body, subject or attachments. Store content hashes over the complete approved payload. Effective suppression always overrides prior approval.

In a database, use uniqueness on idempotency_key and provider event ID, scoped to provider/account. Reserve actions transactionally before execution; a spreadsheet alone cannot guarantee concurrent-send safety. Scope email access and row permissions to the agency. Log meaningful changes, limit access, define retention/deletion with the owner and remove unnecessary personal data.

## Stages and orthogonal states

Opportunity: researched → qualifying → draft_ready → approval_pending → approved → contacted → engaged → discovery → proposal → closed_won or closed_lost. Hold is allowed from any pre-close stage with reason. Each transition requires evidence, actor and time. A provider acceptance moves to contacted; delivery is a separate event. Human reply plus intent review moves to engaged. Sent is not delivered; booked is not held; interested is not won.

Keep qualification, approval, delivery, reply intent and suppression separate from opportunity stage. Suppressed records cannot send regardless of stage. Contact updates do not erase prior messages or exclusions.

## Multi-business email extension

Add business_id to every record, and campaign_id for campaign-specific records. Partition queries, uniqueness and provider account mapping by business. Add Subscription records: id, business_id, contact_id, purpose, source, captured_at, permission_state, preference_version and withdrawn_at. Add CampaignEnrollment: id, business_id, campaign_id, contact_id, eligibility_evidence_ids, sequence_revision, current_step, state and stop_reason. Store use_case_ids and offer revision on campaigns. Suppression may have business or all-owner scope; apply the appropriate union.

Pipeline stages describe opportunities, not every newsletter subscriber. Track subscriber state and campaign delivery separately; do not create a sales opportunity merely because someone subscribed. A confirmed human reply can create a reviewed task; qualification still precedes an opportunity stage change.
