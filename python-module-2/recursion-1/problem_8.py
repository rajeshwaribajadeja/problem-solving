"""Recursion-1: count_8 problem solution."""


def count_8(n: int) -> int:
    """Return count of 8s, with an 8 next to an 8 on the left counting double.

    Args:
        n: Non-negative integer.

    Returns:
        Weighted count of digit 8.

    Complexity:
        Time Complexity: O(log10(n)) recursive calls.
        Space Complexity: O(log10(n)) auxiliary space for call stack.

    Examples:
        >>> count_8(8)
        1
        >>> count_8(818)
        2
        >>> count_8(8818)
        4
    """
    if n == 0:
        return 0
    if n % 10 == 8:
        if (n // 10) % 10 == 8:
            return 2 + count_8(n // 10)
        return 1 + count_8(n // 10)
    return count_8(n // 10)


if __name__ == "__main__":
    print(count_8(8))
    print(count_8(818))
    print(count_8(8818))
