# frontend/quality/performance.md

## Use this file when
The task may affect rendering cost, bundle size, network behavior, startup work, or interaction latency.

## Rules
- Avoid unnecessary rerenders.
- Avoid heavy computation in render paths.
- Be careful with cache invalidation and duplicated network requests.
- Lazy-load heavy or optional functionality when appropriate.
- Do not add heavy libraries for marginal convenience.
- Prefer predictable state transitions and stable event behavior.

## Check for
- Bundle impact
- Render hot paths
- Repeated requests
- Slow loading or interaction regressions
