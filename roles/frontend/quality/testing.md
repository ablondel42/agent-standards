# frontend/quality/testing.md

## Use this file when
The task changes behavior, risk, validation depth, or testing scope.

## Rules
- Update or add tests for changed behavior when tests should exist.
- Run the smallest relevant checks first.
- Expand validation when risk or surface area increases.
- Keep tests aligned with real behavior, not implementation trivia.
- Do not claim completion if relevant checks fail.

## Minimum expectation
- Relevant lint
- Relevant type checking
- Relevant automated tests
- Explicit disclosure of skipped validation, with reason

## What counts as a relevant test
- Behavior tests: verify what the component or function does, not how it is implemented.
- Edge cases: cover empty state, error state, and boundary inputs where relevant.
- Interaction tests: cover form submission, button states, and async flows where behavior changed.
- Accessibility: cover keyboard navigation and focus management where relevant; use `roles/frontend/quality/accessibility.md` for detailed accessibility guidance.

## What does not replace tests
- Type checking alone is not a behavior test.
- Linting alone is not a correctness check.
- Manual spot-checking without disclosure is not validation.

## Skipping tests
If a test is genuinely unnecessary, for example for a trivial pass-through or pure styling change, say so explicitly.
Do not skip silently.
