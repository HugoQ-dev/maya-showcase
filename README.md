# Maya Rigging & Pipeline TD Showcase

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Maya](https://img.shields.io/badge/Autodesk%20Maya-2022%20--%202026-green.svg)](https://www.autodesk.com/products/maya/)
[![PySide2 / PySide6](https://img.shields.io/badge/GUI-PySide2%20%2F%20PySide6-orange.svg)](https://wiki.qt.io/Qt_for_Python)

Welcome to my Technical Rigging showcase repository. This project serves as a technical portfolio highlighting modular rigging frameworks, matrix-based workflows, and pipeline automation tools developed for production environments.

> **Note on Proprietary Code:** Core production architectures and complete studio tools remain under private development. Each featured tool includes architectural breakdowns, functional demos, and selected code samples (`samples/`) illustrating coding standards, vector/matrix math, and API usage. Standalone scripts in `utilities/` are fully open-source.

---

## 🛠 Tech Stack & Core Competencies

- **Languages & APIs:** Python 3, Maya API 2.0 (`OpenMaya`), `maya.cmds`, MEL
- **Interface & Tooling:** PySide2 / PySide6, Qt Designer, modular MVC architecture
- **Core Specializations:**
  - Matrix-driven rigging (DG performance optimization, cycle-free setups)
  - Modular auto-rigging components (IK/FK switches, stretchy limbs, pole vector locks)
  - Pipeline automation & naming convention enforcement
  - Clean OOP design patterns, type hinting, and PEP 8 compliance

---

## 📌 Featured Tools & Architectural Breakdowns

### 1. [Matrix Constraints Engine](tools/matrix-constraints/)
A high-performance alternative to Maya's legacy constraint nodes, leveraging `multMatrix`, `decomposeMatrix`, and offset parent matrices.
* **Key Features:** Zero DG cyclic dependency risks, native maintain-offset computation via inverted transformation matrices, significant FPS gains in dense evaluation graphs.
* **Tech Focus:** Matrix math, `OpenMaya 2.0`, clean node graph generation.
* **Included:** [Architecture & Demo](tools/matrix-constraints/README.md) | [Sample Code: Offset Math](tools/matrix-constraints/samples/matrix_math.py)

---

### 2. [Modular Rigging Components](tools/modular-rig-components/)
Scalable rigging building blocks designed for seamless integration into studio pipelines.
* **Key Features:** Procedural limb creation, space switching (world/local/root) via matrix layering, seamless IK/FK matching scripts.
* **Tech Focus:** Object-Oriented Programming (OOP), custom attribute serialization, undo chunk safety.
* **Included:** [Architecture & Demo](tools/modular-rig-components/README.md) | [Sample Code: IK/FK Matcher](tools/modular-rig-components/samples/ik_fk_matching.py)

---

### 3. [Scene & Naming Validator](tools/naming-validator/)
A proactive pipeline linting tool built with PySide to enforce strict naming conventions and topological hierarchy checks prior to export.
* **Key Features:** Regex-based naming validation, duplicate transform identifier, one-click hierarchy cleanup.
* **Tech Focus:** PySide UI design, scene traversal, batch error reporting.
* **Included:** [Architecture & Demo](tools/naming-validator/README.md) | [Sample Code: Core Rules Engine](tools/naming-validator/samples/validator_engine.py)

---

## 📦 Open Source Utilities

Fully accessible, plug-and-play Python scripts for daily rigging workflows:

| Utility | Description | Source |
| :--- | :--- | :--- |
| **Zero Out Transforms** | Freezes transforms cleanly using offset parent matrix or group zeroing. | [`utilities/zero_transforms.py`](utilities/) |
| **Joint Chain Align** | Aligns joint orientations along a custom vector using vector projection. | [`utilities/joint_align.py`](utilities/) |

---

## 📁 Repository Structure

```text
maya-showcase/
├── docs/assets/               # Screenshots, diagrams, and demo GIFs
├── tools/                     # Advanced systems (breakdowns + sample code)
│   ├── matrix-constraints/
│   ├── modular-rig-components/
│   └── naming-validator/
├── utilities/                 # Full open-source production helpers
└── README.md
