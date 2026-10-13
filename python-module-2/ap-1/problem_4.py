"""AP-1: scores_average problem solution."""


def average(scores: list, start: int, end: int) -> int:
    """Compute the integer average of elements between start and end indexes.

    Args:
        scores: A list of integers.
        start: Starting index (inclusive).
        end: Ending index (exclusive).

    Returns:
        The integer average of the slice.
    """
    total = sum(scores[start:end])
    return total // (end - start)


def scores_average(scores: list) -> int:
    """Return the larger of the average of the first and second halves.

    Given an array of scores, compute the integer average of the first half
    and the second half, and return whichever is larger.

    Args:
        scores: A list of integers (even length >= 2).

    Returns:
        The larger average of the two halves.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> scores_average([2, 2, 4, 4])
        4
        >>> scores_average([4, 4, 4, 2, 2, 2])
        4
        >>> scores_average([3, 4, 5, 1, 2, 3])
        4
    """
    mid = len(scores) // 2
    return max(average(scores, 0, mid), average(scores, mid, len(scores)))


if __name__ == "__main__":
    print(scores_average([2, 2, 4, 4]))
    print(scores_average([4, 4, 4, 2, 2, 2]))
    print(scores_average([3, 4, 5, 1, 2, 3]))