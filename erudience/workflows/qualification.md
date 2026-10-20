# Partner qualification

## Fit rubric: 100 points

Score evidence, not enthusiasm. Unknown earns zero until established.

| Criterion | Points |
| --- | --- |
| Demonstrated customer relationships in the target market | 0–25 |
| Complementary telecom, IT, CRM, agency or advisory services | 0–25 |
| Explicit partner/reseller programme or evidenced collaboration | 0–20 |
| Specific feasible use case for that partner's customer audience | 0–20 |
| Named relevant commercial decision-maker | 0–10 |

Proposed defaults: 80+ high fit, 60–79 review, below 60 hold. Scores never override gates. Existing spreadsheet scores used a historic rubric and must not be silently compared with this version.

## Draft gates

Confirm business relevance, a source-backed partner angle and no unresolved direct conflict. Draft may use a role placeholder, clearly labelled and unsendable.

## Sending gates: all must pass

1. Target market and partner fit approved for the campaign.
2. Official website validates relevant services.
3. Named relevant decision-maker confirmed, with the exact recipient route; generic routing exception requires explicit approval.
4. Active legal entity verified and matched.
5. Technical email verification is deliverable and within the campaign freshness window; default maximum 30 days, recheck after bounce or material change.
6. Competing offer review clear or owner-approved exception. Absence on reviewed pages is limited evidence, not proof none exists.
7. Suppression checked immediately before sending; recipient basis and applicable campaign requirements reviewed by the owner.
8. Exact sender, content revision, recipient and action approved.
9. Connected sender tested; deduplication key not used; spend and volume limits permit execution.

Default evidence freshness: team, entity and competitor checks within 30 days of the first send. Campaign rules can tighten this. Store checked_at and expires_at. Never label expired evidence current.

## Import rules

Import spreadsheets into a private staging area with source/version. Preserve source record IDs and raw status. Recompute status from evidence instead of trusting labels or scores. Flag contradictions such as Contact validation=Validated with no named contact, or Company=Validated with notes saying entity unknown. Keep exclusions and suppression during merge.
