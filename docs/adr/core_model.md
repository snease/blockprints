# ADR: Core Model (Hybrid / IR Pipeline)

## Status

Accepted

## Context

Blockprints needs to support SVG as primary I/O, constrained auto-layout/routing, and a multi-layer API with custom drawings as first-class objects. Pure scene-graph or pure graph-first models each fail to meet all constraints cleanly.

## Decision

Adopt a **hybrid internal model** with an explicit **IR pipeline**:
- Semantic/graph layer for structure and constraints
- Layout/constraint IR for solver integration
- Scene-graph/render layer for SVG fidelity

## Consequences

- **Pros:**
  - Best fit for SVG import/export and graph layout needs.
  - Clear extension points for layouts, routing, and custom shapes.
  - Supports manual overrides and mixed workflows.
- **Cons:**
  - More architectural complexity.
  - Requires careful sync between layers.
  - Determinism must be enforced across pipeline stages.

## Alternatives Considered

- Scene graph / object-first only
- Graph-first only

## References

- `docs/research/diagram_representation.md`
