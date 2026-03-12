# good-plan

## Use this file when
You need an example of a concise implementation plan before making a change.

## Goal
Show what a useful plan looks like: short, concrete, file-aware, and tied to the actual task.

## A good plan should be
- short
- specific
- grounded in the current codebase
- focused on the smallest safe change
- clear about validation

## Good example
Plan:
1. Inspect the current submit flow in the account settings form and the existing loading-state pattern used in similar forms.
2. Update the submit handler and button state so repeated clicks are blocked while the request is pending.
3. Preserve the current success and error flows.
4. Add or update focused tests for in-flight submit protection.
5. Run the narrowest relevant test scope and verify the disabled-state behavior manually if needed.

## Why this is good
- It starts with inspection rather than assumptions.
- It identifies likely edit areas without pretending certainty.
- It keeps the change narrow.
- It includes validation.
- It does not introduce unrelated refactor work.

## Weak plan example
Plan:
1. Clean up the form code.
2. Improve the UX.
3. Refactor anything that looks outdated.
4. Test everything.

## Why this is weak
- The steps are vague.
- The scope is uncontrolled.
- The edit surface is undefined.
- The validation target is unrealistic and not task-specific.
