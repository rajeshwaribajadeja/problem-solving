"""AP-1: sum_heights_2 problem solution."""


def sum_heights_2(heights: list, start: int, end: int) -> int:
    """Return sum of height changes where increases in height count double.

    Given start/end indexes into the array, return the sum of changes,
    counting increases in altitude with double weight.

    Args:
        heights: A list of integers representing trail altitudes.
        start: Starting index (inclusive).
        end: Ending index (inclusive).

    Returns:
        The weighted sum of height changes.

    Complexity:
        Time Complexity: O(end - start)
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum_heights_2([5, 3, 6, 7, 2], 2, 4)
        7
        >>> sum_heights_2([5, 3, 6, 7, 2], 0, 1)
        2
        >>> sum_heights_2([5, 3, 6, 7, 2], 0, 4)
        15
    """
    total = 0
    for i in range(start, end):
        diff = heights[i + 1] - heights[i]
        if diff > 0:
            total += diff * 2
        else:
            total += -diff
    return total


if __name__ == "__main__":
    print(sum_heights_2([5, 3, 6, 7, 2], 2, 4))
    print(sum_heights_2([5, 3, 6, 7, 2], 0, 1))
    print(sum_heights_2([5, 3, 6, 7, 2], 0, 4))