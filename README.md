# Maya Rigging & Pipeline TD Showcase

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Maya](https://img.shields.io/badge/Autodesk%20Maya-2022%20--%202026-green.svg)](https://www.autodesk.com/products/maya/)
[![PySide2 / PySide6](https://img.shields.io/badge/GUI-PySide2%20%2F%20PySide6-orange.svg)](https://wiki.qt.io/Qt_for_Python)

Welcome to my technical rigging showcase repository, featuring modular rigging systems, matrix-based workflows, and pipeline automation tools for Autodesk Maya.

> **Note:** Production architectures and complete studio tools remain private. Featured projects provide technical breakdowns, demos, and representative samples.

---

## 🛠 Tech Stack & Core Competencies

- **Languages & APIs:** Python 3, Maya API 2.0 (`OpenMaya`), `maya.cmds`, MEL
- **Interface & Tooling:** PySide2 / PySide6, Qt Designer, modular MVC architecture
- **Specializations:** Matrix-driven rigging, modular auto-rigging, IK/FK workflows, pipeline automation, and technical-art tooling

---

## 📌 Featured Tools & Architectural Breakdowns

### 1. [Matrix Constraints Engine](tools/matrix-constraints/)

A lightweight matrix-based constraint toolkit for Autodesk Maya, developed in [`HugoQ-dev/constrain-mtx`](https://github.com/HugoQ-dev/constrain-mtx).

It provides a native-style workflow for creating **Parent, Point, Orient, Scale, Aim, and Pole Vector** networks using Maya matrix nodes instead of traditional constraint nodes.

- Maintain-offset support and weighted transforms
- Per-axis translation, rotation, and scale control
- Joint-orient compensation and aim world-up modes
- Automatic Node Editor bookmarks and optional Outliner indicators

* **Tech Focus:** Matrix math, Maya API 2.0, dependency-graph design, and readable rigging networks.
* **Included:** [Architecture & Demo](tools/matrix-constraints/README.md) | [Source Repository](https://github.com/HugoQ-dev/constrain-mtx)

---

### 2. [Modular Rigging Components](tools/modular-rig-components/)

Scalable rigging building blocks designed for seamless integration into studio pipelines.

- **Key Features:** Procedural limb creation, space switching, and IK/FK matching.
- **Tech Focus:** OOP, custom attribute serialization, and undo-chunk safety.
- **Included:** [Architecture & Demo](tools/modular-rig-components/README.md) | [Sample Code: IK/FK Matcher](tools/modular-rig-components/samples/ik_fk_matching.py)

---

### 3. [Scene & Naming Validator](tools/naming-validator/)

A proactive PySide-based pipeline tool for naming validation and hierarchy checks before export.

- **Key Features:** Regex validation, duplicate detection, and hierarchy cleanup.
- **Tech Focus:** PySide UI design, scene traversal, and batch reporting.
- **Included:** [Architecture & Demo](tools/naming-validator/README.md) | [Sample Code: Core Rules Engine](tools/naming-validator/samples/validator_engine.py)

---

## 📦 Open Source Utilities

| Utility | Description | Source |
| :--- | :--- | :--- |
| **Zero Out Transforms** | Freezes transforms using offset parent matrix or group zeroing. | [`utilities/zero_transforms.py`](utilities/) |
| **Joint Chain Align** | Aligns joint orientations along a custom vector. | [`utilities/joint_align.py`](utilities/) |

---

## 📁 Repository Structure

```text
maya-showcase/
├── docs/assets/               # Screenshots, diagrams, and demo GIFs
├── tools/                     # Advanced systems and technical breakdowns
│   ├── matrix-constraints/
│   ├── modular-rig-components/
│   └── naming-validator/
├── utilities/                 # Open-source production helpers
└── README.md
```
