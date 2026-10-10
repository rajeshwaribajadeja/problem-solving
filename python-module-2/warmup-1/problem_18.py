"""Warmup-1: last_digit problem solution."""


def last_digit(a: int, b: int) -> bool:
    """Return True if two non-negative integers have the same last digit.

    Given two non-negative int values, return True if they have the same
    last digit, such as with 27 and 57.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        True if both numbers share the same last digit, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> last_digit(7, 17)
        True
        >>> last_digit(6, 17)
        False
        >>> last_digit(3, 113)
        True
    """
    return a % 10 == b % 10


if __name__ == "__main__":
    print(last_digit(7, 17))
    print(last_digit(6, 17))
    print(last_digit(3, 113))