# test-writing

## Use this file when
The task is to add, improve, repair, or expand frontend tests.

## Goal
Add tests that protect meaningful behavior, improve confidence, and fit the repository’s testing style without creating brittle noise.

## Workflow
1. Identify the behavior that actually needs protection.
2. Prefer testing observable behavior over internal implementation details.
3. Follow the project’s existing testing conventions and file placement.
4. Cover the most important success, failure, and edge states for the changed behavior.
5. Keep test setup readable and focused.
6. Run the narrowest relevant test scope first.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/definition-of-done.md`
- `shared/examples/change-review-checklist.md`
- `roles/frontend/quality/testing.md`
- `roles/frontend/quality/forms.md` if form behavior is being tested
- `roles/frontend/quality/accessibility.md` if interaction or semantic behavior matters
- `roles/frontend/architecture/state-and-side-effects.md` if async flow or retries are involved

## Priorities
- Behavior confidence
- Readability
- Stability
- Fast targeted validation

## Avoid
- Testing implementation trivia
- Overspecifying markup that is likely to change harmlessly
- Massive snapshot reliance without strong justification
- Leaving changed behavior untested when tests should exist
