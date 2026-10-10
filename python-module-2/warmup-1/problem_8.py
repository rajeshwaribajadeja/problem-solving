"""Warmup-1: has_teen problem solution."""


def has_teen(a: int, b: int, c: int) -> bool:
    """Return True if 1 or more of the given integers are in 13..19 inclusive.

    We'll say that a number is "teen" if it is in the range 13..19
    inclusive. Given 3 int values, return True if 1 or more of them are teen.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        True if any of a, b, or c are in 13..19, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> has_teen(13, 20, 10)
        True
        >>> has_teen(20, 19, 10)
        True
        >>> has_teen(20, 10, 21)
        False
    """
    return 13 <= a <= 19 or 13 <= b <= 19 or 13 <= c <= 19


if __name__ == "__main__":
    print(has_teen(13, 20, 10))
    print(has_teen(20, 19, 10))
    print(has_teen(20, 10, 21))