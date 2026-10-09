"""Warmup-1: makes10 problem solution."""


def makes10(a: int, b: int) -> bool:
    """Determine if either integer is 10 or if their sum equals 10.

    Given 2 ints, a and b, return True if one of them is 10 or if their
    sum is 10.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if either number is 10 or their sum is 10, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> makes10(9, 10)
        True
        >>> makes10(9, 9)
        False
        >>> makes10(1, 9)
        True
    """
    return a == 10 or b == 10 or a + b == 10


if __name__ == "__main__":
    print(makes10(9, 10))
    print(makes10(9, 9))
    print(makes10(1, 9))