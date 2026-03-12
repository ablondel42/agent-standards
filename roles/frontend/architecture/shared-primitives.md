# frontend/architecture/shared-primitives.md

## Use this file when
The task affects design-system primitives, shared utilities, hooks, or reusable UI foundations.

## Rules
- Reuse existing primitives before creating new ones.
- Keep shared APIs small, stable, and easy to reason about.
- Do not push feature-specific behavior into shared primitives without clear reuse justification.
- Prefer composition over overly configurable mega-components.
- Treat shared primitives as high-impact surfaces and validate accordingly.
