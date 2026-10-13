"""AP-1: scores_100 problem solution."""


def scores_100(scores: list) -> bool:
    """Return True if there are adjacent scores of 100 in the array.

    Given an array of scores, return True if there are scores of 100
    next to each other in the array. The array length will be at least 2.

    Args:
        scores: A list of integers (length >= 2).

    Returns:
        True if two adjacent scores are both 100, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> scores_100([1, 100, 100])
        True
        >>> scores_100([1, 100, 99, 100])
        False
        >>> scores_100([100, 1, 100, 100])
        True
    """
    return any(
        scores[i] == 100 and scores[i + 1] == 100
        for i in range(len(scores) - 1)
    )


if __name__ == "__main__":
    print(scores_100([1, 100, 100]))
    print(scores_100([1, 100, 99, 100]))
    print(scores_100([100, 1, 100, 100]))