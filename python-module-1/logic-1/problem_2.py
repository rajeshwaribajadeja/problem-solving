"""Logic-1: date_fashion problem solution."""


def date_fashion(you: int, date: int) -> int:
    """Return 0 (no), 1 (maybe), or 2 (yes) for getting a restaurant table.

    If either you or your date is very stylish (8 or more), the result
    is 2 (yes). With the exception that if either has style of 2 or less,
    the result is 0 (no). Otherwise the result is 1 (maybe).

    Args:
        you: Stylishness of your clothes (0..10).
        date: Stylishness of your date's clothes (0..10).

    Returns:
        0 for no, 1 for maybe, or 2 for yes.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> date_fashion(5, 10)
        2
        >>> date_fashion(5, 2)
        0
        >>> date_fashion(5, 5)
        1
    """
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1


if __name__ == "__main__":
    print(date_fashion(5, 10))
    print(date_fashion(5, 2))
    print(date_fashion(5, 5))
