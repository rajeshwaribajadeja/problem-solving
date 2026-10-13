"""Logic-1: teen_sum problem solution."""


def teen_sum(a: int, b: int) -> int:
    """Return the sum of two integers, or 19 if either is a 'teen'.

    Given 2 ints, a and b, return their sum. However, "teen" values in the
    range 13..19 inclusive, are extra lucky. So if either value is a teen,
    just return 19.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        19 if either integer is in 13..19, otherwise a + b.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> teen_sum(3, 4)
        7
        >>> teen_sum(10, 13)
        19
        >>> teen_sum(13, 2)
        19
    """
    return 19 if 13 <= a <= 19 or 13 <= b <= 19 else a + b


if __name__ == "__main__":
    print(teen_sum(3, 4))
    print(teen_sum(10, 13))
    print(teen_sum(13, 2))