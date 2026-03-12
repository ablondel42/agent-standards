# forbidden-patterns

## Use this file when
You want examples of behaviors and implementation patterns that should be treated as warning signs or outright mistakes.

## Goal
Make high-risk anti-patterns easy to recognize before they ship.

## Forbidden or high-risk patterns
- Making broad rewrites to solve a narrow problem
- Adding dependencies without approval
- Weakening validation, auth, privacy, or security controls for convenience
- Logging secrets, tokens, personal data, or sensitive operational details
- Returning raw internal errors directly to end users
- Swallowing exceptions or adding silent fallbacks with no diagnostic value
- Marking work complete when validation failed or was skipped without disclosure
- Changing externally meaningful behavior without calling it out
- Creating large always-on instruction files instead of modular retrieval paths
- Duplicating shared guidance into multiple role files without reason
- Writing vague plans that hide uncertainty and expand scope
- Treating “probably safe” as if it were a verified fact

## Warning signs
Be especially cautious when you notice:
- a task suddenly touching many unrelated files
- a proposed fix that depends on disabling checks
- new complexity with no clear user or maintenance benefit
- reduced debuggability in the name of simplicity
- broad cleanup work mixed into a risky change
- confidence claims that are not backed by validation

## Safer alternatives
- Prefer the smallest safe change.
- Prefer explicit disclosure over false certainty.
- Prefer shared guidance for shared concerns.
- Prefer targeted validation over broad assumptions.
- Prefer approval requests over risky guesses.
