"""Logic-2: round_sum problem solution."""


def round10(num: int) -> int:
    """Round an integer to the nearest multiple of 10.

    Rounds up if the rightmost digit is 5 or more, otherwise rounds down.

    Args:
        num: The integer to round.

    Returns:
        The rounded multiple of 10.
    """
    return num + (10 - num % 10) if num % 10 >= 5 else num - num % 10


def round_sum(a: int, b: int, c: int) -> int:
    """Return sum of 3 numbers each rounded to nearest multiple of 10.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        The sum of the three rounded values.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> round_sum(16, 17, 18)
        60
        >>> round_sum(12, 13, 14)
        30
        >>> round_sum(6, 4, 4)
        10
    """
    return round10(a) + round10(b) + round10(c)


if __name__ == "__main__":
    print(round_sum(16, 17, 18))
    print(round_sum(12, 13, 14))
    print(round_sum(6, 4, 4))
