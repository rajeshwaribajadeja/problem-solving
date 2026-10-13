"""Logic-1: two_as_one problem solution."""


def two_as_one(a: int, b: int, c: int) -> bool:
    """Return True if it is possible to add two of the ints to get the third.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        True if the sum of any two numbers equals the third, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> two_as_one(1, 2, 3)
        True
        >>> two_as_one(3, 1, 2)
        True
        >>> two_as_one(3, 2, 2)
        False
    """
    return a + b == c or a + c == b or b + c == a


if __name__ == "__main__":
    print(two_as_one(1, 2, 3))
    print(two_as_one(3, 1, 2))
    print(two_as_one(3, 2, 2))