# new-feature

## Use this file when
The task introduces new user-facing functionality, new UI flows, or net-new product behavior.

## Goal
Add the feature in a way that fits the existing architecture, preserves production quality, and handles all relevant user states.

## Workflow
1. Clarify the feature goal, scope, and constraints.
2. Inspect similar existing features before designing the implementation.
3. Reuse existing primitives, patterns, data access methods, and UI conventions.
4. Identify the smallest implementation that fully satisfies the request.
5. Handle loading, empty, error, success, and pending states where relevant.
6. Add or update tests for the introduced behavior.
7. Validate UX, responsiveness, accessibility, and performance impact.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/scope-and-safety.md`
- `shared/core/definition-of-done.md`
- `shared/risk/security-and-privacy.md` if the feature touches user data, trust boundaries, permissions, or consent
- `roles/frontend/quality/accessibility.md`
- `roles/frontend/quality/responsive-ui.md`
- `roles/frontend/quality/forms.md`
- `roles/frontend/quality/testing.md`
- `roles/frontend/architecture/component-design.md`
- `roles/frontend/architecture/data-fetching.md`

## Priorities
- Fit existing architecture
- Preserve consistency with current UX patterns
- Build complete user flows, not just the happy path
- Keep the initial version focused

## Avoid
- Introducing unnecessary abstractions too early
- Shipping placeholder states or incomplete error handling
- Adding dependencies without approval
- Mixing unrelated refactors into feature work
