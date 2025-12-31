#!/usr/bin/env python3
import sys
from pathlib import Path
import difflib

RED = "\x1b[31m"
GREEN = "\x1b[32m"
CYAN = "\x1b[36m"
RESET = "\x1b[0m"


def usage() -> None:
    print(
        "Usage: write_requirements.py <path> <original_text> <replacement_text> <propose|replace>",
        file=sys.stderr,
    )


def color_line(line: str) -> str:
    if line.startswith("+++") or line.startswith("---"):
        return f"{CYAN}{line}{RESET}"
    if line.startswith("+"):
        return f"{GREEN}{line}{RESET}"
    if line.startswith("-"):
        return f"{RED}{line}{RESET}"
    return line


def unified_diff(old: str, new: str, path: str) -> str:
    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=f"a/{path}",
        tofile=f"b/{path}",
        lineterm="",
    )
    return "\n".join(color_line(line) for line in diff)


def main() -> int:
    if len(sys.argv) != 5:
        usage()
        return 2

    path = sys.argv[1]
    original = sys.argv[2]
    replacement = sys.argv[3]
    mode = sys.argv[4]

    file_path = Path(path)
    if not file_path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 1

    if mode not in {"propose", "replace"}:
        print("Error: mode must be 'propose' or 'replace'", file=sys.stderr)
        return 2

    if mode == "propose":
        print(unified_diff(original, replacement, path))
        return 0

    # replace mode
    content = file_path.read_text()
    if original not in content:
        print("Error: original text not found in file; aborting.", file=sys.stderr)
        return 1

    new_content = content.replace(original, replacement, 1)
    file_path.write_text(new_content)
    print(unified_diff(original, replacement, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
