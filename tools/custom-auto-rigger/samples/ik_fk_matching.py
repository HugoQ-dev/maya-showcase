"""Focused IK/FK matching sample used by the custom auto-rigger."""


def compute_fk_rotations_from_ik(joint_positions, ik_effector_position):
    """Return target FK rotations for a simplified 2-bone chain.

    This keeps the snippet concise for portfolio visibility.
    """

    shoulder, elbow, wrist = joint_positions
    upper_vec = [elbow[i] - shoulder[i] for i in range(3)]
    lower_vec = [wrist[i] - elbow[i] for i in range(3)]
    reach_vec = [ik_effector_position[i] - shoulder[i] for i in range(3)]
    return {
        "shoulder_aim_vector": normalize(reach_vec),
        "elbow_plane_vector": normalize(cross(upper_vec, lower_vec)),
    }


def normalize(vector):
    length = sum(v * v for v in vector) ** 0.5
    if not length:
        return [0.0, 0.0, 0.0]
    return [v / length for v in vector]


def cross(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
