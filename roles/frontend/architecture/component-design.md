# frontend/architecture/component-design.md

## Use this file when
The task affects components, hooks, composition, responsibilities, or UI boundaries.

## Rules
- Prefer small, focused components.
- Keep presentation logic separate from complex side effects when the codebase already distinguishes them.
- Avoid prop APIs that accumulate boolean flags and unclear modes.
- Keep important business rules visible, not hidden in vague helpers.
- Reuse established patterns before inventing new abstractions.
