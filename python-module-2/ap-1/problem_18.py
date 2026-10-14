"""AP-1: big_heights problem solution."""


def big_heights(heights: list, start: int, end: int) -> int:
    """Return the number of big steps (height change of 5 or more).

    Given start/end indexes into the array, return the number of "big"
    steps for a walk starting at start and ending at end. A step is big
    if it is 5 or more up or down.

    Args:
        heights: A list of integers representing trail altitudes.
        start: Starting index (inclusive).
        end: Ending index (inclusive).

    Returns:
        The count of height changes of 5 or more.

    Complexity:
        Time Complexity: O(end - start)
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> big_heights([5, 3, 6, 7, 2], 2, 4)
        1
        >>> big_heights([5, 3, 6, 7, 2], 0, 1)
        0
        >>> big_heights([5, 3, 6, 7, 2], 0, 4)
        1
    """
    count = 0
    for i in range(start, end):
        if abs(heights[i + 1] - heights[i]) >= 5:
            count += 1
    return count


if __name__ == "__main__":
    print(big_heights([5, 3, 6, 7, 2], 2, 4))
    print(big_heights([5, 3, 6, 7, 2], 0, 1))
    print(big_heights([5, 3, 6, 7, 2], 0, 4))