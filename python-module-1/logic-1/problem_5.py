"""Logic-1: sorta_sum problem solution."""


def sorta_sum(a: int, b: int) -> int:
    """Return the sum of two ints, returning 20 if the sum is in 10..19.

    Given 2 ints, a and b, return their sum. However, sums in the range
    10..19 inclusive, are forbidden, so in that case just return 20.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        20 if the sum falls in 10..19 inclusive, otherwise a + b.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> sorta_sum(3, 4)
        7
        >>> sorta_sum(9, 4)
        20
        >>> sorta_sum(10, 11)
        21
    """
    return 20 if 10 <= a + b <= 19 else a + b


if __name__ == "__main__":
    print(sorta_sum(3, 4))
    print(sorta_sum(9, 4))
    print(sorta_sum(10, 11))
