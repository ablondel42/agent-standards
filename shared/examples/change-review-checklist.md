# change-review-checklist

## Use this file when
You want a final self-review pass before calling work complete.

## Goal
Catch common quality, safety, and maintainability issues before a change is finalized.

## Checklist
- Does the change solve the requested problem rather than a guessed variant?
- Is the diff focused and reasonably reviewable?
- Did I inspect nearby patterns before editing?
- Did I avoid unrelated cleanup or opportunistic refactors?
- Did I preserve the existing architecture unless a design change was requested?
- Did I handle relevant loading, empty, error, success, and recovery states?
- Did I preserve accessibility, security, privacy, and approval boundaries?
- Did I avoid exposing secrets, sensitive data, or unsafe diagnostics?
- Did I add or update relevant tests where they should exist?
- Did I run meaningful validation or clearly disclose what was not validated?
- Did I preserve debuggability and useful error handling?
- Would another reviewer understand why this change is safe?

## If any answer is no
Do not mark the work complete until the gap is fixed or explicitly disclosed with a real reason.

## Review reminder
A change can be small and still be risky.
A change can work locally and still be incomplete for production.
