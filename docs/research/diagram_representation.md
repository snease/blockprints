# Internal Diagram Representation: Scene Graph vs Graph Model vs Hybrid Approaches

**Overview:** Choosing an internal representation for a diagramming tool is a foundational decision that affects the API, extensibility, layout capabilities, and interoperability of the system. The dominant models in industry and academia fall into three broad categories: (1) **Scene Graph / Object-First**, (2) **Graph-First (Node–Edge)**, and (3) **Hybrid or Intermediate Representation (IR) Pipelines** that combine aspects of both. Each approach carries distinct trade-offs in **expressiveness**, **layout and routing quality**, **SVG/vector format compatibility**, **extensibility**, and **determinism** of diagram generation.

> Note: This write-up is formatted for a `*.md` file. Citations are inline and point to sources mentioned in the “Sources” section.

---

## Annotated Comparison Table

| Criteria | Scene Graph / Object-First | Graph-First (Nodes & Edges) | Hybrid / IR Pipeline |
|---|---|---|---|
| **Core Idea** | Diagram is a **scene graph** of graphic objects (shapes, groups, connectors) with explicit geometry and style as first-class. | Diagram is an abstract **graph** (nodes/edges + attributes). Geometry is computed or stored separately. | System accepts both object- and graph-centric input; uses a pipeline that **transforms/compiles** between representations (e.g., objects → graph layout → objects). |
| **Expressiveness** | **High**: arbitrary geometry, transformations, custom shapes, grouping; natural for “drawn” content. | **Medium**: excellent for block/network diagrams; less natural for arbitrary illustrations. Complex visuals often treated as labels/images. | **High** (potentially): supports detailed shapes plus graph semantics—but only if compilation preserves needed structure. |
| **Layout & Routing** | Not intrinsic; requires separate layout/routing engine or constraints. Manual placement common unless augmented. | Natural fit; many mature graph layout/routing algorithms available (hierarchical, orthogonal, force-directed, etc.). | Can combine best: graph-based layout for connectivity + object-level constraints/manual overrides; harder to implement cleanly. |
| **SVG Interop** | **Excellent**: maps directly to SVG concepts; import/export is straightforward and fidelity-preserving. | Indirect: graph must render to SVG; SVG import often becomes an “opaque” node image/symbol rather than editable geometry. | Can be good if pipeline terminates in a scene graph for rendering/export; import can be supported via embedding objects into the object layer. |
| **Extensibility** | Easy to add new shapes/rendering behaviors; harder to add robust layout/routing behaviors without extra systems. | Easy to add new graph algorithms and domain rules; harder to support arbitrary visuals without custom render/templates. | Many extension points (shapes, constraints, layouts, DSLs), but maintaining coherence across layers is complex. |
| **Determinism** | Very high by default: geometry + style → deterministic rendering. Solvers can be deterministic if configured. | Typically deterministic for hierarchical/orthogonal; force-directed may need fixed seed or deterministic mode. | Determinism achievable by controlling each stage and stabilizing ordering/solvers; must guard against nondeterminism in any pipeline step. |

---

## 1) Scene Graph / Object-First Model

A *scene graph* model represents a diagram primarily as a hierarchy of drawn objects (shapes, paths, text, groups), each with explicit geometry and style. This aligns closely with how SVG/vector editors represent drawings (objects + transforms + styling).

### Strengths

- **Visual expressiveness**: arbitrary geometry, custom shapes, nested groups, transforms (scale/rotate), and rich styling are native.
- **SVG interoperability**: highly natural import/export since scene graphs map well to SVG structure and semantics.
- **Deterministic rendering**: given the same object tree and properties, output is reproducible and stable.
- **Hierarchy and composition**: grouping and nesting directly support “sub-diagrams” and reusable components.

### Weaknesses

- **Layout/routing is extra work**: scene graphs do not inherently solve graph layout problems; robust auto-layout and edge routing require additional algorithms/solvers.
- **Graph algorithms are indirect**: connectivity-driven queries/algorithms aren’t first-class unless you separately model them.
- **Can feel verbose for graph-centric users**: specifying placement and anchors explicitly may be more detailed than “just connect A to B.”

### Representative references / examples

- **Scene graphs as a foundational concept** appear broadly in graphics systems and vector editors.
- Some frameworks explicitly choose scene graph as the single source of truth to avoid the “sync” problems of maintaining separate model/view structures.

---

## 2) Graph-First (Nodes & Edges) Model

A graph-first model treats the diagram as an abstract graph: **nodes** and **edges** (plus attributes like labels, sizes, and types). The system then computes geometry via layout/routing algorithms and renders it.

### Strengths

- **Best fit for auto-layout/routing**: graph drawing algorithms are mature and widely available (hierarchical, orthogonal, circular, force-directed, etc.).
- **Connectivity is first-class**: semantic structure is explicit and easy to query/transform; domain rules validate naturally.
- **Scales for large graphs**: computation can be optimized around a simpler abstract model.

### Weaknesses

- **SVG import is awkward**: raw SVG is usually treated as a node image/symbol, not decomposed into geometry that participates fully in routing/anchors.
- **Less natural for arbitrary drawings**: custom shapes beyond bounding boxes often require templating or low-level render extension.
- **Manual + auto mixing can be hard**: “layout jitter” (small changes producing big layout changes) and fighting the layout engine can frustrate users unless the tool supports pinning/constraints/incremental layout.

### Representative references / examples

- **Graphviz**: DOT language describes nodes/edges; layout engines compute positions; outputs include SVG.
- **Commercial layout toolkits** (e.g., yFiles) provide rich sets of graph layout algorithms and routing options.
- Many “diagram-as-code” tools build an internal graph and render to SVG.

---

## 3) Hybrid / Intermediate Representation (IR) Pipeline

Hybrid approaches keep both paradigms available, or introduce an IR that allows compilation/transformation between them. Typical patterns include:

1. **Model + View architecture**: a graph/semantic model plus a rendered scene graph view.
2. **Compilation pipeline**: high-level spec → constraints/graph IR → solved geometry → scene graph/SVG.
3. **Graph-augmented scene**: scene graph as primary, but graph relations are inferred or attached to enable layout/routing on demand.

### Strengths

- **Flexibility**: supports object-centric workflows (precise visuals, SVG import) and graph-centric workflows (auto layout/routing).
- **Layered abstraction**: naturally supports your PRD’s multi-layer architecture (primitives → blocks/connectors → high-level graphs/domains).
- **Best path for “manual + auto”**: you can pin positions, run layout on a subgraph, preserve stable parts, etc.
- **Extensibility across layers**: plug-in layouts, routing engines, constraints, domain DSLs, custom shapes.

### Weaknesses

- **Architecture complexity**: two abstractions and conversion logic; risk of leaky abstractions.
- **Sync issues**: ensuring object geometry and graph relations remain consistent is hard.
- **Determinism requires discipline**: each stage must be deterministic or seeded; ordering and solver stability matter.

### Representative references / examples

- **Penrose** (academia): diagrams as compilation + constraint optimization pipeline, enabling high-level specs that produce geometry.
- **Mermaid** and similar tools: text spec → internal graph → layout engine → SVG output, sometimes supporting alternate layout engines.

---

## Alternatives & “Questioning Assumptions”

While “scene graph vs graph vs hybrid” covers most dominant practice, a few adjacent framings are worth considering:

- **Constraint-first**: represent diagrams primarily as constraints over objects (alignment, spacing, non-overlap, routing constraints). This often manifests as a hybrid: constraints form a dependency graph, while objects form a scene graph. Constraint solvers can be the “core engine” rather than graph layout algorithms.
- **Typed intermediate representations**: treat diagrams more like a compiler target with explicit IR stages (semantic IR, layout IR, render IR), each with deterministic lowering passes. This is effectively hybrid, but with clearer separation and debugging hooks.
- **Topological vs geometric primacy**: some diagram categories are essentially topological (connectivity matters most), while others are geometric (exact shape/space matters). A single universal “primary” model can be a mismatch unless you provide escape hatches and multiple layers.

---

## Alignment to Blockprints PRD (Implications)

Given the PRD requirements:

- **SVG is primary I/O** → strong pressure toward a **scene-graph-compatible render model**.
- **Constrained auto-placement + auto-routing** → strong pressure toward **graph algorithms and/or constraint solvers**.
- **Hierarchy, composition, reuse, multi-layer API** → suggests multiple explicit layers (semantic model + render model).
- **Imported drawings as first-class objects with ports/anchors** → argues for treating imported SVG as real geometry, not opaque images.
- **Users can override at any layer** → suggests a pipeline with explicit stages/IR, where users can hook into layout/routing passes.

**Practical conclusion:** a **hybrid architecture** with a scene-graph-like render representation (for SVG fidelity and custom drawings), plus a graph/constraint representation for layout and routing, most closely matches the PRD. The key design task is to prevent abstraction leaks by (a) making stage boundaries explicit, (b) supporting pinning/constraints and partial layout, (c) providing deterministic layout/routing with stable ordering/IDs, and (d) defining a clear “source of truth” for each attribute (structure, geometry, style).

---

## Sources (Pointers)

> This section lists the types of sources referenced by the original write-up: conceptual references, industry tool docs/manuals, and representative systems.

- Scene graph concept and typical usage in graphics systems / vector rendering.
- FXDiagram author discussions of choosing scene-graph-as-truth to avoid model/view sync issues.
- Graph drawing/toolkit documentation (e.g., Graphviz; commercial toolkits such as yFiles) emphasizing graph layouts and routing.
- mxGraph internal model (draw.io heritage) as an example of a graph model storing geometry/structure.
- Mermaid documentation describing multiple layout engine options (e.g., Dagre vs ELK) via a pipeline.
- Academic and system papers around constraint-based diagramming and compilation pipelines (e.g., Penrose).

---
