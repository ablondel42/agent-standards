# frontend index

## Purpose
This file helps agents load only the frontend guidance relevant to the current task.
Use it after `roles/frontend/role-guidelines.md` to decide which frontend-specific files and shared cross-cutting files should be loaded.

## Loading strategy
Start small.
Load only the files directly relevant to the task, and pull in shared guidance when the work touches cross-cutting concerns like privacy, logging, approvals, or overall execution safety.

## Start here
For any frontend task, begin with:
- `roles/frontend/role-guidelines.md`
- `shared/_index.md`

Then load only the additional files needed for the task.

## Load shared files when needed
Use shared guidance for concerns that are not frontend-specific:

- `shared/core/workflow.md`
  Load when: you need execution order, change discipline, or validation sequencing.
- `shared/core/scope-and-safety.md`
  Load when: the task may expand in scope, affect external behavior, or touch sensitive systems.
- `shared/core/communication.md`
  Load when: you need guidance on reporting assumptions, blockers, or tradeoffs.
- `shared/core/definition-of-done.md`
  Load when: deciding whether a task is complete enough for production.

- `shared/risk/security-and-privacy.md`
  Load when: the task touches auth, permissions, user data, consent, cookies, CSP, uploads, or trust boundaries.
- `shared/risk/observability-and-logging.md`
  Load when: the task affects logging, monitoring, error catching, or diagnosability.
- `shared/risk/approvals.md`
  Load when: a change may require explicit approval due to risk, scope, compliance, or user impact.
- `shared/risk/secrets-and-sensitive-data.md`
  Load when: the task touches secrets, credentials, tokens, or sensitive operational data.

- `shared/examples/good-task-brief.md`
  Load when: refining task framing.
- `shared/examples/good-plan.md`
  Load when: drafting a concise implementation plan.
- `shared/examples/change-review-checklist.md`
  Load when: reviewing a change before completion.
- `shared/examples/forbidden-patterns.md`
  Load when: checking for risky anti-patterns.

## Load frontend quality files
Use these files for frontend-specific quality concerns:

- `roles/frontend/quality/accessibility.md`
  Load when: the task affects semantics, keyboard support, labels, focus, dialogs, or interactive controls.
- `roles/frontend/quality/responsive-ui.md`
  Load when: the task affects layout, spacing, breakpoints, media, or cross-device behavior.
- `roles/frontend/quality/forms.md`
  Load when: the task affects forms, validation, user input, submit states, or inline editing.
- `roles/frontend/quality/testing.md`
  Load when: behavior changes require test updates or validation strategy decisions.
- `roles/frontend/quality/performance.md`
  Load when: the task may affect rendering cost, bundle size, network behavior, or interaction speed.

## Load frontend architecture files
Use these files for implementation shape and code organization:

- `roles/frontend/architecture/component-design.md`
  Load when: the task affects component boundaries, hooks, composition, or UI responsibilities.
- `roles/frontend/architecture/state-and-side-effects.md`
  Load when: the task affects state ownership, async flow, retries, optimistic updates, or side effects.
- `roles/frontend/architecture/data-fetching.md`
  Load when: the task affects data loading, caching, invalidation, or API-client boundaries.
- `roles/frontend/architecture/file-organization.md`
  Load when: the task affects file placement, module structure, imports, or ownership boundaries.
- `roles/frontend/architecture/shared-primitives.md`
  Load when: the task affects shared UI primitives, utilities, or reusable hooks.

## Load taskmaps
Use taskmaps only when the work benefits from a task-specific execution pattern:

- `roles/frontend/taskmaps/bugfix.md`
- `roles/frontend/taskmaps/new-feature.md`
- `roles/frontend/taskmaps/refactor.md`
- `roles/frontend/taskmaps/ui-polish.md`
- `roles/frontend/taskmaps/test-writing.md`
- `roles/frontend/taskmaps/perf-investigation.md`

Load only the one that matches the current task type.

## Retrieval rules
- Prefer 1 to 4 relevant files over broad context loading.
- Do not load all frontend files by default.
- Use shared files for cross-cutting concerns and frontend files for frontend-specific details.
- If a task touches security, privacy, logging, or approvals, load the relevant shared risk files before implementing.
- If a task crosses role boundaries, start with frontend guidance and then load the minimum additional shared or adjacent-role guidance needed.
