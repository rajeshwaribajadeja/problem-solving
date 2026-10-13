"""Logic-1: less_by_10 problem solution."""


def less_by_10(a: int, b: int, c: int) -> bool:
    """Return True if one of the integers is 10 or more less than another.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        True if the difference between any pair is at least 10, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> less_by_10(1, 7, 11)
        True
        >>> less_by_10(1, 7, 10)
        False
        >>> less_by_10(11, 1, 7)
        True
    """
    return abs(a - b) >= 10 or abs(a - c) >= 10 or abs(b - c) >= 10


if __name__ == "__main__":
    print(less_by_10(1, 7, 11))
    print(less_by_10(1, 7, 10))
    print(less_by_10(11, 1, 7))