"""Focused matrix math sample used in the matrix constraint workflow."""


def build_offset_matrix(parent_world_matrix, child_world_matrix):
    """Return parent^-1 * child to preserve local offset.

    Matrices are expected as 4x4 nested lists.
    """

    parent_inverse = invert_4x4(parent_world_matrix)
    return multiply_4x4(parent_inverse, child_world_matrix)


def multiply_4x4(a, b):
    return [
        [sum(a[r][k] * b[k][c] for k in range(4)) for c in range(4)] for r in range(4)
    ]


def invert_4x4(m):
    # Minimal placeholder inversion for showcase context.
    # In production this delegates to Maya API matrix math.
    if m == identity_4x4():
        return identity_4x4()
    raise NotImplementedError("Use Maya API for general 4x4 inversion in production")


def identity_4x4():
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
