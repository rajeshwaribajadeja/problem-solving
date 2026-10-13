"""Logic-1: blue_ticket problem solution."""


def blue_ticket(a: int, b: int, c: int) -> int:
    """Return the blue lottery ticket outcome: 10, 5, or 0.

    You have a blue lottery ticket, with ints a, b, and c on it.
    If any pair sums to exactly 10, return 10.
    Otherwise, if the ab sum is exactly 10 more than either
    the bc or ac sums, return 5.
    Otherwise, return 0.

    Args:
        a: First ticket number.
        b: Second ticket number.
        c: Third ticket number.

    Returns:
        10, 5, or 0 depending on the pair sums.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> blue_ticket(9, 1, 0)
        10
        >>> blue_ticket(9, 2, 0)
        0
        >>> blue_ticket(6, 1, 4)
        10
    """
    ab = a + b
    bc = b + c
    ac = a + c

    if ab == 10 or bc == 10 or ac == 10:
        return 10
    if ab == bc + 10 or ab == ac + 10:
        return 5
    return 0


if __name__ == "__main__":
    print(blue_ticket(9, 1, 0))
    print(blue_ticket(9, 2, 0))
    print(blue_ticket(6, 1, 4))