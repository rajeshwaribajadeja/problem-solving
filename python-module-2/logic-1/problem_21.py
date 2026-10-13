"""Logic-1: share_digit problem solution."""


def share_digit(a: int, b: int) -> bool:
    """Return True if there is a digit that appears in both two-digit numbers.

    Given two ints, each in the range 10..99, return True if there is a digit
    that appears in both numbers, such as the 2 in 12 and 23.

    Args:
        a: First integer in range 10..99.
        b: Second integer in range 10..99.

    Returns:
        True if any digit is shared between a and b, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> share_digit(12, 23)
        True
        >>> share_digit(12, 43)
        False
        >>> share_digit(12, 44)
        False
    """
    a_left, a_right = a // 10, a % 10
    b_left, b_right = b // 10, b % 10

    return (
        a_left == b_left
        or a_left == b_right
        or a_right == b_left
        or a_right == b_right
    )


if __name__ == "__main__":
    print(share_digit(12, 23))
    print(share_digit(12, 43))
    print(share_digit(12, 44))