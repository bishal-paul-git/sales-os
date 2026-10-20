# Architecture decisions

20 October 2026: the owner requested reusable Sales OS separate from multiple business workspaces in one repository, prioritising email marketing and detailed use cases/campaigns.

Core is business-agnostic procedure. Businesses supply identity, offers, knowledge, specialised roles, memory, restrictions and campaigns. Campaign types are reusable; campaign instances belong to a business. Use cases describe product/service workflows and are referenced by ID. Real audiences and activity stay private.

The migration begins from c612428960bf62ce55502f5c3bff07192d2e478b. The other chat's Australia telecom brief and six templates are preserved, as are its workflow changes. See migration-2026-10-20.json for exact paths. Eighteen duplicate skill reference files are replaced by direct canonical references. The installed skill distribution is generated outside this repository and is not a second editable source of truth.

Legacy erudience/README.md remains a navigation pointer. Future work must use core/ or businesses/. Cross-chat coordination requires each chat to read current GitHub state and use the shared protocol; unsaved work in another chat is not visible.
