"""Logic-1: more20 problem solution."""


def more20(n: int) -> bool:
    """Return True if the number is 1 or 2 more than a multiple of 20.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is 1 or 2 more than a multiple of 20, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> more20(20)
        False
        >>> more20(21)
        True
        >>> more20(22)
        True
    """
    return n % 20 in (1, 2)


if __name__ == "__main__":
    print(more20(20))
    print(more20(21))
    print(more20(22))