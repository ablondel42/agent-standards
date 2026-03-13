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

    def _render_template(self, template_name: str, **values: str) -> str:
        """Read a template file and render placeholders."""
        template_path = self.templates_dir / template_name
        if not template_path.exists():
            print(f"❌ Error: Template not found: {template_path}")
            sys.exit(1)
        return template_path.read_text().format(**values)

    def _create_role_guidelines(self, role_path: Path, role_name: str, description: Optional[str]) -> None:
        """Create role-guidelines.md from template."""
        role_title = role_name.title()
        content = self._render_template(
            "role-guidelines.template.md",
            role_name=role_name,
            role_title=role_title,
            description=description or f"Production {role_name} development",
        )
        (role_path / "role-guidelines.md").write_text(content)

    def _create_index(self, role_path: Path, role_name: str) -> None:
        """Create _index.md retrieval map from template."""
        content = self._render_template(
            "index.template.md",
            role_name=role_name,
            role_title=role_name.title(),
        )
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
