"""Recursion-1: count_7 problem solution."""


def count_7(n: int) -> int:
    """Return the count of occurrences of digit 7 in non-negative int n.

    Args:
        n: Non-negative integer.

    Returns:
        Number of times digit 7 appears in n.

    Complexity:
        Time Complexity: O(log10(n)) recursive calls.
        Space Complexity: O(log10(n)) auxiliary space for call stack.

    Examples:
        >>> count_7(717)
        2
        >>> count_7(7)
        1
        >>> count_7(123)
        0
    """

    return 0 if n==0 else 1 + count_7(n//10) if n % 10 == 7 else count_7(n // 10)


if __name__ == "__main__":
    print(count_7(717))
    print(count_7(7))
    print(count_7(123))
