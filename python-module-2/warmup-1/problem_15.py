"""Warmup-1: in3050 problem solution."""


def in3050(a: int, b: int) -> bool:
    """Return True if both numbers are in 30..40 or both in 40..50.

    Given 2 int values, return True if they are both in the range
    30..40 inclusive, or they are both in the range 40..50 inclusive.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if both numbers fall in either [30, 40] or [40, 50], False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> in3050(30, 31)
        True
        >>> in3050(30, 41)
        False
        >>> in3050(40, 50)
        True
    """
    return (30 <= a <= 40 and 30 <= b <= 40) or (40 <= a <= 50 and 40 <= b <= 50)


if __name__ == "__main__":
    print(in3050(30, 31))
    print(in3050(30, 41))
    print(in3050(40, 50))