# bugfix

## Use this file when
The task is to fix broken behavior, regressions, edge cases, production defects, or incorrect UI state.

## Goal
Fix the issue with the smallest safe change while preserving existing architecture, user expectations, and production safety boundaries.

## Workflow
1. Reproduce or clearly define the failing behavior.
2. Identify the narrowest code path responsible for the bug.
3. Inspect nearby patterns, related tests, and similar logic before editing.
4. Fix the root cause, not just the visible symptom, unless the task explicitly asks for a temporary mitigation.
5. Add or update tests for the failing behavior when tests should exist.
6. Validate the fix with the smallest relevant checks first.
7. Confirm the change does not create regressions in adjacent states.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/scope-and-safety.md`
- `shared/core/definition-of-done.md`
- `shared/risk/security-and-privacy.md` if the bug touches auth, user data, trust boundaries, or sensitive flows
- `shared/risk/observability-and-logging.md` if better diagnostics or error handling are needed
- `roles/frontend/quality/testing.md`
- `roles/frontend/architecture/state-and-side-effects.md`
- `roles/frontend/architecture/data-fetching.md`

## Priorities
- Correctness before elegance
- Root-cause fixes before cosmetic cleanup
- Minimal diff before opportunistic refactor
- Production safety before speed

## Avoid
- Broad rewrites while fixing a narrow bug
- Silent fallback behavior that hides the issue
- Changing unrelated UX or copy
- Weakening validation or checks to “make the bug disappear”
