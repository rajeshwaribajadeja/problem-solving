"""Recursion-1: bunny_ears problem solution."""


def bunny_ears(n: int) -> int:
    """Return the total number of ears for n bunnies recursively.

    Args:
        n: Number of bunnies (non-negative integer).

    Returns:
        Total number of ears (2 per bunny).

    Complexity:
        Time Complexity: O(n) recursive calls.
        Space Complexity: O(n) auxiliary space for the call stack.

    Examples:
        >>> bunny_ears(0)
        0
        >>> bunny_ears(1)
        2
        >>> bunny_ears(2)
        4
    """

    return 0 if n == 0 else 2 + bunny_ears(n - 1)


if __name__ == "__main__":
    print(bunny_ears(0))
    print(bunny_ears(1))
    print(bunny_ears(2))
