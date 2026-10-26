"""Compact naming validator sample."""

import re

RULES = {
    "joint": re.compile(r"^jnt_[a-z0-9_]+$"),
    "control": re.compile(r"^ctrl_[a-z0-9_]+$"),
    "group": re.compile(r"^grp_[a-z0-9_]+$"),
}


def validate_name(node_type, node_name):
    pattern = RULES.get(node_type)
    if pattern is None:
        return False, f"Unsupported node type: {node_type}"
    valid = bool(pattern.match(node_name))
    return valid, "ok" if valid else f"Invalid {node_type} name: {node_name}"
