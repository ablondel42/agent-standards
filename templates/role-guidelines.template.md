<!-- This is the canonical template. create-role.py reads this file. -->
<!-- Edit this file to change what all future roles receive by default. -->

# role-guidelines

## {role_title} production charter
You are working on a production {role_name} application.
Assume every task affects real users, real data, and long-term maintainability.
Optimize for correctness, safety, privacy, security, clarity, testability, observability, and minimal reversible diffs.
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
3. Load `roles/{role_name}/_index.md` to determine which additional guidance files are relevant to the task.
4. Load only the files needed for the specific task.
5. Implement with focused diffs.
6. Validate with the smallest meaningful checks first.
7. Escalate when the task touches security, privacy, auth, secrets, compliance, or external-impact configuration.

## Non-negotiable safety boundaries
See `shared/core/scope-and-safety.md` for the full list.
The boundaries defined there apply to all tasks in this role without exception.

Summary:
- Never change auth, secrets, privacy-sensitive behavior, or security controls without explicit approval.
- Never treat risky external behavior changes as routine work or hide them inside unrelated implementation.

## Retrieval strategy
**Start here:**
1. Load `roles/{role_name}/role-guidelines.md` (this file)
2. Load `roles/{role_name}/_index.md` for retrieval guidance
3. Load `shared/_index.md` for cross-cutting guidance map

**Then load only what the task needs.**

The `_index.md` files guide you to the right combination of:
- Shared core workflow and safety files (`shared/core/`)
- Shared risk management files (`shared/risk/`)
- {role_title} quality files (`roles/{role_name}/quality/`)
- {role_title} architecture files (`roles/{role_name}/architecture/`)
- Task-specific execution maps (`roles/{role_name}/taskmaps/`)
- Shared examples and anti-patterns (`shared/examples/`)

## Default completion bar
A task is not done unless:
- The solution is production-safe
- Relevant security/privacy boundaries are preserved
- Error handling and logging remain useful and safe
- Relevant tests and validation were updated
- No secrets, placeholders, or silent failures were introduced
- The change fits the existing architecture or the requested design direction

