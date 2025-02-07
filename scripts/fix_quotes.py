#!/usr/bin/env python3
"""Script to convert double quotes to single quotes in Python files."""

import os
import re
import sys
from pathlib import Path


def fix_quotes(file_path: str) -> None:
    """Fix quotes in a Python file."""
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # Skip lines that already use single quotes correctly
        if not any(c in line for c in ['"', "'''"]):
            new_lines.append(line)
            continue

        # Handle triple quotes first
        if '"""' in line:
            line = line.replace('"""', "'''")

        # Handle f-strings with nested quotes
        def replace_fstring(match):
            fstring = match.group(0)
            # If the f-string contains single quotes, use double quotes
            if "'" in fstring[2:-1]:  # content between f" and "
                return fstring
            # Otherwise convert to single quotes
            return f"f'{fstring[2:-1]}'"

        line = re.sub(r'f"[^"]*"', replace_fstring, line)

        # Handle regular strings
        def replace_quotes(match):
            text = match.group(0)
            # Skip if it's an f-string (already handled)
            if text.startswith('f"'):
                return text
            # Skip if it contains single quotes
            if "'" in text:
                return text
            return "'" + text[1:-1] + "'"

        line = re.sub(r'"(?:[^"\\]|\\.)*"', replace_quotes, line)
        new_lines.append(line)

    # Write back the changes
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Fixed quotes in {file_path}")


def main():
    """Main function."""
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("Error: backend directory not found")
        sys.exit(1)

    python_files = []
    for root, _, files in os.walk(backend_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                if "venv" not in file_path and ".git" not in file_path:
                    python_files.append(file_path)

    for file_path in python_files:
        fix_quotes(file_path)


if __name__ == "__main__":
    main()
