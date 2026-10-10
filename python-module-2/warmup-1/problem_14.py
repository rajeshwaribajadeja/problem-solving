"""Warmup-1: close10 problem solution."""


def close10(a: int, b: int) -> int:
    """Return the integer nearest to 10, or 0 in the event of a tie.

    Given 2 int values, return whichever value is nearest to the value
    10, or return 0 in the event of a tie.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The integer closest to 10, or 0 if they are equidistant.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> close10(8, 13)
        8
        >>> close10(13, 8)
        8
        >>> close10(13, 7)
        0
    """
    return 0 if abs(10 - a) == abs(10 - b) else a if abs(10 - a) < abs(10 - b) else b


if __name__ == "__main__":
    print(close10(8, 13))
    print(close10(13, 8))
    print(close10(13, 7))