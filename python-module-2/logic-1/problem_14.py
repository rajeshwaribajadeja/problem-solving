"""Logic-1: last_digit problem solution."""


def last_digit(a: int, b: int, c: int) -> bool:
    """Return True if two or more integers have the same rightmost digit.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.
        c: Third non-negative integer.

    Returns:
        True if at least two integers share the same last digit,
        False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> last_digit(23, 19, 13)
        True
        >>> last_digit(23, 19, 12)
        False
        >>> last_digit(23, 19, 3)
        True
    """
    da = a % 10
    db = b % 10
    dc = c % 10
    return da == db or da == dc or db == dc


if __name__ == "__main__":
    print(last_digit(23, 19, 13))
    print(last_digit(23, 19, 12))
    print(last_digit(23, 19, 3))