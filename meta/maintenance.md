# maintenance

## Purpose
This file defines how the `agent-standards` repository should be maintained over time.
It aims to keep the corpus consistent, strict, and useful as new roles and rule sets are added.

## Maintenance goals
- Keep the repository easy to navigate
- Keep retrieval paths stable and predictable
- Minimize duplication across files
- Preserve strict production-grade standards
- Expand only when there is a clear practical need

## When to create a new file
Create a new file when:
- a topic is meaningfully distinct
- a file is becoming hard to retrieve cleanly
- the same rule set is repeatedly needed independently
- a role needs a clearly scoped concern that should not be mixed into another file

Do not create a new file just to make the tree look symmetrical.

## When to merge files
Merge files when:
- two files are always loaded together
- the distinction between them is artificial
- separate files are causing repetitive maintenance with no retrieval benefit

## Duplication policy
Shared rules should be written once in `shared/` whenever possible.
Role files may reference shared rules, narrow them, or add stricter constraints, but they should not casually duplicate them.

If a role needs a stricter version of a shared rule, prefer:
- referencing the shared rule
- then adding the role-specific stricter rule locally

## Update policy
When a new best practice is added:
1. Decide whether it is shared or role-specific
2. Place it in the narrowest correct file
3. Update the relevant `_index.md`
4. Update any affected `role-guidelines.md`
5. Check whether examples or templates also need updates

## Naming and path stability
Avoid renaming files unless the current name is misleading or retrieval-hostile.
Stable paths improve reliability for humans and agents.

If a rename is necessary:
- update all retrieval maps
- update setup docs if they reference the path
- avoid leaving multiple conflicting entry points behind

## Review standards
Changes to this repository should be reviewed for:
- clarity
- retrieval efficiency
- duplication
- consistency with taxonomy
- security and privacy completeness
- whether the change improves or worsens maintainability

## Safety for the standards repo
This repository defines production-oriented standards, so changes to it should be conservative.
Do not weaken safety, privacy, approval, logging, or validation rules casually.

If a change makes a rule more permissive, it should be justified explicitly.
If a change makes a rule stricter, confirm that it does not create unnecessary noise or unusable friction.

## Practical hygiene
- Remove stale placeholders once real content exists
- Avoid empty directories unless they are intentionally documented
- Keep examples realistic and concise
- Keep entry files short
- Keep indexes current whenever files move
- Delete obsolete compatibility layers once migration is complete

## Growth policy
Expand the repo incrementally.
Do not pre-build large trees for roles that are not yet being used.
Let real usage patterns determine where the corpus becomes more granular.
