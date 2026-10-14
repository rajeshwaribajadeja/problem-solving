"""Logic-1: red_ticket problem solution."""


def red_ticket(a: int, b: int, c: int) -> int:
    """Return the red lottery ticket outcome: 10, 5, 1, or 0.

    You have a red lottery ticket showing ints a, b, and c, each of
    which is 0, 1, or 2.
    If they are all 2, the result is 10.
    Otherwise if they are all the same, the result is 5.
    Otherwise, if both b and c are different from a, the result is 1.
    Otherwise the result is 0.

    Args:
        a: First ticket number (0, 1, or 2).
        b: Second ticket number (0, 1, or 2).
        c: Third ticket number (0, 1, or 2).

    Returns:
        The lottery result value (10, 5, 1, or 0).

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> red_ticket(2, 2, 2)
        10
        >>> red_ticket(2, 2, 1)
        0
        >>> red_ticket(0, 0, 0)
        5
    """
    return (
        10 if (a, b, c) == (2, 2, 2)
        else 5 if len({a, b, c}) == 1
        else 1 if a not in (b, c)
        else 0
    )


if __name__ == "__main__":
    print(red_ticket(2, 2, 2))
    print(red_ticket(2, 2, 1))
    print(red_ticket(0, 0, 0))