"""Logic-2: lone_sum problem solution."""


def lone_sum(a: int, b: int, c: int) -> int:
    """Return the sum of 3 ints, omitting duplicate values from the sum.

    Given 3 int values, a, b, c, return their sum. However, if one of the
    values is the same as another of the values, it does not count towards
    the sum.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        The sum of the non-duplicated values.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> lone_sum(1, 2, 3)
        6
        >>> lone_sum(3, 2, 3)
        2
        >>> lone_sum(3, 3, 3)
        0
    """
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return total


if __name__ == "__main__":
    print(lone_sum(1, 2, 3))
    print(lone_sum(3, 2, 3))
    print(lone_sum(3, 3, 3))
