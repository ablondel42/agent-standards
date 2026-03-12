# secrets-and-sensitive-data

## Use this file when
The task touches secrets, credentials, tokens, keys, certificates, environment variables, internal identifiers, or other sensitive operational data.

## Goal
Prevent exposure, unsafe handling, or accidental propagation of sensitive values.

## Core rules
- Treat all secrets and sensitive operational values as highly restricted.
- Do not log, print, echo, serialize, or expose secrets in user-visible outputs.
- Do not hardcode secrets, credentials, or real operational identifiers in code, tests, docs, or examples.
- Do not move sensitive values into less protected locations for convenience.
- Minimize the number of places where a sensitive value is accessed or transformed.

## Handling rules
- Prefer existing secret-management patterns over inventing local workarounds.
- Use the narrowest possible scope when accessing sensitive values.
- Redact or omit sensitive fields in logs, telemetry, and debugging output.
- Avoid passing secrets through unnecessary intermediate layers.
- Preserve existing protection boundaries around credentials and environment access.

## Review prompts
Before finalizing a change, check:
- Could a secret leak into logs, errors, screenshots, telemetry, or client-visible responses?
- Was a sensitive value copied into tests, fixtures, examples, or comments?
- Did the change widen access to an operational secret?
- Did the change make rotation, revocation, or auditing harder?

## Approval expectations
Changes involving secret handling, credential flow, environment usage, or protected operational access should be treated as approval-sensitive by default.

## Avoid
- Hardcoded credentials
- Secrets in logs
- Secrets in test fixtures copied from real environments
- Debug output that reveals protected values
- Convenience shortcuts that weaken secret boundaries
