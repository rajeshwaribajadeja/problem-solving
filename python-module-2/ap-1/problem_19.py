"""AP-1: user_compare problem solution."""


def user_compare(name_a: str, id_a: int, name_b: str, id_b: int) -> int:
    """Compare two users, ordering first by name and then by ID.

    Return -1 if user A comes before user B, 1 if user A comes after user B,
    and 0 if they are identical.

    Args:
        name_a: Name of user A.
        id_a: ID of user A.
        name_b: Name of user B.
        id_b: ID of user B.

    Returns:
        -1, 1, or 0 according to user comparison order.

    Complexity:
        Time Complexity: O(min(len(name_a), len(name_b)))
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> user_compare("bb", 1, "zz", 2)
        -1
        >>> user_compare("bb", 1, "aa", 2)
        1
        >>> user_compare("bb", 1, "bb", 1)
        0
    """
    cmp_name = (name_a > name_b) - (name_a < name_b)
    return cmp_name or (id_a > id_b) - (id_a < id_b)


if __name__ == "__main__":
    print(user_compare("bb", 1, "zz", 2))
    print(user_compare("bb", 1, "aa", 2))
    print(user_compare("bb", 1, "bb", 1))