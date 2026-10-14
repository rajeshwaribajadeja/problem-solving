"""Recursion-1: bunny_ears_2 problem solution."""


def bunny_ears_2(n: int) -> int:
    """Return total ears for line of bunnies (even have 3, odd have 2).

    Args:
        n: Number of bunnies (non-negative integer).

    Returns:
        Total number of ears.

    Complexity:
        Time Complexity: O(n) recursive calls.
        Space Complexity: O(n) auxiliary space for the call stack.

    Examples:
        >>> bunny_ears_2(0)
        0
        >>> bunny_ears_2(1)
        2
        >>> bunny_ears_2(2)
        5
    """

    return (
        0 if n == 0
        else 3 + bunny_ears_2(n - 1) if n % 2 == 0
        else 2 + bunny_ears_2(n - 1)
    )


if __name__ == "__main__":
    print(bunny_ears_2(0))
    print(bunny_ears_2(1))
    print(bunny_ears_2(2))
