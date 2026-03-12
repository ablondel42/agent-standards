# frontend/quality/accessibility.md

## Use this file when
The task affects UI semantics, navigation, forms, dialogs, interactive controls, messaging, or any user-facing experience.

## Required
- Use semantic HTML first.
- Ensure controls have accessible names.
- Preserve keyboard navigation and visible focus.
- Use correct labels, descriptions, and status messages.
- Keep error messages clear and discoverable.
- Ensure interactions do not rely on color alone.
- Handle screen-reader announcement needs for async updates where relevant.

## Do not ship
- Unlabeled controls
- Click-only interactions without keyboard access
- Hidden focus states
- Broken tab order
- Inaccessible modal or popover behavior
