# SKILL.md

## Overview

Blockprints follows a structured flow from high-level requirements to low-level implementation. This document outlines how agents should contribute to that flow by co-authoring design artifacts alongside human designers.

Agents are expected to:

* Collaborate on design documents.
* Capture irreversible decisions in Architecture Decision Records (ADRs).
* Produce fully self-contained ExecPlans for implementation.

## Document Hierarchy

The project maintains the following hierarchy:

### 1. Product Requirements Document (PRD)

* **Location:** `docs/prd.md`
* **Authored by:** Human designers (with agent suggestions permitted)
* **Purpose:** Define what the software must do and why it matters
* **Notes:** Agents may propose PRD edits, but human approval is required

### 2. Design Documents

* **Location:** `docs/design/feature_name.md`
* **Authored by:** Designers and agents
* **Purpose:** Describe how a subsystem or capability will be implemented
* **Properties:**

  * Living documents
  * May include multiple related features
  * Serve as the canonical reference for system behavior and structure

### 3. Architecture Decision Records (ADRs)

* **Location:** `docs/adr/feature_name.md`
* **Authored by:** Agents or designers
* **Purpose:** Record high-impact decisions made during design evolution
* **Properties:**

  * One ADR per significant decision
  * Immutable after acceptance, with status (`Proposed`, `Accepted`, etc.)

### 4. Execution Plans (ExecPlans)

* **Location:** `docs/plans/planNNNN_feature_name.md`
* **Authored by:** Agents (with iterative human review)
* **Purpose:** Provide a complete, self-contained plan for a coding agent to deliver a working feature
* **Formatting and lifecycle:** Governed strictly by `docs/plans.md`

## Agent Responsibilities

* Use the PRD as a source of constraints and goals; do not overwrite without explicit instruction
* Assist in authoring and refining design documents with the goal of creating implementation-ready guidance
* Record important decisions made during design doc creation as ADRs in `docs/adr/`
* Generate executable specifications as ExecPlans in `docs/plans/`, conforming strictly to `plans.md`

## Best Practices for Agents

* Respect the document hierarchy and conventions
* Prefer clarity over cleverness
* Reference design documents when generating code, comments, or ExecPlans
* Treat all authored documents as part of a living design system
* Collaborate closely with the designer; escalate ambiguity through the `Decision Log` section in ExecPlans

## File Naming Summary

* PRD: `docs/prd.md`
* Design Docs: `docs/design/feature_name.md`
* ADRs: `docs/adr/feature_name.md`
* ExecPlans: `docs/plans/planNNNN_feature_name.md` (zero-padded global sequence)

## Last Updated

Jan 1, 2026
