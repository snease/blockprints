---
name: write_requirements
description: Propose and apply section-by-section requirement edits
metadata:
  short-description: Write requirements with simple before/after deltas
---

# Write Requirements

Use this skill when the user asks to edit requirements or PRDs with iterative, section-by-section edits.

## Workflow

Phase 1: Conceptual feedback
1) Review the section and provide numbered, high-level, architectural/conceptual feedback.
2) Iterate with the user until the conceptual feedback is aligned and approved.

Phase 2: Detailed edits
3) Extract the exact original text to replace.
4) Draft the replacement text based on the approved conceptual direction.
5) Present easy-to-see differences using a numbered before → after list of changes.
6) Wait for user approval.
7) Apply the change after approval.

## Notes

- Always propose section-by-section.
- Keep diffs minimal and scoped to the user-approved text.
- If the original text does not match, do not replace; ask the user to re-sync or re-copy the section.
