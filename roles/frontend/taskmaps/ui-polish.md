# ui-polish

## Use this file when
The task improves existing UI behavior, clarity, layout, visual consistency, accessibility, or interaction quality without introducing a major new feature.

## Goal
Improve the frontend experience while preserving existing behavior, architecture, and production stability.

## Workflow
1. Identify the exact UI issue or quality gap.
2. Check existing design patterns and shared primitives before editing.
3. Make the smallest change that meaningfully improves the experience.
4. Preserve semantics, keyboard access, responsive behavior, and user feedback states.
5. Validate the result across the relevant states and viewports.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/definition-of-done.md`
- `roles/frontend/quality/accessibility.md`
- `roles/frontend/quality/responsive-ui.md`
- `roles/frontend/quality/forms.md` if controls or validation are involved
- `roles/frontend/quality/performance.md` if rendering or interaction cost may change
- `roles/frontend/architecture/shared-primitives.md`

## Priorities
- Clarity
- Consistency
- Accessibility
- Resilience across states and screen sizes

## Avoid
- Visual-only fixes that break semantics
- Pixel-level polishing that ignores real UX problems
- Rebuilding shared components for one-off tweaks
- Hiding failures behind prettier UI
