# frontend/architecture/file-organization.md

## Use this file when
The task affects file placement, module boundaries, imports, or project structure.

## Rules
- Follow the repository's existing structure and ownership boundaries.
- Put shared logic in shared locations and feature-specific logic near the feature.
- Keep modules cohesive and avoid mixing unrelated responsibilities.
- Avoid circular dependencies and hidden cross-module coupling.
- Do not move files with external impact without approval.
