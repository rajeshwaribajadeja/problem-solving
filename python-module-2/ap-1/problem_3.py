"""AP-1: scores_clump problem solution."""


def scores_clump(scores: list) -> bool:
    """Return True if 3 adjacent scores differ by at most 2.

    Given an array of scores sorted in increasing order, return True
    if the array contains 3 adjacent scores that differ from each
    other by at most 2.

    Args:
        scores: A list of integers sorted in non-decreasing order.

    Returns:
        True if 3 adjacent scores differ by at most 2, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> scores_clump([3, 4, 5])
        True
        >>> scores_clump([3, 4, 6])
        False
        >>> scores_clump([1, 3, 5, 5])  
        True
    """
    return any(scores[i + 2] - scores[i] <= 2 for i in range(len(scores) - 2))


if __name__ == "__main__":
    print(scores_clump([3, 4, 5]))
    print(scores_clump([3, 4, 6]))
    print(scores_clump([1, 3, 5, 5]))