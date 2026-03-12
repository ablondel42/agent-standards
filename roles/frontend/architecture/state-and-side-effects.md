# frontend/architecture/state-and-side-effects.md

## Use this file when
The task affects state ownership, async flow, retries, side effects, optimistic updates, or race conditions.

## Rules
- Keep state as local as practical.
- Make side effects explicit and easy to trace.
- Handle cancellation, stale data, duplicate submissions, and race conditions where relevant.
- Avoid hidden network calls or mutations inside generic helpers that obscure behavior.
- Keep optimistic updates conservative unless a proven safe pattern already exists.
