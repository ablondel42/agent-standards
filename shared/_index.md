# shared index

## Purpose
This file is the navigation map for all cross-cutting guidance in `shared/`.
It tells agents when and how to use shared rules alongside role-specific files without overloading context.

## Structure
The `shared/` directory has three main areas:

- `shared/core/` – universal execution rules:
  - `workflow.md`
  - `scope-and-safety.md`
  - `communication.md`
  - `definition-of-done.md`

- `shared/risk/` – high-risk cross-cutting concerns:
  - `security-and-privacy.md`
  - `observability-and-logging.md`
  - `approvals.md`
  - `secrets-and-sensitive-data.md`

- `shared/examples/` – reusable examples and anti-pattern references:
  - `good-task-brief.md`
  - `good-plan.md`
  - `change-review-checklist.md`
  - `forbidden-patterns.md`

## When to use shared/core
Load from `shared/core/` when you need general engineering discipline, not domain-specific details:

- `shared/core/workflow.md`
  Use when: you need a clear sequence for inspecting, planning, implementing, and validating changes.
- `shared/core/scope-and-safety.md`
  Use when: the task might expand in scope, affect external behavior, or touch sensitive systems.
- `shared/core/communication.md`
  Use when: you need guidance on how the agent should report assumptions, risks, and blockers.
- `shared/core/definition-of-done.md`
  Use when: deciding if a task is actually complete for a production system.

## When to use shared/risk
Load from `shared/risk/` whenever the task touches security, privacy, approvals, or sensitive 

- `shared/risk/security-and-privacy.md`
  Use when: dealing with auth, permissions, user data, PII, consent, cookies, CSP, or any trust boundary.
- `shared/risk/observability-and-logging.md`
  Use when: changing logging, monitoring, error handling, or diagnosability.
- `shared/risk/approvals.md`
  Use when: a change clearly requires higher-level approval, for example breaking changes, security posture changes, or compliance impact.
- `shared/risk/secrets-and-sensitive-data.md`
  Use when: handling secrets, tokens, credentials, environment variables, or other sensitive operational data.

If a change touches more than one of these areas, load each relevant file, but avoid loading the whole `risk/` folder by default.

## When to use shared/examples
Load from `shared/examples/` for concrete patterns and review help, not as always-on context:

- `shared/examples/good-task-brief.md`
  Use when: drafting or refining a task description for an agent.
- `shared/examples/good-plan.md`
  Use when: constructing a short, file-specific implementation plan.
- `shared/examples/change-review-checklist.md`
  Use when: self-reviewing or code-reviewing a change against the standards.
- `shared/examples/forbidden-patterns.md`
  Use when: checking for high-risk anti-patterns before finalizing a change.

## Retrieval rules
- Start with the role's `role-guidelines.md` and `roles/<role>/_index.md`.
- Load shared files only when the task clearly matches one of the triggers above.
- Prefer loading 1 to 3 precise shared files over loading entire directories.
- Do not duplicate shared content into role files; reference it instead.

## Adding new shared files
When adding a new shared file:

1. Decide whether it belongs in `core/`, `risk/`, or `examples/`.
2. Give it a clear, retrieval-friendly name.
3. Add a short `Use this file when...` section at the top of the file.
4. Update this `shared/_index.md` with:
   - a one-line trigger description
   - a short explanation of when to load it.
