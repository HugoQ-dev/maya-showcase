"""Utility to zero transform channels for a given Maya transform node."""


def zero_out_transform(cmds, node):
    """Set translate/rotate to 0 and scale to 1.

    `cmds` is expected to be `maya.cmds` or a compatible mock.
    """

    for axis in "XYZ":
        cmds.setAttr(f"{node}.translate{axis}", 0)
        cmds.setAttr(f"{node}.rotate{axis}", 0)
        cmds.setAttr(f"{node}.scale{axis}", 1)
