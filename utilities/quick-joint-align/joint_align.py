"""Utility to align a joint's transform to a target object."""


def align_joint_to_target(cmds, joint, target):
    """Copy world-space translation and rotation from target to joint."""

    t = cmds.xform(target, q=True, ws=True, t=True)
    r = cmds.xform(target, q=True, ws=True, ro=True)
    cmds.xform(joint, ws=True, t=t)
    cmds.xform(joint, ws=True, ro=r)
