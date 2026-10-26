# Quick Joint Align

A lightweight, standalone Autodesk Maya utility to align a joint's world-space position and orientation to a target transform.

---

## 🎯 Purpose

When building deformation skeletons from animation guides or temporary locators, joints often need to snap precisely to reference transforms without manually keying values or using heavy temporary constraints.

This utility copies world-space translation and rotation matrices directly via `maya.cmds.xform`.

---

## 🚀 Usage

Execute directly in the Maya Script Editor (Python):

```python
import maya.cmds as cmds
from utilities.quick_joint_align.joint_align import align_joint_to_target

# Align a joint to a reference locator
align_joint_to_target(cmds, joint="jnt_arm_l", target="loc_arm_guide_l")
```

---

## ⚙ Details

- **Space:** World-space transformation (`ws=True`).
- **Compatibility:** Autodesk Maya 2020 through 2026.
- **Dependencies:** Requires Maya Python environment (`maya.cmds`).
