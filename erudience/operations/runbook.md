# Operations and recovery

## Before each run

Read current instructions and run control. Resolve the private CRM and sender account, verify the campaign and owner platform. Review new suppressions and replies first. Check outstanding actions with unknown outcomes before creating new sends. Record run ID, scope and cap.

## Daily active-session routine

1. Process replies, opt-outs, complaints and bounces.
2. Review due follow-ups and agreed actions; draft responses.
3. Finish verification of existing high-fit leads.
4. Prepare a small reviewed approval batch.
5. Execute only approved actions and reconcile provider results.
6. Update private memory: decisions, events, next actions and blockers.

No recurring run exists until a real scheduler and worker are configured and tested. ChatGPT roles do not keep running after a conversation merely because these files exist.

## Action state machine

prepared → reserved → attempted → confirmed, failed, or unknown. Unknown cannot re-enter attempted without provider reconciliation. Check provider sent items or query by external request ID. If a message exists, store its ID and confirm. Retry only after evidence establishes no send occurred, with the original deduplication key and bounded retry policy.

Stop on wrong sender/recipient, expired approval, suppression, missing contact evidence, authentication failure, exhausted budget, unexpected provider behaviour or ambiguous writes. Save a blocked record and the smallest corrective task. Never silently switch account/provider or weaken gates to complete a batch.

## Weekly report

Report eligible leads, qualification backlog by missing gate, unique contacted, provider-accepted, delivered, human replies, positive replies, meetings booked/held, opportunities, proposals and won/lost. Define each denominator and date window. Show bounces/complaints, cost where measured and outstanding unknown actions. Do not infer delivery from acceptance or include synthetic fixtures.

## Durable memory

Private memory: decision log with source/date/scope; campaign summary; relationship history; suppression; event log; task list. Public memory: system decisions and anonymised status only. At session start, read authoritative current records. At session end, persist changes through authorised tools; if unavailable, give a proposed update and mark not saved. Never claim chat-only memory updates changed the CRM.
