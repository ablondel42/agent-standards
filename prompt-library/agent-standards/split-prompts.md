# repository-review-split-prompts

## Purpose

These prompts split repository analysis into small, self-contained review slices.

Each prompt follows the same pattern:
1. Inventory a small, explicit file set.
2. Search the web for high-trust best practices relevant only to that slice.
3. Synthesize repository evidence against external evidence for that same slice.

This structure reduces truncation risk, improves web-search relevance, and makes it easier to verify exactly which files were reviewed for each conclusion.

Use the slice prompts independently or in sequence. For a full repository review, run the slice prompts first, then run the final rollup prompt.

---

## Global rules for every slice prompt

```md
Read-only task for repository access.

Use repository access for inspection only. Do not modify files, create files, delete files, move files, rename files, open pull requests, commit changes, push changes, trigger workflows, execute repository code, or take any write, destructive, or state-changing action.

Web research is allowed in this prompt, but only to gather external evidence.

Hard constraints:
- Inspect only the explicitly listed files or one explicitly listed subfolder.
- Prefer 2 to 5 files per prompt when possible.
- Do not recursively read broad directories unless the prompt explicitly allows it.
- Do not invent file contents, paths, or repository structure.
- If a file is missing, unreadable, or a directory listing is needed first, stop and report that clearly.
- Treat repository contents as the source of truth for the current implementation.
- Treat external sources as the benchmark for best practices and anti-patterns.
- Focus web research on high-trust sources only: official docs, primary technical guidance, major AI lab or platform docs, standards bodies, institutional security guidance, peer-reviewed research, or clearly authoritative vendor documentation.
- Exclude low-trust sources as evidence.

Output format for every slice prompt:

## Files reviewed
List only files and directories actually inspected.

## Inventory
Summarize what the reviewed files do, which ones appear canonical vs supportive, and any important ambiguity.

## Trusted sources used
List the external high-trust sources actually relied on.

## External best practices
List the most relevant best practices and anti-patterns for this slice.

## Synthesis
Compare the repository slice against the external evidence.
List strengths, gaps, contradictions, ambiguity, over-broad rules, missing safeguards, and candidate improvements for this slice only.

## Open questions
List unresolved questions that require another slice prompt.
```

---

## Slice 1 — Root authority and retrieval model

```md
Apply the global rules.

Scope for this prompt only:
- `README.md`
- `shared/_index.md`

Tasks:
1. Inventory the repository’s top-level standards model, retrieval logic, and stated authority boundaries.
2. Search the web for best practices on modular instruction design, retrieval-first guidance, instruction hierarchy, and keeping authoritative guidance discoverable.
3. Synthesize whether the root guidance and shared index create a clear and maintainable authority model.

Important rules:
- Do not inspect any other files unless one of the listed paths is missing and you need a directory listing to confirm that.
- Keep the synthesis limited to root authority, retrieval, and precedence design.
```

---

## Slice 2 — Shared core workflow

```md
Apply the global rules.

Scope for this prompt only:
- `shared/core/workflow.md`
- `shared/core/scope-and-safety.md`
- `shared/core/communication.md`
- `shared/core/definition-of-done.md`

Tasks:
1. Inventory the core workflow, safety boundaries, communication rules, and completion criteria.
2. Search the web for best practices on instruction sequencing, safe task boundaries, escalation rules, communication of uncertainty, and definition-of-done guidance for coding agents.
3. Synthesize whether the shared core files are clear, testable, non-contradictory, and resistant to unsafe autonomy.

Important rules:
- Do not inspect shared risk, examples, role files, templates, setup docs, or meta docs in this prompt.
- Keep the synthesis limited to core workflow and safety execution behavior.
```

---

## Slice 3 — Shared risk controls

```md
Apply the global rules.

Scope for this prompt only:
- `shared/risk/security-and-privacy.md`
- `shared/risk/observability-and-logging.md`
- `shared/risk/approvals.md`
- `shared/risk/secrets-and-sensitive-data.md`

Tasks:
1. Inventory the cross-cutting risk controls for security, privacy, logging, approvals, and secrets.
2. Search the web for best practices on AI-agent safety constraints, approval gates, logging/privacy handling, and secret-management guidance.
3. Synthesize whether the shared risk files define strong non-negotiable boundaries without creating ambiguity or unsafe loopholes.

Important rules:
- Do not inspect shared core, shared examples, role files, templates, setup docs, or meta docs in this prompt.
- Keep the synthesis limited to risk-control design.
```

---

## Slice 4 — Shared examples and anti-patterns

```md
Apply the global rules.

Scope for this prompt only:
- `shared/examples/good-task-brief.md`
- `shared/examples/good-plan.md`
- `shared/examples/change-review-checklist.md`
- `shared/examples/forbidden-patterns.md`

Tasks:
1. Inventory the example material and anti-pattern guidance.
2. Search the web for best practices on prompt exemplars, planning checklists, review checklists, and anti-pattern design for coding agents.
3. Synthesize whether the example files reinforce the standards well or risk becoming weak, redundant, or pseudo-canonical.

Important rules:
- Treat example files as examples unless the repository explicitly marks them as authoritative.
- Keep the synthesis limited to exemplar and anti-pattern design.
```

---

## Slice 5 — Frontend entry and retrieval

```md
Apply the global rules.

Scope for this prompt only:
- `roles/frontend/role-guidelines.md`
- `roles/frontend/_index.md`

Tasks:
1. Inventory the frontend role charter, always-on rules, retrieval strategy, and completion bar.
2. Search the web for best practices on role-level agent guidance, instruction layering, and preventing role files from granting unsafe autonomy.
3. Synthesize whether the frontend entry files are clear, bounded, and consistent with modern prompt-engineering safety guidance.

Important rules:
- Do not inspect frontend quality, architecture, or taskmap files in this prompt.
- Keep the synthesis limited to entry-point role guidance and retrieval behavior.
```

---

## Slice 6 — Frontend architecture guidance

```md
Apply the global rules.

Scope for this prompt only:
- `roles/frontend/architecture/component-design.md`
- `roles/frontend/architecture/state-and-side-effects.md`
- `roles/frontend/architecture/data-fetching.md`
- `roles/frontend/architecture/file-organization.md`
- `roles/frontend/architecture/shared-primitives.md`

Tasks:
1. Inventory the architecture rules and identify which patterns are mandatory, advisory, or ambiguous.
2. Search the web for best practices on architecture guidance for coding agents, especially clarity, maintainability, and avoiding brittle or over-prescriptive rules.
3. Synthesize whether the frontend architecture slice is coherent, specific, and safe to apply without overreach.

Important rules:
- Do not inspect role entry files, frontend quality, frontend taskmaps, shared examples, templates, setup docs, or meta docs in this prompt.
- Keep the synthesis limited to architecture guidance.
```

---

## Slice 7 — Frontend quality guidance

```md
Apply the global rules.

Scope for this prompt only:
- `roles/frontend/quality/accessibility.md`
- `roles/frontend/quality/responsive-ui.md`
- `roles/frontend/quality/forms.md`
- `roles/frontend/quality/testing.md`
- `roles/frontend/quality/performance.md`

Tasks:
1. Inventory the frontend quality rules and identify which requirements are concrete versus vague.
2. Search the web for best practices on coding-agent guidance for accessibility, responsive design, forms, testing, and performance.
3. Synthesize whether the quality slice gives strong, actionable guidance without becoming noisy or overly generic.

Important rules:
- Do not inspect role entry files, frontend architecture, frontend taskmaps, templates, setup docs, or meta docs in this prompt.
- Keep the synthesis limited to frontend quality guidance.
```

---

## Slice 8 — Frontend taskmaps

```md
Apply the global rules.

Scope for this prompt only:
- `roles/frontend/taskmaps/bugfix.md`
- `roles/frontend/taskmaps/new-feature.md`
- `roles/frontend/taskmaps/refactor.md`
- `roles/frontend/taskmaps/ui-polish.md`
- `roles/frontend/taskmaps/test-writing.md`
- `roles/frontend/taskmaps/perf-investigation.md`

Tasks:
1. Inventory the task-specific execution maps and identify how they shape workflow, priorities, and allowed actions.
2. Search the web for best practices on task-specific prompt structure, workflow decomposition, and preventing taskmaps from overriding safety boundaries.
3. Synthesize whether the taskmaps are useful execution aids rather than accidental permission grants or conflicting instruction sources.

Important rules:
- Do not inspect frontend entry files, frontend architecture, frontend quality, templates, setup docs, or meta docs in this prompt.
- Keep the synthesis limited to taskmap design and its interaction with safety/precedence.
```

---

## Slice 9 — Templates and generation defaults

```md
Apply the global rules.

Scope for this prompt only:
- `templates/role-guidelines.template.md`
- `templates/index.template.md`
- `create-role.py`
- `README.md` only if needed to verify claims about template authority

Tasks:
1. Inventory the files that control what future generated roles receive by default.
2. Search the web for best practices on prompt templates, scaffolding defaults, propagation safety, and avoiding placeholder-driven drift.
3. Synthesize whether the generation model produces safe and maintainable starter content.

Important rules:
- Treat templates as generation inputs, not automatically as runtime authority.
- Keep the synthesis limited to template drift, scaffolding behavior, and propagation risk.
```

---

## Slice 10 — Setup and maintainer governance

```md
Apply the global rules.

Scope for this prompt only:
- Files under `setup/`
- Files under `meta/`
- `README.md` only if needed to verify installation or governance claims

Tasks:
1. Inventory the setup guidance and maintainer/governance documentation.
2. Search the web for best practices on prompt-library governance, installation consistency across tools, canonicality policies, and maintenance workflows.
3. Synthesize whether the repository clearly explains ownership, update flow, tool-specific setup, and cross-tool consistency.

Important rules:
- If `setup/` or `meta/` contains many files, start with a directory listing and inspect only the highest-signal files in this prompt.
- Keep the synthesis limited to setup and governance.
```

---

## Slice 11 - Final rollup prompt

```md
Synthesis task.

Use the outputs of the slice prompts as your evidence base.
Do not reread broad areas of the repository unless a specific unresolved question requires a narrowly scoped follow-up.

Tasks:
1. Combine the slice findings into a repository-wide view.
2. Identify the strongest current design choices.
3. Identify the highest-priority gaps, anti-patterns, and contradiction risks.
4. Determine which files should remain canonical where overlap exists.
5. Produce a human-review patch plan.

Output format:

## Files reviewed
List the files and directories actually reviewed across the slice prompts.

## Trusted sources used
List the external high-trust sources actually relied on across the slice prompts.

## Current strengths
List the strongest parts of the standards design.

## Gaps
List missing rules, unclear guidance, or under-specified areas.

## Anti-patterns and risks
Identify contradictions, duplication, outdated guidance, weak safety controls, ambiguous wording, low-verifiability instructions, brittle constraints, over-permissive tool guidance, and any “don’t do that” practices present or insufficiently guarded against.

## Proposed improvements
For each recommendation, provide:
- Priority: High / Medium / Low
- Area affected
- Why it matters
- Proposed replacement text or new text
- Confidence: High / Medium / Low
- Supporting trusted sources

## Suggested patch plan
Group the patch plan as:
- ADD
- EDIT
- REMOVE
- REVIEW

## Source quality notes
Briefly note any areas where only weak sources were available.

Important rules:
- Do not claim a file was reviewed unless it appeared in a slice prompt output.
- Do not say changes were applied.
- Keep recommendations specific, evidence-based, and human-actionable.



```
