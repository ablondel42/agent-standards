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
