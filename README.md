# Sales OS

Reusable sales and email marketing system, with isolated business workspaces and campaign briefs. Current focus: email marketing. Status: instructions and validation tooling; external sending remains disabled.

| Area | Purpose |
| --- | --- |
| [Core](core/README.md) | Shared agents, skills, workflows, policies, templates, use cases and data contracts |
| [Businesses](businesses/README.md) | Each business's facts, offers, approvals, agents, memory and campaigns |
| [Campaign types](core/campaigns/types.json) | Reusable email campaign definitions |
| [Erudience](businesses/erudience/README.md) | Erudience's workspace and campaign registry |
| [Collaboration](governance/COLLABORATION.md) | Rules for concurrent chats and contributors |
| [Work board](governance/work-board.json) | Current scope and next tasks |

Start with [AGENTS.md](AGENTS.md), select a business, then a campaign. Read the resolved workflow and business overlay before drafting. No sender, audience, offer, proof or approval can be borrowed across businesses.

Use: "Read AGENTS.md. Use core/skills/sales-os/SKILL.md with business_id=erudience and campaign_id=CAMPAIGN-AU-TELECOM-2026. Audit the current state and prepare the next five actions. Draft only."

Validate with `python3 scripts/validate_repository.py`; run behavioural contract checks with `python3 -m unittest discover -s tests`.

Legacy links under erudience/ now lead to the canonical workspace. Do not rebuild the old directory tree. Private contacts, subscriber lists, message history and commercial records belong outside this public repository.
