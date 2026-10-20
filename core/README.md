# Shared Sales OS

This layer contains reusable procedures, not a business identity. Supply a business_id and campaign_id before using it.

- [Routing skill](skills/sales-os/SKILL.md)
- [Six shared agent roles](agents/README.md)
- [Email marketing workflow](workflows/email-marketing.md)
- [Partner qualification](workflows/qualification.md)
- [Campaign types](campaigns/types.json) and [campaign contract](campaigns/CONTRACT.md)
- [Eligibility and approval rules](policies/email-eligibility.md)
- [Use-case library](use-cases/catalog.json)
- [CRM data contract](operations/data-model.md)
- [Business separation](policies/business-isolation.md)

Templates are blank working structures. A campaign references a template and adds its business context; it does not maintain a fork of core instructions. Examples are synthetic. Core does not contain live campaign performance or connection credentials.
