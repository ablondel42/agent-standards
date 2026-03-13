# workflow

## Use this file when
The task needs a general execution pattern for inspecting, planning, implementing, validating, and reporting work safely.

## Goal
Make changes in a way that is disciplined, reviewable, and production-safe without wasting context or creating unnecessary churn.

## Default workflow
1. Inspect the current code, configuration, docs, and nearby patterns before editing.
2. Clarify the task, assumptions, and constraints.
3. Identify the smallest safe change that solves the actual problem.
4. Load only the additional guidance files relevant to the task.
5. Implement in focused, reviewable steps.
6. Validate with the narrowest meaningful checks first.
7. Report clearly what changed, what was validated, and any remaining risks or follow-ups.

## Planning rules
- Prefer short, file-specific plans over broad speculative planning.
- Base decisions on the current codebase, not on idealized architecture.
- Reuse established patterns before introducing new abstractions.
- Escalate when the task touches approvals, secrets, security, privacy, or externally meaningful behavior.

## Implementation rules
- Keep diffs minimal and intentional.
- Preserve existing architecture unless a design change is explicitly requested.
- Avoid mixing unrelated cleanup into focused task work.
- Do not trade correctness for speed.

## Validation rules
- Start with the smallest relevant validation.
- Increase validation depth when risk increases, especially when task type, changed surface area, or safety sensitivity increases.
- Do not claim success if meaningful checks failed or were skipped without disclosure.
- If validation cannot be run, say so clearly and explain why.

## Avoid
- Editing before understanding the current implementation
- Large rewrites without clear need
- Loading broad context by default
- Marking work complete with unresolved known failures
