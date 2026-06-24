from roles import ROLES


def has_permission(role, action):
    return action in ROLES.get(role, [])