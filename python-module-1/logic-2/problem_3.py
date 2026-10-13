"""Logic-2: lucky_sum problem solution."""


def lucky_sum(a: int, b: int, c: int) -> int:
    """Return sum of 3 ints, ignoring 13 and values to the right of 13.

    Given 3 int values, a, b, c, return their sum. However, if any of the
    values is 13 then it does not count towards the sum, and values to its
    right do not count.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        The sum of values appearing before any 13.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> lucky_sum(1, 2, 3)
        6
        >>> lucky_sum(1, 2, 13)
        3
        >>> lucky_sum(1, 13, 3)
        1
    """
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c


if __name__ == "__main__":
    print(lucky_sum(1, 2, 3))
    print(lucky_sum(1, 2, 13))
    print(lucky_sum(1, 13, 3))
