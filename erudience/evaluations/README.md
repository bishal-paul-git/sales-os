# Acceptance scenarios

Use scenarios.json as behavioural checks before activating a sender or changing readiness rules. All cases are synthetic. Ask the operator for its next action and compare with the expected decision. Record actual outputs and review failures. Do not describe a schema check as a behavioural pass.

Before automation, also simulate duplicate provider webhooks, two workers reserving one action, token expiry, CRM unavailability, out-of-order events and sender account mismatch. These integration tests need a real implementation and are not completed by this instruction package.
