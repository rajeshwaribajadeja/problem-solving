"""Logic-2: blackjack problem solution."""


def blackjack(a: int, b: int) -> int:
    """Return whichever value is nearest to 21 without going over.

    Given 2 int values greater than 0, return whichever value is nearest to 21
    without going over. Return 0 if they both go over.

    Args:
        a: The first positive integer.
        b: The second positive integer.

    Returns:
        The value closest to 21 without going over, or 0 if both exceed 21.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> blackjack(19, 21)
        21
        >>> blackjack(21, 19)
        21
        >>> blackjack(19, 22)
        19
    """
    return max((x for x in (a, b) if x <= 21), default=0)


if __name__ == "__main__":
    print(blackjack(19, 21))
    print(blackjack(21, 19))
    print(blackjack(19, 22))