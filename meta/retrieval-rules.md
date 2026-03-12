# retrieval-rules

## Purpose
This file defines how agents should navigate the repository without loading too much context.
It exists to keep the standards corpus high-signal, modular, and efficient to retrieve from.

## Core retrieval principle
Load the smallest set of files that can safely guide the current task.
Do not load the entire repository or an entire role subtree by default.

## Retrieval order
Use this order unless a narrower file is already known to be sufficient:
1. Load the relevant role entry file: `roles/<role>/role-guidelines.md`
2. Load the role retrieval map: `roles/<role>/_index.md`
3. Load only the topical files directly relevant to the task
4. Load shared files only when the task touches cross-cutting concerns
5. Stop loading once you have enough guidance to act safely

## Shared file triggers
Load from `shared/core/` when the task needs general workflow, communication, approval, scope, or completion guidance.

Load from `shared/risk/` when the task touches any of the following:
- authentication or authorization
- secrets or environment variables
- sensitive data or privacy boundaries
- logging or observability
- telemetry, analytics, or consent
- external integrations
- HTML rendering, uploads, or trust boundaries
- any change with security implications

Load from `shared/examples/` when the task benefits from examples, review checklists, or anti-pattern references.

## Role file triggers
Load role-specific files only for concerns unique to that role.
For example, frontend tasks may require files for forms, accessibility, responsive UI, rendering performance, component design, or data-fetching boundaries.

## Context budget rules
Prefer 1 to 4 relevant files over large context dumps.
Avoid loading sibling files just in case.
Do not load examples unless they improve the current task.
Do not load future-role files when working within a current role.

## Escalation rules
If the task crosses role boundaries, start with the initiating role and then load the minimum shared or adjacent-role files needed to handle the overlap safely.
If the task touches a high-risk area, prioritize `shared/risk/` guidance before implementation.

## Index-writing rules
Every `_index.md` should:
- map concerns to file paths
- use human-recognizable concern names
- avoid repeating full rule content
- stay compact enough to be always useful

## Role-guidelines rules
Every `role-guidelines.md` should:
- stay small and always-on
- define the role charter and non-negotiable boundaries
- point to `_index.md` and shared files
- avoid becoming a long handbook

## Anti-patterns
Avoid:
- loading entire folders by default
- duplicating shared rules into every role
- overly broad miscellaneous files
- giant always-on instruction files
- retrieval maps that duplicate the full contents of the referenced files
