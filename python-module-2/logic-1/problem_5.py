"""Logic-1: near_ten problem solution."""


def near_ten(num: int) -> bool:
    """Return True if the number is within 2 of a multiple of 10.

    Args:
        num: A non-negative integer.

    Returns:
        True if num is within 2 of a multiple of 10, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> near_ten(12)
        True
        >>> near_ten(17)
        False
        >>> near_ten(19)
        True
    """
    return num % 10 <= 2 or num % 10 >= 8    


if __name__ == "__main__":
    print(near_ten(12))
    print(near_ten(17))
    print(near_ten(19))