# perf-investigation

## Use this file when
The task is to investigate or improve rendering speed, bundle size, interaction latency, network efficiency, or frontend resource usage.

## Goal
Find and address meaningful performance issues without making the code less safe, less clear, or harder to maintain.

## Workflow
1. Define the observed performance problem as concretely as possible.
2. Identify the likely hot path before changing code.
3. Inspect rendering behavior, fetch patterns, state churn, or bundle cost depending on the symptom.
4. Prefer targeted measurement and narrow fixes over premature optimization.
5. Validate that the change improves the intended bottleneck without creating correctness regressions.

## Load these files when relevant
- `shared/core/workflow.md`
- `shared/core/definition-of-done.md`
- `shared/risk/observability-and-logging.md` if instrumentation or diagnostics are needed
- `roles/frontend/quality/performance.md`
- `roles/frontend/architecture/state-and-side-effects.md`
- `roles/frontend/architecture/data-fetching.md`
- `roles/frontend/architecture/component-design.md`

## Priorities
- Measured bottlenecks
- Targeted fixes
- Preserved readability
- No regressions in correctness or UX

## Avoid
- Premature optimization
- Broad rewrites justified only by vague performance claims
- Adding heavy dependencies for tiny gains
- Removing useful safety checks without evidence
