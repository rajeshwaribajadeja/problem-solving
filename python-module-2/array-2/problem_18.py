"""Array-2: fizz_array_3 problem solution."""


def fizz_array_3(start: int, end: int) -> list:
    """Return array containing sequence of integers from start up to end.

    Given start and end numbers, return a new array containing the
    sequence of integers from start up to but not including end.

    Args:
        start: Starting integer (inclusive).
        end: Ending integer (exclusive).

    Returns:
        A list of integers from start up to end - 1.

    Complexity:
        Time Complexity: O(end - start)
        Space Complexity: O(end - start)

    Examples:
        >>> fizz_array_3(5, 10)
        [5, 6, 7, 8, 9]
        >>> fizz_array_3(11, 18)
        [11, 12, 13, 14, 15, 16, 17]
        >>> fizz_array_3(1, 3)
        [1, 2]
    """
    return list(range(start, end))


if __name__ == "__main__":
    print(fizz_array_3(5, 10))
    print(fizz_array_3(11, 18))
    print(fizz_array_3(1, 3))
