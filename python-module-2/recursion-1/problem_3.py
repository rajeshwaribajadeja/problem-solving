"""Recursion-1: fibonacci problem solution."""


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number recursively.

    The sequence starts with 0 at n=0 and 1 at n=1.

    Args:
        n: Non-negative integer index.

    Returns:
        The nth Fibonacci number.

    Complexity:
        Time Complexity: O(2^n) without memoization.
        Space Complexity: O(n) auxiliary space for the call stack.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
    """

    return 0 if n==0 else 1 if n==1 else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
