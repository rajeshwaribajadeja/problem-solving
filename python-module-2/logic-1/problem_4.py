"""Logic-1: less20 problem solution."""


def less20(n: int) -> bool:
    """Return True if the number is 1 or 2 less than a multiple of 20.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is 1 or 2 less than a multiple of 20, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> less20(18)
        True
        >>> less20(19)
        True
        >>> less20(20)
        False
    """
    return n % 20 in (18, 19)


if __name__ == "__main__":
    print(less20(18))
    print(less20(19))
    print(less20(20))