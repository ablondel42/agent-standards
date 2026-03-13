#!/usr/bin/env python3
"""
Agent Standards Role Scaffolding Tool

Creates a new role folder with the complete standard structure:
- role-guidelines.md
- _index.md
- quality/ folder with placeholder files
- architecture/ folder with placeholder files
- taskmaps/ folder with placeholder files
"""

import sys
from pathlib import Path
from typing import Optional


class RoleScaffolder:
    """Handles creation of new role folders with standard structure."""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.roles_dir = repo_root / "roles"
        self.templates_dir = repo_root / "templates"

    def create_role(self, role_name: str, description: Optional[str] = None) -> None:
        """Create a new role folder with complete structure."""
        role_path = self.roles_dir / role_name

        # Check if role already exists
        if role_path.exists():
            print(f"❌ Error: Role '{role_name}' already exists at {role_path}")
            sys.exit(1)

        print(f"\n🚀 Creating new role: {role_name}")
        print(f"📁 Location: {role_path}\n")

        # Create main role directory
        role_path.mkdir(parents=True, exist_ok=True)

        # Create subdirectories
        subdirs = ["quality", "architecture", "taskmaps"]
        for subdir in subdirs:
            (role_path / subdir).mkdir(exist_ok=True)
            print(f"  ✓ Created {role_name}/{subdir}/")

        # Create role-guidelines.md
        self._create_role_guidelines(role_path, role_name, description)
        print(f"  ✓ Created {role_name}/role-guidelines.md")

        # Create _index.md
        self._create_index(role_path, role_name)
        print(f"  ✓ Created {role_name}/_index.md")

        # Create quality files
        quality_files = [
            "testing.md",
            "security.md",
            "performance.md",
            "observability.md",
            "code-quality.md"
        ]
        for filename in quality_files:
            self._create_placeholder(role_path / "quality" / filename, filename.replace(".md", ""))
        print(f"  ✓ Created {len(quality_files)} quality files")

        # Create architecture files
        architecture_files = [
            "structure.md",
            "patterns.md",
            "data-flow.md",
            "file-organization.md",
            "dependencies.md"
        ]
        for filename in architecture_files:
            self._create_placeholder(role_path / "architecture" / filename, filename.replace(".md", ""))
        print(f"  ✓ Created {len(architecture_files)} architecture files")

        # Create taskmap files
        taskmap_files = [
            "bugfix.md",
            "new-feature.md",
            "refactor.md",
            "test-writing.md",
            "perf-investigation.md",
            "deployment.md"
        ]
        for filename in taskmap_files:
            self._create_taskmap(role_path / "taskmaps" / filename, filename.replace(".md", ""))
        print(f"  ✓ Created {len(taskmap_files)} taskmap files")

        print(f"\n✅ Role '{role_name}' scaffolded successfully!")
        print(f"\n📝 Next steps:")
        print(f"   1. Edit {role_name}/role-guidelines.md to define the role charter")
        print(f"   2. Customize quality, architecture, and taskmap files as needed")
        print(f"   4. Update README.md to mark {role_name} as ✅ available\n")

    def _create_role_guidelines(self, role_path: Path, role_name: str, description: Optional[str]) -> None:
        """Create role-guidelines.md from template."""
        desc = description or f"Production {role_name} development"
        content = f"""# role-guidelines

## {role_name.title()} production charter
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
Never do any of the following without explicit approval:
- Add, remove, or upgrade dependencies
- Change authentication, authorization, roles, permissions, sessions, or security-sensitive flows
- Change environment variables, secrets handling, CSP, headers, cookie behavior, proxying, analytics, telemetry destinations, consent flows, or deployment configuration
- Expose sensitive data, log secrets, weaken validation, disable checks, or add unsafe rendering
- Delete, rename, or move externally significant files or public APIs

## Retrieval strategy
**Start here:**
1. Load `roles/{role_name}/role-guidelines.md` (this file)
2. Load `roles/{role_name}/_index.md` for retrieval guidance
3. Load `shared/_index.md` for cross-cutting guidance map

**Then load only what the task needs.**

The `_index.md` files guide you to the right combination of:
- Shared core workflow and safety files (`shared/core/`)
- Shared risk management files (`shared/risk/`)
- {role_name.title()} quality files (`roles/{role_name}/quality/`)
- {role_name.title()} architecture files (`roles/{role_name}/architecture/`)
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
"""
        (role_path / "role-guidelines.md").write_text(content)

    def _create_index(self, role_path: Path, role_name: str) -> None:
        """Create _index.md retrieval map."""
        content = f"""# {role_name} index

## Purpose
This file helps agents load only the {role_name} guidance relevant to the current task.
Use it after `roles/{role_name}/role-guidelines.md` to decide which {role_name}-specific files and shared cross-cutting files should be loaded.

## Loading strategy
Start small.
Load only the files directly relevant to the task, and pull in shared guidance when the work touches cross-cutting concerns like privacy, logging, approvals, or overall execution safety.

## Start here
For any {role_name} task, begin with:
- `roles/{role_name}/role-guidelines.md`
- `shared/_index.md`

Then load only the additional files needed for the task.

## Load shared files when needed
Use shared guidance for concerns that are not {role_name}-specific:

- `shared/core/workflow.md`
  Load when: you need execution order, change discipline, or validation sequencing.
- `shared/core/scope-and-safety.md`
  Load when: the task may expand in scope, affect external behavior, or touch sensitive systems.
- `shared/core/communication.md`
  Load when: you need guidance on reporting assumptions, blockers, or tradeoffs.
- `shared/core/definition-of-done.md`
  Load when: deciding whether a task is complete enough for production.

- `shared/risk/security-and-privacy.md`
  Load when: the task touches auth, permissions, user data, consent, or trust boundaries.
- `shared/risk/observability-and-logging.md`
  Load when: the task affects logging, monitoring, error catching, or diagnosability.
- `shared/risk/approvals.md`
  Load when: a change may require explicit approval due to risk, scope, compliance, or user impact.
- `shared/risk/secrets-and-sensitive-data.md`
  Load when: the task touches secrets, credentials, tokens, or sensitive operational data.

- `shared/examples/good-task-brief.md`
  Load when: refining task framing.
- `shared/examples/good-plan.md`
  Load when: drafting a concise implementation plan.
- `shared/examples/change-review-checklist.md`
  Load when: reviewing a change before completion.
- `shared/examples/forbidden-patterns.md`
  Load when: checking for risky anti-patterns.

## Load {role_name} quality files
Use these files for {role_name}-specific quality concerns:

- `roles/{role_name}/quality/testing.md`
  Load when: behavior changes require test updates or validation strategy decisions.
- `roles/{role_name}/quality/security.md`
  Load when: the task has {role_name}-specific security implications.
- `roles/{role_name}/quality/performance.md`
  Load when: the task may affect performance or resource usage.
- `roles/{role_name}/quality/observability.md`
  Load when: the task affects {role_name}-specific logging or monitoring.
- `roles/{role_name}/quality/code-quality.md`
  Load when: the task involves code style, clarity, or maintainability decisions.

## Load {role_name} architecture files
Use these files for implementation shape and code organization:

- `roles/{role_name}/architecture/structure.md`
  Load when: the task affects overall code structure or module boundaries.
- `roles/{role_name}/architecture/patterns.md`
  Load when: the task involves design patterns or architectural patterns.
- `roles/{role_name}/architecture/data-flow.md`
  Load when: the task affects data movement, state, or side effects.
- `roles/{role_name}/architecture/file-organization.md`
  Load when: the task affects file placement or import structure.
- `roles/{role_name}/architecture/dependencies.md`
  Load when: the task involves dependency management or external integrations.

## Load taskmaps
Use taskmaps only when the work benefits from a task-specific execution pattern:

- `roles/{role_name}/taskmaps/bugfix.md`
- `roles/{role_name}/taskmaps/new-feature.md`
- `roles/{role_name}/taskmaps/refactor.md`
- `roles/{role_name}/taskmaps/test-writing.md`
- `roles/{role_name}/taskmaps/perf-investigation.md`
- `roles/{role_name}/taskmaps/deployment.md`

Load only the one that matches the current task type.

## Retrieval rules
- Prefer 1 to 4 relevant files over broad context loading.
- Do not load all {role_name} files by default.
- Use shared files for cross-cutting concerns and {role_name} files for {role_name}-specific details.
- If a task touches security, privacy, logging, or approvals, load the relevant shared risk files before implementing.
- If a task crosses role boundaries, start with {role_name} guidance and then load the minimum additional shared or adjacent-role guidance needed.
"""
        (role_path / "_index.md").write_text(content)

    def _create_placeholder(self, filepath: Path, topic: str) -> None:
        """Create a placeholder quality or architecture file."""
        content = f"""# {topic}

## Use this file when
[TODO: Define when this file should be loaded]

## Goal
[TODO: Define the goal of this guidance]

## Core rules
[TODO: Add core rules for {topic}]

## Avoid
[TODO: Add anti-patterns to avoid]
"""
        filepath.write_text(content)

    def _create_taskmap(self, filepath: Path, task_type: str) -> None:
        """Create a taskmap file with standard structure."""
        content = f"""# {task_type}

## Use this file when
[TODO: Define when this taskmap applies]

## Goal
[TODO: Define the goal for this task type]

## Workflow
1. [TODO: Add workflow steps]

## Load these files when relevant
[TODO: List relevant shared and role-specific files]

## Priorities
[TODO: Define priorities for this task type]

## Avoid
[TODO: Add anti-patterns specific to this task type]
"""
        filepath.write_text(content)


def main():
    """CLI entry point."""
    # Simple argument handling without argparse
    if len(sys.argv) < 2:
        print("Usage: python create-role.py <role_name> [-d <description>]")
        sys.exit(1)
    
    role_name = sys.argv[1]
    description = None
    
    # Check for -d flag
    if len(sys.argv) > 2:
        if sys.argv[2] == "-d" and len(sys.argv) > 3:
            description = sys.argv[3]

    # Validate we're in the right repo (must be run from repo root)
    repo_root = Path.cwd()
    if not (repo_root / "roles").exists():
        print(f"❌ Error: 'roles' directory not found in {repo_root}")
        print("   This script must be run from the agent-standards repository root.")
        print(f"   Current directory: {repo_root}")
        sys.exit(1)

    # Create scaffolder and run
    scaffolder = RoleScaffolder(repo_root)
    scaffolder.create_role(role_name, description)


if __name__ == "__main__":
    main()
