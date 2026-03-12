# taxonomy

## Purpose
This file defines the information architecture of the `agent-standards` repository.
It explains how rules are grouped, what belongs in each section, and how new files should be categorized so the corpus stays scalable across multiple roles.

## Top-level model
The repository is organized into five layers:
- `setup/`: editor-specific installation and mapping guidance
- `shared/`: cross-cutting rules that apply across roles
- `roles/`: role-specific standards such as frontend, backend, or database
- `templates/`: starter files for creating new rule sets consistently
- `meta/`: governance for the guideline corpus itself

## Shared vs role-specific
Put guidance in `shared/` when it is broadly applicable across engineering roles.
Typical shared topics include workflow discipline, approval boundaries, privacy and security rules, logging expectations, completion standards, and review examples.

Put guidance in `roles/<role>/` when it depends on the responsibilities, architecture, or quality bar of a specific role.
Typical role-specific topics include UI accessibility for frontend, API contract design for backend, or migration safety for database.

## File classification rules
Use these placement rules when adding or moving files:
- If a rule would be duplicated across two or more roles, it probably belongs in `shared/`.
- If a rule requires domain-specific implementation knowledge, it belongs in a role subtree.
- If a file explains how to install or map guidance into a tool, it belongs in `setup/`.
- If a file is a reusable scaffold for future docs, it belongs in `templates/`.
- If a file explains how this repository should evolve, it belongs in `meta/`.

## Shared subtrees
`shared/core/` is for universal execution rules.
This includes workflow, communication, scope control, safety boundaries, and definition-of-done expectations.

`shared/risk/` is for high-risk cross-cutting concerns.
This includes security, privacy, observability, logging, approvals, secrets handling, sensitive data handling, and similar topics.

`shared/examples/` is for reusable examples and anti-pattern references.
This includes good task briefs, good plans, review checklists, and forbidden patterns.

## Role subtree expectations
Each role subtree should generally contain:
- `role-guidelines.md`: the compact always-on entry point for the role
- `_index.md`: the role-specific retrieval map
- focused topical subdirectories such as `quality/`, `architecture/`, `frameworks/`, or `taskmaps/`

Do not force every role to use the exact same subtree names if that harms clarity.
The role structure should be consistent in spirit, not mechanically identical.

## Naming conventions
Use lowercase kebab-case filenames.
Choose names that reveal retrieval intent, for example `security-and-privacy.md` or `observability-and-logging.md`.
Avoid vague names such as `misc.md`, `notes.md`, or `rules2.md`.

Use `_index.md` only for retrieval maps.
Use `role-guidelines.md` only for the compact role entrypoint.
Do not create multiple competing entry files within the same role.

## Content boundaries
Each file should cover one coherent topic.
Do not mix unrelated concerns in a single file just because they are short.
Prefer splitting files by retrieval need rather than by arbitrary word count.

Examples:
- Keep `security-and-privacy.md` separate from `observability-and-logging.md`
- Keep `forms.md` separate from `responsive-ui.md`
- Keep `workflow.md` separate from `definition-of-done.md`

## Future growth
When adding a new role, start by creating only:
- `roles/<role>/role-guidelines.md`
- `roles/<role>/_index.md`
- the minimum number of topical files needed for immediate use

Do not scaffold large empty trees for future roles unless there is a concrete near-term need.
Favor gradual expansion guided by real usage.
