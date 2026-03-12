# frontend-guidelines.md

## Frontend production charter
You are working on a production frontend application.
Assume every task affects real users, real data, and long-term maintainability.
Optimize for correctness, safety, privacy, security, clarity, accessibility, testability, observability, and minimal reversible diffs.
Do not optimize for speed if it reduces production quality.

## Always-on rules
- Preserve the existing architecture unless the task explicitly requests architectural change.
- Prefer the smallest safe implementation that solves the problem.
- Reuse existing patterns before introducing new abstractions.
- Do not add dependencies, change auth, weaken validation, reduce privacy protections, or alter security-sensitive behavior without explicit approval.
- Do not mark work complete while known errors, regressions, or failed checks remain.

## Required workflow
1. Inspect the current code, nearby patterns, relevant tests, and docs before editing.
2. Identify the smallest safe change.
3. Load only the additional guidance files relevant to the task.
4. Implement with focused diffs.
5. Validate with the smallest meaningful checks first.
6. Escalate when the task touches security, privacy, auth, secrets, compliance, or external-impact configuration.

## Non-negotiable safety boundaries
Never do any of the following without explicit approval:
- Add, remove, or upgrade dependencies
- Change authentication, authorization, roles, permissions, sessions, or security-sensitive flows
- Change environment variables, secrets handling, CSP, headers, cookie behavior, proxying, analytics, telemetry destinations, consent flows, or deployment configuration
- Expose sensitive data, log secrets, weaken validation, disable checks, or add unsafe HTML rendering
- Delete, rename, or move externally significant files or public APIs

## Retrieval map
Load only the files relevant to the task.

Core guidance:
- Workflow and execution discipline: `frontend/core/workflow.md`
- Scope, approvals, and risk boundaries: `frontend/core/scope-and-safety.md`
- Definition of done and completion bar: `frontend/core/definition-of-done.md`
- Agent communication style: `frontend/core/communication.md`

Quality and UX:
- Accessibility and inclusive UI: `frontend/quality/accessibility.md`
- Responsive behavior and layout resilience: `frontend/quality/responsive-ui.md`
- Forms, validation, submit states, and recoverability: `frontend/quality/forms.md`
- Testing strategy and validation depth: `frontend/quality/testing.md`
- Rendering, bundle, and interaction performance: `frontend/quality/performance.md`
- Logging, monitoring, and diagnosability: `frontend/quality/observability.md`
- Sensitive data, input trust, and privacy/security behavior: `frontend/quality/security-and-privacy.md`

Architecture:
- Component shape and separation of concerns: `frontend/architecture/component-design.md`
- State ownership, async flow, and side effects: `frontend/architecture/state-and-side-effects.md`
- Data loading, cache behavior, and network boundaries: `frontend/architecture/data-fetching.md`
- File placement and module boundaries: `frontend/architecture/file-organization.md`
- Shared UI primitives and reuse rules: `frontend/architecture/shared-primitives.md`

Task-specific workflow maps:
- Bug fixes: `frontend/taskmaps/bugfix.md`
- New features: `frontend/taskmaps/new-feature.md`
- Refactors: `frontend/taskmaps/refactor.md`
- UI polish and quality hardening: `frontend/taskmaps/ui-polish.md`
- Test-focused work: `frontend/taskmaps/test-writing.md`
- Performance investigation: `frontend/taskmaps/perf-investigation.md`

Examples and anti-patterns:
- Good task framing: `frontend/examples/good-task-brief.md`
- Good implementation planning: `frontend/examples/good-plan.md`
- Self-review checklist: `frontend/examples/change-review-checklist.md`
- Prohibited patterns and warning signs: `frontend/examples/forbidden-patterns.md`

Framework-specific rules:
- React: `frontend/frameworks/react.md`
- Next.js: `frontend/frameworks/nextjs.md`
- Vite: `frontend/frameworks/vite.md`
- Vue: `frontend/frameworks/vue.md`
- Svelte: `frontend/frameworks/svelte.md`

## Default completion bar
A task is not done unless:
- The solution is production-safe
- Relevant security/privacy boundaries are preserved
- Accessibility and resilient states were handled where relevant
- Relevant tests and validation were updated
- No secrets, placeholders, or silent failures were introduced

