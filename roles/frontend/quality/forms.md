# frontend/quality/forms.md

## Use this file when
The task affects forms, field validation, submission flows, inline editing, filters, or user-entered values.

## Rules
- Validate inputs at the right layer.
- Show clear field-level or form-level errors.
- Preserve user input during recoverable failures.
- Prevent duplicate submissions when actions are in flight.
- Expose pending, success, and failure states clearly.
- Keep forms keyboard- and screen-reader-friendly.
- Normalize and sanitize user-controlled values when existing patterns require it.

## Avoid
- Silent validation failures
- Disappearing user input after recoverable errors
- Submit actions with no pending state
- Ambiguous success or failure behavior
