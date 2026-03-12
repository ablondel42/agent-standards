# observability-and-logging

## Use this file when
The task affects logging, monitoring, metrics, tracing, failure reporting, debugging signals, diagnosability, or error handling behavior.

## Goal
Preserve useful operational visibility without creating noisy, unsafe, or privacy-harming diagnostics.

## Core rules
- Preserve useful error context.
- Keep logs actionable and appropriately scoped.
- Catch errors at the boundary where they can be handled meaningfully or enriched with useful context.
- Re-throw, surface, or explicitly return failures when they cannot be handled safely locally.
- Distinguish expected failures from unexpected system failures.
- Keep logging patterns consistent across similar code paths.

## Error handling rules
- Do not add broad catch blocks that hide root causes.
- Do not convert actionable failures into vague fallbacks without clear intent.
- Do not silently ignore exceptions.
- Prefer one clear handling path per failure mode instead of scattered ad hoc handling.
- Preserve debuggability even when simplifying user-facing output.

## Logging rules
- Log for diagnosis, not noise.
- Include stable, non-sensitive context such as subsystem, action, and failure point when useful.
- Keep message shape and terminology consistent for similar events.
- Avoid duplicate logging of the same failure across multiple layers unless the duplication is intentional and adds value.
- Do not leak secrets, credentials, tokens, personal data, or protected internal details into logs.

## Escalation rules
Load additional risk guidance when:
- logging touches personal or regulated data
- telemetry destinations or retention may change
- user-visible error handling may affect trust or supportability
- instrumentation could change privacy or compliance behavior

## Avoid
- Empty catch blocks
- Catch-and-ignore behavior
- Opaque error messages with no diagnostic value
- Verbose logging with no operational purpose
- Sensitive data in logs, traces, metrics, or error payloads
