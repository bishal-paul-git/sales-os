# Campaign contract

Each business registers campaigns in campaigns/index.json. Each entry points to exactly one campaign.json and strategy.md. Each campaign has a stable ID, one type and one business owner; use case IDs reference core/use-cases/catalog.json. A use case describes the customer workflow; a campaign describes who receives what message, why and when.

Required campaign fields: schema_version, campaign_id, business_id, type_id, name, status, audience, offer_ref, use_case_ids, core_workflow, business_workflow, agent_roles, sender_account_ref, private_audience_ref, sequence, metrics, activation, blockers and strategy_path.

Audience includes countries, industries, company_types, decision_roles, relationship, inclusion, exclusion and eligibility_evidence. Unknowns must be explicit. Do not populate a private audience in the public brief.

Sequence steps define id, purpose, delay_business_days and trigger. Each draft adds exact recipient, sender, content revision/hash, personalisation evidence and review decision privately. Metrics define unit and denominator. Activation starts enabled=false with approval_required=true and daily_send_cap=0. Business restrictions remain authoritative.

Statuses: proposed, validation, drafting, review, approved, active, paused, completed, archived. No status alone grants execution. Only enabled, approved and fully resolved campaigns with passing runtime gates may execute. Record launch/pause decisions with actor and date in the private event store.

Preserve an existing campaign ID during migration. Register one canonical campaign per business/market/audience/objective; test variants belong under that campaign rather than duplicate campaigns. Use templates/campaign-strategy.md for strategy details and campaign.json for machine-readable fields.
