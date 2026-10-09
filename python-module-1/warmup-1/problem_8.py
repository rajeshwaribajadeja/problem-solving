"""Warmup-1: pos_neg problem solution."""


def pos_neg(a: int, b: int, negative: bool) -> bool:
    """Check signs of two integers based on whether negative mode is enabled.

    Given 2 int values, a and b, return True if one is positive and one
    is negative. If the parameter "negative" is True, return True only if
    both are negative.

    Args:
        a: First integer.
        b: Second integer.
        negative: If True, requires both a and b to be negative.

    Returns:
        True if condition is met, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> pos_neg(1, -1, False)
        True
        >>> pos_neg(-1, -1, False)
        False
        >>> pos_neg(-4, -5, True)
        True
    """
    return (a < 0 and b < 0) if negative else (a * b < 0)


if __name__ == "__main__":
    print(pos_neg(1, -1, False))
    print(pos_neg(-1, -1, False))
    print(pos_neg(-4, -5, True))