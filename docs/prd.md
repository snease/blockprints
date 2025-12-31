# Blockprints PRD

---

## 1. Overview

### 1.1 Purpose
The goal of this project is to build a diagramming tool that is powerful, programmable, and highly customizable. It gives users an unprecedented amount of control over their diagrams, while also having sensible defaults. The system targets engineers, researchers, and technical users who require precise control over diagram structure (placement, routing, layout etc), styling, and semantics beyond what typical diagram tools provide.

The tool is intended to function as a full-stack diagram ecosystem, spanning low-level drawing primitives through multiple abstraction layers up to high-level diagram constructs, with user control available at every layer. We plan to take advantage of the open-source ecosystem and use existing drawing libraries where we can. We care much more about the final tool than the fancy technology used to create it.

---

## 2. Target Users

- Engineers (especially VLSI / SoC / hardware designers)
- Researchers and scientists
- Software architects
- Educators creating conceptual or algorithmic diagrams
- Advanced technical users comfortable with code-based workflows

---

## 3. Core Use Cases

- Conceptual diagrams for algorithms and scientific ideas
- VLSI / SoC block diagrams and architectural overviews
- Hierarchical system diagrams with reusable, parameterized components
- Diagrams that evolve iteratively as ideas or designs mature
- Domain-specific diagram extensions (future)

---

## 4. Key Product Values

- Programmability: diagrams are described using Python code
- Layered abstraction: users can operate at any abstraction level, from primitives to high-level constructs.
- Customization: users can deeply customize behavior and appearance without breaking the system model.
- Extensibility: the system should support new domains, diagram types, and user-defined primitives.
- Co-existence with manual drawing. The system should enable users to provide their own custom drawings/blocks that can be parameterized and imported into the system.
- Standing on giants' shoulders: the tool should reuse open-source solutions / ideas / standards wherever possible

---

## 5. Functional Requirements

### 5.1 Diagram Description
- Diagrams are defined programmatically using Python.
- The API supports:
  - Declarative specification of structure
  - Parameterization of components
  - Reuse and composition of diagram elements

---

### 5.2 Multi-Layer Architecture

The system shall provide multiple, explicit abstraction layers, including but not limited to:

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

- Users can import external drawings (e.g., images or vector shapes).
- Imported drawings can be promoted to **first-class blocks**.
- Custom blocks must support:
  - Ports and anchors
  - Layout and routing participation
  - Attached automation or behavior

This allows users to escape predefined shapes while remaining within the system.

---

### 5.6 Automation and Behavior Attachment

- Users can attach automation or logic to diagram elements, including:
  - Custom blocks
  - Imported drawings
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

## 6. Non-Goals (Initial Scope)

- WYSIWYG, mouse-driven diagram editing
- Real-time collaborative editing
- Animation

---

## 7. Extensibility Requirements

- Clear APIs for adding:
  - New diagram types
  - New layout or routing strategies
  - Domain-specific abstractions
- The system should not assume a single domain (e.g., only software or only hardware).

---

## 8. Success Criteria

- Users can produce complex diagrams that would be unwieldy in existing tools.
- Diagrams remain readable despite high information density.
- Advanced users can deeply customize diagrams without forking the system.
- The tool feels closer to an **EDA framework for diagrams** than a traditional diagram editor.

---

## 9. Open Questions

- Supported input formats for custom drawings (SVG, PNG, others)
- Output formats and rendering backends
- Performance targets for large diagrams

