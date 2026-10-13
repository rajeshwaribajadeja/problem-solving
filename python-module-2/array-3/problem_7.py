"""Array-3: series_up problem solution."""


def series_up(n: int) -> list:
    """Create an array with the pattern {1, 1, 2, 1, 2, 3, ... 1..n}.

    Given n>=0, create an array with the pattern {1,  1, 2,  1, 2, 3,
    ... 1, 2, 3 .. n}. Note that the length of the array will be n*(n + 1)/2.

    Args:
        n: A non-negative integer.

    Returns:
        A list of integers following the series-up pattern.

    Complexity:
        Time Complexity: O(n^2) where n is the given integer.
        Space Complexity: O(n^2) to hold the output list.

    Examples:
        >>> series_up(3)
        [1, 1, 2, 1, 2, 3]
        >>> series_up(4)
        [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
        >>> series_up(2)
        [1, 1, 2]
    """
    return [j for i in range(1, n + 1) for j in range(1, i + 1)]


if __name__ == "__main__":
    print(series_up(3))
    print(series_up(4))
    print(series_up(2))
