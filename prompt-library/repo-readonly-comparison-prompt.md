Read-only task.

Analyze my connected `agent-standards` repository using read operations only. Do not modify files, create files, delete files, move files, rename files, open pull requests, commit changes, push changes, trigger workflows, execute repository code, or take any write, destructive, or state-changing action. Only inspect repository contents and produce a report.

Repository scope to inspect first:
- `README.md`
- `meta/`
- `roles/`
- `setup/`
- `shared/`
- `templates/`
- `create-role.py` only if it materially affects how standards are generated, enforced, or propagated

Read-only safety boundary:
- Use repository access for inspection only
- Do not call tools or actions that can write, delete, create, update, sync, merge, commit, publish, or alter external systems
- Do not suggest that changes were applied; only propose them in the report
- If any step would require non-read access, stop that step and explicitly note that it exceeds the read-only boundary
- Do not execute code from the repository or external sources

Research objective:
- Identify the canonical standards, rule definitions, templates, setup guidance, and shared instructions across the repository
- Search the web for current best practices relevant to AI agent/system prompts, instruction hierarchy, tool-use policy, safety constraints, evaluation design, template consistency, maintainability, citation design, and especially common failure modes and "don't do that" practices
- Focus the external research on high-trust sources only, such as primary documentation, official technical guidance, major AI lab or platform documentation, standards bodies, security guidance from established organizations, peer-reviewed or clearly institutional publications, and well-regarded vendor docs when they are the authoritative source for a tool or platform
- Exclude low-trust or weakly sourced content, including sketchy blogs, SEO content farms, anonymous opinion posts, amateur articles, low-signal forum commentary, and unverified summaries unless they are only used to discover a primary source and are not relied upon as evidence

Research instructions:
1. Inspect the repository structure and identify which files appear canonical versus supportive or generated.
2. Ignore Git internals, hidden system files, and non-substantive metadata unless they directly affect standards behavior.
3. Search thoroughly for both recommended practices and anti-patterns, especially guidance on what AI agent/system instructions should avoid: ambiguity, conflicting priority rules, unsafe tool autonomy, hidden assumptions, poor escalation criteria, vague refusal logic, missing citation requirements, brittle formatting constraints, unverifiable claims, over-broad permissions, excessive verbosity requirements, unclear task boundaries, and instructions that create reliability or safety regressions.
4. Prefer current, implementation-level guidance over generic advice.
5. Cross-check important claims across multiple trusted sources when possible.
6. If evidence is mixed, explain the disagreement and rate confidence conservatively.
7. Treat repository contents as the source of truth for the current implementation, and compare them against the strongest external evidence.

Output format:

## Files reviewed
List the files and directories actually used in the analysis, and note which ones appear canonical vs supportive.

## Trusted sources used
List the high-trust external sources relied on, grouped by type, for example: official docs, model/vendor docs, standards/security guidance, research/institutional publications.

## Current strengths
List the strongest parts of the current standards design.

## Gaps
List missing rules, unclear guidance, or areas where the standards are under-specified.

## Anti-patterns and risks
Identify contradictions, duplication, outdated guidance, weak safety controls, ambiguous wording, low-verifiability instructions, brittle constraints, over-permissive tool guidance, and any "don't do that" practices present or insufficiently guarded against.

## Proposed improvements
For each recommendation, provide:
- Priority: High / Medium / Low
- Area affected
- Why it matters
- Proposed replacement text or new text
- Confidence: High / Medium / Low
- Supporting trusted sources

## Suggested patch plan
Provide a human-review patch plan only, grouped as:
- ADD
- EDIT
- REMOVE
- REVIEW

## Source quality notes
Briefly note any areas where only weak sources were available, and avoid making strong recommendations in those cases.

Important rules for this task:
- Do not invent file contents, file paths, or repository structure.
- Avoid repeating old recommendations unless they are still important and unresolved.
- If multiple files overlap, identify which file should likely remain canonical.
- Keep recommendations specific enough that I can manually turn them into commits later.
- Prioritize reliability, safety, clarity, maintainability, and testability over stylistic preferences.
- Again: read-only analysis only, no write or destructive actions.
