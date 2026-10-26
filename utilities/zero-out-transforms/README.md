# Zero-Out Transforms

A standalone production utility for resetting Maya transform attributes to neutral rest values.

---

## 🎯 Purpose

Pre-rigging cleanup frequently requires resetting unneeded channel offsets across control groups and helper nodes. This utility reliably resets translation and rotation channels to `0.0` and scales to `1.0`.

---

## 🚀 Usage

Execute directly in the Maya Script Editor (Python):

```python
import maya.cmds as cmds
from utilities.zero_out_transforms.zero_transforms import zero_out_transform

# Reset channels for a target transform
zero_out_transform(cmds, node="ctrl_hand_l")
```

---

## ⚙ Details

- **Channels Reset:**
  - `translateX`, `translateY`, `translateZ` $\to 0.0$
  - `rotateX`, `rotateY`, `rotateZ` $\to 0.0$
  - `scaleX`, `scaleY`, `scaleZ` $\to 1.0$
- **Compatibility:** Autodesk Maya 2020 through 2026.
- **Dependencies:** Requires Maya Python environment (`maya.cmds`) or compatible mock.
