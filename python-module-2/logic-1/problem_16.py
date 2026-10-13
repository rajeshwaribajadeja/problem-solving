"""Logic-1: without_doubles problem solution."""


def without_doubles(die1: int, die2: int, no_doubles: bool) -> int:
    """Return the sum of two 6-sided dice rolls, adjusting for doubles if requested.

    If no_doubles is True and both dice show the same value, increment one
    die to the next value, wrapping around to 1 if its value was 6.

    Args:
        die1: First die roll (1-6).
        die2: Second die roll (1-6).
        no_doubles: Whether doubles should be disallowed and adjusted.

    Returns:
        The sum of the dice rolls after applying the rule.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> without_doubles(2, 3, True)
        5
        >>> without_doubles(3, 3, True)
        7
        >>> without_doubles(3, 3, False)
        6
    """
    return die1 + (die2 % 6 + 1 if no_doubles and die1 == die2 else die2)


if __name__ == "__main__":
    print(without_doubles(2, 3, True))
    print(without_doubles(3, 3, True))
    print(without_doubles(3, 3, False))