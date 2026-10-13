"""AP-1: has_one problem solution."""


def has_one(n: int) -> bool:
    """Return True if positive integer n contains the digit 1.

    Args:
        n: A positive integer.

    Returns:
        True if the digit 1 is present, False otherwise.

    Complexity:
        Time Complexity: O(log10(n)) where n is the given integer (or O(d)
            where d is the number of digits in n).
        Space Complexity: O(log10(n)) auxiliary space due to the string
            conversion of n.

    Examples:
        >>> has_one(10)
        True
        >>> has_one(22)
        False
        >>> has_one(220)
        False
    """
    return '1' in str(n)


if __name__ == "__main__":
    print(has_one(10))
    print(has_one(22))
    print(has_one(220))