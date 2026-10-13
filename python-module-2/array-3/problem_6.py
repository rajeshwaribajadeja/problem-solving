"""Array-3: square_up problem solution."""


def square_up(n: int) -> list:
    """Create an array of length n*n following the square-up pattern.

    Given n>=0, create an array length n*n with the pattern shown
    for n=3: [0, 0, 1,  0, 2, 1,  3, 2, 1].

    Args:
        n: A non-negative integer.

    Returns:
        A list of length n*n matching the pattern.

    Complexity:
        Time Complexity: O(n^2) where n is the given integer.
        Space Complexity: O(n^2) to hold the output list.

    Examples:
        >>> square_up(3)
        [0, 0, 1, 0, 2, 1, 3, 2, 1]
        >>> square_up(2)
        [0, 1, 2, 1]
        >>> square_up(4)
        [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
    """
    result = []

    for i in range(1, n + 1):
        result.extend([0] * (n - i))
        result.extend(range(i, 0, -1))

    return result


if __name__ == "__main__":
    print(square_up(3))
    print(square_up(2))
    print(square_up(4))
