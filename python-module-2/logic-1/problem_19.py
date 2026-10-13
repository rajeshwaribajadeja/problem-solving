"""Logic-1: green_ticket problem solution."""


def green_ticket(a: int, b: int, c: int) -> int:
    """Return the green lottery ticket outcome: 20, 10, or 0.

    You have a green lottery ticket, with ints a, b, and c on it.
    If the numbers are all different, return 0.
    If all of the numbers are the same, return 20.
    If two of the numbers are the same, return 10.

    Args:
        a: First ticket number.
        b: Second ticket number.
        c: Third ticket number.

    Returns:
        20 if all three numbers match, 10 if two match, 0 if all different.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> green_ticket(1, 2, 3)
        0
        >>> green_ticket(2, 2, 2)
        20
        >>> green_ticket(1, 1, 2)
        10
    """
    return 20 if a == b == c else 10 if a == b or a == c or b == c else 0


if __name__ == "__main__":
    print(green_ticket(1, 2, 3))
    print(green_ticket(2, 2, 2))
    print(green_ticket(1, 1, 2))