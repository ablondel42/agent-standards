<!-- This is the canonical template. create-role.py reads this file. -->
<!-- Edit this file to change what all future roles receive by default. -->

# {role_name} index

## Purpose
This file helps agents load only the {role_name} guidance relevant to the current task.
Use it after `roles/{role_name}/role-guidelines.md` to decide which {role_name}-specific files and shared cross-cutting files should be loaded.

## Loading strategy
Start small.
Load only the files directly relevant to the task, and pull in shared guidance when the work touches cross-cutting concerns like privacy, logging, approvals, or overall execution safety.

## Start here
For any {role_name} task, begin with:
- `roles/{role_name}/role-guidelines.md`
- `shared/_index.md`

Then load only the additional files needed for the task.

## Load shared files when needed
Use shared guidance for concerns that are not {role_name}-specific:

- `shared/core/workflow.md`
  Load when: you need execution order, change discipline, or validation sequencing.
- `shared/core/scope-and-safety.md`
  Load when: the task may expand in scope, affect external behavior, or touch sensitive systems.
- `shared/core/communication.md`
  Load when: you need guidance on reporting assumptions, blockers, or tradeoffs.
- `shared/core/definition-of-done.md`
  Load when: deciding whether a task is complete enough for production.

- `shared/risk/security-and-privacy.md`
  Load when: the task touches auth, permissions, user data, consent, or trust boundaries.
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

## Load {role_name} quality files
Use these files for {role_name}-specific quality concerns:

- `roles/{role_name}/quality/testing.md`
  Load when: behavior changes require test updates or validation strategy decisions.
- `roles/{role_name}/quality/security.md`
  Load when: the task has {role_name}-specific security implications.
- `roles/{role_name}/quality/performance.md`
  Load when: the task may affect performance or resource usage.
- `roles/{role_name}/quality/observability.md`
  Load when: the task affects {role_name}-specific logging or monitoring.
- `roles/{role_name}/quality/code-quality.md`
  Load when: the task involves code style, clarity, or maintainability decisions.

## Load {role_name} architecture files
Use these files for implementation shape and code organization:

- `roles/{role_name}/architecture/structure.md`
  Load when: the task affects overall code structure or module boundaries.
- `roles/{role_name}/architecture/patterns.md`
  Load when: the task involves design patterns or architectural patterns.
- `roles/{role_name}/architecture/data-flow.md`
  Load when: the task affects data movement, state, or side effects.
- `roles/{role_name}/architecture/file-organization.md`
  Load when: the task affects file placement or import structure.
- `roles/{role_name}/architecture/dependencies.md`
  Load when: the task involves dependency management or external integrations.

## Load taskmaps
Use taskmaps only when the work benefits from a task-specific execution pattern:

- `roles/{role_name}/taskmaps/bugfix.md`
- `roles/{role_name}/taskmaps/new-feature.md`
- `roles/{role_name}/taskmaps/refactor.md`
- `roles/{role_name}/taskmaps/test-writing.md`
- `roles/{role_name}/taskmaps/perf-investigation.md`
- `roles/{role_name}/taskmaps/deployment.md`

Load only the one that matches the current task type.

## Retrieval rules
- Prefer 1 to 4 relevant files over broad context loading.
- Do not load all {role_name} files by default.
- Use shared files for cross-cutting concerns and {role_name} files for {role_name}-specific details.
- If a task touches security, privacy, logging, or approvals, load the relevant shared risk files before implementing.
- If a task crosses role boundaries, start with {role_name} guidance and then load the minimum additional shared or adjacent-role guidance needed.

