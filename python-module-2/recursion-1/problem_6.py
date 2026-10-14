"""Recursion-1: sum_digits problem solution."""


def sum_digits(n: int) -> int:
    """Return the sum of the digits of non-negative integer n.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of all digits in n.

    Complexity:
        Time Complexity: O(log10(n)) recursive calls.
        Space Complexity: O(log10(n)) auxiliary space for call stack.

    Examples:
        >>> sum_digits(126)
        9
        >>> sum_digits(49)
        13
        >>> sum_digits(12)
        3
    """

    return 0 if n==0 else (n % 10) + sum_digits(n // 10)


if __name__ == "__main__":
    print(sum_digits(126))
    print(sum_digits(49))
    print(sum_digits(12))
