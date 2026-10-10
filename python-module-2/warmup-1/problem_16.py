"""Warmup-1: max1020 problem solution."""


def max1020(a: int, b: int) -> int:
    """Return the larger value in range 10..20 inclusive, or 0 if neither is.

    Given 2 positive int values, return the larger value that is in the
    range 10..20 inclusive, or return 0 if neither is in that range.

    Args:
        a: First positive integer.
        b: Second positive integer.

    Returns:
        The larger integer within 10..20, or 0 if neither qualifies.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> max1020(11, 19)
        19
        >>> max1020(19, 11)
        19
        >>> max1020(11, 9)
        11
    """
    return max(a if 10 <= a <= 20 else 0, b if 10 <= b <= 20 else 0)


if __name__ == "__main__":
    print(max1020(19, 11))
    print(max1020(11, 19))
    print(max1020(11, 9))