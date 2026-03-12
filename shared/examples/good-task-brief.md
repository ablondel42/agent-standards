# good-task-brief

## Use this file when
You need an example of a well-scoped task brief for an agent.

## Goal
Show what a clear, high-signal task request looks like so implementation starts with the right scope, constraints, and expectations.

## A good task brief should include
- the problem to solve
- the desired outcome
- the relevant constraints
- any explicit non-goals
- any important safety or approval boundaries
- the expected validation level if known

## Good example
Update the account settings save flow so duplicate submissions are prevented while a request is in flight.

Constraints:
- Preserve the current API contract.
- Do not change analytics behavior.
- Reuse the existing button and form patterns.
- Keep the diff limited to the settings form flow unless a small shared fix is clearly necessary.

Validation:
- Update or add relevant tests.
- Verify the form disables correctly during submission.
- Verify the user still sees a useful error state if the request fails.

## Why this is good
- The user-facing outcome is explicit.
- The scope is narrow.
- Safety boundaries are named.
- Validation expectations are clear.
- The brief gives enough direction without prescribing the full implementation.

## Weak brief example
Fix the settings page.

## Why this is weak
- The problem is ambiguous.
- The expected result is unclear.
- There are no constraints.
- It invites scope expansion and guesswork.
