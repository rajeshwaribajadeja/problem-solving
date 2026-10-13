"""AP-1: scores_increasing problem solution."""


def scores_increasing(scores: list) -> bool:
    """Return True if each score is equal or greater than the one before.

    Given an array of scores, return True if each score is equal or greater
    than the one before. The array will be length 2 or more.

    Args:
        scores: A list of integers (length >= 2).

    Returns:
        True if scores are in non-decreasing order, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> scores_increasing([1, 3, 4])
        True
        >>> scores_increasing([1, 3, 2])
        False
        >>> scores_increasing([1, 1, 4])
        True
    """
    return all(scores[i] <= scores[i + 1] for i in range(len(scores) - 1))


if __name__ == "__main__":
    print(scores_increasing([1, 3, 4]))
    print(scores_increasing([1, 3, 2]))
    print(scores_increasing([1, 1, 4]))