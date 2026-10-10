"""Warmup-1: lone_teen problem solution."""


def lone_teen(a: int, b: int) -> bool:
    """Return True if one integer is teen (13..19) but not both.

    We'll say that a number is "teen" if it is in the range 13..19
    inclusive. Given 2 int values, return True if one or the other is
    teen, but not both.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if exactly one of a or b is in 13..19, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> lone_teen(13, 99)
        True
        >>> lone_teen(21, 19)
        True
        >>> lone_teen(13, 13)
        False
    """
    return (13 <= a <= 19) != (13 <= b <= 19)


if __name__ == "__main__":
    print(lone_teen(13, 99))
    print(lone_teen(21, 19))
    print(lone_teen(13, 13))