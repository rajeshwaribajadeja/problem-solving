"""Logic-1: in1to10 problem solution."""


def in1to10(n: int, outside_mode: bool) -> bool:
    """Return True if n is in 1..10 or outside the range in outside_mode.

    Given a number n, return True if n is in the range 1..10, inclusive.
    Unless outside_mode is True, in which case return True if the number
    is less or equal to 1, or greater or equal to 10.

    Args:
        n: The integer to test.
        outside_mode: Whether outside range mode is enabled.

    Returns:
        True if n satisfies the range conditions, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> in1to10(5, False)
        True
        >>> in1to10(11, False)
        False
        >>> in1to10(11, True)
        True
    """
    return (n >= 1 and n <= 10) or (outside_mode and (n <= 1 or n >= 10))


if __name__ == "__main__":
    print(in1to10(5, False))
    print(in1to10(11, False))
    print(in1to10(11, True))
