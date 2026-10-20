---
name: sales-os
description: Run a multi-business sales and email marketing workspace. Use to plan campaigns, qualify audiences, draft email sequences, review replies and opportunities, or maintain Sales OS architecture without mixing business identities.
---

# Sales OS

Use this skill inside the sales-os repository. Find the repository root from AGENTS.md and README.md; do not assume paths are relative to the current directory.

Read root AGENTS.md, governance/COLLABORATION.md and governance/work-board.json. Resolve business_id and campaign_id from the request or current campaign registry. If ambiguous, inspect registries and prepare an explicit scoped proposal; do not send or access another business's private data.

Load businesses/<business_id>/AGENTS.md, knowledge/business.md, config/run-control.json and memory/current-state.md. Load its campaign.json and strategy.md. Read core/campaigns/CONTRACT.md, core/campaigns/types.json and core/policies/email-eligibility.md. Route via core/agents/README.md and core/workflows/email-marketing.md. Load only the role and workflow needed.

Reference canonical files. Do not duplicate shared roles, skills or templates inside business folders. Business agents specialise offers and knowledge; campaign documents specialise targets, message strategy and success measures.

Distinguish verified facts, owner statements, hypotheses and unknowns. Preserve source dates, audience eligibility, unsubscribe/suppression state and exact content approval. Keep live records in a private business-scoped store. Writing a campaign does not enrol anyone or activate automation.

Before any execution, resolve the effective business and campaign restrictions, exact sender/recipient/content revision, approval and duplicate key. Fail closed on missing capability or evidence. Hold unknown provider outcomes for reconciliation. Return completed work, source evidence, saved status, blockers and the next scoped action.
