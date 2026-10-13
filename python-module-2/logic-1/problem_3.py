"""Logic-1: old35 problem solution."""


def old35(n: int) -> bool:
    """Return True if the number is a multiple of 3 or 5, but not both.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is divisible by 3 or 5 (exclusive), False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> old35(3)
        True
        >>> old35(10)
        True
        >>> old35(15)
        False
    """
    return (n % 3 == 0) ^ (n % 5 == 0)


if __name__ == "__main__":
    print(old35(3))
    print(old35(10))
    print(old35(15))