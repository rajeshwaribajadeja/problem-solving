"""Warmup-1: in1020 problem solution."""


def in1020(a: int, b: int) -> bool:
    """Check if either integer is in the range 10..20 inclusive.

    Given 2 int values, return True if either of them is in the range
    10..20 inclusive.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if either a or b is between 10 and 20, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> in1020(12, 99)
        True
        >>> in1020(21, 12)
        True
        >>> in1020(8, 99)
        False
    """
    return 10 <= a <= 20 or 10 <= b <= 20


if __name__ == "__main__":
    print(in1020(12, 99))
    print(in1020(21, 12))
    print(in1020(8, 99))