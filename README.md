# Maya Rigging & Pipeline TD Showcase

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Maya](https://img.shields.io/badge/Autodesk%20Maya-2022%20--%202026-green.svg)](https://www.autodesk.com/products/maya/)
[![PySide2 / PySide6](https://img.shields.io/badge/GUI-PySide2%20%2F%20PySide6-orange.svg)](https://wiki.qt.io/Qt_for_Python)

Welcome to my technical rigging showcase repository, designed as a public portfolio hub for 3D animation and VFX studios. It presents technical breakdowns, dependency graphs, performance benchmarks, and representative code samples of production-grade rigging tools for Autodesk Maya.

> [!NOTE]
> **Source Code & IP Policy:**  
> Complete production frameworks, automated pipeline toolsets, and full PySide interfaces are maintained in private repositories to protect intellectual property. Access to complete repositories (including [`HugoQ-dev/constrain-mtx`](https://github.com/HugoQ-dev/constrain-mtx)) can be granted upon request to recruiters, pipeline supervisors, and technical directors for code review.

---

## 🛠 Tech Stack & Core Competencies

- **Languages & APIs:** Python 3, Maya API 2.0 (`OpenMaya`), `maya.cmds`, MEL
- **Interface & Tooling:** PySide2 / PySide6, Qt Designer, modular MVC architecture
- **Core Focus:** Matrix-driven rigging architectures, Parallel Evaluation optimization, cycle-free DG networking, and pipeline tooling

---

## 📌 Featured Tool: Matrix Constraints Engine

A high-performance, matrix-driven constraint engine developed for Autodesk Maya, replacing legacy constraint nodes with lightweight native Dependency Graph (DG) networks.

- **Primary Repository:** Private development repo [`HugoQ-dev/constrain-mtx`](https://github.com/HugoQ-dev/constrain-mtx) *(access granted on request)*.
- **Showcase Breakdown:** [`tools/matrix-constraints/`](tools/matrix-constraints/)

### Highlights & Architecture
- **Supported Network Types:** Transform (Parent), Translation (Point), Rotation (Orient), Scale, Aim, and Pole Vector networks.
- **Maintain Offset Preservation:** Explicit build-time matrix inversion:
  $$\mathbf{M}_{\text{offset}} = \mathbf{M}_{\text{driven\_world}} \times \mathbf{M}_{\text{driver\_world\_inverse}}$$
- **Joint Orient Compensation:** Dedicated inverted `jointOrient` matrix stream ensuring zero axis drifting or flipping on skeletal hierarchies.
- **Weight & Blending:** Channel-level blending via native `blendMatrix` nodes.
- **Parallel Evaluation Ready:** Cycle-free, single-plug dirty propagation, and modern `offsetParentMatrix` (OPM) integration.

👉 **Explore the full technical documentation:** [Matrix Constraints Engine Breakdown & DG Schemas](tools/matrix-constraints/README.md)  
👉 **Inspect the code sample:** [Matrix Math Sample (`matrix_math.py`)](tools/matrix-constraints/samples/matrix_math.py)

---

## 📦 Open Source Utilities

Lightweight, fully open-source helper scripts for daily rigging tasks:

| Utility | Description | Source |
| :--- | :--- | :--- |
| **Zero Out Transforms** | Resets transform channels to neutral rest values (`T=(0,0,0)`, `R=(0,0,0)`, `S=(1,1,1)`). | [`utilities/zero-out-transforms/`](utilities/zero-out-transforms/) |
| **Quick Joint Align** | Direct world-space transformation copy between reference transforms and joints. | [`utilities/quick-joint-align/`](utilities/quick-joint-align/) |

---

## 📁 Repository Structure

```text
maya-showcase/
├── docs/assets/                      # Screenshots, architecture diagrams, demo GIFs
├── tools/
│   ├── matrix-constraints/           # Featured System: Matrix Constraints Engine
│   │   ├── README.md                 # Technical breakdown, DG schemas, and PE analysis
│   │   └── samples/
│   │       └── matrix_math.py        # Representative matrix math implementation
│   └── ...                           # Future modular systems in preparation
├── utilities/                        # Open-source standalone helpers
│   ├── quick-joint-align/            # Joint alignment utility
│   └── zero-out-transforms/          # Transform channel zeroing utility
└── README.md                         # Main portfolio showcase hub
```

---

## 📬 Contact & Code Review Requests

Recruiters, Lead Riggers, and Pipeline Supervisors interested in reviewing the complete codebases, unit test suites, or live Maya tool demonstrations:

- **GitHub:** [@HugoQ-dev](https://github.com/HugoQ-dev)
- **Private Repo Access:** Available upon request for [`HugoQ-dev/constrain-mtx`](https://github.com/HugoQ-dev/constrain-mtx)
