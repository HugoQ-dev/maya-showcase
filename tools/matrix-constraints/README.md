# Matrix Constraints Engine

A lightweight, high-performance matrix-based constraint system for Autodesk Maya. Designed to eliminate evaluation bottlenecks, avoid cycle dependencies, and replace legacy Maya constraint nodes using native matrix math and DG connections.

![Matrix Constraint Demo](../../docs/assets/matrix_constraint_demo.gif)

---

## 🎯 Overview & Purpose

Legacy Maya constraint nodes (`parentConstraint`, `pointConstraint`, etc.) introduce unnecessary Dependency Graph (DG) complexity, pairBlend clutter, and potential cycle evaluation warnings in complex rigs.

This tool builds constraints dynamically using native matrix operations (`multMatrix`, `decomposeMatrix`, or Maya's `offsetParentMatrix`), drastically reducing node count and ensuring optimal performance under Maya's Parallel Evaluation and GPU deformer engines.

---

## ✨ Key Features

- **Constraint Types Supported:**
  - **Transform (Parent):** Drives translate, rotate, and scale via `multMatrix` and `decomposeMatrix`.
  - **Translate Only (Point):** Isolated translation extraction.
  - **Rotate Only (Orient):** Isolated rotation extraction.
  - **Scale Only:** Dedicated matrix scaling connection.
  - **Aim & Look-At:** Vector math computed through matrix construction.
- **Maintain Offset Preservation:**
  - Automatically computes the initial relative offset via inverted matrix multiplication:
    $$\text{Offset} = \text{DrivenWorldMatrix} \times \text{DriverWorldInverseMatrix}$$
- **Cycle-Free Architecture:** Eliminates cyclic dependency issues frequently seen in space switching and complex rig hierarchies.
- **Modern Maya Ready:** Full support for `offsetParentMatrix` (OPM) integration to maintain completely zeroed transform channels.

---

## 📊 Technical Comparison & Benchmark

| Feature | Legacy Maya Constraints | Matrix Constraints Engine |
| :--- | :--- | :--- |
| **Node Count per Target** | 1 heavy constraint node + blends | 1 `multMatrix` + 1 `decomposeMatrix` |
| **Transform Channels** | Locked or polluted with blend values | Clean, zeroed or directly driven via OPM |
| **Graph Evaluation** | Serial bottlenecks common | Optimized for Maya Parallel Evaluation |
| **Maintain Offset** | Opaque internal calculation | Explicit, mathematical matrix inversion |

---

## 🧠 Mathematical Architecture

To maintain the driven object's position relative to the driver without manual grouping or pops, the relative transformation matrix is computed at build time:

```text
[Driven World] = [Driver World] * [Driven Local Offset]
=> [Driven Local Offset] = [Driven World] * [Driver World Inverse]
