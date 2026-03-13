# scope-and-safety

## Use this file when
The task may expand beyond its original boundary, affect risky systems, or require explicit approval before changes are made.

## Goal
Keep work within the requested scope while protecting security, privacy, correctness, and externally meaningful behavior.

## Scope rules
- Solve the requested problem, not every related problem you notice.
- Prefer the smallest safe change that addresses the real need.
- Do not turn focused tasks into broad refactors without approval.
- Separate optional improvements from required work.

## Safety rules
This file is the canonical source for cross-role safety boundaries.
Role-specific guidelines may summarize these rules, but they should reference this file rather than duplicate the full list.

Do not make the following changes without explicit approval:
- Dependency additions, removals, or upgrades
- Authentication, authorization, permissions, or session behavior changes
- Environment variable, secret, token, or credential handling changes
- Telemetry, logging destination, consent, retention, or privacy-sensitive collection changes
- Public API changes, externally significant file moves, schema changes, or deployment-impacting configuration changes
- Security headers, CSP, cookie behavior, proxy behavior, or trust-boundary changes

## Risk handling
When a task touches a risky area:
1. Slow down and inspect the surrounding system carefully.
2. Load the relevant shared risk guidance before editing.
3. Avoid making assumptions about safe behavior.
4. Escalate when the risk exceeds the task’s explicit scope or authority.

## Canonical escalation triggers
This file is the canonical source for escalation triggers across the shared core layer.

Escalate when:
- approval is required by policy or task constraints
- the task conflicts with safety rules
- the request is ambiguous in a way that changes implementation meaningfully
- validation is blocked
- multiple risky interpretations are possible
- the task touches security, privacy, auth, secrets, compliance, or externally meaningful behavior beyond clearly granted scope

## Decision rule
If a change is technically possible but may create security, privacy, compliance, production, or user-impact risk, do not proceed as if it is routine.

## Avoid
- Silent scope expansion
- Risky changes disguised as cleanup
- Assuming approval where none was given
- Weakening safeguards for convenience
