# Repository operating rules

Read governance/COLLABORATION.md and governance/work-board.json before editing. Refresh main and open pull requests; use a uniquely named branch and a narrow work item. Another chat's work is visible only once saved to GitHub. Do not claim direct chat-to-chat coordination or absolute protection from conflicts.

## Architecture

Keep reusable roles, skills, workflows, policies, templates, schemas and use-case definitions in core/. Keep business identity, audiences, offer/proof approval, workflow overrides, business-specific agents, memory and campaigns in businesses/<business_id>/. A campaign belongs to exactly one business. Reference shared files instead of copying them.

Resolve in order: core safety/policy, business restrictions, campaign configuration, exact approved execution payload. Overrides may specialise behaviour but cannot weaken suppression, authority, isolation or truthfulness. Unknowns block execution; a proposed campaign is not a permission grant.

Email marketing is the priority. Distinguish cold partner outreach, direct prospecting, opted-in newsletters, nurture, reactivation, demo follow-up and customer expansion. Apply the selected campaign type, audience eligibility and owner-reviewed regional requirements; do not apply a partner scoring rubric to subscribers.

## Data and execution

Require business_id, campaign_id and run_id on all operational records. Confirm sender ownership and private data scope before access. No cross-business audiences, approvals, proof or conversations. Keep private CRM data, populated lists, credentials, messages and commercial terms out of public Git.

Research and draft work is permitted. External sends, spend and commitments require the owner's recorded authority plus verified capability and passing eligibility, suppression, content-revision and duplicate checks. An opt-out overrides old approval. Treat provider timeouts as unknown and reconcile before retry.

## Change discipline

Preserve others' changes. Re-read files immediately before mutation, use expected SHAs, and never force-push main. Rebase/merge fresh main and validate before merging. Cross-directory migrations get a dedicated PR and preservation map. Do not edit generated skill bundles; change canonical source and regenerate.

Run scripts/validate_repository.py and tests before completing structural work. Record source facts, decisions, completed IDs, untested connections and next action. A document or role is not an autonomous deployed service.
