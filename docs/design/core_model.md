# Core Model: Hybrid / IR Pipeline

## Summary

This document describes the proposed **hybrid internal representation (IR) pipeline** for Blockprints. The goal is to combine a scene-graph/object model (for SVG fidelity and custom geometry) with a graph/constraint model (for layout and routing), while keeping determinism and extensibility.

## Goals

- Support SVG as primary input/output with high fidelity.
- Enable constrained auto-layout and auto-routing.
- Preserve manual overrides and mixed auto/manual workflows.
- Allow custom drawings to become first-class API objects with ports/anchors.
- Keep deterministic outputs and stable ordering.

## Non-goals

- Define a full GUI editor.
- Solve all layout/routing algorithms in v1.
- Specify every backend implementation detail.

## Context

- PRD requires multi-layer abstraction, SVG primary I/O, and determinism.
- Research comparison favors hybrid approaches for flexibility but warns about complexity and sync issues.

## Proposed Architecture

### Representations (layers)

1) **Semantic / Graph Layer**
   - Nodes, edges, connectivity, and domain semantics.
   - Constraints and routing intents live here.

2) **Layout / Constraint IR**
   - Normalized constraints, geometry variables, and solver inputs.
   - Stable ordering and IDs for deterministic behavior.

3) **Render / Scene Graph Layer**
   - Concrete geometry, style, and renderable objects.
   - Maps cleanly to SVG and supports import/export.

## IR Layers (Detailed)

### 1) Semantic / Graph Layer (structure + intent)

**Purpose:** capture diagram meaning and connectivity independent of layout.

**Core entities:**
- **Block**: id, type, label, ports, attributes, children (hierarchy)
- **Connection**: id, src_port, dst_port, attributes, routing_intent
- **Group/System**: id, members, constraints, boundary behavior

**Key rules:**
- Stable IDs required.
- No absolute geometry here (only size hints or constraints).

### 2) Layout / Constraint IR (geometry solving)

**Purpose:** normalize constraints and variables for layout/routing solvers.

**Core entities:**
- **Var**: id, kind (x/y/w/h/anchor), domain, locked?
- **Constraint**: id, type (align/spacing/nonoverlap/route), refs, params
- **RouteSpec**: id, edge_ref, style (orthogonal/straight), obstacles

**Notes:**
- Internal layout engines may model Blocks/Connections as nodes/edges.

**Key rules:**
- Deterministic ordering of vars/constraints.
- Pinned geometry becomes locked vars.

### 3) Render / Scene Graph Layer (final geometry + style)

**Purpose:** produce concrete renderable objects for SVG export.

**Core entities:**
- **Shape**: id, geometry (path/rect/text), style, transform
- **Connector**: id, geometry (path), style, markers
- **Group**: id, children, transform

**Key rules:**
- All geometry is absolute or locally transformed.
- Must be sufficient to re‑export to SVG losslessly.

## Pipeline Boundaries

1) **Lowering:** Semantic layer → Layout IR (constraints + vars)
2) **Solving:** Layout IR → resolved geometry
3) **Materialization:** geometry → Scene graph

## Source of Truth

- **Structure/semantics:** Semantic layer
- **Constraints + layout intent:** Layout IR
- **Final geometry + style:** Scene graph

## Serialization (for debugging/tests)

- JSON‑like snapshots per layer (stable ordering)
- Used for determinism tests and regression diffs

## Ports & Anchors

**Concept:** ports are semantic connection points; anchors are concrete geometric points derived during layout/rendering.

### Semantic Layer

- **Port**: id, parent_block_id, name, kind (input/output/bidirectional), constraints (side/edge), attributes
- Ports are first-class and referenced by Connections.

### Layout / Constraint IR

- **AnchorVar**: id, port_id, x/y vars, side constraints, allowed regions
- Routing uses anchors as connection endpoints.

### Render / Scene Graph

- **AnchorPoint**: id, port_id, x/y, marker style
- Rendered as connection attach points (may be hidden or visible).

### Imported SVGs

- Ports may be inferred from SVG metadata (IDs, custom attributes) or specified in API.
- Anchors are resolved from the imported geometry during layout.

### Pipeline (high-level)

1) **Authoring** (Python API)
   - User defines primitives/blocks/connectors/constraints.
2) **Lowering**
   - Compile user objects into semantic graph + constraints.
3) **Layout / Routing**
   - Apply layout and routing strategies to compute geometry.
4) **Rendering**
   - Materialize scene graph for export (SVG).

### Source of Truth

- **Structure/semantics** live in the semantic graph.
- **Geometry** is produced by layout/routing but can be pinned/overridden.
- **Style** lives in the render layer with inheritance from higher layers.

## Determinism Strategy

- Stable IDs at each layer.
- Deterministic solver settings and ordering.
- Explicit pipeline stages with reproducible outputs.

## Extensibility Points

- New diagram types via semantic layer schemas.
- Layout/routing strategies plug into the IR stage.
- Custom shapes and rendering logic in scene graph layer.

## Risks

- Complexity and leaky abstractions between layers.
- Sync problems between graph and scene representations.
- Layout quality might lag without robust routing engines.

## Open Questions

- Exact IR schema and serialization format.
- Layout/routing engine selection and integration details.
- How to represent partial or incremental layout.
