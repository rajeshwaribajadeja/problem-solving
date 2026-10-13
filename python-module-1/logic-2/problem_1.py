"""Logic-2: make_bricks problem solution."""


def make_bricks(small: int, big: int, goal: int) -> bool:
    """Return True if goal length can be reached using given bricks.

    We want to make a row of bricks that is goal inches long. We have a
    number of small bricks (1 inch each) and big bricks (5 inches each).
    Return True if it is possible to make the goal by choosing from the
    given bricks.

    Args:
        small: Number of 1-inch small bricks.
        big: Number of 5-inch big bricks.
        goal: The target length in inches.

    Returns:
        True if the goal can be reached, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> make_bricks(3, 1, 8)
        True
        >>> make_bricks(3, 1, 9)
        False
        >>> make_bricks(3, 2, 10)
        True
    """
    rem = goal - min(big, goal // 5) * 5
    return rem <= small


if __name__ == "__main__":
    print(make_bricks(3, 1, 8))
    print(make_bricks(3, 1, 9))
    print(make_bricks(3, 2, 10))
