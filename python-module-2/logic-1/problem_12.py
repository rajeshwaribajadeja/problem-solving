"""Logic-1: in_order problem solution."""


def in_order(a: int, b: int, c: int, b_ok: bool) -> bool:
    """Return True if b is greater than a and c is greater than b.

    However, if b_ok is True, b does not need to be greater than a.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.
        b_ok: Whether b is allowed to be <= a.

    Returns:
        True if the ordering conditions are met, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> in_order(1, 2, 4, False)
        True
        >>> in_order(1, 2, 1, False)
        False
        >>> in_order(1, 1, 2, True)
        True
    """
    return c > b if b_ok else b > a and c > b


if __name__ == "__main__":
    print(in_order(1, 2, 4, False))
    print(in_order(1, 2, 1, False))
    print(in_order(1, 1, 2, True))