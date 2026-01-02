# API Design (Placeholder)

## Summary

This document describes the public Python API surface for Blockprints. The API is **object‑oriented** and centered around Blocks, Ports, and Connections. Parameterization is handled through **user‑defined functions** that map parameters to geometry and constraints.

## Goals

- Make diagram construction ergonomic and composable.
- Support parameterized, reusable blocks.
- Expose layout/routing intent without leaking internal IR details.
- Keep deterministic behavior by default.

## Non-goals

- GUI editor bindings.
- UI/interaction APIs.

## Core Concepts (Draft)

- Diagram
- Block
- Connection
- Port
- Bus
- Library (primitive shapes)
- Parameter + Transform
- Layout / Routing Intent

## API Shape (Draft)

### Diagram

Represents a full diagram with top‑level blocks and connections.

```python
diagram = Diagram()
```

#### Determinism

Determinism is mandatory; outputs should be stable for identical inputs by default.

### Block

Reusable, parameterized component. Users subclass Block and declare ports and geometry.

```python
class ALU(Block):
    def __init__(self, bitwidth: int):
        super().__init__(name="ALU")
        self.bitwidth = bitwidth
        self.in_a = self.port("in_a")
        self.in_b = self.port("in_b")
        self.out = self.port("out")
```

### Port

Semantic connection point on a Block.

```python
alu = ALU(bitwidth=32)
alu.in_a  # Port instance
```

### Connection

Connects two Ports and can include routing hints.

```python
diagram.connect(alu.out, reg.in_)
```

#### Layout / Routing Intent

Users can influence layout and routing without fully specifying geometry.

```python
diagram.layout("hierarchical")
conn = diagram.connect(alu.out, reg.in_)
conn.route("orthogonal")
alu.pin(x=100, y=200)
```

### Layout and Routing Strategies

The API exposes strategy selection and per‑connection overrides.

```python
diagram.layout("hierarchical", direction="LR")
diagram.route("orthogonal")

conn = diagram.connect(alu.out, reg.in_)
conn.route("spline")
conn.avoid([cache, bus])
```

### Constraints, Pinning, and Locking

Non‑overlap is the default; users can explicitly allow overlap when needed.

```python
# Pin a block at a fixed position
alu.pin(x=100, y=200)

# Lock size but allow position to move
alu.lock(width=True, height=True)

# Relative constraints
diagram.align(alu, reg, axis="y")
diagram.spacing(alu, reg, gap=20)

# Default is no-overlap; allow overlap explicitly
diagram.allow_overlap([annotation, highlight_box])
```

### Bus

Represents a multi-port connection (many-to-many).

```python
bus = diagram.bus([alu.out, fpu.out], [reg_a.in_, reg_b.in_])
```

### Libraries / Primitives

The API provides standard **primitive libraries** (e.g., Square, Circle, Text, Path). These primitives can be composed and promoted into Blocks.

```python
square = primitives.Square(size=20)
block = Block.from_primitives([square], name="SquareBlock")
```

### SVG Import

SVGs can be imported as first‑class API objects and promoted to Blocks.
SVG elements with specific attributes may be auto‑translated into Ports.

```python
svg_obj = svg.import_file("icons/adder.svg")
adder = Block.from_svg(svg_obj, name="Adder")
adder.add_port("in_a").at("left", y=10)
adder.add_port("out").at("right", y=10)
```

### SVG Export

SVG export preserves geometry, ports, and styling.

```python
diagram.export_svg("out.svg")
```

### Parameter + Transform

Parameters are stored on the Block; users define **arbitrary functions** that map parameters to geometry and constraints using built‑in API helpers. These functions are invoked by convention (to be defined).

```python
class Grid(Block):
    def __init__(self, num_columns: int):
        super().__init__(name="Grid")
        self.num_columns = num_columns

def grid_transform(block: Grid):
    block.set_grid(columns=block.num_columns)
```

### Hierarchy and Composition

Sub‑diagrams can be embedded as Blocks or Groups.

```python
sub = Diagram()
cpu = CPU()
sub.add(cpu)
top = Diagram()
top.add(sub.as_block(name="Subsystem"))
```

### Styling

Styling can be applied at global, component, or instance level.

```python
diagram.style.default(stroke="black", fill="white")
alu.style(fill="lightgray")
alu.out.style(color="red")
```

### Styling: Themes and Inheritance

Styles inherit from global → block → instance unless overridden.

```python
diagram.theme("clean")
alu.style(stroke_width=2)
```

### Validation and Errors

Validation runs during compilation; errors should surface actionable information tied to elements.

```python
ir, scene = diagram.compile()
```

### Input / Output

SVG is the primary I/O format.

```python
diagram.export_svg("out.svg")
```

### Extensibility Hooks

Users can register new diagram types or layout/routing strategies.

```python
diagram.register_layout("custom", custom_layout_fn)
```

### Custom Diagram Types

Users can define domain‑specific diagram types by subclassing Diagram.

```python
class GanttDiagram(Diagram):
    pass
```

## Open Questions

- API shape (OO vs functional)?
- How are constraints expressed (helpers vs direct constraints)?
- How to represent imported SVGs as API objects?
