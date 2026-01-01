# Blockprints PRD

---

## 1. Overview

### 1.1 Purpose
The goal of this project is to build a diagramming tool that is powerful, programmable, and highly customizable while still providing sensible defaults. It targets technical users who require precise control over diagram structure (placement, routing, layout), styling, and semantics beyond what typical diagram tools provide.

The tool is intended to function as a full-stack diagram ecosystem, spanning low-level drawing primitives through multiple abstraction layers up to high-level diagram constructs, with user control available at every layer. We plan to take advantage of the open-source ecosystem and use existing drawing libraries where we can. We prioritize the capabilities of the final tool over specific implementation choices.

---

## 2. Target Users

- Engineers (hardware, software, systems)
- Researchers and scientists
- Software architects / systems engineers
- Educators creating conceptual or algorithmic diagrams
- Advanced technical users comfortable with code-based workflows

---

## 3. Core Use Cases

- Conceptual diagrams for algorithms and scientific ideas
- Software and hardware architecture block diagrams and overviews (e.g., systems, SoC)
- Hierarchical system diagrams with reusable, parameterized components across projects
- Diagrams that evolve iteratively as ideas or designs mature
- Domain-specific diagram extensions (future)

---

## 4. Key Product Values

- Programmability: diagrams are described as code
- Layered abstraction: users can operate at any abstraction level, from primitives to high-level constructs.
- Customization: users can deeply customize behavior and appearance without breaking the system model.
- Extensibility: the system should support new domains, diagram types, user-defined primitives, and layout/routing strategies.
- Domain-agnostic: the system does not assume a single domain (e.g., Gantt charts, schematics, network diagrams).
- Co-existence with manual drawing: users can mix programmatic diagrams with hand-drawn elements.

### 4.1 Technical Direction (Non-binding)
- Primary authoring API is Python
- Reuse existing open-source drawing/layout libraries where practical
- Support importing custom drawings and promoting them to parameterized blocks
- Favor open standards and reusable ideas where applicable

---

## 5. Functional Requirements

### 5.1 Diagram Description
- Diagrams are defined programmatically using Python and must render deterministically.
- The API supports:
  - Declarative specification of structure
  - Parameterization of components
  - Deterministic outputs (same input → same output)
  - Reuse and composition of diagram elements

---

### 5.2 Multi-Layer Architecture

The system shall provide multiple, explicit abstraction layers (examples below; not exhaustive):

- Low-level primitives (potentially using an existing framework):
  - Shapes, paths, ports, anchors
  - Coordinate and geometry manipulation
- **Mid-level constructs**
  - Blocks, connectors, routing constraints
  - Styling and layout policies
- **High-level constructs**
  - Graphs, block diagrams, hierarchical systems
  - Domain-specific diagram types (pluggable)

Users must be able to override or customize behavior at any layer.

---

### 5.3 Layout and Routing

- Support **constrained auto-placement and auto-routing**.
- Default layouts should produce reasonable results with minimal configuration.
- Users must be able to:
  - Override placement decisions
  - Influence routing constraints
  - Mix automatic and manual control

---

### 5.4 Hierarchy and Composition

- Hierarchy is a first-class concept.
- Diagrams may contain nested sub-diagrams.
- Components can be:
  - Parameterized
  - Reused across diagrams
  - Composed into higher-level structures

---

### 5.5 Custom User-Defined Drawings

- Users can import external drawings (SVG as primary format; others TBD).
- Imported drawings are exposed as **first-class API objects**.
- Custom blocks must support:
  - Ports and anchors
  - Layout and routing participation
  - Attached automation or behavior

This allows users to escape predefined shapes while remaining within the system.

---

### 5.6 Automation and Behavior Attachment

- Users can attach automation or parameters to API objects (including imported SVGs), enabling parameterized variants (e.g., `num_columns` on a grid-like object).
- The API should provide transformation functions that let users map parameters to structural or visual changes in diagram elements.
- Automation may influence:
  - Layout
  - Routing
  - Parameter propagation
  - Structural constraints

---

### 5.7 Styling and Visualization

- Styling is configurable at multiple levels:
  - Global defaults
  - Component-level overrides
  - Instance-level overrides
- Visualization must clearly convey structure, hierarchy, and connectivity.

---

### 5.8 Validation and Error Reporting

- The system must validate constraints, layout conflicts, and invalid structures.
- Errors should be actionable and point to the responsible element or rule.

---

### 5.9 Input and Output Formats

- SVG is the primary input and output format.
- Other formats are TBD and not required for v1.

---

## 6. Non-Goals (Initial Scope)

- WYSIWYG, mouse-driven diagram editing
- Built-in editor or viewer tools
- Real-time collaborative editing
- Interactive or animated presentations

---

## 7. Success Criteria

- Users can produce complex diagrams that would be unwieldy in existing tools.
- Diagrams remain readable despite high information density.
- Advanced users can deeply customize diagrams without forking the system (e.g., layout, routing, styling).
- The tool provides a **full-stack API** from primitives to domain-specific abstractions.

---


