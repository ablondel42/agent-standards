# refactor

## Use this file when
The task is primarily about restructuring code without intentionally changing behavior.

## Goal
Improve maintainability, clarity, or structure while preserving functional behavior and production safety.

## Workflow
1. Define the exact refactor boundary before editing.
2. Confirm which behavior must remain unchanged.
3. Inspect the existing architecture and avoid fighting the codebase’s established structure.
4. Make the refactor in small, reviewable steps.
5. Preserve tests or strengthen them if they are needed as behavior guards.
6. Validate that behavior remains stable after the structural changes.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/scope-and-safety.md`
- `shared/core/definition-of-done.md`
- `shared/examples/change-review-checklist.md`
- `roles/frontend/architecture/component-design.md`
- `roles/frontend/architecture/file-organization.md`
- `roles/frontend/architecture/shared-primitives.md`
- `roles/frontend/quality/testing.md`

## Priorities
- Behavior preservation
- Smaller, reviewable diffs
- Better local clarity
- Stronger structural consistency

## Avoid
- Sneaking in feature changes during refactor work
- Renaming or moving externally meaningful files without approval
- Rewriting large surfaces without clear justification
- Removing useful logging or diagnostics during cleanup
