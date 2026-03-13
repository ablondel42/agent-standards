# approvals

## Use this file when
The task may exceed routine implementation authority and could require explicit approval before proceeding.

## Goal
Prevent agents from making high-impact changes without clear authorization.

## Approval is required before changing
- Authentication, authorization, permissions, roles, or session behavior
- Secret handling, environment usage, credentials, token flows, or sensitive operational access
- Logging destinations, telemetry scope, analytics behavior, consent flows, retention, or privacy-sensitive collection
- Public APIs, schema design, migration strategy, deployment configuration, or externally significant file moves
- Security posture, trust boundaries, CSP, cookies, headers, proxy behavior, or sandboxing rules
- Third-party integrations, external embeds, payment behavior, or compliance-relevant flows
- Data deletion behavior, irreversible operations, or user-visible breaking changes

## Approval decision rule
If a change could materially affect security, privacy, compliance, infrastructure safety, user trust, external integrations, or backward compatibility, do not treat it as routine.

## What to do instead
When approval is needed:
1. Stop before implementing the risky change.
2. Explain what change is being considered.
3. Explain why it needs approval.
4. Describe the smallest safe path forward.
5. Wait for explicit confirmation before proceeding.

## Escalation output format
When escalation is required, stop and emit a structured block before any implementation:

```text
ESCALATION REQUIRED
Trigger: [what rule or boundary was reached]
Proposed change: [one sentence description]
Risk: [why this needs approval]
Awaiting: explicit approval before proceeding
```

Do not implement the change until this block is acknowledged.

## Safe defaults
- Prefer preserving current behavior over making risky assumptions.
- Prefer narrower changes over broad policy shifts.
- Prefer asking for approval over retroactively justifying a sensitive change.

## Avoid
- Treating “probably fine” as approval
- Hiding risky changes inside broader implementation work
- Making irreversible or externally impactful changes by default
- Assuming a change is safe just because it is technically simple
