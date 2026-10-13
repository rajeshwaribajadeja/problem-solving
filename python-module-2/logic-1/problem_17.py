"""Logic-1: max_mod5 problem solution."""


def max_mod5(a: int, b: int) -> int:
    """Return the larger value, unless they have the same mod 5 remainder.

    Given two int values, return whichever value is larger. However, if the
    two values have the same remainder when divided by 5, return the smaller
    value. If the two values are the same, return 0.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        0 if equal; smaller value if remainder mod 5 matches; larger value otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> max_mod5(2, 3)
        3
        >>> max_mod5(6, 2)
        6
        >>> max_mod5(3, 2)
        3
    """
    return 0 if a == b else min(a, b) if a % 5 == b % 5 else max(a, b)


if __name__ == "__main__":
    print(max_mod5(2, 3))
    print(max_mod5(6, 2))
    print(max_mod5(3, 2))