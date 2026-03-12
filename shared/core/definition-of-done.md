# definition-of-done

## Use this file when
You need to decide whether a task is actually complete for a production-grade environment.

## Goal
Prevent premature completion claims and ensure that work meets an appropriate quality and safety bar.

## A task is done only if
- The implementation solves the requested problem.
- The change fits the existing architecture or the requested design direction.
- The diff is focused and reviewable.
- Relevant user-facing states are handled where applicable, including loading, empty, error, success, and recovery paths.
- Relevant tests were added, updated, or intentionally judged unnecessary with clear reasoning.
- Relevant validation was run, or skipped validation was disclosed with a real reason.
- No avoidable regressions, placeholders, debug remnants, or silent failures were introduced.
- Security, privacy, and approval boundaries were preserved.
- Error handling and logging remain useful, consistent, and safe where relevant.

## Not done if
- The change only addresses the happy path when other relevant states were ignored.
- Checks fail or meaningful validation is missing without explanation.
- Known regressions remain.
- Sensitive behavior changed without approval.
- The implementation hides failures instead of handling them responsibly.
- The result technically works but is not maintainable, reviewable, or production-safe.

## Final check
Before calling work complete, ask:
- Does this solve the real task?
- Did I validate the right thing?
- Did I preserve safety boundaries?
- Would another reviewer understand and trust this change?
