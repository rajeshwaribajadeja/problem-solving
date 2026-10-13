"""Logic-1: special_eleven problem solution."""


def special_eleven(n: int) -> bool:
    """Return True if the non-negative number is special.

    We'll say a number is special if it is a multiple of 11 or if it is
    one more than a multiple of 11.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is a multiple of 11 or 1 more than a multiple of 11, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> special_eleven(22)
        True
        >>> special_eleven(23)
        True
        >>> special_eleven(24)
        False
    """
    return n % 11 in (0, 1)


if __name__ == "__main__":
    print(special_eleven(22))
    print(special_eleven(23))
    print(special_eleven(24))