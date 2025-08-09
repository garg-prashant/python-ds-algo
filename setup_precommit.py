#!/usr/bin/env python3
"""
Setup script for installing and configuring pre-commit hooks.
This script automates the installation of pre-commit hooks for the project.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """
    Run a shell command and handle errors.

    Args:
        command: The command to run
        description: Description of what the command does

    Returns:
        bool: True if successful, False otherwise
    """
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        if e.stderr:
            print(f"   Error output: {e.stderr.strip()}")
        return False


def main():
    """Main setup function."""
    print("🚀 Setting up pre-commit hooks for Python DS Algo project")
    print("=" * 60)

    # Check if we're in the right directory
    if not Path(".pre-commit-config.yaml").exists():
        print("❌ .pre-commit-config.yaml not found in current directory")
        print("   Please run this script from the project root directory")
        sys.exit(1)

    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        print(
            "❌ Failed to install requirements. Please check your Python environment."
        )
        sys.exit(1)

    # Install pre-commit hooks
    if not run_command("pre-commit install", "Installing pre-commit hooks"):
        print("❌ Failed to install pre-commit hooks")
        sys.exit(1)

    # Update pre-commit hooks to latest versions
    if not run_command("pre-commit autoupdate", "Updating pre-commit hooks"):
        print("⚠️  Warning: Failed to update pre-commit hooks, but continuing...")

    # Run pre-commit on all files to test setup
    print("\n🔧 Testing pre-commit setup by running on all files...")
    if run_command("pre-commit run --all-files", "Running pre-commit on all files"):
        print("\n🎉 Pre-commit setup completed successfully!")
    else:
        print("\n⚠️  Pre-commit setup completed, but some files need formatting/fixes.")
        print("   This is normal for initial setup. The hooks will automatically")
        print("   format and check your code on future commits.")

    print("\n📋 What happens now:")
    print("   • pyink will automatically format your Python code before commits")
    print("   • pylint will check for code quality issues")
    print("   • Additional checks for trailing whitespace, file endings, etc.")
    print("   • If any check fails, the commit will be blocked until issues are fixed")
    print(
        "\n💡 Tip: You can run 'pre-commit run --all-files' manually anytime to check all files"
    )


if __name__ == "__main__":
    main()
