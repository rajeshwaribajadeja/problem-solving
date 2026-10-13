"""Logic-2: no_teen_sum problem solution."""


def fix_teen(n: int) -> int:
    """Adjust teen values in range 13..19 except 15 and 16 to 0.

    Args:
        n: The integer value.

    Returns:
        0 if n is a non-exempt teen, otherwise n.
    """
    return 0 if 13 <= n <= 19 and n not in (15, 16) else n


def no_teen_sum(a: int, b: int, c: int) -> int:
    """Return the sum of 3 integers with teen rules applied.

    Teens in the range 13..19 inclusive count as 0, except 15 and 16
    which are preserved.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        The adjusted sum.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> no_teen_sum(1, 2, 3)
        6
        >>> no_teen_sum(2, 13, 1)
        3
        >>> no_teen_sum(2, 1, 14)
        3
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


if __name__ == "__main__":
    print(no_teen_sum(1, 2, 3))
    print(no_teen_sum(2, 13, 1))
    print(no_teen_sum(2, 1, 14))