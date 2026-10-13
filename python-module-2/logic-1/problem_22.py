"""Logic-1: sum_limit problem solution."""


def sum_limit(a: int, b: int) -> int:
    """Return a + b if it has the same number of digits as a, else return a.

    Given 2 non-negative ints, a and b, return their sum, so long as the sum
    has the same number of digits as a. If the sum has more digits than a,
    just return a without b.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        a + b if digit counts match, otherwise a.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> sum_limit(2, 3)
        5
        >>> sum_limit(8, 3)
        8
        >>> sum_limit(8, 1)
        9
    """
    return a if len(str(a + b)) == len(str(a)) else a + b


if __name__ == "__main__":
    print(sum_limit(2, 3))
    print(sum_limit(8, 3))
    print(sum_limit(8, 1))