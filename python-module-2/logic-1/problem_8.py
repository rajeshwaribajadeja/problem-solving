"""Logic-1: tea_party problem solution."""


def tea_party(tea: int, candy: int) -> int:
    """Return the outcome of the party: 0=bad, 1=good, 2=great.

    A party is good (1) if both tea and candy are at least 5.
    If either tea or candy is at least double the amount of the other,
    the party is great (2).
    If either tea or candy is less than 5, the party is always bad (0).

    Args:
        tea: Amount of tea.
        candy: Amount of candy.

    Returns:
        0 for bad, 1 for good, or 2 for great party outcome.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> tea_party(6, 8)
        1
        >>> tea_party(3, 8)
        0
        >>> tea_party(20, 6)
        2
    """
    return (
        0 if min(tea, candy) < 5
        else 2 if max(tea, candy) >= 2 * min(tea, candy)
        else 1
    )


if __name__ == "__main__":
    print(tea_party(6, 8))
    print(tea_party(3, 8))
    print(tea_party(20, 6))