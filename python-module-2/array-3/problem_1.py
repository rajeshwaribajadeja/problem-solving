"""Array-3: max_span problem solution."""


def max_span(nums: list) -> int:
    """Return the largest span between identical values in the array.

    Consider the leftmost and rightmost appearances of some value in an
    array. We'll say that the "span" is the number of elements between
    the two inclusive. A single value has a span of 1.

    Args:
        nums: A list of integers.

    Returns:
        The largest span found in the array, or 0 if the array is empty.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space for first occurrences map.

    Examples:
        >>> max_span([1, 2, 1, 1, 3])
        4
        >>> max_span([1, 4, 2, 1, 4, 1, 4])
        6
        >>> max_span([1, 4, 2, 1, 4, 4, 4])
        6
    """
    first = {}
    max_len = 0

    for i, x in enumerate(nums):
        first.setdefault(x, i)
        max_len = max(max_len, i - first[x] + 1)

    return max_len


if __name__ == "__main__":
    print(max_span([1, 2, 1, 1, 3]))
    print(max_span([1, 4, 2, 1, 4, 1, 4]))
    print(max_span([1, 4, 2, 1, 4, 4, 4]))