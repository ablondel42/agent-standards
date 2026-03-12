# frontend/architecture/data-fetching.md

## Use this file when
The task affects data loading, caching, invalidation, request ownership, or API client behavior.

## Rules
- Follow the approved data-access pattern already used by the codebase.
- Do not fetch ad hoc inside presentational components when an established data layer exists.
- Be explicit about cache invalidation and refetch triggers.
- Avoid duplicated requests and unnecessary background churn.
- Preserve existing API contracts unless a change is explicitly requested.
