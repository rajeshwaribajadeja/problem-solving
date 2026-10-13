"""Logic-1: love6 problem solution."""


def love6(a: int, b: int) -> bool:
    """Return True if either number is 6, or their sum or difference is 6.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if a=6, b=6, a+b=6, or abs(a-b)=6, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> love6(6, 4)
        True
        >>> love6(4, 5)
        False
        >>> love6(1, 5)
        True
    """
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6


if __name__ == "__main__":
    print(love6(6, 4))
    print(love6(4, 5))
    print(love6(1, 5))
