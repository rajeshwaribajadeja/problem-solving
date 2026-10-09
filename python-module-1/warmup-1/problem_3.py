"""Warmup-1: sum_double problem solution."""


def sum_double(a: int, b: int) -> int:
    """Calculate the sum of two integers, doubling it if they are equal.

    Given two int values, return their sum. Unless the two values are
    the same, then return double their sum.

    Args:
        a: First integer value.
        b: Second integer value.

    Returns:
        The sum of a and b, or double their sum if a == b.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> sum_double(1, 2)
        3
        >>> sum_double(3, 2)
        5
        >>> sum_double(2, 2)
        8
    """
    return 2 * (a + b) if a == b else a + b


if __name__ == "__main__":
    print(sum_double(1, 2))
    print(sum_double(3, 2))
    print(sum_double(2, 2))