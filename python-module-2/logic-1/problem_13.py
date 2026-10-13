"""Logic-1: in_order_equal problem solution."""


def in_order_equal(a: int, b: int, c: int, equal_ok: bool) -> bool:
    """Return True if the three integers are in increasing order.

    Given three ints, a, b, c, return True if they are in strict
    increasing order. If equal_ok is True, equality is allowed.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.
        equal_ok: Whether equality between adjacent elements is allowed.

    Returns:
        True if the numbers are ordered correctly, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> in_order_equal(2, 5, 11, False)
        True
        >>> in_order_equal(5, 7, 6, False)
        False
        >>> in_order_equal(5, 5, 7, True)
        True
    """
    return a <= b <= c if equal_ok else a < b < c


if __name__ == "__main__":
    print(in_order_equal(2, 5, 11, False))
    print(in_order_equal(5, 7, 6, False))
    print(in_order_equal(5, 5, 7, True))