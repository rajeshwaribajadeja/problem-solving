"""Recursion-1: factorial problem solution."""


def factorial(n: int) -> int:
    """Return the factorial of n computed recursively.

    Args:
        n: A positive integer (n >= 1).

    Returns:
        The factorial of n.

    Complexity:
        Time Complexity: O(n) recursive calls.
        Space Complexity: O(n) auxiliary space for the call stack.

    Examples:
        >>> factorial(1)
        1
        >>> factorial(2)
        2
        >>> factorial(3)
        6
    """

    return 1 if n==1 else n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
