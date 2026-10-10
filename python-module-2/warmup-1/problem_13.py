"""Warmup-1: int_max problem solution."""


def int_max(a: int, b: int, c: int) -> int:
    """Return the largest of three integers.

    Given three int values, a, b, c, return the largest.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        The maximum integer among a, b, and c.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> int_max(1, 2, 3)
        3
        >>> int_max(1, 3, 2)
        3
        >>> int_max(3, 2, 1)
        3
    """
    return max(a, b, c)


if __name__ == "__main__":
    print(int_max(1, 2, 3))
    print(int_max(1, 3, 2))
    print(int_max(3, 2, 1))