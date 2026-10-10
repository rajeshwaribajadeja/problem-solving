"""Warmup-1: or35 problem solution."""


def or35(n: int) -> bool:
    """Return True if a non-negative number is a multiple of 3 or 5.

    Given a non-negative number, return True if it is a multiple of 3
    or a multiple of 5.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is divisible by 3 or 5, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> or35(3)
        True
        >>> or35(10)
        True
        >>> or35(8)
        False
    """
    return n % 3 == 0 or n % 5 == 0


if __name__ == "__main__":
    print(or35(3))
    print(or35(10))
    print(or35(8))