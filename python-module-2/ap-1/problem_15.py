"""AP-1: scores_special problem solution."""


def largest_special(scores: list) -> int:
    """Find the largest special score (multiple of 10) in an array.

    Args:
        scores: A list of non-negative integers.

    Returns:
        The largest multiple of 10 in scores, or 0 if none found.
    """
    largest = 0
    for score in scores:
        if score % 10 == 0 and score > largest:
            largest = score
    return largest


def scores_special(a: list, b: list) -> int:
    """Return the sum of the largest special score in a and in b.

    A "special" score is one which is a multiple of 10, such as 40 or 90.

    Args:
        a: First list of non-negative integers.
        b: Second list of non-negative integers.

    Returns:
        Sum of the largest special scores from both lists.

    Complexity:
        Time Complexity: O(len(a) + len(b))
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> scores_special([12, 10, 4], [2, 20, 30])
        40
        >>> scores_special([20, 10, 4], [2, 20, 10])
        40
        >>> scores_special([12, 11, 4], [2, 20, 31])
        20
    """
    return largest_special(a) + largest_special(b)


if __name__ == "__main__":
    print(scores_special([12, 10, 4], [2, 20, 30]))
    print(scores_special([20, 10, 4], [2, 20, 10]))
    print(scores_special([12, 11, 4], [2, 20, 31]))