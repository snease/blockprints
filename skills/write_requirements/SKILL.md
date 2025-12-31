---
name: write_requirements
description: Propose and apply section-by-section requirement edits using a diff tool that supports colored output and safe replacements.
metadata:
  short-description: Write requirements with colored diffs and safe replacements
---

# Write Requirements

Use this skill when the user asks to edit requirements or PRDs with iterative, section-by-section edits.

## Workflow

1) Extract the exact original text to replace.
2) Draft the replacement text.
3) Run the diff tool in **propose** mode to show a colored diff.
4) Wait for user approval.
5) Run the diff tool in **replace** mode to apply the change.

## Tool

Use the script:

- `scripts/write_requirements.py <path> <original_text> <replacement_text> <propose|replace>`

Behavior:
- `propose`: print ANSI-colored unified diff.
- `replace`: validate the original text exists, then replace it once and write to file.

## Notes

- Always propose section-by-section.
- Keep diffs minimal and scoped to the user-approved text.
- If the original text does not match, do not replace; ask the user to re-sync or re-copy the section.
