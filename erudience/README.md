# Erudience Sales OS

Owner: Bishal Paul. Scope: Erudience's own partner-led sales. Version: 1.0, 20 October 2026.

## Start here

1. Read [AGENTS.md](AGENTS.md) and [business context](knowledge/business.md).
2. Read [current state](memory/current-state.md) before describing progress.
3. Use [the skill](skills/erudience-sales-os/SKILL.md) to route work.
4. Follow [the sales playbook](workflows/sales-playbook.md) and write private records using [the data model](operations/data-model.md).
5. Use [the runbook](operations/runbook.md) for daily operations and [the roadmap](ROADMAP.md) to activate integrations.

## What this provides

Six role instructions, one reusable routing skill, partner qualification and outreach procedures, discovery and proposal frameworks, pipeline rules, approval and suppression controls, integration contracts, operational memory and synthetic evaluation cases.

## Working assets

- [Australia telecom pilot brief](campaigns/australia-telecom.md)
- [Personalisation brief](templates/personalisation-brief.md)
- [Account brief](templates/account-brief.md)
- [Email sequence structure](templates/email-sequence.md)
- [Discovery record](templates/discovery-record.md)
- [Proposal checklist](templates/proposal-checklist.md)
- [Job card](templates/job-card.yaml)

## What is active

The system can guide an assistant working in an active session. This is an operating package, not a deployed CRM, autonomous agent service or email sender. No recurring job is enabled by this package. Research data is not imported into this public repository.

## Use in ChatGPT Work

Invoke the installed Erudience Sales OS skill, or attach its SKILL.md and relevant references. Ask: "Run Erudience Sales OS. Read current memory, inspect the connected private pipeline, prioritise existing incomplete leads and prepare the next five actions. Draft only."

If private data is unavailable, report that gap and work from owner-provided records; never invent a live pipeline. Six roles can run sequentially within one assistant. Separate running processes are not required.

## Use in Claude Code

Open this repository and say: "Read erudience/AGENTS.md and erudience/README.md. Use the Erudience Sales OS skill and playbook. Audit existing private data and integrations first. Complete the next unblocked roadmap task, validate it and update the status. Do not send outreach."

## Source of truth

GitHub holds versioned instructions and public-safe memory. A private CRM holds leads, correspondence, suppression, approvals and events. Reconcile by stable IDs. Never use chat memory as the only record of a sent message or a commercial agreement.
