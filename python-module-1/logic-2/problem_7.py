"""Logic-2: make_chocolate problem solution."""


def make_chocolate(small: int, big: int, goal: int) -> int:
    """Return the number of small bars needed to reach the goal, or -1.

    We want to make a package of goal kilos of chocolate. We have small bars
    (1 kilo each) and big bars (5 kilos each). Return the number of small bars
    to use, assuming we always use big bars before small bars. Return -1 if
    it cannot be done.

    Args:
        small: Number of available 1-kilo bars.
        big: Number of available 5-kilo bars.
        goal: Target weight in kilos.

    Returns:
        Number of small bars used, or -1 if impossible.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> make_chocolate(4, 1, 9)
        4
        >>> make_chocolate(4, 1, 10)
        -1
        >>> make_chocolate(4, 1, 7)
        2
    """
    rem = goal - min(big, goal // 5) * 5
    return rem if rem <= small else -1


if __name__ == "__main__":
    print(make_chocolate(4, 1, 9))
    print(make_chocolate(4, 1, 10))
    print(make_chocolate(4, 1, 7))
