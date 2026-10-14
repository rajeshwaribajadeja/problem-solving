"""AP-1: sum_heights problem solution."""


def sum_heights(heights: list, start: int, end: int) -> int:
    """Return the sum of the absolute altitude changes along a walking trail.

    Given start/end indexes into the array, return the sum of the changes
    for a walk beginning at the start index and ending at the end index.

    Args:
        heights: A list of integers representing trail altitudes.
        start: Starting index (inclusive).
        end: Ending index (inclusive).

    Returns:
        The sum of absolute height changes between start and end.

    Complexity:
        Time Complexity: O(end - start)
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum_heights([5, 3, 6, 7, 2], 2, 4)
        6
        >>> sum_heights([5, 3, 6, 7, 2], 0, 1)
        2
        >>> sum_heights([5, 3, 6, 7, 2], 0, 4)
        11
    """
    total = 0
    for i in range(start, end):
        total += abs(heights[i + 1] - heights[i])
    return total


if __name__ == "__main__":
    print(sum_heights([5, 3, 6, 7, 2], 2, 4))
    print(sum_heights([5, 3, 6, 7, 2], 0, 1))
    print(sum_heights([5, 3, 6, 7, 2], 0, 4))