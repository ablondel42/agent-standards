# agent-standards

Production-grade instruction files for AI coding agents.

## What is this?

A modular, retrieval-friendly repository of guidance files designed to help AI coding agents (Claude, Cursor, Copilot, etc.) write safer, more maintainable code for production applications.

Instead of one massive always-on instruction file, this repo provides:
- **Role-specific guidance** (frontend, backend, devops, etc.)
- **Shared cross-cutting rules** (security, privacy, workflow, approvals)
- **Task-specific execution maps** (bugfix, new feature, refactor, etc.)
- **Retrieval indexes** that tell agents which files to load for each task

## Why this approach?

**Traditional problem:** Long, monolithic `AGENTS.md` files that try to cover everything at once lead to:
- Context dilution (agents can't distinguish critical rules from nice-to-haves)
- Maintenance burden (updating one rule requires re-reading the entire file)
- Poor retrieval (agents load everything or nothing)

**This solution:** Small, focused files organized by concern, with explicit retrieval maps:
- Agents load only the 2-5 files relevant to the current task
- High-signal, low-noise context for every task type
- Shared guidance stays DRY (security rules written once, used across all roles)
- Easy to extend (add a new role without touching existing files)

## Design principles

1. **Modular by concern** – One file, one concern. Security in one place, accessibility in another.
2. **Retrieval-first** – Every file has a "Use this file when..." section. Index files guide agents to the right combination.
3. **Production-focused** – Assume every task affects real users and real data.
4. **Role-aware** – Frontend agents get frontend-specific guidance without backend noise.
5. **DRY for cross-cutting concerns** – Security, logging, approvals live in `shared/`, not duplicated per role.
6. **Task-specific execution** – Different workflows for bugfixes vs new features vs refactors.

## Repository structure

```
agent-standards/
├── README.md                   # This file
├── shared/                     # Cross-cutting guidance (all roles)
│   ├── _index.md               # Shared retrieval map
│   ├── core/                   # Universal workflow and safety
│   │   ├── workflow.md
│   │   ├── scope-and-safety.md
│   │   ├── communication.md
│   │   └── definition-of-done.md
│   ├── risk/                   # High-risk cross-cutting concerns
│   │   ├── security-and-privacy.md
│   │   ├── observability-and-logging.md
│   │   ├── approvals.md
│   │   └── secrets-and-sensitive-data.md
│   └── examples/               # Reusable patterns and anti-patterns
│       ├── good-task-brief.md
│       ├── good-plan.md
│       ├── change-review-checklist.md
│       └── forbidden-patterns.md
├── roles/                      # Role-specific guidance
│   └── frontend/               # Frontend role (example)
│       ├── _index.md           # Frontend retrieval map
│       ├── role-guidelines.md  # Frontend entry point
│       ├── quality/            # Frontend quality concerns
│       │   ├── accessibility.md
│       │   ├── responsive-ui.md
│       │   ├── forms.md
│       │   ├── testing.md
│       │   └── performance.md
│       ├── architecture/       # Frontend code organization
│       │   ├── component-design.md
│       │   ├── state-and-side-effects.md
│       │   ├── data-fetching.md
│       │   ├── file-organization.md
│       │   └── shared-primitives.md
│       └── taskmaps/           # Task-specific execution patterns
│           ├── bugfix.md
│           ├── new-feature.md
│           ├── refactor.md
│           ├── ui-polish.md
│           ├── test-writing.md
│           └── perf-investigation.md
├── templates/                  # Starter templates for new roles
│   ├── role-guidelines.template.md
│   ├── index.template.md
│   └── editor-mapping/
├── setup/                      # Editor-specific installation guides
└── meta/                       # Repo maintenance and taxonomy docs
```

## How to use this repo

### For a coding agent (Claude, Cursor, etc.)

**Entry sequence:**
1. Load the role entry point: `roles/<role>/role-guidelines.md`
2. Load the role retrieval map: `roles/<role>/_index.md`
3. Load the shared retrieval map: `shared/_index.md`
4. Based on the task, load only the 2-5 relevant guidance files

**Example: Frontend bugfix task**
```
Load order:
1. roles/frontend/role-guidelines.md    (role charter)
2. roles/frontend/_index.md             (retrieval map)
3. roles/frontend/taskmaps/bugfix.md    (bugfix workflow)
4. shared/core/workflow.md              (general execution discipline)
5. shared/risk/security-and-privacy.md  (if touching auth/data)
```

The agent now has focused context for the specific task without loading irrelevant files.

### For a human developer

**Use case 1: Set up agent instructions for your project**
1. Copy the relevant role folder (e.g., `roles/frontend/`) to your project
2. Copy `shared/` to your project
3. Add a project-root `AGENTS.md` that references the role entry point
4. Customize the role files to match your stack and conventions

**Use case 2: Add a new role (e.g., backend)**
1. Use `create-role.py` to scaffold the new role from the canonical templates in `templates/`
2. Or, if creating files manually, copy `templates/role-guidelines.template.md` to `roles/backend/role-guidelines.md`
3. Copy `templates/index.template.md` to `roles/backend/_index.md`
4. Create role-specific quality, architecture, and taskmap folders
5. Reference shared guidance from `shared/` where applicable

**Use case 3: Improve an existing rule**
1. Find the file via the retrieval maps (e.g., `shared/risk/security-and-privacy.md`)
2. Update the rule in that one place
3. All roles that reference it automatically get the update

## What makes this production-grade?

- **Non-negotiable safety boundaries** – Never weaken auth, expose secrets, or skip approvals without explicit permission
- **Always-on error handling and logging** – No silent failures, no empty catch blocks
- **Accessibility-first for frontend** – Semantic HTML, keyboard nav, ARIA, screen reader support
- **Security by default** – Treat all input as untrusted, validate, sanitize, escape
- **Privacy-conscious** – No PII in logs, explicit consent for data collection
- **Test-driven validation** – Changes require relevant test updates
- **Minimal, reversible diffs** – Smallest safe change, preserve existing architecture
- **Clear escalation rules** – When to stop and ask for approval

## Current roles

- 🛠️ **Frontend** – Work in progress
- 🚧 **Backend** – Coming soon
- 🚧 **DevOps** – Coming soon
- 🚧 **Mobile** – Coming soon

## Templates

The files in `templates/` are the canonical starter content for new roles.
`create-role.py` reads these templates when scaffolding a new role, so edits to the template files change what all future generated roles receive by default.

## Contributing

To add a new role or improve existing guidance:
1. Use the templates in `templates/` as a starting point
2. Follow the modular file structure (quality, architecture, taskmaps)
3. Reference shared guidance instead of duplicating it
4. Add "Use this file when..." sections to all new files
5. Update the relevant `_index.md` retrieval maps

## Philosophy

**Good agent instructions are like good code:**
- Modular, not monolithic
- DRY for cross-cutting concerns
- Single responsibility per file
- Easy to navigate and extend
- Context-aware, not context-heavy

This repo treats agent guidance as a codebase, not a document.
